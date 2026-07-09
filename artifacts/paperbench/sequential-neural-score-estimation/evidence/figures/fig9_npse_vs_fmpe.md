# Figure 9: NPSE vs FMPE Comparison

- **Source**: Figure 9, Appendix F
- **Caption**: "Comparison between NPSE and FMPE on eight benchmark tasks."
- **Experimental conditions**:
  - Methods: NPSE-VE, NPSE-VP, FMPE (Dax et al., 2023)
  - FMPE results taken directly from Dax et al. (2023); per-task hyperparameter tuning (5 hyperparameters swept per experiment).
  - NPSE uses single fixed hyperparameter set across all experiments (no per-task tuning).
  - Metric: C2ST score (y-axis), simulation budgets 10k and 100k (x-axis)
  - 8 benchmark tasks

## Qualitative Data Points (Read from Plot)

All values are approximate (≈).

| Task | Budget | NPSE-VE | NPSE-VP | FMPE |
|------|--------|---------|---------|------|
| Lotka Volterra | 10k | ≈0.75 | ≈0.75 | ≈0.73 |
| Lotka Volterra | 100k | ≈0.65 | ≈0.65 | ≈0.62 |
| SLCP | 10k | ≈0.72 | ≈0.72 | ≈0.68 |
| SLCP | 100k | ≈0.58 | ≈0.58 | ≈0.56 |
| Gaussian Linear Uniform | 10k | ≈0.70 | ≈0.70 | ≈0.60 |
| Gaussian Linear Uniform | 100k | ≈0.62 | ≈0.62 | ≈0.53 |
| Bernoulli GLM | 10k | ≈0.65 | ≈0.65 | ≈0.62 |
| Bernoulli GLM | 100k | ≈0.58 | ≈0.58 | ≈0.56 |
| SIR | 10k | ≈0.62 | ≈0.73 | ≈0.57 |
| SIR | 100k | ≈0.55 | ≈0.65 | ≈0.52 |
| Two Moons | 10k | ≈0.65 | ≈0.78 | ≈0.57 |
| Two Moons | 100k | ≈0.55 | ≈0.72 | ≈0.52 |
| Gaussian Mixture | 10k | ≈0.62 | ≈0.78 | ≈0.58 |
| Gaussian Mixture | 100k | ≈0.53 | ≈0.70 | ≈0.52 |
| Gaussian Linear | 10k | ≈0.60 | ≈0.60 | ≈0.55 |
| Gaussian Linear | 100k | ≈0.53 | ≈0.53 | ≈0.51 |

## Key Takeaways
- FMPE (with per-task hyperparameter tuning) achieves lower C2ST on most lower-dimensional tasks.
- NPSE (without any per-task tuning) is competitive with FMPE, particularly on harder tasks (SLCP, Lotka Volterra).
- The comparison is not fully fair since FMPE benefits from per-experiment hyperparameter sweeps while NPSE uses a single fixed configuration.
- Further tuning of NPSE hyperparameters would likely narrow or close the gap with FMPE.
