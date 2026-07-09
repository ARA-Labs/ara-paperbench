# Figure 5: NPSE vs NLSE Comparison

- **Source**: Figure 5, Appendix B.3
- **Caption**: "Comparison between NPSE and NLSE on four benchmark tasks."
- **Experimental conditions**:
  - Methods: NPSE-VE, NPSE-VP, NLSE-VE (Neural Likelihood Score Estimation with VE SDE)
  - NLSE uses analytically computable perturbed prior (VE SDE with uniform/Gaussian priors)
  - Metric: C2ST score (y-axis), simulation budgets (x-axis, 10k and 100k)
  - 4 benchmark tasks (subset of the 8; exact tasks not specified in paper text but inferred to be benchmark tasks from Appendix E.1)

## Qualitative Data Points (Read from Plot)

All values are approximate (≈).

| Task | Budget | NPSE-VE | NPSE-VP | NLSE-VE |
|------|--------|---------|---------|---------|
| Task A | 10k | ≈0.65 | ≈0.65 | ≈0.65 |
| Task A | 100k | ≈0.55 | ≈0.55 | ≈0.55 |
| Task B | 10k | ≈0.70 | ≈0.73 | ≈0.70 |
| Task B | 100k | ≈0.60 | ≈0.63 | ≈0.60 |
| Task C | 10k | ≈0.63 | ≈0.78 | ≈0.63 |
| Task C | 100k | ≈0.54 | ≈0.72 | ≈0.54 |
| Task D | 10k | ≈0.65 | ≈0.65 | ≈0.65 |
| Task D | 100k | ≈0.57 | ≈0.57 | ≈0.57 |

## Key Takeaways
- When the perturbed prior is analytically tractable (VE SDE case), NPSE-VE and NLSE-VE achieve roughly equivalent C2ST.
- This validates both approaches as equivalent in the analytically tractable prior case.
- When the prior is not analytically tractable (requiring a second score network), NPSE significantly outperforms NLSE (stated in text of Appendix B.3; not shown in Figure 5).
