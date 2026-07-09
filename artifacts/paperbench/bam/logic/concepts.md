# Key Concepts

## Score-Based Divergence
- **Notation**: D(q;p) = E_q[||∇log(q/p)||²_{Cov(q)}] = E_q[(∇log q - ∇log p)^T Cov(q) (∇log q - ∇log p)]
- **Definition**: A divergence between distributions q and p measuring agreement of their score functions (gradients of log densities), weighted by the covariance matrix of q. For general q: D(q;p) = E_q[(∇log q - ∇log p)^T Γ_q^{-1} (∇log q - ∇log p)], where Γ_q = E_q[(∇log q)(∇log q)^T]. For Gaussian q = N(ν, Ψ): Γ_q = Ψ^{-1} = [Cov(q)]^{-1}, so D(q;p) = E_q[||∇log(q/p)||²_Ψ].
- **Boundary conditions**: Requires p(z)>0, q(z)>0 for all z ∈ R^D; ∇log p exists and can be evaluated (but p need not be normalized); E_q[||∇log q||²] < ∞.
- **Related concepts**: Fisher Divergence, Weighted Fisher Divergence, KL Divergence, Score Function

## Score Function
- **Notation**: s(z) = ∇_z log p(z) ∈ R^D
- **Definition**: The gradient of the log (unnormalized) target density with respect to the latent variable z. Crucially, s(z) = ∇log p̃(z) for unnormalized p̃ = c·p, since the constant c vanishes in differentiation.
- **Boundary conditions**: Requires log p to be differentiable. Computable via automatic differentiation even when p is intractable.
- **Related concepts**: Score-Based Divergence, Fisher Divergence, BBVI

## BaM Algorithm (Batch and Match)
- **Notation**: Algorithm 1; iterates (μ_t, Σ_t) → (μ_{t+1}, Σ_{t+1})
- **Definition**: An iterative BBVI algorithm alternating between (1) a batch step that draws B samples z_b ~ N(μ_t, Σ_t) and computes sufficient statistics (z̄, ḡ, C, Γ), and (2) a match step that minimizes the regularized empirical score-based divergence L_BaM(q) = D̂_{q_t}(q;p) + (2/λ_t) KL(q_t; q) in closed form.
- **Boundary conditions**: Variational family must be Gaussian; λ_t > 0 required; convergence proof only covers Gaussian targets; finite-batch non-Gaussian convergence is empirical.
- **Related concepts**: Score-Based Divergence, Quadratic Matrix Equation, Stochastic Proximal Point Method

## Quadratic Matrix Equation (BaM covariance update)
- **Notation**: ΣUΣ + Σ = V; solution Σ = 2V[I + (I + 4UV)^{1/2}]^{-1}
- **Definition**: A matrix equation in Σ where U ⪰ 0 and V ≻ 0 are given PSD matrices. The unique symmetric positive-definite solution is given by Lemma B.1. For low-rank U = QQ^T (B << D): Σ = V - V^T Q (2I + (Q^T V Q + I)^{1/2})^{-2} Q^T V, costing O(D²B + B³) instead of O(D³).
- **Boundary conditions**: V must be positive definite; U must be positive semidefinite. Cost O(D³) generally, O(D²B + B³) when B << D.
- **Related concepts**: BaM Algorithm, Match Step

## Batch Step Statistics
- **Notation**: z̄ = (1/B)Σz_b, C = (1/B)Σ(z_b-z̄)(z_b-z̄)^T, ḡ = (1/B)Σg_b, Γ = (1/B)Σ(g_b-ḡ)(g_b-ḡ)^T
- **Definition**: For B samples z_b ~ N(μ_t, Σ_t) with scores g_b = ∇log p(z_b): z̄ and ḡ are sample means; C and Γ are sample covariance matrices of positions and scores. Used to form U = λ_t Γ + (λ_t/(1+λ_t)) ḡḡ^T and V = Σ_t + λ_t C + (λ_t/(1+λ_t))(μ_t - z̄)(μ_t - z̄)^T.
- **Boundary conditions**: By the law of large numbers, as B→∞: z̄→μ_t, C→Σ_t, ḡ→Σ*^{-1}(μ*-μ_t), Γ→Σ*^{-1}Σ_t Σ*^{-1} for Gaussian target.
- **Related concepts**: BaM Algorithm, Batch Step, Quadratic Matrix Equation

## Inverse Regularization Parameter (λ_t)
- **Notation**: λ_t > 0; can be fixed (λ_t = BD for Gaussian) or decaying (λ_t = BD/(t+1) for non-Gaussian)
- **Definition**: Controls trade-off between fitting the empirical score-based divergence and staying close to the current iterate. Small λ → strong regularization (conservative update); large λ → aggressive update. In convergence analysis, δ = λβ/(1+λ) is the per-iteration error decay rate. Unlike SGD learning rates, convergence holds for any fixed λ>0.
- **Boundary conditions**: λ_t > 0 required; λ_t → 0 recovers no update; λ_t → ∞ with B=1 recovers GSM.
- **Related concepts**: BaM Algorithm, Stochastic Proximal Point Method, Convergence Rate

## Normalized Error (Convergence Analysis)
- **Notation**: ε_t = Σ*^{-1/2}(μ_t - μ*) ∈ R^D; Δ_t = Σ*^{-1/2}Σ_t Σ*^{-1/2} - I ∈ R^{D×D}; J_t = Σ*^{-1/2}Σ_t Σ*^{-1/2} = I + Δ_t
- **Definition**: Whitened (Σ*-normalized) errors measuring the distance of the current variational parameters from the target. Convergence theorem shows ||ε_t|| ≤ (1-δ)^t||ε_0|| and ||Δ_t|| ≤ (1-δ)^t||Δ_0|| + t(1-δ)^{t-1}||ε_0||².
- **Boundary conditions**: Valid only in the infinite-batch limit (B→∞) and for Gaussian targets. α = min eigenvalue of J_0 must be positive (Σ_0 ≻ 0).
- **Related concepts**: Convergence Rate, BaM Algorithm

## Affine Invariance
- **Notation**: D(q;p) = D(h#q; h#p) for affine h(z) = Az + b
- **Definition**: A divergence is affine invariant if applying any invertible affine transformation to all distributions leaves the divergence value unchanged. The score-based divergence D(q;p) is affine invariant due to the Cov(q) weighting. The unweighted Fisher divergence E_q[||∇log(q/p)||²] is NOT affine invariant.
- **Boundary conditions**: Requires the weight matrix to transform appropriately under affine maps. Covariance matrix Cov(q) transforms as A Cov(q) A^T, ensuring cancellation (Theorem A.4).
- **Related concepts**: Score-Based Divergence, Fisher Divergence

## Weighted Fisher Divergence
- **Notation**: D_M(q;p) = E_q[||∇log(q/p)||²_M] for fixed M ∈ R^{D×D}
- **Definition**: Generalization of Fisher divergence with fixed weighting matrix M. The score-based divergence of BaM is the special case M = Cov(q) (which depends on q), making it a non-standard weighted Fisher divergence where the weight adapts to the variational distribution.
- **Boundary conditions**: For fixed M, not affine invariant. Only the choice M = Cov(q) yields affine invariance.
- **Related concepts**: Score-Based Divergence, Fisher Divergence, Affine Invariance

## Sinh-Arcsinh Normal Distribution
- **Notation**: z = sinh(τ^{-1} (sinh^{-1}(y) + s)) where y ~ N(μ, Σ)
- **Definition**: A family of non-Gaussian distributions obtained by transforming a Gaussian via the sinh function and its inverse. Parameter s ∈ R controls skewness (s=0 → symmetric), τ>0 controls tail heaviness (τ=1 → Gaussian tails). Used in paper as a controlled test of non-Gaussianity.
- **Boundary conditions**: Recovers standard Gaussian when s=0, τ=1. Used with D=10 dimensional targets.
- **Related concepts**: Non-Gaussian targets, BaM Algorithm
