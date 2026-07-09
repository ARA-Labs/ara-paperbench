"""
SAPG Policy Network: Shared Backbone + Hanging Parameters (ϕ_j)

Implements the multi-policy architecture described in Section 4.4:
- Shared backbone B_θ (actor) and C_ψ (critic) across all M policies
- Per-policy learnable hanging parameters ϕ_j ∈ R^d
- Three task-specific backbones:
    - AllegroKuka: MLP(768×512×256) + ELU + LSTM(768)
    - ShadowHand: MLP(512×512×256×128) + ELU
    - AllegroHand: MLP(512×256×128) + ELU
"""

import torch
import torch.nn as nn
from typing import Optional, Tuple


class ELUMlpBackbone(nn.Module):
    """
    MLP backbone with ELU activations, shared across all policies.
    Input is concatenated with hanging parameter ϕ_j before processing.

    Used for ShadowHand (512×512×256×128) and AllegroHand (512×256×128).
    Also used as MLP pre-processor for AllegroKuka LSTM policy.
    """

    def __init__(
        self,
        obs_dim: int,             # dimension of observation vector
        hidden_dims: list,        # e.g., [512, 512, 256, 128] for ShadowHand
        phi_dim: int,             # dimension of hanging parameter ϕ_j
    ):
        super().__init__()
        self.phi_dim = phi_dim
        input_dim = obs_dim + phi_dim

        layers = []
        in_features = input_dim
        for h in hidden_dims:
            layers += [nn.Linear(in_features, h), nn.ELU()]
            in_features = h
        self.net = nn.Sequential(*layers)
        self.output_dim = in_features

    def forward(
        self,
        obs: torch.Tensor,    # (B, obs_dim)
        phi: torch.Tensor,    # (B, phi_dim) — per-policy hanging parameter, broadcast as needed
    ) -> torch.Tensor:        # (B, output_dim)
        x = torch.cat([obs, phi], dim=-1)
        return self.net(x)


class LSTMPolicyBackbone(nn.Module):
    """
    LSTM-based policy backbone for AllegroKuka tasks (Section B.1).
    Architecture: MLP(obs+ϕ → 768×512×256) + LSTM(256 → 768).
    Sigma is a fixed learnable vector independent of input.
    """

    def __init__(
        self,
        obs_dim: int,         # observation dimension (AllegroKuka: ~75+)
        action_dim: int,      # action dimension (AllegroKuka: 23)
        phi_dim: int = 32,    # hanging parameter dimension (R32 for AllegroKuka)
        mlp_dims: list = None,  # MLP dims before LSTM: [768, 512, 256]
        lstm_hidden: int = 768, # LSTM hidden size
    ):
        super().__init__()
        if mlp_dims is None:
            mlp_dims = [768, 512, 256]

        self.phi_dim = phi_dim
        self.lstm_hidden = lstm_hidden

        # MLP pre-processor (shared backbone)
        self.mlp = ELUMlpBackbone(obs_dim, mlp_dims, phi_dim)

        # LSTM core (shared backbone)
        self.lstm = nn.LSTM(input_size=mlp_dims[-1], hidden_size=lstm_hidden, num_layers=1, batch_first=True)

        # Action mean head
        self.action_mean = nn.Linear(lstm_hidden, action_dim)

        # Fixed learnable sigma (not input-dependent, shared or per-block depending on entropy mode)
        self.log_sigma = nn.Parameter(torch.zeros(action_dim))

    def forward(
        self,
        obs: torch.Tensor,          # (B, obs_dim) or (B, T, obs_dim) for sequences
        phi: torch.Tensor,          # (phi_dim,) or (B, phi_dim) hanging parameters
        hidden: Optional[Tuple[torch.Tensor, torch.Tensor]] = None,  # LSTM hidden state
    ) -> Tuple[torch.Tensor, Optional[Tuple]]:
        """
        Returns:
            action_mean: (B, action_dim)
            hidden: updated LSTM hidden state
        """
        if obs.dim() == 2:
            obs = obs.unsqueeze(1)   # add time dim for LSTM: (B, 1, obs_dim)

        B, T, _ = obs.shape
        if phi.dim() == 1:
            phi = phi.unsqueeze(0).unsqueeze(0).expand(B, T, -1)
        elif phi.dim() == 2:
            phi = phi.unsqueeze(1).expand(B, T, -1)

        obs_flat = obs.reshape(B * T, -1)
        phi_flat = phi.reshape(B * T, -1)

        mlp_out = self.mlp(obs_flat, phi_flat)          # (B*T, mlp_dims[-1])
        lstm_in = mlp_out.reshape(B, T, -1)

        lstm_out, hidden = self.lstm(lstm_in, hidden)   # (B, T, lstm_hidden)
        action_mean = self.action_mean(lstm_out[:, -1, :])  # take last step
        return action_mean, hidden

    def get_log_prob(
        self,
        obs: torch.Tensor,      # (B, obs_dim)
        actions: torch.Tensor,  # (B, action_dim)
        phi: torch.Tensor,      # (phi_dim,) or (B, phi_dim)
        hidden: Optional[Tuple] = None,
    ) -> Tuple[torch.Tensor, Optional[Tuple]]:
        """Compute log π(a|s, ϕ) under Gaussian policy."""
        mean, hidden = self.forward(obs, phi, hidden)
        sigma = torch.exp(self.log_sigma)
        dist = torch.distributions.Normal(mean, sigma)
        log_prob = dist.log_prob(actions).sum(-1)  # (B,)
        return log_prob, hidden


class MLPPolicy(nn.Module):
    """
    MLP-based policy for ShadowHand and AllegroHand tasks.
    Uses ELUMlpBackbone with task-specific hidden dims.
    """

    def __init__(
        self,
        obs_dim: int,
        action_dim: int,
        phi_dim: int = 16,          # R16 for easy tasks
        hidden_dims: list = None,   # [512, 512, 256, 128] for ShadowHand
    ):
        super().__init__()
        if hidden_dims is None:
            hidden_dims = [512, 512, 256, 128]  # ShadowHand default
        self.backbone = ELUMlpBackbone(obs_dim, hidden_dims, phi_dim)
        self.action_mean = nn.Linear(self.backbone.output_dim, action_dim)
        self.log_sigma = nn.Parameter(torch.zeros(action_dim))

    def forward(
        self,
        obs: torch.Tensor,   # (B, obs_dim)
        phi: torch.Tensor,   # (phi_dim,) or (B, phi_dim)
    ) -> torch.Tensor:       # (B, action_dim) action means
        if phi.dim() == 1:
            phi = phi.unsqueeze(0).expand(obs.shape[0], -1)
        h = self.backbone(obs, phi)
        return self.action_mean(h)

    def get_log_prob(
        self,
        obs: torch.Tensor,      # (B, obs_dim)
        actions: torch.Tensor,  # (B, action_dim)
        phi: torch.Tensor,
    ) -> torch.Tensor:
        """Compute log π(a|s, ϕ) under Gaussian policy."""
        mean = self.forward(obs, phi)
        sigma = torch.exp(self.log_sigma)
        dist = torch.distributions.Normal(mean, sigma)
        return dist.log_prob(actions).sum(-1)   # (B,)


class SAPGMultiPolicy(nn.Module):
    """
    Full SAPG multi-policy system with shared backbone and per-policy hanging parameters.

    Contains:
    - Shared actor backbone parameters θ (B_θ)
    - Shared critic backbone parameters ψ (C_ψ)
    - Per-policy hanging parameters ϕ_j, j=1..M
    - Per-policy log_sigma (when entropy regularization is active)

    Parameter update rules:
    - θ, ψ: updated by ALL policy gradients
    - ϕ_j: updated ONLY by policy j's objective gradient
    """

    def __init__(
        self,
        obs_dim: int,
        action_dim: int,
        M: int = 6,                  # total number of policies (1 leader + M-1 followers)
        phi_dim: int = 32,           # hanging parameter dimension
        policy_type: str = 'lstm',   # 'lstm' for AllegroKuka, 'mlp' for ShadowHand/AllegroHand
        hidden_dims: list = None,
        lstm_hidden: int = 768,
    ):
        super().__init__()
        self.M = M
        self.phi_dim = phi_dim

        # Shared hanging parameters ϕ_j for each policy (learnable, per-policy)
        # θ, ψ are implicitly shared via the backbone networks
        self.phi = nn.ParameterList([
            nn.Parameter(torch.randn(phi_dim) * 0.01) for _ in range(M)
        ])

        if policy_type == 'lstm':
            self.actor_backbone = LSTMPolicyBackbone(
                obs_dim, action_dim, phi_dim=phi_dim,
                mlp_dims=hidden_dims or [768, 512, 256],
                lstm_hidden=lstm_hidden
            )
        else:
            self.actor_backbone = MLPPolicy(
                obs_dim, action_dim, phi_dim=phi_dim,
                hidden_dims=hidden_dims or [512, 512, 256, 128]
            )

        # Critic backbone (same structure, conditioned on ϕ_j)
        # For simplicity, critic uses a separate MLP backbone
        critic_mlp_dims = hidden_dims or [512, 512, 256, 128]
        self.critic_backbone = ELUMlpBackbone(obs_dim, critic_mlp_dims, phi_dim)
        self.critic_head = nn.Linear(self.critic_backbone.output_dim, 1)

    def get_value(
        self,
        obs: torch.Tensor,   # (B, obs_dim)
        policy_idx: int,     # which policy (0=leader, 1..M-1=followers)
    ) -> torch.Tensor:       # (B,) scalar values
        phi = self.phi[policy_idx].unsqueeze(0).expand(obs.shape[0], -1)
        h = self.critic_backbone(obs, phi)
        return self.critic_head(h).squeeze(-1)

    def get_action_log_prob(
        self,
        obs: torch.Tensor,
        actions: torch.Tensor,
        policy_idx: int,
    ) -> torch.Tensor:  # (B,) log probabilities
        phi = self.phi[policy_idx]
        if hasattr(self.actor_backbone, 'get_log_prob'):
            return self.actor_backbone.get_log_prob(obs, actions, phi)
        return self.actor_backbone.get_log_prob(obs, actions, phi)

    def get_backbone_params(self):
        """Returns shared backbone parameters (θ, ψ) for joint optimization."""
        backbone_params = (
            list(self.actor_backbone.parameters()) +
            list(self.critic_backbone.parameters()) +
            list(self.critic_head.parameters())
        )
        return backbone_params

    def get_hanging_params(self, policy_idx: int):
        """Returns hanging parameters ϕ_j for per-policy optimization."""
        return [self.phi[policy_idx]]
