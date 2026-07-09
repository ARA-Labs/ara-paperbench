"""
APT Adapter — Core implementation of the Adaptive Pruning and Tuning adapter.

Based on: "APT: Adaptive Pruning and Tuning Pretrained Language Models
           for Efficient Training and Inference" (Zhao et al., ICML 2024)
arXiv:2401.12200

The APT adapter extends LoRA with:
  - Binary input/output pruning masks (m_i, m_o)
  - Dynamic rank (r_apt) that grows during training in salient layers
  - Forward: H_apt(X) = m_o ∘ (W + s · W_B W_A) X ∘ m_i

This file implements ONLY the novel APT adapter; no argparse or logging.
"""

import math
import torch
import torch.nn as nn
from typing import Optional


class APTAdapter(nn.Module):
    """
    APT Adapter layer.

    Wraps a frozen linear layer W ∈ R^{d_o × d_i} with:
      - m_i ∈ R^{d_i}: binary input pruning mask (prunes hidden dims)
      - m_o ∈ R^{d_o}: binary output pruning mask (prunes heads or FFN neurons)
      - W_A ∈ R^{r_apt × d_i}: low-rank tuning matrix (trained)
      - W_B ∈ R^{d_o × r_apt}: low-rank tuning matrix (trained)
      - s: constant scaling factor (default 2, following LoRA)

    Forward pass (Equation 2 in paper):
      H_apt(X) = m_o ∘ (W + s · W_B W_A) X ∘ m_i

    Pruning masks are applied as Hadamard products (∘) between the mask
    vectors and the corresponding rows/columns of the weight matrix.
    A mask entry of 0 prunes the corresponding block; 1 retains it.
    """

    def __init__(
        self,
        d_i: int,         # input dimension
        d_o: int,         # output dimension
        rank: int = 8,    # initial adapter rank r_apt
        scaling: float = 2.0,  # LoRA scaling factor s
        bias: bool = False,
    ):
        super().__init__()
        self.d_i = d_i
        self.d_o = d_o
        self.rank = rank
        self.scaling = scaling

        # Frozen pre-trained weight (not updated during training)
        self.W = nn.Parameter(torch.empty(d_o, d_i), requires_grad=False)

        # Tuning parameters (trained)
        # W_A initialized from N(0, σ²) following LoRA convention
        self.W_A = nn.Parameter(torch.empty(rank, d_i))
        # W_B initialized to zeros (output unchanged at initialization)
        self.W_B = nn.Parameter(torch.zeros(d_o, rank))

        # Binary pruning masks (0=pruned, 1=retained)
        # Stored as float for gradual decay; thresholded during forward
        self.register_buffer('m_i', torch.ones(d_i))   # input mask
        self.register_buffer('m_o', torch.ones(d_o))   # output mask

        if bias:
            self.bias = nn.Parameter(torch.zeros(d_o))
        else:
            self.bias = None

        self._init_weights()

    def _init_weights(self):
        """Initialize W_A from N(0, 1/rank), W_B to zeros (LoRA convention)."""
        nn.init.normal_(self.W_A, mean=0.0, std=1.0 / math.sqrt(self.rank))
        nn.init.zeros_(self.W_B)

    def forward(self, X: torch.Tensor) -> torch.Tensor:
        """
        APT adapter forward pass.

        Args:
            X: input tensor of shape (..., d_i)

        Returns:
            output tensor of shape (..., d_o) with pruned dimensions zeroed.

        Implements: H_apt(X) = m_o ∘ (W + s · W_B W_A) X ∘ m_i
        """
        # Apply input mask: zero out pruned input dimensions
        # m_i shape: (d_i,) → broadcast to (..., d_i)
        X_masked = X * self.m_i  # element-wise; pruned dims become 0

        # Compute effective weight: W + s · W_B W_A
        # W: (d_o, d_i), W_B: (d_o, rank), W_A: (rank, d_i)
        W_eff = self.W + self.scaling * (self.W_B @ self.W_A)  # (d_o, d_i)

        # Linear transform
        out = X_masked @ W_eff.T  # (..., d_o)

        if self.bias is not None:
            out = out + self.bias

        # Apply output mask: zero out pruned output dimensions (heads/neurons)
        # m_o shape: (d_o,) → broadcast to (..., d_o)
        out = out * self.m_o

        return out

    def expand_rank(self, new_rank: int, sigma: float = 0.01) -> None:
        """
        Expand adapter rank from self.rank to new_rank (Section 4.3).

        New W_A rows: initialized from N(0, sigma²)
        New W_B columns: initialized to zeros (preserves output unchanged)

        Args:
            new_rank: target rank r'_apt = floor(r_apt * Δt' / Δt)
            sigma: std for Gaussian initialization of new W_A rows
        """
        assert new_rank > self.rank, "new_rank must be larger than current rank"
        delta_r = new_rank - self.rank

        # Expand W_A: concatenate new rows sampled from N(0, sigma²)
        new_W_A_rows = torch.randn(delta_r, self.d_i, device=self.W_A.device) * sigma
        new_W_A = torch.cat([self.W_A.data, new_W_A_rows], dim=0)  # (new_rank, d_i)

        # Expand W_B: concatenate new zero columns
        new_W_B_cols = torch.zeros(self.d_o, delta_r, device=self.W_B.device)
        new_W_B = torch.cat([self.W_B.data, new_W_B_cols], dim=1)  # (d_o, new_rank)

        # Replace parameters
        self.W_A = nn.Parameter(new_W_A)
        self.W_B = nn.Parameter(new_W_B)
        self.rank = new_rank

    def merge_weights(self) -> torch.Tensor:
        """
        Merge adapter weights into frozen weight for inference.

        Returns W_merged = W + s · W_B W_A, to replace W at inference time.
        After merging, the adapter add no inference overhead.
        """
        return self.W + self.scaling * (self.W_B @ self.W_A)

    def compute_adapter_importance(self) -> float:
        """
        Compute adapter importance score I(H_apt) = Σ_{i,j} S(W_{B_{i,j}}).

        Used in Adaptive Tuning (Section 4.3) to rank adapters for rank growth.
        Salience S(W_{B_{i,j}}) = |W_{B_{i,j}} · ∂L/∂W_{B_{i,j}}|

        Note: this requires W_B.grad to be populated after backward().
        Returns sum of |W_B * grad_W_B| as scalar importance score.
        """
        if self.W_B.grad is None:
            return 0.0
        return (self.W_B * self.W_B.grad).abs().sum().item()
