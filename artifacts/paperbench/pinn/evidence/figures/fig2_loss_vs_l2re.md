---
# Figure 2: Final Loss vs. Final L2RE Across All Runs

- **Source**: Figure 2, Section 4
- **Caption**: "We plot the final L2RE against the final loss for each combination of network width, optimization strategy, and random seed. Across all three PDEs, a lower loss generally corresponds to a lower L2RE."
- **Axis labels**: X-axis: Loss (log scale); Y-axis: L2RE (log scale)
- **Conditions**: All (width, optimizer, lr, seed) combinations; 41000 iterations; Convection β=40, Reaction ρ=5, Wave β=5

## Extracted Data Points (approximate readings from log-scale axes)

### Convection (β=40)
| Loss Range | L2RE Range | Notes |
|-----------|-----------|-------|
| ~1e-1 | ~3e-1 to 1 | High loss, high error (mostly Adam runs) |
| ~1e-3 | ~1e-1 | Moderate loss |
| ~1e-4 | ~5e-2 to 1e-1 | — |
| ~1e-5 | ~1e-2 to 5e-2 | Best Adam+L-BFGS runs |
| ~5e-6 | ~4e-3 | Best run (Adam+L-BFGS, lowest) |
| near 0 | ≈1 | Trivial solutions (constant u) |

### Reaction (ρ=5)
| Loss Range | L2RE Range | Notes |
|-----------|-----------|-------|
| ~1e-4 to 1e-2 | ~1e-1 | Moderate runs |
| ~1e-6 | ~1e-2 | Best runs |
| ~5e-9 to 1e-7 | ≈1 | Trivial solutions (u=0 or u=1) |

### Wave (β=5)
| Loss Range | L2RE Range | Notes |
|-----------|-----------|-------|
| ~1e-1 | ~3e-1 | Worst Adam runs |
| ~1e-2 | ~3e-1 | Most L-BFGS/Adam runs |
| ~1e-3 | ~5e-2 | Best Adam+L-BFGS runs |
| ~1.1e-3 | ~5.5e-2 | Best overall (Adam+L-BFGS) |

## Key Observations
1. Monotone trend: lower loss → lower L2RE across all PDEs
2. On convection: loss ~1e-3 → L2RE ~1e-1; loss ~1e-5 → L2RE ~1e-2 (100× loss reduction → 10× L2RE improvement)
3. On reaction and convection: instances where loss ≈ 0 but L2RE ≈ 1 exist (trivial constant solutions)
4. Data points colored by optimizer type (see Figure 2 legend: Adam, L-BFGS, Adam+L-BFGS(1k), Adam+L-BFGS(11k), Adam+L-BFGS(31k))
