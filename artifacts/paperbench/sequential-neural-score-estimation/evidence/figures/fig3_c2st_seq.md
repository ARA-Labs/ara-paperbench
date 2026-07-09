# Figure 3: C2ST Scores — Sequential Methods
- **Source**: Figure 3, Section 5.2
- **Caption**: "Results on eight benchmark tasks (sequential methods)."
- **Axes**: X = Simulation Budget (10k, 100k); Y = C2ST (range 0.5–1.0+, lower is better)
- **Methods**: TSNPSE-VE (blue), TSNPSE-VP (orange), SNPE-C (green), TSNPE (red)

## Summary (read from figure, sequential methods)

| Task | Budget | TSNPSE-VE | TSNPSE-VP | SNPE-C | TSNPE |
|------|--------|-----------|-----------|--------|-------|
| SLCP | 10k | best | best | worse | worse |
| SLCP | 100k | best | best | worse | worse |
| Lotka-Volterra | 10k | best | best | worse | worse |
| Lotka-Volterra | 100k | best | best | worse | worse |
| Bernoulli GLM | 10k | best | best | worse | worse |
| Bernoulli GLM | 100k | best | best | worse | worse |
| Gaussian Linear | 10k | equiv | equiv | equiv | worse |
| Gaussian Linear | 100k | equiv | equiv | equiv | worse |

## Qualitative findings (from paper text):

### Tasks where TSNPSE is best or equal (SLCP, Lotka-Volterra, Bernoulli GLM):
- TSNPSE-VE and TSNPSE-VP achieve lower or roughly equivalent C2ST than both SNPE-C and TSNPE at both 10k and 100k budgets

### Gaussian Linear:
- TSNPSE-VE and TSNPSE-VP achieve lower or roughly equivalent C2ST compared to TSNPE

### Gaussian Linear Uniform, SIR, Two Moons, Gaussian Mixture (TSNPSE-VE):
- TSNPSE-VE achieves equivalent or higher C2ST compared to SNPE-C (i.e., SNPE-C is better or equal)
- TSNPSE-VE achieves equivalent or higher C2ST compared to TSNPE on GLU, SIR, Two Moons, Gaussian Mixture

### Gaussian Linear Uniform, Bernoulli GLM, SIR, Two Moons, Gaussian Mixture, Gaussian Linear (TSNPSE-VP):
- TSNPSE-VP achieves equivalent or higher C2ST compared to both SNPE-C and TSNPE (these baselines are better or equal)

### Overall observation (§5.2):
- "The best performing method can fluctuate based on the task at hand as well as the simulation budget"
- Results are "more mixed" for simpler benchmarks; TSNPSE excels on challenging tasks
