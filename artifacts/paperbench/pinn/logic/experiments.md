---
# Experiments

## E01: Loss vs. L2RE correlation across PDEs
- **Verifies**: C01
- **Setup**:
  - Model: MLP with 3 hidden layers, widths {50, 100, 200, 400}, tanh activations, Xavier normal init
  - Hardware: Single NVIDIA Titan V GPU
  - Dataset: Convection (β=40), Reaction (ρ=5), Wave (β=5) from Appendix A.1-A.3
  - System: All optimizer combinations (Adam, L-BFGS, Adam+L-BFGS with 1k/11k/31k switch points)
- **Procedure**:
  1. Run full training sweep: all (PDE, optimizer, width, seed) combinations for 41000 iterations
  2. At end of training, record final loss L(w) and L2RE on full evaluation grid
  3. Scatter-plot final loss vs. final L2RE for each combination
  4. Identify cases where loss ≈ 0 but L2RE ≈ 1 (trivial solutions)
- **Metrics**: Final training loss, final L2RE, presence of trivial solution cases
- **Expected outcome**:
  - Lower training loss generally corresponds to lower L2RE (monotone trend)
  - Very low loss does not always guarantee low L2RE (trivial solutions exist for convection and reaction)
  - Substantial loss reduction (orders of magnitude) is needed for meaningful L2RE improvement
- **Baselines**: All optimizer variants provide data points for the scatter
- **Dependencies**: none

## E02: Hessian spectral analysis before and after L-BFGS preconditioning
- **Verifies**: C02, C03, C04
- **Setup**:
  - Model: Best model from Adam+L-BFGS training sweep (width with best final L2RE, best learning rate)
  - Hardware: Single NVIDIA Titan V GPU
  - Dataset: Convection, Reaction, Wave
  - System: 41000 iterations Adam+L-BFGS; Stochastic Lanczos Quadrature (SLQ) for spectral density estimation
- **Procedure**:
  1. Train MLP using best Adam+L-BFGS configuration for each PDE
  2. Save L-BFGS stored directions {y_i}, steps {s_i}, and inverse inner products {ρ_i} (m=100 pairs)
  3. Compute spectral density of H_L using SLQ (via PyHessian or equivalent)
  4. Unroll L-BFGS update (Algorithm 2) to form Ỹ, Ṡ, Ṽ matrices
  5. Compute spectral density of preconditioned Hessian H̃_k^T H_L H̃_k using Algorithm 3 (matrix-vector products via Algorithm 3)
  6. Repeat for each loss component (residual, IC, BC) separately
  7. Visualize spectral density plots (solid = Hessian, dashed = preconditioned)
- **Metrics**: Maximum eigenvalue, spectral density near zero, visual comparison of component spectra
- **Expected outcome**:
  - Total loss Hessian shows large outlier eigenvalues and significant density near 0
  - Preconditioned Hessian shows substantially reduced maximum eigenvalues (at least 1000× reduction)
  - Residual component is more ill-conditioned than IC and BC components
  - Preconditioning improves each individual component
- **Baselines**: Unpreconditioned Hessian spectral density
- **Dependencies**: E01 (need trained models)

## E03: Optimizer comparison: Adam vs L-BFGS vs Adam+L-BFGS
- **Verifies**: C05
- **Setup**:
  - Model: MLP widths {50, 100, 200, 400}, 3 hidden layers, tanh, Xavier init
  - Hardware: Single NVIDIA Titan V GPU
  - Dataset: Convection (β=40), Reaction (ρ=5), Wave (β=5)
  - System: 41000 total iterations; 5 random seeds per configuration
- **Procedure**:
  1. For Adam: grid search lr ∈ {1e-5, 1e-4, 1e-3, 1e-2, 1e-1}
  2. For L-BFGS: lr=1.0, memory=100, strong Wolfe line search
  3. For Adam+L-BFGS: grid search Adam lr ∈ {1e-5,...,1e-1} × switch point ∈ {1k, 11k, 31k}
  4. Record final loss and L2RE for all combinations
  5. For each (PDE, width, optimizer), find lr configuration with lowest final loss (and lowest L2RE)
  6. Report min, median, max across 5 seeds at optimal lr
- **Metrics**: Final training loss, final L2RE; min/median/max across seeds
- **Expected outcome**:
  - Adam+L-BFGS achieves lower minimum loss than Adam or L-BFGS alone across most width-PDE combinations
  - Adam+L-BFGS achieves lower minimum L2RE in most cases
  - Exception expected on reaction problem at certain widths where Adam performs comparably
- **Baselines**: Adam alone, L-BFGS alone
- **Dependencies**: none

## E04: NNCG fine-tuning after Adam+L-BFGS
- **Verifies**: C06
- **Setup**:
  - Model: Best Adam+L-BFGS configuration from E03 (width, lr, switch point with lowest L2RE) per PDE
  - Hardware: Single NVIDIA Titan V GPU
  - Dataset: Convection, Reaction, Wave
  - System: NNCG run for 2000 additional steps with η=1, K=2000, s=60, F=20, ε=1e-16, M=1000, α=0.1, β=0.5, μ ∈ {1e-5, 1e-4, 1e-3, 1e-2, 1e-1}; GD also run for comparison
- **Procedure**:
  1. Take trained model from best Adam+L-BFGS run
  2. Continue training with NNCG for 2000 iterations (tuning μ)
  3. Also continue with GD for 2000 iterations (as baseline)
  4. Record loss and gradient norm at each NNCG/GD step
  5. Record final L2RE for NNCG, GD, and original Adam+L-BFGS
  6. Visualize pointwise absolute error at each optimizer switch point
  7. Measure per-iteration wall-clock times for L-BFGS and NNCG
- **Metrics**: Loss trajectory, gradient norm trajectory, final L2RE, pointwise absolute error maps, per-iteration wall-clock time
- **Expected outcome**:
  - NNCG reduces loss by >10× compared to Adam+L-BFGS endpoint
  - NNCG significantly reduces gradient norm on convection and wave
  - GD produces no improvement in loss or L2RE
  - NNCG is 5–322× slower per-iteration than L-BFGS (depending on PDE)
  - Pointwise error maps show progressive improvement: Adam → Adam+L-BFGS → Adam+L-BFGS+NNCG
- **Baselines**: GD fine-tuning, Adam+L-BFGS without fine-tuning
- **Dependencies**: E03

## E05: Empirical verification of condition number growth with n_res
- **Verifies**: C07
- **Setup**:
  - Model: MLP with 2 hidden layers, width 32 (small for tractable Hessian computation)
  - Hardware: Single NVIDIA Titan V GPU
  - Dataset: Convection (β=1)
  - System: Vary n_res from small to large (subsets of 255×100 grid)
- **Procedure**:
  1. Train model with Adam+L-BFGS for 41000 iterations using varying n_res
  2. Compute ratio λ_1(H_L)/λ_129(H_L) near minimizer w* as lower bound for condition number
  3. Plot this ratio vs. log₂(n_res)
  4. Fit polynomial to check Ω(n_res^α) growth
- **Metrics**: Condition number estimate (λ_1/λ_129), rate of growth with n_res
- **Expected outcome**:
  - Condition number estimate grows polynomially with n_res (at least proportionally)
  - Plot confirms Ω(n_res^α) prediction from Theorem 8.4
- **Baselines**: none
- **Dependencies**: none

## E06: Hessian density for trivial solution analysis
- **Verifies**: C01
- **Setup**:
  - Model: Best MLP from convection and reaction training
  - Hardware: NVIDIA Titan V GPU
  - Dataset: Convection, Reaction
- **Procedure**:
  1. Identify runs where loss ≈ 0 but L2RE ≈ 1
  2. Visualize PINN solution, ground truth, IC/BC fits
  3. Check if solution is a trivial constant (u=0, u=1, etc.)
- **Metrics**: Visual comparison of PINN solution vs. exact solution; IC/BC satisfaction
- **Expected outcome**:
  - PINN solutions with small loss but large L2RE are near-constant functions
  - These satisfy the IC but fail at BC
  - For convection: constant u satisfies residual loss; for reaction: u=0 or u=1 satisfies residual
- **Baselines**: Analytical solutions from Appendix A
- **Dependencies**: E03
