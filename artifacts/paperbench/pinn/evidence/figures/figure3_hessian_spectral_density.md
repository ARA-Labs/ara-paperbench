# Figure 3: Hessian Spectral Density and Preconditioning Effect

**Source**: Figure 3, Section 5
**Caption**: (Top) Spectral density of the Hessian and preconditioned Hessian after 41000 iterations of Adam+L-BFGS. The plots show that the PINN loss is ill-conditioned and that L-BFGS improves the conditioning, reducing the top eigenvalue by 10^3 or more. (Bottom) Spectral density of Hessian and preconditioned Hessian of each loss component after 41000 iterations for convection.

## Key Quantitative Data (from paper text)

### Top Eigenvalue Magnitudes (Hessian, unpreconditioned)
| PDE | Top Eigenvalue Magnitude |
|-----|--------------------------|
| Convection (β=40) | > 10^4 |
| Reaction (ρ=5) | > 10^3 |
| Wave (β=5) | > 10^5 |

### Preconditioning Effect
- For ALL three PDEs: L-BFGS preconditioning reduces magnitude of top eigenvalue by at least **10^3×**
- Spectral density near 0: significant for all PDEs (indicating ill-conditioning)

### Loss Component Analysis (Convection, Figure 3 bottom)
- Residual component: most ill-conditioned (largest eigenvalue outliers)
- Initial condition component: comparatively less ill-conditioned
- Boundary condition component: comparatively less ill-conditioned

### Observation from §6.2
- Convection: largest eigenvalue ~10^4
- Reaction: largest eigenvalue ~10^3 (least ill-conditioned — explains why Adam ≈ Adam+L-BFGS on reaction)
- Wave: largest eigenvalue ~10^5 (most ill-conditioned)

## Method
- Stochastic Lanczos Quadrature (SLQ) via PyHessian (Yao et al., 2020)
- Preconditioned Hessian: H̃ᵀ H_L H̃ computed via Algorithm 2+3 (L-BFGS unrolling)
- Memory size m=100 used for L-BFGS
