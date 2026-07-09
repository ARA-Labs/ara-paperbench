# Benchmark Results: Sequential Methods (Figure 3)
- **Source**: Figure 3, Section 5.2
- **Caption**: "Results on eight benchmark tasks (sequential methods)." C2ST scores for TSNPSE-VE, TSNPSE-VP, SNPE-C, and TSNPE at simulation budgets 10k and 100k.

| Task | Method | Budget 10k C2ST (≈) | Budget 100k C2ST (≈) |
|------|--------|----------------------|----------------------|
| Lotka Volterra | TSNPSE-VE | ≈0.72 | ≈0.58 |
| Lotka Volterra | TSNPSE-VP | ≈0.68 | ≈0.57 |
| Lotka Volterra | SNPE-C | ≈0.75 | ≈0.65 |
| Lotka Volterra | TSNPE | ≈0.73 | ≈0.63 |
| SLCP | TSNPSE-VE | ≈0.65 | ≈0.56 |
| SLCP | TSNPSE-VP | ≈0.63 | ≈0.56 |
| SLCP | SNPE-C | ≈0.75 | ≈0.68 |
| SLCP | TSNPE | ≈0.70 | ≈0.63 |
| Gaussian Linear Uniform | TSNPSE-VE | ≈0.72 | ≈0.60 |
| Gaussian Linear Uniform | TSNPSE-VP | ≈0.72 | ≈0.60 |
| Gaussian Linear Uniform | SNPE-C | ≈0.62 | ≈0.54 |
| Gaussian Linear Uniform | TSNPE | ≈0.60 | ≈0.53 |
| Bernoulli GLM | TSNPSE-VE | ≈0.63 | ≈0.57 |
| Bernoulli GLM | TSNPSE-VP | ≈0.63 | ≈0.57 |
| Bernoulli GLM | SNPE-C | ≈0.65 | ≈0.58 |
| Bernoulli GLM | TSNPE | ≈0.63 | ≈0.57 |
| SIR | TSNPSE-VE | ≈0.60 | ≈0.53 |
| SIR | TSNPSE-VP | ≈0.70 | ≈0.58 |
| SIR | SNPE-C | ≈0.58 | ≈0.52 |
| SIR | TSNPE | ≈0.58 | ≈0.52 |
| Two Moons | TSNPSE-VE | ≈0.57 | ≈0.52 |
| Two Moons | TSNPSE-VP | ≈0.72 | ≈0.60 |
| Two Moons | SNPE-C | ≈0.56 | ≈0.51 |
| Two Moons | TSNPE | ≈0.56 | ≈0.51 |
| Gaussian Mixture | TSNPSE-VE | ≈0.57 | ≈0.52 |
| Gaussian Mixture | TSNPSE-VP | ≈0.72 | ≈0.60 |
| Gaussian Mixture | SNPE-C | ≈0.57 | ≈0.51 |
| Gaussian Mixture | TSNPE | ≈0.57 | ≈0.51 |
| Gaussian Linear | TSNPSE-VE | ≈0.53 | ≈0.51 |
| Gaussian Linear | TSNPSE-VP | ≈0.53 | ≈0.51 |
| Gaussian Linear | SNPE-C | ≈0.54 | ≈0.52 |
| Gaussian Linear | TSNPE | ≈0.53 | ≈0.51 |

**Key findings (from paper text, §5.2)**:
- TSNPSE outperforms SNPE-C and TSNPE on SLCP and Lotka-Volterra
- Performance is mixed on simpler tasks; best method varies by task
- TSNPSE results improve with sequential rounds vs non-sequential NPSE
