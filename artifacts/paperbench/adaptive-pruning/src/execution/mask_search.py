"""
Binary Search for Block Selection under Sparsity Constraint.

Implements the efficient block search from Section 4.2 and Appendix C:
- Sort blocks by salience density (salience / param_count)
- Binary search for top-i blocks satisfying the sparsity constraint γ_t

Parameter count model (Eq. 6, 10-12 for RoBERTa-base):
  C(Θ_t; M_t) ≈ d_m * Σ_i (4 * n_h^i * d_h + 2 * n_f^i)
  
  For RoBERTa-base:
    C_head = 4 * d_m * d_m/n_h = 4 * 768 * 64 = 196608   (Eq. 10)
    C_neuron = 2 * d_m = 2 * 768 = 1536                   (Eq. 11)
    C_dimension = n_L * (4*d_m + 2*n_f) = 12*(4*768+2*3072) = 110592  (Eq. 12)
"""

import torch
from typing import List, Tuple, Dict
from enum import IntEnum


class BlockType(IntEnum):
    """Block category function f(b_i) from Eq. 13."""
    HEAD = 0       # Attention head
    NEURON = 1     # FFN neuron
    DIMENSION = 2  # Hidden dimension


def compute_roberta_base_block_params() -> Dict[str, int]:
    """
    Compute parameter counts for RoBERTa-base blocks (Eqs. 10-12).
    
    RoBERTa-base: d_m=768, n_L=12, n_h=12, d_h=64, n_f=3072
    """
    d_m, n_L, n_h, d_h, n_f = 768, 12, 12, 64, 3072
    
    C_head = 4 * d_m * d_h              # 4 * 768 * 64 = 196608
    C_neuron = 2 * d_m                   # 2 * 768 = 1536
    C_dimension = n_L * (4 * d_m + 2 * n_f)  # 12 * (3072 + 6144) = 110592
    
    return {"head": C_head, "neuron": C_neuron, "dimension": C_dimension}


def compute_top_i_params(
    sorted_blocks: List[Tuple[float, BlockType, int, int]],  # (salience_density, type, layer, idx)
    i: int,
    d_m_full: int,
    n_L: int,
    n_h_per_layer: int,
    d_h: int,
    n_f_per_layer: int,
) -> int:
    """
    Compute parameter count for top-i blocks (Eq. 14).
    
    C_{top-i} = (4 * d_h' * n_h' + 2 * n_f') * d_m'
    
    where:
        n_h' = Σ_{j=0}^{i-1} δ(0, f(b_j))  — number of head blocks in top-i
        n_f' = Σ_{j=0}^{i-1} δ(1, f(b_j))  — number of neuron blocks in top-i
        d_m' = Σ_{j=0}^{i-1} δ(2, f(b_j))  — number of dimension blocks in top-i
    
    δ(i, j) = 1 if i==j else 0 (Kronecker delta)
    
    Args:
        sorted_blocks: Blocks sorted by salience density (descending)
        i: Number of top blocks to count
        d_m_full: Full hidden dimension
        n_L: Number of layers
        n_h_per_layer: Number of attention heads per layer
        d_h: Head dimension
        n_f_per_layer: FFN intermediate dimension
    
    Returns:
        Approximate parameter count for the top-i configuration
    """
    top_i = sorted_blocks[:i]
    
    # Count retained blocks by type (Kronecker delta)
    n_h_prime = sum(1 for _, btype, _, _ in top_i if btype == BlockType.HEAD)
    n_f_prime = sum(1 for _, btype, _, _ in top_i if btype == BlockType.NEURON)
    d_m_prime = sum(1 for _, btype, _, _ in top_i if btype == BlockType.DIMENSION)
    
    # Parameter count: (4 * d_h' * n_h' + 2 * n_f') * d_m'
    # Note: d_h' is constant (head dimension doesn't change with pruning heads)
    param_count = (4 * d_h * n_h_prime + 2 * n_f_prime) * d_m_prime
    return param_count


def binary_search_blocks(
    sorted_blocks: List[Tuple[float, BlockType, int, int]],
    original_param_count: int,
    target_sparsity: float,   # γ_t: fraction of params to PRUNE
    d_m: int,
    n_L: int,
    n_h: int,
    d_h: int,
    n_f: int,
) -> Tuple[List[int], List[int]]:
    """
    Binary search for top-i salient blocks satisfying sparsity constraint.
    
    Finds largest i such that C_{top-i} / C_0 >= (1 - γ_t).
    
    Since parameter count monotonically increases with i (blocks sorted by salience density),
    binary search works correctly.
    
    Args:
        sorted_blocks: All blocks sorted by salience density (descending)
        original_param_count: C_0 (total parameters before pruning)
        target_sparsity: γ_t (fraction to prune; keep (1 - γ_t) fraction)
        d_m, n_L, n_h, d_h, n_f: Model architecture parameters
    
    Returns:
        (retained_indices, pruned_indices): Block indices to retain and prune
    """
    N = len(sorted_blocks)
    target_count = original_param_count * (1 - target_sparsity)
    
    # Binary search: find largest i where C_{top-i} <= target_count
    lo, hi = 0, N
    while lo < hi:
        mid = (lo + hi + 1) // 2
        params = compute_top_i_params(sorted_blocks, mid, d_m, n_L, n_h, d_h, n_f)
        if params <= target_count:
            lo = mid
        else:
            hi = mid - 1
    
    retained_count = lo
    retained_indices = list(range(retained_count))
    pruned_indices = list(range(retained_count, N))
    
    return retained_indices, pruned_indices


def compute_cubic_sparsity(
    target_sparsity: float,  # γ_T
    t: int,                  # current step
    T: int,                  # total steps
) -> float:
    """
    Cubic gradual sparsity schedule (Appendix A).
    
    γ_t = γ_T + (1 - γ_T) * (1 - t/T)^3
    
    At t=0: γ_0 ≈ 1.0 (no pruning yet — keep all params)
    At t=T: γ_T (full target sparsity)
    """
    return target_sparsity + (1 - target_sparsity) * (1 - t / T) ** 3
