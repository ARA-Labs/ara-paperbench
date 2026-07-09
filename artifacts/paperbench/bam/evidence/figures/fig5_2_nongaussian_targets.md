# Figure 5.2: Non-Gaussian Targets (Sinh-Arcsinh, Forward KL)
- **Source**: Figure 5.2, Section 5.1
- **Caption**: "Non-Gaussian targets constructed using the sinh-arcsinh distribution, varying the skew s and the tail weight t. The curves denote the mean of the forward KL divergence over 10 runs, and shaded regions denote their standard error. ADVI, Score, Fisher, and GSM use a batch size of B=5."

## Experimental Conditions
- Distribution: D=10 sinh-arcsinh normal, z = sinh(τ^{-1}(sinh^{-1}(y)+s)), y ~ N(μ,Σ)
- Learning rate: BaM: λ_t = BD/(t+1) (decaying); ADVI/Score/Fisher: grid-searched
- Metric: Forward KL KL(p; q_t) vs. gradient evaluations

## Configurations

### Varying Skew (τ=1 fixed, normal tails)
| s | BaM batches | Other batches |
|---|-------------|---------------|
| 0.2 | B=5 (BaM-5), B=10 (BaM-10) | B=5 |
| 1.0 | B=5, B=10 | B=5 |
| 1.8 | B=5, B=10 | B=5 |

### Varying Tails (s=0 fixed, no skew)
| τ | BaM batches | Other batches |
|---|-------------|---------------|
| 0.1 | B=5, B=10 | B=5 |
| 0.9 | B=5, B=10 | B=5 |
| 1.7 | B=5, B=10 | B=5 |

## Qualitative Findings (from paper text)
- BaM converges faster than ADVI for all skew/tail configurations
- For large skew (s=1.0, 1.8): BaM converges to higher forward KL but similar reverse KL vs ADVI (Gaussian approximation is limited)
- GSM reverse KL diverges for highly skewed target (s=1.8)
- ADVI-Score also diverges for highly skewed targets; more sensitive to learning rate
- For varying tails: all methods converge to similar reverse KL; BaM and ADVI converge to better values than GSM in some cases
- BaM stabilizes more quickly with larger batch sizes
- Decaying λ_t necessary for non-Gaussian convergence (constant λ_t fails)
