# Figure 3: Hessian and Preconditioned Hessian Spectral Densities

- **Source**: Figure 3, Sections 5.1–5.3
- **Caption**: "(Top) Spectral density of the Hessian and the preconditioned Hessian after 41000 iterations of Adam+L-BFGS. The plots show that the PINN loss is ill-conditioned and that L-BFGS improves the conditioning, reducing the top eigenvalue by 10^3 or more. (Bottom) Spectral density of the Hessian and the preconditioned Hessian of each loss component after 41000 iterations of Adam+L-BFGS for convection. The plots show that each component loss is ill-conditioned and that the conditioning is improved by L-BFGS."
- **Experimental conditions**: Best Adam+L-BFGS (11k) model for each PDE; spectral density estimated via stochastic Lanczos quadrature; preconditioned Hessian computed via Algorithm 2+3 (Appendix C.2); memory m=100

## Top Row: Total Loss Spectral Density

### Convection (β=40)
| Hessian | Max Eigenvalue (≈) | Bulk location | Condition number estimate |
|---------|-------------------|---------------|--------------------------|
| Raw H_L | >10^4 (outliers at 10^4–10^5) | Near 0 (dense) | >10^4 |
| Preconditioned | ~10^1 (much smaller outliers) | Near 0 (still present but compressed) | ≈10–100× improvement |

### Reaction (ρ=5)
| Hessian | Max Eigenvalue (≈) | Notes |
|---------|-------------------|-------|
| Raw H_L | >10^3 | Smaller outliers than convection/wave |
| Preconditioned | ~10^0 | Significant improvement |

### Wave (β=5)
| Hessian | Max Eigenvalue (≈) | Notes |
|---------|-------------------|-------|
| Raw H_L | >10^5 | Largest outliers of all three PDEs |
| Preconditioned | ~10^2 | Still larger than convection after preconditioning; 10^3× reduction |

## Bottom Row: Loss Component Spectral Density (Convection β=40)

### Residual Loss Component
| Hessian | Max Eigenvalue (≈) | Notes |
|---------|-------------------|-------|
| Raw H_L (residual) | >10^4 | Most ill-conditioned component |
| Preconditioned | Reduced by ≥10^3 | Largest improvement |

### Initial Condition Component
| Hessian | Max Eigenvalue (≈) | Notes |
|---------|-------------------|-------|
| Raw H_L (IC) | ~10^1–10^2 | Much less ill-conditioned than residual |
| Preconditioned | ~1 | Good improvement |

### Boundary Condition Component
| Hessian | Max Eigenvalue (≈) | Notes |
|---------|-------------------|-------|
| Raw H_L (BC) | ~10^1 | Least ill-conditioned component |
| Preconditioned | ~1 | Good improvement |

**Key observation**: Residual component has largest outlier eigenvalues, confirming D is the source of ill-conditioning. L-BFGS reduces max eigenvalue by ≥10^3 across all PDEs and all components.

**Note**: Figure 7 (Appendix) shows the same analysis for Reaction and Wave component losses; qualitatively similar results with residual component most ill-conditioned.
