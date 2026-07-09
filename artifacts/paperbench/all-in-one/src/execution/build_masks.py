"""
Attention mask construction for the Simformer.

The attention mask M_E is a binary (d x d) matrix controlling which tokens
can attend to which in the transformer. It encodes the dependency structure
of the simulator's graphical model.

Three types:
  - Dense:      Full attention (all-ones). No structural prior.
  - Undirected: Symmetric mask from an undirected graphical model.
  - Directed:   Asymmetric mask from a DAG (Bayesian network).

Example masks are provided for the benchmark tasks from the paper:
  - Linear Gaussian (d=10): dense or chain-structured
  - Two Moons (d=4): dense
  - SLCP (d=13): dense
  - HMM (d=9): chain-structured (directed)
  - Tree (d=8): tree-structured (undirected)

Reference: Gloeckler et al., 2024, Section 3.2, Appendix A1.1
"""

import numpy as np
from typing import Optional


# ---------------------------------------------------------------------------
# Core mask builders
# ---------------------------------------------------------------------------

def dense_mask(d: int) -> np.ndarray:
    """
    Dense (full) attention mask: every token attends to every other token.

    This is the baseline used when no structural prior is available.
    Equivalent to standard transformer self-attention.

    Args:
        d: number of variables (tokens)

    Returns:
        mask: (d, d) all-ones matrix
    """
    return np.ones((d, d), dtype=np.float32)


def undirected_mask(adjacency: np.ndarray) -> np.ndarray:
    """
    Undirected attention mask from an undirected graphical model.

    Token i can attend to token j if and only if:
      - i == j (self-attention, diagonal), OR
      - adjacency[i, j] == 1 (edge exists in the undirected graph)

    The adjacency matrix must be symmetric. The diagonal is always added
    (every token attends to itself).

    Args:
        adjacency: (d, d) symmetric binary adjacency matrix of the
                   undirected graphical model. adjacency[i,j] = 1 means
                   variables i and j are neighbors.

    Returns:
        mask: (d, d) binary attention mask (symmetric, with diagonal)
    """
    d = adjacency.shape[0]
    assert adjacency.shape == (d, d), f"Expected ({d},{d}), got {adjacency.shape}"

    # Symmetrize (in case of minor asymmetries)
    adj_sym = np.maximum(adjacency, adjacency.T)

    # Add diagonal (self-attention)
    mask = np.clip(adj_sym + np.eye(d), 0, 1).astype(np.float32)

    return mask


def directed_mask(adjacency: np.ndarray) -> np.ndarray:
    """
    Directed attention mask from a DAG (Bayesian network).

    Token i can attend to token j if and only if:
      - i == j (self-attention, diagonal), OR
      - adjacency[j, i] == 1 (j is a parent of i in the DAG)

    Convention: adjacency[j, i] = 1 means there is a directed edge j -> i,
    i.e., j is a parent of i. Token i attends to its parents and itself.

    Note: For the Simformer, the directed mask is asymmetric. When combined
    with the condition mask M_C (observed variables), an additional step
    using the Webb et al. (2018) algorithm can be applied to add edges
    that preserve d-separation properties. This function provides the
    base DAG mask; see directed_mask_with_conditioning() for the full version.

    Args:
        adjacency: (d, d) binary adjacency matrix of the DAG.
                   adjacency[j, i] = 1 means j -> i (j is parent of i).

    Returns:
        mask: (d, d) binary attention mask (asymmetric, with diagonal).
              mask[i, j] = 1 means token i attends to token j.
    """
    d = adjacency.shape[0]
    assert adjacency.shape == (d, d), f"Expected ({d},{d}), got {adjacency.shape}"

    # mask[i, j] = 1 if j is a parent of i (adjacency[j, i] = 1)
    # OR if i == j (self-attention)
    mask = adjacency.T.copy().astype(np.float32)  # transpose: parents -> attending
    mask += np.eye(d)
    mask = np.clip(mask, 0, 1).astype(np.float32)

    return mask


def directed_mask_with_conditioning(
    adjacency: np.ndarray,
    condition_mask: np.ndarray,
) -> np.ndarray:
    """
    Directed attention mask with conditioning-aware edge augmentation.

    When some variables are observed (condition_mask == 1), additional edges
    may be needed to preserve d-separation properties. This implements the
    moralization step: if two parents share a common observed child, they
    must be connected (explaining away / Berkson's paradox).

    Based on Webb et al. (2018) for structure-preserving attention.

    Args:
        adjacency: (d, d) DAG adjacency matrix. adjacency[j, i] = 1 means j -> i.
        condition_mask: (d,) binary mask. 1 = observed, 0 = unobserved.

    Returns:
        mask: (d, d) augmented directed attention mask
    """
    d = adjacency.shape[0]

    # Start with the base directed mask
    mask = directed_mask(adjacency)

    # Moralization: for each observed node, connect all its parents
    for node in range(d):
        if condition_mask[node] == 1:
            # Find parents of this observed node
            parents = np.where(adjacency[:, node] == 1)[0]
            # Connect all pairs of parents (marry parents)
            for p1 in parents:
                for p2 in parents:
                    if p1 != p2:
                        mask[p1, p2] = 1.0
                        mask[p2, p1] = 1.0

    return mask


def ancestors_mask(adjacency: np.ndarray) -> np.ndarray:
    """
    Ancestor attention mask: token i attends to all its ancestors in the DAG.

    Uses transitive closure of the parent relation. This is a more permissive
    mask than the direct parent mask, allowing information flow across
    longer causal chains.

    Args:
        adjacency: (d, d) DAG adjacency matrix. adjacency[j, i] = 1 means j -> i.

    Returns:
        mask: (d, d) binary mask. mask[i, j] = 1 if j is an ancestor of i.
    """
    d = adjacency.shape[0]

    # Transitive closure via repeated matrix multiplication (boolean)
    reach = adjacency.T.copy().astype(np.float32)   # (d, d): reach[i, j] = j is parent of i
    closure = reach.copy()
    for _ in range(d - 1):
        closure = np.clip(closure + closure @ reach, 0, 1)

    # Add diagonal (self-attention)
    mask = np.clip(closure + np.eye(d), 0, 1).astype(np.float32)

    return mask


# ---------------------------------------------------------------------------
# Example masks for benchmark tasks
# ---------------------------------------------------------------------------

def linear_gaussian_mask(d_theta: int = 5, d_x: int = 5) -> np.ndarray:
    """
    Dense mask for the Linear Gaussian benchmark task.

    All variables are connected because the linear map A couples all
    theta dimensions to all x dimensions.

    Args:
        d_theta: number of parameter dimensions (default: 5)
        d_x: number of data dimensions (default: 5)

    Returns:
        mask: (d_theta + d_x, d_theta + d_x) dense mask
    """
    return dense_mask(d_theta + d_x)


def two_moons_mask() -> np.ndarray:
    """
    Dense mask for the Two Moons benchmark task.

    theta = (theta_1, theta_2), x = (x_1, x_2), d = 4.
    All variables are coupled through the nonlinear likelihood.

    Returns:
        mask: (4, 4) dense mask
    """
    return dense_mask(4)


def slcp_mask() -> np.ndarray:
    """
    Dense mask for the SLCP (Simple Likelihood Complex Posterior) task.

    theta = (theta_1, ..., theta_5), x = (x_1, ..., x_8), d = 13.
    Parameters define mean and covariance of a 4D Gaussian from which
    4 pairs of observations are drawn.

    Returns:
        mask: (13, 13) dense mask
    """
    return dense_mask(13)


def hmm_mask(n_timesteps: int = 3) -> np.ndarray:
    """
    Directed mask for the Hidden Markov Model (HMM) benchmark task.

    Structure:
      theta -> z_1 -> z_2 -> ... -> z_T
                |       |            |
                v       v            v
               x_1     x_2         x_T

    Variable ordering: [theta, z_1, ..., z_T, x_1, ..., x_T]
    Total d = 1 + 2*T (one param, T latent states, T observations)

    For the paper benchmark: 2 parameters, 5 latent states, 5 observations.
    Simplified here for illustration.

    Args:
        n_timesteps: number of HMM time steps T

    Returns:
        adjacency: (d, d) DAG adjacency matrix
        mask:      (d, d) directed attention mask
    """
    T = n_timesteps
    d = 1 + 2 * T   # theta + z_1..z_T + x_1..x_T

    adjacency = np.zeros((d, d), dtype=np.float32)

    # theta -> z_1
    adjacency[0, 1] = 1

    # z_t -> z_{t+1} (chain)
    for t in range(T - 1):
        adjacency[1 + t, 1 + t + 1] = 1

    # z_t -> x_t (emission)
    for t in range(T):
        adjacency[1 + t, 1 + T + t] = 1

    mask = directed_mask(adjacency)
    return adjacency, mask


def tree_mask() -> np.ndarray:
    """
    Undirected mask for the Tree benchmark task.

    Structure (example binary tree with 7 nodes + 1 root param):
      Variable ordering: [theta, v_1, v_2, v_3, v_4, v_5, v_6, v_7]

      theta - v_1
              / \\
            v_2  v_3
           / \\   / \\
         v_4 v_5 v_6 v_7

    This is a simplified tree for illustration. The paper's tree task
    has its own specific structure.

    Returns:
        adjacency: (8, 8) undirected adjacency matrix
        mask:      (8, 8) undirected attention mask
    """
    d = 8
    adjacency = np.zeros((d, d), dtype=np.float32)

    # theta (0) -- v_1 (1)
    adjacency[0, 1] = 1
    adjacency[1, 0] = 1

    # v_1 (1) -- v_2 (2), v_3 (3)
    adjacency[1, 2] = 1
    adjacency[2, 1] = 1
    adjacency[1, 3] = 1
    adjacency[3, 1] = 1

    # v_2 (2) -- v_4 (4), v_5 (5)
    adjacency[2, 4] = 1
    adjacency[4, 2] = 1
    adjacency[2, 5] = 1
    adjacency[5, 2] = 1

    # v_3 (3) -- v_6 (6), v_7 (7)
    adjacency[3, 6] = 1
    adjacency[6, 3] = 1
    adjacency[3, 7] = 1
    adjacency[7, 3] = 1

    mask = undirected_mask(adjacency)
    return adjacency, mask


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------

def mask_density(mask: np.ndarray) -> float:
    """
    Compute density of an attention mask (fraction of allowed connections).

    Returns:
        density: float in [0, 1]. 1.0 = fully dense, 0.0 = no connections.
    """
    return float(mask.sum() / mask.size)


def validate_mask(mask: np.ndarray, mask_type: str = "any") -> bool:
    """
    Validate an attention mask.

    Checks:
      - Square matrix
      - Binary values (0 or 1)
      - Diagonal is all ones (self-attention)
      - If mask_type == "undirected": symmetric
      - If mask_type == "directed": not necessarily symmetric

    Args:
        mask: (d, d) attention mask
        mask_type: "any", "undirected", or "directed"

    Returns:
        True if valid, False otherwise
    """
    d = mask.shape[0]
    if mask.shape != (d, d):
        return False

    # Binary
    if not np.all((mask == 0) | (mask == 1)):
        return False

    # Diagonal
    if not np.all(np.diag(mask) == 1):
        return False

    # Symmetry for undirected
    if mask_type == "undirected":
        if not np.allclose(mask, mask.T):
            return False

    return True
