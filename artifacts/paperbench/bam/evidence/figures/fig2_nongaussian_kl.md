# Figure 5.2: Non-Gaussian (sinh-arcsinh) Targets — KL Divergence vs. Gradient Evaluations

**Source**: Figures 5.2, E.4 (§5.1, Appendix E.4)  
**Claims**: C01, C04  
**Description**: Forward KL divergence (main figure 5.2; mean over 10 runs with std error bands) and reverse KL divergence (Appendix Figure E.4) for BaM, ADVI, ADVI-Score, ADVI-Fisher, and GSM on 10-dimensional sinh-arcsinh normal distributions. ADVI/Score/Fisher/GSM use B=5; BaM uses B=5 and B=10.

## Target Configurations

| Config | Parameters | Distribution Type |
|--------|------------|-------------------|
| (t=1, s=0.2) | Normal tails, mild skew | Near-Gaussian |
| (t=1, s=1.0) | Normal tails, moderate skew | Moderately non-Gaussian |
| (t=1, s=1.8) | Normal tails, high skew | Highly skewed |
| (t=0.1, s=0) | Very light tails, no skew | Light-tailed |
| (t=0.9, s=0) | Slightly light tails, no skew | Near-Gaussian tails |
| (t=1.7, s=0) | Heavy tails, no skew | Heavy-tailed |

## Key Observations from Paper (§5.1)

### Varying skew (normal tails t=1):
- **BaM vs ADVI convergence speed**: BaM converges faster than ADVI for all skew values.
- **Forward KL**: For large skew (s=1.0, s=1.8), BaM converges to a *higher* forward KL than ADVI.
- **Reverse KL**: For all skew values, BaM converges to *similar* reverse KL as ADVI.
- **GSM failure**: For s=1.8 (high skew), GSM's reverse KL *diverges*; ADVI-Score also diverges.
- **BaM stability**: BaM with larger B stabilizes more quickly than smaller B.

### Varying tails (no skew s=0):
- **All methods**: Converge to *similar* values of reverse KL divergence.
- **BaM vs ADVI**: BaM typically converges in fewer gradient evaluations than ADVI.
- **BaM vs GSM**: In some cases, BaM and ADVI converge to better values than GSM.

## Learning Rates Used (Appendix E.4)
- **BaM**: λ_t = BD/(t+1) (decaying)
- **ADVI**: lr = 0.02
- **Fisher**: lr = 0.05
- **Score (t=1, varying s)**: lr = [0.01, 0.001, 0.001] for s=0.2, 1.0, 1.8
- **Score (s=0, varying t)**: lr = [0.001, 0.01, 0.01] for t=0.1, 0.9, 1.7
