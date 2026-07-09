# Figure 5.3: Posterior Inference in Bayesian Models (Relative Mean Error)
- **Source**: Figure 5.3, Section 5.2
- **Caption**: "Posterior inference in Bayesian models. The curves denote the mean over 5 runs, and shaded regions denote their standard error. Solid curves (B=32) correspond to larger batch sizes than dashed curves (B=8)."

## Experimental Conditions
- Models from PosteriorDB (Magnusson et al., 2022)
- Reference: HMC samples
- Metric: Relative mean error = ||μ_VI - μ_HMC|| / ||μ_HMC|| vs. gradient evaluations
- Seeds: 5

## Models

| Model | D | Type |
|-------|---|------|
| arK (nearly Gaussian) | 7 | Autoregressive |
| gp-pois-regr (Gaussian Process) | 13 | Non-Gaussian |
| eight-schools-centered (Hierarchical) | 10 | Non-Gaussian |

## Method Configurations
| Method | Batch Sizes | Learning Rate |
|--------|-------------|---------------|
| BaM | 8 (dashed), 32 (solid) | λ_t = BD/(t+1) |
| ADVI | 8 (dashed), 32 (solid) | Grid searched |
| GSM | 8 (dashed), 32 (solid) | N/A |

## Qualitative Findings (from paper text)
- BaM outperforms ADVI overall (lower relative mean error, faster convergence)
- GSM can converge faster than BaM at smaller batch sizes (B=8) but oscillates around the solution
- BaM improves with larger batch size (B=32 > B=8); ADVI and GSM do not benefit from larger batches
- All 3 panels show same qualitative trend (arK, GP, hierarchical)
- For relative SD error (Fig E.6): similar trends, except hierarchical model where BaM converges to larger relative SD error than GSM (potential for improvement with better learning rate tuning)
