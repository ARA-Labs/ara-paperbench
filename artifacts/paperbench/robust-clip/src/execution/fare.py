"""
FARE: Fine-tuning for Adversarially Robust Embeddings
Core algorithm stub — implements the FARE loss and PGD inner maximization.

Paper: "Robust CLIP: Unsupervised Adversarial Fine-Tuning of Vision Embeddings
        for Robust Large Vision-Language Models" (Schlarmann et al., ICML 2024)
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch import Tensor
from typing import Tuple


def pgd_inner_maximization(
    phi: nn.Module,
    phi_org: nn.Module,
    x: Tensor,                # Clean images, shape (B, C, H, W), values in [0, 1]
    eps: float,               # ℓ∞ perturbation radius (e.g., 4/255)
    alpha: float = 1/255,     # PGD step size
    n_steps: int = 10,        # Number of PGD inner steps
) -> Tensor:
    """
    Solves the inner maximization of FARE:
        max_{||z - x||_inf <= eps} ||phi(z) - phi_org(x)||_2^2

    Uses signed gradient ascent (PGD) with random initialization.

    Args:
        phi:      Fine-tuned CLIP vision encoder (being optimized, gradients flow through)
        phi_org:  Original frozen CLIP vision encoder (reference)
        x:        Clean input images, shape (B, C, H, W), in [0, 1]
        eps:      ℓ∞ perturbation radius
        alpha:    PGD step size per iteration
        n_steps:  Number of PGD ascent steps

    Returns:
        z_adv: Adversarially perturbed images, shape (B, C, H, W), in [0, 1]
    """
    # Frozen reference embedding (class token only, as per Appendix B.1)
    with torch.no_grad():
        target_embedding = phi_org(x)  # shape: (B, D)

    # Initialize perturbation with uniform random noise within [-eps, eps]
    delta = torch.empty_like(x).uniform_(-eps, eps)
    delta = torch.clamp(x + delta, 0.0, 1.0) - x  # project to valid image range

    for _ in range(n_steps):
        delta = delta.detach().requires_grad_(True)
        z = torch.clamp(x + delta, 0.0, 1.0)

        # Compute FARE inner loss: ||phi(z) - phi_org(x)||_2^2 (maximize)
        adv_embedding = phi(z)  # shape: (B, D)
        inner_loss = torch.sum((adv_embedding - target_embedding.detach()) ** 2, dim=-1)
        inner_loss.sum().backward()

        with torch.no_grad():
            # Signed gradient ascent step (elementwise sign)
            delta = delta + alpha * delta.grad.sign()
            # Project back to ℓ∞ ball
            delta = torch.clamp(delta, -eps, eps)
            # Project back to valid image domain [0, 1]
            delta = torch.clamp(x + delta, 0.0, 1.0) - x

    return (x + delta).detach()


def fare_loss(
    phi: nn.Module,
    phi_org: nn.Module,
    x: Tensor,          # Clean images, shape (B, C, H, W)
    eps: float,
    alpha: float = 1/255,
    n_steps: int = 10,
) -> Tensor:
    """
    Computes the FARE loss for a batch:
        L_FARE(phi, x) = mean_i max_{||z-x_i||_inf <= eps} ||phi(z) - phi_org(x_i)||_2^2

    The inner maximization is solved by PGD (inner_pgd_maximization).

    Args:
        phi:      Fine-tuned encoder (trainable)
        phi_org:  Original frozen encoder (reference)
        x:        Batch of clean images (B, C, H, W) in [0, 1]
        eps:      ℓ∞ radius for adversarial perturbation
        alpha:    PGD step size
        n_steps:  Number of PGD inner steps

    Returns:
        Scalar mean FARE loss over the batch
    """
    # Find adversarial perturbations (no gradient needed through this call for outer loop)
    with torch.no_grad():
        target_embedding = phi_org(x)  # shape: (B, D); frozen

    z_adv = pgd_inner_maximization(phi, phi_org, x, eps, alpha, n_steps)

    # Outer loss: ||phi(z_adv) - phi_org(x)||_2^2
    adv_embedding = phi(z_adv)  # shape: (B, D)
    loss = torch.sum((adv_embedding - target_embedding.detach()) ** 2, dim=-1)
    return loss.mean()


def train_fare(
    phi: nn.Module,                         # CLIP vision encoder (ViT-L/14), initialized from phi_org
    phi_org: nn.Module,                     # Original frozen CLIP vision encoder
    dataloader: torch.utils.data.DataLoader,  # ImageNet images (no labels needed)
    eps: float,                             # ℓ∞ radius: 2/255 or 4/255
    n_epochs: int = 2,
    lr: float = 1e-5,
    weight_decay: float = 1e-4,
    beta1: float = 0.9,
    beta2: float = 0.95,
    pgd_steps: int = 10,
    pgd_alpha: float = 1/255,
    warmup_fraction: float = 0.07,          # Warmup to peak LR at 7% of total steps
) -> nn.Module:
    """
    Full FARE training loop.

    Fine-tunes phi (initialized from phi_org) using the FARE loss on unlabeled images.
    Only the vision encoder phi is updated; phi_org remains frozen throughout.
    The FARE loss uses only the class token output of the CLIP encoder (Appendix B.1).

    Args:
        phi:           Fine-tuned encoder (trainable ViT-L/14 copy of phi_org)
        phi_org:       Original frozen CLIP ViT-L/14 encoder
        dataloader:    ImageNet DataLoader (images only; batch_size=128; 224x224)
        eps:           ℓ∞ perturbation radius (2/255 for FARE2, 4/255 for FARE4)
        n_epochs:      Number of training epochs (2 in the paper)
        lr:            Peak learning rate (1e-5)
        weight_decay:  AdamW weight decay (1e-4)
        beta1:         AdamW β1 (0.9)
        beta2:         AdamW β2 (0.95)
        pgd_steps:     PGD inner steps (10)
        pgd_alpha:     PGD step size (1/255)
        warmup_fraction: Fraction of total steps for linear LR warmup (0.07)

    Returns:
        Fine-tuned phi (FARE-CLIP encoder)
    """
    # Freeze original encoder
    for p in phi_org.parameters():
        p.requires_grad_(False)
    phi_org.eval()

    optimizer = optim.AdamW(
        phi.parameters(),
        lr=lr,
        betas=(beta1, beta2),
        weight_decay=weight_decay,
    )

    total_steps = n_epochs * len(dataloader)
    warmup_steps = int(warmup_fraction * total_steps)

    # Cosine LR schedule with linear warmup
    def lr_lambda(step: int) -> float:
        if step < warmup_steps:
            return float(step) / max(1, warmup_steps)
        progress = float(step - warmup_steps) / max(1, total_steps - warmup_steps)
        return 0.5 * (1.0 + torch.cos(torch.tensor(3.14159265 * progress)).item())

    scheduler = optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)

    phi.train()
    step = 0
    for epoch in range(n_epochs):
        for batch in dataloader:
            # DataLoader yields (images, labels) from ImageNet; labels are discarded
            if isinstance(batch, (list, tuple)):
                x = batch[0]  # images only
            else:
                x = batch
            x = x.cuda()

            loss = fare_loss(phi, phi_org, x, eps=eps, alpha=pgd_alpha, n_steps=pgd_steps)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            scheduler.step()
            step += 1

    return phi


def embedding_preservation_bound(
    phi_ft_x: Tensor,   # Fine-tuned embedding ϕ_FT(x), shape (D,) or (B, D)
    phi_org_x: Tensor,  # Original embedding ϕ_Org(x), shape (D,) or (B, D)
) -> Tensor:
    """
    Computes the bound from Theorem 3.1:
        |cos(phi_FT(x), psi(t)) - cos(phi_Org(x), psi(t))|
        <= min( ||phi_FT - phi_Org|| / ||phi_FT||,
                ||phi_FT - phi_Org|| / ||phi_Org|| )

    This gives an upper bound on how much cosine similarity with any
    text embedding can change after fine-tuning.

    Args:
        phi_ft_x:  Fine-tuned vision embedding
        phi_org_x: Original vision embedding (same input x)

    Returns:
        Upper bound on cosine similarity change (scalar per sample)
    """
    diff_norm = torch.norm(phi_ft_x - phi_org_x, p=2, dim=-1)
    ft_norm = torch.norm(phi_ft_x, p=2, dim=-1)
    org_norm = torch.norm(phi_org_x, p=2, dim=-1)

    bound = torch.minimum(diff_norm / ft_norm.clamp(min=1e-8),
                           diff_norm / org_norm.clamp(min=1e-8))
    return bound
