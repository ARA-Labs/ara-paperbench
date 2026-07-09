---
# Claims

## C01: Near-zero training loss is necessary for accurate PINN solutions
- **Statement**: For PINNs, there is a monotone but nonlinear relationship between training loss and L2 relative error (L2RE): achieving acceptably low L2RE (e.g., <0.1) requires training loss to be in the range 10^-5 or smaller, depending on the PDE. Instances exist where loss ≈ 0 but L2RE ≈ 1 (trivial solutions).
- **Status**: supported
- **Falsification criteria**: A PINN achieving L2RE < 0.05 with training loss > 10^-3 would refute this claim.
- **Proof**: [E01]
- **Dependencies**: none
- **Tags**: generalization, interpolation, loss-accuracy relationship

## C02: PINN loss is ill-conditioned with condition number >10^4
- **Statement**: After training with Adam+L-BFGS for 41000 iterations, the Hessian of the PINN loss shows large outlier eigenvalues (>10^4 for convection, >10^3 for reaction, >10^5 for wave) and significant spectral density near 0, indicating ill-conditioning that impedes first-order optimizer convergence.
- **Status**: supported
- **Falsification criteria**: A PINN Hessian with condition number < 100 on these benchmark problems would refute this.
- **Proof**: [E02]
- **Dependencies**: none
- **Tags**: ill-conditioning, Hessian, spectral density

## C03: Residual loss (differential operator term) is the dominant source of ill-conditioning
- **Statement**: Among the three components of PINN loss (residual, initial condition, boundary condition), the residual component containing the differential operator D is the most ill-conditioned. This is both empirically observed and theoretically predicted.
- **Status**: supported
- **Falsification criteria**: Another component (IC or BC) having larger or equal maximum Hessian eigenvalue would refute this claim.
- **Proof**: [E02]
- **Dependencies**: C02
- **Tags**: residual loss, differential operator, ill-conditioning

## C04: L-BFGS preconditioning reduces the condition number by ≥1000×
- **Statement**: The L-BFGS preconditioned Hessian (H_k · H_L) has top eigenvalue reduced by at least 10^3 compared to the unpreconditioned Hessian, for all three studied PDEs and all individual loss components.
- **Status**: supported
- **Falsification criteria**: Preconditioned Hessian with top eigenvalue reduction < 100× on these problems would refute this.
- **Proof**: [E02]
- **Dependencies**: C02
- **Tags**: preconditioning, L-BFGS, quasi-Newton

## C05: Adam+L-BFGS consistently outperforms Adam or L-BFGS alone
- **Statement**: Across all tested network widths (50, 100, 200, 400) and all three PDEs, the Adam+L-BFGS combined strategy achieves the lowest minimum loss and L2RE. Specifically: 14.2× smaller L2RE than Adam on convection; 6.07× smaller L2RE than L-BFGS on wave.
- **Status**: supported
- **Falsification criteria**: Adam or L-BFGS alone achieving lower min loss/L2RE than all Adam+L-BFGS variants across any PDE-width combination (beyond the one noted exception on reaction) would weaken this claim.
- **Proof**: [E03]
- **Dependencies**: C02, C04
- **Tags**: optimizer comparison, Adam, L-BFGS, combined method

## C06: NNCG further improves solutions where Adam+L-BFGS stalls
- **Statement**: Running NNCG for 2000 iterations after Adam+L-BFGS reduces training loss by >10× and improves L2RE on all three PDEs. Gradient descent applied identically produces zero improvement. NNCG is 5–322× slower per-iteration than L-BFGS.
- **Status**: supported
- **Falsification criteria**: NNCG failing to reduce loss by >2× after 2000 steps on any problem would weaken this claim; GD achieving similar improvement would fully refute it.
- **Proof**: [E04]
- **Dependencies**: C02, C04, C05
- **Tags**: NNCG, second-order optimizer, NystromPCG, Armijo

## C07: Ill-conditioned differential operators provably induce large PINN condition numbers
- **Statement**: Theorem 8.4 shows that if the eigenvalues of A◦K∞(w*) satisfy λ_j = O(j^{-2α}) with α > 1/2, and √n_res = Ω(log(1/δ)), then κ_L(S) = Ω(n_res^α) with high probability. This bound grows polynomially with the number of residual points n_res (typically 10^3–10^4).
- **Status**: supported
- **Falsification criteria**: A polynomial eigenvalue decay setting where the condition number does not grow with n_res would refute this theorem.
- **Proof**: [E05]
- **Dependencies**: C02, C03
- **Tags**: theory, condition number, PL-star, Gauss-Newton, operator theory
