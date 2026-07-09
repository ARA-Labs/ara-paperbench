---
# Constraints and Limitations

## Boundary Conditions (Where the Solution Works)

### Regime Constraints
- C1: NNCG requires a good initialization (from Adam+L-BFGS); applied directly after Adam it does not improve results because Phase I has not escaped saddle points.
- C2: The PŁ* condition must hold locally; this is satisfied with high probability for sufficiently wide networks but may fail for very narrow or very deep networks.
- C3: The PINN approach solves forward problems without labeled data; for inverse problems, additional terms enter the loss.
- C4: Training points are fixed throughout (no adaptive sampling); this may cause issues for PDEs with localized features not well-represented by uniform sampling from a 255×100 grid.
- C5: The theoretical analysis (Theorem 8.4) applies to linear PDEs; nonlinear extension requires additional work.

## Known Limitations

### Computational
- L1: NNCG is 5–322× slower per-iteration than L-BFGS; for wave PDE, each NNCG step takes ~29 seconds due to second-derivative HVPs. Not practical as primary optimizer.
- L2: The preconditioned Hessian spectral density computation requires storing m=100 L-BFGS direction pairs (memory cost O(mp)).
- L3: Sketch size s=60 for NyströmPCG is tuned empirically; different PDEs may require different s.

### Methodological
- L4: Adam+L-BFGS's switch point (1k, 11k, 31k) requires tuning; no principled criterion for the switch.
- L5: L-BFGS terminates early due to strong Wolfe line search failure; this is structural and limits its effectiveness without NNCG follow-up.
- L6: The paper studies only 1D PDEs (convection, reaction, wave); scaling to higher dimensions is not validated.
- L7: Trivial solutions (constant functions satisfying residual but not BC) can occur; adaptive loss reweighting could help but is not studied here.

### Theoretical
- L8: The GDND analysis uses GD (not Adam) in Phase I; a rigorous analysis of Adam+L-BFGS+NNCG does not exist.
- L9: Theorem 8.4's polynomial decay assumption (λ_j(A◦K∞) = O(j^{-2α})) is not verified analytically; it is supported empirically via Figure 10.
- L10: The ill-conditioning results apply to any ML approach that penalizes PDE residuals; physics-informed DeepONet and similar hybrid methods also inherent this difficulty.

## Assumptions in the Analysis
- A1: Interpolation (L(w*)=0) is achievable by sufficiently expressive networks
- A2: PŁ* constant μ > 0 exists locally (valid for wide nets with high probability)
- A3: Hessian Lipschitz constant L_{HL} and Jacobian norm L_F are finite
- A4: Eigenvalue decay λ_j(A◦K∞(w*)) = O(j^{-2α}), α > 1/2 (empirically supported)
