"""
Forgetting of Pre-trained Capabilities (FPC) Analysis Utilities.

Implements tools for measuring, diagnosing, and visualizing FPC in RL fine-tuning:
- CKA-based representation drift measurement
- CLOSE/FAR state partitioning analysis
- Log-likelihood analysis of expert trajectories
- Forward Transfer metric computation

Paper: "Fine-tuning RL Models is Secretly a Forgetting Mitigation Problem"
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

import numpy as np
import torch
import torch.nn as nn
from torch import Tensor


# ---------------------------------------------------------------------------
# Central Kernel Alignment (CKA)
# ---------------------------------------------------------------------------

def linear_cka(
    X: Tensor,
    Y: Tensor,
) -> float:
    """
    Compute linear CKA between activation matrices X and Y.

    CKA(K, L) = HSIC(K, L) / sqrt(HSIC(K, K) * HSIC(L, L))

    where K = X @ X.T (linear kernel), L = Y @ Y.T.
    HSIC = Hilbert-Schmidt Independence Criterion (Gretton et al., 2005).

    Used to quantify representation drift in actor/critic during fine-tuning.
    Higher CKA → more similar representations.

    Args:
        X: Activations from pre-trained model; shape (N, p1) where N = number of samples
        Y: Activations from fine-tuned model; shape (N, p2)

    Returns:
        CKA value in [0, 1]
    """
    X = X - X.mean(0)  # center
    Y = Y - Y.mean(0)  # center

    # Linear kernel matrices
    K = X @ X.T  # (N, N)
    L = Y @ Y.T  # (N, N)

    def hsic(A: Tensor, B: Tensor) -> float:
        n = A.shape[0]
        # Centering matrix H = I - 11^T/n
        H = torch.eye(n, device=A.device) - torch.ones(n, n, device=A.device) / n
        return (torch.trace(A @ H @ B @ H) / ((n - 1) ** 2)).item()

    hsic_kl = hsic(K, L)
    hsic_kk = hsic(K, K)
    hsic_ll = hsic(L, L)

    if hsic_kk == 0 or hsic_ll == 0:
        return 0.0
    return hsic_kl / (hsic_kk * hsic_ll) ** 0.5


# ---------------------------------------------------------------------------
# Log-likelihood Analysis (push-wall / FAR state evaluation)
# ---------------------------------------------------------------------------

def compute_expert_log_likelihood(
    policy: nn.Module,
    expert_trajectories: List[Tuple[Tensor, Tensor]],
    device: torch.device = torch.device("cpu"),
) -> Tensor:
    """
    Compute log-likelihood of expert state-action pairs under the current policy.

    Used to track forgetting: L(θ) = E_{(s,a*)~π*}[log π_θ(a*|s)]

    For RoboticSequence push-wall experiment: computed every 50K training steps.
    Visualized via 2D PCA projections (Figure 8).

    Args:
        policy: Current fine-tuned policy π_θ
        expert_trajectories: List of (states, expert_actions) tuples from π*
        device: Computation device

    Returns:
        Per-state log-likelihoods; shape (N,)
    """
    policy.eval()
    all_log_probs = []

    with torch.no_grad():
        for states, expert_actions in expert_trajectories:
            states = states.to(device)
            expert_actions = expert_actions.to(device)

            # Determine action space type from policy output
            output = policy(states)
            if isinstance(output, tuple) and len(output) == 2:
                # Continuous (Gaussian) policy: output is (mu, log_std)
                mu, log_std = output
                sigma = log_std.exp()
                dist = torch.distributions.Normal(mu, sigma)
                expert_log_probs = dist.log_prob(expert_actions).sum(dim=-1)
            else:
                # Discrete policy: output is logits
                logits = output
                log_probs = torch.nn.functional.log_softmax(logits, dim=-1)
                expert_log_probs = log_probs.gather(
                    1, expert_actions.long().unsqueeze(-1)
                ).squeeze(-1)

            all_log_probs.append(expert_log_probs)

    return torch.cat(all_log_probs, dim=0)


def compute_pca_log_likelihoods(
    policy: nn.Module,
    expert_trajectories: List[Tuple[Tensor, Tensor]],
    checkpoints: List[str],
    device: torch.device = torch.device("cpu"),
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute 2D PCA projections of per-state log-likelihoods across training checkpoints.

    For each checkpoint, loads the policy weights and computes per-state log-likelihoods
    on the push-wall expert trajectories. The resulting (n_checkpoints, n_states) matrix
    is then projected to 2D via PCA for visualization (Figure 8).

    Args:
        policy: Policy network (weights will be overwritten per checkpoint)
        expert_trajectories: (states, actions) tuples from π* on push-wall
        checkpoints: List of checkpoint file paths (ordered by training step)
        device: Computation device

    Returns:
        (pca_2d, log_lik_matrix):
            pca_2d: (n_checkpoints, 2) PCA-projected log-likelihoods
            log_lik_matrix: (n_checkpoints, n_states) raw log-likelihoods
    """
    from sklearn.decomposition import PCA

    log_lik_matrix = []
    for ckpt_path in checkpoints:
        state_dict = torch.load(ckpt_path, map_location=device)
        policy.load_state_dict(state_dict)
        log_liks = compute_expert_log_likelihood(policy, expert_trajectories, device)
        log_lik_matrix.append(log_liks.cpu().numpy())

    log_lik_matrix = np.stack(log_lik_matrix)  # (n_checkpoints, n_states)
    pca = PCA(n_components=2)
    pca_2d = pca.fit_transform(log_lik_matrix)  # (n_checkpoints, 2)
    return pca_2d, log_lik_matrix


# ---------------------------------------------------------------------------
# Forward Transfer Metric
# ---------------------------------------------------------------------------

def forward_transfer(
    finetuned_success_rates: np.ndarray,
    scratch_success_rates: np.ndarray,
    dt: float = 1.0,
) -> float:
    """
    Compute Forward Transfer metric.

    FT = (AUC_finetuned - AUC_scratch) / (1 - AUC_scratch)
    AUC = (1/T) * integral_0^T p(t) dt

    Measures how much faster fine-tuning learns than training from scratch.
    Range: negative (worse than scratch) to 1.0 (perfect immediate transfer).

    Used in Table 6 (RoboticSequence prefix task ablation).

    Args:
        finetuned_success_rates: p(t) for fine-tuned model; shape (T,)
        scratch_success_rates: p_b(t) for scratch model; shape (T,)
        dt: Time step size

    Returns:
        Forward transfer value (can be negative)
    """
    T = len(finetuned_success_rates)
    auc = np.trapz(finetuned_success_rates, dx=dt) / T
    auc_b = np.trapz(scratch_success_rates, dx=dt) / T

    if auc_b >= 1.0:
        return 0.0
    return (auc - auc_b) / (1.0 - auc_b)


# ---------------------------------------------------------------------------
# RoboticSequence Augmented Reward
# ---------------------------------------------------------------------------

def augmented_success_reward(
    base_reward: float,
    timestep: int,
    max_steps: int = 200,
    beta: float = 1.5,
) -> float:
    """
    Augmented reward for early success in RoboticSequence.

    r'_t = β * r_t * (T - t)

    Provides "remaining" reward to prevent policy from avoiding early termination.

    Args:
        base_reward: Original reward r_t at success timestep
        timestep: Current timestep t
        max_steps: Maximum episode length T (default: 200)
        beta: Scaling coefficient β (default: 1.5)

    Returns:
        Augmented reward r'_t
    """
    return beta * base_reward * (max_steps - timestep)


# ---------------------------------------------------------------------------
# CLOSE/FAR State Partitioning (Diagnostic)
# ---------------------------------------------------------------------------

def estimate_far_visitation_rate(
    trajectory_states: List[Tensor],
    far_classifier,  # callable: state → bool (True if FAR state)
) -> float:
    """
    Estimate what fraction of trajectory states are FAR states.

    Used to diagnose severity of CLOSE/FAR imbalance during early fine-tuning.
    Low FAR visitation rate → high FPC risk.

    Args:
        trajectory_states: List of state tensors from episode(s)
        far_classifier: Function returning True for FAR states

    Returns:
        Fraction of states classified as FAR (in [0, 1])
    """
    total = 0
    far_count = 0
    for state in trajectory_states:
        total += 1
        if far_classifier(state):
            far_count += 1
    return far_count / max(total, 1)
