# Figure 5.1: Gaussian Targets of Increasing Dimension (Forward KL)
- **Source**: Figure 5.1, Section 5.1
- **Caption**: "Gaussian targets of increasing dimension. Solid curves indicate the mean over 10 runs (transparent curves). ADVI, Score, Fisher, and GSM use a batch size of B=2. The batch size for BaM is given in the legend."

## Experimental Conditions
- Target: Random Gaussian N(μ*, Σ*) with Σ* = AA^T
- Dimensions: D = 4, 16, 64, 256
- Metric: Forward KL divergence KL(p; q_t) vs. number of gradient evaluations
- Methods compared: BaM (large B), BaM-2, GSM, ADVI-Score, ADVI-Fisher, ADVI-ELBO

## Configurations per Dimension

| D | BaM large batch | BaM small batch | Other methods batch |
|---|----------------|----------------|---------------------|
| 4 | B=5 (BaM-5) | B=2 (BaM-2) | B=2 |
| 16 | B=15 (BaM-15) | B=2 (BaM-2) | B=2 |
| 64 | B=40 (BaM-40) | B=2 (BaM-2) | B=2 |
| 256 | B=150 (BaM-150) | B=2 (BaM-2) | B=2 |

## Qualitative Findings (from paper text)
- BaM converges orders of magnitude faster than ADVI (in gradient evaluations)
- GSM is competitive with BaM at B=2 but BaM at larger B converges more quickly
- Gradient-based methods (ADVI, Score, Fisher) have similar performance to each other
- Score divergence is typically more sensitive to learning rate than ELBO
- BaM at larger batch sizes converges faster; GSM shows marginal gain beyond B=2 for Gaussian targets
- Wallclock timings: all methods similar for D≤64; low-rank BaM similar for larger D (see Fig E.1)

Note: Exact numerical KL values at each iteration are not reported in paper; figure shows qualitative convergence curves over 10 runs. Trend: BaM large-B converges to ~0 forward KL within ~100-1000 gradient evaluations; ADVI requires ~10× to 100× more.
