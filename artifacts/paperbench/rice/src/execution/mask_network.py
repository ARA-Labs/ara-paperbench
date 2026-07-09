"""
RICE: Optimized StateMask Mask Network Training (Algorithm 1)

Implements the simplified StateMask training where:
- Objective: J(θ) = max η(π̄)  [simplified from min|η(π) - η(π̄)| via Theorem 3.3]
- Modified reward: R'(s,a) = R(s,a) + α * a^m_t
- Optimizer: vanilla PPO (replaces primal-dual from original StateMask)

Key insight (Theorem 3.3): Under Assumption 3.1 (pre-trained policy > random),
η(π̄) ≤ η(π) always holds, so maximizing η(π̄) is equivalent to minimizing
|η(π) - η(π̄)| without the need for primal-dual optimization.
"""

import torch
import torch.nn as nn
from torch import Tensor
from typing import Tuple, Dict, Optional


class MaskNetwork(nn.Module):
    """
    Mask network ˜πθ that outputs binary importance scores for each state.
    
    Output a^m = 0 (critical step): preserve target agent's action.
    Output a^m = 1 (non-critical step): replace action with random action.
    
    The importance of a state is P(a^m = 0 | s) — probability of NOT blinding.
    """
    
    def __init__(
        self,
        state_dim: int,        # Dimension of state observation vector
        hidden_sizes: Tuple[int, ...] = (64, 64),
    ) -> None:
        """
        Initialize mask network with same architecture as target policy.
        
        Args:
            state_dim: Dimension of input state observation
            hidden_sizes: Tuple of hidden layer sizes
        """
        super().__init__()
        layers = []
        in_size = state_dim
        for h in hidden_sizes:
            layers += [nn.Linear(in_size, h), nn.Tanh()]
            in_size = h
        # Binary output: logits for {0=critical, 1=non-critical}
        layers.append(nn.Linear(in_size, 2))
        self.net = nn.Sequential(*layers)
    
    def forward(self, state: Tensor) -> Tensor:
        """
        Compute logits over binary mask actions.
        
        Args:
            state: Tensor of shape (batch_size, state_dim)
            
        Returns:
            logits: Tensor of shape (batch_size, 2)
                    logits[:, 0] = critical (preserve action)
                    logits[:, 1] = non-critical (randomize action)
        """
        return self.net(state)
    
    def get_importance_score(self, state: Tensor) -> Tensor:
        """
        Compute state importance score = P(a^m = 0 | s).
        Used to identify critical states in a trajectory.
        
        Args:
            state: Tensor of shape (batch_size, state_dim)
            
        Returns:
            importance: Tensor of shape (batch_size,), values in [0, 1]
        """
        logits = self.forward(state)
        probs = torch.softmax(logits, dim=-1)
        return probs[:, 0]  # P(a^m = 0 | s) = P(critical)


def compute_perturbed_action(
    target_action: Tensor,           # Action from pre-trained policy π: shape (batch, action_dim)
    mask_action: Tensor,             # Binary mask a^m: shape (batch,), 0=critical, 1=non-critical
    action_space_low: Tensor,        # Lower bound of action space: shape (action_dim,)
    action_space_high: Tensor,       # Upper bound of action space: shape (action_dim,)
) -> Tensor:
    """
    Compute the actual action taken by the perturbed policy π̄.
    
    a_t ⊙ a^m_t = a_t     if a^m_t = 0 (critical: preserve action)
                 = a_random if a^m_t = 1 (non-critical: randomize)
    
    Args:
        target_action: Action from pre-trained policy
        mask_action: Binary mask from mask network
        action_space_low: Lower bound of action space
        action_space_high: Upper bound of action space
        
    Returns:
        perturbed_action: Tensor of shape (batch, action_dim)
    """
    random_action = torch.rand_like(target_action) * (
        action_space_high - action_space_low
    ) + action_space_low
    
    is_non_critical = (mask_action == 1).float().unsqueeze(-1)  # (batch, 1)
    perturbed = (1 - is_non_critical) * target_action + is_non_critical * random_action
    return perturbed


def compute_mask_reward(
    task_reward: Tensor,   # Environment reward R(s, a): shape (batch,)
    mask_action: Tensor,   # Binary mask a^m: shape (batch,), 0=critical, 1=non-critical
    alpha: float = 0.0001, # Blinding bonus hyperparameter α (default from Table 3: all envs = 0.0001)
) -> Tensor:
    """
    Compute modified reward for mask network training.
    
    R'(s_t, a_t) = R(s_t, a_t) + α * a^m_t
    
    The bonus α * a^m_t encourages the mask to blind the agent (output 1)
    at non-critical steps, preventing the trivial solution of never blinding.
    
    Args:
        task_reward: Environment reward
        mask_action: Binary mask action from mask network
        alpha: Blinding bonus coefficient (low sensitivity; 0.0001 default for all envs)
        
    Returns:
        modified_reward: Tensor of shape (batch,)
    """
    return task_reward + alpha * mask_action.float()


def identify_critical_state(
    trajectory_states: Tensor,       # All states in trajectory: shape (T, state_dim)
    mask_net: MaskNetwork,           # Trained mask network
) -> Tuple[Tensor, int]:
    """
    Identify the most critical state in a trajectory using the trained mask network.
    
    The critical state is the one where P(a^m = 0 | s) is highest,
    i.e., the step the mask network deems most important to preserve.
    
    Args:
        trajectory_states: States from a trajectory rolled out by pre-trained policy π
        mask_net: Trained mask network ˜πθ
        
    Returns:
        critical_state: Tensor of shape (state_dim,)
        critical_idx: Index of critical state in trajectory
    """
    with torch.no_grad():
        importance_scores = mask_net.get_importance_score(trajectory_states)  # (T,)
    
    critical_idx = int(torch.argmax(importance_scores).item())
    critical_state = trajectory_states[critical_idx]
    return critical_state, critical_idx


def train_mask_network_step(
    mask_net: MaskNetwork,
    target_policy: nn.Module,       # Pre-trained DRL policy π (frozen weights)
    env,                            # OpenAI Gym-compatible environment
    ppo_optimizer,                  # PPO algorithm instance (e.g., from stable-baselines3)
    alpha: float = 0.0001,          # Blinding bonus (α); same value for all environments
    trajectory_length: int = 1000,  # Episode length T
) -> Dict[str, float]:
    """
    Perform one training iteration for the mask network (Algorithm 1).
    
    Steps:
    1. Reset environment, collect trajectory using π with mask perturbation
    2. Compute modified rewards R' = R + α * a^m
    3. Update mask network using PPO on collected data
    
    Args:
        mask_net: Mask network to train
        target_policy: Pre-trained policy π (NOT updated here)
        env: RL environment
        ppo_optimizer: PPO optimizer for the mask network
        alpha: Blinding bonus coefficient
        trajectory_length: Number of steps per episode
        
    Returns:
        metrics: Dict with 'mean_reward', 'mean_mask_ratio' (fraction of blinded steps)
    """
    states, mask_actions, modified_rewards = [], [], []
    
    obs = env.reset()
    for _ in range(trajectory_length):
        state_tensor = torch.FloatTensor(obs).unsqueeze(0)
        
        # Sample action from pre-trained policy π (frozen)
        with torch.no_grad():
            target_action = target_policy.predict(obs)
        
        # Sample mask action from mask network ˜πθ
        mask_logits = mask_net(state_tensor)
        mask_dist = torch.distributions.Categorical(logits=mask_logits)
        mask_act = mask_dist.sample().item()
        
        # Compute perturbed action
        if mask_act == 1:  # Non-critical: randomize
            action = env.action_space.sample()
        else:              # Critical: preserve
            action = target_action
        
        obs, reward, done, info = env.step(action)
        mod_reward = reward + alpha * mask_act
        
        states.append(state_tensor)
        mask_actions.append(mask_act)
        modified_rewards.append(mod_reward)
        
        if done:
            obs = env.reset()
    
    # Update mask network using PPO (implementation-dependent on PPO library)
    # ppo_optimizer.update(states, mask_actions, modified_rewards)
    
    return {
        'mean_reward': float(torch.tensor(modified_rewards).mean()),
        'mean_mask_ratio': float(sum(mask_actions) / len(mask_actions)),
    }
