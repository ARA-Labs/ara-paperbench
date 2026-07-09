"""
FlexAttention with Document-Aware Masking — Core optimization from Record 11.
Verifies: C04 (64K context with doc-aware masking), H06 (block masking design)

Enables 64K token sequences with document-boundary-aware causal masking
and configurable sliding window, compiled into efficient CUDA kernels.
"""

import torch
from torch.nn.attention.flex_attention import (
    flex_attention,
    create_block_mask,
    BlockMask,
)
from typing import Optional


def build_document_causal_mask(
    document_ids: torch.Tensor,
    seq_len: int,
    sliding_window: int = 1024,
    block_size: int = 128,
) -> BlockMask:
    """
    Create a block mask that enforces:
    1. Causal masking (no future token attention)
    2. Document boundaries (no cross-document attention)
    3. Sliding window (attend only to last `sliding_window` tokens)

    Args:
        document_ids: (seq_len,) tensor where document_ids[i] is the document
                      index for token i. Packed sequences have multiple documents.
        seq_len: Total sequence length (e.g., 64K)
        sliding_window: Maximum attention span in tokens (default 1024)
        block_size: FlexAttention block granularity (must be 128 for H100)

    Returns:
        BlockMask compiled for efficient GPU execution
    """

    def mask_fn(b, h, q_idx, kv_idx):
        """Per-element mask function compiled by FlexAttention."""
        causal = q_idx >= kv_idx
        same_doc = document_ids[q_idx] == document_ids[kv_idx]
        in_window = (q_idx - kv_idx) <= sliding_window
        return causal & same_doc & in_window

    block_mask = create_block_mask(
        mask_fn,
        B=None,  # broadcast across batch
        H=None,  # broadcast across heads
        Q_LEN=seq_len,
        KV_LEN=seq_len,
        BLOCK_SIZE=block_size,
    )

    return block_mask


def flex_attention_forward(
    Q: torch.Tensor,
    K: torch.Tensor,
    V: torch.Tensor,
    block_mask: BlockMask,
    scale: Optional[float] = None,
) -> torch.Tensor:
    """
    Forward pass using FlexAttention with precomputed block mask.

    Args:
        Q: (B, H, S, D) query tensor
        K: (B, H, S, D) key tensor
        V: (B, H, S, D) value tensor
        block_mask: Precomputed BlockMask from build_document_causal_mask
        scale: Optional attention scale (default 1/sqrt(D))

    Returns:
        (B, H, S, D) attention output
    """
    return flex_attention(Q, K, V, block_mask=block_mask, scale=scale)
