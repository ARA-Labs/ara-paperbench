"""
Semantic Self-Consistency: Core algorithm implementations.

Implements:
  - Centroid Proximity Weighting (CPW) — Section 4.1.1
  - Semantic Consensus Weighting (SCW) — Section 4.1.2
  - Outlier removal methods: Isolation Forest, KNN, One-Class SVM — Section 4.2
  - Answer parsing and self-consistency baseline

NO scaffolding (no argparse, logging, distributed wrappers).
"""

from __future__ import annotations
from typing import List, Tuple, Dict, Optional
import numpy as np
from collections import defaultdict


# ---------------------------------------------------------------------------
# Answer parsing
# ---------------------------------------------------------------------------

def parse_answer(response: str) -> Optional[str]:
    """
    Extract the final answer from a chain-of-thought response.

    Parses the string after "The answer is", stripping whitespace,
    fullstops, and parentheses. Returns None if pattern not found.

    Args:
        response: Full model-generated chain-of-thought string.

    Returns:
        Parsed answer string, or None if not extractable.
    """
    marker = "The answer is"
    idx = response.find(marker)
    if idx == -1:
        return None
    answer = response[idx + len(marker):].strip()
    answer = answer.rstrip(".").strip()
    answer = answer.strip("()")
    return answer.strip().lower() if answer else None


# ---------------------------------------------------------------------------
# Embedding extraction
# ---------------------------------------------------------------------------

def get_cls_embedding(
    text: str,
    tokenizer,   # transformers PreTrainedTokenizer
    model,       # transformers PreTrainedModel
    device: str = "cpu",
) -> np.ndarray:
    """
    Produce a [CLS] token embedding for a full reasoning-path string.

    Args:
        text: The full chain-of-thought reasoning path.
        tokenizer: A HuggingFace tokenizer (SciBERT or RoBERTa).
        model: A HuggingFace model (SciBERT or RoBERTa).
        device: Torch device string.

    Returns:
        1-D numpy array of shape (hidden_dim,) — the [CLS] token embedding.
    """
    import torch
    inputs = tokenizer(
        text, return_tensors="pt", truncation=True, max_length=512, padding=True
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = model(**inputs)
    # CLS token is at position 0 of the last hidden state
    cls_embedding = outputs.last_hidden_state[:, 0, :].squeeze(0).cpu().numpy()
    return cls_embedding


# ---------------------------------------------------------------------------
# Self-consistency baseline
# ---------------------------------------------------------------------------

def self_consistency_vote(answers: List[Optional[str]]) -> Optional[str]:
    """
    Standard self-consistency: majority vote over extracted answers.

    Args:
        answers: List of k extracted answer strings (may contain None for
                 unparseable responses).

    Returns:
        The most frequent answer, or None if all answers are None.
    """
    counts: Dict[str, int] = defaultdict(int)
    for a in answers:
        if a is not None:
            counts[a] += 1
    if not counts:
        return None
    return max(counts, key=counts.__getitem__)


# ---------------------------------------------------------------------------
# Centroid Proximity Weighting (CPW)
# ---------------------------------------------------------------------------

def centroid_proximity_weighting(
    embeddings: np.ndarray,  # shape: (k, hidden_dim)
    answers: List[Optional[str]],
) -> Optional[str]:
    """
    Centroid Proximity Weighting (Section 4.1.1).

    Computes the centroid of k embeddings, assigns weights inversely
    proportional to normalized Euclidean distance from centroid, sums
    weights per unique answer, returns the highest-weight answer.

    Args:
        embeddings: Array of shape (k, hidden_dim) — one embedding per response.
        answers: List of k extracted answers (may contain None).

    Returns:
        The selected answer string, or None.
    """
    valid_mask = [a is not None for a in answers]
    if not any(valid_mask):
        return None

    valid_embs = embeddings[valid_mask]   # (n_valid, hidden_dim)
    valid_ans = [a for a, m in zip(answers, valid_mask) if m]

    centroid = valid_embs.mean(axis=0)  # (hidden_dim,)
    distances = np.linalg.norm(valid_embs - centroid, axis=1)  # (n_valid,)

    total_dist = distances.sum()
    if total_dist == 0:
        # All embeddings identical — fall back to majority vote
        return self_consistency_vote(valid_ans)

    norm_distances = distances / total_dist   # (n_valid,)
    weights = 1.0 / norm_distances            # (n_valid,) inverse weighting

    score_by_answer: Dict[str, float] = defaultdict(float)
    for i, ans in enumerate(valid_ans):
        score_by_answer[ans] += weights[i]

    return max(score_by_answer, key=score_by_answer.__getitem__)


# ---------------------------------------------------------------------------
# Semantic Consensus Weighting (SCW)
# ---------------------------------------------------------------------------

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Compute cosine similarity between two 1-D vectors."""
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / denom)


def semantic_consensus_weighting(
    embeddings: np.ndarray,  # shape: (k, hidden_dim)
    answers: List[Optional[str]],
) -> Optional[str]:
    """
    Semantic Consensus Weighting (Section 4.1.2).

    For each embedding, computes the sum of cosine similarities with all
    other embeddings. Aggregates scores by answer; selects highest-score answer.

    Args:
        embeddings: Array of shape (k, hidden_dim).
        answers: List of k extracted answers (may contain None).

    Returns:
        The selected answer string, or None.
    """
    valid_mask = [a is not None for a in answers]
    if not any(valid_mask):
        return None

    valid_embs = embeddings[valid_mask]   # (n_valid, hidden_dim)
    valid_ans = [a for a, m in zip(answers, valid_mask) if m]
    n = len(valid_embs)

    scores = np.zeros(n, dtype=float)
    for i in range(n):
        for j in range(n):
            scores[i] += cosine_similarity(valid_embs[i], valid_embs[j])

    score_by_answer: Dict[str, float] = defaultdict(float)
    for i, ans in enumerate(valid_ans):
        score_by_answer[ans] += scores[i]

    return max(score_by_answer, key=score_by_answer.__getitem__)


# ---------------------------------------------------------------------------
# Outlier removal methods
# ---------------------------------------------------------------------------

def isolation_forest_filter(
    embeddings: np.ndarray,  # shape: (k, hidden_dim)
    answers: List[Optional[str]],
    n_estimators: int = 200,
    contamination: str = "auto",
    max_samples: str = "auto",
) -> Optional[str]:
    """
    Isolation Forest outlier removal (Section 4.2, Appendix I.2.2).

    Fits IsolationForest on embeddings, removes predicted outliers,
    applies majority vote to remaining answers.

    Args:
        embeddings: Array of shape (k, hidden_dim).
        answers: List of k extracted answers.
        n_estimators: Number of base estimators (default=200 per paper).
        contamination: Fraction of outliers; 'auto' uses sklearn default.
        max_samples: Samples per tree; 'auto' = min(256, n_samples).

    Returns:
        Majority vote answer over inlier responses.
    """
    from sklearn.ensemble import IsolationForest

    valid_mask = np.array([a is not None for a in answers])
    if not any(valid_mask):
        return None

    valid_embs = embeddings[valid_mask]
    valid_ans = [a for a, m in zip(answers, valid_mask) if m]

    clf = IsolationForest(
        n_estimators=n_estimators,
        contamination=contamination,
        max_samples=max_samples,
        random_state=42,
    )
    labels = clf.fit_predict(valid_embs)   # 1 = inlier, -1 = outlier
    retained = [valid_ans[i] for i in range(len(valid_ans)) if labels[i] == 1]

    if not retained:
        return self_consistency_vote(valid_ans)
    return self_consistency_vote(retained)


def knn_outlier_filter(
    embeddings: np.ndarray,  # shape: (k, hidden_dim)
    answers: List[Optional[str]],
    n_neighbors: int = 5,
    threshold_pct: float = 90.0,
    algorithm: str = "ball_tree",
    metric: str = "euclidean",
) -> Optional[str]:
    """
    K-Nearest Neighbor outlier removal (Section 4.2, Appendix I.2.1).

    Computes average distance to 5 nearest neighbors; removes top-10%
    highest-distance embeddings; applies majority vote to remaining.

    Args:
        embeddings: Array of shape (k, hidden_dim).
        answers: List of k extracted answers.
        n_neighbors: Number of neighbors (default=5 per paper).
        threshold_pct: Percentile threshold; default=90 (remove top 10%).
        algorithm: sklearn algorithm; default='ball_tree'.
        metric: Distance metric; default='euclidean'.

    Returns:
        Majority vote answer over retained responses.
    """
    from sklearn.neighbors import NearestNeighbors

    valid_mask = np.array([a is not None for a in answers])
    if not any(valid_mask):
        return None

    valid_embs = embeddings[valid_mask]
    valid_ans = [a for a, m in zip(answers, valid_mask) if m]

    n = len(valid_embs)
    actual_neighbors = min(n_neighbors, n - 1)
    if actual_neighbors < 1:
        return self_consistency_vote(valid_ans)

    nbrs = NearestNeighbors(
        n_neighbors=actual_neighbors + 1,  # +1 because point is its own neighbor
        algorithm=algorithm,
        metric=metric,
    )
    nbrs.fit(valid_embs)
    distances, _ = nbrs.kneighbors(valid_embs)
    avg_distances = distances[:, 1:].mean(axis=1)   # exclude self (index 0)

    threshold = np.percentile(avg_distances, threshold_pct)
    retained = [valid_ans[i] for i in range(n) if avg_distances[i] <= threshold]

    if not retained:
        return self_consistency_vote(valid_ans)
    return self_consistency_vote(retained)


def ocsvm_outlier_filter(
    embeddings: np.ndarray,  # shape: (k, hidden_dim)
    answers: List[Optional[str]],
    kernel: str = "linear",
    nu: float = 0.01,
    gamma: str = "scale",
) -> Optional[str]:
    """
    One-Class SVM outlier removal (Section 4.2, Appendix I.2.3).

    Fits OneClassSVM on embeddings, removes predicted outliers,
    applies majority vote to remaining answers.

    Args:
        embeddings: Array of shape (k, hidden_dim).
        answers: List of k extracted answers.
        kernel: SVM kernel type; default='linear' per paper.
        nu: Upper bound on fraction of outliers; default=0.01.
        gamma: Kernel coefficient; default='scale'.

    Returns:
        Majority vote answer over inlier responses.
    """
    from sklearn.svm import OneClassSVM

    valid_mask = np.array([a is not None for a in answers])
    if not any(valid_mask):
        return None

    valid_embs = embeddings[valid_mask]
    valid_ans = [a for a, m in zip(answers, valid_mask) if m]

    clf = OneClassSVM(kernel=kernel, nu=nu, gamma=gamma)
    labels = clf.fit_predict(valid_embs)   # 1 = inlier, -1 = outlier
    retained = [valid_ans[i] for i in range(len(valid_ans)) if labels[i] == 1]

    if not retained:
        return self_consistency_vote(valid_ans)
    return self_consistency_vote(retained)


# ---------------------------------------------------------------------------
# Evaluation helper
# ---------------------------------------------------------------------------

def evaluate_accuracy(
    predictions: List[Optional[str]],
    ground_truths: List[str],
) -> float:
    """
    Compute accuracy (fraction correct) for a list of predictions.

    Args:
        predictions: Model predictions (may include None for abstentions).
        ground_truths: Reference answers (lower-cased strings expected).

    Returns:
        Accuracy as a float in [0, 1].
    """
    if not predictions:
        return 0.0
    correct = sum(
        1 for p, g in zip(predictions, ground_truths)
        if p is not None and p.strip().lower() == g.strip().lower()
    )
    return correct / len(predictions)
