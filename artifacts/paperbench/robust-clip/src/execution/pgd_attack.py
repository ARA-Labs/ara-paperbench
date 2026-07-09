"""
PGD and APGD attack implementations for evaluating robustness of CLIP-based models.

Reference: Schlarmann et al. (2024) - "Robust CLIP"
Attack details: §4.1, §4.2, Appendix B.6, B.8
Croce & Hein (2020) AutoAttack for APGD evaluation.
"""

import torch
import torch.nn as nn
from typing import Callable, Optional


def pgd_linf_attack(
    model_fn: Callable[[torch.Tensor], torch.Tensor],
    x: torch.Tensor,
    loss_fn: Callable[[torch.Tensor], torch.Tensor],
    epsilon: float,
    step_size: float,
    num_steps: int,
    momentum: float = 0.9,
    targeted: bool = False,
    random_init: bool = True,
) -> torch.Tensor:
    """
    PGD ℓ∞ attack with momentum (for both training and evaluation).

    For FARE training: maximizes ||phi(z) - phi_org(x)||²₂
    For evaluation: maximizes classification cross-entropy or autoregressive loss

    Args:
        model_fn: Function mapping images to outputs used by loss_fn
        x: Clean input images (B, 3, H, W), values in [0, 1]
        loss_fn: Loss function applied to model_fn(z); scalar output
        epsilon: ℓ∞ perturbation radius
        step_size: Step size α per PGD iteration
        num_steps: Number of PGD iterations
        momentum: Momentum factor (0.9 during training)
        targeted: If True, minimizes loss (for targeted attacks); else maximizes
        random_init: Random initialization within ℓ∞ ball

    Returns:
        x_adv: Adversarial examples, shape (B, 3, H, W), values in [0, 1]
    """
    sign = -1.0 if targeted else 1.0

    if random_init:
        delta = torch.empty_like(x).uniform_(-epsilon, epsilon)
        delta = torch.clamp(x + delta, 0.0, 1.0) - x
    else:
        delta = torch.zeros_like(x)

    delta = delta.detach()
    grad_momentum = torch.zeros_like(x)

    for step in range(num_steps):
        delta.requires_grad_(True)
        z = x + delta

        output = model_fn(z)
        loss = loss_fn(output)

        grad = torch.autograd.grad(loss, delta)[0]
        grad = grad.detach()

        # ℓ₁ normalization for momentum PGD
        grad_norm = grad.abs().sum(dim=(1, 2, 3), keepdim=True) + 1e-12
        grad_normalized = grad / grad_norm
        grad_momentum = momentum * grad_momentum + grad_normalized

        # Sign gradient step (ℓ∞ constraint)
        delta_new = delta.detach() + sign * step_size * grad_momentum.sign()
        delta_new = torch.clamp(delta_new, -epsilon, epsilon)
        delta_new = torch.clamp(x + delta_new, 0.0, 1.0) - x
        delta = delta_new.detach()

    return (x + delta).detach()


def apgd_untargeted_lvlm(
    model_fn: Callable[[torch.Tensor], torch.Tensor],
    x: torch.Tensor,
    loss_fn: Callable[[torch.Tensor], torch.Tensor],
    epsilon: float,
    num_steps: int = 100,
    half_precision: bool = True,
    init_delta: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    """
    APGD-based untargeted attack for LVLM evaluation (Appendix B.6).
    Initial step size = epsilon (following Schlarmann & Hein 2023).

    Attack pipeline (Appendix B.6):
    1. Run at half precision (float16), 100 iterations per ground-truth label
    2. Skip samples below CIDEr threshold (< 10 for COCO, < 2 for Flickr30k)
    3. Run final single-precision attack on remaining hard samples

    Args:
        model_fn: LVLM forward function (vision encoder + LLM)
        x: Clean input images (B, 3, H, W), values in [0, 1]
        loss_fn: Autoregressive cross-entropy loss w.r.t. ground-truth caption/answer
        epsilon: ℓ∞ perturbation radius (2/255 or 4/255)
        num_steps: Number of APGD iterations (100 for half-precision; same for single)
        half_precision: Whether to run in float16
        init_delta: Initial perturbation (None for random; use best from prev attack for warm start)

    Returns:
        x_adv: Adversarial examples
    """
    if half_precision:
        x = x.half()
        model_fn_cast = lambda z: model_fn(z.half())
    else:
        model_fn_cast = model_fn

    step_size = epsilon  # Initial step size = epsilon (Schlarmann & Hein 2023)

    if init_delta is not None:
        delta = init_delta.clone().detach()
    else:
        delta = torch.empty_like(x).uniform_(-epsilon, epsilon)
        delta = torch.clamp(x + delta, 0.0, 1.0) - x

    delta = delta.detach()

    for step in range(num_steps):
        delta.requires_grad_(True)
        z = x + delta
        output = model_fn_cast(z)
        loss = loss_fn(output)
        grad = torch.autograd.grad(loss, delta)[0].detach()

        # APGD step (simplified; full APGD has adaptive step size reduction)
        delta_new = delta.detach() + step_size * grad.sign()
        delta_new = torch.clamp(delta_new, -epsilon, epsilon)
        delta_new = torch.clamp(x + delta_new, 0.0, 1.0) - x
        delta = delta_new.detach()

    return (x + delta).detach().float()


def apgd_targeted_lvlm(
    model_fn: Callable[[torch.Tensor], torch.Tensor],
    x: torch.Tensor,
    target_loss_fn: Callable[[torch.Tensor], torch.Tensor],
    epsilon: float,
    num_steps: int = 10000,
    step_size: Optional[float] = None,
) -> torch.Tensor:
    """
    APGD targeted attack for stealthy targeted attacks on LVLMs (§4.2, Appendix B.8).
    Minimizes autoregressive cross-entropy w.r.t. target string.
    10,000 iterations for strong attack evaluation.

    Success criterion: target string exactly contained in model output (Appendix B.8).

    Args:
        model_fn: LVLM forward pass
        x: Clean input images (B, 3, H, W)
        target_loss_fn: Loss function that computes -log p(target|z) (to be minimized)
        epsilon: ℓ∞ radius (2/255 or 4/255)
        num_steps: Number of iterations (10,000 for full evaluation; 500 for ablation)
        step_size: Step size (default: epsilon / 4 if None)

    Returns:
        x_adv: Adversarial examples
    """
    if step_size is None:
        step_size = epsilon / 4.0

    delta = torch.empty_like(x).uniform_(-epsilon, epsilon)
    delta = torch.clamp(x + delta, 0.0, 1.0) - x
    delta = delta.detach()
    grad_momentum = torch.zeros_like(x)
    momentum = 0.9

    for step in range(num_steps):
        delta.requires_grad_(True)
        z = x + delta
        output = model_fn(z)
        # targeted: minimize loss (i.e., maximize likelihood of target string)
        loss = target_loss_fn(output)

        grad = torch.autograd.grad(loss, delta)[0].detach()
        grad_norm = grad.abs().sum(dim=(1, 2, 3), keepdim=True) + 1e-12
        grad_normalized = grad / grad_norm
        grad_momentum = momentum * grad_momentum + grad_normalized

        # Minimize: step in negative gradient direction
        delta_new = delta.detach() - step_size * grad_momentum.sign()
        delta_new = torch.clamp(delta_new, -epsilon, epsilon)
        delta_new = torch.clamp(x + delta_new, 0.0, 1.0) - x
        delta = delta_new.detach()

    return (x + delta).detach()


def check_targeted_attack_success(model_output: str, target_string: str) -> bool:
    """
    Success criterion for targeted attacks: target string exactly contained in output.

    Args:
        model_output: Text output from LVLM
        target_string: Target string to inject

    Returns:
        True if attack succeeded (target string in output)
    """
    return target_string in model_output
