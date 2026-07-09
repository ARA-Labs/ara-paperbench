---
# Figure 3 & Figure 7: Hessian Spectral Density Before and After L-BFGS Preconditioning

- **Source**: Figure 3 (§5.1, §5.2, §5.3) + Figure 7 (Appendix C)
- **Caption**: Figure 3: "(Top) Spectral density of the Hessian and the preconditioned Hessian after 41000 iterations of Adam+L-BFGS. The plots show that the PINN loss is ill-conditioned and that L-BFGS improves the conditioning, reducing the top eigenvalue by 10^3 or more. (Bottom) Spectral density of the Hessian and the preconditioned Hessian of each loss component after 41000 iterations of Adam+L-BFGS for convection."
- **Axis labels**: X-axis: Eigenvalue; Y-axis: Density (log scale ~1e-10 to 1e-1)
- **Conditions**: Best Adam+L-BFGS run per PDE (width and lr with lowest L2RE at 41000 iterations)

## Top Row: Total Loss Hessian Spectral Density

### Convection (β=40)
| | Unpreconditioned | Preconditioned |
|--|--|--|
| Max eigenvalue (approximate) | >10^4 | ~10 |
| Spectral range | ~[-10^1, 10^4] | ~[-1, 10^1] |
| Density near 0 | High (significant) | Lower |
| Condition number | >10^4 | Much reduced |

### Reaction (ρ=5)
| | Unpreconditioned | Preconditioned |
|--|--|--|
| Max eigenvalue | >10^3 | ~1 |
| Spectral range | ~[0, 10^3] | ~[0, 1] |
| Density near 0 | High | Lower |
| Condition number | >10^3 | Much reduced |

### Wave (β=5)
| | Unpreconditioned | Preconditioned |
|--|--|--|
| Max eigenvalue | >10^5 | ~10^2 |
| Spectral range | ~[-10^2, 10^5] | ~[-10^1, 10^2] |
| Density near 0 | High (significant) | Lower |
| Condition number | >10^5 | Much reduced |

## Bottom Row: Loss Component Spectral Density (Convection β=40)

| Component | Unpreconditioned Max | Preconditioned Max | Most ill-conditioned? |
|-----------|---------------------|-------------------|----------------------|
| Residual | ~10^4 (largest) | ~10 | YES |
| Initial Condition | ~10^2 | ~1 | No |
| Boundary Condition | ~10^1 | ~0.1 | No (least) |

## Figure 7: Loss Component Spectral Density (Reaction, Wave)

### Reaction (ρ=5) — Component Spectral Density
| Component | Unpreconditioned Max | Preconditioned Max |
|-----------|---------------------|-------------------|
| Residual | ~10^3 (largest) | ~1 |
| Initial Condition | ~10^2 | ~0.1 |
| Boundary Condition | ~10^1 | ~0.1 |

### Wave (β=5) — Component Spectral Density
| Component | Unpreconditioned Max | Preconditioned Max |
|-----------|---------------------|-------------------|
| Residual | ~10^5 (largest, note: includes negative eigenvalues) | ~10^2 |
| Initial Condition | ~10^3 | ~10^1 |
| Boundary Condition | ~10^2 | ~1 |

## Key Observations
1. All total losses show significant spectral density near eigenvalue 0 (many near-zero eigenvalues) — indicates flat directions
2. Preconditioned Hessian reduces top eigenvalue by ≥1000× for all three PDEs
3. Residual component is consistently the most ill-conditioned across all PDEs
4. Preconditioning also reduces condition number of each individual component
5. Wave residual shows negative eigenvalues in the spectrum (indefinite Hessian near solution)
