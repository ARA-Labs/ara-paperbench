# Figure 2: Final Loss vs. L2RE Across All Optimizer/Width/Seed Combinations

- **Source**: Figure 2, Section 4
- **Caption**: "We plot the final L2RE against the final loss for each combination of network width, optimization strategy, and random seed. Across all three PDEs, a lower loss generally corresponds to a lower L2RE."
- **Axis labels**: x-axis = Final Loss (log scale); y-axis = Final L2RE (log scale)
- **Series**: Adam, L-BFGS, Adam+L-BFGS(1k), Adam+L-BFGS(11k), Adam+L-BFGS(31k)
- **Experimental conditions**: All combinations of 4 widths × 5 learning rates (for Adam/Adam+L-BFGS) or 1 setting (L-BFGS) × 5 seeds × 3 switch points; all 3 PDEs shown

## Key Data Points (Approximate from Figure)

### Convection (β=40)
| Loss Range | L2RE Range | Notes |
|-----------|-----------|-------|
| ≈1e-4 to 1e-5 | ≈1e-1 to 5e-2 | Adam cluster |
| ≈1e-5 to 5e-6 | ≈1e-2 to 5e-3 | L-BFGS + Adam+L-BFGS cluster |
| ≈1e-3 to 1e-2 | ≈1e-1 | Some L-BFGS runs (worse) |
| ≈1e-7 to 1e-6 | ≈1e-3 | Best Adam+L-BFGS runs |

### Reaction (ρ=5)
| Loss Range | L2RE Range | Notes |
|-----------|-----------|-------|
| ≈1e-6 to 1e-4 | ≈1e-1 to 1e-2 | Scattered; some points with loss≈0, L2RE≈1 (trivial solutions) |
| ≈1e-6 | ≈2e-2 | Best Adam and Adam+L-BFGS |

### Wave (β=5)
| Loss Range | L2RE Range | Notes |
|-----------|-----------|-------|
| ≈1e-2 to 1e-3 | ≈3e-1 | Adam and L-BFGS cluster |
| ≈1e-3 | ≈5e-2 | Best Adam+L-BFGS |
| ≈1e-1 | ≈1e-1 | Worst runs |

**Key observations**:
- Strong positive correlation (lower loss → lower L2RE) in log-log space across all PDEs
- Some reaction runs at loss≈0 have L2RE≈1 (trivial constant solutions satisfying residual but not BC)
- Adam+L-BFGS variants systematically in the lower-left (better) region
