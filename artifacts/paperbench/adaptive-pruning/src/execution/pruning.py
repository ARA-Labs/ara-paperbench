"""
Low-Cost Adaptive LM Pruning for APT.

Based on: "APT: Adaptive Pruning and Tuning Pretrained Language Models
           for Efficient Training and Inference" (Zhao et al., ICML 2024)
arXiv:2401.12200

Implements:
  - Block type classification (head / neuron / dimension) — Equation 13
  - Parameter count computation — Equations 10, 11, 12, 14
  - Salience density computation (salience / parameter count)
  - Binary search block selection given sparsity constraint — Equation 6
  - Cubic sparsity schedule — γ_t = γ_T + (1-γ_T)(1-t/T)^3
  - Mask update with gradual decay (α = 0.01)
"""

import torch
from typing import List, Tuple, Dict
from enum import IntEnum


class BlockType(IntEnum):
    HEAD = 0       # MHA attention head block
    NEURON = 1     # FFN neuron block
    DIMENSION = 2  # Hidden dimension block (shared across all layers)


def count_head_params(d_m: int, n_h: int) -> int:
    """
    Number of parameters in one MHA attention head.
    C_head = 4 × d_m × d_m / n_h  (Equation 10)

    Args:
        d_m: model hidden dimension
        n_h: total number of attention heads (current)
    Returns:
        parameter count per head
    """
    return 4 * d_m * d_m // n_h


def count_neuron_params(d_m: int) -> int:
    """
    Number of parameters associated with one FFN neuron.
    C_neuron = 2 × d_m  (Equation 11)

    For gated FFN models (T5, LLaMA), use 3 × d_m instead of 2 × d_m.

    Args:
        d_m: model hidden dimension
    Returns:
        parameter count per neuron
    """
    return 2 * d_m


def count_dimension_params(n_L: int, d_m: int, n_f: int) -> int:
    """
    Number of parameters associated with one hidden dimension unit across all layers.
    C_dimension = n_L × (4 × d_m + 2 × n_f)  (Equation 12)

    Args:
        n_L: number of transformer layers
        d_m: current hidden dimension
        n_f: current number of FFN neurons per layer
    Returns:
        total parameter count for one dimension step
    """
    return n_L * (4 * d_m + 2 * n_f)


def compute_top_i_params(
    sorted_blocks: List[Tuple[BlockType, float]],  # (block_type, salience_density) sorted desc
    i: int,
    d_h: int,   # dimension per head (fixed by architecture)
) -> int:
    """
    Compute total parameter count of the LM retaining top-i blocks.
    (Equation 14)

    Args:
        sorted_blocks: list of (BlockType, salience_density) sorted by density descending
        i: number of top blocks to retain
        d_h: dimension per head (d_m / n_h_original)

    Returns:
        C_{top-i}: total parameter count of LM with top-i blocks retained
    """
    n_h_prime = sum(1 for btype, _ in sorted_blocks[:i] if btype == BlockType.HEAD)
    n_f_prime = sum(1 for btype, _ in sorted_blocks[:i] if btype == BlockType.NEURON)
    d_m_prime = sum(1 for btype, _ in sorted_blocks[:i] if btype == BlockType.DIMENSION)

    if d_m_prime == 0 or n_h_prime == 0:
        return 0
    return (4 * d_h * n_h_prime + 2 * n_f_prime) * d_m_prime


def compute_sparsity_schedule(
    t: int,
    T: int,
    gamma_T: float,
) -> float:
    """
    Cubic sparsity schedule.
    γ_t = γ_T + (1 - γ_T) * (1 - t/T)^3

    Args:
        t: current training step
        T: total pruning training steps
        gamma_T: final target sparsity (fraction of params pruned)

    Returns:
        gamma_t: sparsity constraint at step t
    """
    return gamma_T + (1 - gamma_T) * (1 - t / T) ** 3


def binary_search_top_blocks(
    sorted_blocks: List[Tuple[BlockType, float]],
    gamma_t: float,
    C_total: int,
    d_h: int,
) -> int:
    """
    Binary search for the maximum number of blocks to retain
    given sparsity constraint gamma_t.

    Finds max i such that:
      C_{top-i} <= (1 - gamma_t) * C_total

    Args:
        sorted_blocks: blocks sorted by salience density (descending)
        gamma_t: current sparsity constraint (fraction to be pruned)
        C_total: total parameter count of unpruned model
        d_h: dimension per head

    Returns:
        i_star: number of top-i blocks to retain
    """
    budget = (1 - gamma_t) * C_total
    lo, hi = 0, len(sorted_blocks)

    while lo < hi:
        mid = (lo + hi + 1) // 2
        if compute_top_i_params(sorted_blocks, mid, d_h) <= budget:
            lo = mid
        else:
            hi = mid - 1

    return lo


def update_masks(
    current_masks: Dict[str, torch.Tensor],
    retained_block_ids: set,
    alpha: float = 0.01,
) -> Dict[str, torch.Tensor]:
    """
    Gradually update binary pruning masks.

    Retained blocks: mask += α (clamped at 1)
    Pruned blocks:   mask -= α (clamped at 0)

    α = 0.01 (Appendix C): gradual decay prevents training instability.

    Args:
        current_masks: dict mapping block_id → mask tensor
        retained_block_ids: set of block_ids to retain (not pruned)
        alpha: mask update step size (0.01 from paper)

    Returns:
        updated masks dict
    """
    updated = {}
    for block_id, mask in current_masks.items():
        if block_id in retained_block_ids:
            updated[block_id] = torch.clamp(mask + alpha, max=1.0)
        else:
            updated[block_id] = torch.clamp(mask - alpha, min=0.0)
    return updated
