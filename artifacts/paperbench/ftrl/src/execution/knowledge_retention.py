"""
Knowledge Retention Methods for RL Fine-tuning.
Implements EWC, Behavioral Cloning (BC), Kickstarting (KS) auxiliary losses.
Applied only to the actor (policy) network, NOT the critic.

Reference: Wołczyk et al. (2024), "Fine-tuning Reinforcement Learning Models is
Secretly a Forgetting Mitigation Problem", ICML 2024.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, List, Optional, Tuple
from torch import Tensor


def compute_ewc_loss(
    current_params: Dict[str, Tensor],
    pretrained_params: Dict[str, Tensor],
    fisher_diagonal: Dict[str, Tensor],
    regularization_coeff: float,
) -> Tensor:
    """
    Compute Elastic Weight Consolidation (EWC) auxiliary loss.

    L_EWC(θ) = λ · Σᵢ Fᵢ(θ*ᵢ - θᵢ)²

    Applied ONLY to actor parameters. Penalizes deviation from pre-trained
    weights, weighted by Fisher Information Matrix diagonal.

    Args:
        current_params: Dict of current model parameter tensors {name: tensor}
        pretrained_params: Dict of pre-trained (frozen) parameter tensors {name: tensor}
        fisher_diagonal: Dict of Fisher diagonal values {name: tensor}
            - NetHack: estimated over 10,000 batches from NLD-AA
            - RoboticSequence: estimated over 2,560 replay buffer examples;
              clipped to min 1e-5
        regularization_coeff: λ scalar weight
            - NetHack: 2e6
            - RoboticSequence: 100 (actor), 0 (critic - do NOT call for critic)

    Returns:
        Scalar EWC loss tensor
    """
    ewc_loss = torch.tensor(0.0, requires_grad=True)
    for name, current_param in current_params.items():
        pretrained_param = pretrained_params[name]
        fisher = fisher_diagonal[name]
        ewc_loss = ewc_loss + (fisher * (pretrained_param - current_param) ** 2).sum()
    return regularization_coeff * ewc_loss


def compute_fisher_diagonal_nethack(
    model: nn.Module,
    data_loader,
    n_batches: int = 10000,
) -> Dict[str, Tensor]:
    """
    Estimate Fisher Information Matrix diagonal for NetHack (actor parameters only).

    F_ii = E[(∂ℓ/∂θᵢ)²]

    Estimated using squared gradients of behavioral cloning cross-entropy loss
    over 10,000 batches from the NLD-AA dataset subset (~8000 Human Monk games).

    Args:
        model: Pre-trained LSTM policy network (actor only)
        data_loader: DataLoader over NLD-AA Human Monk subset
        n_batches: Number of batches to average over (paper: 10,000)

    Returns:
        Dict mapping parameter name → Fisher diagonal tensor (same shape as param)
    """
    fisher: Dict[str, Tensor] = {
        name: torch.zeros_like(param)
        for name, param in model.named_parameters()
        if param.requires_grad
    }
    model.eval()
    for batch_idx, batch in enumerate(data_loader):
        if batch_idx >= n_batches:
            break
        states, actions = batch
        model.zero_grad()
        log_probs = model(states).log_prob(actions)
        loss = -log_probs.mean()
        loss.backward()
        for name, param in model.named_parameters():
            if param.grad is not None:
                fisher[name] += param.grad.data ** 2
    for name in fisher:
        fisher[name] /= n_batches
    return fisher


def compute_fisher_diagonal_robotic(
    model: nn.Module,
    replay_buffer,
    n_samples: int = 2560,
    clip_min: float = 1e-5,
) -> Dict[str, Tensor]:
    """
    Estimate Fisher diagonal for RoboticSequence (SAC Gaussian policy actor).

    Uses analytical formula for Gaussian policy:
    I_kk = (∂μ/∂θ_k · 1/σ)² + 2(∂σ/∂θ_k · 1/σ)²

    Outer expectation approximated with n_samples from replay buffer.
    Fisher is clipped to minimum value of 1e-5.

    Args:
        model: SAC actor (Gaussian policy MLP)
        replay_buffer: SAC replay buffer; sample 2560 state examples
        n_samples: Number of examples for Fisher estimation (paper: 2560)
        clip_min: Minimum Fisher value for numerical stability (paper: 1e-5)

    Returns:
        Dict mapping parameter name → Fisher diagonal tensor, clipped at clip_min
    """
    fisher: Dict[str, Tensor] = {
        name: torch.zeros_like(param)
        for name, param in model.named_parameters()
        if param.requires_grad
    }
    model.eval()
    states = replay_buffer.sample_states(n_samples)
    for state in states:
        # Analytical Fisher for Gaussian policy:
        #   I_kk = (∂μ/∂θ_k · 1/σ)² + 2·(∂σ/∂θ_k · 1/σ)²
        # We compute gradients of μ and σ w.r.t. each parameter separately,
        # then combine using the formula above.
        mu, log_std = model(state.unsqueeze(0))
        sigma = log_std.exp().detach()  # detach σ for the μ-term gradient

        # Term 1: (∂μ/∂θ_k / σ)² — gradient of (μ/σ) w.r.t. θ
        for d in range(mu.shape[-1]):
            model.zero_grad()
            proxy_mu = (mu[0, d] / sigma[0, d])
            proxy_mu.backward(retain_graph=True)
            for name, param in model.named_parameters():
                if param.grad is not None:
                    fisher[name] += param.grad.data ** 2

        # Term 2: 2·(∂σ/∂θ_k / σ)² — gradient of (σ/σ_detached)
        mu_detached = mu.detach()
        sigma_fresh = log_std.exp()  # recompute with gradients
        for d in range(sigma_fresh.shape[-1]):
            model.zero_grad()
            proxy_sigma = (sigma_fresh[0, d] / sigma[0, d])
            proxy_sigma.backward(retain_graph=True)
            for name, param in model.named_parameters():
                if param.grad is not None:
                    fisher[name] += 2.0 * param.grad.data ** 2

    for name in fisher:
        fisher[name] /= n_samples
        fisher[name] = torch.clamp(fisher[name], min=clip_min)
    return fisher


def compute_bc_loss(
    current_policy: nn.Module,
    pretrained_policy: nn.Module,
    bc_buffer: List[Tensor],
    scale: float = 2.0,
) -> Tensor:
    """
    Compute Behavioral Cloning (BC) auxiliary loss using static pre-training buffer.

    L_BC(θ) = λ · E_{s ~ B_BC}[D_KL(π*(s) ‖ π_θ(s))]

    Uses a STATIC buffer of states from the pre-training environment.
    B_BC = {(s, π*(s)) : s ∈ S_BC} collected before fine-tuning starts.

    NetHack: scale=2.0, NO decay; states from NLD-AA (~8000 Human Monk games)
    RoboticSequence: actor_coeff=1; BC also adds L2 loss on critic (not here)
    Montezuma's Revenge: KL weight coefficient tuned per experiment

    Args:
        current_policy: Current fine-tuned policy πθ
        pretrained_policy: Frozen pre-trained policy π* (no gradient)
        bc_buffer: List of state tensors from pre-training environment
        scale: λ coefficient (NetHack: 2.0; RoboticSequence: 1.0)

    Returns:
        Scalar BC loss tensor
    """
    pretrained_policy.eval()
    states = torch.stack(bc_buffer)
    with torch.no_grad():
        pretrained_dist = pretrained_policy.get_distribution(states)
    current_dist = current_policy.get_distribution(states)
    kl_loss = torch.distributions.kl_divergence(pretrained_dist, current_dist).mean()
    return scale * kl_loss


def compute_ks_loss(
    current_policy: nn.Module,
    pretrained_policy: nn.Module,
    online_states: Tensor,
    scale: float = 0.5,
    decay: float = 0.99998,
    step: int = 0,
) -> Tensor:
    """
    Compute Kickstarting (KS) auxiliary loss using ONLINE policy data.

    L_KS(θ) = λ_t · E_{s ~ B_θ}[D_KL(π*(s) ‖ π_θ(s))]

    λ_t = scale · decay^step (exponential decay)

    Key difference from BC: expectation over states collected by CURRENT policy,
    not a static pre-training buffer. This means KS matches π* only on states
    the online policy actually visits.

    FAILURE CASE (State Coverage Gap): When the online policy visits CLOSE states
    that π* was never trained on, KL(π*(s) ‖ πθ(s)) is meaningless/harmful.
    Only use KS for Imperfect Cloning Gap scenarios (NetHack).

    Args:
        current_policy: Current fine-tuned policy πθ
        pretrained_policy: Frozen pre-trained policy π* (no gradient)
        online_states: States from recent online rollouts (B_θ)
        scale: Initial KS loss scale (NetHack: 0.5)
        decay: Exponential decay rate per training step (NetHack: 0.99998)
        step: Current training step (for decay computation)

    Returns:
        Scalar KS loss tensor (with decayed coefficient)
    """
    lambda_t = scale * (decay ** step)
    pretrained_policy.eval()
    with torch.no_grad():
        pretrained_dist = pretrained_policy.get_distribution(online_states)
    current_dist = current_policy.get_distribution(online_states)
    kl_loss = torch.distributions.kl_divergence(pretrained_dist, current_dist).mean()
    return lambda_t * kl_loss


def setup_episodic_memory_buffer(
    pretrained_policy: nn.Module,
    environment,
    n_samples: int = 10000,
    replay_buffer_size: int = 100000,
) -> List[Tuple[Tensor, Tensor, Tensor]]:
    """
    Collect episodic memory samples from pre-trained environment for SAC.

    Samples n_samples state-action-reward tuples from pre-trained policy π*
    on the pre-training tasks (last two stages of RoboticSequence).
    These samples occupy 10% of the SAC replay buffer and are PROTECTED
    (never overwritten during fine-tuning).

    Args:
        pretrained_policy: Pre-trained SAC policy π* (100% success on last 2 stages)
        environment: Pre-training environment (peg-unplug-side + push-wall)
        n_samples: Number of samples to collect (paper: 10,000 = 10% of 100K buffer)
        replay_buffer_size: Total SAC replay buffer size (100,000)

    Returns:
        List of (state, action, reward) tuples to be protected in replay buffer
    """
    assert n_samples <= 0.1 * replay_buffer_size, \
        f"EM buffer ({n_samples}) should be ≤10% of replay buffer ({replay_buffer_size})"
    memory: List[Tuple[Tensor, Tensor, Tensor]] = []
    state = environment.reset()
    while len(memory) < n_samples:
        state_tensor = torch.tensor(state, dtype=torch.float32)
        with torch.no_grad():
            action = pretrained_policy.act(state_tensor)
        next_state, reward, done, _ = environment.step(action.numpy())
        memory.append((state_tensor, action, torch.tensor(reward)))
        state = next_state if not done else environment.reset()
    return memory
