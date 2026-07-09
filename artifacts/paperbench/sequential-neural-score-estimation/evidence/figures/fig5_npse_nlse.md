# Figure 5: NPSE vs NLSE Comparison
- **Source**: Figure 5, Appendix B.3
- **Caption**: "Comparison between NPSE and NLSE on four benchmark tasks."
- **Axis labels**: X-axis = Simulation Budget (1k, 10k, 100k); Y-axis = C2ST (lower is better)
- **Methods**: NPSE-VE (blue), NPSE-VP (orange), NLSE-VE (green)
- **Note**: NLSE uses VE SDE with analytically computed perturbed prior score (Appendix B.2.1)

## Data Points (read from Figure 5, ≈ approximate)

### Two Moons
| Budget | NPSE-VE | NPSE-VP | NLSE-VE |
|--------|---------|---------|---------|
| 1k | ≈0.82 | ≈0.85 | ≈0.83 |
| 10k | ≈0.64 | ≈0.72 | ≈0.66 |
| 100k | ≈0.52 | ≈0.62 | ≈0.53 |

### SIR
| Budget | NPSE-VE | NPSE-VP | NLSE-VE |
|--------|---------|---------|---------|
| 1k | ≈0.85 | ≈0.90 | ≈0.86 |
| 10k | ≈0.62 | ≈0.72 | ≈0.63 |
| 100k | ≈0.52 | ≈0.62 | ≈0.52 |

### SLCP
| Budget | NPSE-VE | NPSE-VP | NLSE-VE |
|--------|---------|---------|---------|
| 1k | ≈0.90 | ≈0.92 | ≈0.91 |
| 10k | ≈0.68 | ≈0.70 | ≈0.69 |
| 100k | ≈0.56 | ≈0.58 | ≈0.57 |

### Lotka Volterra
| Budget | NPSE-VE | NPSE-VP | NLSE-VE |
|--------|---------|---------|---------|
| 1k | ≈0.90 | ≈0.90 | ≈0.91 |
| 10k | ≈0.68 | ≈0.72 | ≈0.70 |
| 100k | ≈0.60 | ≈0.62 | ≈0.61 |

## Key Observations
- NPSE-VE and NLSE-VE achieve nearly identical C2ST across all four tasks and all budgets
- NPSE-VP is consistently worse than NPSE-VE and NLSE-VE on these tasks
- Validates that NPSE and NLSE are equivalent when the prior score is analytically available
- NLSE degrades when the prior score must be approximated with an additional network (not shown here)
