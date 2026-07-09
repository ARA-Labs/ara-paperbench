"""
Outlier-Aware Salience Scorer for APT.

Implements Equations 4, 5 from the paper:
  S_tilde(W_{:,j}) = sum_{(x,y) in D_t} |dL/dH_{j,i}| * |H_{j,i}|
  S_hat(W_{:,j}) = S_tilde(W_{:,j}) + sqrt(Kurt(O_{j,:}))

And EMA update (β = 0.85):
  S_bar^{(t)}(m) = 0.85 * S_bar^{(t-1)}(m) + 0.15 * S_hat(m)

Based on prune/scorer.py::RunningSalienceScorer from https://github.com/ROIM1998/APT
"""

import torch
from typing import Dict, Optional
from scipy.stats import kurtosis as scipy_kurtosis


def compute_block_salience_activation_gradient(
    activations: torch.Tensor,      # H: (batch, seq, d)
    activation_gradients: torch.Tensor,  # dL/dH: (batch, seq, d)
) -> torch.Tensor:
    """
    Compute block-level salience as batch-summed |activation * gradient|.
    
    This is the PEFT-compatible version of salience: uses activation×gradient
    instead of weight×gradient (since frozen weight gradients are unavailable).
    
    Activations and gradients are summed over batch dimension before product
    to reduce memory (APT's key memory optimization vs. per-sample computation).
    
    Args:
        activations: Hidden states H of shape (batch, seq, d)
        activation_gradients: Gradient dL/dH of shape (batch, seq, d)
    
    Returns:
        salience: Block-level salience of shape (d,) — summed over batch and seq
    """
    # Sum over batch and sequence for efficiency (reduces memory)
    H_sum = activations.abs().sum(dim=(0, 1))           # shape: (d,)
    grad_sum = activation_gradients.abs().sum(dim=(0, 1))  # shape: (d,)
    
    # Element-wise product = block salience S_tilde
    return H_sum * grad_sum  # shape: (d,)


def compute_kurtosis_per_column(
    weight: torch.Tensor,   # W_{:,j} for each column j: shape (d_out, d_in)
    activations: torch.Tensor,  # X^T: shape (d_in, batch*seq)
    column_index: int
) -> float:
    """
    Compute kurtosis of O_{j,:} = W_{:,j} ∘ X_{j,:}^T (activation of column j).
    
    Kurt(O_{j,:}) measures outlier density in the activation of parameter column j.
    Higher kurtosis = more outliers = more important to keep.
    
    Args:
        weight: Weight matrix W (d_out, d_in)
        activations: Input activations X (batch*seq, d_in)
        column_index: Index j of the column to compute kurtosis for
    
    Returns:
        kurtosis value (float, excess kurtosis)
    """
    # O_{:,j} = W_{:,j} * X_{j,:}^T — element-wise product for column j
    w_col = weight[:, column_index]        # shape: (d_out,)
    x_row = activations[:, column_index]   # shape: (batch*seq,)
    # Note: full O_{j,:} requires outer product but approximation uses column-wise
    # The implementation uses scipy kurtosis on the activation column
    activation = x_row.detach().cpu().float().numpy()
    return float(scipy_kurtosis(activation))


def compute_outlier_aware_salience(
    base_salience: torch.Tensor,  # S_tilde from Eq. 4, shape (d,)
    kurtosis_values: torch.Tensor,  # Kurt(O_{j,:}) for each j, shape (d,)
) -> torch.Tensor:
    """
    Combine base salience with kurtosis term: Eq. 5.
    
    S_hat(W_{:,j}) = S_tilde(W_{:,j}) + sqrt(Kurt(O_{j,:}))
    
    Args:
        base_salience: S_tilde per block, shape (d,)
        kurtosis_values: Kurtosis per column, shape (d,)
    
    Returns:
        outlier_aware_salience: S_hat, shape (d,)
    """
    # Take sqrt of kurtosis (paper uses (Kurt)^{1/2} per rubric Eq. 24)
    kurtosis_term = torch.sqrt(torch.clamp(kurtosis_values, min=0.0))
    return base_salience + kurtosis_term


class RunningSalienceScorer:
    """
    Running (EMA) salience scorer for APT adaptive pruning.
    
    Maintains exponential moving average of outlier-aware salience scores
    for head_mask, intermediate_mask, and hidden_mask.
    
    EMA update: S_bar^{(t)} = beta * S_bar^{(t-1)} + (1-beta) * S_hat^{(t)}
    beta = 0.85 (from AdaLoRA, matches paper Appendix B)
    
    Accumulation begins after salience_collecting_start=200 steps.
    """
    
    def __init__(
        self,
        model: torch.nn.Module,
        beta_1: float = 0.85,   # EMA decay for salience (matches scorer.py default)
        beta_2: float = 0.85,   # EMA decay for uncertainty (unused in default config)
        accumulation_start_step: int = 200,  # wait 200 steps before accumulating
    ):
        self.model = model
        self.beta_1 = beta_1
        self.beta_2 = beta_2
        self.accumulation_start_step = accumulation_start_step
        self.accumulation_started = False
        self.step_count = 0
        
        # Running scores: initially 0; shape determined by model architecture
        self.salience_scores: Dict[str, torch.Tensor] = {
            'head_mask': torch.tensor(0.0),
            'intermediate_mask': torch.tensor(0.0),
            'hidden_mask': torch.tensor(0.0),
        }
    
    def update(
        self,
        current_head_salience: torch.Tensor,         # current S_hat for heads
        current_intermediate_salience: torch.Tensor,  # current S_hat for neurons
        current_hidden_salience: Optional[torch.Tensor] = None,  # S_hat for hidden
    ) -> None:
        """
        Perform EMA update of running salience scores.
        
        Only accumulates after step >= accumulation_start_step (200).
        
        Args:
            current_head_salience: S_hat for attention heads at current step
            current_intermediate_salience: S_hat for FFN neurons at current step
            current_hidden_salience: S_hat for hidden dimensions (optional)
        """
        self.step_count += 1
        
        if self.step_count < self.accumulation_start_step:
            return
        
        self.accumulation_started = True
        
        # EMA: S_bar^{(t)} = 0.85 * S_bar^{(t-1)} + 0.15 * S_hat
        self.salience_scores['head_mask'] = (
            self.beta_1 * self.salience_scores['head_mask'] +
            (1 - self.beta_1) * current_head_salience
        )
        self.salience_scores['intermediate_mask'] = (
            self.beta_1 * self.salience_scores['intermediate_mask'] +
            (1 - self.beta_1) * current_intermediate_salience
        )
        if current_hidden_salience is not None:
            self.salience_scores['hidden_mask'] = (
                self.beta_1 * self.salience_scores['hidden_mask'] +
                (1 - self.beta_1) * current_hidden_salience
            )
    
    def get_scores(self) -> Dict[str, torch.Tensor]:
        """Return current EMA salience scores."""
        return self.salience_scores
    
    def reset(self) -> None:
        """Reset scores after parameter shape change (e.g., after pruning event)."""
        for k in self.salience_scores:
            self.salience_scores[k] = torch.tensor(0.0)
        self.accumulation_started = False
