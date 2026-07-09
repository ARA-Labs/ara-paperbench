"""
SAPG Model Architecture: Shared Backbone + Hanging Parameters

Implements the latent conditioning scheme from §4.4:
  - Shared actor backbone B_θ conditioned on per-policy hanging parameters ϕ_j
  - Shared critic backbone C_ψ conditioned on per-policy hanging parameters ϕ_j
  - ϕ_j ∈ R^32 for AllegroKuka; ϕ_j ∈ R^16 for ShadowHand/AllegroHand

Reference: Singla, Agarwal, Pathak (2024). SAPG. arXiv:2407.20230v1
"""

import torch
import torch.nn as nn
from typing import Tuple, Optional


class ELUNet(nn.Module):
    """
    MLP with ELU activation. Used as actor/critic backbone and observation preprocessor.
    """
    def __init__(self, input_dim: int, hidden_dims: Tuple[int, ...], output_dim: int):
        """
        Args:
            input_dim: input feature dimension
            hidden_dims: tuple of hidden layer widths
                AllegroKuka obs preprocessor: (768, 512, 256)
                ShadowHand actor: (512, 512, 256, 128)
                AllegroHand actor: (512, 256, 128)
            output_dim: output feature dimension
        """
        super().__init__()
        dims = [input_dim] + list(hidden_dims) + [output_dim]
        layers = []
        for i in range(len(dims) - 1):
            layers.append(nn.Linear(dims[i], dims[i + 1]))
            if i < len(dims) - 2:
                layers.append(nn.ELU())
        self.net = nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


class SharedBackboneActorMLP(nn.Module):
    """
    MLP actor with shared backbone B_θ conditioned on per-policy hanging params ϕ_j.

    Used for ShadowHand (512×512×256×128) and AllegroHand (512×256×128) tasks.

    The shared parameters θ are updated by gradients from all M policy objectives.
    The hanging parameters ϕ_j are only updated by policy j's objective.
    """
    def __init__(
        self,
        obs_dim: int,
        act_dim: int,
        hidden_dims: Tuple[int, ...],       # e.g. (512, 512, 256, 128)
        phi_dim: int = 16,                  # ϕ_j dimension: 32 for AllegroKuka, 16 for ShadowHand/AllegroHand
    ):
        """
        Args:
            obs_dim: observation space dimension
            act_dim: action space dimension
            hidden_dims: MLP hidden layer sizes (backbone θ)
            phi_dim: dimension of hanging parameters ϕ_j (16 or 32)
        """
        super().__init__()
        # Shared backbone processes obs + hanging params
        self.backbone = ELUNet(obs_dim + phi_dim, hidden_dims[:-1], hidden_dims[-1])
        # Mean head (shared θ)
        self.mean_head = nn.Linear(hidden_dims[-1], act_dim)
        # Log std: fixed learnable vector independent of observation (§B.1)
        self.log_std = nn.Parameter(torch.zeros(act_dim))
        # Hanging parameters ϕ_j (local to this policy instance)
        self.phi = nn.Parameter(torch.zeros(phi_dim))   # initialized to zero; trained only by this policy's objective

    def forward(self, obs: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Args:
            obs: observation tensor (B, obs_dim)

        Returns:
            mean: Gaussian action mean (B, act_dim)
            std: Gaussian action std (act_dim,) broadcast
        """
        phi_expanded = self.phi.unsqueeze(0).expand(obs.shape[0], -1)   # (B, phi_dim)
        x = torch.cat([obs, phi_expanded], dim=-1)                        # (B, obs_dim + phi_dim)
        features = self.backbone(x)                                        # (B, hidden_dims[-1])
        mean = self.mean_head(features)                                    # (B, act_dim)
        std = torch.exp(self.log_std).expand_as(mean)
        return mean, std

    def get_log_prob(self, obs: torch.Tensor, actions: torch.Tensor) -> torch.Tensor:
        """Compute log π(a|s) for given obs and actions."""
        mean, std = self.forward(obs)
        dist = torch.distributions.Normal(mean, std)
        return dist.log_prob(actions).sum(-1)   # (B,)

    def get_old_log_prob(self, obs: torch.Tensor, actions: torch.Tensor) -> torch.Tensor:
        """
        Compute log π_old(a|s) using a stored snapshot of old parameters.
        In practice, this is maintained by keeping a copy of the policy before the update.
        Placeholder — should be populated with old (pre-update) network weights.
        """
        raise NotImplementedError("Maintain old policy snapshot externally.")

    def get_entropy(self, obs: torch.Tensor) -> torch.Tensor:
        """Compute Gaussian entropy H(π(a|s)) = sum_d 0.5*log(2πe*σ_d^2)."""
        _, std = self.forward(obs)
        dist = torch.distributions.Normal(torch.zeros_like(std), std)
        return dist.entropy().sum(-1)    # (B,)

    def sample_action(self, obs: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Sample action and return (action, log_prob)."""
        mean, std = self.forward(obs)
        dist = torch.distributions.Normal(mean, std)
        action = dist.sample()
        log_prob = dist.log_prob(action).sum(-1)
        return action, log_prob


class SharedBackboneActorLSTM(nn.Module):
    """
    Recurrent actor for AllegroKuka tasks with:
      - MLP observation preprocessor: 768×512×256, ELU (Appendix B.1)
      - LSTM: 1 layer, 768 hidden units
      - Mean head: linear
      - log_std: fixed learnable vector independent of observation
      - Hanging params ϕ_j ∈ R^32 appended to LSTM input

    Shared backbone parameters θ updated by all M objectives.
    Local ϕ_j updated only by this policy's objective.
    """
    def __init__(
        self,
        obs_dim: int,
        act_dim: int,
        phi_dim: int = 32,
        mlp_hidden: Tuple[int, ...] = (768, 512, 256),   # observation preprocessor
        lstm_hidden: int = 768,
    ):
        """
        Args:
            obs_dim: observation dimension
            act_dim: action dimension
            phi_dim: hanging parameter dimension (32 for AllegroKuka, Appendix B.1)
            mlp_hidden: MLP preprocessor hidden dims (768×512×256 from paper)
            lstm_hidden: LSTM hidden dimension (768 from paper)
        """
        super().__init__()
        # Observation preprocessor MLP
        self.obs_mlp = ELUNet(obs_dim, mlp_hidden[:-1], mlp_hidden[-1])
        # LSTM takes preprocessed obs + hanging params
        self.lstm = nn.LSTM(input_size=mlp_hidden[-1] + phi_dim, hidden_size=lstm_hidden, num_layers=1, batch_first=True)
        # Action mean head
        self.mean_head = nn.Linear(lstm_hidden, act_dim)
        # Fixed learnable log std (state-independent)
        self.log_std = nn.Parameter(torch.zeros(act_dim))
        # Hanging params ϕ_j
        self.phi = nn.Parameter(torch.zeros(phi_dim))

    def forward(
        self,
        obs: torch.Tensor,                               # (B, T, obs_dim) or (B, obs_dim)
        hidden: Optional[Tuple[torch.Tensor, torch.Tensor]] = None,
    ) -> Tuple[torch.Tensor, torch.Tensor, Tuple]:
        """
        Returns:
            mean: (B, T, act_dim) or (B, act_dim)
            std: broadcast std
            hidden: updated LSTM hidden state
        """
        if obs.dim() == 2:
            obs = obs.unsqueeze(1)   # (B, 1, obs_dim)

        B, T, _ = obs.shape
        obs_flat = obs.view(B * T, -1)
        features = self.obs_mlp(obs_flat).view(B, T, -1)   # (B, T, 256)

        phi_expanded = self.phi.unsqueeze(0).unsqueeze(0).expand(B, T, -1)  # (B, T, phi_dim)
        lstm_input = torch.cat([features, phi_expanded], dim=-1)             # (B, T, 256+phi_dim)

        lstm_out, hidden = self.lstm(lstm_input, hidden)                     # (B, T, lstm_hidden)
        mean = self.mean_head(lstm_out)                                      # (B, T, act_dim)
        std = torch.exp(self.log_std).expand_as(mean)
        return mean.squeeze(1), std.squeeze(1), hidden

    def get_log_prob(self, obs: torch.Tensor, actions: torch.Tensor) -> torch.Tensor:
        mean, std, _ = self.forward(obs)
        dist = torch.distributions.Normal(mean, std)
        return dist.log_prob(actions).sum(-1)

    def get_entropy(self, obs: torch.Tensor) -> torch.Tensor:
        _, std, _ = self.forward(obs)
        dist = torch.distributions.Normal(torch.zeros_like(std), std)
        return dist.entropy().sum(-1)


class SharedCritic(nn.Module):
    """
    Shared critic backbone C_ψ conditioned on hanging parameters ϕ_j.
    Same architecture choice as actor backbone but outputs scalar value.

    ψ updated by all M critic objectives; ϕ_j updated only by policy j's critic objective.
    """
    def __init__(
        self,
        obs_dim: int,
        hidden_dims: Tuple[int, ...],
        phi_dim: int = 16,
    ):
        super().__init__()
        self.backbone = ELUNet(obs_dim + phi_dim, hidden_dims, hidden_dims[-1])
        self.value_head = nn.Linear(hidden_dims[-1], 1)
        self.phi = nn.Parameter(torch.zeros(phi_dim))

    def forward(self, obs: torch.Tensor) -> torch.Tensor:
        """
        Args:
            obs: (B, obs_dim)

        Returns:
            value: (B,) scalar value estimates
        """
        phi_expanded = self.phi.unsqueeze(0).expand(obs.shape[0], -1)
        x = torch.cat([obs, phi_expanded], dim=-1)
        features = self.backbone(x)
        return self.value_head(features).squeeze(-1)
