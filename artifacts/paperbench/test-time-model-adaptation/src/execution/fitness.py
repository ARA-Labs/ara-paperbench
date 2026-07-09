"""
FOA Fitness Function (Equation 5)
Paper: "Test-Time Model Adaptation with Only Forward Passes" (ICML 2024)
arXiv: 2404.01650

Implements the unsupervised fitness function combining:
1. Prediction entropy: Σ_{x∈X_t} Σ_c -ŷ_c log ŷ_c
2. Activation distribution discrepancy:
   λ Σ_{i=1}^{N} [||μ_i(X_t) - μ^S_i||_2 + ||σ_i(X_t) - σ^S_i||_2]
"""

import torch
import torch.nn.functional as F
from typing import List


@torch.no_grad()
def prediction_entropy(logits: torch.Tensor) -> torch.Tensor:
    """
    Compute total prediction entropy over batch.

    Σ_{x∈X_t} Σ_{c∈C} -ŷ_c log ŷ_c

    Args:
        logits: Unnormalized predictions of shape (B, num_classes).

    Returns:
        Scalar entropy value (higher = more uncertain).
    """
    probs = F.softmax(logits, dim=-1)  # (B, num_classes)
    # Clamp for numerical stability
    log_probs = torch.log(probs.clamp(min=1e-10))
    # Per-sample entropy: Σ_c -ŷ_c log ŷ_c
    per_sample_entropy = -(probs * log_probs).sum(dim=-1)  # (B,)
    # Sum over batch (not mean, per Eq. 5)
    return per_sample_entropy.sum()


@torch.no_grad()
def activation_discrepancy(
    cls_features: List[torch.Tensor],
    source_means: List[torch.Tensor],
    source_stds: List[torch.Tensor],
) -> torch.Tensor:
    """
    Compute activation distribution discrepancy between test and source.

    Σ_{i=1}^{N} [||μ_i(X_t) - μ^S_i||_2 + ||σ_i(X_t) - σ^S_i||_2]

    Args:
        cls_features: List of N tensors, each (B, d) — CLS features per layer.
        source_means: List of N tensors, each (d,) — source layer means μ^S_i.
        source_stds: List of N tensors, each (d,) — source layer stds σ^S_i.

    Returns:
        Scalar discrepancy value.
    """
    device = cls_features[0].device
    total_discrepancy = torch.tensor(0.0, device=device)

    for i, feat in enumerate(cls_features):
        # feat: (B, d)
        mu_test = feat.mean(dim=0)     # (d,) — μ_i(X_t)
        sigma_test = feat.std(dim=0)   # (d,) — σ_i(X_t)

        mu_src = source_means[i].to(device)    # (d,)
        sigma_src = source_stds[i].to(device)  # (d,)

        # L2 norm of mean difference
        mean_diff = torch.norm(mu_test - mu_src, p=2)
        # L2 norm of std difference
        std_diff = torch.norm(sigma_test - sigma_src, p=2)

        total_discrepancy += mean_diff + std_diff

    return total_discrepancy


@torch.no_grad()
def foa_fitness(
    logits: torch.Tensor,
    cls_features: List[torch.Tensor],
    source_means: List[torch.Tensor],
    source_stds: List[torch.Tensor],
    lam: float = 0.4,
) -> float:
    """
    Full FOA fitness function (Equation 5).

    L(f_Θ(p; X_t)) = entropy_term + λ * discrepancy_term

    Lower fitness = better prompt candidate.

    Args:
        logits: Predicted logits of shape (B, num_classes).
        cls_features: List of N tensors, each (B, d) — per-layer CLS features.
        source_means: List of N tensors, each (d,) — source layer means.
        source_stds: List of N tensors, each (d,) — source layer stds.
        lam: Trade-off parameter λ (default 0.4 for BS=64 on ImageNet-C).

    Returns:
        Scalar fitness value as Python float.
    """
    # Term 1: Prediction entropy (summed over batch)
    entropy = prediction_entropy(logits)

    # Term 2: Activation discrepancy (summed over layers)
    discrepancy = activation_discrepancy(cls_features, source_means, source_stds)

    # Total fitness (Eq. 5)
    fitness = entropy + lam * discrepancy

    return float(fitness.item())


@torch.no_grad()
def entropy_only_fitness(logits: torch.Tensor) -> float:
    """
    Entropy-only fitness (baseline; shown to be insufficient in Table 9).

    This is the naive approach that fails when CMA is applied:
    - Leads to degenerate solutions (44.9% accuracy, 36.8% ECE for prompts+CMA+entropy)

    Args:
        logits: Predicted logits of shape (B, num_classes).

    Returns:
        Scalar entropy fitness as Python float.
    """
    return float(prediction_entropy(logits).item())
