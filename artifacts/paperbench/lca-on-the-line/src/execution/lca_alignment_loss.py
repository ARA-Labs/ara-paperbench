"""
LCA Alignment Loss (Algorithm 1 from paper)
For taxonomy-guided linear probe training.
Reference: Algorithm 1, Appendix E.2 of LCA-on-the-Line paper.
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from typing import Literal


def build_soft_label_matrix(
    lca_depth_matrix: np.ndarray,  # shape: (K, K), pairwise D^P_LCA distances
    temperature: float = 25.0
) -> torch.Tensor:
    """
    Construct normalized soft label matrix from LCA distance matrix.
    
    M_LCA = MinMax(M^T) where T is temperature (element-wise exponentiation).
    
    Args:
        lca_depth_matrix: Pairwise D^P_LCA distance matrix, shape (K, K)
        temperature: Temperature for scaling (default 25 from paper)
    
    Returns:
        Soft label matrix, shape (K, K), values in [0, 1]
        Row i contains soft labels for class i as ground truth
    """
    # Apply temperature scaling (element-wise exponentiation)
    M = lca_depth_matrix ** temperature
    
    # MinMax scaling to [0, 1]
    M_min = M.min()
    M_max = M.max()
    if M_max - M_min > 1e-8:
        M_normalized = (M - M_min) / (M_max - M_min)
    else:
        M_normalized = np.zeros_like(M)
    
    return torch.tensor(M_normalized, dtype=torch.float32)


def lca_alignment_loss(
    logits: torch.Tensor,       # shape: (batch_size, K)
    targets: torch.Tensor,      # shape: (batch_size,), integer class indices
    lca_matrix: torch.Tensor,   # shape: (K, K), M_LCA (already min-max normalized)
    alignment_mode: Literal['BCE', 'CE'] = 'CE',
    lambda_weight: float = 0.03
) -> torch.Tensor:
    """
    LCA Alignment Loss combining cross-entropy with hierarchical soft label loss.
    
    Algorithm 1 from the paper:
    total_loss = lambda * standard_CE_loss + soft_LCA_loss
    
    Args:
        logits: Raw model outputs, shape (batch_size, K)
        targets: Ground truth class indices, shape (batch_size,)
        lca_matrix: Pre-computed M_LCA = MinMax(M^T), shape (K, K)
        alignment_mode: 'BCE' or 'CE' for soft loss type ('CE' used in main paper)
        lambda_weight: Weight for standard CE loss (default 0.03 from paper)
    
    Returns:
        Scalar loss tensor
    """
    # Step 1: Compute reverse LCA matrix (ground truth index has value 1)
    reverse_lca_matrix = 1.0 - lca_matrix  # shape: (K, K)
    
    # Step 2: Compute predicted probabilities
    probs = F.softmax(logits, dim=1)  # shape: (batch_size, K)
    
    # Step 3: One-hot encode targets
    K = logits.shape[1]
    one_hot_targets = F.one_hot(targets, num_classes=K).float()  # (batch_size, K)
    
    # Step 4: Standard cross-entropy loss
    standard_loss = -torch.sum(one_hot_targets * torch.log(probs + 1e-10), dim=1)  # (batch_size,)
    
    # Steps 5-10: Soft loss
    soft_targets = reverse_lca_matrix[targets]  # (batch_size, K): soft labels for each sample
    
    if alignment_mode == 'BCE':
        criterion = nn.BCEWithLogitsLoss(reduction='none')
        soft_loss = torch.mean(criterion(logits, soft_targets), dim=1)  # (batch_size,)
    elif alignment_mode == 'CE':
        soft_loss = -torch.mean(soft_targets * torch.log(probs + 1e-10), dim=1)  # (batch_size,)
    else:
        raise ValueError(f"Unknown alignment_mode: {alignment_mode}. Use 'BCE' or 'CE'.")
    
    # Step 12: Combine losses
    total_loss = lambda_weight * standard_loss + soft_loss  # (batch_size,)
    
    # Step 13: Return mean over batch
    return torch.mean(total_loss)


def interpolate_weights(
    weights_ce: dict,    # State dict from CE-only trained model
    weights_soft: dict,  # State dict from CE+soft trained model
    alpha: float         # Weight for CE model: W_interp = alpha*W_CE + (1-alpha)*W_soft
) -> dict:
    """
    Linear interpolation between CE-only and CE+soft probe weights.
    
    W_interp = alpha * W_CE + (1-alpha) * W_{CE+soft}
    
    Alpha is selected on ID validation set to maximize Top-1 accuracy.
    Search range: alpha in {0.0, 0.1, 0.2, ..., 1.0}
    
    Args:
        weights_ce: State dict of CE-only trained linear probe
        weights_soft: State dict of CE+soft trained linear probe
        alpha: Interpolation coefficient (alpha=1.0 -> CE-only; alpha=0.0 -> CE+soft)
    
    Returns:
        Interpolated state dict
    """
    assert 0.0 <= alpha <= 1.0
    interpolated = {}
    for key in weights_ce:
        interpolated[key] = alpha * weights_ce[key] + (1.0 - alpha) * weights_soft[key]
    return interpolated
