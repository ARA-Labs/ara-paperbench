---
# Related Work

## RW01: Raissi et al., 2019
- **DOI**: Journal of Computational Physics, 378:686–707, 2019
- **Type**: imports
- **Delta**:
  - What changed: This paper analyzes why PINN training fails and proposes improved optimizers; Raissi et al. introduced PINNs and used Adam/L-BFGS without systematic analysis.
  - Why: To understand and overcome the optimization challenges that limit PINNs introduced by Raissi et al.
- **Claims affected**: C01, C02, C05
- **Adopted elements**: PINN formulation (Eq. 1-2), Adam+L-BFGS training pipeline, benchmark PDEs

## RW02: Krishnapriyan et al., 2021 (NeurIPS)
- **DOI**: Advances in Neural Information Processing Systems, 2021
- **Type**: baseline
- **Delta**:
  - What changed: This paper empirically confirms ill-conditioning via Hessian spectral density and shows quasi-Newton methods improve conditioning; Krishnapriyan et al. only identified failure modes without Hessian analysis.
  - Why: To provide a more principled characterization of PINN failure.
- **Claims affected**: C02, C03, C05
- **Adopted elements**: Benchmark PDE formulations (convection, reaction, wave) and coefficient settings

## RW03: De Ryck et al., 2023
- **DOI**: arXiv:2310.05801
- **Type**: extends
- **Delta**:
  - What changed: This paper's Theorem 8.4 works on the empirical loss (not population loss) and does not require the NTK/lazy training assumption; De Ryck et al. used NTK linearization.
  - Why: NTK assumption doesn't accurately capture finite-width practical PINN behavior.
- **Claims affected**: C07
- **Adopted elements**: Operator preconditioning perspective; proof structure for Gauss-Newton matrix analysis

## RW04: Wang et al., 2022b (When and why PINNs fail to train)
- **DOI**: Journal of Computational Physics, 449:110768, 2022
- **Type**: baseline
- **Delta**:
  - What changed: This paper uses direct Hessian spectral analysis (finite-width); Wang et al. used NTK analysis requiring infinite-width.
  - Why: Finite-width analysis is more practically relevant.
- **Claims affected**: C02, C03
- **Adopted elements**: NTK-based conditioning analysis (as comparison point)

## RW05: Frangella et al., 2023 (Randomized Nyström Preconditioning)
- **DOI**: SIAM Journal on Matrix Analysis and Applications, 44(2):718–752, 2023
- **Type**: imports
- **Delta**:
  - What changed: This paper applies NyströmPCG to PINN Newton steps; Frangella et al. developed the general algorithm.
  - Why: PINN Hessian has fast spectral decay, matching the design target of NyströmPCG.
- **Claims affected**: C06
- **Adopted elements**: RandomizedNyströmApproximation (Algorithm 5), NyströmPCG (Algorithm 6)

## RW06: Liu et al., 2022 (Loss landscapes in over-parameterized systems)
- **DOI**: Applied and Computational Harmonic Analysis, 59:85–116, 2022
- **Type**: imports
- **Delta**:
  - What changed: This paper applies PŁ* theory to PINNs and derives condition numbers for the PINN objective.
  - Why: PŁ* analysis provides convergence guarantees for gradient-based methods without convexity.
- **Claims affected**: C07
- **Adopted elements**: PŁ*-condition definition, convergence theorem for gradient descent under PŁ*

## RW07: Wang et al., 2021a (Understanding gradient pathologies)
- **DOI**: SIAM Journal on Scientific Computing, 43(5):A3055–A3081, 2021
- **Type**: baseline
- **Delta**:
  - What changed: This paper focuses on optimizer design (second-order methods) rather than loss reweighting.
  - Why: Loss reweighting does not eliminate the differential operator from the objective.
- **Claims affected**: C02
- **Adopted elements**: Gradient pathology characterization in PINNs

## RW08: Liu et al., 2024 (Preconditioning for PINNs)
- **DOI**: Not specified in paper (conference paper, 2024)
- **Type**: baseline
- **Delta**:
  - What changed: This paper studies right-preconditioning (optimizer-level); Liu et al. 2024 does left-preconditioning (loss-level).
  - Why: The two approaches are complementary; combining them may yield further improvements.
- **Claims affected**: C04, C05
- **Adopted elements**: Comparison as baseline; motivation for combining approaches

## RW09: Yao et al., 2020 (PyHessian)
- **DOI**: 2020 IEEE International Conference on Big Data
- **Type**: imports
- **Delta**:
  - What changed: Uses PyHessian's SLQ implementation for Hessian spectral density estimation in PINN context.
  - Why: Efficient computation of spectral density via Hessian-vector products scales to large neural networks.
- **Claims affected**: C02, C03, C04
- **Adopted elements**: Stochastic Lanczos quadrature for spectral density estimation

## RW10: Kingma & Ba, 2014 (Adam)
- **DOI**: arXiv:1412.6980
- **Type**: imports
- **Delta**:
  - What changed: Uses Adam as Phase I of the training pipeline specifically to escape saddle points.
  - Why: Adam (like other first-order methods) avoids saddle points while L-BFGS does not.
- **Claims affected**: C05
- **Adopted elements**: Adam optimizer as Phase I of pipeline

## RW11: Nocedal & Wright, 2006 (Numerical Optimization)
- **DOI**: Springer, 2nd edition, 2006
- **Type**: imports
- **Delta**:
  - What changed: Strong Wolfe line search used in L-BFGS implementation; Armijo line search in NNCG.
  - Why: Strong Wolfe required for L-BFGS stability (though it causes early termination); Armijo is weaker and allows NNCG to continue where L-BFGS stops.
- **Claims affected**: C06
- **Adopted elements**: L-BFGS algorithm with strong Wolfe; Armijo line search condition

## RW12: Dauphin et al., 2014 (Saddle point problem)
- **DOI**: Advances in Neural Information Processing Systems, 2014
- **Type**: imports
- **Delta**:
  - What changed: Provides theoretical justification for running Adam before L-BFGS (saddle-point avoidance).
  - Why: L-BFGS converges to saddle points; Adam avoids them.
- **Claims affected**: C05
- **Adopted elements**: Observation that quasi-Newton methods converge to saddle points; first-order methods avoid them
