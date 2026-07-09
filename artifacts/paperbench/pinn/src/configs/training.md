---
# Training Configuration

## Total Iterations
- **Value**: 41000 iterations per run
- **Rationale**: All three optimizer strategies (Adam, L-BFGS, Adam+L-BFGS) run for exactly 41000 iterations total for fair comparison.
- **Search range**: Not varied
- **Sensitivity**: medium
- **Source**: Section 2.2

## Number of Random Seeds
- **Value**: 5 seeds per configuration
- **Rationale**: Statistical robustness; min/median/max reported across seeds.
- **Search range**: Not varied
- **Sensitivity**: low
- **Source**: Section 2.2

## Adam Learning Rate
- **Value**: Grid searched over {1e-5, 1e-4, 1e-3, 1e-2, 1e-1}
- **Rationale**: No single lr works across all PDEs and widths; grid search finds optimal per (PDE, width) combination.
- **Search range**: {1e-5, 1e-4, 1e-3, 1e-2, 1e-1}
- **Sensitivity**: high
- **Source**: Section 2.2

## Adam+L-BFGS Switch Points
- **Value**: {1000, 11000, 31000} iterations (Adam+L-BFGS (1k), (11k), (31k))
- **Rationale**: Three switch points evaluated; allows Adam varying amounts of time to escape saddle points before L-BFGS takes over.
- **Search range**: {1k, 11k, 31k}
- **Sensitivity**: medium
- **Source**: Section 2.2

## L-BFGS Learning Rate
- **Value**: 1.0 (default)
- **Rationale**: Standard L-BFGS learning rate; line search controls actual step size.
- **Search range**: Not varied
- **Sensitivity**: low
- **Source**: Section 2.2

## L-BFGS Memory Size
- **Value**: m = 100
- **Rationale**: Larger memory improves Hessian approximation quality; default (m=20) is insufficient for well-conditioned updates on ill-conditioned PINN loss.
- **Search range**: Not varied
- **Sensitivity**: medium
- **Source**: Section 2.2

## L-BFGS Line Search
- **Value**: Strong Wolfe conditions
- **Rationale**: Required for L-BFGS stability; however, strong Wolfe can fail to find a valid step (leading to early termination, as observed in Figure 9).
- **Search range**: Not varied (strong Wolfe is standard for L-BFGS)
- **Sensitivity**: high (structural limitation)
- **Source**: Section 2.2, Section 7.1

## Residual Points (n_res)
- **Value**: 10000, randomly sampled from a 255×100 grid on the interior domain
- **Rationale**: Sufficient coverage; fixed throughout training for deterministic loss (required for L-BFGS and Newton methods).
- **Search range**: Not varied during training (varied only in Appendix F.5 for condition number scaling experiment)
- **Sensitivity**: medium
- **Source**: Section 2.2

## Initial Condition Points (n_ic)
- **Value**: 257 equally spaced points at t=0
- **Rationale**: Matches grid spacing; covers the full spatial domain.
- **Search range**: Not varied
- **Sensitivity**: low
- **Source**: Section 2.2

## Boundary Condition Points (n_bc)
- **Value**: 101 equally spaced points per boundary
- **Rationale**: Covers the full temporal domain at each spatial boundary.
- **Search range**: Not varied
- **Sensitivity**: low
- **Source**: Section 2.2

## NNCG Parameters
- **Value**: η=1, K=2000, s=60, F=20, ε=1e-16, M=1000, α=0.1, β=0.5, μ ∈ {1e-5, 1e-4, 1e-3, 1e-2, 1e-1} (μ tuned)
- **Rationale**: η=1 (initial max step); K=2000 additional steps; s=60 sketch size for Nyström; F=20 preconditioner update frequency; ε=1e-16 CG tolerance; M=1000 max CG iterations; α=0.1, β=0.5 for Armijo; μ∈{1e-2, 1e-1} found to work best in practice.
- **Search range**: μ ∈ {1e-5, 1e-4, 1e-3, 1e-2, 1e-1}
- **Sensitivity**: high (μ); medium (s, F)
- **Source**: Appendix E.2
