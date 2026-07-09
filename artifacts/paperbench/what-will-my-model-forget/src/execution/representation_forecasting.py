"""
Representation-Based Forgetting Forecaster
Based on: Jin & Ren, "What Will My Model Forget?" (ICML 2024)

Implements Algorithm 3 (training) and Algorithm 4 (inference).
The forecasting model predicts which upstream pretraining examples will be
forgotten when a specific online learning example is used to update the base LM.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor
from typing import Optional


class RepresentationEncoder(nn.Module):
    """
    Encoder h: maps (x, y) pairs to averaged token representations.
    Architecture: pretrained LM backbone + 2-layer MLP adapter.
    
    For BART0 experiments: uses BART0 backbone.
    For FLAN-T5 experiments: uses FLAN-T5small backbone.
    """

    def __init__(self, backbone_model: nn.Module, hidden_dim: int, output_dim: int):
        """
        Args:
            backbone_model: Pre-trained LM (e.g., BART0 or FLAN-T5small) for encoding
            hidden_dim: Intermediate MLP dimension
            output_dim: d, the final representation dimension
        """
        super().__init__()
        self.backbone = backbone_model
        # 2-layer MLP as specified in Appendix B
        self.mlp = nn.Sequential(
            nn.Linear(backbone_model.config.hidden_size, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(
        self,
        input_ids: Tensor,          # (B, L_in) — input token ids
        attention_mask: Tensor,     # (B, L_in)
        decoder_input_ids: Tensor,  # (B, L_out) — output token ids (y)
        decoder_attention_mask: Tensor,  # (B, L_out)
    ) -> Tensor:
        """
        Returns: averaged representation h(x, y) ∈ R^{B × d}
        
        Extracts final-layer decoder representations of output tokens,
        then averages over token positions (as described in Section 3.3).
        """
        outputs = self.backbone(
            input_ids=input_ids,
            attention_mask=attention_mask,
            decoder_input_ids=decoder_input_ids,
            decoder_attention_mask=decoder_attention_mask,
            output_hidden_states=True,
        )
        # Final layer decoder hidden states: (B, L_out, H)
        decoder_hidden = outputs.decoder_hidden_states[-1]
        # Average over output token positions (masked mean)
        mask = decoder_attention_mask.unsqueeze(-1).float()  # (B, L_out, 1)
        avg_hidden = (decoder_hidden * mask).sum(dim=1) / mask.sum(dim=1)  # (B, H)
        # Project to output_dim via MLP
        return self.mlp(avg_hidden)  # (B, d)


class RepresentationForecaster(nn.Module):
    """
    Binary classifier g(⟨x_i,y_i⟩, ⟨x_j,y_j⟩) = σ(h_j · h_i^T + b_j)
    
    Predicts whether upstream example j is forgotten when online example i is learned.
    Implements Equation 4 from Section 3.3.
    """

    def __init__(self, encoder: RepresentationEncoder):
        super().__init__()
        self.encoder = encoder

    def compute_frequency_prior(
        self,
        train_forgetting_counts: Tensor,  # (N_PT,) — times each j was forgotten in D^train_R
        n_train: int,                     # |D^train_R|
    ) -> Tensor:
        """
        Computes log-odds frequency prior b_j for all upstream examples j.
        
        b_j = log(p_forget) - log(1 - p_forget)
        where p_forget = |{i ∈ D^train : z_ij=1}| / |D^train|
        
        Returns: b_j ∈ R^{N_PT}
        """
        p_forget = train_forgetting_counts.float() / n_train
        p_forget = p_forget.clamp(1e-6, 1 - 1e-6)  # numerical stability
        b_j = torch.log(p_forget) - torch.log(1 - p_forget)  # log odds
        return b_j  # (N_PT,)

    def forward(
        self,
        h_i: Tensor,  # (B, d) — online example representations
        h_j: Tensor,  # (B, d) — upstream example representations
        b_j: Tensor,  # (B,) — frequency prior for each j
    ) -> Tensor:
        """
        Computes forgetting probability for each (i, j) pair.
        
        Returns: p_forget ∈ R^{B}, values in (0, 1)
        """
        # Inner product of representations: sum over d dimensions
        inner_product = (h_j * h_i).sum(dim=-1)  # (B,)
        logit = inner_product + b_j              # (B,)
        return torch.sigmoid(logit)              # (B,)


def train_representation_forecaster(
    forecaster: RepresentationForecaster,
    train_online_examples: list,       # List of (input_ids, attn_mask, dec_ids, dec_mask) for D^train_R
    train_pretraining_examples: list,  # List of (input_ids, attn_mask, dec_ids, dec_mask) for D_PT
    forgetting_labels: Tensor,         # (N_train_R, N_PT) — z_ij ground truth
    frequency_priors: Tensor,          # (N_PT,) — b_j
    optimizer_lm: torch.optim.Optimizer,   # LR=1e-5 for backbone
    optimizer_mlp: torch.optim.Optimizer,  # LR=1e-4 for MLP
    max_steps: int = 100000,
    batch_size: int = 16,
    positive_weight: float = 0.1,     # α=0.1 for positive pairs
    device: str = 'cuda',
) -> None:
    """
    Training loop for representation-based forecaster (Algorithm 3).
    
    Mini-batch: 8 positive + 8 negative pairs per batch of 16 (Appendix B).
    Positive pairs receive weight α=0.1 in BCE loss.
    """
    forecaster.train()
    for step in range(max_steps):
        # Sample balanced batch: 8 positive + 8 negative pairs
        pos_batch = _sample_pairs(forgetting_labels, n_pos=8, n_neg=8, label=1)
        neg_batch = _sample_pairs(forgetting_labels, n_pos=8, n_neg=8, label=0)
        # For each pair (i, j): encode h_i, h_j; compute BCE loss with weighting
        # ... (data loading and forward pass)
        pass  # Implementation: sample, encode, compute BCE, backprop


def infer_representation_forecaster(
    forecaster: RepresentationForecaster,
    online_example: tuple,             # (input_ids, attn_mask, dec_ids, dec_mask) for single ⟨x_i,y_i⟩
    cached_h_j: Tensor,               # (N_PT, d) — precomputed encoder output for all j ∈ D_PT
    cached_b_j: Tensor,               # (N_PT,) — frequency priors for all j
    threshold: float = 0.5,
    device: str = 'cuda',
) -> Tensor:
    """
    Inference for representation-based forecaster (Algorithm 4).
    
    Predicts ẑ_ij for all j ∈ D_PT given a single online example ⟨x_i,y_i⟩.
    Representations of D_PT examples are precomputed and cached for efficiency.
    
    Returns: ẑ_ij ∈ {0,1}^{N_PT}
    """
    forecaster.eval()
    with torch.no_grad():
        # Encode online example
        h_i = forecaster.encoder(*[t.to(device) for t in online_example])  # (1, d)
        h_i_expanded = h_i.expand(cached_h_j.shape[0], -1)  # (N_PT, d)
        # Compute forgetting probabilities for all j
        p_forget = forecaster(h_i_expanded, cached_h_j.to(device), cached_b_j.to(device))
        ẑ = (p_forget >= threshold).long()
    return ẑ  # (N_PT,)


def _sample_pairs(
    forgetting_labels: Tensor,  # (N_R, N_PT)
    n_pos: int,
    n_neg: int,
    label: int,
) -> list:
    """Helper to sample balanced positive/negative pairs from the label matrix."""
    raise NotImplementedError("Sampling implementation depends on data loader setup")
