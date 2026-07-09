"""
RICE: Random Network Distillation (RND) Exploration Module
Implements intrinsic reward: R_RND(s') = |f(s') - f_hat(s')|^2
where f is a fixed random target network and f_hat is a learned predictor.
"""

import torch
import torch.nn as nn
import numpy as np
from typing import Tuple


class RNDTargetNetwork(nn.Module):
    """
    Fixed random target network f: S → R^k.
    Randomly initialized and FROZEN throughout training.
    """

    def __init__(self, state_dim: int, output_dim: int = 512, hidden_dim: int = 256):
        """
        Args:
            state_dim: Input state dimension
            output_dim: Embedding dimension k
            hidden_dim: Hidden layer width
        """
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
        )
        # Freeze all parameters — this network is never trained
        for param in self.parameters():
            param.requires_grad = False

    def forward(self, state: torch.Tensor) -> torch.Tensor:
        """
        Args:
            state: (batch, state_dim)
        Returns:
            embedding: (batch, output_dim)
        """
        return self.net(state)


class RNDPredictorNetwork(nn.Module):
    """
    Learned predictor network f_hat: S → R^k.
    Trained to predict the fixed target network's output.
    Higher prediction error → state is more novel.
    """

    def __init__(self, state_dim: int, output_dim: int = 512, hidden_dim: int = 256):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, state: torch.Tensor) -> torch.Tensor:
        """
        Args:
            state: (batch, state_dim)
        Returns:
            predicted_embedding: (batch, output_dim)
        """
        return self.net(state)


class RNDModule:
    """
    Complete RND module: maintains running statistics for normalization
    and computes intrinsic rewards.
    """

    def __init__(
        self,
        state_dim: int,
        output_dim: int = 512,
        hidden_dim: int = 256,
        lr: float = 1e-3,
    ):
        self.target = RNDTargetNetwork(state_dim, output_dim, hidden_dim)
        self.predictor = RNDPredictorNetwork(state_dim, output_dim, hidden_dim)
        self.optimizer = torch.optim.Adam(self.predictor.parameters(), lr=lr)

        # Running statistics for normalization (Algorithm 2: "with normalization")
        self.reward_running_mean = 0.0
        self.reward_running_var = 1.0
        self.reward_count = 0

    def compute_intrinsic_reward(
        self, next_states: torch.Tensor, normalize: bool = True
    ) -> torch.Tensor:
        """
        Compute RND intrinsic reward for a batch of next states.
        R_RND(s') = |f(s') - f_hat(s')|^2
        
        Args:
            next_states: (batch, state_dim)
            normalize: Whether to apply running-stats normalization
        
        Returns:
            intrinsic_rewards: (batch,) non-negative float tensor
        """
        with torch.no_grad():
            target_embed = self.target(next_states)
        pred_embed = self.predictor(next_states)
        raw_reward = ((target_embed - pred_embed) ** 2).sum(dim=-1)

        if normalize:
            raw_reward_np = raw_reward.detach().numpy()
            # Update running statistics (Welford's online algorithm)
            batch_size = raw_reward_np.shape[0]
            self.reward_count += batch_size
            delta = raw_reward_np.mean() - self.reward_running_mean
            self.reward_running_mean += delta * batch_size / self.reward_count
            delta2 = raw_reward_np.mean() - self.reward_running_mean
            self.reward_running_var += delta * delta2 * batch_size
            std = max(np.sqrt(self.reward_running_var / max(self.reward_count, 1)), 1e-8)
            raw_reward = raw_reward / std

        return raw_reward.detach()

    def update_predictor(self, next_states: torch.Tensor) -> float:
        """
        Update predictor network to minimize MSE with target network.
        Called after each PPO update (Algorithm 2: "Optimize f_hat w.r.t. MSE loss").
        
        Args:
            next_states: (batch, state_dim)
        
        Returns:
            loss_value: float MSE loss
        """
        with torch.no_grad():
            target_embed = self.target(next_states)
        pred_embed = self.predictor(next_states)
        loss = nn.functional.mse_loss(pred_embed, target_embed)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        return loss.item()
