---
# Concepts

## Physics-Informed Neural Network (PINN)
- **Notation**: u(x; w) where w ∈ ℝ^p, x ∈ Ω ⊆ ℝ^d
- **Definition**: A neural network parameterization of the solution to a PDE system D[u(x),x]=0, B[u(x),x]=0, trained by minimizing a least-squares loss combining PDE residual and boundary/initial condition violations: L(w) = (1/2n_res)∑|D[u(x_r^i;w),x_r^i]|² + (1/2n_bc)∑|B[u(x_b^j;w),x_b^j]|²
- **Boundary conditions**: Requires Ω compact, D and B smooth differential/algebraic operators; solution exists in appropriate Sobolev space.
- **Related concepts**: PINN Loss, L2 Relative Error, Interpolation

## PINN Loss
- **Notation**: L(w) = L_res(w) + L_bc(w)
- **Definition**: The sum of mean-squared PDE residual over n_res collocation points and mean-squared boundary/initial condition violation over n_bc points. L(w)=0 iff u(x;w) satisfies PDE and BCs exactly at training points.
- **Boundary conditions**: Interpolation (L=0) is the target; requires sufficiently expressive network.
- **Related concepts**: Physics-Informed Neural Network, PŁ*-Condition

## L2 Relative Error (L2RE)
- **Notation**: L2RE = ||y - y'||₂ / ||y'||₂
- **Definition**: Standard evaluation metric comparing PINN prediction y = (y_i)_{i=1}^n to ground truth y' = (y'_i)_{i=1}^n over a dense evaluation grid. Computed on the full 255×100 interior grid plus IC and BC points.
- **Boundary conditions**: Requires known analytical solution (available for convection, reaction, wave benchmarks).
- **Related concepts**: PINN Loss, Physics-Informed Neural Network

## Hessian Spectral Density
- **Notation**: ρ_H(λ) = (1/p)∑_i δ(λ - λ_i(H_L(w)))
- **Definition**: Approximation to the eigenvalue distribution of the loss Hessian H_L(w) ∈ ℝ^{p×p}. Computed via stochastic Lanczos quadrature (SLQ) using Hessian-vector products. For large p, this is the practical substitute for full diagonalization.
- **Boundary conditions**: SLQ requires symmetric matrix; for preconditioned Hessian H̃_k^T H_L(w) H̃_k, symmetry holds by construction (Appendix C.2).
- **Related concepts**: Condition Number, Ill-Conditioning, L-BFGS Preconditioning

## Condition Number (PŁ* sense)
- **Notation**: κ_L(S) = sup_{w∈S} ||H_L(w)|| / μ where μ is the PŁ* constant
- **Definition**: Ratio of largest Hessian operator norm to PŁ* constant μ over a neighborhood S containing minimizers. Controls convergence rate of gradient descent: O(κ_L(S) · log(1/ε)) iterations to ε-suboptimality.
- **Boundary conditions**: Requires PŁ* condition to hold (valid for wide networks with high probability).
- **Related concepts**: PŁ*-Condition, Hessian Spectral Density, GDND

## PŁ*-Condition (Polyak-Łojasiewicz star)
- **Notation**: ||∇L(w)||² ≥ 2μ·L(w) ∀w ∈ S
- **Definition**: Local condition relating gradient norm to loss value; implies any stationary point in S is a global minimizer. μ is the PŁ* constant (related to smallest singular value of the Jacobian). Known to hold with high probability for sufficiently wide networks.
- **Boundary conditions**: Local (requires S to contain w*); interpolation assumption (L(w*)=0) required.
- **Related concepts**: Condition Number, Interpolation, GDND

## NysNewton-CG (NNCG)
- **Notation**: Algorithm 4; uses RandomizedNyströmApproximation + NyströmPCG + Armijo
- **Definition**: A damped Newton method that computes the Newton step (H_L(w_k)+μI)^{-1}∇L(w_k) via preconditioned conjugate gradient (PCG) using a Nyström approximation of the Hessian as preconditioner, then takes a step using Armijo line search. Exploits fast spectral decay of Hessian.
- **Boundary conditions**: Requires Hessian-vector products (O((n_res+n_bc)p) per step); practical only after Adam+L-BFGS has found good initialization due to high per-iteration cost.
- **Related concepts**: L-BFGS Preconditioning, Armijo Line Search, Nyström Approximation

## Nyström Approximation
- **Notation**: M ≈ V̂Λ̂V̂^T where V̂∈ℝ^{p×s}, Λ̂∈ℝ^{s×s}
- **Definition**: Randomized rank-s approximation of a symmetric PSD matrix M using a sketch Q (random test matrix), computing Y=MQ, then SVD of a small s×s system. Used as preconditioner P in NyströmPCG: P^{-1} = ((λ̂_s+μ)U(Λ̂+μI)^{-1}U^T + (I-UU^T)).
- **Boundary conditions**: Requires M to be (approximately) PSD; effective when M has fast spectral decay; sketch size s ≪ p.
- **Related concepts**: NysNewton-CG, Hessian Spectral Density

## L-BFGS Preconditioning
- **Notation**: w_{k+1} = w_k - η_k H_k ∇L(w_k) where H_k ≈ H_L^{-1}(w_k)
- **Definition**: Limited-memory BFGS updates H_k (approximate inverse Hessian) from m recent (step, gradient-difference) pairs. Equivalent to right-preconditioning: transforms loss to a better-conditioned space. Memory parameter m=100 used.
- **Boundary conditions**: Requires strong Wolfe line search for stability (failure of this leads to early termination, Appendix E.1); effective when H_k approximates H_L^{-1} well.
- **Related concepts**: Condition Number, NysNewton-CG, Adam+L-BFGS

## GDND (Gradient-Damped Newton Descent)
- **Notation**: Algorithm 1: Phase I (GD, K_GD steps), Phase II (damped Newton, K_DN steps with step size η_DN=5/6, damping γ=μ)
- **Definition**: Hybrid theoretical algorithm: Phase I uses gradient descent to escape saddle points and reach a neighborhood of a minimizer; Phase II uses damped Newton (H_L(w)+γI)^{-1}∇L(w) for fast local convergence independent of condition number. Theoretical proxy for Adam+L-BFGS+NNCG.
- **Boundary conditions**: Requires PŁ* condition; Phase II convergence is local (needs good initialization from Phase I); only a fixed K_GD steps are needed before switching.
- **Related concepts**: PŁ*-Condition, Condition Number, NysNewton-CG
