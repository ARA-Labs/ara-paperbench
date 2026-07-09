"""
Random Network Distillation (RND) Model
=========================================
Implements the RND exploration bonus for RICE refining.

From Burda et al. (2018): "Exploration by Random Network Distillation"
Used in RICE to provide intrinsic reward: R^RND = ||f(s') - ˆf(s')||²

Architecture (MuJoCo, from Refine_mujoco/models.py):
    Both target f and predictor ˆf:
        Linear(input_size, 128) -> ReLU -> Linear(128, 128) -> ReLU -> Linear(128, output_size)
    
    Initialization: Orthogonal with gain=√2, zero bias
    Target f: frozen (no gradient)
    Predictor ˆf: updated by MSE loss during refining

The RND bonus naturally decays to zero as ˆf converges to f,
recovering the original task reward policy as training progresses.

Dependencies: torch, numpy
"""

import numpy as np
import torch
import torch.nn as nn
from torch.nn import init
from typing import Tuple


class RNDModel(nn.Module):
    """
    RND model with a fixed target network f and a trainable predictor network ˆf.

    Intrinsic reward = (target_feature - predict_feature)^2 / 2
    Summed over feature dimensions.
    """

    def __init__(
        self,
        device: torch.device,
        input_size: int,    # Observation dimension (MuJoCo: env-specific)
        output_size: int    # Feature size (typically same as input_size)
    ):
        """
        Args:
            device: CUDA device or CPU
            input_size: Dimension of state observations
            output_size: Dimension of RND feature embedding
        """
        super(RNDModel, self).__init__()
        self.device = device
        self.input_size = input_size
        self.output_size = output_size

        # Trainable predictor ˆf: updated to minimize MSE with frozen target
        self.predictor = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, output_size)
        )

        # Fixed target network f: randomly initialized and frozen
        self.target = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU(),
            nn.Linear(128, output_size)
        )

        # Orthogonal initialization (gain=√2) for all linear layers; zero bias
        for m in self.modules():
            if isinstance(m, nn.Linear):
                init.orthogonal_(m.weight, np.sqrt(2))
                m.bias.data.zero_()

        # Freeze target network — must never be updated
        for param in self.target.parameters():
            param.requires_grad = False

    def forward(
        self,
        next_obs: torch.Tensor  # Shape: [batch_size, input_size]
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Forward pass through both networks.

        Args:
            next_obs: Batch of next-state observations s_{t+1}

        Returns:
            (predict_feature, target_feature): Both shape [batch_size, output_size]
            Used for MSE loss: L = MSE(predict_feature, target_feature.detach())
        """
        target_feature = self.target(next_obs)
        predict_feature = self.predictor(next_obs)
        return predict_feature, target_feature

    def compute_bonus(
        self,
        next_obs: np.ndarray    # Shape: [batch_size, input_size]
    ) -> np.ndarray:
        """
        Compute per-sample RND intrinsic reward.

        R^RND(s') = ||f(s') - ˆf(s')||² / 2

        Args:
            next_obs: Next states as numpy array

        Returns:
            intrinsic_reward: Shape [batch_size], numpy array
        """
        next_obs_tensor = torch.FloatTensor(next_obs).to(self.device)
        with torch.no_grad():
            target_next_feature = self.target(next_obs_tensor)
            predict_next_feature = self.predictor(next_obs_tensor)
        intrinsic_reward = (target_next_feature - predict_next_feature).pow(2).sum(1) / 2
        return intrinsic_reward.data.cpu().numpy()


class RunningMeanStd:
    """
    Welford online algorithm for computing running mean and variance.
    Used to normalize RND intrinsic rewards to prevent overwhelming task reward.

    From Refine_mujoco/utils.py
    """

    def __init__(self, epsilon: float = 1e-4, shape: int = 0):
        """
        Args:
            epsilon: Initial count to avoid division by zero
            shape: Dimension of tracked values (0 = scalar)
        """
        self.mean = np.zeros(shape, np.float64)
        self.var = np.ones(shape, np.float64)
        self.count = epsilon

    def update(self, arr: np.ndarray) -> None:
        """Update running statistics with a new batch of values."""
        batch_mean = np.mean(arr, axis=0)
        batch_var = np.var(arr, axis=0)
        batch_count = arr.shape[0]
        self.update_from_moments(batch_mean, batch_var, batch_count)

    def update_from_moments(
        self,
        batch_mean: np.ndarray,
        batch_var: np.ndarray,
        batch_count: float
    ) -> None:
        delta = batch_mean - self.mean
        tot_count = self.count + batch_count
        new_mean = self.mean + delta * batch_count / tot_count
        m_a = self.var * self.count
        m_b = batch_var * batch_count
        m_2 = m_a + m_b + np.square(delta) * self.count * batch_count / (self.count + batch_count)
        new_var = m_2 / (self.count + batch_count)
        self.mean = new_mean
        self.var = new_var
        self.count = batch_count + self.count

    def normalize(self, value: np.ndarray) -> np.ndarray:
        """Normalize value using running mean and std."""
        return (value - self.mean) / (np.sqrt(self.var) + 1e-8)
