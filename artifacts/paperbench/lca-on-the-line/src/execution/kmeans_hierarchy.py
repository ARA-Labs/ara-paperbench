"""
K-means Latent Hierarchy Construction
Builds a 9-layer hierarchical taxonomy from pretrained model features.
Reference: Appendix E.1 of LCA-on-the-Line paper.
"""
import numpy as np
from typing import Dict, Tuple, List
from sklearn.cluster import KMeans


def extract_class_average_features(
    model,               # Pretrained model M with feature extraction capability
    dataset,             # Dataset (X, Y) - image dataset with labels
    num_classes: int = 1000
) -> np.ndarray:
    """
    Extract per-class average feature representations from a pretrained model.
    
    For each class c in 0..K-1:
        class_features[c] = mean(M.features(X[Y==c]))
    
    Args:
        model: Pretrained model supporting feature extraction
        dataset: Image dataset with (image, label) pairs
        num_classes: Number of classes (1000 for ImageNet)
    
    Returns:
        np.ndarray of shape (num_classes, feature_dim) — per-class average features
    """
    import torch
    model.eval()
    
    class_feature_sums = np.zeros((num_classes, None))  # Will be initialized on first batch
    class_counts = np.zeros(num_classes)
    
    with torch.no_grad():
        for images, labels in dataset:  # Assumes batched DataLoader
            features = model.forward_features(images)  # Extract pre-classifier features
            features = features.cpu().numpy()
            
            for i, label in enumerate(labels.numpy()):
                if class_feature_sums.shape[1] is None:
                    class_feature_sums = np.zeros((num_classes, features.shape[1]))
                class_feature_sums[label] += features[i]
                class_counts[label] += 1
    
    # Average over samples per class
    class_avg_features = class_feature_sums / class_counts[:, np.newaxis]
    return class_avg_features  # shape: (K, feature_dim)


def build_kmeans_hierarchy(
    class_avg_features: np.ndarray,  # shape: (K, feature_dim)
    num_levels: int = 9,              # 2^i clusters for i=1..9; since 2^9=512 < 1000
    num_classes: int = 1000
) -> np.ndarray:
    """
    Build 9-layer K-means latent class hierarchy.
    
    For each level i=1..9: apply K-means with 2^i cluster centers.
    The LCA height for a class pair (c1, c2) is the minimum level at which
    both classes share a cluster. All classes share level 10 by default.
    
    Args:
        class_avg_features: Per-class average features, shape (K, feature_dim)
        num_levels: Number of hierarchy levels (9 for ImageNet's 1000 classes)
        num_classes: Number of classes K
    
    Returns:
        np.ndarray of shape (K, K) — pairwise LCA height matrix
        Entry [c1, c2] = deepest shared cluster level (lower = more similar)
    """
    # Run K-means at each level independently
    cluster_assignments = []  # List of length num_levels, each shape (K,)
    
    for level in range(1, num_levels + 1):
        n_clusters = 2 ** level  # 2, 4, 8, ..., 512
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        labels = kmeans.fit_predict(class_avg_features)
        cluster_assignments.append(labels)
    
    # Compute pairwise LCA heights
    # LCA height = index of first level (from most general=1 to most specific=9)
    # at which classes c1 and c2 share a cluster
    lca_heights = np.full((num_classes, num_classes), num_levels + 1, dtype=int)  # Default: 10
    
    # Fill diagonal with 0 (same class has 0 distance)
    np.fill_diagonal(lca_heights, 0)
    
    # For each level (from most specific to most general), update LCA heights
    for level_idx in range(num_levels - 1, -1, -1):  # 8, 7, ..., 0 (level 9 down to 1)
        level_labels = cluster_assignments[level_idx]
        
        for c1 in range(num_classes):
            for c2 in range(c1 + 1, num_classes):
                if level_labels[c1] == level_labels[c2]:
                    # Classes share a cluster at this level (finer resolution = higher level number)
                    current_height = level_idx + 1  # levels are 1-indexed in the paper
                    lca_heights[c1, c2] = min(lca_heights[c1, c2], current_height)
                    lca_heights[c2, c1] = lca_heights[c1, c2]
    
    return lca_heights  # shape: (K, K), lower values = more similar classes


def lca_height_to_distance_matrix(
    lca_heights: np.ndarray  # shape: (K, K), pairwise LCA heights
) -> np.ndarray:
    """
    Convert LCA height matrix to a distance matrix (higher height = more distant).
    
    Since shared cluster at a finer level (higher index) means classes are MORE similar,
    the distance is proportional to the LCA height.
    
    Args:
        lca_heights: Pairwise LCA height matrix from build_kmeans_hierarchy
    
    Returns:
        Distance matrix (can be used as soft label input, normalized externally)
    """
    # Higher LCA height means less similar classes (further apart in hierarchy)
    # Return as-is; normalization done in soft label construction
    return lca_heights.astype(float)
