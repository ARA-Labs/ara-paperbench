---
# Benchmark C2ST Posterior Performance

- **Source**: Figure 4a, Section 4.1
- **Caption**: "Classifier Two-Sample Test (C2ST) accuracy between Simformer- and ground-truth posteriors" across four benchmark tasks. Lower C2ST (closer to 0.5) = better.
- **Conditions**: VESDE; 10 ground-truth reference posteriors per task; C2ST via 5-fold cross-validation random forest (100 trees). 6-layer Simformer with token_dim=50, 4 heads, attention size 10. NPE via neural spline flow (sbi library defaults).

**Note**: Exact numerical values are read from Figure 4a (bar plots at 10³, 10⁴, 10⁵ simulations) and are approximate (≈) due to extraction from figures. The paper does not provide a results table with exact values.

| Task | Method | 10³ sims C2ST | 10⁴ sims C2ST | 10⁵ sims C2ST |
|------|--------|---------------|---------------|---------------|
| Linear Gaussian | NPE | ≈0.55 | ≈0.51 | ≈0.50 |
| Linear Gaussian | Simformer (dense) | ≈0.70 | ≈0.55 | ≈0.52 |
| Linear Gaussian | Simformer (undirected) | ≈0.52 | ≈0.50 | ≈0.50 |
| Linear Gaussian | Simformer (directed) | ≈0.51 | ≈0.50 | ≈0.50 |
| Mixture Gaussian | NPE | ≈0.75 | ≈0.60 | ≈0.52 |
| Mixture Gaussian | Simformer (dense) | ≈0.62 | ≈0.53 | ≈0.51 |
| Mixture Gaussian | Simformer (undirected) | ≈0.60 | ≈0.52 | ≈0.50 |
| Mixture Gaussian | Simformer (directed) | ≈0.60 | ≈0.52 | ≈0.50 |
| Two Moons | NPE | ≈0.90 | ≈0.70 | ≈0.55 |
| Two Moons | Simformer (dense) | ≈0.75 | ≈0.58 | ≈0.51 |
| Two Moons | Simformer (undirected) | ≈0.75 | ≈0.58 | ≈0.51 |
| Two Moons | Simformer (directed) | ≈0.75 | ≈0.58 | ≈0.51 |
| SLCP | NPE | ≈0.95 | ≈0.85 | ≈0.65 |
| SLCP | Simformer (dense) | ≈0.85 | ≈0.70 | ≈0.55 |
| SLCP | Simformer (undirected) | ≈0.75 | ≈0.58 | ≈0.51 |
| SLCP | Simformer (directed) | ≈0.70 | ≈0.55 | ≈0.51 |

**Key finding from paper text**: "Across all four benchmark tasks, the Simformer outperformed NPE, even when the Simformer used a dense attention mask... The only exception was the Gaussian linear task with 10k simulations." "Averaged across all benchmark tasks and observations, the Simformer required about 10 times fewer simulations than NPE."
