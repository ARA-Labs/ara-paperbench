# Figure 2: C2ST Scores — Non-Sequential Methods
- **Source**: Figure 2, Section 5.2
- **Caption**: "Results on eight benchmark tasks (non-sequential methods)."
- **Axes**: X = Simulation Budget (10k, 100k); Y = C2ST (range 0.5–1.0+, lower is better)
- **Methods**: NPSE-VE (blue), NPSE-VP (orange), NPE (green)
- **Note**: All values are approximate visual reads from line plots (≈). Exact numerical data not provided in paper; tabulated data in tables/benchmark_nonsequential.md.

## Summary Table of Qualitative Outcomes (from paper text §5.2)

| Task | Best method at 100k | NPSE-VE vs NPE | NPSE-VP vs NPE | NPSE-VE vs NPSE-VP |
|------|---------------------|----------------|----------------|---------------------|
| Lotka-Volterra | NPSE-VE or NPSE-VP | NPSE-VE ≤ NPE | NPSE-VP ≤ NPE | roughly equivalent |
| SLCP | NPSE-VE or NPSE-VP | NPSE-VE < NPE (better) | NPSE-VP < NPE (better) | roughly equivalent |
| Gaussian Linear Uniform | NPE | NPSE-VE > NPE (worse) | NPSE-VP > NPE (worse) | roughly equivalent |
| Bernoulli GLM | all equal | roughly equivalent | roughly equivalent | roughly equivalent |
| SIR | NPE | NPSE-VE ≈ NPE | NPSE-VP > NPE (worse) | NPSE-VE < NPSE-VP |
| Two Moons | NPE | NPSE-VE ≈ NPE | NPSE-VP > NPE (worse) | NPSE-VE < NPSE-VP |
| Gaussian Mixture | NPE / NPSE-VE | NPSE-VE ≈ NPE | NPSE-VP > NPE (worse) | NPSE-VE < NPSE-VP |
| Gaussian Linear | all equal | roughly equivalent | roughly equivalent | roughly equivalent |

## Qualitative findings (from paper text):

### Lotka-Volterra
- NPSE-VE and NPSE-VP achieve similar or lower C2ST than NPE at 10k and 100k
- All methods roughly equivalent within ±0.15 C2ST

### SLCP
- NPSE-VE ≈ NPSE-VP (roughly equivalent C2ST at both budgets)
- Both NPSE variants achieve lower C2ST than NPE (outperform)

### Gaussian Linear Uniform
- NPE achieves lower C2ST than both NPSE-VE and NPSE-VP
- NPSE-VE ≈ NPSE-VP (roughly equivalent)

### Bernoulli GLM
- All three methods achieve roughly equivalent C2ST

### SIR
- NPE achieves lower C2ST than NPSE-VP (NPE outperforms NPSE-VP)
- NPSE-VE competitive with NPE

### Two Moons
- NPE achieves lower C2ST than NPSE-VP
- NPSE-VE roughly equivalent to NPE

### Gaussian Mixture
- NPE ≈ NPSE-VE (roughly equivalent); both outperform NPSE-VP

### Gaussian Linear
- All three methods roughly equivalent C2ST (near 0.5 at 100k budget)
