"""
LCA Alignment Soft Loss for linear probing generalization improvement.

Implements Algorithm 1 from the paper:
  L = lambda * L_CE + L_soft_lca

Reference: Section 4.3.2, Appendix E.2 in the paper.

Hyperparameters (from paper):
  - lambda_weight = 0.03
  - temperature = 25
  - alignment_mode = 'CE'
"""
from __future__ import annotations
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from typing import Literal


def build_lca_soft_label_matrix(
    lca_dist_matrix: np.ndarray,
    temperature: float = 25.0,
) -> torch.Tensor:
    """
    Construct the normalized LCA soft label matrix from raw LCA distances.

    Steps (Appendix E.2):
    1. Apply temperature scaling: M_scaled = M ** temperature (elementwise power)
       Note: paper uses M^T notation for "M raised to temperature T" via min-max scaling
    2. Apply min-max normalization across all off-diagonal entries: M_LCA = MinMax(M_scaled)
    3. Soft labels for ground-truth y: 1 - M_LCA[y, :]  (ground-truth has value 1)

    Args:
        lca_dist_matrix: [K, K] numpy float array of raw LCA distances (0 on diagonal)
        temperature: Scaling temperature T (default 25)

    Returns:
        reverse_lca_matrix: [K, K] torch tensor; entry [y, k] = soft label weight for
                            class k given ground truth y. Diagonal = 1.0.
    """
    M = lca_dist_matrix.copy().astype(np.float64)
    # Temperature scaling (effectively sharpens the soft labels)
    M_scaled = M * temperature  # additive temperature scaling (see Appendix E.2)
    # Min-max normalize to [0, 1]
    m_min, m_max = M_scaled.min(), M_scaled.max()
    if m_max > m_min:
        M_norm = (M_scaled - m_min) / (m_max - m_min)
    else:
        M_norm = np.zeros_like(M_scaled)
    # Reverse: ground-truth class gets 1.0, distant classes get values close to 0
    reverse_lca = 1.0 - M_norm
    return torch.tensor(reverse_lca, dtype=torch.float32)


class LCAAlignmentLoss(nn.Module):
    """
    Combined Cross-Entropy + LCA Soft Label alignment loss.

    L = lambda_weight * L_CE + L_soft_lca   (Algorithm 1)

    Args:
        lca_dist_matrix: [K, K] numpy float array of LCA distances
        temperature: Temperature for soft label construction (default 25)
        lambda_weight: Weight for standard CE loss component (default 0.03)
        alignment_mode: 'CE' (cross-entropy soft loss) or 'BCE' (binary cross-entropy)
    """

    def __init__(
        self,
        lca_dist_matrix: np.ndarray,
        temperature: float = 25.0,
        lambda_weight: float = 0.03,
        alignment_mode: Literal["CE", "BCE"] = "CE",
    ):
        super().__init__()
        self.lambda_weight = lambda_weight
        self.alignment_mode = alignment_mode
        # Precompute reverse LCA matrix and register as buffer
        reverse_lca = build_lca_soft_label_matrix(lca_dist_matrix, temperature)
        self.register_buffer("reverse_lca_matrix", reverse_lca)  # [K, K]

    def forward(
        self,
        logits: torch.Tensor,  # [N, K]
        targets: torch.Tensor,  # [N] long
    ) -> torch.Tensor:
        """
        Compute combined loss.

        Args:
            logits: [N, K] raw model outputs (pre-softmax)
            targets: [N] ground-truth class indices

        Returns:
            scalar loss tensor
        """
        N, K = logits.shape
        probs = F.softmax(logits, dim=1)                    # [N, K]
        log_probs = F.log_softmax(logits, dim=1)            # [N, K]

        # Standard CE loss
        one_hot = F.one_hot(targets, num_classes=K).float()  # [N, K]
        standard_loss = -(one_hot * log_probs).sum(dim=1)   # [N]

        # Soft LCA loss
        soft_targets = self.reverse_lca_matrix[targets]      # [N, K]

        if self.alignment_mode == "BCE":
            bce = nn.BCEWithLogitsLoss(reduction="none")
            soft_loss = bce(logits, soft_targets).mean(dim=1)  # [N]
        else:  # CE mode (default, as in paper)
            soft_loss = -(soft_targets * log_probs).mean(dim=1)  # [N]

        total_loss = self.lambda_weight * standard_loss + soft_loss
        return total_loss.mean()


def weight_interpolation(
    model_ce: nn.Module,
    model_ce_soft: nn.Module,
    alpha: float,
) -> nn.Module:
    """
    Linear weight interpolation between CE-only and CE+soft models (Wortsman et al., 2022).

    W_interp = alpha * W_ce + (1 - alpha) * W_ce+soft

    Args:
        model_ce: Model trained with CE loss only
        model_ce_soft: Model trained with CE + soft LCA loss
        alpha: Interpolation coefficient; alpha=1.0 → pure CE; alpha=0.0 → pure CE+soft

    Returns:
        Interpolated model (in-place modification of model_ce_soft)
    """
    import copy
    interpolated = copy.deepcopy(model_ce)
    sd_ce = model_ce.state_dict()
    sd_soft = model_ce_soft.state_dict()
    sd_interp = {}
    for key in sd_ce:
        sd_interp[key] = alpha * sd_ce[key] + (1.0 - alpha) * sd_soft[key]
    interpolated.load_state_dict(sd_interp)
    return interpolated
