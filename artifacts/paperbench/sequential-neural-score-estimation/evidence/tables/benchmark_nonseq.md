# Non-Sequential Benchmark Results (Figure 2)
- **Source**: Figure 2, Section 5.2
- **Caption**: "Results on eight benchmark tasks (non-sequential methods)."
- **Conditions**: Non-sequential methods; R=1 round; observation #1 per task; C2ST evaluated on 10000 samples (lower is better, 0.5 = perfect)
- **Note**: Values read from Figure 2 bar charts (approximate ≈ due to figure reading)

| Task | Budget | NPSE-VE C2ST | NPSE-VP C2ST | NPE C2ST |
|------|--------|-------------|-------------|---------|
| Lotka Volterra | 10k | ≈0.68 | ≈0.72 | ≈0.72 |
| Lotka Volterra | 100k | ≈0.60 | ≈0.62 | ≈0.68 |
| SLCP | 10k | ≈0.68 | ≈0.70 | ≈0.82 |
| SLCP | 100k | ≈0.56 | ≈0.58 | ≈0.73 |
| Gaussian Linear Uniform | 10k | ≈0.76 | ≈0.75 | ≈0.62 |
| Gaussian Linear Uniform | 100k | ≈0.65 | ≈0.65 | ≈0.52 |
| Bernoulli GLM | 10k | ≈0.72 | ≈0.68 | ≈0.71 |
| Bernoulli GLM | 100k | ≈0.55 | ≈0.54 | ≈0.53 |
| SIR | 10k | ≈0.62 | ≈0.72 | ≈0.58 |
| SIR | 100k | ≈0.52 | ≈0.62 | ≈0.51 |
| Two Moons | 10k | ≈0.64 | ≈0.72 | ≈0.58 |
| Two Moons | 100k | ≈0.52 | ≈0.62 | ≈0.51 |
| Gaussian Mixture | 10k | ≈0.58 | ≈0.75 | ≈0.57 |
| Gaussian Mixture | 100k | ≈0.52 | ≈0.68 | ≈0.51 |
| Gaussian Linear | 10k | ≈0.56 | ≈0.58 | ≈0.55 |
| Gaussian Linear | 100k | ≈0.51 | ≈0.52 | ≈0.51 |

**Key findings from paper text (§5.2)**:
- SLCP and Lotka Volterra: NPSE-VE and NPSE-VP both outperform NPE
- Gaussian Linear Uniform: NPE achieves lower C2ST than both NPSE variants
- SIR, Two Moons, Gaussian Mixture: NPE achieves lower C2ST than NPSE-VP (but NPSE-VE may be comparable)
- Gaussian Linear, Bernoulli GLM: all methods roughly equivalent
- Best SDE choice varies by task: VE generally better for low-D, VP generally better for high-D
