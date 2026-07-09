# Figure 4: NNCG and GD Performance After Adam+L-BFGS

**Source**: Figure 4, Section 7.3
**Caption**: Performance of NNCG and GD after Adam+L-BFGS. (Top) NNCG reduces the loss by a factor greater than 10 in all instances, while GD fails to make progress. (Bottom) NNCG significantly reduces the gradient norm on convection and wave, while GD fails to do so.

## Key Quantitative Observations

### Loss Reduction (from Figure 4 top row)
| PDE | Adam+L-BFGS Final Loss | NNCG Final Loss | Reduction Factor |
|-----|------------------------|-----------------|------------------|
| Convection | 5.95e-6 | 3.63e-7 | ~16× |
| Reaction | 5.26e-6 | 2.89e-7 | ~18× |
| Wave | 1.12e-3 | 6.13e-5 | ~18× |

All > 10× as claimed in §7.3.

### Gradient Norm at Adam+L-BFGS Termination (from Figure 4 bottom row)
| PDE | Approximate Gradient Norm |
|-----|--------------------------|
| Convection | ~10^-2 to 10^-3 |
| Reaction | ~10^-4 to 10^-3 |
| Wave | ~10^-2 to 10^-1 |

### GD Performance
- GD applied after Adam+L-BFGS: **no loss reduction** (same loss as Adam+L-BFGS endpoint for all PDEs)

## Optimizer Phases Visible in Figure 4
- Phase 1 (Adam): iterations 0 to ~1k/11k/31k — rapid initial descent, noisy
- Phase 2 (L-BFGS): Switch at ~11k iterations — fast descent then plateau
- Phase 3 (NNCG): After L-BFGS plateau — sudden further improvement > 10×
