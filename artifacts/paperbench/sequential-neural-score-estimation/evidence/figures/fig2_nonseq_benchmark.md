# Figure 2: Non-Sequential Benchmark Results
- **Source**: Figure 2, Section 5.2
- **Caption**: "Results on eight benchmark tasks (non-sequential methods)."
- **Experimental conditions**: C2ST score (lower is better, 0.5=perfect) at simulation budgets of 10k and 100k. Methods: NPSE-VE, NPSE-VP, NPE. C2ST computed using 10000 samples from true and approximate posterior each.
- **Axis**: x-axis = Simulation Budget (10k, 100k); y-axis = C2ST ∈ [0.5, 1.0]

Note: Exact numerical values are read from bar plots; ≈ indicates approximate visual readings.

| Task | Method | Budget=10k C2ST | Budget=100k C2ST |
|------|--------|-----------------|------------------|
| Lotka Volterra | NPSE-VE | ≈0.75 | ≈0.65 |
| Lotka Volterra | NPSE-VP | ≈0.70 | ≈0.62 |
| Lotka Volterra | NPE | ≈0.75 | ≈0.72 |
| SLCP | NPSE-VE | ≈0.65 | ≈0.55 |
| SLCP | NPSE-VP | ≈0.68 | ≈0.57 |
| SLCP | NPE | ≈0.80 | ≈0.75 |
| Gaussian Linear Uniform | NPSE-VE | ≈0.72 | ≈0.65 |
| Gaussian Linear Uniform | NPSE-VP | ≈0.70 | ≈0.63 |
| Gaussian Linear Uniform | NPE | ≈0.60 | ≈0.52 |
| Bernoulli GLM | NPSE-VE | ≈0.60 | ≈0.52 |
| Bernoulli GLM | NPSE-VP | ≈0.62 | ≈0.53 |
| Bernoulli GLM | NPE | ≈0.60 | ≈0.52 |
| SIR | NPSE-VE | ≈0.55 | ≈0.52 |
| SIR | NPSE-VP | ≈0.70 | ≈0.65 |
| SIR | NPE | ≈0.55 | ≈0.51 |
| Two Moons | NPSE-VE | ≈0.58 | ≈0.53 |
| Two Moons | NPSE-VP | ≈0.72 | ≈0.70 |
| Two Moons | NPE | ≈0.55 | ≈0.52 |
| Gaussian Mixture | NPSE-VE | ≈0.55 | ≈0.52 |
| Gaussian Mixture | NPSE-VP | ≈0.75 | ≈0.72 |
| Gaussian Mixture | NPE | ≈0.55 | ≈0.52 |
| Gaussian Linear | NPSE-VE | ≈0.55 | ≈0.51 |
| Gaussian Linear | NPSE-VP | ≈0.55 | ≈0.51 |
| Gaussian Linear | NPE | ≈0.54 | ≈0.50 |

**Key findings (from §5.2 text)**:
- On SLCP and Lotka Volterra, NPSE variants outperform NPE
- On Gaussian Linear Uniform, NPE achieves lower C2ST than both NPSE variants
- On SIR and Two Moons, NPE achieves lower C2ST than NPSE-VP (but not NPSE-VE)
- On Gaussian Linear and Bernoulli GLM, all three methods achieve comparable results
- VE SDE recommended for 2D tasks; VP SDE recommended for higher-D tasks
