# Figure E.6: PosteriorDB Models — Relative Standard Deviation Error
- **Source**: Figure E.6, Appendix E.5
- **Caption**: "Posterior inference in Bayesian models measured by the relative standard deviation error. The curves denote the mean over 5 runs, and shaded regions denote their standard error. Solid curves (B=32) correspond to larger batch sizes than the dashed curves (B=8)."

## Experimental Conditions
- Same as Figure 5.3
- Metric: Relative SD error = ||σ_VI - σ_HMC|| / ||σ_HMC|| vs. gradient evaluations
  (where σ denotes marginal standard deviation from equation 242)

## Models
| Model | D |
|-------|---|
| arK (nearly Gaussian) | 7 |
| gp-pois-regr | 13 |
| eight-schools-centered | 10 |

## Key Observations (from paper text)
- "We typically observe the same trends as for the mean" (BaM outperforms ADVI; GSM oscillates)
- **Exception**: "In the hierarchical example [eight-schools-centered], BaM converges to a larger relative SD error" (compared to GSM and ADVI)
- Note: "the low error of GSM suggests that more robust tuning of the learning rate may lead to better performance with BaM" in the hierarchical case
- BaM benefits from B=32 over B=8; ADVI and GSM do not (consistent with mean error findings)

## Y-axis Scale Note
For the hierarchical model SD error: scale reaches at least 2×10^0 = 2 (visible from "2 × 10^0" annotation in figure caption)
