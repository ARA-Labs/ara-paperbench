"""
Toxic Vector Extraction and SVD Decomposition.

Implements Section 3.1:
- Find N=128 MLP value vectors with highest cosine similarity to W_Toxic
- Stack and apply SVD to obtain SVD.U_Toxic basis vectors
- Project vectors onto vocabulary space for interpretability
"""

import torch
import torch.nn.functional as F
from torch import Tensor
from typing import List, Tuple, Dict


def extract_mlp_value_vectors(
    model: "GPT2LMHeadModel",
    layer_indices: List[int],
) -> Tuple[Tensor, List[Tuple[int, int]]]:
    """
    Extract all MLP value vectors (W_V columns) from specified layers.

    Per Section 2 / Geva et al. (2022):
        MLP^ℓ(x) = σ(W_K^ℓ x) @ W_V^ℓ
    Each column of W_V^ℓ is a value vector v_i^ℓ ∈ R^d.

    Args:
        model: GPT2LMHeadModel with accessible transformer.h layers.
        layer_indices: Which layers to extract from (0 to L-1=23).
    Returns:
        all_value_vectors: Tensor of shape [total_vectors, d] where
                           total_vectors = len(layer_indices) * d_mlp (=4096).
        vector_ids: List of (layer_idx, neuron_idx) for each row.
    """
    all_vecs = []
    vector_ids = []
    for layer_idx in layer_indices:
        # GPT2 MLP: c_fc (W_K) and c_proj (W_V)
        # W_V columns correspond to c_proj.weight.T rows → shape [d_mlp, d]
        mlp_layer = model.transformer.h[layer_idx].mlp
        # c_proj.weight shape: [d, d_mlp]; columns = value vectors
        W_V = mlp_layer.c_proj.weight.T  # [d_mlp, d]
        for i in range(W_V.shape[0]):
            all_vecs.append(W_V[i])
            vector_ids.append((layer_idx, i))
    all_value_vectors = torch.stack(all_vecs)  # [total_vectors, d]
    return all_value_vectors, vector_ids


def extract_toxic_vectors(
    all_value_vectors: Tensor,
    vector_ids: List[Tuple[int, int]],
    w_toxic: Tensor,
    n: int = 128,
) -> Tuple[Tensor, Tensor, List[Tuple[int, int]]]:
    """
    Select top-N MLP value vectors by cosine similarity with W_Toxic.

    Section 3.1: "we search for value vectors that promote toxicity,
    by checking for all value vectors with the highest cosine similarity
    with W_Toxic."

    Args:
        all_value_vectors: [total_vectors, d] all MLP value vectors.
        vector_ids: [(layer_idx, neuron_idx), ...] for each vector.
        w_toxic: [d] toxicity probe direction.
        n: Number of top vectors to select (default 128).
    Returns:
        mlp_v_toxic: [n, d] top-n toxic value vectors.
        cos_sims: [n] cosine similarities of selected vectors.
        selected_ids: [(layer_idx, neuron_idx), ...] for selected vectors.
    """
    cos_sims = F.cosine_similarity(
        all_value_vectors,
        w_toxic.unsqueeze(0).expand_as(all_value_vectors),
        dim=1,
    )  # [total_vectors]
    top_n_indices = cos_sims.topk(n).indices  # [n]
    mlp_v_toxic = all_value_vectors[top_n_indices]  # [n, d]
    selected_ids = [vector_ids[i.item()] for i in top_n_indices]
    return mlp_v_toxic, cos_sims[top_n_indices], selected_ids


def extract_key_vectors(
    model: "GPT2LMHeadModel",
    selected_ids: List[Tuple[int, int]],
) -> Tensor:
    """
    Extract key vectors corresponding to selected toxic value vectors.

    Key vectors are rows of W_K^ℓ (c_fc.weight).

    Args:
        model: GPT2LMHeadModel.
        selected_ids: [(layer_idx, neuron_idx), ...] for toxic vectors.
    Returns:
        mlp_k_toxic: [n, d] key vectors for each toxic value vector.
    """
    key_vecs = []
    for layer_idx, neuron_idx in selected_ids:
        mlp_layer = model.transformer.h[layer_idx].mlp
        # c_fc.weight shape: [d_mlp, d]; rows = key vectors
        k_i = mlp_layer.c_fc.weight[neuron_idx]  # [d]
        key_vecs.append(k_i)
    return torch.stack(key_vecs)  # [n, d]


def svd_decompose_toxic_vectors(
    mlp_v_toxic: Tensor,
) -> Tuple[Tensor, Tensor, Tensor]:
    """
    Apply SVD to MLP.vToxic matrix to get basis vectors.

    Section 3.1: "we stack them into a N×d matrix. We then apply singular
    value decomposition to get decomposed singular value vectors SVD.U_Toxic."

    Args:
        mlp_v_toxic: [N, d] matrix of toxic value vectors (N=128, d=1024).
    Returns:
        U: [N, N] left singular vectors; SVD.U_Toxic[i] = U[:, i] ∈ R^N
           but projected back to d-space via mlp_v_toxic.T @ U
        S: [min(N,d)] singular values.
        Vh: [min(N,d), d] right singular vectors.
    Note:
        SVD.U_Toxic[i] as used in the paper refers to the i-th left singular
        vector, which in standard torch.linalg.svd is U[:, i] of shape [N].
        To get d-dimensional vectors for vocabulary projection, use Vh[i] (rows
        of Vh), which are the right singular vectors in R^d.
    """
    U, S, Vh = torch.linalg.svd(mlp_v_toxic, full_matrices=False)
    # U: [N, min(N,d)], S: [min(N,d)], Vh: [min(N,d), d]
    return U, S, Vh


def project_onto_vocabulary(
    vector: Tensor,
    embedding_matrix: Tensor,
    top_k: int = 10,
) -> Tuple[Tensor, Tensor]:
    """
    Project a value vector onto vocabulary space to find promoted tokens.

    Section 2: r_i = E @ v_i ∈ R^{|V|}
    Tokens with highest e_w · v_i are most promoted.

    Args:
        vector: [d] value vector to project.
        embedding_matrix: [|V|, d] token embedding matrix E.
        top_k: Number of top tokens to return.
    Returns:
        top_scores: [top_k] dot product scores.
        top_token_ids: [top_k] token IDs with highest projection.
    """
    scores = embedding_matrix @ vector  # [|V|]
    top_k_result = scores.topk(top_k)
    return top_k_result.values, top_k_result.indices


def compute_mean_activation(
    model: "GPT2LMHeadModel",
    input_ids: Tensor,
    selected_ids: List[Tuple[int, int]],
    device: torch.device,
    n_generate: int = 20,
) -> Dict[Tuple[int, int], float]:
    """
    Compute mean activations m_i = σ(x^ℓ · k_i^ℓ) for toxic key vectors.

    Section 5.2: Used to show drop in activations after DPO.
    Activations measured over 20 generated tokens × 1,199 prompts.

    Args:
        model: GPT2LMHeadModel (either base or DPO-tuned).
        input_ids: [batch, seq_len] prompt token IDs.
        selected_ids: [(layer_idx, neuron_idx)] for MLP.kToxic vectors.
        device: Computation device.
        n_generate: Number of tokens to generate per prompt (default 20).
    Returns:
        mean_activations: Dict mapping (layer_idx, neuron_idx) → mean activation.
    """
    # Register hooks to capture MLP pre-activation values
    activations: Dict[Tuple[int, int], List[float]] = {sid: [] for sid in selected_ids}
    hooks = []

    def make_hook(layer_idx: int) -> callable:
        def hook_fn(module, input, output):
            # input[0]: [batch, seq_len, d_mlp] pre-activation
            pre_act = input[0].detach()  # before GeLU
            for (l, i) in selected_ids:
                if l == layer_idx:
                    # σ(x · k_i) = GeLU(pre_act[:, :, i])
                    act_vals = torch.nn.functional.gelu(pre_act[:, :, i])
                    activations[(l, i)].extend(act_vals.flatten().tolist())
        return hook_fn

    for layer_idx in set(l for l, _ in selected_ids):
        hook = model.transformer.h[layer_idx].mlp.act.register_forward_hook(
            make_hook(layer_idx)
        )
        hooks.append(hook)

    with torch.no_grad():
        model.generate(input_ids.to(device), max_new_tokens=n_generate)

    for h in hooks:
        h.remove()

    return {sid: sum(v) / len(v) for sid, v in activations.items()}
