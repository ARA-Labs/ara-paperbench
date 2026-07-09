"""
Semantic Self-Consistency: CPW and SCW weighting algorithms.

Implements Centroid Proximity Weighting (CPW) and Semantic Consensus
Weighting (SCW) over BERT-based embeddings of chain-of-thought reasoning
paths. These are post-generation reweighting methods that replace the
standard majority vote in self-consistency.

Reference: Knappe et al., NeurIPS 2024, arXiv:2410.07839
"""

from __future__ import annotations
from collections import defaultdict
from typing import List, Tuple, Optional
import numpy as np


def parse_answer(text: str) -> Optional[str]:
    """
    Extract the final answer from a chain-of-thought response.

    Parses the full string after "The answer is", removing surrounding
    whitespace, trailing full stops, and parentheses.

    Args:
        text: Full generated text from the LLM.

    Returns:
        Extracted answer string, or None if the trigger phrase is not found.
    """
    trigger = "The answer is"
    if trigger not in text:
        return None
    answer = text.split(trigger)[-1]
    answer = answer.strip().rstrip(".").strip("()")
    return answer if answer else None


def centroid_proximity_weighting(
    embeddings: np.ndarray,          # shape: (k, d)
    answers: List[Optional[str]],    # length k; None = unparseable
) -> Optional[str]:
    """
    Centroid Proximity Weighting (CPW).

    Assigns weights inversely proportional to each embedding's normalized
    distance from the centroid. Aggregates weights per unique answer and
    returns the highest-weight answer.

    Algorithm:
      centroid = mean(embeddings, axis=0)
      distances[i] = ||embeddings[i] - centroid||_2
      norm_dists[i] = distances[i] / sum(distances)
      weights[i] = 1 / norm_dists[i]
      score[answer] = sum of weights[i] where answers[i] == answer
      return argmax(score)

    Args:
        embeddings: Array of k embedding vectors, shape (k, d).
        answers: List of k extracted answer strings (None = skip).

    Returns:
        The answer with the highest aggregated inverse-distance weight,
        or None if no valid answer exists.
    """
    valid = [(emb, ans) for emb, ans in zip(embeddings, answers) if ans is not None]
    if not valid:
        return None

    valid_embeddings = np.array([v[0] for v in valid])  # (n_valid, d)
    valid_answers = [v[1] for v in valid]

    centroid = valid_embeddings.mean(axis=0)            # (d,)
    distances = np.linalg.norm(valid_embeddings - centroid, axis=1)  # (n_valid,)

    total_dist = distances.sum()
    if total_dist == 0:
        # All embeddings identical: fall back to majority vote
        return _majority_vote(valid_answers)

    norm_dists = distances / total_dist                 # normalized
    weights = 1.0 / (norm_dists + 1e-12)               # inverse; guard divide-by-zero

    score: dict = defaultdict(float)
    for w, ans in zip(weights, valid_answers):
        score[ans] += w

    return max(score, key=score.__getitem__)


def semantic_consensus_weighting(
    embeddings: np.ndarray,          # shape: (k, d)
    answers: List[Optional[str]],    # length k
) -> Optional[str]:
    """
    Semantic Consensus Weighting (SCW).

    Computes pairwise cosine similarities between all embedding vectors.
    Each embedding's score is the sum of its cosine similarities to all
    others. Scores are aggregated per unique answer; the highest-score
    answer is returned.

    Algorithm:
      normed[i] = embeddings[i] / ||embeddings[i]||_2
      sim_matrix[i, j] = normed[i] . normed[j]   (cosine similarity)
      score_per_embedding[i] = sum_j sim_matrix[i, j]
      score[answer] = sum of score_per_embedding[i] where answers[i] == answer
      return argmax(score)

    Args:
        embeddings: Array of k embedding vectors, shape (k, d).
        answers: List of k extracted answer strings (None = skip).

    Returns:
        The answer with the highest aggregated cosine similarity score,
        or None if no valid answer exists.
    """
    valid = [(emb, ans) for emb, ans in zip(embeddings, answers) if ans is not None]
    if not valid:
        return None

    valid_embeddings = np.array([v[0] for v in valid])  # (n_valid, d)
    valid_answers = [v[1] for v in valid]

    # L2-normalize each row for cosine similarity computation
    norms = np.linalg.norm(valid_embeddings, axis=1, keepdims=True)  # (n_valid, 1)
    norms = np.where(norms == 0, 1e-12, norms)  # guard zero-norm
    normed = valid_embeddings / norms           # (n_valid, d)

    sim_matrix = normed @ normed.T              # (n_valid, n_valid)
    embedding_scores = sim_matrix.sum(axis=1)  # (n_valid,)

    score: dict = defaultdict(float)
    for s, ans in zip(embedding_scores, valid_answers):
        score[ans] += s

    return max(score, key=score.__getitem__)


def majority_vote_sc(answers: List[Optional[str]]) -> Optional[str]:
    """
    Standard self-consistency majority vote baseline.

    Counts occurrences of each unique extracted answer and returns the
    modal answer. Ignores None (unparseable) responses.

    Args:
        answers: List of extracted answer strings (None = skip).

    Returns:
        The most frequent answer, or None if all answers are None.
    """
    return _majority_vote([a for a in answers if a is not None])


def _majority_vote(answers: List[str]) -> Optional[str]:
    """Internal majority vote over a filtered list of answers."""
    if not answers:
        return None
    counts: dict = defaultdict(int)
    for a in answers:
        counts[a] += 1
    return max(counts, key=counts.__getitem__)


def top_prob_sample(text: str) -> Optional[str]:
    """
    Greedy / top-probability single sample baseline.

    Given a single generated text (from greedy decoding), extracts and
    returns the parsed answer.

    Args:
        text: Single LLM output from greedy decoding.

    Returns:
        Extracted answer string or None.
    """
    return parse_answer(text)
