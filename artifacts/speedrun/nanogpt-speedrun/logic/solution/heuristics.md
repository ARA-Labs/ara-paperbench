---
type: heuristics
paper: nanogpt-speedrun
---

# Design Heuristics

## H01 — Orthogonalize Only 2D+ Parameters
- **Choice**: Apply Muon's Newton-Schulz orthogonalization only to parameters with ndim ≥ 2; use standard AdamW for 1D parameters (biases, LayerNorm, embeddings).
- **Rationale**: Orthogonal updates are only meaningful for matrix-valued parameters where the Stiefel manifold structure exists. 1D parameters lack this geometric structure.
- **Sensitivity**: Critical — applying orthogonalization to 1D params causes training divergence.
- **Provenance**: Record 3 (Muon introduction)
- **Bounds**: Requires careful parameter partitioning. QKV splitting (Record 4) further refines which matrices get Muon vs. AdamW.

## H02 — Padded Vocabulary to Multiple of 64
- **Choice**: Pad vocabulary size from 50257 to 50304 (next multiple of 64).
- **Rationale**: GPU tensor cores operate most efficiently on dimensions that are multiples of 64. Padding eliminates wasted cycles in embedding and output projection layers.
- **Sensitivity**: Low — any multiple of 64 works. 128 alignment gives marginal further gains.
- **Provenance**: Record 5
- **Bounds**: Increases embedding table size by 47 × hidden_dim parameters (negligible).

## H03 — ReLU-Squared Activation
- **Choice**: Replace GELU with ReLU² (x * relu(x)) in MLP layers.
- **Rationale**: ReLU² is faster to compute than GELU (no tanh approximation), works well with torch.compile, and empirically matches GELU quality at this scale.
- **Sensitivity**: Medium — works at 124M scale. May not transfer to larger models where GELU/SwiGLU are preferred.
- **Provenance**: Record 5
- **Bounds**: Requires retuning learning rates after activation change.

## H04 — U-Net Skip Connections with Learnable Mixing
- **Choice**: Add encoder-decoder residual connections between transformer layers (layer i ↔ layer N-1-i) with learnable blending weights initialized near zero.
- **Rationale**: Provides gradient shortcuts across depth, enabling faster convergence. Zero-initialization means skip connections are gradually learned, not forced.
- **Sensitivity**: High — initialization and mixing schedule are critical. Momentum warmup (0.85→0.95) required for stability.
- **Provenance**: Record 8, refined in Record 10
- **Bounds**: Requires even number of layers. Adds 2N parameters (negligible).

## H05 — bfloat16 Throughout with CastedLinear
- **Choice**: Use bfloat16 for all activations via custom CastedLinear layer. Remove autocast and explicit dtype management.
- **Rationale**: Eliminates dtype casting overhead. CastedLinear handles precision at the layer boundary, simplifying the forward pass and enabling better torch.compile optimization.
- **Sensitivity**: Medium — requires careful handling of loss scaling and gradient accumulation.
- **Provenance**: Record 9
- **Bounds**: Requires hardware with native bfloat16 support (A100/H100).

## H06 — Document-Aware Block Masking
- **Choice**: Use FlexAttention's `create_block_mask` with document-aware causal masking: tokens attend only within the same document, with sliding window (1024 tokens) as fallback.
- **Rationale**: Prevents cross-document contamination in packed sequences. Sliding window bounds memory and compute while preserving local context.
- **Sensitivity**: Sliding window size (1024 → 128 in later records) trades off context vs. speed. Block mask granularity (128 tokens) must align with sequence packing.
- **Provenance**: Record 11, optimized in Records 12, 15, 17
- **Bounds**: Requires PyTorch 2.5+ and CUDA 12.5+.

## H07 — Async AllGather for Distributed Muon
- **Choice**: Overlap Muon's all_gather communication with Newton-Schulz computation using async NCCL operations.
- **Rationale**: Newton-Schulz iterations are compute-bound; all_gather is communication-bound. Overlapping hides communication latency behind useful compute.
- **Sensitivity**: Low — straightforward overlap. Requires careful CUDA stream management.
- **Provenance**: Records 6, 14
- **Bounds**: Benefit scales with number of GPUs. Minimal on single-GPU.

## H08 — FP8 Linear Head with Custom CUDA Ops
- **Choice**: Use FP8 (E4M3) precision for the language model head's linear layer via custom CUDA kernel, with per-tensor scaling.
- **Rationale**: The LM head (hidden_dim × vocab_size) is the largest single matrix multiply. FP8 halves its compute cost with negligible quality loss at this scale.
- **Sensitivity**: High — FP8 scale factors require careful tuning. Sigmoid logit offset (Record 18) compensates for FP8 quantization bias.
- **Provenance**: Record 18
- **Bounds**: Requires H100 with FP8 tensor core support. Not available on A100.

## H09 — Momentum Warmup Schedule
- **Choice**: Warm up Muon momentum from 0.85 to 0.95 over early training steps.
- **Rationale**: High initial momentum causes instability when combined with U-Net skip connections and aggressive learning rates. Gradual warmup allows the optimizer to explore before committing to momentum-driven directions.
- **Sensitivity**: Critical when combined with H04 (skip connections). Start value (0.85) and warmup schedule affect early training stability.
- **Provenance**: Record 8
- **Bounds**: Interacts with learning rate schedule. Must be co-tuned.

## H10 — Sequence Length Tuning (Training vs. Validation)
- **Choice**: Train on 48K tokens but validate on 256K tokens (Record 20).
- **Rationale**: Shorter training sequences reduce per-step wall-clock time. Longer validation sequences improve loss estimation stability. The model generalizes to longer contexts via RoPE position encoding.
- **Sensitivity**: Medium — 64K→48K training saves ~10% wall-clock. Further reduction degrades val_loss.
- **Provenance**: Record 20
- **Bounds**: Requires RoPE (not learned positional embeddings). Validation sequence length bounded by GPU memory.
