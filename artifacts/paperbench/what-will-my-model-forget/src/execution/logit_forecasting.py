"""
Logit-Change-Based Forgetting Forecaster
Based on: Jin & Ren, "What Will My Model Forget?" (ICML 2024)

Implements Algorithm 1 (training) and Algorithm 2 (inference).
Uses NTK-inspired logit-change transfer (Equation 2) to forecast forgetting.
Two variants:
  - Fixed Logit: uses frozen final-layer representations as kernel
  - Trainable Logit: learns a low-dimensional kernel approximation
"""

import torch
import torch.nn as nn
from torch import Tensor
from typing import Optional, Tuple


class TrainableLogitForecaster(nn.Module):
    """
    Logit-based forgetting forecaster with trainable kernel.
    
    Approximates Θ(x_j, x_i) Θ^{-1}(x_i, x_i) with Θ̃(x_j, x_i) = h_j · h_i^T.
    
    Predicted updated logits (Eqn. 2 approximation):
        f̂_i(x_j) = Θ̃(x_j, x_i) [f̂_i(x_i) - f̂_0(x_i)] + f̂_0(x_j)
    """

    def __init__(self, encoder: nn.Module):
        """
        Args:
            encoder: Trainable encoder h: (x,y) → R^{T×d}
                     For BART0: BART0 + 2-layer MLP
                     For FLAN-T5: FLAN-T5small + 2-layer MLP
        """
        super().__init__()
        self.encoder = encoder

    def predict_logit_change(
        self,
        h_i: Tensor,             # (T_i, d) — output representations of online example x_i
        h_j: Tensor,             # (T_j, d) — output representations of upstream example x_j
        delta_logits_i: Tensor,  # (T_i, V) — observed logit change of online example
        logits_j_before: Tensor, # (T_j, V) — pre-update logits of upstream example (top-k cached)
    ) -> Tensor:
        """
        Predicts the post-update logits for upstream example x_j.
        
        Θ̃(x_j, x_i) = h_j · h_i^T ∈ R^{T_j × T_i}
        f̂_i(x_j) = Θ̃ · Δf̂_i(x_i) + f̂_0(x_j)
        
        Note: Δf̂_i(x_i) has shape (T_i, V); Θ̃ has shape (T_j, T_i);
        product gives (T_j, V) — logit change for x_j.
        
        Returns: predicted post-update logits for x_j, shape (T_j, V) or (T_j, k) for top-k
        """
        # Trainable kernel: T_j × T_i
        kernel = torch.matmul(h_j, h_i.transpose(-1, -2))  # (T_j, T_i)
        # Predicted logit change for x_j
        delta_logits_j_pred = torch.matmul(kernel, delta_logits_i)  # (T_j, V)
        # Predicted post-update logits
        logits_j_after_pred = delta_logits_j_pred + logits_j_before  # (T_j, V)
        return logits_j_after_pred

    def predict_forgetting(
        self,
        h_i: Tensor,             # (T_i, d)
        h_j: Tensor,             # (T_j, d)
        delta_logits_i: Tensor,  # (T_i, V or k)
        logits_j_before: Tensor, # (T_j, V or k) — cached top-k=100 logits
        y_j_token_ids: Tensor,   # (T_j,) — correct token ids for output y_j
    ) -> Tensor:
        """
        Binary forgetting prediction: ẑ_ij = 1 if argmax predicted logits ≠ y_j.
        
        Returns: ẑ_ij ∈ {0, 1}
        """
        logits_pred = self.predict_logit_change(h_i, h_j, delta_logits_i, logits_j_before)
        # Check if predicted argmax differs from ground truth y_j
        predicted_tokens = logits_pred.argmax(dim=-1)  # (T_j,)
        correct = (predicted_tokens == y_j_token_ids).all()
        return torch.tensor(0 if correct else 1, dtype=torch.long)


def margin_loss(
    logits_j_pred: Tensor,  # (T_j, V) — predicted post-update logits for x_j
    y_j: Tensor,            # (T_j,) — correct token ids
    z_ij: int,              # 0 (not forgotten) or 1 (forgotten)
    margin: float = 1.0,
) -> Tensor:
    """
    Margin loss from Equation 3:
    L = max(0, 1 + (-1)^z_ij * (max_{v≠y_j} f̂_i(x_j)[v] - f̂_i(x_j)[y_j]))
    
    If z_ij=0 (not forgotten): penalizes if correct token score < second-best + margin
    If z_ij=1 (forgotten): penalizes if correct token score > second-best - margin
    
    Averaged over T_j output positions.
    """
    total_loss = torch.tensor(0.0)
    for t in range(logits_j_pred.shape[0]):
        logit_correct = logits_j_pred[t, y_j[t]]
        # Max logit over all tokens except y_j[t]
        mask = torch.ones(logits_j_pred.shape[-1], dtype=torch.bool)
        mask[y_j[t]] = False
        logit_best_wrong = logits_j_pred[t, mask].max()
        sign = (-1) ** z_ij
        loss_t = torch.clamp(margin + sign * (logit_best_wrong - logit_correct), min=0.0)
        total_loss = total_loss + loss_t
    return total_loss / logits_j_pred.shape[0]


def fixed_logit_forecaster(
    base_lm: nn.Module,
    online_example: Tuple,     # Tokenized (x_i, y_i)
    upstream_example: Tuple,   # Tokenized (x_j, y_j)
    updated_lm: nn.Module,     # f_i = f_0 updated on (x_i, y_i)
    top_k: int = 100,
) -> int:
    """
    Fixed logit-based forecasting (non-trainable).
    Uses frozen final-layer representations as the kernel (Algorithm 2 variant).
    
    When only LM heads are tuned, gradients ∇W_Head f̂(x) = representations before head,
    making the fixed kernel identical to the ground-truth NTK (Section 3.2).
    
    Returns: ẑ_ij ∈ {0, 1}
    """
    with torch.no_grad():
        # Get final-layer representations from base LM (before head)
        # These serve as h(x,y) in the fixed kernel
        rep_i = _get_final_layer_repr(base_lm, *online_example)    # (T_i, H)
        rep_j = _get_final_layer_repr(base_lm, *upstream_example)  # (T_j, H)

        # Logits before update
        logits_i_before = _get_logits(base_lm, *online_example)    # (T_i, V)
        logits_j_before = _get_logits(base_lm, *upstream_example)  # (T_j, V)

        # Logits after update for online example
        logits_i_after = _get_logits(updated_lm, *online_example)  # (T_i, V)
        delta_logits_i = logits_i_after - logits_i_before           # (T_i, V)

        # Fixed kernel: rep_j · rep_i^T  ∈ R^{T_j × T_i}
        kernel = torch.matmul(rep_j, rep_i.transpose(-1, -2))       # (T_j, T_i)
        delta_logits_j_pred = torch.matmul(kernel, delta_logits_i)  # (T_j, V)
        logits_j_pred = delta_logits_j_pred + logits_j_before        # (T_j, V)

        y_j = upstream_example[2]  # decoder_input_ids as target
        predicted = logits_j_pred.argmax(dim=-1)
        forgotten = not (predicted == y_j).all().item()
    return int(forgotten)


def _get_final_layer_repr(model: nn.Module, input_ids: Tensor, attn_mask: Tensor,
                          dec_ids: Tensor, dec_mask: Tensor) -> Tensor:
    """Extract final decoder layer representations (before LM head)."""
    outputs = model(input_ids=input_ids, attention_mask=attn_mask,
                    decoder_input_ids=dec_ids, decoder_attention_mask=dec_mask,
                    output_hidden_states=True)
    return outputs.decoder_hidden_states[-1].squeeze(0)  # (T, H)


def _get_logits(model: nn.Module, input_ids: Tensor, attn_mask: Tensor,
                dec_ids: Tensor, dec_mask: Tensor) -> Tensor:
    """Extract pre-softmax logits from the model."""
    outputs = model(input_ids=input_ids, attention_mask=attn_mask,
                    decoder_input_ids=dec_ids, decoder_attention_mask=dec_mask)
    return outputs.logits.squeeze(0)  # (T, V)
