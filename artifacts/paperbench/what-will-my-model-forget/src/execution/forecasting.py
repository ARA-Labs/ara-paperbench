"""
Forecasting models for predicting which upstream pretraining examples
will be forgotten upon learning an online example.

Implements:
1. ThresholdForecaster (Section 3.1)
2. LogitBasedForecaster (Section 3.2)
3. RepresentationBasedForecaster (Section 3.3)
"""

from __future__ import annotations
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor
from typing import Optional, Dict, Tuple, List


class ExampleEncoder(nn.Module):
    """
    Encodes an (input, output) example pair to a low-dimensional vector.
    
    For logit-based forecasting: returns per-token representations [T, d].
    For representation-based forecasting: returns averaged representation [d].
    
    Architecture: PTLM backbone (BART0 or FLAN-T5small) + 2-layer trainable MLP.
    """
    
    def __init__(
        self,
        backbone: nn.Module,  # Pre-trained LM backbone (BART0 or FLAN-T5small)
        hidden_dim: int,       # Hidden dimension of backbone
        output_dim: int,       # Output dimension d
        mode: str = "avg",     # "avg" for rep-based, "per_token" for logit-based
    ):
        super().__init__()
        self.backbone = backbone
        self.mlp = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
        )
        self.mode = mode
    
    def forward(
        self,
        input_ids: Tensor,       # [B, L_in] — tokenized input x
        decoder_input_ids: Tensor,  # [B, T] — tokenized output y
        attention_mask: Tensor,     # [B, L_in]
    ) -> Tensor:
        """
        Returns:
          mode="avg": [B, d] — averaged representation over output tokens
          mode="per_token": [B, T, d] — per-token representation of output
        """
        outputs = self.backbone(
            input_ids=input_ids,
            attention_mask=attention_mask,
            decoder_input_ids=decoder_input_ids,
        )
        # Extract final decoder hidden states: [B, T, H]
        hidden_states = outputs.last_hidden_state
        
        # Project through MLP
        projected = self.mlp(hidden_states)  # [B, T, d]
        
        if self.mode == "avg":
            return projected.mean(dim=1)  # [B, d]
        else:
            return projected  # [B, T, d]


class ThresholdForecaster:
    """
    Frequency-threshold based forecasting (Section 3.1, Equation 1).
    
    Predicts forgetting if the upstream example was forgotten >= gamma times
    in the training set, regardless of the online example.
    
    Non-parametric: threshold gamma is tuned on D_R^train to maximize F1.
    """
    
    def __init__(self, gamma: int = 1):
        self.gamma = gamma
        self.forgetting_counts: Dict[int, int] = {}  # xj_id -> count of times forgotten
        self.n_train: int = 0
    
    def fit(
        self,
        forgetting_counts: Dict[int, int],  # upstream example id -> forgetting count
        n_train: int,                         # total number of training online examples
    ) -> None:
        """
        Store forgetting counts and tune threshold gamma to maximize F1.
        forgetting_counts[j] = number of online examples in D_R^train that caused xj to be forgotten.
        """
        self.forgetting_counts = forgetting_counts
        self.n_train = n_train
        # Note: gamma should be tuned externally by searching over values and computing F1 on D_R^train
    
    def predict(self, upstream_example_ids: List[int]) -> List[int]:
        """
        Returns binary predictions: 1 if forgotten (count >= gamma), else 0.
        
        Args:
            upstream_example_ids: list of upstream example indices
        Returns:
            List of binary predictions z_ij (same value for all online examples)
        """
        return [
            1 if self.forgetting_counts.get(j, 0) >= self.gamma else 0
            for j in upstream_example_ids
        ]


class LogitBasedForecaster(nn.Module):
    """
    Trainable logit-based forecasting model (Section 3.2).
    
    Predicts updated logits of upstream example xj by approximating
    the logit-change transfer via a trainable kernel:
      Theta_tilde(xj, xi) = h(xj, yj) @ h(xi, yi).T  [T x T]
      f_hat_i(xj) = Theta_tilde @ (f_hat_i(xi) - f_hat_0(xi)) + f_hat_0(xj)
    
    Trained with margin loss (Equation 3).
    """
    
    def __init__(self, encoder: ExampleEncoder, top_k_logits: int = 100):
        """
        Args:
            encoder: ExampleEncoder in "per_token" mode, outputs [B, T, d]
            top_k_logits: Number of top logit values to cache per token
        """
        super().__init__()
        self.encoder = encoder  # must be mode="per_token"
        self.top_k_logits = top_k_logits
    
    def predict_updated_logits(
        self,
        h_xi: Tensor,         # [T_i, d] — encoder output for online example xi
        h_xj: Tensor,         # [T_j, d] — encoder output for upstream example xj
        delta_logits_xi: Tensor,  # [T_i, V] — logit change of xi (f_i(xi) - f_0(xi))
        logits_xj_base: Tensor,   # [T_j, V] — base logits f_0(xj) (possibly sparse top-k)
    ) -> Tensor:
        """
        Predicts f_hat_i(xj) using the trainable kernel.
        
        Returns:
            Predicted updated logits of xj: [T_j, V]
        """
        # Compute trainable kernel: [T_j, T_i]
        kernel = torch.matmul(h_xj, h_xi.T)
        
        # Transfer logit changes: [T_j, V]
        transferred_changes = torch.matmul(kernel, delta_logits_xi)
        
        # Predicted updated logits
        predicted_logits = logits_xj_base + transferred_changes
        return predicted_logits
    
    def margin_loss(
        self,
        predicted_logits_xj: Tensor,  # [T, V] — predicted logits of xj under fi
        yj_token_ids: Tensor,          # [T] — ground truth token ids of yj
        zij: int,                       # binary forgetting label (0 or 1)
    ) -> Tensor:
        """
        Margin loss (Equation 3):
        max(0, 1 + (-1)^zij * (max_{v!=yj} f_hat_i(xj)[v] - f_hat_i(xj)[yj]))
        
        For zij=0 (not forgotten): penalize if correct token NOT predicted
        For zij=1 (forgotten): penalize if correct token IS still predicted
        """
        T = predicted_logits_xj.shape[0]
        losses = []
        for t in range(T):
            logits_t = predicted_logits_xj[t]  # [V]
            y_t = yj_token_ids[t].item()
            
            # Score of correct token
            correct_score = logits_t[y_t]
            
            # Max score among incorrect tokens
            mask = torch.ones_like(logits_t, dtype=torch.bool)
            mask[y_t] = False
            max_wrong_score = logits_t[mask].max()
            
            # Margin loss
            loss_t = F.relu(1.0 + (-1) ** zij * (max_wrong_score - correct_score))
            losses.append(loss_t)
        
        return torch.stack(losses).mean()
    
    def forward_train(
        self,
        xi_input_ids: Tensor,   # [T_in_i] — tokenized input of online example xi
        xi_decoder_ids: Tensor, # [T_i] — tokenized output yi
        xj_input_ids: Tensor,   # [T_in_j] — tokenized input of upstream xj
        xj_decoder_ids: Tensor, # [T_j] — tokenized output yj
        delta_logits_xi: Tensor,    # [T_i, V] — logit change of xi
        logits_xj_base: Tensor,     # [T_j, V] — base logits of xj
        yj_token_ids: Tensor,       # [T_j] — ground truth tokens
        zij: int,                   # forgetting label
    ) -> Tensor:
        """Training step: compute margin loss."""
        h_xi = self.encoder(
            xi_input_ids.unsqueeze(0),
            xi_decoder_ids.unsqueeze(0),
            attention_mask=None,
        ).squeeze(0)  # [T_i, d]
        
        h_xj = self.encoder(
            xj_input_ids.unsqueeze(0),
            xj_decoder_ids.unsqueeze(0),
            attention_mask=None,
        ).squeeze(0)  # [T_j, d]
        
        predicted_logits = self.predict_updated_logits(h_xi, h_xj, delta_logits_xi, logits_xj_base)
        return self.margin_loss(predicted_logits, yj_token_ids, zij)


class RepresentationBasedForecaster(nn.Module):
    """
    Black-box representation-based forecasting model (Section 3.3, Equation 4).
    
    Predicts forgetting probability directly via:
      g(xi, xj) = sigmoid(h(xj, yj) . h(xi, yi) + b_j)
    
    where b_j is a log-odds frequency prior for upstream example xj.
    
    Trained with binary cross-entropy, positive pairs weighted by alpha=0.1.
    """
    
    def __init__(
        self,
        encoder: ExampleEncoder,   # mode="avg", outputs [B, d]
        positive_weight: float = 0.1,  # alpha for positive pairs
    ):
        super().__init__()
        self.encoder = encoder  # must be mode="avg"
        self.positive_weight = positive_weight
        self.frequency_priors: Optional[Dict[int, float]] = None
    
    def compute_frequency_priors(
        self,
        forgetting_counts: Dict[int, int],  # xj_id -> count of times forgotten in D^train_R
        n_train: int,                         # |D^train_R|
    ) -> Dict[int, float]:
        """
        Compute log-odds frequency prior for each upstream example (Section 3.3).
        
        b_j = log(P(forgot|xj) / P(not_forgot|xj)) estimated from training data.
        
        Returns:
            Dict mapping upstream example id -> log-odds prior b_j
        """
        priors = {}
        for j, count in forgetting_counts.items():
            p_forgot = count / n_train
            p_not_forgot = 1 - p_forgot
            # Clamp to avoid log(0)
            p_forgot = max(p_forgot, 1e-10)
            p_not_forgot = max(p_not_forgot, 1e-10)
            priors[j] = torch.log(torch.tensor(p_forgot / p_not_forgot)).item()
        self.frequency_priors = priors
        return priors
    
    def forward(
        self,
        xi_input_ids: Tensor,   # [B, L_in]
        xi_decoder_ids: Tensor, # [B, T_i]
        xj_input_ids: Tensor,   # [B, L_in]
        xj_decoder_ids: Tensor, # [B, T_j]
        xi_attention_mask: Tensor,  # [B, L_in]
        xj_attention_mask: Tensor,  # [B, L_in]
        bias: Optional[Tensor] = None,  # [B] frequency priors b_j; None = no prior
    ) -> Tensor:
        """
        Returns:
            Forgetting probabilities p_ij: [B] — P(xj forgotten | xi learned)
        """
        h_xi = self.encoder(xi_input_ids, xi_decoder_ids, xi_attention_mask)  # [B, d]
        h_xj = self.encoder(xj_input_ids, xj_decoder_ids, xj_attention_mask)  # [B, d]
        
        # Inner product similarity: [B]
        similarity = (h_xj * h_xi).sum(dim=-1)
        
        if bias is not None:
            similarity = similarity + bias
        
        return torch.sigmoid(similarity)
    
    def compute_bce_loss(
        self,
        p_ij: Tensor,   # [B] predicted probabilities
        z_ij: Tensor,   # [B] ground truth binary labels
    ) -> Tensor:
        """
        Weighted binary cross-entropy loss.
        Positive pairs (z_ij=1) get weight alpha=0.1.
        """
        pos_mask = z_ij == 1
        weights = torch.ones_like(z_ij, dtype=torch.float)
        weights[pos_mask] = self.positive_weight
        
        bce = F.binary_cross_entropy(p_ij, z_ij.float(), reduction='none')
        return (bce * weights).mean()
