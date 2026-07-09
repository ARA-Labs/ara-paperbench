# Figure 6: Sequential Method Comparison (SNPSE-A vs SNPSE-B vs TSNPSE)
- **Source**: Figure 6, Appendix C.5
- **Caption**: "Comparison between SNPSE-A, SNPSE-B, and TSNPSE on two benchmark tasks."
- **Experimental conditions**: Sequential methods on SLCP and Gaussian Linear Uniform (GLU) tasks. R=10 rounds. Same architecture and training hyperparameters. SNPSE-C omitted (C2ST ≈ 1.0 failure).
- **Axes**: x-axis = Simulation Budget; y-axis = C2ST ∈ [0.5, 1.0]

Note: Values are approximate visual readings from line plots.

| Task | Method | Budget=10k C2ST | Budget=100k C2ST |
|------|--------|-----------------|------------------|
| SLCP | TSNPSE | ≈0.60 | ≈0.55 |
| SLCP | SNPSE-A | ≈0.80 | ≈0.72 |
| SLCP | SNPSE-B | ≈0.85 | ≈0.78 |
| Gaussian Linear Uniform | TSNPSE | ≈0.62 | ≈0.58 |
| Gaussian Linear Uniform | SNPSE-A | ≈0.75 | ≈0.68 |
| Gaussian Linear Uniform | SNPSE-B | ≈0.80 | ≈0.72 |

**Key findings (from Appendix C.5 text)**:
- TSNPSE significantly outperforms both SNPSE-A and SNPSE-B on both tasks
- Finding replicated across other tasks (not shown)
- SNPSE-C excluded: empirically achieves C2ST ≈ 1.0 (complete failure)
- SNPSE-C failure attributed to significant approximation error in estimating proposal prior score (§C.4.3)
- SNPSE-B performance could likely be improved using techniques from Xiong et al. (2023)
