"""
Core stochastic interpolant training loop with data-dependent couplings.

Implements Algorithm 1 from Albergo et al., 2024 (ICML):
"Stochastic Interpolants with Data-Dependent Couplings"

This module handles the generic training framework; task-specific coupling
construction is in inpainting.py and superresolution.py.
"""

import torch
import torch.nn as nn
from torch.optim import Adam
from torch.optim.lr_scheduler import StepLR
from typing import Callable, Tuple


def compute_interpolant(
    x0: torch.Tensor,   # (B, C, H, W) base sample (corrupted/masked target)
    x1: torch.Tensor,   # (B, C, H, W) target sample (clean ImageNet image)
    t: torch.Tensor,    # (B,) time in [0, 1]
    alpha_fn: Callable[[torch.Tensor], torch.Tensor],  # αₜ schedule
    beta_fn: Callable[[torch.Tensor], torch.Tensor],   # βₜ schedule
    alpha_dot_fn: Callable[[torch.Tensor], torch.Tensor],  # α̇ₜ
    beta_dot_fn: Callable[[torch.Tensor], torch.Tensor],   # β̇ₜ
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Compute the stochastic interpolant Iₜ and its time derivative İₜ.

    Eq. (1): Iₜ = αₜ·x₀ + βₜ·x₁  (with γₜ=0 in all experiments)
    İₜ = α̇ₜ·x₀ + β̇ₜ·x₁

    For both inpainting (αₜ=t, βₜ=1-t) and super-resolution (αₜ=1-t, βₜ=t):
        İₜ = ±(x₁ - x₀)

    Args:
        x0: Base samples, shape (B, C, H, W)
        x1: Target samples, shape (B, C, H, W)
        t: Time points, shape (B,)
        alpha_fn, beta_fn: Interpolant coefficient functions
        alpha_dot_fn, beta_dot_fn: Time derivatives of coefficient functions

    Returns:
        I_t: Interpolant at time t, shape (B, C, H, W)
        I_dot_t: Time derivative of interpolant, shape (B, C, H, W)
    """
    # Reshape t for broadcasting over spatial dims
    t_shape = t.view(-1, 1, 1, 1)  # (B, 1, 1, 1)

    alpha_t = alpha_fn(t_shape)
    beta_t = beta_fn(t_shape)
    alpha_dot_t = alpha_dot_fn(t_shape)
    beta_dot_t = beta_dot_fn(t_shape)

    I_t = alpha_t * x0 + beta_t * x1
    I_dot_t = alpha_dot_t * x0 + beta_dot_t * x1
    return I_t, I_dot_t


def velocity_loss(
    b_hat: torch.Tensor,  # (B, C, H, W) predicted velocity
    I_dot_t: torch.Tensor,  # (B, C, H, W) true time derivative of interpolant
) -> torch.Tensor:
    """
    Compute the quadratic regression loss for the velocity field (Eq. 22).

    L̂_b(b̂) = n_b⁻¹ Σᵢ [|b̂ₜᵢ(Iₜᵢ)|² - 2·İₜᵢ·b̂ₜᵢ(Iₜᵢ)]

    This objective has unique minimizer bₜ(x) = E(İₜ | Iₜ = x) for ANY
    coupling ρ(x₀,x₁) with the correct marginals (Theorem 3.1 / Theorem A.1).

    Args:
        b_hat: Predicted velocity field from network, shape (B, C, H, W)
        I_dot_t: True interpolant time derivative, shape (B, C, H, W)

    Returns:
        Scalar loss value.
    """
    # |b̂|² - 2·İ·b̂ summed over spatial dims, averaged over batch
    loss = (b_hat ** 2 - 2.0 * I_dot_t * b_hat).mean()
    return loss


def train_step(
    model: nn.Module,         # U-Net velocity model b̂_θ
    x0: torch.Tensor,         # (B, C, H, W) base samples (from data-dependent coupling)
    x1: torch.Tensor,         # (B, C, H, W) target samples
    xi: torch.Tensor,         # (B, ...) conditioning variable (mask or low-res image)
    class_labels: torch.Tensor,  # (B,) integer class labels
    alpha_fn: Callable,
    beta_fn: Callable,
    alpha_dot_fn: Callable,
    beta_dot_fn: Callable,
    optimizer: Adam,
    output_mask: torch.Tensor = None,  # (B, 1, H, W) optional output masking (inpainting)
) -> float:
    """
    Single training step implementing Algorithm 1.

    Returns:
        Scalar loss value for logging.
    """
    B = x0.shape[0]
    device = x0.device

    # Sample time uniformly: tᵢ ~ U(0, 1)
    t = torch.rand(B, device=device)

    # Compute interpolant
    I_t, I_dot_t = compute_interpolant(x0, x1, t, alpha_fn, beta_fn, alpha_dot_fn, beta_dot_fn)

    # Append conditioning to input (channel dimension)
    # xi is appended as extra channels following Ho et al. 2022a
    model_input = torch.cat([I_t, xi], dim=1)  # (B, C+C_cond, H, W)

    # Forward pass: predict velocity
    b_hat_full = model(model_input, t, class_labels)  # (B, C, H, W)

    # Apply output mask for inpainting (zero velocity on known pixels)
    if output_mask is not None:
        b_hat = b_hat_full * output_mask  # zero out unmasked regions
        I_dot_t_masked = I_dot_t * output_mask
    else:
        b_hat = b_hat_full
        I_dot_t_masked = I_dot_t

    # Compute quadratic velocity loss (Eq. 22)
    loss = velocity_loss(b_hat, I_dot_t_masked)

    # Backward pass
    optimizer.zero_grad()
    loss.backward()

    # Gradient norm clipping at 10,000 (global L2 norm, PyTorch default)
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=10_000)

    optimizer.step()
    return loss.item()


def build_optimizer_and_scheduler(
    model: nn.Module,
    lr: float = 2e-4,
    step_size: int = 1000,
    gamma: float = 0.99,
) -> Tuple[Adam, StepLR]:
    """
    Build Adam optimizer and StepLR scheduler as specified in Appendix B.

    Args:
        model: U-Net velocity model.
        lr: Initial learning rate (default 2e-4).
        step_size: Number of gradient steps between LR decay (default 1000).
        gamma: Multiplicative LR decay factor (default 0.99).

    Returns:
        (optimizer, scheduler) tuple.
    """
    # Adam with no weight decay
    optimizer = Adam(model.parameters(), lr=lr, weight_decay=0.0)
    scheduler = StepLR(optimizer, step_size=step_size, gamma=gamma)
    return optimizer, scheduler


# ---- Interpolant schedules ----

def alpha_inpainting(t: torch.Tensor) -> torch.Tensor:
    """αₜ = t for inpainting (§4.1)."""
    return t

def beta_inpainting(t: torch.Tensor) -> torch.Tensor:
    """βₜ = 1 - t for inpainting (§4.1)."""
    return 1.0 - t

def alpha_dot_inpainting(t: torch.Tensor) -> torch.Tensor:
    """α̇ₜ = 1 for inpainting."""
    return torch.ones_like(t)

def beta_dot_inpainting(t: torch.Tensor) -> torch.Tensor:
    """β̇ₜ = -1 for inpainting."""
    return -torch.ones_like(t)


def alpha_superres(t: torch.Tensor) -> torch.Tensor:
    """αₜ = 1 - t for super-resolution (§3.3)."""
    return 1.0 - t

def beta_superres(t: torch.Tensor) -> torch.Tensor:
    """βₜ = t for super-resolution (§3.3)."""
    return t

def alpha_dot_superres(t: torch.Tensor) -> torch.Tensor:
    """α̇ₜ = -1 for super-resolution."""
    return -torch.ones_like(t)

def beta_dot_superres(t: torch.Tensor) -> torch.Tensor:
    """β̇ₜ = 1 for super-resolution."""
    return torch.ones_like(t)
