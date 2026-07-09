---
# Heuristics and Design Tricks

## H01: Population size K = 4 + 3 × log(prompt_dim)
- **Rationale**: Following the CMA-ES convention (Hansen, 2016), the default population size is derived from the optimization problem dimension (prompt_dim = d × Np). This balances exploration and exploitation: too small K degrades performance; K > 15 gives converging returns.
- **Sensitivity**: low — FOA works for all K ∈ [2, 28] ∩ N+
- **Bounds**: K ≥ 2 for reasonable adaptation; K = 28 for best accuracy; K = 6 matches TENT accuracy with lower memory
- **Code ref**: [src/execution/foa.py]
- **Source**: Section 4 (Implementation Details); Figure 2(a)

## H02: Trade-off parameter λ = 0.4 × BS/64 (0.2 × BS/64 for ImageNet-R)
- **Rationale**: λ balances the magnitude of the entropy term and the activation discrepancy term in Eq. 5. Scaling with BS/64 normalizes for batch size variations. ImageNet-R uses 0.2 because the rendition distribution shift is less severe, requiring less discrepancy correction relative to entropy.
- **Sensitivity**: low — accuracy varies only slightly across λ ∈ [0.1, 1.0] (Table 13: 61.1% to 61.8% accuracy, 2.5% to 5.9% ECE)
- **Bounds**: Best performance in range λ ∈ {0.3, 0.4, 0.5} for ImageNet-C; below 0.3 or above 0.5 shows slightly higher ECE
- **Code ref**: [src/execution/fitness.py]
- **Source**: Section 4 (Implementation Details); Appendix C (Table 13)

## H03: EMA factor α = 0.1 for activation shifting direction
- **Rationale**: The exponential moving average of test activation means μ_N(t) provides a stable estimate of the OOD domain center across the online test stream. α = 0.1 gives low weight to individual batches, smoothing noise while still adapting to distribution drift. Without EMA (α = 1.0), BS=1 results in 0.1% accuracy and 0.0% ECE (collapsed predictions).
- **Sensitivity**: medium — without EMA, single-sample adaptation collapses; with EMA, performance is stable even at BS=1
- **Bounds**: α ∈ (0, 1); α = 0.1 gives consistent performance across all batch sizes; initialization: μ_N(0) = μ_N(X_1)
- **Code ref**: [src/execution/foa.py]
- **Source**: Section 3.2; Appendix C (Table 14)

## H04: Step size γ = 1.0 for activation shifting
- **Rationale**: γ = 1.0 exactly aligns the overall center of testing features with the source domain center (d_t is the direction from OOD center to source center; γ = 1 applies full correction). This is the "exact center alignment" strategy.
- **Sensitivity**: medium — values close to 1.0 are expected to work best; too small under-corrects, too large over-corrects
- **Bounds**: γ = 1.0 is the default; sensitivity is analyzed in Appendix C
- **Code ref**: [src/execution/foa.py]
- **Source**: Section 4 (Implementation Details); Section 3.2

## H05: Np = 3 prompt embeddings with uniform initialization
- **Rationale**: Np = 3 reduces optimization dimension to 3 × 768 = 2,304 (ViT-Base), making CMA-ES tractable. Uniform initialization provides a neutral starting point. Sensitivity analysis (Figure 2b) shows low variation across Np ∈ {1, ..., 10}; Np = 5 or 7 is marginally better but Np = 3 is used consistently for simplicity.
- **Sensitivity**: low — performance varies only slightly across Np ∈ {1, ..., 10}
- **Bounds**: Np = 3 is default; Np ∈ {5, 7} yields marginally better performance
- **Code ref**: [src/execution/foa.py]
- **Source**: Section 4 (Implementation Details); Section 4.3; Figure 2(b)

## H06: Batch statistics (not EMA) for fitness function discrepancy term
- **Rationale**: Using per-batch statistics μ_i(X_t), σ_i(X_t) (β=1.0 in Appendix C Table 15) rather than EMA-accumulated statistics for the fitness function Eq. 5 yields better performance. EMA in the fitness function introduces a biased objective that encourages compensation for accumulated historical errors rather than direct source alignment. β=1.0 also requires no additional hyperparameter.
- **Sensitivity**: medium — small β (e.g., 0.1) causes notable performance degradation (61.0% accuracy, 9.5% ECE vs. 61.5% accuracy, 2.5% ECE for β=1.0 on ImageNet-C)
- **Bounds**: β = 1.0 (pure batch statistics) is optimal; best ECE is achieved at β = 1.0 for both ImageNet-C and ImageNet-R
- **Code ref**: [src/execution/fitness.py]
- **Source**: Appendix C (Table 15)
