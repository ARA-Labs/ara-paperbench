---
# Problem Specification

## Observations

### O1: Near-zero loss required for accurate PINN solutions
- **Statement**: A PINN loss of 10^-3 yields L2RE ~10^-1 on convection, while reducing loss 100× to 10^-5 yields L2RE ~10^-2 (10× improvement). The relationship is monotone but requires extremely low loss values.
- **Evidence**: Figure 2; the plot shows final loss vs. final L2RE for all combinations of width, optimizer, and seed across three PDEs.
- **Implication**: Ordinary convergence (e.g., loss ~10^-3) is insufficient; solvers must achieve interpolation (L(w)→0).

### O2: PINN loss is ill-conditioned
- **Statement**: After 41000 iterations of Adam+L-BFGS, the Hessian spectral density of the total PINN loss shows large outlier eigenvalues (>10^4 for convection, >10^3 for reaction, >10^5 for wave) and significant density near eigenvalue 0.
- **Evidence**: Figure 3 (top row); Hessian spectral density plots for all three PDEs.
- **Implication**: The condition number κ > 10^4 causes first-order methods like gradient descent to require O(κ log(1/ε)) iterations, which is slow.

### O3: Ill-conditioning originates in the residual loss
- **Statement**: The residual loss component (containing differential operator D) is the most ill-conditioned among residual, initial condition, and boundary condition components across all three PDEs.
- **Evidence**: Figure 3 (bottom row, Convection); Figure 7 (Reaction, Wave); spectral density plots of individual components.
- **Implication**: The differential operator D is the primary source of ill-conditioning.

### O4: L-BFGS preconditioning reduces condition number ≥1000×
- **Statement**: The preconditioned Hessian (via L-BFGS) shows reduced top eigenvalues by at least 10^3 for all three problems, and reduced condition number of each loss component.
- **Evidence**: Figure 3, dashed vs. solid lines; Section 5.3.
- **Implication**: Quasi-Newton methods effectively precondition the loss landscape.

### O5: Adam+L-BFGS outperforms either alone
- **Statement**: Adam+L-BFGS attains 14.2× smaller L2RE than Adam on convection, 6.07× smaller than L-BFGS on wave. Across all widths and PDEs, Adam+L-BFGS consistently achieves the lowest loss and L2RE.
- **Evidence**: Table 1; Figure 8 (Appendix D).
- **Implication**: The combination leverages saddle-point escape from Adam and improved local conditioning from L-BFGS.

### O6: L-BFGS terminates early with non-zero gradient
- **Statement**: L-BFGS stops making progress before reaching the maximum number of iterations; for convection and wave, the strong Wolfe line search finds no acceptable step size, while for reaction the gradient slope is below threshold. Gradient norm at termination is ~10^-2 to 10^-3.
- **Evidence**: Figure 4 (bottom row); Figure 9 (Appendix E).
- **Implication**: The loss is under-optimized at L-BFGS termination, but residual gradient information remains exploitable.

### O7: NNCG further reduces loss and L2RE after Adam+L-BFGS
- **Statement**: Running NNCG for 2000 additional steps after Adam+L-BFGS reduces loss by >10× and improves L2RE: Convection 4.19e-3 → 1.94e-3, Reaction 1.92e-2 → 9.92e-3, Wave 5.52e-2 → 1.27e-2. GD applied similarly produces zero improvement.
- **Evidence**: Table 2; Figure 4; Figure 5.
- **Implication**: A damped Newton method with Armijo line search can escape where L-BFGS's strong Wolfe conditions fail.

## Gaps

### G1: No principled optimizer for ill-conditioned PINN loss
- **Statement**: Existing methods (Adam, L-BFGS, Adam+L-BFGS) are insufficient: Adam is slow due to ill-conditioning; L-BFGS terminates early; no method reliably achieves the near-zero loss required.
- **Caused by**: O1, O2, O3, O6
- **Existing attempts**: Loss reweighting (Wang et al. 2021a), NTK-based analysis (Wang et al. 2022b), operator preconditioning (Liu et al. 2024)
- **Why they fail**: Loss reweighting does not eliminate the differential operator from the objective; NTK analysis requires infinite-width assumptions; operator preconditioning is left-preconditioning vs. right-preconditioning studied here.

### G2: Lack of theory connecting differential operator conditioning to loss conditioning
- **Statement**: Prior theory (De Ryck et al. 2023) relied on lazy training / NTK assumption, which does not accurately reflect practical finite-width PINN training.
- **Caused by**: O2, O3
- **Existing attempts**: De Ryck et al. 2023 proved similar results using NTK linearization
- **Why they fail**: The NTK assumption requires the network to stay near initialization, which is not empirically observed.

## Key Insight

- **Insight**: The spectral decay of the PINN Hessian (fast decay, many small eigenvalues) is precisely the structure that Nyström-based preconditioned conjugate gradient exploits—NNCG can efficiently solve the Newton step to escape where L-BFGS's line search fails.
- **Derived from**: O2, O3, O4, O6
- **Enables**: Design of NNCG that uses NyströmPCG to exploit fast spectral decay, paired with Armijo line search (weaker than strong Wolfe) to guarantee descent; also the Adam+NNCG pipeline where Adam handles saddle-point escape and NNCG handles local second-order convergence.

## Assumptions

- A1: Neural networks can achieve near-zero loss (interpolation) if optimized sufficiently (supported by universal approximation theorems).
- A2: The PŁ*-condition holds locally around minimizers (supported for wide networks by Liu et al. 2022).
- A3: The differential operator D is ill-conditioned for the studied PDEs (convection, reaction, wave at given coefficients).
- A4: The eigenvalues of A◦K∞(w*) decay polynomially as j^{-2α} for α > 1/2.
- A5: The number of residual points n_res is in the range 10^3 to 10^4 (as used experimentally).
