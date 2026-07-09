# Figure 5.1: Gaussian Targets — Forward KL Divergence vs. Gradient Evaluations

**Source**: Figure 5.1 (main paper, §5.1)  
**Claims**: C01, C03, C04  
**Description**: Forward KL divergence KL(p;q) plotted against number of gradient evaluations for BaM, ADVI, ADVI-Score, ADVI-Fisher, and GSM on randomly constructed Gaussian targets of increasing dimension. Solid curves = mean over 10 runs (transparent = individual runs). ADVI/Score/Fisher/GSM use B=2; BaM uses two batch sizes per dimension.

## Qualitative Results (from paper)

| Dimension | BaM Batch Sizes | Key Observation |
|-----------|----------------|-----------------|
| D=4 | B=2, B=5 | BaM converges orders of magnitude faster than ADVI |
| D=16 | B=2, B=15 | BaM at larger B converges faster; GSM competitive at B=2 |
| D=64 | B=2, B=40 | BaM benefit increases with dimension; ADVI/Score/Fisher similar |
| D=256 | B=2, B=150 | BaM at B=150 converges much faster than B=2; ADVI still slow |

## Key Numerical Observations (from paper text §5.1 and Appendix E.3)

- **BaM vs ADVI**: BaM converges orders of magnitude faster (in gradient evaluations) than ADVI on all dimensions.
- **BaM batch scaling**: Larger batch sizes lead to faster convergence for BaM.
- **GSM vs BaM at B=2**: GSM and BaM perform similarly at B=2; GSM does not benefit from B>2 (paper: "marginal gains beyond B=2").
- **ADVI variants**: ADVI, ADVI-Score, and ADVI-Fisher all perform similarly; score-based divergence more sensitive to LR.
- **Learning rate**: BaM uses constant λ=BD; ADVI: lr=0.01; Fisher: lr=0.01; Score: [0.01, 0.005, 0.001, 0.001] for D=4,16,64,256.

## Appendix E.3 Results (Reverse KL and Learning Rate Comparison)

- Similar conclusions for reverse KL as forward KL (Figure E.3).
- Constant learning rate λ=BD performs best among tested schedules for Gaussian targets (Figure E.2 for D=16).
- Lines for B=20, B=40 overlap at constant LR for D=16, indicating good convergence behavior.
