"""
Score Network for NPSE/TSNPSE.

Implements the conditional score network s_psi(theta_t, x, t) that approximates
the score of the perturbed posterior ∇_θ log p_t(θ_t | x).

Architecture (Appendix E.3.2):
  - Independent MLP embeddings for theta_t, x, and t (sinusoidal)
  - Concatenated embeddings fed into final MLP score network
  - All MLPs: 3 layers, 256 hidden units, SiLU activations
  - theta_t embedding output: max(30, 4*d)
  - x embedding output: max(30, 4*p)
  - t sinusoidal embedding: 64 dimensions
  - Score network output: d (same as theta_t dimension)
"""

import torch
import torch.nn as nn
import math
from typing import Tuple


def build_mlp(input_dim: int, hidden_dim: int, output_dim: int, n_layers: int = 3) -> nn.Sequential:
    """Build a fully connected MLP with SiLU activations.

    Args:
        input_dim: Input feature dimension.
        hidden_dim: Number of hidden units per layer (256 for all networks).
        output_dim: Output feature dimension.
        n_layers: Number of fully connected layers (3 for all networks).

    Returns:
        nn.Sequential MLP with SiLU activations between layers.
    """
    layers = []
    in_dim = input_dim
    for i in range(n_layers - 1):
        layers.append(nn.Linear(in_dim, hidden_dim))
        layers.append(nn.SiLU())
        in_dim = hidden_dim
    layers.append(nn.Linear(in_dim, output_dim))
    return nn.Sequential(*layers)


def sinusoidal_embedding(t: torch.Tensor, embed_dim: int = 64) -> torch.Tensor:
    """Compute sinusoidal time embedding (Eq. 138 in Appendix E.3.2).

    Formula:
        (t_emb)_i = sin(t / 10000^{(i-1)/31})  if i <= 32
        (t_emb)_i = cos(t / 10000^{((i-32)-1)/31})  if i > 32

    Args:
        t: Time values, shape (batch_size,) or (batch_size, 1), in range (0, 1].
        embed_dim: Output embedding dimension (64 in paper).

    Returns:
        Sinusoidal embeddings, shape (batch_size, embed_dim).
    """
    if t.dim() == 1:
        t = t.unsqueeze(-1)  # (B, 1)

    half_dim = embed_dim // 2  # 32
    # indices i from 1 to 32 (for sin part)
    i_sin = torch.arange(1, half_dim + 1, device=t.device, dtype=t.dtype)
    # indices i from 33 to 64 (for cos part), mapped to (i-32)-1 = 0,...,31
    i_cos = torch.arange(0, half_dim, device=t.device, dtype=t.dtype)

    # sin part: sin(t / 10000^{(i-1)/31})
    sin_freqs = torch.pow(10000.0, (i_sin - 1) / 31.0)  # (half_dim,)
    sin_emb = torch.sin(t / sin_freqs.unsqueeze(0))  # (B, half_dim)

    # cos part: cos(t / 10000^{(i_cos)/31})
    cos_freqs = torch.pow(10000.0, i_cos / 31.0)  # (half_dim,)
    cos_emb = torch.cos(t / cos_freqs.unsqueeze(0))  # (B, half_dim)

    return torch.cat([sin_emb, cos_emb], dim=-1)  # (B, 64)


class ScoreNetwork(nn.Module):
    """Conditional score network for NPSE.

    Approximates s_psi(theta_t, x, t) ≈ ∇_θ log p_t(θ_t | x).

    Args:
        theta_dim: Dimension d of parameter space.
        x_dim: Dimension p of observation space.
        hidden_dim: Width of all MLP layers (256 in paper).
        t_embed_dim: Dimension of sinusoidal time embedding (64 in paper).
        theta_embed_dim: Output dim of theta embedding = max(30, 4*theta_dim).
        x_embed_dim: Output dim of x embedding = max(30, 4*x_dim).
    """

    def __init__(
        self,
        theta_dim: int,
        x_dim: int,
        hidden_dim: int = 256,
        t_embed_dim: int = 64,
    ):
        super().__init__()
        self.theta_dim = theta_dim
        self.x_dim = x_dim
        self.theta_embed_dim = max(30, 4 * theta_dim)
        self.x_embed_dim = max(30, 4 * x_dim)
        self.t_embed_dim = t_embed_dim

        # theta_t embedding network: 3-layer MLP, input=theta_dim, output=max(30,4d)
        self.theta_embedder = build_mlp(theta_dim, hidden_dim, self.theta_embed_dim, n_layers=3)

        # x embedding network: 3-layer MLP, input=x_dim, output=max(30,4p)
        self.x_embedder = build_mlp(x_dim, hidden_dim, self.x_embed_dim, n_layers=3)

        # Score network: 3-layer MLP, input=concat dims, output=theta_dim
        score_input_dim = self.theta_embed_dim + self.x_embed_dim + t_embed_dim
        self.score_net = build_mlp(score_input_dim, hidden_dim, theta_dim, n_layers=3)

        # Running statistics for standardisation (set during training)
        self.register_buffer('theta_mean', torch.zeros(theta_dim))
        self.register_buffer('theta_std', torch.ones(theta_dim))
        self.register_buffer('x_mean', torch.zeros(x_dim))
        self.register_buffer('x_std', torch.ones(x_dim))

    def standardise(self, theta: torch.Tensor, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Standardise theta and x using stored empirical mean/std (Appendix E.3.3).

        Args:
            theta: Parameter tensor, shape (batch_size, theta_dim).
            x: Observation tensor, shape (batch_size, x_dim).

        Returns:
            Tuple of standardised (theta, x).
        """
        theta_std = (theta - self.theta_mean) / (self.theta_std + 1e-8)
        x_std = (x - self.x_mean) / (self.x_std + 1e-8)
        return theta_std, x_std

    def set_standardisation(self, theta: torch.Tensor, x: torch.Tensor) -> None:
        """Set standardisation statistics from training data.

        Args:
            theta: All training theta_0 samples, shape (N, theta_dim).
            x: All training x samples, shape (N, x_dim).
        """
        self.theta_mean = theta.mean(0)
        self.theta_std = theta.std(0).clamp(min=1e-8)
        self.x_mean = x.mean(0)
        self.x_std = x.std(0).clamp(min=1e-8)

    def forward(
        self,
        theta_t: torch.Tensor,
        x: torch.Tensor,
        t: torch.Tensor,
    ) -> torch.Tensor:
        """Compute score estimate s_psi(theta_t, x, t).

        Args:
            theta_t: Noised parameters at time t, shape (batch_size, theta_dim).
            x: Conditioning observations, shape (batch_size, x_dim).
            t: Diffusion time values, shape (batch_size,).

        Returns:
            Score estimate, shape (batch_size, theta_dim), approximating
            ∇_{θ_t} log p_t(θ_t | x).
        """
        # Standardise inputs
        theta_t_std, x_std = self.standardise(theta_t, x)

        # Embed each input independently
        theta_emb = self.theta_embedder(theta_t_std)   # (B, theta_embed_dim)
        x_emb = self.x_embedder(x_std)                 # (B, x_embed_dim)
        t_emb = sinusoidal_embedding(t, self.t_embed_dim)  # (B, 64)

        # Concatenate and compute score
        combined = torch.cat([theta_emb, x_emb, t_emb], dim=-1)  # (B, total_dim)
        score = self.score_net(combined)                            # (B, theta_dim)
        return score
