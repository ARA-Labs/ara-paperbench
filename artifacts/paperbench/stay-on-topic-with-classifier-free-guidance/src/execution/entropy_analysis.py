"""
Entropy and top-p overlap analysis for CFG vs. vanilla vs. instruction-tuned models.

Implements the analysis from Section 5 and Figures 6, 7 of:
"Stay on topic with Classifier-Free Guidance" (Sanchez et al., 2023)

Key experiments:
- Entropy: H(p) = -sum_k p_k log p_k  (scipy implementation)
- Top-p overlap: inner product of binary top-p indicator vectors
- Perplexity measurement and Spearman correlation
"""

import torch
import torch.nn.functional as F
import numpy as np
from typing import List, Tuple, Dict
from scipy.stats import entropy as scipy_entropy, spearmanr
from transformers import PreTrainedModel, PreTrainedTokenizer


def compute_logit_entropy(
    logits: torch.FloatTensor,  # shape: (seq_len, vocab_size) or (vocab_size,)
) -> float:
    """
    Compute Shannon entropy of logit distribution.

    H(p) = -sum_k p_k * log(p_k)

    Uses scipy entropy implementation for consistency with paper.

    Args:
        logits: Unnormalized logits. If 2D, entropy is averaged over sequence.

    Returns:
        entropy_val: Scalar entropy value.
    """
    if logits.dim() == 2:
        entropies = []
        for t in range(logits.shape[0]):
            probs = F.softmax(logits[t], dim=-1).cpu().numpy()
            entropies.append(float(scipy_entropy(probs)))
        return float(np.mean(entropies))
    else:
        probs = F.softmax(logits, dim=-1).cpu().numpy()
        return float(scipy_entropy(probs))


def compute_topk_overlap(
    logits_a: torch.FloatTensor,  # (vocab_size,)
    logits_b: torch.FloatTensor,  # (vocab_size,)
    top_p: float = 0.9,
) -> float:
    """
    Compute top-p vocabulary overlap between two distributions.

    Constructs binary indicator vectors for the smallest sets of tokens
    whose cumulative probability mass ≥ top_p, then takes inner product.

    As described in Figure 6b: measures overlap between CFG, vanilla P(y|x),
    and unprompted P(x) distributions at top-p=90%.

    Args:
        logits_a: Logits for distribution A, shape (vocab_size,).
        logits_b: Logits for distribution B, shape (vocab_size,).
        top_p: Probability mass threshold (default 0.9 = 90%).

    Returns:
        overlap: Scalar overlap score (inner product of binary indicators).
    """
    def get_topk_mask(logits: torch.FloatTensor, p: float) -> np.ndarray:
        probs = F.softmax(logits, dim=-1)
        sorted_probs, sorted_idx = torch.sort(probs, descending=True)
        cumsum = torch.cumsum(sorted_probs, dim=0)
        # Find cutoff index
        cutoff = int((cumsum <= p).sum().item()) + 1
        mask = torch.zeros_like(probs)
        mask[sorted_idx[:cutoff]] = 1.0
        return mask.cpu().numpy()

    mask_a = get_topk_mask(logits_a, top_p)
    mask_b = get_topk_mask(logits_b, top_p)

    # Inner product of binary masks = number of tokens in common
    # Normalize by geometric mean to get overlap fraction
    n_a = mask_a.sum()
    n_b = mask_b.sum()
    if n_a == 0 or n_b == 0:
        return 0.0
    return float(np.dot(mask_a, mask_b) / np.sqrt(n_a * n_b))


def compute_perplexity(
    model: PreTrainedModel,
    input_ids: torch.LongTensor,   # shape: (1, seq_len)
    completion_start_idx: int,     # index where completion begins
) -> float:
    """
    Compute perplexity of completion tokens under the model.

    Args:
        model: Language model (base or instruct variant).
        input_ids: Full input token IDs (prompt + completion), shape (1, seq_len).
        completion_start_idx: Index of first completion token in input_ids.

    Returns:
        ppl: Perplexity scalar.
    """
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
        # Compute token-level loss only on completion portion
        logits = outputs.logits[0, completion_start_idx - 1:-1, :]  # (comp_len, vocab)
        targets = input_ids[0, completion_start_idx:]               # (comp_len,)
        loss = F.cross_entropy(logits, targets, reduction='mean')
    return float(torch.exp(loss).item())


def analyze_entropy_across_dataset(
    model_base: PreTrainedModel,
    tokenizer: PreTrainedTokenizer,
    samples: List[str],             # list of P3 text samples
    gamma: float = 1.5,             # CFG guidance strength
    model_instruct: PreTrainedModel = None,  # optional instruct model for comparison
) -> Dict[str, List[float]]:
    """
    Run entropy analysis across a dataset (e.g., P3).

    For each sample, compute:
    - Entropy under vanilla prompted model P(y|x)
    - Entropy under CFG-guided model P̂_γ(y|x)
    - Entropy under unprompted model P(x) [using last prompt token only]
    - Entropy under instruction-tuned model P_instruct(y|x) [if provided]

    Args:
        model_base: Base (unfinetuned) language model.
        tokenizer: Shared tokenizer.
        samples: List of text samples to evaluate.
        gamma: CFG guidance strength.
        model_instruct: Optional instruction-tuned model.

    Returns:
        Dict mapping condition name to list of per-sample mean entropies.
    """
    results = {
        'vanilla': [],
        'cfg': [],
        'unprompted': [],
    }
    if model_instruct is not None:
        results['instruct'] = []

    for sample in samples:
        # Tokenize — split into prompt and completion for analysis
        tokens = tokenizer.encode(sample, return_tensors='pt')
        # For P3, the full sample is both prompt+completion
        # In practice, split at midpoint or use dataset-provided split
        prompt_len = max(1, tokens.shape[1] // 2)

        cond_ids = tokens
        uncond_ids = tokens[:, prompt_len - 1:]  # last prompt token onwards

        with torch.no_grad():
            # Vanilla: full conditional
            logits_vanilla = model_base(cond_ids).logits[0]
            # Unprompted: unconditional approximation
            logits_uncond = model_base(uncond_ids).logits[0]
            # CFG: interpolated
            min_len = min(logits_vanilla.shape[0], logits_uncond.shape[0])
            logits_cfg_seq = (logits_uncond[-min_len:] +
                              gamma * (logits_vanilla[-min_len:] - logits_uncond[-min_len:]))

        results['vanilla'].append(compute_logit_entropy(logits_vanilla))
        results['cfg'].append(compute_logit_entropy(logits_cfg_seq))
        results['unprompted'].append(compute_logit_entropy(logits_uncond))

        if model_instruct is not None:
            with torch.no_grad():
                logits_instruct = model_instruct(cond_ids).logits[0]
            results['instruct'].append(compute_logit_entropy(logits_instruct))

    return results


def compute_perplexity_spearman_correlation(
    ppl_a: List[float],  # perplexities from model A
    ppl_b: List[float],  # perplexities from model B
) -> Tuple[float, float]:
    """
    Compute Spearman correlation between perplexities of two models.

    As reported in Figure 7b, Table 7 of the paper: measures whether models
    agree on which inputs are "hard."

    Args:
        ppl_a: List of perplexity values from model A.
        ppl_b: List of perplexity values from model B.

    Returns:
        rs: Spearman correlation coefficient.
        p_val: p-value for the correlation.
    """
    rs, p_val = spearmanr(ppl_a, ppl_b)
    return float(rs), float(p_val)
