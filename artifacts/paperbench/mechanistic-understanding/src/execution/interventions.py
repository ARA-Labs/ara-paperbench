"""
Residual Stream Subtraction Interventions.

Implements Section 3.3: subtract toxic vectors from the last layer
residual stream during generation to suppress toxic outputs.

x^{L-1} ← x^{L-1} - α * W

where W ∈ {W_Toxic, MLP.v19_770, SVD.U_Toxic[0]}
"""

import torch
from torch import Tensor
from typing import Callable, Optional


def subtract_vector_hook(
    vector: Tensor,
    alpha: float,
) -> Callable:
    """
    Create a forward hook that subtracts α*vector from the residual stream.

    The hook is registered on the last transformer layer (L-1=23 for GPT2-medium).
    During the forward pass:
        x^{L-1} ← x^{L-1} - α * W

    Args:
        vector: [d] toxicity vector to subtract (W_Toxic, MLP.v19, or SVD.U_Toxic[0]).
        alpha: Scale factor; chosen so resulting perplexity ≈ GPT2DPO perplexity.
    Returns:
        Hook function compatible with PyTorch register_forward_hook.
    """
    def hook(module, input: tuple, output: Tensor) -> Tensor:
        # output: [batch, seq_len, d] — residual stream at layer L-1
        v_scaled = alpha * vector.to(output.device)
        return output - v_scaled.unsqueeze(0).unsqueeze(0)
    return hook


def generate_with_intervention(
    model: "GPT2LMHeadModel",
    tokenizer: "GPT2Tokenizer",
    prompt_ids: Tensor,
    toxic_vector: Tensor,
    alpha: float,
    max_new_tokens: int = 20,
    device: torch.device = torch.device("cpu"),
) -> Tensor:
    """
    Generate text while subtracting the toxic vector from the last layer.

    Section 3.3: intervention applied during the forward pass.

    Args:
        model: GPT2-medium (pre-DPO).
        tokenizer: GPT2 tokenizer.
        prompt_ids: [1, seq_len] input token IDs.
        toxic_vector: [d] vector to subtract.
        alpha: Scale factor.
        max_new_tokens: Number of tokens to generate.
        device: Computation device.
    Returns:
        generated_ids: [1, seq_len + max_new_tokens] output token IDs.
    """
    hook_fn = subtract_vector_hook(toxic_vector, alpha)
    # Register hook on the last transformer block (layer 23)
    handle = model.transformer.h[-1].register_forward_hook(hook_fn)
    try:
        with torch.no_grad():
            generated_ids = model.generate(
                prompt_ids.to(device),
                max_new_tokens=max_new_tokens,
            )
    finally:
        handle.remove()
    return generated_ids


def compute_perplexity(
    model: "GPT2LMHeadModel",
    text_loader: "DataLoader",
    toxic_vector: Optional[Tensor],
    alpha: float,
    device: torch.device,
) -> float:
    """
    Compute perplexity on Wikitext-2 with optional intervention.

    Section 3.3: Perplexity measured on Wikitext-2 dataset to ensure
    interventions do not degrade generation quality.

    Args:
        model: GPT2-medium.
        text_loader: DataLoader over Wikitext-2 token IDs.
        toxic_vector: [d] vector to subtract, or None for no intervention.
        alpha: Scale factor.
        device: Computation device.
    Returns:
        perplexity: Scalar perplexity score.
    """
    if toxic_vector is not None:
        hook_fn = subtract_vector_hook(toxic_vector, alpha)
        handle = model.transformer.h[-1].register_forward_hook(hook_fn)
    total_nll = 0.0
    total_tokens = 0
    model.eval()
    with torch.no_grad():
        for batch in text_loader:
            input_ids = batch.to(device)
            outputs = model(input_ids, labels=input_ids)
            nll = outputs.loss * input_ids.numel()
            total_nll += nll.item()
            total_tokens += input_ids.numel()
    if toxic_vector is not None:
        handle.remove()
    return torch.exp(torch.tensor(total_nll / total_tokens)).item()


def compute_f1(
    generated_tokens: list,
    reference_tokens: list,
) -> float:
    """
    Compute token-level F1 between generated and reference continuations.

    Section 3.3: F1 = harmonic mean of precision and recall where:
    - Precision = fraction of generated tokens in reference continuation
    - Recall = fraction of reference tokens in generated output

    Args:
        generated_tokens: List of generated token strings.
        reference_tokens: List of reference continuation token strings.
    Returns:
        f1: Float F1 score.
    """
    gen_set = set(generated_tokens)
    ref_set = set(reference_tokens)
    if not gen_set or not ref_set:
        return 0.0
    precision = len(gen_set & ref_set) / len(gen_set)
    recall = len(gen_set & ref_set) / len(ref_set)
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)
