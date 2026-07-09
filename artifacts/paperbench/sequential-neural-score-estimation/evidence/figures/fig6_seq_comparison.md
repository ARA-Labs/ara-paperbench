# Figure 6: Sequential Variant Comparison (TSNPSE vs SNPSE-A/B)

- **Source**: Figure 6, Appendix C.5
- **Caption**: "Comparison between SNPSE-A, SNPSE-B, and TSNPSE on two benchmark tasks."
- **Experimental conditions**:
  - Methods: TSNPSE (VE or VP — not specified), SNPSE-A, SNPSE-B
  - SNPSE-C omitted: "failed to provide meaningful results (e.g., C2ST ≈ 1)"
  - Tasks: SLCP and Gaussian Linear Uniform (GLU)
  - Metric: C2ST score (y-axis), simulation budget (x-axis)

## Qualitative Data Points (Read from Plot)

All values are approximate (≈).

### SLCP Task
| Budget | TSNPSE | SNPSE-A | SNPSE-B |
|--------|--------|---------|---------|
| 10k | ≈0.67 | ≈0.82 | ≈0.85 |
| 100k | ≈0.55 | ≈0.78 | ≈0.80 |

### Gaussian Linear Uniform (GLU) Task
| Budget | TSNPSE | SNPSE-A | SNPSE-B |
|--------|--------|---------|---------|
| 10k | ≈0.63 | ≈0.78 | ≈0.82 |
| 100k | ≈0.56 | ≈0.70 | ≈0.75 |

### SNPSE-C (Not Shown)
- C2ST ≈ 1.0 on all tested tasks (stated explicitly in Appendix C.5).

## Key Takeaways
- TSNPSE significantly outperforms both SNPSE-A and SNPSE-B on both tasks.
- SNPSE-A is better than SNPSE-B but both are substantially worse than TSNPSE.
- SNPSE-C completely fails (C2ST ≈ 1.0) due to proposal prior score approximation errors.
- Result replicated across other tasks (not shown); TSNPSE is the recommended sequential method.
