# NPSE vs NLSE Comparison (Figure 5)
- **Source**: Figure 5, Appendix B.3
- **Caption**: "Comparison between NPSE and NLSE on four benchmark tasks."
- **Conditions**: Non-sequential; budgets 1k, 10k, 100k; NPSE-VE and NPSE-VP use VE and VP SDEs respectively; NLSE-VE uses VE SDE with analytical perturbed prior score. C2ST (lower is better).

| Task | Budget | NPSE-VE | NPSE-VP | NLSE-VE |
|------|--------|---------|---------|---------|
| Two Moons | 1k | ≈0.82 | ≈0.85 | ≈0.83 |
| Two Moons | 10k | ≈0.64 | ≈0.72 | ≈0.66 |
| Two Moons | 100k | ≈0.52 | ≈0.62 | ≈0.53 |
| SIR | 1k | ≈0.85 | ≈0.90 | ≈0.86 |
| SIR | 10k | ≈0.62 | ≈0.72 | ≈0.63 |
| SIR | 100k | ≈0.52 | ≈0.62 | ≈0.52 |
| SLCP | 1k | ≈0.90 | ≈0.92 | ≈0.91 |
| SLCP | 10k | ≈0.68 | ≈0.70 | ≈0.69 |
| SLCP | 100k | ≈0.56 | ≈0.58 | ≈0.57 |
| Lotka Volterra | 1k | ≈0.90 | ≈0.90 | ≈0.91 |
| Lotka Volterra | 10k | ≈0.68 | ≈0.72 | ≈0.70 |
| Lotka Volterra | 100k | ≈0.60 | ≈0.62 | ≈0.61 |

**Note**: All values read from Figure 5 (approximate). Paper conclusion (Appendix B.3): "in cases where it was possible to compute the perturbed prior analytically, we found little empirical difference between NPSE and NLSE." NLSE is worse when the prior score must be approximated by an additional network.
