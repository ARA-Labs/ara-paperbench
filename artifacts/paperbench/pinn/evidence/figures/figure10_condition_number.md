# Figure 10: Condition Number Growth with Residual Points

**Source**: Figure 10, Appendix F.5
**Caption**: Estimated condition number after 41000 iterations of Adam+L-BFGS with different number of residual points from 255×100 grid. Here λ_i denotes the i-th largest eigenvalue of the Hessian. The model has 2 layers and hidden layer width 32. The plot shows κ_L grows polynomially in the number of residual points.

## Setup
- PDE: Convection (β=1)
- Model: 2 hidden layers, width=32
- Condition number proxy: λ_1(H_L) / λ_129(H_L) (computationally tractable lower bound)
- X-axis: log₂(n_res), swept over subset of {n_res: sampled from 255×100 grid}
- Y-axis: ratio λ_1/λ_129

## Extracted Data Points (approximate, from Figure 10)

| log₂(n_res) | n_res (approx) | λ₁/λ₁₂₉ (approx, log scale) |
|-------------|----------------|------------------------------|
| 7 | 128 | low |
| 8 | 256 | moderate |
| 9 | 512 | higher |
| 10 | 1024 | higher still |
| 11 | 2048 | high |
| 12 | 4096 | highest |

(Exact values not tabulated in paper; trend is polynomial growth in n_res)

## Key Observation
- The ratio λ_1/λ_129 grows polynomially (approximately linearly in log-log plot) with n_res
- This empirically confirms Theorem 8.4: κ_L(S) = Ω(n_res^α)
- Supports the claim that increasing n_res makes the problem harder for first-order methods

## Significance
- Demonstrates that the ill-conditioning problem is fundamental and worsens with more training points
- Motivates the use of second-order methods (L-BFGS, NNCG) which are relatively insensitive to condition number
