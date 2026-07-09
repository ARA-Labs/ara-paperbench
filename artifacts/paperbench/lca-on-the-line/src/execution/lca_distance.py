"""
LCA Distance Computation Module
Implements D^I_LCA (information content) and D^P_LCA (tree depth) variants.
Reference: Section 2, Appendix D.2.1 of LCA-on-the-Line paper.
"""
import math
from typing import Dict, Tuple, Optional
import numpy as np


def compute_node_probabilities(hierarchy: Dict[str, list], leaf_nodes: list) -> Dict[str, float]:
    """
    Compute probability of each node in hierarchy using uniform distribution over leaves.
    
    Leaf nodes receive p = 1/K where K = total number of leaf classes.
    Internal nodes receive probability equal to sum of descendants' probabilities.
    
    Args:
        hierarchy: Dict mapping node_id -> list of children node_ids
        leaf_nodes: List of leaf node ids (classes)
    
    Returns:
        Dict mapping node_id -> probability
    """
    K = len(leaf_nodes)
    probs: Dict[str, float] = {}
    
    # Assign uniform probability to leaves
    for leaf in leaf_nodes:
        probs[leaf] = 1.0 / K
    
    # Bottom-up pass: internal nodes sum children probabilities
    def compute_prob(node: str) -> float:
        if node in probs:
            return probs[node]
        children = hierarchy.get(node, [])
        p = sum(compute_prob(child) for child in children)
        probs[node] = p
        return p
    
    # Trigger computation for all internal nodes
    for node in hierarchy:
        if node not in probs:
            compute_prob(node)
    
    return probs


def compute_information_content(probs: Dict[str, float]) -> Dict[str, float]:
    """
    Compute information content I(node) = -log2(p(node)) for each node.
    
    Args:
        probs: Dict mapping node_id -> probability
    
    Returns:
        Dict mapping node_id -> information content
    """
    ic: Dict[str, float] = {}
    for node, p in probs.items():
        if p > 0:
            ic[node] = -math.log2(p)
        else:
            ic[node] = float('inf')
    return ic


def find_lca(node_a: str, node_b: str, parents: Dict[str, str]) -> str:
    """
    Find the Lowest Common Ancestor (LCA) of two nodes N_LCA(y', y).
    
    Args:
        node_a: First node (e.g., predicted class)
        node_b: Second node (e.g., ground truth class)
        parents: Dict mapping node_id -> parent_id (None for root)
    
    Returns:
        LCA node id
    """
    # Collect ancestors of node_a (including itself)
    ancestors_a = set()
    current = node_a
    while current is not None:
        ancestors_a.add(current)
        current = parents.get(current)
    
    # Walk up from node_b until we hit an ancestor of node_a
    current = node_b
    while current is not None:
        if current in ancestors_a:
            return current
        current = parents.get(current)
    
    raise ValueError(f"No LCA found for {node_a} and {node_b}")


def lca_distance_information_content(
    y_pred: str,
    y_true: str,
    ic: Dict[str, float],
    parents: Dict[str, str]
) -> float:
    """
    Compute D^I_LCA(y', y) = I(y) - I(N_LCA(y, y')).
    
    Primary variant used in main correlation experiments.
    
    Args:
        y_pred: Predicted class node id
        y_true: Ground truth class node id
        ic: Information content for each node
        parents: Parent map for LCA computation
    
    Returns:
        LCA distance (scalar >= 0)
    """
    lca_node = find_lca(y_pred, y_true, parents)
    return ic[y_true] - ic[lca_node]


def lca_distance_depth(
    y_pred: str,
    y_true: str,
    depths: Dict[str, int],
    parents: Dict[str, str]
) -> float:
    """
    Compute D^P_LCA(y', y) = (P(y) - P(LCA)) + (P(y') - P(LCA)).
    
    Used for linear probing experiments (soft label construction).
    Both terms included to counter tree imbalance.
    
    Args:
        y_pred: Predicted class node id
        y_true: Ground truth class node id
        depths: Dict mapping node_id -> tree depth (root=0)
        parents: Parent map for LCA computation
    
    Returns:
        LCA distance using depth (scalar >= 0)
    """
    lca_node = find_lca(y_pred, y_true, parents)
    depth_lca = depths[lca_node]
    return (depths[y_true] - depth_lca) + (depths[y_pred] - depth_lca)


def compute_average_lca_distance(
    predictions: list,  # list of predicted class ids
    ground_truths: list,  # list of ground truth class ids
    ic: Dict[str, float],
    parents: Dict[str, str],
    use_information_content: bool = True,
    depths: Optional[Dict[str, int]] = None
) -> float:
    """
    Compute average LCA distance D_LCA(model, M) over a dataset.
    
    Only computed over MISCLASSIFIED samples (y_i != y_hat_i).
    
    D_LCA(model, M) = (1/n) * sum_{i: y_i != y_hat_i} D_LCA(y_hat_i, y_i)
    
    Args:
        predictions: List of predicted class node ids (length n)
        ground_truths: List of ground truth class node ids (length n)
        ic: Information content for each node (for IC variant)
        parents: Parent map for LCA computation
        use_information_content: If True, use IC variant; else use depth variant
        depths: Node depths (required if use_information_content=False)
    
    Returns:
        Average LCA distance over misclassified samples
    """
    assert len(predictions) == len(ground_truths)
    n = len(predictions)
    
    total_lca = 0.0
    for y_pred, y_true in zip(predictions, ground_truths):
        if y_pred != y_true:  # Only count misclassified samples
            if use_information_content:
                total_lca += lca_distance_information_content(y_pred, y_true, ic, parents)
            else:
                assert depths is not None
                total_lca += lca_distance_depth(y_pred, y_true, depths, parents)
    
    return total_lca / n  # Divide by total n (not just misclassified count)


def compute_elca_distance(
    probs_matrix: np.ndarray,  # shape: (n_samples, K_classes)
    ground_truths: list,  # list of class indices (0..K-1)
    lca_distance_matrix: np.ndarray,  # shape: (K, K), precomputed pairwise LCA distances
) -> float:
    """
    Compute Expected LCA Distance (ELCA) over a dataset.
    
    D_ELCA(model, M) = (1/n) sum_i sum_k p_hat_{k,i} * D_LCA(k, y_i)
    
    NOTE: ELCA should NOT be compared across modalities (sensitive to logit temperature).
    
    Args:
        probs_matrix: Softmax probability outputs, shape (n_samples, K_classes)
        ground_truths: List of ground truth class indices, length n_samples
        lca_distance_matrix: Precomputed pairwise LCA distances, shape (K, K)
    
    Returns:
        Average ELCA distance over all samples
    """
    n_samples = len(ground_truths)
    total_elca = 0.0
    
    for i, y_true in enumerate(ground_truths):
        # Weighted sum of LCA distances for sample i
        lca_row = lca_distance_matrix[:, y_true]  # D_LCA(k, y_i) for all k
        total_elca += np.dot(probs_matrix[i], lca_row)
    
    return total_elca / n_samples


def compute_pairwise_lca_matrix(
    classes: list,  # list of class ids
    ic: Dict[str, float],
    parents: Dict[str, str],
    use_information_content: bool = True,
    depths: Optional[Dict[str, int]] = None
) -> np.ndarray:
    """
    Compute full n×n pairwise LCA distance matrix.
    
    Matrix[i, k] = D_LCA(class_i, class_k)
    
    Args:
        classes: Ordered list of class ids (length K)
        ic: Information content dict
        parents: Parent map
        use_information_content: Variant to use
        depths: Node depths (for depth variant)
    
    Returns:
        np.ndarray of shape (K, K)
    """
    K = len(classes)
    matrix = np.zeros((K, K))
    
    for i, class_i in enumerate(classes):
        for j, class_j in enumerate(classes):
            if i == j:
                matrix[i, j] = 0.0
            elif j > i:
                if use_information_content:
                    d = lca_distance_information_content(class_i, class_j, ic, parents)
                else:
                    assert depths is not None
                    d = lca_distance_depth(class_i, class_j, depths, parents)
                matrix[i, j] = d
                matrix[j, i] = d  # symmetric
    
    return matrix
