# Figure E.4: Non-Gaussian Targets — Reverse KL Divergence
- **Source**: Figure E.4, Appendix E.4
- **Caption**: "Non-Gaussian targets constructed using the sinh-arcsinh distribution, varying the skew s and the tail weight t. ADVI and GSM use a batch size of B=5."

## Experimental Conditions
- Same setup as Figure 5.2 (D=10, sinh-arcsinh)
- Metric: Reverse KL divergence KL(q_t; p) vs. gradient evaluations
- Method configurations: BaM (B=5, B=10), ADVI, GSM, Score, Fisher (all at B=5 for non-BaM methods)
- Learning rate: λ_t = BD/(t+1) for BaM

## Key Observations (from paper text)

### Varying Skew (τ=1)
| s | Observation |
|---|-------------|
| 0.2 | BaM converges faster; GSM and ADVI often similar |
| 1.0 | BaM converges to similar reverse KL as ADVI; GSM oscillates |
| 1.8 | GSM reverse KL diverges (instability); Score method also diverges; BaM converges |

### Varying Tails (s=0)
| τ | Observation |
|---|-------------|
| 0.1, 0.9, 1.7 | All methods tend to converge to similar reverse KL values |
| | In some cases BaM and ADVI converge to better values than GSM |
| | BaM converges faster than ADVI |

## Critical Finding
GSM divergence for s=1.8 (highly skewed target) validates the need for BaM's regularization — GSM's lack of a proper divergence objective leads to instability on non-Gaussian targets.
