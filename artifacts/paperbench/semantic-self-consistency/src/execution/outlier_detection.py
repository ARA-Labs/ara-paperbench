"""
Semantic Self-Consistency — Outlier Detection Methods

Implements KNN, Isolation Forest, and One-class SVM filtering of LLM responses
based on their BERT-variant embedding representations, as described in Section 4.2
of Knappe et al., NeurIPS 2024.

After filtering, standard majority vote is applied to the remaining inlier responses.
"""

import numpy as np
from typing import List, Optional, Tuple
from collections import defaultdict


def extract_answer(response: str) -> Optional[str]:
    """
    Parse final answer from CoT response. See semantic_consistency.py for full docstring.
    """
    marker = "the answer is"
    lower = response.lower()
    idx = lower.rfind(marker)
    if idx == -1:
        return None
    answer = response[idx + len(marker):].strip().strip(". \t\n()[]")
    return answer if answer else None


def majority_vote_filtered(answers: List[Optional[str]]) -> Optional[str]:
    """Majority vote over a filtered set of answers."""
    counts: dict = defaultdict(int)
    for a in answers:
        if a is not None:
            counts[a] += 1
    if not counts:
        return None
    return max(counts, key=lambda k: counts[k])


def knn_outlier_filter(
    embeddings: np.ndarray,
    n_neighbors: int = 5,
    threshold_percentile: float = 90.0,
    algorithm: str = "ball_tree",
    metric: str = "euclidean"
) -> np.ndarray:
    """
    K-Nearest Neighbor outlier filtering (Section 4.2, Appendix I.2.1).

    Computes average distance from each embedding to its n_neighbors nearest neighbors.
    Removes the top (100 - threshold_percentile)% of points with highest average distances.

    Best configuration: n_neighbors=5, euclidean metric, ball_tree algorithm, threshold=90%.
    Average accuracy (best config): 56.18% averaged across all models and datasets.

    Args:
        embeddings: Array of shape (k, hidden_size).
        n_neighbors: Number of nearest neighbors (default 5, best config per paper).
        threshold_percentile: Retain points below this percentile of avg distances (default 90).
        algorithm: Algorithm for nearest neighbor computation ("ball_tree" per paper).
        metric: Distance metric ("euclidean" per paper).

    Returns:
        Boolean inlier mask of shape (k,); True = inlier (keep), False = outlier (remove).
    """
    from sklearn.neighbors import NearestNeighbors

    k = len(embeddings)
    if k <= n_neighbors:
        # Not enough points to apply KNN; keep all
        return np.ones(k, dtype=bool)

    nn = NearestNeighbors(
        n_neighbors=n_neighbors,
        algorithm=algorithm,
        metric=metric
    )
    nn.fit(embeddings)
    distances, _ = nn.kneighbors(embeddings)  # shape: (k, n_neighbors)

    avg_distances = distances.mean(axis=1)  # shape: (k,)

    threshold = np.percentile(avg_distances, threshold_percentile)
    inlier_mask = avg_distances <= threshold  # keep points below threshold

    # Ensure at least 1 inlier
    if not np.any(inlier_mask):
        inlier_mask = np.ones(k, dtype=bool)

    return inlier_mask


def isolation_forest_filter(
    embeddings: np.ndarray,
    n_estimators: int = 200,
    contamination: str = "auto",
    max_samples: str = "auto"
) -> np.ndarray:
    """
    Isolation Forest outlier filtering (Section 4.2, Appendix I.2.2).

    Best configuration: n_estimators=200, contamination=auto, max_samples=auto.
    Average accuracy (best config): 58.56% averaged across all models and datasets.

    Anomaly score: s(x, n) = 2^{-E(h(x))/c(n)}
    where h(x) = path length to isolate x, c(n) = average path length for n samples.

    Args:
        embeddings: Array of shape (k, hidden_size).
        n_estimators: Number of base estimators (default 200, best config per paper).
        contamination: Expected fraction of outliers; "auto" uses original paper threshold.
        max_samples: Samples per estimator; "auto" uses min(256, n_samples).

    Returns:
        Boolean inlier mask of shape (k,); True = inlier, False = outlier.
    """
    from sklearn.ensemble import IsolationForest

    k = len(embeddings)
    if k < 2:
        return np.ones(k, dtype=bool)

    iso_forest = IsolationForest(
        n_estimators=n_estimators,
        contamination=contamination,
        max_samples=max_samples
    )
    # predict returns 1 for inliers, -1 for outliers
    predictions = iso_forest.fit_predict(embeddings)
    inlier_mask = predictions == 1

    # Ensure at least 1 inlier
    if not np.any(inlier_mask):
        inlier_mask = np.ones(k, dtype=bool)

    return inlier_mask


def one_class_svm_filter(
    embeddings: np.ndarray,
    kernel: str = "linear",
    nu: float = 0.01,
    gamma: str = "scale"
) -> np.ndarray:
    """
    One-class SVM outlier filtering (Section 4.2, Appendix I.2.3).

    Objective: min_{omega, zeta} (1/2)*omega^T*omega + C*sum(zeta_i)
    Best configuration: linear kernel, nu=0.01, gamma=scale.
    Average accuracy (best config): 55.17% averaged across all models and datasets.

    Args:
        embeddings: Array of shape (k, hidden_size).
        kernel: SVM kernel type ("linear" is best config per paper).
        nu: Upper bound on fraction of training errors and lower bound on fraction
            of support vectors (0.01 per paper).
        gamma: Kernel coefficient; "scale" = 1/(n_features * X.var()).

    Returns:
        Boolean inlier mask of shape (k,); True = inlier, False = outlier.
    """
    from sklearn.svm import OneClassSVM

    k = len(embeddings)
    if k < 2:
        return np.ones(k, dtype=bool)

    oc_svm = OneClassSVM(
        kernel=kernel,
        nu=nu,
        gamma=gamma
    )
    # predict returns 1 for inliers, -1 for outliers
    predictions = oc_svm.fit_predict(embeddings)
    inlier_mask = predictions == 1

    # Ensure at least 1 inlier
    if not np.any(inlier_mask):
        inlier_mask = np.ones(k, dtype=bool)

    return inlier_mask


def outlier_filtered_self_consistency(
    responses: List[str],
    embeddings: np.ndarray,
    method: str = "isolation_forest"
) -> Optional[str]:
    """
    Apply outlier detection filtering to embeddings, then standard majority vote
    on the remaining (inlier) responses.

    Args:
        responses: List of k LLM responses (full CoT text).
        embeddings: Array of shape (k, hidden_size) of precomputed embeddings.
        method: Outlier detection method: "knn", "isolation_forest", or "one_class_svm".

    Returns:
        Selected final answer after filtering and majority vote.
    """
    k = len(responses)

    if method == "knn":
        inlier_mask = knn_outlier_filter(embeddings)
    elif method == "isolation_forest":
        inlier_mask = isolation_forest_filter(embeddings)
    elif method == "one_class_svm":
        inlier_mask = one_class_svm_filter(embeddings)
    else:
        raise ValueError(f"Unknown method: {method}. Choose knn, isolation_forest, one_class_svm.")

    # Filter responses to inliers
    filtered_responses = [responses[i] for i in range(k) if inlier_mask[i]]

    if not filtered_responses:
        filtered_responses = responses  # fallback: use all

    # Extract answers and apply majority vote
    answers = [extract_answer(r) for r in filtered_responses]
    return majority_vote_filtered(answers)
