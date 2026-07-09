"""
FARE: Fine-tuning for Adversarially Robust Embeddings
Core training loop for unsupervised adversarial fine-tuning of CLIP vision encoder.

Reference: Schlarmann et al. (2024) - "Robust CLIP: Unsupervised Adversarial Fine-Tuning
of Vision Embeddings for Robust Large Vision-Language Models"
Section 3.3, Appendix B.1
"""

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from typing import Optional


def pgd_inner_maximization(
    phi_ft: nn.Module,
    phi_org: nn.Module,
    x: torch.Tensor,
    epsilon: float,
    step_size: float,
    num_steps: int,
    momentum: float = 0.9,
) -> torch.Tensor:
    """
    PGD inner maximization for FARE loss.
    Finds worst-case perturbation z* = argmax_{||z-x||_inf <= epsilon} ||phi_ft(z) - phi_org(x)||_2^2

    Args:
        phi_ft: Fine-tuned CLIP vision encoder (being trained); must support gradient computation
        phi_org: Original frozen CLIP vision encoder
        x: Clean input images, shape (B, 3, H, W), values in [0, 1]
        epsilon: ℓ∞ perturbation radius (e.g., 2/255 or 4/255)
        step_size: PGD step size α (e.g., 1/255)
        num_steps: Number of PGD iterations (10 during training, 100 during eval)
        momentum: Momentum factor for gradient accumulation (default 0.9)

    Returns:
        z: Adversarially perturbed images, shape (B, 3, H, W), values in [0, 1]
    """
    B = x.shape[0]

    # Compute frozen reference embeddings (class token)
    with torch.no_grad():
        phi_org_x = phi_org.encode_image(x)  # shape: (B, D), unnormalized

    # Random initialization within ℓ∞ ball
    delta = torch.empty_like(x).uniform_(-epsilon, epsilon)
    delta = torch.clamp(x + delta, 0.0, 1.0) - x
    delta = delta.detach().requires_grad_(True)

    # Momentum accumulator
    grad_momentum = torch.zeros_like(x)

    for t in range(num_steps):
        z = x + delta
        # Forward pass through fine-tuned encoder (class token)
        phi_ft_z = phi_ft.encode_image(z)  # shape: (B, D), unnormalized

        # FARE loss: ||phi_ft(z) - phi_org(x)||_2^2 per sample, then mean
        loss = ((phi_ft_z - phi_org_x) ** 2).sum(dim=-1).mean()

        # Compute gradient w.r.t. delta
        grad = torch.autograd.grad(loss, delta)[0]

        # Momentum update with ℓ₁ normalization (sign gradient for ℓ∞)
        grad_normalized = grad / (grad.abs().sum(dim=(1, 2, 3), keepdim=True) + 1e-12)
        grad_momentum = momentum * grad_momentum + grad_normalized

        # PGD step: sign gradient for ℓ∞ constraint
        delta_data = delta.detach() + step_size * grad_momentum.sign()
        delta_data = torch.clamp(delta_data, -epsilon, epsilon)
        delta_data = torch.clamp(x + delta_data, 0.0, 1.0) - x
        delta = delta_data.detach().requires_grad_(True)

    return (x + delta).detach()


def fare_loss(
    phi_ft: nn.Module,
    phi_org: nn.Module,
    x_adv: torch.Tensor,
    x_clean: torch.Tensor,
) -> torch.Tensor:
    """
    Compute FARE loss: mean squared ℓ₂ distance between adversarial fine-tuned embedding
    and original clean embedding.

    L_FARE = (1/B) sum_i ||phi_ft(z_i) - phi_org(x_i)||_2^2

    Args:
        phi_ft: Fine-tuned CLIP vision encoder
        phi_org: Original frozen CLIP vision encoder
        x_adv: Adversarially perturbed images (z), shape (B, 3, H, W)
        x_clean: Clean images (x), shape (B, 3, H, W)

    Returns:
        loss: Scalar FARE loss
    """
    phi_ft_z = phi_ft.encode_image(x_adv)       # (B, D), unnormalized, class token

    with torch.no_grad():
        phi_org_x = phi_org.encode_image(x_clean)  # (B, D), unnormalized, class token, frozen

    loss = ((phi_ft_z - phi_org_x) ** 2).sum(dim=-1).mean()
    return loss


def fare_train_epoch(
    phi_ft: nn.Module,
    phi_org: nn.Module,
    dataloader: DataLoader,
    optimizer: torch.optim.Optimizer,
    scheduler,
    epsilon: float,
    step_size: float,
    num_pgd_steps: int,
    device: torch.device,
) -> float:
    """
    One training epoch of FARE fine-tuning.

    Args:
        phi_ft: Fine-tuned CLIP vision encoder (updated in-place)
        phi_org: Original frozen CLIP vision encoder (not updated)
        dataloader: ImageNet DataLoader (images only, labels ignored)
        optimizer: AdamW optimizer (β1=0.9, β2=0.95, WD=1e-4)
        scheduler: LR scheduler (cosine decay with linear warmup, peak LR=1e-5 at 7%)
        epsilon: ℓ∞ radius (2/255 for FARE2, 4/255 for FARE4)
        step_size: PGD step size (1/255)
        num_pgd_steps: Number of PGD steps (10)
        device: torch.device

    Returns:
        mean_loss: Average FARE loss over the epoch
    """
    phi_ft.train()
    phi_org.eval()
    # Freeze text encoder and phi_org
    for param in phi_org.parameters():
        param.requires_grad_(False)

    total_loss = 0.0
    num_batches = 0

    for batch in dataloader:
        # Dataloader returns (images, labels) but labels are NOT used
        if isinstance(batch, (list, tuple)):
            x = batch[0].to(device)
        else:
            x = batch.to(device)

        # Inner maximization: find worst-case adversarial perturbation
        phi_ft.eval()  # BN in eval mode during PGD for stability
        z = pgd_inner_maximization(
            phi_ft=phi_ft,
            phi_org=phi_org,
            x=x,
            epsilon=epsilon,
            step_size=step_size,
            num_steps=num_pgd_steps,
            momentum=0.9,
        )

        # Outer minimization: update phi_ft
        phi_ft.train()
        optimizer.zero_grad()
        loss = fare_loss(phi_ft, phi_org, x_adv=z, x_clean=x)
        loss.backward()
        optimizer.step()
        if scheduler is not None:
            scheduler.step()

        total_loss += loss.item()
        num_batches += 1

    return total_loss / max(num_batches, 1)


def build_fare_optimizer_and_scheduler(
    phi_ft: nn.Module,
    total_steps: int,
    peak_lr: float = 1e-5,
    weight_decay: float = 1e-4,
    warmup_fraction: float = 0.07,
    beta1: float = 0.9,
    beta2: float = 0.95,
) -> tuple:
    """
    Build AdamW optimizer and cosine LR scheduler with linear warmup for FARE.

    Training hyperparameters (Appendix B.1):
      - Optimizer: AdamW, β1=0.9, β2=0.95
      - Peak LR: 1e-5 (cosine decay, linear warmup to 7% of total steps)
      - Weight decay: 1e-4
      - Effective batch size: 128
      - Epochs: 2

    Args:
        phi_ft: Model whose parameters are to be optimized (vision encoder only)
        total_steps: Total number of gradient steps (len(dataloader) * epochs)
        peak_lr: Peak learning rate (default 1e-5)
        weight_decay: Weight decay coefficient (default 1e-4)
        warmup_fraction: Fraction of total steps for linear LR warmup (default 0.07)
        beta1: AdamW β1 (default 0.9)
        beta2: AdamW β2 (default 0.95)

    Returns:
        (optimizer, scheduler) tuple
    """
    optimizer = torch.optim.AdamW(
        phi_ft.parameters(),
        lr=peak_lr,
        betas=(beta1, beta2),
        weight_decay=weight_decay,
    )

    warmup_steps = int(warmup_fraction * total_steps)

    def lr_lambda(step: int) -> float:
        if step < warmup_steps:
            return float(step) / float(max(1, warmup_steps))
        progress = float(step - warmup_steps) / float(max(1, total_steps - warmup_steps))
        return max(0.0, 0.5 * (1.0 + torch.cos(torch.tensor(progress * 3.14159265)).item()))

    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda=lr_lambda)
    return optimizer, scheduler
