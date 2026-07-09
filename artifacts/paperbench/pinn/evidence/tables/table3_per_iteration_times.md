# Table 3: Per-Iteration Wall-Clock Times for L-BFGS and NNCG

**Source**: Table 3, Appendix E.3
**Caption**: Per-iteration times (in seconds) of L-BFGS and NNCG on each PDE.

## Raw Data

| Optimizer | Convection | Reaction | Wave |
|-----------|-----------|----------|------|
| L-BFGS | 4.6e-2 s | 3.6e-2 s | 9.0e-2 s |
| NNCG | 2.5e-1 s | 7.2e-1 s | 2.9e1 s |
| Time Ratio (NNCG/L-BFGS) | 5.43 | 20.0 | 322.22 |

## Notes
- Large ratio on Wave (322×) vs Convection (5×) is because wave equation requires second-order spatial AND temporal derivatives in the PDE residual, so Hessian-vector products for NNCG are much more expensive
- Convection and reaction require only first-order derivatives in residual
- Hardware: NVIDIA Titan V GPU
- These times motivate the design choice of using L-BFGS first and NNCG only as a fine-tuning step
