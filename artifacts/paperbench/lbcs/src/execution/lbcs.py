"""
LBCS: Lexicographic Bilevel Coreset Selection
Implements Algorithm 1 (LBCS) and Algorithm 2 (LexiFlow outer loop).
Paper: "Refined Coreset Selection: Towards Minimal Coreset Size under Model Performance Constraints"
"""
import torch
import torch.nn as nn
import numpy as np
from typing import Tuple, List, Optional, Callable


def evaluate_mask(
    mask: torch.Tensor,         # shape: (n,) binary float tensor
    model: nn.Module,
    dataset_x: torch.Tensor,    # shape: (n, *input_dims)
    dataset_y: torch.Tensor,    # shape: (n,) long
    inner_lr: float = 0.001,
    inner_epochs: int = 100,
    device: str = "cuda",
) -> Tuple[float, float]:
    """
    Evaluate a coreset mask by:
      1. Training model on selected coreset (inner loop)
      2. Computing f1 = full-dataset cross-entropy loss with trained model
      3. Computing f2 = L0 norm of mask (coreset size)

    Returns:
        f1: float — cross-entropy on full dataset with inner-loop trained model
        f2: float — coreset size (number of selected samples)
    """
    n = len(dataset_x)
    selected_idx = mask.bool()
    coreset_x = dataset_x[selected_idx].to(device)
    coreset_y = dataset_y[selected_idx].to(device)

    # Inner loop: train model on coreset
    model = model.to(device)
    model.train()
    optimizer = torch.optim.Adam(model.parameters(), lr=inner_lr)
    criterion = nn.CrossEntropyLoss()

    for _ in range(inner_epochs):
        optimizer.zero_grad()
        logits = model(coreset_x)
        loss = criterion(logits, coreset_y)
        loss.backward()
        optimizer.step()

    # Evaluate f1 on full dataset
    model.eval()
    full_x = dataset_x.to(device)
    full_y = dataset_y.to(device)
    with torch.no_grad():
        logits_full = model(full_x)
        f1 = criterion(logits_full, full_y).item()

    # f2 = coreset size
    f2 = float(mask.sum().item())

    return f1, f2


def lexicographic_compare(
    f1_new: float, f2_new: float,
    f1_cur: float, f2_cur: float,
    f1_thresh: float, f2_thresh: float,
) -> bool:
    """
    Returns True if (f1_new, f2_new) lexicographically dominates (f1_cur, f2_cur)
    under practical relations with thresholds (f1_thresh, f2_thresh).

    Practical lexicographic relation: values below the threshold are considered equivalent.
    """
    def leq_thresh(a, b, thresh):
        """Equivalent under threshold: both below thresh, or equal."""
        return (a <= thresh and b <= thresh) or (a == b)

    # Check f1 equivalence
    f1_eq = leq_thresh(f1_new, f1_cur, f1_thresh)

    if not f1_eq:
        # f1 differs (at least one is above threshold): prefer lower f1
        return f1_new < f1_cur and f1_new > f1_thresh  # new must also be meaningfully below cur
    else:
        # f1 equivalent: compare f2
        f2_eq = leq_thresh(f2_new, f2_cur, f2_thresh)
        if not f2_eq:
            return f2_new < f2_cur
        else:
            return False  # Both equivalent — no improvement


def lbcs(
    model_factory: Callable[[], nn.Module],   # factory to create fresh model
    dataset_x: torch.Tensor,                   # shape: (n, *input_dims)
    dataset_y: torch.Tensor,                   # shape: (n,) long
    k: int,                                    # predefined initial coreset size
    epsilon: float = 0.2,                      # voluntary performance compromise
    T: int = 500,                              # number of outer iterations
    inner_lr: float = 0.001,                   # inner loop learning rate
    inner_epochs: int = 100,                   # inner loop epochs per evaluation
    delta_init: float = 0.1,                   # initial step size for LexiFlow
    delta_lower: float = 1e-4,                 # restart threshold
    device: str = "cuda",
    group_size: int = 1,                       # for large-scale: group G examples
) -> Tuple[torch.Tensor, List[Tuple[float, float]]]:
    """
    LBCS Algorithm 1 + Algorithm 2 (LexiFlow).

    Args:
        model_factory: callable returning a fresh nn.Module (proxy network)
        dataset_x, dataset_y: full training dataset tensors
        k: initial coreset size
        epsilon: performance compromise (0.2 default)
        T: outer iterations
        inner_lr, inner_epochs: inner loop hyperparameters
        delta_init, delta_lower: LexiFlow step size parameters
        device: "cuda" or "cpu"
        group_size: G for group-based mask (1 = no grouping)

    Returns:
        best_mask: (n,) binary tensor — the selected coreset
        history: list of (f1, f2) tuples for each outer iteration
    """
    n = len(dataset_x)
    n_groups = n // group_size

    # Initialize mask randomly with ||m||_0 = k
    perm = torch.randperm(n_groups)
    k_groups = k // group_size
    mask_groups = torch.zeros(n_groups)
    mask_groups[perm[:k_groups]] = 1.0

    def expand_mask(mask_g: torch.Tensor) -> torch.Tensor:
        """Expand group mask to sample mask."""
        return mask_g.repeat_interleave(group_size)[:n]

    # Evaluate initial mask
    model0 = model_factory()
    m0 = expand_mask(mask_groups)
    f1_cur, f2_cur = evaluate_mask(m0, model0, dataset_x, dataset_y, inner_lr, inner_epochs, device)

    best_mask_groups = mask_groups.clone()
    best_f1, best_f2 = f1_cur, f2_cur
    incumbent_f1, incumbent_f2 = f1_cur, f2_cur

    # Running minima for practical thresholds
    f1_hat_star = f1_cur
    f2_hat_star = f2_cur

    history = [(f1_cur, f2_cur)]
    delta = delta_init
    t_prime = 0  # last improvement step
    e = 0        # consecutive no-improvement count
    r = 0        # restart count

    for t in range(1, T + 1):
        # Sample random direction
        u = torch.randn(n_groups)
        u = u / u.norm()

        # Try m + delta*u and m - delta*u
        improved = False
        for sign in [1.0, -1.0]:
            candidate_groups = mask_groups + sign * delta * u
            # Project to [0,1] and threshold
            candidate_groups = torch.clamp(candidate_groups, 0.0, 1.0)
            candidate_binary = (candidate_groups > 0.5).float()

            # Skip if identical to current
            if (candidate_binary == mask_groups).all():
                continue

            m_cand = expand_mask(candidate_binary)
            model_cand = model_factory()
            f1_cand, f2_cand = evaluate_mask(
                m_cand, model_cand, dataset_x, dataset_y, inner_lr, inner_epochs, device
            )

            # Compute practical thresholds
            f1_hat_star = min(f1_hat_star, f1_cand)
            f2_hat_star = min(f2_hat_star, f2_cand)
            f1_thresh = f1_hat_star * (1.0 + epsilon)
            f2_thresh = f2_hat_star

            # Lexicographic comparison against incumbent
            if lexicographic_compare(f1_cand, f2_cand, incumbent_f1, incumbent_f2, f1_thresh, f2_thresh):
                mask_groups = candidate_binary.clone()
                incumbent_f1, incumbent_f2 = f1_cand, f2_cand
                t_prime = t
                improved = True

                # Update global best
                if lexicographic_compare(f1_cand, f2_cand, best_f1, best_f2, f1_thresh, f2_thresh):
                    best_mask_groups = candidate_binary.clone()
                    best_f1, best_f2 = f1_cand, f2_cand
                break

        if not improved:
            e += 1

        history.append((incumbent_f1, incumbent_f2))

        # Step-size adaptation
        if e >= 2 * n_groups - 1:
            e = 0
            delta = delta * ((t_prime + 1.0) / (t + 1.0)) ** 0.5

        # Random restart
        if delta < delta_lower:
            r += 1
            noise = torch.randn(n_groups)
            mask_groups = torch.clamp(mask_groups + noise, 0.0, 1.0)
            mask_groups = (mask_groups > 0.5).float()
            delta = delta_init + r

    best_mask = expand_mask(best_mask_groups)
    return best_mask, history


def compute_test_accuracy(
    model: nn.Module,
    test_x: torch.Tensor,    # shape: (n_test, *input_dims)
    test_y: torch.Tensor,    # shape: (n_test,)
    device: str = "cuda",
) -> float:
    """
    Evaluate model test accuracy.

    Returns:
        accuracy: float in [0, 1]
    """
    model.eval().to(device)
    test_x, test_y = test_x.to(device), test_y.to(device)
    with torch.no_grad():
        logits = model(test_x)
        preds = logits.argmax(dim=1)
        accuracy = (preds == test_y).float().mean().item()
    return accuracy
