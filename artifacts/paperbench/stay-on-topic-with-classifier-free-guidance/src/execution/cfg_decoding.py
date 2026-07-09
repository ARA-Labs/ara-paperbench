"""
Classifier-Free Guidance (CFG) decoding for autoregressive language models.

Implements Equation 7 from "Stay on topic with Classifier-Free Guidance"
(Sanchez et al., 2023, arXiv:2306.17806).

Core formula:
    log P_hat(w_i | w_{j<i}, c) = log P(w_i | w_{j<i})
                                 + gamma * (log P(w_i | w_{j<i}, c) - log P(w_i | w_{j<i}))

This is architecture-agnostic and requires no model fine-tuning.
"""

import torch
import torch.nn.functional as F
from typing import List, Optional, Tuple
from transformers import PreTrainedModel, PreTrainedTokenizer


def get_unconditional_prefix(
    prompt_token_ids: List[int],
    negative_prompt_token_ids: Optional[List[int]] = None,
) -> List[int]:
    """
    Construct the unconditional prefix for CFG.

    Per Section 3.1: "we implement CFG by starting the unconditional prompt
    at the last token of the initial prompt."

    For negative prompting (Section 3.4), the negative prompt replaces
    the last-token unconditional prefix.

    Args:
        prompt_token_ids: Full tokenized prompt [seq_len]
        negative_prompt_token_ids: Optional negative prompt tokens.
            If None, use the last token of prompt_token_ids.

    Returns:
        List of token ids for the unconditional prefix.
    """
    if negative_prompt_token_ids is not None:
        return list(negative_prompt_token_ids)
    else:
        # Use last token of the prompt as the unconditional starting point
        return [prompt_token_ids[-1]]


def cfg_logits(
    logits_cond: torch.Tensor,
    logits_uncond: torch.Tensor,
    gamma: float,
) -> torch.Tensor:
    """
    Combine conditional and unconditional logits using CFG formula (Eq. 7).

    Args:
        logits_cond: Conditional log-probs or logits [vocab_size].
            From forward pass with full prompt c.
        logits_uncond: Unconditional log-probs or logits [vocab_size].
            From forward pass with unconditional prefix (last prompt token or neg prompt).
        gamma: Guidance strength scalar.
            gamma=1.0 → standard conditional generation (no guidance effect).
            gamma>1.0 → amplifies conditioning; gamma=0.0 → unconditional generation.

    Returns:
        cfg_logits: [vocab_size] tensor of CFG-adjusted logits.
            log P_hat(w|c) = logits_uncond + gamma * (logits_cond - logits_uncond)
    """
    return logits_uncond + gamma * (logits_cond - logits_uncond)


@torch.no_grad()
def cfg_generate(
    model: PreTrainedModel,
    tokenizer: PreTrainedTokenizer,
    prompt_token_ids: List[int],
    gamma: float = 1.5,
    max_new_tokens: int = 128,
    temperature: float = 1.0,
    top_p: float = 1.0,
    negative_prompt_token_ids: Optional[List[int]] = None,
    eos_token_id: Optional[int] = None,
) -> List[int]:
    """
    Generate tokens from an autoregressive LM using CFG decoding.

    Performs two forward passes per token:
    1. Conditional: full prompt + generated tokens so far
    2. Unconditional: last prompt token (or negative prompt) + generated tokens

    Args:
        model: HuggingFace PreTrainedModel (GPT-2, Pythia, LLaMA, CodeGen, etc.)
        tokenizer: Corresponding tokenizer
        prompt_token_ids: Tokenized prompt [seq_len]; shape (seq_len,)
        gamma: CFG guidance strength (>1.0 increases prompt adherence)
        max_new_tokens: Maximum number of tokens to generate
        temperature: Sampling temperature (applied to CFG logits)
        top_p: Nucleus sampling threshold
        negative_prompt_token_ids: If provided, use as reference instead of last-token unconditional
        eos_token_id: Stop generation at this token; defaults to tokenizer.eos_token_id

    Returns:
        List of generated token ids (not including prompt)
    """
    if eos_token_id is None:
        eos_token_id = tokenizer.eos_token_id

    uncond_prefix = get_unconditional_prefix(prompt_token_ids, negative_prompt_token_ids)

    device = next(model.parameters()).device
    generated: List[int] = []

    for _ in range(max_new_tokens):
        # --- Conditional forward pass: full prompt + generated so far ---
        cond_ids = torch.tensor(
            [prompt_token_ids + generated], dtype=torch.long, device=device
        )  # shape: [1, seq_len + num_generated]
        cond_out = model(input_ids=cond_ids)
        logits_cond = cond_out.logits[0, -1, :]  # [vocab_size]

        # --- Unconditional forward pass: uncond_prefix + generated so far ---
        uncond_ids = torch.tensor(
            [uncond_prefix + generated], dtype=torch.long, device=device
        )  # shape: [1, uncond_len + num_generated]
        uncond_out = model(input_ids=uncond_ids)
        logits_uncond = uncond_out.logits[0, -1, :]  # [vocab_size]

        # --- CFG combination (Equation 7) ---
        logits_guided = cfg_logits(logits_cond, logits_uncond, gamma)

        # --- Apply temperature ---
        if temperature != 1.0:
            logits_guided = logits_guided / temperature

        # --- Sample next token (nucleus sampling) ---
        probs = F.softmax(logits_guided, dim=-1)
        if top_p < 1.0:
            probs = nucleus_filter(probs, top_p)
        next_token_id = torch.multinomial(probs, num_samples=1).item()

        generated.append(next_token_id)
        if next_token_id == eos_token_id:
            break

    return generated


def nucleus_filter(probs: torch.Tensor, top_p: float) -> torch.Tensor:
    """
    Apply nucleus (top-p) filtering to probability distribution.

    Args:
        probs: Probability distribution [vocab_size]
        top_p: Cumulative probability threshold

    Returns:
        Filtered probability distribution [vocab_size] (renormalized)
    """
    sorted_probs, sorted_indices = torch.sort(probs, descending=True)
    cumulative_probs = torch.cumsum(sorted_probs, dim=-1)

    # Remove tokens that exceed top_p cumulative probability
    sorted_indices_to_remove = cumulative_probs - sorted_probs > top_p
    sorted_probs[sorted_indices_to_remove] = 0.0

    # Scatter back and renormalize
    filtered = torch.zeros_like(probs)
    filtered.scatter_(0, sorted_indices, sorted_probs)
    filtered = filtered / filtered.sum()
    return filtered


def compute_token_importance(
    logits_cond: torch.Tensor,
    logits_uncond: torch.Tensor,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Compute per-token importance scores for CFG visualization (Section 5.3).

    Implements: Delta(w) = log P(w_t|w_{<t}, c) - log P(w_T|w_hat)
    Ranking vocabulary by this score shows which tokens CFG encourages (top)
    or discourages (bottom) at each step.

    Args:
        logits_cond: Conditional logits [vocab_size]
        logits_uncond: Unconditional logits [vocab_size]

    Returns:
        importance_scores: [vocab_size] delta scores
        sorted_indices: [vocab_size] token ids sorted by importance (descending)
    """
    log_p_cond = F.log_softmax(logits_cond, dim=-1)
    log_p_uncond = F.log_softmax(logits_uncond, dim=-1)

    importance_scores = log_p_cond - log_p_uncond  # [vocab_size]
    sorted_indices = torch.argsort(importance_scores, descending=True)

    return importance_scores, sorted_indices


def compute_logit_entropy(logits: torch.Tensor) -> float:
    """
    Compute Shannon entropy of the logit distribution (Section 5.1).

    H(p) = -sum_k p_k * log(p_k)

    Args:
        logits: Raw logits [vocab_size]

    Returns:
        entropy: Scalar entropy value (nats)
    """
    probs = F.softmax(logits, dim=-1)
    log_probs = F.log_softmax(logits, dim=-1)
    entropy = -(probs * log_probs).sum().item()
    return entropy
