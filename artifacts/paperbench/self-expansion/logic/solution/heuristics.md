# Heuristics

## H01: Z-Score Normalization for Robust Expansion Signal
- **Rationale**: Raw reconstruction errors vary across tasks and adapters due to differing feature scales and distributions. Direct thresholding of raw errors would require per-dataset threshold tuning. Z-score normalization removes scale and perturbation, making the threshold τ robust across datasets.
- **Sensitivity**: low
- **Bounds**: Expansion threshold τ ∈ [1.0, 2.0] works well for ImageNet-A; τ ∈ [1.0, 6.0] for VTAB. Values >1.5 (ImageNet-A) or >6.0 (VTAB) risk under-expansion; values <1.0 risk over-expansion.
- **Code ref**: [src/execution/sema.py]
- **Source**: §3.6, Fig. 6

## H02: 500-Sample Sliding Buffer for Running Statistics
- **Rationale**: Computing population statistics over all training samples is impractical at inference/scanning time. A fixed-size buffer of the 500 most recent samples provides a stable estimate that adapts to the local data distribution without unbounded memory growth.
- **Sensitivity**: low
- **Bounds**: Buffer size=500 (fixed in implementation). Smaller buffers may produce noisier estimates; larger buffers add memory overhead.
- **Code ref**: [src/execution/sema.py]
- **Source**: Appendix A.1

## H03: Shallow-to-Deep Layer Scanning Order
- **Rationale**: Distribution shifts in shallow layers propagate and affect all deeper layers. By scanning from shallow to deep, new adapters are added and trained at shallow layers first, ensuring that the representations seen by deeper RDs are already adapted before deep-layer scanning occurs.
- **Sensitivity**: medium
- **Bounds**: Scanning order must be shallow-to-deep. Reversing the order would cause deep RDs to evaluate unadapted features.
- **Code ref**: [src/execution/sema.py]
- **Source**: §3.6

## H04: Freeze Existing Router Columns When Expanding
- **Rationale**: When a new adapter is added, only the new column of $\mathbf{W}^l_{\text{mix}}$ should be trained. Freezing existing columns prevents the weights for previously learned adapters from being disrupted (analogous to the common practice for expanding classification heads in CL).
- **Sensitivity**: medium
- **Bounds**: The frozen columns control forgetting in the router but cannot fully eliminate it due to softmax normalization across all entries.
- **Code ref**: [src/execution/sema.py]
- **Source**: §3.4

## H05: Separate Learning Rates for Adapters vs. RDs
- **Rationale**: Functional adapters and RDs have different learning objectives (classification + adaptation vs. reconstruction). Higher LR for RDs (0.01 vs. 0.005) allows faster convergence of the reconstruction objective without destabilizing adapter training.
- **Sensitivity**: medium
- **Bounds**: adapter LR=0.005, RD LR=0.01; both with cosine annealing decay. SGD optimizer.
- **Code ref**: [src/configs/training.md]
- **Source**: §4.1

## H06: Soft Mixture Router Over Hard Selection
- **Rationale**: Hard selection (top-1 or random) of a single adapter discards information from all other adapters and is unreliable for individual samples (particularly for inputs that lie between known distributions). Soft weighted mixture allows the model to combine representations from multiple adapters, producing more robust outputs.
- **Sensitivity**: medium
- **Bounds**: Any differentiable mixing strategy (softmax) outperforms hard selection. Average weighting (uniform) also underperforms the learned router, confirming the need for a trained weighting function.
- **Code ref**: [src/execution/sema.py]
- **Source**: §3.4, Table 2, Appendix C.3
