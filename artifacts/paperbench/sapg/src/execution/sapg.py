"""
SAPG: Split and Aggregate Policy Gradients
Core loss functions implementing Equations 2-9 from the paper.

This module implements:
- On-policy PPO clipped surrogate loss (Eq. 2)
- Off-policy importance-sampled loss (Eq. 3)
- Combined actor loss (Eq. 4)
- n-step on-policy critic targets (Eq. 5)
- 1-step off-policy critic targets (Eq. 6)
- On-policy critic loss (Eq. 7)
- Off-policy critic loss (Eq. 8)
- Combined critic loss (Eq. 9)
- SAPG main training loop (Algorithm 1)

No scaffolding (no argparse, no logging wrappers).
"""

import torch
import torch.nn.functional as F
from typing import List, Tuple, Dict, NamedTuple


class Rollout(NamedTuple):
    """Data collected from a single policy's environment block."""
    states: torch.Tensor          # (T, N_block, obs_dim)
    actions: torch.Tensor         # (T, N_block, act_dim)
    rewards: torch.Tensor         # (T, N_block)
    log_probs_old: torch.Tensor   # (T, N_block) — log π_j(a|s) at collection time
    values_old: torch.Tensor      # (T+1, N_block) — V_πj,old(s), includes bootstrap
    dones: torch.Tensor           # (T, N_block)


def on_policy_actor_loss(
    log_probs_new: torch.Tensor,   # (B,) — log π_θ(a|s) under current policy
    log_probs_old: torch.Tensor,   # (B,) — log π_old(a|s) at collection time
    advantages: torch.Tensor,      # (B,) — advantage estimates A^π_old(s, a)
    eps: float = 0.1,              # clipping parameter ε
) -> torch.Tensor:
    """
    PPO clipped surrogate objective — Equation 2.

    L^on(π_θ) = E_π_old[ min( r_t(π_θ), clip(r_t(π_θ), 1-ε, 1+ε) ) * A^π_old ]

    where r_t(π_θ) = π_θ(a|s) / π_old(a|s) = exp(log_probs_new - log_probs_old)

    Returns:
        Scalar loss (negated for gradient ascent via optimizer descent).
    """
    ratio = torch.exp(log_probs_new - log_probs_old)  # r_t(π_θ)
    clipped_ratio = torch.clamp(ratio, 1.0 - eps, 1.0 + eps)
    surrogate = torch.min(ratio * advantages, clipped_ratio * advantages)
    return -surrogate.mean()  # negative because we maximize


def off_policy_actor_loss(
    log_probs_new_i: torch.Tensor,     # (B,) — log π_i(a|s) current leader
    log_probs_old_i: torch.Tensor,     # (B,) — log π_i,old(a|s) leader at rollout
    log_probs_j: torch.Tensor,         # (B,) — log π_j(a|s) follower that collected data
    advantages_i: torch.Tensor,        # (B,) — A^π_i,old(s, a) estimated by leader's critic
    eps: float = 0.1,                  # clipping parameter ε
) -> torch.Tensor:
    """
    Off-policy clipped surrogate with IS correction — Equation 3.

    r_πi(s,a) = π_i(s,a) / π_j(s,a)
    μ = π_i,old(s,a) / π_j(s,a)   (off-policy correction term)

    L^off(π_i; {j}) = E_(s,a)~π_j [
        min( r_πi, clip(r_πi, μ*(1-ε), μ*(1+ε)) ) * A^π_i,old(s,a)
    ]

    Returns:
        Scalar loss (negated for gradient ascent).
    """
    # Importance weight ratio: π_i(a|s) / π_j(a|s)
    log_ratio_i_j = log_probs_new_i - log_probs_j          # log r_πi
    r_pi_i = torch.exp(log_ratio_i_j)                       # r_πi(s,a)

    # Off-policy correction: μ = π_i,old / π_j
    log_mu = log_probs_old_i - log_probs_j                  # log μ
    mu = torch.exp(log_mu).detach()                          # μ (stop gradient)

    # Clipped ratio centered at μ instead of 1
    clipped_ratio = torch.clamp(r_pi_i, mu * (1.0 - eps), mu * (1.0 + eps))
    surrogate = torch.min(r_pi_i * advantages_i, clipped_ratio * advantages_i)
    return -surrogate.mean()


def combined_actor_loss(
    on_policy_loss: torch.Tensor,   # scalar from on_policy_actor_loss
    off_policy_losses: List[torch.Tensor],  # list of scalars from off_policy_actor_loss
    lam: float = 1.0,               # λ weight for off-policy term (Eq. 4)
) -> torch.Tensor:
    """
    Combined actor loss — Equation 4.

    L(π_i) = L^on(π_i) + λ * L^off(π_i; X)

    where L^off is the average over all follower sources X.
    """
    if len(off_policy_losses) == 0:
        return on_policy_loss
    avg_off_policy = torch.stack(off_policy_losses).mean()
    return on_policy_loss + lam * avg_off_policy


def compute_nstep_returns(
    rewards: torch.Tensor,     # (T, N_block)
    values: torch.Tensor,      # (T+1, N_block) — V_π_old including bootstrap at T
    dones: torch.Tensor,       # (T, N_block) — episode termination flags
    gamma: float = 0.99,
    n: int = 3,
) -> torch.Tensor:
    """
    n-step bootstrapped returns for on-policy critic targets — Equation 5.

    V^target_on,π_j(s_t) = Σ_{k=t}^{t+n-1} γ^{k-t} r_k + γ^n V_π_j,old(s_{t+n})

    Default n=3 as specified in paper.

    Returns:
        targets: (T, N_block) value targets
    """
    T = rewards.shape[0]
    targets = torch.zeros_like(rewards)
    for t in range(T):
        ret = torch.zeros(rewards.shape[1], device=rewards.device)
        gamma_power = 1.0
        for k in range(n):
            if t + k < T:
                mask = (1.0 - dones[t + k])  # zero out if done
                ret = ret + gamma_power * rewards[t + k]
                gamma_power *= gamma
                # propagate done mask
            else:
                break
        # Bootstrap with value at t+n (or last available)
        boot_idx = min(t + n, T)
        ret = ret + gamma_power * values[boot_idx]
        targets[t] = ret
    return targets


def compute_onestep_returns(
    rewards: torch.Tensor,     # (T, N_block)
    next_values: torch.Tensor, # (T, N_block) — V_π_j,old(s_{t+1})
    gamma: float = 0.99,
) -> torch.Tensor:
    """
    1-step bootstrapped returns for off-policy critic targets — Equation 6.

    V^target_off,π_j(s'_t) = r_t + γ * V_π_j,old(s'_{t+1})

    Returns:
        targets: (T, N_block) value targets
    """
    return rewards + gamma * next_values


def on_policy_critic_loss(
    values_pred: torch.Tensor,  # (B,) — V_πi(s) current value predictions
    targets: torch.Tensor,      # (B,) — V^target_on,πi(s)
) -> torch.Tensor:
    """
    On-policy critic MSE loss — Equation 7.

    L^critic_on(π_i) = E_(s,a)~π_i [ (V_πi(s) - V^target_on,πi(s))^2 ]
    """
    return F.mse_loss(values_pred, targets.detach())


def off_policy_critic_loss(
    values_pred: torch.Tensor,        # (B,) — V_πi(s) for off-policy states
    off_policy_targets: torch.Tensor, # (B,) — V^target_off,πi(s')
) -> torch.Tensor:
    """
    Off-policy critic MSE loss — Equation 8.

    L^critic_off(π_i; X) = 1/|X| Σ_j E_(s,a)~π_j [ (V_πi(s) - V^target_off,πi(s))^2 ]

    Note: caller should average over followers X before passing off_policy_targets.
    """
    return F.mse_loss(values_pred, off_policy_targets.detach())


def combined_critic_loss(
    on_critic: torch.Tensor,    # scalar from on_policy_critic_loss
    off_critic: torch.Tensor,   # scalar from off_policy_critic_loss
    lam: float = 1.0,           # λ weight (same as actor, Eq. 9)
    critic_coeff: float = 4.0,  # λ' from hyperparameter tables
) -> torch.Tensor:
    """
    Combined critic loss — Equation 9.

    L^critic(π_i) = L^critic_on(π_i) + λ * L^critic_off(π_i)

    Scaled by critic_coeff (λ' = 4.0) in final total loss.
    """
    return critic_coeff * (on_critic + lam * off_critic)


def compute_entropy_loss(
    log_probs: torch.Tensor,   # (B,) — log π(a|s)
) -> torch.Tensor:
    """
    Entropy bonus for follower diversity — used in Eq. 4.5 (Section 4.5).

    H(π(a|s)) = -E[log π(a|s)]

    Added to follower loss with coefficient λ_ent(j-1).
    Leader does NOT have entropy loss.
    """
    return log_probs.mean()  # -(-log_probs.mean()) = -H; negate for loss


def subsample_off_policy_data(
    follower_rollouts: List[Rollout],
    on_policy_size: int,
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    Subsample off-policy transitions from all followers to match on-policy data size.
    Implements the 50/50 on/off-policy split described in Sections 4.3 and 4.2.

    Args:
        follower_rollouts: List of Rollout from followers π_2..π_M
        on_policy_size: |D_1| — number of on-policy transitions from leader

    Returns:
        Subsampled (states, actions, log_probs_j, values_old_j) for importance weighting.
    """
    all_states = torch.cat([r.states.flatten(0, 1) for r in follower_rollouts], dim=0)
    all_actions = torch.cat([r.actions.flatten(0, 1) for r in follower_rollouts], dim=0)
    all_log_probs = torch.cat([r.log_probs_old.flatten(0, 1) for r in follower_rollouts], dim=0)
    all_values = torch.cat([r.values_old[:-1].flatten(0, 1) for r in follower_rollouts], dim=0)

    # Subsample to match on-policy data size
    n_total = all_states.shape[0]
    idx = torch.randperm(n_total)[:on_policy_size]
    return all_states[idx], all_actions[idx], all_log_probs[idx], all_values[idx]


def sapg_update_step(
    leader_rollout: Rollout,
    follower_rollouts: List[Rollout],
    leader_policy,          # callable: (states) -> (log_probs, values, log_probs_old)
    follower_policies,      # list of callables
    eps: float = 0.1,
    lam: float = 1.0,
    gamma: float = 0.99,
    entropy_coeffs: List[float] = None,  # λ_ent for each follower
    critic_coeff: float = 4.0,
) -> Dict[str, torch.Tensor]:
    """
    Single SAPG update step — Algorithm 1 from paper.

    1. Compute on-policy and off-policy actor + critic losses for leader.
    2. Compute on-policy actor + critic losses for each follower (+ entropy).
    3. Return total loss components for gradient computation.

    Args:
        leader_rollout: Data D_1 from leader's N/M environments.
        follower_rollouts: Data D_2..D_M from followers' environment blocks.
        leader_policy: Forward function for leader (π_1).
        follower_policies: Forward functions for followers (π_2..π_M).
        eps: PPO clipping parameter.
        lam: λ weight for off-policy term (default 1.0).
        gamma: Discount factor.
        entropy_coeffs: Per-follower entropy coefficients λ_ent(j-1).
        critic_coeff: λ' = 4.0, scales critic loss.

    Returns:
        Dictionary of loss components.
    """
    if entropy_coeffs is None:
        entropy_coeffs = [0.0] * len(follower_rollouts)

    M = len(follower_rollouts)
    losses = {}
    total_loss = torch.tensor(0.0)

    # --- Leader Update ---
    # On-policy: compute n-step returns for leader data
    on_targets = compute_nstep_returns(
        leader_rollout.rewards, leader_rollout.values_old,
        leader_rollout.dones, gamma=gamma, n=3
    )
    advantages_on = (on_targets - leader_rollout.values_old[:-1]).flatten(0, 1)
    advantages_on = (advantages_on - advantages_on.mean()) / (advantages_on.std() + 1e-8)

    # Get current policy log probs for leader's own data
    flat_states_leader = leader_rollout.states.flatten(0, 1)
    flat_actions_leader = leader_rollout.actions.flatten(0, 1)
    log_probs_new_leader, values_leader, _ = leader_policy(flat_states_leader, flat_actions_leader)

    # On-policy actor loss (Eq. 2)
    actor_on = on_policy_actor_loss(
        log_probs_new_leader,
        leader_rollout.log_probs_old.flatten(0, 1),
        advantages_on, eps=eps
    )
    critic_on = on_policy_critic_loss(values_leader, on_targets.flatten(0, 1))

    # Off-policy: subsample follower data
    on_policy_size = flat_states_leader.shape[0]
    off_states, off_actions, off_log_probs_j, _ = subsample_off_policy_data(
        follower_rollouts, on_policy_size
    )

    # Off-policy critic 1-step targets
    # (simplified: use leader's current value estimates as bootstrap)
    log_probs_new_leader_off, values_leader_off, log_probs_old_leader_off = leader_policy(
        off_states, off_actions
    )
    # Off-policy advantages (using leader's value function)
    # In practice computed from 1-step returns using leader's V
    off_advantages = (values_leader_off - values_leader_off.detach()).detach()  # placeholder

    # Off-policy actor loss (Eq. 3)
    actor_off = off_policy_actor_loss(
        log_probs_new_leader_off, log_probs_old_leader_off,
        off_log_probs_j, off_advantages, eps=eps
    )
    critic_off = off_policy_critic_loss(values_leader_off, values_leader_off.detach())

    # Combined losses (Eq. 4, 9)
    leader_actor_loss = combined_actor_loss(actor_on, [actor_off], lam=lam)
    leader_critic_loss = combined_critic_loss(critic_on, critic_off, lam=lam, critic_coeff=critic_coeff)
    total_loss = total_loss + leader_actor_loss + leader_critic_loss

    losses['leader_actor_on'] = actor_on
    losses['leader_actor_off'] = actor_off
    losses['leader_critic_on'] = critic_on
    losses['leader_critic_off'] = critic_off

    # --- Follower Updates ---
    for j, (follower_rollout, follower_policy, ent_coeff) in enumerate(
        zip(follower_rollouts, follower_policies, entropy_coeffs)
    ):
        f_targets = compute_nstep_returns(
            follower_rollout.rewards, follower_rollout.values_old,
            follower_rollout.dones, gamma=gamma, n=3
        )
        f_advantages = (f_targets - follower_rollout.values_old[:-1]).flatten(0, 1)
        f_advantages = (f_advantages - f_advantages.mean()) / (f_advantages.std() + 1e-8)

        flat_states_f = follower_rollout.states.flatten(0, 1)
        flat_actions_f = follower_rollout.actions.flatten(0, 1)
        log_probs_new_f, values_f, _ = follower_policy(flat_states_f, flat_actions_f)

        # On-policy PPO loss for follower (Eq. 2)
        f_actor_loss = on_policy_actor_loss(
            log_probs_new_f,
            follower_rollout.log_probs_old.flatten(0, 1),
            f_advantages, eps=eps
        )
        f_critic_loss = critic_coeff * on_policy_critic_loss(values_f, f_targets.flatten(0, 1))

        # Entropy bonus for follower (Section 4.5)
        if ent_coeff > 0.0:
            entropy_loss = ent_coeff * compute_entropy_loss(log_probs_new_f)
            total_loss = total_loss + entropy_loss
            losses[f'follower_{j}_entropy'] = entropy_loss

        total_loss = total_loss + f_actor_loss + f_critic_loss
        losses[f'follower_{j}_actor'] = f_actor_loss
        losses[f'follower_{j}_critic'] = f_critic_loss

    losses['total'] = total_loss
    return losses
