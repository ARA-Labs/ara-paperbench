# Figure 3: Sequential Benchmark Results
- **Source**: Figure 3, Section 5.2
- **Caption**: "Results on eight benchmark tasks (sequential methods)."
- **Experimental conditions**: C2ST score (lower is better) at simulation budgets of 10k and 100k. Methods: TSNPSE-VE, TSNPSE-VP, SNPE (=SNPE-C), TSNPE. R=10 rounds; equal distribution of simulations per round.

Note: Values read from bar plots; ≈ indicates approximate visual readings.

| Task | Method | Budget=10k C2ST | Budget=100k C2ST |
|------|--------|-----------------|------------------|
| Lotka Volterra | TSNPSE-VE | ≈0.63 | ≈0.58 |
| Lotka Volterra | TSNPSE-VP | ≈0.60 | ≈0.55 |
| Lotka Volterra | SNPE | ≈0.72 | ≈0.70 |
| Lotka Volterra | TSNPE | ≈0.70 | ≈0.68 |
| SLCP | TSNPSE-VE | ≈0.58 | ≈0.53 |
| SLCP | TSNPSE-VP | ≈0.60 | ≈0.55 |
| SLCP | SNPE | ≈0.72 | ≈0.68 |
| SLCP | TSNPE | ≈0.70 | ≈0.65 |
| Gaussian Linear Uniform | TSNPSE-VE | ≈0.65 | ≈0.60 |
| Gaussian Linear Uniform | TSNPSE-VP | ≈0.62 | ≈0.58 |
| Gaussian Linear Uniform | SNPE | ≈0.60 | ≈0.55 |
| Gaussian Linear Uniform | TSNPE | ≈0.63 | ≈0.58 |
| Bernoulli GLM | TSNPSE-VE | ≈0.55 | ≈0.52 |
| Bernoulli GLM | TSNPSE-VP | ≈0.57 | ≈0.53 |
| Bernoulli GLM | SNPE | ≈0.58 | ≈0.53 |
| Bernoulli GLM | TSNPE | ≈0.60 | ≈0.55 |
| SIR | TSNPSE-VE | ≈0.52 | ≈0.51 |
| SIR | TSNPSE-VP | ≈0.60 | ≈0.56 |
| SIR | SNPE | ≈0.55 | ≈0.52 |
| SIR | TSNPE | ≈0.60 | ≈0.55 |
| Two Moons | TSNPSE-VE | ≈0.54 | ≈0.51 |
| Two Moons | TSNPSE-VP | ≈0.65 | ≈0.60 |
| Two Moons | SNPE | ≈0.55 | ≈0.52 |
| Two Moons | TSNPE | ≈0.62 | ≈0.58 |
| Gaussian Mixture | TSNPSE-VE | ≈0.54 | ≈0.51 |
| Gaussian Mixture | TSNPSE-VP | ≈0.70 | ≈0.65 |
| Gaussian Mixture | SNPE | ≈0.55 | ≈0.52 |
| Gaussian Mixture | TSNPE | ≈0.62 | ≈0.58 |
| Gaussian Linear | TSNPSE-VE | ≈0.52 | ≈0.51 |
| Gaussian Linear | TSNPSE-VP | ≈0.52 | ≈0.50 |
| Gaussian Linear | SNPE | ≈0.53 | ≈0.51 |
| Gaussian Linear | TSNPE | ≈0.55 | ≈0.52 |

**Key findings (from §5.2 text)**:
- TSNPSE methods outperform SNPE and TSNPE on SLCP and Lotka Volterra (most challenging tasks)
- On Gaussian Linear Uniform, Bernoulli GLM, SIR, Two Moons, Gaussian Mixture, Gaussian Linear: results are more mixed
- Best-performing SDE variant (VE vs. VP) fluctuates by task; VE SDE recommended for low-D, VP SDE for high-D
