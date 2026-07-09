"""
Functional Reward Encoding (FRE) — Core Implementation Stub

Implements:
  - Reward discretization and embedding
  - Permutation-invariant transformer encoder p_theta(z | {s^e_k, eta(s^e_k)})
  - Feedforward decoder q_theta(eta(s^d) | s^d, z)
  - Random reward function samplers (goal-reaching, linear, MLP)
  - FRE VAE training objective (ELBO with KL penalty)

Reference: Frans et al., "Unsupervised Zero-Shot RL via Functional Reward Encodings"
           arXiv:2402.17135, Section 4.1, 4.2, Algorithm 1, Appendix B
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from typing import Tuple, List, Optional


# ── Reward Discretization ────────────────────────────────────────────────────

def discretize_reward(rewards: torch.Tensor, n_bins: int = 32) -> torch.Tensor:
    """
    Discretize scalar rewards in approximately [-1, 1] into n_bins integer bins.

    Args:
        rewards: (B,) or (B, K) float tensor of scalar reward values
        n_bins:  number of bins (default: 32 per Appendix A)

    Returns:
        bin_indices: same shape as rewards, dtype=long, values in {0, ..., n_bins-1}

    Implementation:
        1. Rescale [-1, 1] -> [0, 1]: r_norm = (r + 1) / 2
        2. Clip to [0, 1]
        3. Multiply by n_bins and floor
        4. Clamp to [0, n_bins - 1]
    """
    r_norm = (rewards + 1.0) / 2.0
    r_clipped = r_norm.clamp(0.0, 1.0)
    bin_idx = (r_clipped * n_bins).floor().long()
    return bin_idx.clamp(0, n_bins - 1)


# ── FRE Encoder ───────────────────────────────────────────────────────────────

class FREEncoder(nn.Module):
    """
    Permutation-invariant transformer encoder for FRE.

    Encodes a set of K (state, reward) pairs into a Gaussian distribution
    over latent task vector z.

    Architecture (Appendix A, Section 4.1):
      - Reward: discretized to {0,...,31}, then embedded (32 x reward_emb_dim)
      - State:  linear projection (state_dim -> state_emb_dim)
      - Token:  concat(state_emb, reward_emb) -> token_dim
      - Transformer: 4 layers, 256 hidden dim, NO causal mask, NO positional encoding
      - Mean pool over K tokens -> linear -> (mu, log_sigma) of latent z
    """

    def __init__(
        self,
        state_dim: int,
        latent_dim: int,
        n_reward_bins: int = 32,
        reward_emb_dim: int = 64,
        state_emb_dim: int = 192,
        n_layers: int = 4,
        n_heads: int = 4,
        hidden_dim: int = 256,
    ):
        super().__init__()
        self.n_reward_bins = n_reward_bins
        token_dim = state_emb_dim + reward_emb_dim

        # Reward embedding table: n_reward_bins x reward_emb_dim
        self.reward_embedding = nn.Embedding(n_reward_bins, reward_emb_dim)

        # State linear projection
        self.state_proj = nn.Linear(state_dim, state_emb_dim)

        # Permutation-invariant transformer (no causal mask, no positional encodings)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=token_dim,
            nhead=n_heads,
            dim_feedforward=hidden_dim * 4,
            batch_first=True,
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=n_layers)

        # Output heads for Gaussian parameters
        self.mu_head = nn.Linear(token_dim, latent_dim)
        self.log_sigma_head = nn.Linear(token_dim, latent_dim)

    def forward(
        self,
        states: torch.Tensor,    # (B, K, state_dim)
        rewards: torch.Tensor,   # (B, K) float, in approximately [-1, 1]
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Encode a set of (state, reward) context pairs into Gaussian parameters.

        Args:
            states:  (B, K, state_dim) — K encoder context states per batch
            rewards: (B, K)            — corresponding scalar rewards

        Returns:
            mu:        (B, latent_dim) — mean of latent distribution
            log_sigma: (B, latent_dim) — log std of latent distribution
        """
        B, K, _ = states.shape

        # Discretize and embed rewards
        bin_idx = discretize_reward(rewards, self.n_reward_bins)  # (B, K)
        reward_emb = self.reward_embedding(bin_idx)               # (B, K, reward_emb_dim)

        # Project states
        state_emb = self.state_proj(states)                       # (B, K, state_emb_dim)

        # Concatenate to form tokens (no positional encoding)
        tokens = torch.cat([state_emb, reward_emb], dim=-1)       # (B, K, token_dim)

        # Permutation-invariant transformer (no causal mask)
        h = self.transformer(tokens)                               # (B, K, token_dim)

        # Mean pool over K tokens
        h_mean = h.mean(dim=1)                                     # (B, token_dim)

        mu = self.mu_head(h_mean)                                  # (B, latent_dim)
        log_sigma = self.log_sigma_head(h_mean)                    # (B, latent_dim)
        return mu, log_sigma

    def sample(
        self,
        states: torch.Tensor,    # (B, K, state_dim)
        rewards: torch.Tensor,   # (B, K)
    ) -> torch.Tensor:
        """
        Sample latent z ~ N(mu, sigma) via reparameterization.

        Returns:
            z: (B, latent_dim)
        """
        mu, log_sigma = self.forward(states, rewards)
        sigma = log_sigma.exp()
        eps = torch.randn_like(sigma)
        return mu + sigma * eps


# ── FRE Decoder ───────────────────────────────────────────────────────────────

class FREDecoder(nn.Module):
    """
    Feedforward decoder that predicts reward for a single state given latent z.

    Architecture (Appendix A):
      - Input: concat(s^d, z) -> MLP [512, 512, 512] -> scalar reward prediction

    Args:
        state_dim:  observation dimension
        latent_dim: dimension of z
        hidden_dim: hidden layer size (default: 512 per Appendix A)
        n_layers:   number of hidden layers (default: 3)
    """

    def __init__(
        self,
        state_dim: int,
        latent_dim: int,
        hidden_dim: int = 512,
        n_layers: int = 3,
    ):
        super().__init__()
        layers = [nn.Linear(state_dim + latent_dim, hidden_dim), nn.ReLU()]
        for _ in range(n_layers - 1):
            layers += [nn.Linear(hidden_dim, hidden_dim), nn.ReLU()]
        layers.append(nn.Linear(hidden_dim, 1))
        self.net = nn.Sequential(*layers)

    def forward(
        self,
        states: torch.Tensor,   # (B, state_dim) or (B, K', state_dim)
        z: torch.Tensor,        # (B, latent_dim) or (B, 1, latent_dim)
    ) -> torch.Tensor:
        """
        Predict reward for each decoder state independently given shared z.

        Args:
            states: (B, K', state_dim) — K' decoder states
            z:      (B, latent_dim)    — shared latent encoding

        Returns:
            r_hat: (B, K', 1) — predicted rewards
        """
        if states.dim() == 3:
            B, K_prime, _ = states.shape
            z_expanded = z.unsqueeze(1).expand(B, K_prime, -1)
            inp = torch.cat([states, z_expanded], dim=-1)   # (B, K', state+latent)
            return self.net(inp)                             # (B, K', 1)
        else:
            inp = torch.cat([states, z], dim=-1)
            return self.net(inp)                             # (B, 1)


# ── FRE VAE Training Objective ────────────────────────────────────────────────

def fre_elbo_loss(
    encoder: FREEncoder,
    decoder: FREDecoder,
    enc_states: torch.Tensor,    # (B, K, state_dim)
    enc_rewards: torch.Tensor,   # (B, K)
    dec_states: torch.Tensor,    # (B, K', state_dim)
    dec_rewards: torch.Tensor,   # (B, K')
    beta: float = 0.01,
) -> torch.Tensor:
    """
    Compute FRE ELBO loss (Eq. 6 in paper):

      L = -MSE(r_hat, r_true) - beta * KL(N(mu, sigma) || N(0, I))

    Args:
        enc_states:  encoder context states    (B, K, state_dim)
        enc_rewards: encoder context rewards   (B, K)
        dec_states:  decoder target states     (B, K', state_dim)  [disjoint from enc]
        dec_rewards: decoder target rewards    (B, K')
        beta:        KL weight (default: 0.01 per Appendix A)

    Returns:
        loss: scalar tensor (negated ELBO, to minimize)
    """
    # Encode
    mu, log_sigma = encoder(enc_states, enc_rewards)   # (B, latent_dim)
    sigma = log_sigma.exp()

    # Reparameterized sample
    eps = torch.randn_like(sigma)
    z = mu + sigma * eps                               # (B, latent_dim)

    # Decode
    r_hat = decoder(dec_states, z).squeeze(-1)         # (B, K')

    # Reconstruction loss (MSE)
    recon_loss = F.mse_loss(r_hat, dec_rewards)

    # KL divergence: KL(N(mu, sigma) || N(0, I))
    kl_loss = -0.5 * (1 + 2 * log_sigma - mu.pow(2) - sigma.pow(2)).sum(dim=-1).mean()

    return recon_loss + beta * kl_loss


# ── Random Reward Function Samplers ───────────────────────────────────────────

def sample_goal_reaching_reward(
    dataset_states: np.ndarray,    # (N, state_dim) all offline states
    trajectory_states: np.ndarray, # (T, state_dim) current trajectory states
    goal_dist_threshold: float = 2.0,
    p_current: float = 0.2,
    p_future: float = 0.5,
    p_random: float = 0.3,
) -> callable:
    """
    Sample a singleton goal-reaching reward function using HER-style goal selection.

    Goal selection (Appendix B, Section 4.2):
      - With prob 0.2: goal = current/random state from dataset
      - With prob 0.5: goal = future state in same trajectory
      - With prob 0.3: goal = completely random state from dataset

    Returns:
        reward_fn: callable (state -> float), reward = -1 until goal, 0 at goal
    """
    r = np.random.random()
    if r < p_current:
        goal_idx = np.random.randint(len(dataset_states))
        goal = dataset_states[goal_idx]
    elif r < p_current + p_future:
        future_idx = np.random.randint(len(trajectory_states))
        goal = trajectory_states[future_idx]
    else:
        goal_idx = np.random.randint(len(dataset_states))
        goal = dataset_states[goal_idx]

    def reward_fn(state: np.ndarray) -> float:
        dist = np.linalg.norm(state - goal)
        return 0.0 if dist < goal_dist_threshold else -1.0

    return reward_fn


def sample_random_linear_reward(
    state_dim: int,
    exclude_dims: Optional[List[int]] = None,
    sparsity_prob: float = 0.9,
) -> callable:
    """
    Sample a random linear reward function.

    Implementation (Appendix B):
      - Sample weight vector w ~ Uniform(-1, 1)^state_dim
      - Apply sparse binary mask: each dim zeroed with prob 0.9
      - For AntMaze: exclude XY dims (passed via exclude_dims)

    Returns:
        reward_fn: callable (state -> float)
    """
    w = np.random.uniform(-1.0, 1.0, size=state_dim)
    mask = (np.random.random(state_dim) > sparsity_prob).astype(float)
    w = w * mask
    if exclude_dims is not None:
        for d in exclude_dims:
            w[d] = 0.0

    def reward_fn(state: np.ndarray) -> float:
        return float(np.dot(w, state))

    return reward_fn


def sample_random_mlp_reward(state_dim: int) -> nn.Module:
    """
    Sample a random 2-layer MLP reward function.

    Architecture (Appendix B, Section 4.2):
      - Linear(state_dim -> 32) + tanh + Linear(32 -> 1)
      - Parameters ~ N(0, sigma^2) where sigma = 1/sqrt(avg_layer_dim)
      - Output clipped to [-1, 1]

    Returns:
        reward_mlp: nn.Module, call with torch.Tensor(state_dim) -> scalar in [-1, 1]
    """
    hidden_dim = 32

    class RandomMLP(nn.Module):
        def __init__(self):
            super().__init__()
            self.fc1 = nn.Linear(state_dim, hidden_dim)
            self.fc2 = nn.Linear(hidden_dim, 1)
            # Init: normal scaled by average dim
            scale1 = 1.0 / ((state_dim + hidden_dim) / 2.0) ** 0.5
            scale2 = 1.0 / ((hidden_dim + 1) / 2.0) ** 0.5
            nn.init.normal_(self.fc1.weight, std=scale1)
            nn.init.normal_(self.fc1.bias, std=scale1)
            nn.init.normal_(self.fc2.weight, std=scale2)
            nn.init.normal_(self.fc2.bias, std=scale2)

        def forward(self, state: torch.Tensor) -> torch.Tensor:
            h = torch.tanh(self.fc1(state))
            out = self.fc2(h)
            return out.clamp(-1.0, 1.0)

    return RandomMLP()


def sample_reward_function(
    state_dim: int,
    dataset_states: np.ndarray,
    trajectory_states: np.ndarray,
    ratio_goal: float = 1.0 / 3.0,
    ratio_linear: float = 1.0 / 3.0,
    ratio_mlp: float = 1.0 / 3.0,
    exclude_xy_dims: Optional[List[int]] = None,
) -> callable:
    """
    Sample from the FRE-all prior reward distribution (uniform mixture of three families).

    Args:
        state_dim:          observation dimensionality
        dataset_states:     (N, state_dim) offline dataset states
        trajectory_states:  (T, state_dim) states from current trajectory (for HER)
        ratio_goal/linear/mlp: sampling probabilities (must sum to ~1.0)
        exclude_xy_dims:    dims to exclude from linear rewards (AntMaze XY)

    Returns:
        reward_fn: callable (state: np.ndarray -> float)
    """
    r = np.random.random()
    if r < ratio_goal:
        return sample_goal_reaching_reward(dataset_states, trajectory_states)
    elif r < ratio_goal + ratio_linear:
        fn = sample_random_linear_reward(state_dim, exclude_dims=exclude_xy_dims)
        return fn
    else:
        mlp = sample_random_mlp_reward(state_dim)
        mlp.eval()

        def reward_fn(state: np.ndarray) -> float:
            with torch.no_grad():
                s = torch.FloatTensor(state)
                return mlp(s).item()

        return reward_fn
