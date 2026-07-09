"""
Prior Reward Distribution for FRE.

Implements the three random unsupervised reward families from Section 4.2:
  1. GoalReachingRewardFunction  -- singleton goal-reaching rewards
  2. LinearRewardFunction        -- random sparse linear reward functions
  3. RandomRewardFunction        -- random 2-layer MLP reward functions

All classes implement the RewardFunction interface:
  generate_params_and_pairs(traj_states, random_states, random_states_decode)
    -> (params, encode_pairs, decode_pairs, rewards, masks)
  compute_reward(states, params) -> rewards

Implementation: NumPy (CPU; called during data sampling in training loop)
"""

import numpy as np
from typing import Tuple, Optional, List


class RewardFunction:
    """Base class for all reward functions."""

    def generate_params_and_pairs(
        self,
        traj_states: np.ndarray,         # [batch, traj_len, obs_dim]
        random_states: np.ndarray,       # [batch, n_random, obs_dim]
        random_states_decode: np.ndarray,  # [batch, K', obs_dim]
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Sample reward function params and generate (state, reward) pairs.

        Returns:
            params:          [batch, param_dim] -- reward function parameters
            encode_pairs:    [batch, K, obs_dim + 1] -- (state, reward) for encoder
            decode_pairs:    [batch, K', obs_dim + 1] -- (state, reward) for decoder
            rewards:         [batch] -- reward for current state (first in traj)
            masks:           [batch] -- done mask (1 if not done, 0 if done)
        """
        raise NotImplementedError

    def compute_reward(
        self,
        states: np.ndarray,   # [batch, obs_dim] or [batch, pairs, obs_dim]
        params: np.ndarray,   # [batch, param_dim] or [batch, 1, param_dim]
    ) -> np.ndarray:          # [batch] or [batch, pairs]
        raise NotImplementedError

    def make_encoder_pairs_testing(
        self,
        params: np.ndarray,         # [batch, param_dim]
        random_states: np.ndarray,  # [batch, K, obs_dim]
    ) -> np.ndarray:                # [batch, K, obs_dim + 1]
        """Construct encoder pairs for test-time task encoding."""
        raise NotImplementedError


class GoalReachingRewardFunction(RewardFunction):
    """
    Singleton goal-reaching rewards.

    Reward: -1 at every timestep until goal reached, 0 at goal.
    Goal selection uses hindsight relabeling (HER-style, Andrychowicz et al. 2017):
      - p=0.2: current state is goal
      - p=0.5: random future state within trajectory
      - p=0.3: completely random state from dataset

    Goal reaching criterion (per environment):
      - AntMaze (obs_dim=29): L2 distance of XY < 2.0
      - Cheetah (obs_dim=18): normalized L2 < 0.08 (with per-dim std normalization)
      - Walker  (obs_dim=27): normalized L2 < 0.2  (with per-dim std normalization)
      - Kitchen (obs_dim=30): L2 / obs_dim < 1e-6

    At test time: ensure goal state is included in the encoder context set.
    """
    p_current: float = 0.2
    p_trajectory: float = 0.5
    p_random: float = 0.3

    def __init__(self, obs_dim: int = 29, state_std: Optional[np.ndarray] = None):
        """
        Args:
            obs_dim: observation dimensionality, used to determine environment type.
            state_std: [obs_dim] per-dimension standard deviation for normalization
                       (required for ExORL cheetah/walker).
        """
        self.obs_dim = obs_dim
        self.state_std = state_std

        # Determine environment-specific thresholds
        if obs_dim == 29:
            # AntMaze: L2 distance of XY (first 2 dims)
            self.threshold = 2.0
            self.env_type = "antmaze"
        elif obs_dim == 18:
            # ExORL cheetah: normalized L2
            self.threshold = 0.08
            self.env_type = "cheetah"
        elif obs_dim == 27:
            # ExORL walker: normalized L2
            self.threshold = 0.2
            self.env_type = "walker"
        elif obs_dim == 30:
            # Kitchen: L2 / obs_dim
            self.threshold = 1e-6
            self.env_type = "kitchen"
        else:
            # Default: treat as generic goal reaching with L2 threshold 2.0
            self.threshold = 2.0
            self.env_type = "generic"

    def compute_reward(self, states, params):
        """
        params: [batch, obs_dim] -- goal state (or [batch, 1, obs_dim] for paired states)
        states: [batch, obs_dim] or [batch, K, obs_dim]
        Returns reward: [batch] or [batch, K] in {-1, 0}
        """
        # Handle broadcasting: if params has fewer dims, expand
        if params.ndim == 2 and states.ndim == 3:
            # params [batch, obs_dim] -> [batch, 1, obs_dim]
            params = params[:, np.newaxis, :]

        if self.env_type == "antmaze":
            # L2 distance in XY space (first 2 dimensions)
            diff = states[..., :2] - params[..., :2]
            dist = np.sqrt(np.sum(diff ** 2, axis=-1))
            reached = dist < self.threshold
        elif self.env_type in ("cheetah", "walker"):
            # Normalized L2 distance (normalize by per-dim std)
            if self.state_std is not None:
                std = self.state_std + 1e-8
                diff = (states - params) / std
            else:
                diff = states - params
            dist = np.sqrt(np.mean(diff ** 2, axis=-1))
            reached = dist < self.threshold
        elif self.env_type == "kitchen":
            # L2 / obs_dim
            diff = states - params
            dist = np.sqrt(np.sum(diff ** 2, axis=-1)) / self.obs_dim
            reached = dist < self.threshold
        else:
            # Generic: full L2 distance
            diff = states - params
            dist = np.sqrt(np.sum(diff ** 2, axis=-1))
            reached = dist < self.threshold

        # Reward: 0 if reached, -1 otherwise
        reward = np.where(reached, 0.0, -1.0)
        return reward

    def generate_params_and_pairs(
        self,
        traj_states: np.ndarray,         # [batch, traj_len, obs_dim]
        random_states: np.ndarray,       # [batch, n_random, obs_dim]
        random_states_decode: np.ndarray,  # [batch, K', obs_dim]
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        HER-style goal selection:
          p=0.2 current state (random from trajectory)
          p=0.5 future state in trajectory
          p=0.3 completely random state from dataset

        Generate K=32 encoder pairs and K' decoder pairs.
        """
        batch_size = traj_states.shape[0]
        traj_len = traj_states.shape[1]
        obs_dim = traj_states.shape[2]
        K = random_states.shape[1]  # num encoder pairs
        K_prime = random_states_decode.shape[1]  # num decoder pairs

        # Select goals using HER-style sampling
        goals = np.zeros((batch_size, obs_dim), dtype=np.float32)
        r = np.random.random(batch_size)

        for i in range(batch_size):
            if r[i] < self.p_current:
                # Current: random state from trajectory
                idx = np.random.randint(traj_len)
                goals[i] = traj_states[i, idx]
            elif r[i] < self.p_current + self.p_trajectory:
                # Future: random future state in trajectory
                # Pick a random starting index, then pick a future state
                start_idx = np.random.randint(traj_len)
                future_idx = np.random.randint(start_idx, traj_len)
                goals[i] = traj_states[i, future_idx]
            else:
                # Random: completely random state from the random_states pool
                idx = np.random.randint(K)
                goals[i] = random_states[i, idx]

        # params = goal states [batch, obs_dim]
        params = goals

        # Compute rewards for encoder states
        encode_rewards = self.compute_reward(random_states, params)  # [batch, K]
        encode_pairs = np.concatenate(
            [random_states, encode_rewards[..., np.newaxis]], axis=-1
        )  # [batch, K, obs_dim + 1]

        # Compute rewards for decoder states
        decode_rewards = self.compute_reward(random_states_decode, params)  # [batch, K']
        decode_pairs = np.concatenate(
            [random_states_decode, decode_rewards[..., np.newaxis]], axis=-1
        )  # [batch, K', obs_dim + 1]

        # Reward for the current state (first state of trajectory)
        current_state = traj_states[:, 0, :]  # [batch, obs_dim]
        rewards = self.compute_reward(current_state, params)  # [batch]

        # Mask: 0 if goal reached (done), 1 if not
        masks = np.where(rewards == 0.0, 0.0, 1.0)

        return params, encode_pairs, decode_pairs, rewards, masks

    def make_encoder_pairs_testing(
        self,
        params: np.ndarray,         # [batch, param_dim=obs_dim] -- goal state
        random_states: np.ndarray,  # [batch, K, obs_dim]
    ) -> np.ndarray:                # [batch, K, obs_dim + 1]
        """Construct encoder pairs for test-time task encoding."""
        # Compute reward for each random_state given the goal (params)
        rewards = self.compute_reward(random_states, params)  # [batch, K]
        # Concatenate [state, reward]
        pairs = np.concatenate(
            [random_states, rewards[..., np.newaxis]], axis=-1
        )  # [batch, K, obs_dim + 1]
        return pairs


class LinearRewardFunction(RewardFunction):
    """
    Random sparse linear reward functions.

    r(s) = clip(dot(w, s), -1, 1)  (when clip_bit=True) or dot(w, s) clipped to [-1, 1]
    where w in R^obs_dim is a random vector with:
      - w_i ~ Uniform(-1, 1) for each dimension
      - w_i = 0 with probability 0.9 (sparse mask)
      - at least one dimension is forced non-zero
      - XY dimensions masked to 0 for AntMaze (to avoid scale instability)
      - Auxiliary physics dimensions masked to 0 for DMC environments

    Clipping: 50% probability of clipping to [0, 1] (clip_bit=True) vs [-1, 1]
    """

    def __init__(
        self,
        obs_dim: int = 29,
        exclude_dims: Optional[List[int]] = None,
        sparsity_prob: float = 0.9,
    ):
        """
        Args:
            obs_dim: observation dimensionality.
            exclude_dims: dimensions to exclude from linear reward (set to 0).
                          For AntMaze: [0, 1] (XY positions).
            sparsity_prob: probability of zeroing each dimension (default 0.9).
        """
        self.obs_dim = obs_dim
        self.exclude_dims = exclude_dims if exclude_dims is not None else []
        self.sparsity_prob = sparsity_prob

    def _sample_weights(self, batch_size: int) -> Tuple[np.ndarray, np.ndarray]:
        """
        Sample random sparse linear weight vectors and clip bits.

        Returns:
            weights: [batch, obs_dim]
            clip_bits: [batch] in {0, 1}
        """
        # Sample weights ~ Uniform(-1, 1)
        w = np.random.uniform(-1.0, 1.0, size=(batch_size, self.obs_dim)).astype(np.float32)

        # Apply sparse mask: zero with probability sparsity_prob
        mask = (np.random.random((batch_size, self.obs_dim)) > self.sparsity_prob).astype(np.float32)
        w = w * mask

        # Ensure at least one dimension is non-zero per sample
        for i in range(batch_size):
            if np.sum(np.abs(w[i])) < 1e-10:
                forced_dim = np.random.randint(self.obs_dim)
                # Skip excluded dims
                while forced_dim in self.exclude_dims and len(self.exclude_dims) < self.obs_dim:
                    forced_dim = np.random.randint(self.obs_dim)
                w[i, forced_dim] = np.random.uniform(-1.0, 1.0)

        # Exclude specified dimensions
        for d in self.exclude_dims:
            w[:, d] = 0.0

        # 50% probability of clipping to [0,1] vs [-1,1]
        clip_bits = (np.random.random(batch_size) > 0.5).astype(np.float32)

        return w, clip_bits

    def compute_reward(self, states, params):
        """
        params: [batch, obs_dim + 1] -- last element is clip_bit (0 or 1)
                or [batch, 1, obs_dim + 1] for paired computation
        r = clip(dot(w, s), [0,1] if clip_bit else [-1,1])
        """
        if params.ndim == 3:
            # params [batch, 1, obs_dim+1], states [batch, K, obs_dim]
            w = params[..., :-1]          # [batch, 1, obs_dim]
            clip_bit = params[..., -1:]   # [batch, 1, 1] or [batch, 1]

            # dot product along last dim
            r = np.sum(w * states, axis=-1)  # [batch, K]

            # Clip based on clip_bit
            clip_bit_expanded = clip_bit.squeeze(-1) if clip_bit.ndim == 3 else clip_bit
            # clip_bit [batch, 1] broadcast to [batch, K]
            r = np.where(
                clip_bit_expanded > 0.5,
                np.clip(r, 0.0, 1.0),
                np.clip(r, -1.0, 1.0),
            )
        elif states.ndim == 3:
            # params [batch, obs_dim+1], states [batch, K, obs_dim]
            w = params[:, :-1]           # [batch, obs_dim]
            clip_bit = params[:, -1]     # [batch]

            # Expand w for batch multiplication
            r = np.sum(w[:, np.newaxis, :] * states, axis=-1)  # [batch, K]

            # Clip based on clip_bit
            r = np.where(
                clip_bit[:, np.newaxis] > 0.5,
                np.clip(r, 0.0, 1.0),
                np.clip(r, -1.0, 1.0),
            )
        else:
            # params [batch, obs_dim+1], states [batch, obs_dim]
            w = params[:, :-1]           # [batch, obs_dim]
            clip_bit = params[:, -1]     # [batch]

            r = np.sum(w * states, axis=-1)  # [batch]

            r = np.where(
                clip_bit > 0.5,
                np.clip(r, 0.0, 1.0),
                np.clip(r, -1.0, 1.0),
            )

        return r

    def generate_params_and_pairs(
        self,
        traj_states: np.ndarray,         # [batch, traj_len, obs_dim]
        random_states: np.ndarray,       # [batch, n_random, obs_dim]
        random_states_decode: np.ndarray,  # [batch, K', obs_dim]
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Sample linear reward params and generate (state, reward) pairs."""
        batch_size = traj_states.shape[0]

        # Sample weights and clip bits
        w, clip_bits = self._sample_weights(batch_size)

        # params = [w, clip_bit] -> [batch, obs_dim + 1]
        params = np.concatenate([w, clip_bits[:, np.newaxis]], axis=-1).astype(np.float32)

        # Compute encoder rewards
        encode_rewards = self.compute_reward(random_states, params)  # [batch, K]
        encode_pairs = np.concatenate(
            [random_states, encode_rewards[..., np.newaxis]], axis=-1
        )  # [batch, K, obs_dim + 1]

        # Compute decoder rewards
        decode_rewards = self.compute_reward(random_states_decode, params)  # [batch, K']
        decode_pairs = np.concatenate(
            [random_states_decode, decode_rewards[..., np.newaxis]], axis=-1
        )  # [batch, K', obs_dim + 1]

        # Reward for current state
        current_state = traj_states[:, 0, :]  # [batch, obs_dim]
        rewards = self.compute_reward(current_state, params)  # [batch]

        # Linear rewards never terminate, mask=1 always
        masks = np.ones(batch_size, dtype=np.float32)

        return params, encode_pairs, decode_pairs, rewards, masks

    def make_encoder_pairs_testing(
        self,
        params: np.ndarray,         # [batch, param_dim=obs_dim+1]
        random_states: np.ndarray,  # [batch, K, obs_dim]
    ) -> np.ndarray:                # [batch, K, obs_dim + 1]
        """Construct encoder pairs for test-time task encoding."""
        rewards = self.compute_reward(random_states, params)  # [batch, K]
        pairs = np.concatenate(
            [random_states, rewards[..., np.newaxis]], axis=-1
        )  # [batch, K, obs_dim + 1]
        return pairs


class RandomRewardFunction(RewardFunction):
    """
    Random 2-layer MLP reward functions.

    Architecture: state_dim -> 32 -> 1 (with tanh activation)
    Parameters initialized with scaled normal distribution:
      - W1: shape (obs_dim, 32), scale = sqrt(1/32)
      - b1: shape (1, 32),       scale = sqrt(16)
      - W2: shape (32, 1),       scale = sqrt(1/16)
    Output clipped to [-1, 1].

    Pre-computed parameter matrices for num_simplex=256 random MLPs.
    Auxiliary physics dimensions zeroed out for DMC environments.

    r(s; idx) = clip(tanh(s @ W1[idx] + b1[idx]) @ W2[idx], -1, 1)
    """

    def __init__(
        self,
        num_simplex: int = 256,
        obs_len: int = 29,
        zero_dims: Optional[List[int]] = None,
    ):
        """
        Pre-compute num_simplex random MLP parameter sets.
        Random seed for parameter generation: np.random.RandomState(0)

        Args:
            num_simplex: number of pre-computed random MLPs (default 256).
            obs_len: observation dimensionality.
            zero_dims: dimensions to zero out in W1 (e.g., auxiliary physics dims for DMC).
        """
        self.num_simplex = num_simplex
        self.obs_len = obs_len

        rng = np.random.RandomState(0)

        hidden_dim = 32

        # W1: (num_simplex, obs_len, 32), scale = sqrt(1/32)
        scale_w1 = np.sqrt(1.0 / hidden_dim)
        self.W1 = (rng.randn(num_simplex, obs_len, hidden_dim) * scale_w1).astype(np.float32)

        # b1: (num_simplex, 1, 32), scale = sqrt(16)
        scale_b1 = np.sqrt(16.0)
        self.b1 = (rng.randn(num_simplex, 1, hidden_dim) * scale_b1).astype(np.float32)

        # W2: (num_simplex, 32, 1), scale = sqrt(1/16)
        scale_w2 = np.sqrt(1.0 / 16.0)
        self.W2 = (rng.randn(num_simplex, hidden_dim, 1) * scale_w2).astype(np.float32)

        # Zero out specified dimensions in W1
        if zero_dims is not None:
            for d in zero_dims:
                self.W1[:, d, :] = 0.0

    def compute_reward(self, states, params):
        """
        params: [batch, 1] integer index into pre-computed MLP bank
                or [batch] integer index
        states: [batch, obs_dim] or [batch, K, obs_dim]
        r = clip(tanh(states @ W1[idx] + b1[idx]) @ W2[idx], -1, 1)
        """
        # Extract integer indices
        if params.ndim == 2:
            idx = params[:, 0].astype(int)  # [batch]
        else:
            idx = params.astype(int)  # [batch]

        batch_size = states.shape[0]

        if states.ndim == 3:
            # states [batch, K, obs_dim]
            K = states.shape[1]
            rewards = np.zeros((batch_size, K), dtype=np.float32)
            for i in range(batch_size):
                # s @ W1[idx] + b1[idx]  -> [K, 32]
                h = np.tanh(states[i] @ self.W1[idx[i]] + self.b1[idx[i]])  # [K, 32]
                r = h @ self.W2[idx[i]]  # [K, 1]
                rewards[i] = np.clip(r.squeeze(-1), -1.0, 1.0)
        else:
            # states [batch, obs_dim]
            rewards = np.zeros(batch_size, dtype=np.float32)
            for i in range(batch_size):
                s = states[i:i+1]  # [1, obs_dim]
                h = np.tanh(s @ self.W1[idx[i]] + self.b1[idx[i]])  # [1, 32]
                r = h @ self.W2[idx[i]]  # [1, 1]
                rewards[i] = np.clip(r.item(), -1.0, 1.0)

        return rewards

    def generate_params_and_pairs(
        self,
        traj_states: np.ndarray,         # [batch, traj_len, obs_dim]
        random_states: np.ndarray,       # [batch, n_random, obs_dim]
        random_states_decode: np.ndarray,  # [batch, K', obs_dim]
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Sample random MLP indices and generate (state, reward) pairs."""
        batch_size = traj_states.shape[0]

        # Sample random MLP indices
        idx = np.random.randint(0, self.num_simplex, size=(batch_size, 1)).astype(np.float32)

        # params = [batch, 1] integer index
        params = idx

        # Compute encoder rewards
        encode_rewards = self.compute_reward(random_states, params)  # [batch, K]
        encode_pairs = np.concatenate(
            [random_states, encode_rewards[..., np.newaxis]], axis=-1
        )  # [batch, K, obs_dim + 1]

        # Compute decoder rewards
        decode_rewards = self.compute_reward(random_states_decode, params)  # [batch, K']
        decode_pairs = np.concatenate(
            [random_states_decode, decode_rewards[..., np.newaxis]], axis=-1
        )  # [batch, K', obs_dim + 1]

        # Reward for current state
        current_state = traj_states[:, 0, :]  # [batch, obs_dim]
        rewards = self.compute_reward(current_state, params)  # [batch]

        # MLP rewards never terminate, mask=1 always
        masks = np.ones(batch_size, dtype=np.float32)

        return params, encode_pairs, decode_pairs, rewards, masks

    def make_encoder_pairs_testing(
        self,
        params: np.ndarray,         # [batch, param_dim=1] -- MLP index
        random_states: np.ndarray,  # [batch, K, obs_dim]
    ) -> np.ndarray:                # [batch, K, obs_dim + 1]
        """Construct encoder pairs for test-time task encoding."""
        rewards = self.compute_reward(random_states, params)  # [batch, K]
        pairs = np.concatenate(
            [random_states, rewards[..., np.newaxis]], axis=-1
        )  # [batch, K, obs_dim + 1]
        return pairs


def sample_reward_function(
    rew_ratio_goal: float = 0.3333,
    rew_ratio_linear: float = 0.3333,
    rew_ratio_mlp: float = 0.3333,
    goal_fn: GoalReachingRewardFunction = None,
    linear_fn: LinearRewardFunction = None,
    mlp_fn: RandomRewardFunction = None,
) -> RewardFunction:
    """
    Sample a reward function from the prior distribution p(eta).

    FRE-all: uniform mixture of three families.
    FRE-goals: only goal-reaching (rew_ratio_goal=1.0, others=0).
    FRE-lin:   only linear (rew_ratio_linear=1.0).
    FRE-mlp:   only MLP (rew_ratio_mlp=1.0).
    FRE-lin-mlp: equal 0.5/0.5 linear and MLP.
    FRE-goal-mlp: equal 0.5/0.5 goal and MLP.
    FRE-goal-lin: equal 0.5/0.5 goal and linear.
    FRE-hint: domain-specific rewards added (e.g., velocity for DMC).
    """
    r = np.random.random()
    if r < rew_ratio_goal:
        return goal_fn
    elif r < rew_ratio_goal + rew_ratio_linear:
        return linear_fn
    else:
        return mlp_fn
