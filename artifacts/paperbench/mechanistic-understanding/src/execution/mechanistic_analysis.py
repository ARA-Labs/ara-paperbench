"""
Mechanistic Analysis: Residual Stream Shift, Activation Measurement, Un-alignment
Implements analysis tools for understanding how DPO changes GPT2's residual stream.
Based on: Lee et al. (2024) "A Mechanistic Understanding of Alignment Algorithms"
Source: toxicity/figures/pca.sync.py, toxicity/figures/activation_drop.sync.py
        toxicity/figures/resid_diff_plot.sync.py
"""

import torch
import torch.nn.functional as F
from typing import List, Tuple, Dict
import numpy as np


def measure_toxic_vector_activations(
    model,                          # HookedTransformer (TransformerLens)
    prompts_tokenized: torch.Tensor, # [n_prompts, seq_len]
    toxic_indices: List[Tuple[int, int]],  # List of (layer, neuron_idx)
    n_generate: int = 20,
) -> Dict[Tuple[int, int], float]:
    """
    Measure mean activation m_i = σ(x^l · k^l_i) for each toxic value vector.
    
    For each prompt, generate n_generate tokens; at each step, record the
    activation σ(x^l · k^l_i) for each toxic key vector. Return the mean.
    
    In HookedTransformer:
        - Residual stream at layer l mid: cache["blocks.{l}.hook_resid_mid"]
        - Key weight: model.blocks[l].mlp.W_in[:, i]  (shape [d_model])
        - Activation: model.blocks[l].mlp.act_fn(x @ W_in[:, i])
    
    Args:
        model: GPT2 or GPT2-DPO as HookedTransformer
        prompts_tokenized: Tokenized prompts, shape [n_prompts, prompt_len]
        toxic_indices: List of (layer, neuron_idx) for each toxic vector
        n_generate: Number of tokens to generate per prompt (default: 20)
    
    Returns:
        Dict mapping (layer, idx) → mean activation (averaged over n_prompts * n_generate)
    """
    activations = {idx: [] for idx in toxic_indices}
    
    for prompt_idx in range(prompts_tokenized.shape[0]):
        prompt = prompts_tokenized[prompt_idx:prompt_idx+1]  # [1, prompt_len]
        
        for step in range(n_generate):
            with torch.inference_mode():
                _, cache = model.run_with_cache(prompt)
            
            for (layer, neuron_idx) in toxic_indices:
                # Residual stream at mid-layer l (after attention, before MLP)
                resid_mid = cache[f"blocks.{layer}.hook_resid_mid"][:, -1, :]  # [1, d_model]
                # Key vector for this neuron: W_in column
                key_vec = model.blocks[layer].mlp.W_in[:, neuron_idx]  # [d_model]
                # Compute pre-activation dot product
                dot = (resid_mid @ key_vec).squeeze()
                activation = model.blocks[layer].mlp.act_fn(dot).item()
                activations[(layer, neuron_idx)].append(activation)
            
            # Generate next token greedily
            with torch.inference_mode():
                next_logits = model(prompt).logits[:, -1, :]
            next_token = next_logits.argmax(dim=-1, keepdim=True)
            prompt = torch.cat([prompt, next_token], dim=-1)
    
    return {k: float(np.mean(v)) for k, v in activations.items()}


def compute_residual_stream_shift(
    gpt2_model,         # HookedTransformer (base GPT2)
    dpo_model,          # HookedTransformer (GPT2-DPO)
    prompts: torch.Tensor,  # [n_prompts, seq_len]
    target_layer: int = 19,
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    Compute the mean residual stream shift δx = x_DPO - x_GPT2 at target_layer mid.
    
    Uses TransformerLens cache key: f"blocks.{target_layer}.hook_resid_mid"
    
    Args:
        gpt2_model: Base GPT2 as HookedTransformer
        dpo_model: GPT2-DPO as HookedTransformer
        prompts: Tokenized prompts, shape [n_prompts, seq_len]
        target_layer: Layer index for which to compute the shift
    
    Returns:
        gpt2_resid: Residual streams from GPT2, shape [n_prompts, d_model]
        dpo_resid: Residual streams from DPO, shape [n_prompts, d_model]
        delta_x_mean: Mean shift vector δ_x = mean(dpo - gpt2), shape [d_model]
    """
    gpt2_resids = []
    dpo_resids = []
    
    for i in range(0, prompts.shape[0], 4):  # batch_size=4
        batch = prompts[i:i+4]
        with torch.inference_mode():
            _, cache_gpt2 = gpt2_model.run_with_cache(batch)
            resid_gpt2 = cache_gpt2[f"blocks.{target_layer}.hook_resid_mid"][:, -1, :]
        with torch.inference_mode():
            _, cache_dpo = dpo_model.run_with_cache(batch)
            resid_dpo = cache_dpo[f"blocks.{target_layer}.hook_resid_mid"][:, -1, :]
        
        gpt2_resids.append(resid_gpt2.cpu())
        dpo_resids.append(resid_dpo.cpu())
    
    gpt2_stacked = torch.cat(gpt2_resids, dim=0)  # [n_prompts, d_model]
    dpo_stacked = torch.cat(dpo_resids, dim=0)    # [n_prompts, d_model]
    delta_x_mean = (dpo_stacked - gpt2_stacked).mean(dim=0)  # [d_model]
    
    return gpt2_stacked, dpo_stacked, delta_x_mean


def compute_cosine_sim_mlp_vs_delta_x(
    gpt2_model,            # HookedTransformer base GPT2
    dpo_model,             # HookedTransformer GPT2-DPO
    delta_x: torch.Tensor, # shape [d_model]: mean residual shift at target layer
    target_layer: int = 19,
) -> Dict[int, List[float]]:
    """
    Compute cosine similarity between δMLP.v_i (DPO-GPT2 value weight diff) and δx.
    
    For each layer j < target_layer, for each neuron i:
        δMLP.v_i^j = W_V_DPO[j,i] - W_V_GPT2[j,i]
        cos_sim = cosine_similarity(δx, δMLP.v_i^j)
    
    Expected finding: cos_sim distributions shift from ~0 (early layers) to
    predominantly negative (layers approaching target_layer), because GeLU
    sparsity causes antipodal δMLP.v to contribute in the δx direction.
    
    Args:
        gpt2_model: Base GPT2 as HookedTransformer
        dpo_model: GPT2-DPO as HookedTransformer
        delta_x: Mean residual stream shift vector, shape [d_model]
        target_layer: Layer of the target toxic vector
    
    Returns:
        Dict mapping layer_idx → list of cosine similarities (one per neuron)
    """
    cos_sims_by_layer = {}
    delta_x_normalized = delta_x / delta_x.norm()
    
    for layer in range(target_layer):
        # Value vectors: c_proj.weight rows, shape [d_mlp, d_model]
        w_v_gpt2 = gpt2_model.transformer.h[layer].mlp.c_proj.weight  # [d_mlp, d_model]
        w_v_dpo = dpo_model.transformer.h[layer].mlp.c_proj.weight
        delta_mlp_v = (w_v_dpo - w_v_gpt2).float()  # [d_mlp, d_model]
        
        # Cosine similarity of each neuron's δv with δx
        cos_sims = F.cosine_similarity(delta_mlp_v, delta_x_normalized.unsqueeze(0), dim=1)
        cos_sims_by_layer[layer] = cos_sims.cpu().tolist()
    
    return cos_sims_by_layer


def project_residual_streams_pca(
    gpt2_resid: torch.Tensor,   # [n_prompts, d_model]
    dpo_resid: torch.Tensor,    # [n_prompts, d_model]
    delta_x_mean: torch.Tensor, # [d_model]
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Project residual streams onto 2D: (δx direction, first PC).
    
    Implements the projection used in Figure 4 of the paper.
    First axis = mean DPO offset direction (shift component).
    Second axis = first principal component of all residual streams (variance direction).
    
    Args:
        gpt2_resid: GPT2 residual streams, shape [n_prompts, d_model]
        dpo_resid: DPO residual streams, shape [n_prompts, d_model]
        delta_x_mean: Mean shift vector, shape [d_model]
    
    Returns:
        projected: 2D projections of all samples, shape [2*n_prompts, 2]
        (first n_prompts rows = GPT2, last n_prompts rows = DPO)
    """
    all_data = torch.cat([gpt2_resid, dpo_resid], dim=0)  # [2*n_prompts, d_model]
    mean = all_data.mean(dim=0)
    stddev = all_data.std(dim=0)
    normalized = (all_data - mean) / (stddev + 1e-8)  # z-normalize
    
    # PCA for second component
    _, _, V = torch.pca_lowrank(normalized)  # V: [d_model, k]
    
    # Projection matrix: [d_model, 2] = [δx_mean | first_PC]
    comps = torch.cat([delta_x_mean.unsqueeze(-1), V[:, :1]], dim=1)  # [d_model, 2]
    projected = normalized @ comps  # [2*n_prompts, 2]
    
    return projected


def check_parameter_similarity(
    gpt2_model: torch.nn.Module,
    dpo_model: torch.nn.Module,
) -> Dict[str, Tuple[float, float]]:
    """
    Check cosine similarity and norm difference between all matching parameters.
    
    Paper finding: All parameters have cosine similarity > 0.99 and
    average norm difference < 1e-5 (unembedding layer: < 1e-3).
    
    Returns:
        Dict mapping parameter_name → (cosine_similarity, norm_difference)
    """
    results = {}
    for (name1, p1), (name2, p2) in zip(
        gpt2_model.named_parameters(), dpo_model.named_parameters()
    ):
        assert name1 == name2, f"Parameter name mismatch: {name1} vs {name2}"
        p1_flat = p1.detach().float().view(-1)
        p2_flat = p2.detach().float().view(-1)
        cos_sim = F.cosine_similarity(p1_flat.unsqueeze(0), p2_flat.unsqueeze(0)).item()
        norm_diff = (p1_flat - p2_flat).norm().item() / p1_flat.numel()  # avg norm diff
        results[name1] = (cos_sim, norm_diff)
    return results
