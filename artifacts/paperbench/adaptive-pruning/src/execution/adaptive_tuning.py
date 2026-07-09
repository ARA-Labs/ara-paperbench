"""
Adaptive Tuning (AT) component of APT.

Implements Section 4.3: dynamically adds tuning parameters to salient APT adapters.

Key operations:
1. Compute adapter importance I(H_apt) = Σ_{i,j} S(W_B_{i,j})
2. Sort adapters by importance; select top-50% salient ones
3. Increase rank of selected adapters: r'_apt = floor(r_apt * Δ_t' / Δ_t)
4. Initialize new W_A rows with N(0, σ²); new W_B cols with zeros
5. Reset optimizer after each expansion (training stability)

param_resizing_strategy=tophalf_limited in scripts
tuning_expanding_ratio=4.0 in scripts
max_lora_r = lora_r * 8 = 64 in scripts
"""

import torch
import torch.nn as nn
import math
from typing import List, Dict, Tuple, Optional
from .apt_adapter import APTAdapter


def compute_adapter_importance(adapter: APTAdapter) -> float:
    """
    Compute importance score for an APT adapter.
    
    I(H_apt) = Σ_{i,j} S(W_B_{i,j})
    
    where S(W_B_{i,j}) = |W_B_{i,j} * dL/dW_B_{i,j}| (Eq. 3)
    
    Note: The paper proves S(W_B) == S(W_A), so either can be used.
    W_B is used by convention (as in the paper).
    
    Args:
        adapter: APT adapter with gradients computed for W_B
    
    Returns:
        Scalar importance score
    """
    if adapter.lora_B.grad is None:
        return 0.0
    
    # S(W_B_{i,j}) = |W_B_{i,j} * dL/dW_B_{i,j}|
    salience = (adapter.lora_B.data * adapter.lora_B.grad.data).abs()
    
    # Sum over all elements of W_B
    return salience.sum().item()


def select_top_half_adapters(
    adapter_importances: Dict[str, float]
) -> List[str]:
    """
    Select top-50% salient adapters for rank expansion.
    
    param_resizing_strategy=tophalf_limited in all training scripts.
    
    Args:
        adapter_importances: Dict mapping adapter name to importance score
    
    Returns:
        List of adapter names in the top-50% by importance
    """
    sorted_adapters = sorted(adapter_importances.items(), key=lambda x: x[1], reverse=True)
    top_half_count = len(sorted_adapters) // 2
    return [name for name, _ in sorted_adapters[:top_half_count]]


def compute_new_rank(
    current_rank: int,
    current_budget: float,   # Δ_t (current tuning parameter budget)
    new_budget: float,        # Δ_t' (new tuning parameter budget)
) -> int:
    """
    Compute new rank for adaptive tuning expansion.
    
    r'_apt = floor(r_apt * Δ_t' / Δ_t)   (Section 4.3)
    
    Args:
        current_rank: Current r_apt
        current_budget: Δ_t
        new_budget: Δ_t'
    
    Returns:
        New rank r'_apt (floored)
    """
    return math.floor(current_rank * new_budget / current_budget)


def expand_adapter_ranks(
    adapters: Dict[str, APTAdapter],
    current_budget: float,
    new_budget: float,
    max_rank: int = 64,   # max_lora_r = initial_r * 8 = 64
    expanding_ratio: float = 4.0,  # tuning_expanding_ratio from scripts
) -> Dict[str, int]:
    """
    Expand ranks of top-50% salient adapters.
    
    Returns dict of adapter_name -> new_rank for expanded adapters.
    Optimizer must be reset after this call.
    
    Args:
        adapters: All APT adapters
        current_budget: Current tuning budget Δ_t
        new_budget: New tuning budget Δ_t'
        max_rank: Maximum allowed rank (64 = 8 * initial_r)
        expanding_ratio: Expansion ratio for budget (4.0 from scripts)
    """
    # Step 1: Compute importance for all adapters
    importances = {
        name: compute_adapter_importance(adapter)
        for name, adapter in adapters.items()
    }
    
    # Step 2: Select top-50% salient adapters
    top_adapters = select_top_half_adapters(importances)
    
    # Step 3: Expand ranks of selected adapters
    expansions = {}
    for name in top_adapters:
        adapter = adapters[name]
        new_rank = min(
            compute_new_rank(adapter.r, current_budget, new_budget),
            max_rank
        )
        if new_rank > adapter.r:
            adapter.expand_rank(new_rank)
            expansions[name] = new_rank
    
    return expansions
