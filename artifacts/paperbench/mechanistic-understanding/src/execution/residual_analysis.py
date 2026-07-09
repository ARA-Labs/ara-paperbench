"""
Residual stream shift analysis and un-alignment via key vector scaling.

Implements:
- Logit lens visualization (per-layer token probability)
- Mean activation measurement for MLP.vToxic
- Residual stream difference δx computation
- Cosine similarity between δMLP.v and δx
- Un-alignment: scale toxic key vectors by λ=10

Reference: §5 of Lee et al. (2024) "A Mechanistic Understanding of Alignment Algorithms"
"""

import torch
import torch.nn as nn
import numpy as np
from typing import List, Tuple, Dict


def logit_lens(
    model: nn.Module,
    input_ids: torch.Tensor,   # shape: (1, seq_len)
    target_token_id: int,      # e.g., token ID for " shit"
    num_layers: int = 24,
) -> np.ndarray:
    """
    Apply logit lens: compute P(target_token | x^l) at each intermediate layer.

    At each layer l (both after attention = x^l_mid, and after MLP = x^{l+1}),
    apply the unembedding matrix U and softmax to get token probabilities.

    Args:
        model: GPT2-medium (or GPT2DPO)
        input_ids: Tokenized prompt, shape (1, seq_len)
        target_token_id: Token ID whose probability to track (e.g., "sh*t")
        num_layers: Number of transformer layers (24)

    Returns:
        probs_per_layer: Array of shape (2*num_layers,) — one entry per
                         x^l_mid (after attention) and x^l (after MLP) per layer
    """
    intermediate_hidden_states = []

    def make_hook(stage: str, l: int):
        def hook_fn(module, input, output):
            hidden = output[0] if isinstance(output, tuple) else output
            intermediate_hidden_states.append((stage, l, hidden[:, -1, :].detach()))
        return hook_fn

    handles = []
    for l in range(num_layers):
        # After attention (x^l_mid)
        h = model.transformer.h[l].attn.register_forward_hook(make_hook('mid', l))
        handles.append(h)
        # After MLP (x^{l+1})
        h = model.transformer.h[l].mlp.register_forward_hook(make_hook('mlp', l))
        handles.append(h)

    model.eval()
    with torch.no_grad():
        model(input_ids)

    for h in handles:
        h.remove()

    # Apply unembedding (logit lens) at each intermediate state
    U = model.lm_head.weight  # shape: (vocab_size, d)
    probs = []
    for stage, l, hidden in sorted(intermediate_hidden_states, key=lambda x: (x[1], x[0])):
        logits = hidden @ U.T  # (1, vocab_size)
        prob = torch.softmax(logits, dim=-1)[0, target_token_id].item()
        probs.append(prob)

    return np.array(probs)


def measure_mlp_mean_activations(
    model: nn.Module,
    input_ids_list: List[torch.Tensor],  # 1,199 prompts
    toxic_vector_indices: List[Tuple[int, int]],  # [(layer, idx), ...]
    num_generate: int = 20,
) -> Dict[Tuple[int, int], float]:
    """
    Measure mean activation m^l_i = σ(x^l · k^l_i) for each toxic key vector.

    Args:
        model: GPT2-medium or GPT2DPO
        input_ids_list: List of 1,199 tokenized prompts
        toxic_vector_indices: List of (layer, idx) for each toxic key vector
        num_generate: Tokens to generate per prompt (20)

    Returns:
        mean_activations: Dict mapping (layer, idx) to mean activation
    """
    activations = {key: [] for key in toxic_vector_indices}
    model.eval()

    for input_ids in input_ids_list:
        with torch.no_grad():
            output = model.generate(input_ids.unsqueeze(0), max_new_tokens=num_generate,
                                    do_sample=False, output_hidden_states=True,
                                    return_dict_in_generate=True)
        # Extract per-step hidden states
        for step_hidden_states in output.hidden_states:
            for (layer, idx) in toxic_vector_indices:
                x = step_hidden_states[layer][:, -1, :]  # (1, d)
                key_vec = model.transformer.h[layer].mlp.c_fc.weight[idx]  # (d,)
                activation = torch.nn.functional.gelu(torch.dot(x.squeeze(), key_vec)).item()
                activations[(layer, idx)].append(activation)

    return {k: float(np.mean(v)) for k, v in activations.items()}


def compute_residual_stream_shift(
    model_gpt2: nn.Module,
    model_dpo: nn.Module,
    input_ids_list: List[torch.Tensor],  # 1,199 prompts
    layer_idx: int = 19,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute δ^l_mid = x^l_mid_DPO - x^l_mid_GPT2 (before MLP at layer l).

    Args:
        model_gpt2: Original GPT2-medium
        model_dpo: Fine-tuned GPT2DPO
        input_ids_list: List of tokenized prompts
        layer_idx: Target layer for analysis (19 for primary analysis)

    Returns:
        delta_x_mean: Mean residual stream shift, shape (d=1024,)
        all_delta_x: All per-prompt shifts, shape (N_prompts, d)
    """
    gpt2_hidden, dpo_hidden = [], []

    def make_hook(store: list):
        def hook(module, input, output):
            hidden = output[0] if isinstance(output, tuple) else output
            store.append(hidden[:, -1, :].detach().cpu().numpy())
        return hook

    for input_ids in input_ids_list:
        g_store, d_store = [], []
        h1 = model_gpt2.transformer.h[layer_idx].attn.register_forward_hook(make_hook(g_store))
        h2 = model_dpo.transformer.h[layer_idx].attn.register_forward_hook(make_hook(d_store))

        with torch.no_grad():
            model_gpt2(input_ids.unsqueeze(0))
            model_dpo(input_ids.unsqueeze(0))

        h1.remove(); h2.remove()
        gpt2_hidden.append(g_store[0])
        dpo_hidden.append(d_store[0])

    gpt2_hidden = np.stack(gpt2_hidden)  # (N, d)
    dpo_hidden = np.stack(dpo_hidden)    # (N, d)
    all_delta_x = dpo_hidden - gpt2_hidden  # (N, d)
    delta_x_mean = all_delta_x.mean(axis=0)  # (d,)

    return delta_x_mean, all_delta_x


def compute_cosine_similarity_delta_mlp_v(
    model_gpt2: nn.Module,
    model_dpo: nn.Module,
    delta_x_mean: np.ndarray,   # shape: (d=1024,) — mean δx at layer l_toxic
    target_layer: int = 19,
    num_layers: int = 24,
) -> Dict[int, np.ndarray]:
    """
    For each preceding layer j < target_layer, compute cosine similarity between
    δ^l_mid and δ^j_{MLP.v_i} for all value vectors i.

    δ^j_{MLP.v_i} = MLP.v^j_{i,DPO} - MLP.v^j_{i,GPT2}

    Args:
        model_gpt2: Original GPT2-medium
        model_dpo: Fine-tuned GPT2DPO
        delta_x_mean: Mean residual stream shift at target_layer's mid position
        target_layer: Layer of primary toxic vector analysis (19)
        num_layers: Total layers (24)

    Returns:
        cos_sims_by_layer: Dict mapping layer_j to array of cosine similarities, shape (dmlp=4096,)
    """
    delta_x_norm = delta_x_mean / (np.linalg.norm(delta_x_mean) + 1e-8)
    cos_sims_by_layer = {}

    for j in range(target_layer):
        # Get value vectors (columns of W_V = c_proj.weight.T)
        v_gpt2 = model_gpt2.transformer.h[j].mlp.c_proj.weight.detach().T.cpu().numpy()  # (dmlp, d)
        v_dpo = model_dpo.transformer.h[j].mlp.c_proj.weight.detach().T.cpu().numpy()    # (dmlp, d)
        delta_v = v_dpo - v_gpt2  # (dmlp, d)

        # Cosine similarity of each δv_i with δx
        delta_v_norms = np.linalg.norm(delta_v, axis=1, keepdims=True) + 1e-8
        delta_v_normalized = delta_v / delta_v_norms
        cos_sims = delta_v_normalized @ delta_x_norm  # (dmlp,)
        cos_sims_by_layer[j] = cos_sims

    return cos_sims_by_layer


def unalign_by_scaling_key_vectors(
    model_dpo: nn.Module,
    w_toxic: np.ndarray,     # shape: (d=1024,)
    K: int = 7,
    scale_factor: float = 10.0,
    num_layers: int = 24,
) -> nn.Module:
    """
    Un-align GPT2DPO by scaling the top-K toxic key vectors by scale_factor.

    This expands γ(MLP.k^l_i) so the DPO-learned residual stream offset
    no longer avoids the toxic activation regions, re-activating toxic outputs.

    Args:
        model_dpo: Aligned GPT2DPO model
        w_toxic: Toxicity probe vector, shape (d,)
        K: Number of key vectors to scale (7)
        scale_factor: Multiplicative scale factor (10.0)
        num_layers: Total number of transformer layers (24)

    Returns:
        model_dpo: Modified (un-aligned) model with scaled key vectors
    """
    w_toxic_t = torch.FloatTensor(w_toxic)
    w_norm = w_toxic_t / w_toxic_t.norm()

    # Find top-K key vectors by cosine similarity to w_toxic
    all_similarities = []
    for l in range(num_layers):
        key_vectors = model_dpo.transformer.h[l].mlp.c_fc.weight  # (dmlp, d)
        for i in range(key_vectors.shape[0]):
            k = key_vectors[i].detach()
            cos_sim = torch.dot(k / k.norm(), w_norm).item()
            all_similarities.append((cos_sim, l, i))

    all_similarities.sort(key=lambda x: x[0], reverse=True)
    top_K = all_similarities[:K]

    # Scale top-K key vectors in-place
    with torch.no_grad():
        for cos_sim, l, i in top_K:
            model_dpo.transformer.h[l].mlp.c_fc.weight[i] *= scale_factor

    return model_dpo


def compute_parameter_similarity(
    model_gpt2: nn.Module,
    model_dpo: nn.Module,
) -> Dict[str, Dict[str, float]]:
    """
    Compare every parameter between GPT2 and GPT2DPO.

    Verifies C03: cosine_sim > 0.99, avg_norm_diff < 1e-5 (unembedding: < 1e-3)

    Returns:
        stats: Dict mapping param_name to {'cosine_sim': float, 'norm_diff': float}
    """
    stats = {}
    gpt2_params = dict(model_gpt2.named_parameters())
    dpo_params = dict(model_dpo.named_parameters())

    for name, p_gpt2 in gpt2_params.items():
        if name not in dpo_params:
            continue
        p_dpo = dpo_params[name]
        v1 = p_gpt2.detach().float().flatten()
        v2 = p_dpo.detach().float().flatten()

        cos_sim = torch.dot(v1 / v1.norm(), v2 / v2.norm()).item()
        norm_diff = (v1 - v2).norm().item() / v1.numel()  # average norm difference

        stats[name] = {'cosine_sim': cos_sim, 'norm_diff': norm_diff}

    return stats
