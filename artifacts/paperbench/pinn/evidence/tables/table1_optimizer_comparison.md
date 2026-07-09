---
# Table 1: Lowest Loss and L2RE for Adam, L-BFGS, and Adam+L-BFGS

- **Source**: Table 1, Section 6.1
- **Caption**: "Lowest loss for Adam, L-BFGS, and Adam+L-BFGS across all network widths after hyperparameter tuning. Adam+L-BFGS attains both smaller loss and L2RE vs. Adam or L-BFGS."
- **Experimental conditions**: Best performance across all widths (50, 100, 200, 400), learning rates, and switch points (for Adam+L-BFGS); 5 seeds per configuration; 41000 total iterations. Convection β=40, Reaction ρ=5, Wave β=5.

| Optimizer | Convection Loss | Convection L2RE | Reaction Loss | Reaction L2RE | Wave Loss | Wave L2RE |
|-----------|----------------|-----------------|---------------|---------------|-----------|-----------|
| Adam | 1.40e-4 | 5.96e-2 | 4.73e-6 | 2.12e-2 | 2.03e-2 | 3.49e-1 |
| L-BFGS | 1.51e-5 | 8.26e-3 | 8.93e-6 | 3.83e-2 | 1.84e-2 | 3.35e-1 |
| Adam+L-BFGS | 5.95e-6 | 4.19e-3 | 3.26e-6 | 1.92e-2 | 1.12e-3 | 5.52e-2 |

**Notes**:
- Adam+L-BFGS achieves 14.2× smaller L2RE than Adam on convection (5.96e-2 / 4.19e-3 ≈ 14.2)
- Adam+L-BFGS achieves 6.07× smaller L2RE than L-BFGS on wave (3.35e-1 / 5.52e-2 ≈ 6.07)
- Exception: Reaction problem — Adam outperforms Adam+L-BFGS on loss at width=100 (not shown in this summary table; see Figure 8)
