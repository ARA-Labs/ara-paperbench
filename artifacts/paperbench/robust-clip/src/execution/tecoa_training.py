"""
TeCoA: Text-guided Contrastive Adversarial Training (Mao et al., 2023)
Supervised adversarial fine-tuning baseline for CLIP vision encoder.

Reference: Schlarmann et al. (2024) - §3.2, Appendix B.1, B.5
Original TeCoA: Mao et al. (2023) ICLR - "Understanding zero-shot adversarial robustness
for large-scale models"

Used in FARE paper as the primary comparison baseline.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from typing import List


def compute_clip_zeroshot_logits(
    phi: nn.Module,
    psi: nn.Module,
    x: torch.Tensor,
    text_embeddings: torch.Tensor,
) -> torch.Tensor:
    """
    Compute CLIP zero-shot classification logits for TeCoA.

    f_k(phi, x) = cos(phi(x), psi(t_k)) for k = 1, ..., K

    Args:
        phi: CLIP vision encoder (being fine-tuned)
        psi: CLIP text encoder (frozen); NOT used in FARE but used in TeCoA
        x: Input images (B, 3, H, W)
        text_embeddings: Pre-computed text embeddings (K, D), already L2-normalized
            These are: psi(t_k) / ||psi(t_k)||_2 for each ImageNet class k

    Returns:
        logits: Cosine similarity logits (B, K)
    """
    # Compute image embeddings
    image_embeddings = phi.encode_image(x)  # (B, D), unnormalized

    # L2 normalize image embeddings
    image_embeddings_norm = F.normalize(image_embeddings, dim=-1)  # (B, D)

    # Cosine similarity = dot product of normalized vectors
    logits = image_embeddings_norm @ text_embeddings.T  # (B, K)
    return logits


def tecoa_loss(
    phi: nn.Module,
    psi: nn.Module,
    x: torch.Tensor,
    labels: torch.Tensor,
    text_embeddings: torch.Tensor,
) -> torch.Tensor:
    """
    TeCoA loss: cross-entropy on CLIP zero-shot logits (Equation 1, §3.2).

    L_TeCoA(y, f(phi, x)) = -log( exp(f_y) / sum_k exp(f_k) )

    Args:
        phi: CLIP vision encoder
        psi: CLIP text encoder (frozen)
        x: Input images (adversarially perturbed), (B, 3, H, W)
        labels: Integer class labels (B,), ImageNet class indices
        text_embeddings: Pre-computed L2-normalized text embeddings for K ImageNet classes (K, D)

    Returns:
        loss: Scalar cross-entropy loss
    """
    logits = compute_clip_zeroshot_logits(phi, psi, x, text_embeddings)
    loss = F.cross_entropy(logits, labels)
    return loss


def tecoa_pgd_step(
    phi: nn.Module,
    psi: nn.Module,
    x: torch.Tensor,
    labels: torch.Tensor,
    text_embeddings: torch.Tensor,
    epsilon: float,
    step_size: float,
    num_steps: int,
    momentum: float = 0.9,
) -> torch.Tensor:
    """
    PGD inner maximization for TeCoA (Equation 2, §3.2).

    Finds z* = argmax_{||z-x||_inf <= eps} L_TeCoA(y, f(phi, z))

    Args:
        phi: CLIP vision encoder (fine-tuned; gradients needed)
        psi: CLIP text encoder (frozen)
        x: Clean images (B, 3, H, W), values in [0, 1]
        labels: Integer class labels (B,)
        text_embeddings: Pre-computed L2-normalized text embeddings (K, D)
        epsilon: ℓ∞ radius
        step_size: PGD step size α (1/255)
        num_steps: Number of PGD steps (10)
        momentum: Momentum factor (0.9)

    Returns:
        z: Adversarial images (B, 3, H, W), values in [0, 1]
    """
    # Random initialization
    delta = torch.empty_like(x).uniform_(-epsilon, epsilon)
    delta = torch.clamp(x + delta, 0.0, 1.0) - x
    delta = delta.detach()
    grad_momentum = torch.zeros_like(x)

    for t in range(num_steps):
        delta.requires_grad_(True)
        loss = tecoa_loss(phi, psi, x + delta, labels, text_embeddings)
        grad = torch.autograd.grad(loss, delta)[0].detach()

        grad_norm = grad.abs().sum(dim=(1, 2, 3), keepdim=True) + 1e-12
        grad_normalized = grad / grad_norm
        grad_momentum = momentum * grad_momentum + grad_normalized

        delta_new = delta.detach() + step_size * grad_momentum.sign()
        delta_new = torch.clamp(delta_new, -epsilon, epsilon)
        delta_new = torch.clamp(x + delta_new, 0.0, 1.0) - x
        delta = delta_new.detach()

    return (x + delta).detach()
