"""
BBOX-ADAPTER: Energy-Based Model Adapter for Black-Box LLM Adaptation
Core implementation of the EBM adapter, ranking-based NCE loss, and
sentence-level beam search inference.

Reference: Sun et al., "BBOX-ADAPTER: Lightweight Adapting for Black-Box LLMs"
ICML 2024. arXiv:2402.08219
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.utils import spectral_norm
from transformers import AutoTokenizer, AutoModel
from typing import List, Tuple, Optional


class EBMAdapter(nn.Module):
    """
    Energy-Based Model Adapter g_theta(x, y) -> scalar score.

    Wraps a pretrained encoder (DeBERTa-v3 or BERT) with a scalar output head.
    The output represents the energy assigned to a (question, answer) pair.
    Higher energy = more likely to come from target domain.

    Architecture:
        - Backbone: deberta-v3-base (86M) / deberta-v3-large (304M) for
          StrategyQA/GSM8K/ScienceQA; bert-base-cased (110M) for TruthfulQA
        - Head: spectral-normalized linear layer, [CLS] -> scalar

    Equation (1):
        p_theta(y|x) = p_LLM(y|x) * exp(g_theta(x, y)) / Z_theta(x)
    """

    def __init__(self, model_name: str, max_length: int = 512):
        """
        Args:
            model_name: HuggingFace model identifier, e.g.:
                - "microsoft/deberta-v3-base"   (86M, StrategyQA/GSM8K/ScienceQA)
                - "microsoft/deberta-v3-large"  (304M, StrategyQA/GSM8K/ScienceQA)
                - "bert-base-cased"             (110M, TruthfulQA)
            max_length: Maximum tokenization length (default: 512)
        """
        super().__init__()
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.encoder = AutoModel.from_pretrained(model_name)
        hidden_size = self.encoder.config.hidden_size

        # Spectral-normalized linear head: [CLS] embedding -> scalar energy
        # Spectral normalization prevents sharp gradients during EBM training
        # (Du & Mordatch, 2019; Section 3.2)
        self.head = spectral_norm(nn.Linear(hidden_size, 1))
        self.max_length = max_length

    def encode(self, texts: List[str]) -> torch.Tensor:
        """
        Tokenize and encode a batch of (question + answer) text pairs.

        Args:
            texts: List[str] of concatenated "Question: ... Answer: ..." strings
        Returns:
            cls_embeddings: Tensor of shape (batch_size, hidden_size)
        """
        encoded = self.tokenizer(
            texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=self.max_length,
        )
        encoded = {k: v.to(next(self.parameters()).device) for k, v in encoded.items()}
        outputs = self.encoder(**encoded)
        # Use [CLS] token representation for sequence-level scoring
        cls_embeddings = outputs.last_hidden_state[:, 0, :]  # (batch, hidden)
        return cls_embeddings

    def forward(self, texts: List[str]) -> torch.Tensor:
        """
        Compute scalar energy scores g_theta(x, y) for a batch of text pairs.

        Args:
            texts: List[str] of (question, answer) concatenated strings
        Returns:
            scores: Tensor of shape (batch_size, 1) — scalar energy per text
        """
        cls_embeddings = self.encode(texts)  # (batch, hidden)
        scores = self.head(cls_embeddings)   # (batch, 1)
        return scores


def ranking_nce_loss(
    adapter: EBMAdapter,
    positive_texts: List[str],
    negative_texts: List[str],
    alpha: float = 1.0,
) -> torch.Tensor:
    """
    Compute the ranking-based NCE loss with spectral normalization regularization.

    Loss gradient (Equation 3):
        nabla_theta * l(theta) = nabla_theta {
            - E_{y+ ~ p_data}[g_theta(x, y+)] + alpha * E[g_theta(x, y+)^2]
            + E_{y- ~ p_theta}[g_theta(x, y-)] + alpha * E[g_theta(x, y-)^2]
        }

    The optimal theta satisfies: p_theta(x) = p_LLM(x) * exp(g_theta(x)) = p_data(x)

    Args:
        adapter: EBMAdapter instance
        positive_texts: List[str] of target-domain (positive) text pairs
                        y+ ~ p_data(y|x)
        negative_texts: List[str] of source-domain/generated (negative) text pairs
                        y- ~ p_theta(y|x)
        alpha: Regularization weight for spectral normalization terms (default 1.0)
    Returns:
        loss: Scalar tensor — NCE loss value to minimize
    """
    # Compute energy scores for positive and negative samples
    pos_scores = adapter(positive_texts)   # (n_pos, 1)
    neg_scores = adapter(negative_texts)   # (n_neg, 1)

    # Ranking NCE objective: maximize E[g(y+)] - log(sum exp(g(y_k)))
    # Minimization form (Equation 2):
    #   loss = -E[g(y+)] + log(sum_k exp(g(y_k)))
    all_scores = torch.cat([pos_scores, neg_scores], dim=0)  # (n_pos + n_neg, 1)
    log_partition = torch.logsumexp(all_scores, dim=0)       # scalar

    loss_nce = -pos_scores.mean() + log_partition

    # Spectral normalization regularization (stabilizes training)
    reg_pos = alpha * (pos_scores ** 2).mean()
    reg_neg = alpha * (neg_scores ** 2).mean()

    loss = loss_nce + reg_pos + reg_neg
    return loss


def sentence_level_beam_search(
    question: str,
    llm_generate_fn,
    adapter: EBMAdapter,
    beam_size: int = 3,
    candidates_per_beam: int = 3,
    max_steps: int = 10,
    stop_token: str = "####",
) -> str:
    """
    Adapted inference via sentence-level beam search (Section 3.3).

    Decomposes the full generation y = [s_1, s_2, ..., s_L] into sentence-level
    steps. At each step l, the LLM generates candidates_per_beam * beam_size new
    sentences; the adapter scores all partial chains and top-k beams are retained.

    Equation (4):
        p_theta(y|x) = exp(g_theta(s_1:L, x)) * prod_l p_LLM(s_l | x, s_1:l-1)

    Args:
        question: str — input question text
        llm_generate_fn: callable(prompt: str, n: int) -> List[str]
                         Black-box LLM sentence generation function.
                         Generates n next-sentence candidates given prompt.
        adapter: EBMAdapter — trained energy scorer
        beam_size: int k — number of beams maintained (default: 3)
        candidates_per_beam: int n — LLM samples per beam per step (default: 3)
        max_steps: int L — maximum sentence generation steps
        stop_token: str — termination token (e.g., "####" for GSM8K/StrategyQA)
    Returns:
        best_answer: str — highest-scoring complete generation
    """
    # Initialize beams: list of (partial_chain, adapter_score)
    beams: List[Tuple[str, float]] = [("", 0.0)]

    for step in range(max_steps):
        candidates: List[Tuple[str, float]] = []
        all_terminated = True

        for chain, _ in beams:
            if stop_token in chain:
                # Beam has already terminated — keep as-is
                candidates.append((chain, 0.0))  # score computed below
                continue

            all_terminated = False
            prompt = question + "\n" + chain if chain else question

            # Generate candidates_per_beam next-sentence continuations
            next_sentences: List[str] = llm_generate_fn(prompt, n=candidates_per_beam)

            for sent in next_sentences:
                extended_chain = chain + " " + sent if chain else sent
                candidates.append((extended_chain, 0.0))

        if all_terminated:
            break

        if not candidates:
            break

        # Score all candidate chains with adapter
        chain_texts = [f"{question} {c[0]}" for c in candidates]
        with torch.no_grad():
            scores = adapter(chain_texts).squeeze(-1)  # (n_candidates,)

        # Update candidates with computed scores
        scored: List[Tuple[str, float]] = [
            (candidates[i][0], scores[i].item()) for i in range(len(candidates))
        ]

        # Prune to top-k beams by adapter score
        scored.sort(key=lambda x: x[1], reverse=True)
        beams = scored[:beam_size]

    # Select highest-scoring complete generation
    if not beams:
        return ""
    best_answer = beams[0][0]
    return best_answer


def single_step_inference(
    question: str,
    llm_generate_fn,
    adapter: EBMAdapter,
    n_candidates: int = 3,
) -> str:
    """
    Single-step adapted inference variant (Section 4.4, Table 4).

    The LLM generates n_candidates complete answers in one shot; the adapter
    selects the best. Lower cost than full beam search but slightly lower accuracy.

    Args:
        question: str — input question text
        llm_generate_fn: callable(prompt: str, n: int) -> List[str]
                         Generates n complete answers.
        adapter: EBMAdapter — trained energy scorer
        n_candidates: int — number of complete answers to generate and score
    Returns:
        best_answer: str — adapter's top-scored complete answer
    """
    candidates: List[str] = llm_generate_fn(question, n=n_candidates)
    if not candidates:
        return ""

    texts = [f"{question} {c}" for c in candidates]
    with torch.no_grad():
        scores = adapter(texts).squeeze(-1)  # (n_candidates,)

    best_idx = scores.argmax().item()
    return candidates[best_idx]
