"""
Un-alignment Attack via Toxic Key Vector Scaling.

Implements Section 5.3: Expand the activation regions γ(k_i^ℓ) of the
top-7 toxic key vectors by scaling them by 10×, causing the DPO-shifted
residual stream to re-enter toxic regions.

Key insight: DPO only learned an offset to bypass toxic regions.
Expanding those regions by scaling key vectors reverses the alignment
without affecting perplexity (unlike residual stream interventions).

Un-alignment procedure:
    k_i^ℓ ← λ * k_i^ℓ  for top-7 (k_i^ℓ, v_i^ℓ) in MLP.kToxic
    λ = 10
"""

import torch
import torch.nn.functional as F
from torch import Tensor
from typing import List, Tuple


def unalign_by_key_scaling(
    model: "GPT2LMHeadModel",
    selected_ids: List[Tuple[int, int]],
    scale_factor: float = 10.0,
    top_k: int = 7,
    w_toxic: Tensor = None,
) -> "GPT2LMHeadModel":
    """
    Un-align GPT2DPO by scaling top-k toxic key vectors.

    Section 5.3: "A simple way to re-activate toxicity is to increase
    those regions by scaling each key vector larger."

    Scaling k_i^ℓ by λ=10 expands γ(k_i^ℓ) = {g | σ(k_i^ℓ · g) > 0},
    making it easier for the DPO-shifted residual stream to satisfy
    σ(k_i^ℓ · x) > 0, thereby re-activating the toxic value vectors.

    Note: This is a white-box attack requiring access to model weights.
    Perplexity is unaffected because key vector scaling does not directly
    modify the residual stream (unlike subtraction interventions).

    Args:
        model: GPT2DPO model to un-align (modified in-place).
        selected_ids: [(layer_idx, neuron_idx)] for MLP.kToxic (pre-ranked
                      by cosine similarity to W_Toxic, use top_k of these).
        scale_factor: Multiplicative scale for key vectors (default 10.0).
        top_k: Number of key vectors to scale (default 7).
        w_toxic: [d] W_Toxic vector for re-ranking if needed.
    Returns:
        model: Modified GPT2DPO with scaled key vectors.
    """
    # If w_toxic provided, re-rank selected_ids by cosine similarity
    if w_toxic is not None and len(selected_ids) > top_k:
        key_vecs = []
        for layer_idx, neuron_idx in selected_ids:
            kv = model.transformer.h[layer_idx].mlp.c_fc.weight[neuron_idx]
            key_vecs.append(kv.detach())
        key_mat = torch.stack(key_vecs)  # [n_selected, d]
        cos_sims = F.cosine_similarity(
            key_mat, w_toxic.unsqueeze(0).expand_as(key_mat), dim=1
        )
        top_indices = cos_sims.topk(top_k).indices.tolist()
        selected_ids = [selected_ids[i] for i in top_indices]
    else:
        selected_ids = selected_ids[:top_k]

    # Scale key vectors in-place
    with torch.no_grad():
        for layer_idx, neuron_idx in selected_ids:
            # c_fc.weight[neuron_idx] is the key vector k_i^ℓ ∈ R^d
            model.transformer.h[layer_idx].mlp.c_fc.weight[neuron_idx] *= scale_factor

    return model


def compute_residual_shift(
    model_base: "GPT2LMHeadModel",
    model_dpo: "GPT2LMHeadModel",
    input_ids: Tensor,
    layer_idx: int,
    device: torch.device,
) -> Tensor:
    """
    Compute the residual stream shift δ^{ℓmid} = x_{DPO}^{ℓmid} - x_{GPT2}^{ℓmid}.

    Section 5.2: Used to characterize how DPO shifts the residual stream
    out of toxic activation regions.

    Args:
        model_base: Original GPT2-medium.
        model_dpo: DPO fine-tuned GPT2DPO.
        input_ids: [batch, seq_len] prompt token IDs.
        layer_idx: Layer ℓ at which to compute residual stream (ℓmid = after attn).
        device: Computation device.
    Returns:
        delta: [batch, seq_len, d] residual stream difference at layer ℓmid.
    """
    residuals_base = {}
    residuals_dpo = {}

    def make_capture_hook(storage: dict, key: str):
        def hook(module, input, output):
            # Capture hidden state after attention (before MLP): input[0]
            storage[key] = input[0].detach()
        return hook

    # Register hooks at the MLP input (= residual after attention = ℓmid)
    h_base = model_base.transformer.h[layer_idx].mlp.register_forward_hook(
        make_capture_hook(residuals_base, "stream")
    )
    h_dpo = model_dpo.transformer.h[layer_idx].mlp.register_forward_hook(
        make_capture_hook(residuals_dpo, "stream")
    )

    with torch.no_grad():
        model_base(input_ids.to(device))
        model_dpo(input_ids.to(device))

    h_base.remove()
    h_dpo.remove()

    delta = residuals_dpo["stream"] - residuals_base["stream"]
    return delta
