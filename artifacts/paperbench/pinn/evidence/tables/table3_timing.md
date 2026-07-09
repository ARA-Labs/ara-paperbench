---
# Table 3: Per-Iteration Wall-Clock Times for L-BFGS and NNCG

- **Source**: Table 3, Appendix E.3
- **Caption**: "Per-iteration times (in seconds) of L-BFGS and NNCG on each PDE."
- **Experimental conditions**: Single NVIDIA Titan V GPU, CUDA 11.8; times measured during training on each PDE.

| Optimizer | Convection (s) | Reaction (s) | Wave (s) |
|-----------|---------------|--------------|----------|
| L-BFGS | 4.6e-2 | 3.6e-2 | 9.0e-2 |
| NNCG | 2.5e-1 | 7.2e-1 | 2.9e1 |
| Time Ratio (NNCG/L-BFGS) | 5.43 | 20.00 | 322.22 |

**Notes**:
- Wave PDE has much larger NNCG cost because it involves second-order temporal and spatial derivatives; NNCG must compute Hessian-vector products involving second derivatives.
- L-BFGS update can be computed in O(mp) time (m=memory size=100, p=parameters).
- Each NNCG Hessian-vector product requires O((n_res + n_bc) × p) time.
- This large ratio justifies running Adam+L-BFGS first and using NNCG only for fine-tuning.
