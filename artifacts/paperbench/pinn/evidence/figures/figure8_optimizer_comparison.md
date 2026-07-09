# Figure 8: Optimizer Comparison Across Network Widths

**Source**: Figure 8, Appendix D
**Caption**: Performance of Adam, L-BFGS, and Adam+L-BFGS after tuning. Min, median, and max loss (L2RE) across seeds for best learning rate per width. Smallest min loss and L2RE are always attained by one of the Adam+L-BFGS strategies.

## Key Observations

### Best Optimizer per PDE (minimum loss across widths)

| PDE | Best Optimizer | Relative to Adam |
|-----|---------------|-----------------|
| Convection (β=40) | Adam+L-BFGS (any variant) | Always better |
| Wave (β=5) | Adam+L-BFGS (any variant) | Always better; largest gap |
| Reaction (ρ=5) | Usually Adam+L-BFGS | Adam better at width=100 (loss) and width=200 (L2RE) |

### Performance by Width Summary (from Figure 8, qualitative)

| Width | Convection: best optimizer | Wave: best optimizer | Reaction: best optimizer |
|-------|---------------------------|---------------------|--------------------------|
| 50 | Adam+L-BFGS | Adam+L-BFGS | Adam+L-BFGS |
| 100 | Adam+L-BFGS | Adam+L-BFGS | Adam (for loss) |
| 200 | Adam+L-BFGS | Adam+L-BFGS | Adam (for L2RE) |
| 400 | Adam+L-BFGS | Adam+L-BFGS | Adam+L-BFGS |

### Exception: Reaction Problem (ρ=5)
- Adam outperforms Adam+L-BFGS on loss at width=100
- Adam outperforms Adam+L-BFGS on L2RE at width=200
- Explained by lower condition number of reaction (~10^3 vs 10^4-10^5 for others)

## Data Format
- Each bar: median across 5 seeds for best learning rate at that width
- Error bars: min (bottom) and max (top) across 5 seeds
- X-axis: network width {50, 100, 200, 400}
- Y-axis: loss (top row) or L2RE (bottom row), log scale
