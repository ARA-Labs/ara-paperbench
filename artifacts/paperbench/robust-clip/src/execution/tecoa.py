"""
TeCoA: Text-guided Contrastive Adversarial Training (Mao et al., 2023)
Baseline implementation stub for comparison with FARE.

Paper reference: Mao et al., "Understanding Zero-Shot Adversarial Robustness
                 for Large-Scale Models", ICLR 2023.
Implemented here following the description in Schlarmann et al., ICML 2024.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch import Tensor
from typing import Tuple


def zero_shot_logits(
    phi: nn.Module,
    psi: nn.Module,       # Frozen CLIP text encoder
    x: Tensor,            # Images, shape (B, C, H, W)
    text_embeddings: Tensor,  # Pre-computed text embeddings, shape (K, D)
) -> Tensor:
    """
    Computes CLIP zero-shot classification logits as cosine similarities.
    Equation from Section 3.1:
        f_k(phi, x) = cos(phi(x), psi(t_k))

    Args:
        phi:              CLIP vision encoder
        psi:              CLIP text encoder (frozen)
        x:                Batch of images, shape (B, C, H, W)
        text_embeddings:  Pre-computed and L2-normalized class text embeddings (K, D)

    Returns:
        Logits tensor of shape (B, K); cosine similarities
    """
    img_emb = phi(x)  # (B, D)
    img_emb_norm = F.normalize(img_emb, p=2, dim=-1)   # (B, D)
    text_emb_norm = F.normalize(text_embeddings, p=2, dim=-1)  # (K, D)
    logits = img_emb_norm @ text_emb_norm.T  # (B, K)
    return logits


def tecoa_loss(
    phi: nn.Module,
    text_embeddings: Tensor,   # Pre-computed ImageNet class text embeddings (K, D)
    x: Tensor,                 # Clean images (B, C, H, W)
    y: Tensor,                 # ImageNet class labels (B,)
    eps: float,
    alpha: float = 1/255,
    n_steps: int = 10,
) -> Tensor:
    """
    Computes the TeCoA adversarial training loss (Equation 1-2 of Schlarmann et al.):
        L_TeCoA = -log( exp(f_y(phi, z)) / sum_k exp(f_k(phi, z)) )
    where z = argmax_{||z-x||_inf <= eps} L_TeCoA(y, f(phi, z))

    Uses PGD for the inner maximization.

    Args:
        phi:              CLIP vision encoder (trainable)
        text_embeddings:  Fixed ImageNet class text embeddings (K, D)
        x:                Batch of clean images (B, C, H, W)
        y:                Ground-truth ImageNet class indices (B,)
        eps:              ℓ∞ perturbation radius
        alpha:            PGD step size
        n_steps:          PGD inner steps

    Returns:
        Mean TeCoA loss (scalar)
    """
    # PGD inner maximization
    delta = torch.empty_like(x).uniform_(-eps, eps)
    delta = torch.clamp(x + delta, 0.0, 1.0) - x

    for _ in range(n_steps):
        delta = delta.detach().requires_grad_(True)
        z = torch.clamp(x + delta, 0.0, 1.0)
        logits = zero_shot_logits(phi, None, z, text_embeddings)
        inner_loss = F.cross_entropy(logits, y)
        inner_loss.backward()

        with torch.no_grad():
            delta = delta + alpha * delta.grad.sign()
            delta = torch.clamp(delta, -eps, eps)
            delta = torch.clamp(x + delta, 0.0, 1.0) - x

    z_adv = (x + delta).detach()
    logits_adv = zero_shot_logits(phi, None, z_adv, text_embeddings)
    loss = F.cross_entropy(logits_adv, y)
    return loss
