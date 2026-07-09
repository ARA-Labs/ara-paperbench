# Sequential Benchmark Results (Figure 3)
- **Source**: Figure 3, Section 5.2
- **Caption**: "Results on eight benchmark tasks (sequential methods)."
- **Conditions**: Sequential methods; R=10 rounds; budget equally divided; observation #1 per task; C2ST on 10000 samples (lower is better)
- **Note**: Values read from Figure 3 bar charts (approximate ≈ due to figure reading). SNPE and TSNPE results from sbibm.

| Task | Budget | TSNPSE-VE C2ST | TSNPSE-VP C2ST | SNPE-C C2ST | TSNPE C2ST |
|------|--------|---------------|---------------|-----------|----------|
| Lotka Volterra | 10k | ≈0.62 | ≈0.65 | ≈0.78 | ≈0.72 |
| Lotka Volterra | 100k | ≈0.55 | ≈0.57 | ≈0.70 | ≈0.65 |
| SLCP | 10k | ≈0.60 | ≈0.62 | ≈0.74 | ≈0.68 |
| SLCP | 100k | ≈0.52 | ≈0.54 | ≈0.65 | ≈0.60 |
| Gaussian Linear Uniform | 10k | ≈0.72 | ≈0.68 | ≈0.60 | ≈0.65 |
| Gaussian Linear Uniform | 100k | ≈0.60 | ≈0.57 | ≈0.52 | ≈0.62 |
| Bernoulli GLM | 10k | ≈0.64 | ≈0.60 | ≈0.68 | ≈0.65 |
| Bernoulli GLM | 100k | ≈0.52 | ≈0.51 | ≈0.55 | ≈0.54 |
| SIR | 10k | ≈0.64 | ≈0.70 | ≈0.56 | ≈0.58 |
| SIR | 100k | ≈0.51 | ≈0.60 | ≈0.51 | ≈0.52 |
| Two Moons | 10k | ≈0.68 | ≈0.72 | ≈0.56 | ≈0.60 |
| Two Moons | 100k | ≈0.52 | ≈0.60 | ≈0.51 | ≈0.52 |
| Gaussian Mixture | 10k | ≈0.60 | ≈0.72 | ≈0.55 | ≈0.58 |
| Gaussian Mixture | 100k | ≈0.51 | ≈0.65 | ≈0.51 | ≈0.52 |
| Gaussian Linear | 10k | ≈0.55 | ≈0.57 | ≈0.55 | ≈0.56 |
| Gaussian Linear | 100k | ≈0.51 | ≈0.51 | ≈0.51 | ≈0.51 |

**Key findings from paper text (§5.2)**:
- SLCP, Lotka Volterra, Bernoulli GLM: TSNPSE-VE and TSNPSE-VP outperform both SNPE-C and TSNPE
- Gaussian Linear: TSNPSE comparable to TSNPE; all roughly equivalent
- Gaussian Linear Uniform, SIR, Two Moons, Gaussian Mixture: TSNPSE-VE and TSNPSE-VP mixed vs SNPE-C and TSNPE (task-dependent)
