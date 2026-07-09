# Benchmark Results: Non-Sequential Methods (Figure 2)
- **Source**: Figure 2, Section 5.2
- **Caption**: "Results on eight benchmark tasks (non-sequential methods)." C2ST scores for NPSE-VE, NPSE-VP, and NPE at simulation budgets 10k and 100k. C2ST ∈ [0.5, 1.0]; lower is better; 0.5 = perfect.
- **Note**: Values are read approximately from Figure 2 bar/line plots. All values marked ≈ (approximate visual reads from figure). The figure shows results only at 10k and 100k budgets.

| Task | Method | Budget 10k C2ST (≈) | Budget 100k C2ST (≈) |
|------|--------|----------------------|----------------------|
| Lotka Volterra | NPSE-VE | ≈0.80 | ≈0.65 |
| Lotka Volterra | NPSE-VP | ≈0.75 | ≈0.62 |
| Lotka Volterra | NPE | ≈0.82 | ≈0.72 |
| SLCP | NPSE-VE | ≈0.70 | ≈0.58 |
| SLCP | NPSE-VP | ≈0.72 | ≈0.59 |
| SLCP | NPE | ≈0.85 | ≈0.75 |
| Gaussian Linear Uniform | NPSE-VE | ≈0.72 | ≈0.60 |
| Gaussian Linear Uniform | NPSE-VP | ≈0.73 | ≈0.60 |
| Gaussian Linear Uniform | NPE | ≈0.60 | ≈0.53 |
| Bernoulli GLM | NPSE-VE | ≈0.65 | ≈0.57 |
| Bernoulli GLM | NPSE-VP | ≈0.67 | ≈0.57 |
| Bernoulli GLM | NPE | ≈0.65 | ≈0.57 |
| SIR | NPSE-VE | ≈0.65 | ≈0.55 |
| SIR | NPSE-VP | ≈0.72 | ≈0.62 |
| SIR | NPE | ≈0.60 | ≈0.52 |
| Two Moons | NPSE-VE | ≈0.58 | ≈0.52 |
| Two Moons | NPSE-VP | ≈0.75 | ≈0.65 |
| Two Moons | NPE | ≈0.57 | ≈0.51 |
| Gaussian Mixture | NPSE-VE | ≈0.58 | ≈0.52 |
| Gaussian Mixture | NPSE-VP | ≈0.78 | ≈0.65 |
| Gaussian Mixture | NPE | ≈0.58 | ≈0.52 |
| Gaussian Linear | NPSE-VE | ≈0.55 | ≈0.52 |
| Gaussian Linear | NPSE-VP | ≈0.55 | ≈0.52 |
| Gaussian Linear | NPE | ≈0.53 | ≈0.51 |

**Key findings (from paper text, §5.2)**:
- NPSE outperforms NPE on Lotka-Volterra and SLCP (most challenging)
- NPE outperforms NPSE on Gaussian Linear Uniform
- Methods roughly equivalent on Gaussian Linear, Bernoulli GLM
- NPSE-VP underperforms NPSE-VE and NPE on SIR and Two Moons (2D tasks where VE SDE is preferred)
- NPE and NPSE-VE roughly equivalent on Gaussian Mixture; both outperform NPSE-VP
