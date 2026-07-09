"""
Semantic Self-Consistency — Core Weighting Methods

Implements Centroid Proximity Weighting (CPW) and Semantic Consensus Weighting (SCW)
as described in Knappe et al., NeurIPS 2024.

These are inference-time post-processing methods applied after generating k chain-of-thought
responses from an LLM. They do NOT include LLM generation code, API wrappers, or data loading.
"""

import numpy as np
from typing import List, Tuple, Dict, Optional
from collections import defaultdict


def extract_answer(response: str) -> Optional[str]:
    """
    Parse the final answer from a chain-of-thought response.

    Looks for the pattern "The answer is <X>" and returns X after stripping
    whitespace, fullstops, and parentheses. Returns None if pattern not found.

    Args:
        response: Full text response from LLM including reasoning path and answer.

    Returns:
        Extracted answer string, or None if pattern not found.
    """
    marker = "the answer is"
    lower = response.lower()
    idx = lower.rfind(marker)
    if idx == -1:
        return None
    answer = response[idx + len(marker):].strip()
    # Strip trailing punctuation and parentheses
    answer = answer.strip(". \t\n()[]")
    return answer if answer else None


def majority_vote(answers: List[Optional[str]]) -> Optional[str]:
    """
    Standard self-consistency: select the most frequent answer.

    Args:
        answers: List of extracted answer strings (may include None for invalid parses).

    Returns:
        Most frequent non-None answer, or None if all answers are None.
    """
    counts: Dict[str, int] = defaultdict(int)
    for a in answers:
        if a is not None:
            counts[a] += 1
    if not counts:
        return None
    return max(counts, key=lambda k: counts[k])


def get_cls_embedding(reasoning_path: str, featurizer_model, featurizer_tokenizer) -> np.ndarray:
    """
    Extract [CLS] token embedding from a reasoning path using a BERT-variant featurizer.

    Args:
        reasoning_path: Full chain-of-thought response text to embed.
        featurizer_model: A HuggingFace AutoModel (e.g., SciBERT, RoBERTa) in eval mode.
        featurizer_tokenizer: Corresponding HuggingFace AutoTokenizer.

    Returns:
        CLS embedding vector of shape (hidden_size,) = (768,) for BERT-base variants.
    """
    import torch
    inputs = featurizer_tokenizer(
        reasoning_path,
        return_tensors="pt",
        truncation=True,
        max_length=512,
        padding=True
    )
    with torch.no_grad():
        outputs = featurizer_model(**inputs)
    # [CLS] token is the first token of last hidden state
    cls_embedding = outputs.last_hidden_state[:, 0, :].squeeze(0).cpu().numpy()
    return cls_embedding  # shape: (768,)


def centroid_proximity_weighting(
    embeddings: np.ndarray,
    answers: List[Optional[str]]
) -> Optional[str]:
    """
    Centroid Proximity Weighting (CPW): weight responses inversely proportional
    to their normalized Euclidean distance from the embedding centroid.

    Algorithm (Section 4.1.1):
    1. Compute centroid = mean(embeddings)
    2. Compute distances[i] = ||embeddings[i] - centroid||_2
    3. Normalize: norm_dist[i] = distances[i] / sum(distances)
    4. Weight: w[i] = 1 / norm_dist[i]
    5. Sum weights per unique answer; return argmax

    Args:
        embeddings: Array of shape (k, hidden_size) containing k embedding vectors.
        answers: List of k extracted answer strings (may include None).

    Returns:
        Selected answer string with highest aggregate weight, or None.
    """
    valid_pairs = [(emb, ans) for emb, ans in zip(embeddings, answers) if ans is not None]
    if not valid_pairs:
        return None

    valid_embeddings = np.array([p[0] for p in valid_pairs])  # (n_valid, hidden_size)
    valid_answers = [p[1] for p in valid_pairs]

    # Step 1: Compute centroid
    centroid = np.mean(valid_embeddings, axis=0)  # (hidden_size,)

    # Step 2: Euclidean distances to centroid
    diffs = valid_embeddings - centroid  # (n_valid, hidden_size)
    distances = np.linalg.norm(diffs, axis=1)  # (n_valid,)

    total_dist = np.sum(distances)
    if total_dist == 0:
        # All embeddings are identical; fall back to majority vote
        return majority_vote(valid_answers)

    # Step 3: Normalize distances
    norm_distances = distances / total_dist  # (n_valid,)

    # Step 4: Inverse weight (avoid division by zero)
    epsilon = 1e-10
    weights = 1.0 / (norm_distances + epsilon)  # (n_valid,)

    # Step 5: Sum weights per unique answer
    score_per_answer: Dict[str, float] = defaultdict(float)
    for w, ans in zip(weights, valid_answers):
        score_per_answer[ans] += w

    return max(score_per_answer, key=lambda k: score_per_answer[k])


def semantic_consensus_weighting(
    embeddings: np.ndarray,
    answers: List[Optional[str]]
) -> Optional[str]:
    """
    Semantic Consensus Weighting (SCW): weight each response by the sum of its
    cosine similarity to all other responses. Aggregate scores per unique answer.

    Algorithm (Section 4.1.2):
    For each embedding n_e:
        S(n_e) = sum over all n_i: cosine_similarity(n_e, n_i)
    Sum S values per unique answer; return argmax.

    Args:
        embeddings: Array of shape (k, hidden_size) containing k embedding vectors.
        answers: List of k extracted answer strings (may include None).

    Returns:
        Selected answer string with highest aggregate cosine similarity score, or None.
    """
    valid_pairs = [(emb, ans) for emb, ans in zip(embeddings, answers) if ans is not None]
    if not valid_pairs:
        return None

    valid_embeddings = np.array([p[0] for p in valid_pairs])  # (n_valid, hidden_size)
    valid_answers = [p[1] for p in valid_pairs]

    n = len(valid_embeddings)

    # Normalize embeddings for cosine similarity
    norms = np.linalg.norm(valid_embeddings, axis=1, keepdims=True)  # (n, 1)
    epsilon = 1e-10
    normed = valid_embeddings / (norms + epsilon)  # (n, hidden_size)

    # Pairwise cosine similarity matrix: sim[i,j] = cosine_sim(emb_i, emb_j)
    sim_matrix = normed @ normed.T  # (n, n)

    # Aggregate score per embedding = sum of its row in similarity matrix
    scores = np.sum(sim_matrix, axis=1)  # (n,)

    # Sum scores per unique answer
    score_per_answer: Dict[str, float] = defaultdict(float)
    for score, ans in zip(scores, valid_answers):
        score_per_answer[ans] += float(score)

    return max(score_per_answer, key=lambda k: score_per_answer[k])


def self_consistency_pipeline(
    responses: List[str],
    embeddings: np.ndarray,
    method: str = "scw"
) -> Optional[str]:
    """
    Full semantic self-consistency pipeline: parse answers from responses,
    then apply the selected weighting method.

    Args:
        responses: List of k LLM responses (full chain-of-thought text strings).
        embeddings: Precomputed array of shape (k, hidden_size).
        method: One of "majority_vote", "cpw", "scw".

    Returns:
        Selected final answer string, or None.
    """
    answers = [extract_answer(r) for r in responses]

    if method == "majority_vote":
        return majority_vote(answers)
    elif method == "cpw":
        return centroid_proximity_weighting(embeddings, answers)
    elif method == "scw":
        return semantic_consensus_weighting(embeddings, answers)
    else:
        raise ValueError(f"Unknown method: {method}. Choose from majority_vote, cpw, scw.")
