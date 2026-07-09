"""
RoboticSequence environment wrapper for Meta-World.
Implements the sequential multi-stage robotic task from Section 3.

Tasks (in order): hammer → push → peg-unplug-side → push-wall
Pre-trained on: peg-unplug-side + push-wall (FAR states)
Fine-tuned on: full 4-stage sequence starting from hammer (CLOSE states)

Reference: Wołczyk et al. (2024), ICML 2024 (Algorithm 1 in Appendix B.3)
"""

import numpy as np
import torch
import torch.nn as nn
from typing import List, Optional, Tuple, Dict


class RoboticSequence:
    """
    Sequential robotic manipulation task built on Meta-World.

    Algorithm 1 (from paper):
        i = 1; t = 1
        while i <= N and t <= T:
            take step in E_i using π
            if E_i is solved:
                i = i + 1; t = 1
        return i - 1

    Key design choices:
    - Random start/goal positions sampled per episode
    - Stage ID encoded as one-hot vector, appended to observation
    - Normalized timestep (t/T) appended to state vector
    - T = 200 max steps per stage
    - Episode terminates on success OR timeout (not after 200 steps regardless)
    - SAC gets terminal signal in both cases (no bootstrapping)
    - Augmented success reward: r'_t = β * r_t * (T - t), β = 1.5
    """

    STAGE_NAMES: List[str] = ["hammer", "push", "peg-unplug-side", "push-wall"]
    T_MAX: int = 200
    BETA: float = 1.5  # success reward multiplier

    def __init__(self, envs: List, stage_names: Optional[List[str]] = None):
        """
        Args:
            envs: List of N Meta-World environment instances (one per stage)
            stage_names: Optional custom stage name list (default: STAGE_NAMES)
        """
        self.envs = envs
        self.stage_names = stage_names or self.STAGE_NAMES
        self.n_stages = len(self.envs)
        self.current_stage = 0
        self.timestep = 0

    def reset(self) -> np.ndarray:
        """Reset to first stage; random start/goal conditions per Meta-World convention."""
        self.current_stage = 0
        self.timestep = 0
        obs = self.envs[self.current_stage].reset()
        return self._augment_obs(obs)

    def step(self, action: np.ndarray) -> Tuple[np.ndarray, float, bool, Dict]:
        """
        Execute one step in the current stage.

        Returns augmented observation with:
        - one-hot stage ID appended
        - normalized timestep (t/T) appended
        - augmented reward on success: r' = β * r * (T - t)
        - terminal=True on success or timeout (SAC does NOT bootstrap)
        """
        obs, reward, done, info = self.envs[self.current_stage].step(action)
        self.timestep += 1

        success = info.get("success", False)
        timeout = self.timestep >= self.T_MAX

        if success:
            # Augment reward: r'_t = β * r_t * (T - t)
            reward = self.BETA * reward * (self.T_MAX - self.timestep)
            # Move to next stage or terminate episode
            if self.current_stage < self.n_stages - 1:
                self.current_stage += 1
                self.timestep = 0
                obs = self.envs[self.current_stage].reset()
                terminal = False
            else:
                terminal = True  # all stages completed
        elif timeout:
            terminal = True
        else:
            terminal = False

        augmented_obs = self._augment_obs(obs)
        return augmented_obs, reward, terminal, info

    def _augment_obs(self, obs: np.ndarray) -> np.ndarray:
        """
        Append stage one-hot encoding and normalized timestep to observation.

        stage_onehot: [0, 0, ..., 1, ..., 0] of length n_stages
        norm_timestep: t / T_MAX ∈ [0, 1]
        """
        stage_onehot = np.zeros(self.n_stages, dtype=np.float32)
        stage_onehot[self.current_stage] = 1.0
        norm_timestep = np.array([self.timestep / self.T_MAX], dtype=np.float32)
        return np.concatenate([obs, stage_onehot, norm_timestep])

    def get_stage_success_rates(self) -> List[float]:
        """Return per-stage success rates for evaluation (Figure 7)."""
        raise NotImplementedError("Track success rates in training loop")


class MultiHeadMLP(nn.Module):
    """
    4-layer MLP with separate output heads per stage.
    Architecture: Input → LayerNorm → LeakyReLU × 4 → stage-specific head

    Outperforms adding stage ID to input (per Appendix B.3).

    Args:
        input_dim: Observation dimension (robot config + stage_onehot + norm_timestep)
        hidden_dim: 256 (paper default)
        output_dim: Action/value dimension
        n_stages: Number of stages (4 for main experiment)
        n_layers: Number of hidden layers (4, paper default)
    """

    def __init__(
        self,
        input_dim: int,
        hidden_dim: int = 256,
        output_dim: int = 4,
        n_stages: int = 4,
        n_layers: int = 4,
    ):
        super().__init__()
        # Shared backbone
        layers = []
        in_dim = input_dim
        for i in range(n_layers):
            layers.append(nn.Linear(in_dim, hidden_dim))
            if i == 0:
                layers.append(nn.LayerNorm(hidden_dim))  # LayerNorm after first layer only
            layers.append(nn.LeakyReLU())
            in_dim = hidden_dim
        self.backbone = nn.Sequential(*layers)

        # Stage-specific output heads
        self.heads = nn.ModuleList([
            nn.Linear(hidden_dim, output_dim) for _ in range(n_stages)
        ])

    def forward(self, x: torch.Tensor, stage_id: int) -> torch.Tensor:
        """
        Forward pass through shared backbone, then stage-specific head.

        Args:
            x: Input observation tensor [batch_size, input_dim]
            stage_id: Integer stage index (0-indexed); used to select output head

        Returns:
            Output tensor [batch_size, output_dim]
        """
        features = self.backbone(x)
        return self.heads[stage_id](features)


def compute_forward_transfer(
    success_rates: List[float],
    scratch_success_rates: List[float],
    T: int,
) -> float:
    """
    Compute forward transfer metric (Wołczyk et al., 2021).

    FT = (AUC - AUC_b) / (1 - AUC_b)
    AUC = (1/T) ∫₀ᵀ p(t) dt   (approximate with list of success rates)
    AUC_b = area under scratch baseline curve

    Args:
        success_rates: List of success rate values over training for fine-tuned model
        scratch_success_rates: List of success rate values for from-scratch baseline
        T: Total training steps

    Returns:
        Forward transfer scalar
    """
    dt = T / len(success_rates)
    auc = sum(success_rates) * dt / T
    auc_b = sum(scratch_success_rates) * dt / T
    if auc_b >= 1.0:
        return 0.0
    return (auc - auc_b) / (1.0 - auc_b)
