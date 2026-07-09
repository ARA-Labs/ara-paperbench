# Claims

## C01: Score-based divergence properties
- **Statement**: The score-based divergence D(q;p) = E_q[||∇log(q/p)||²_{Cov(q)}] satisfies (i) non-negativity with equality iff p=q, (ii) affine invariance under coordinate transformations, and (iii) evaluability for unnormalized target densities (depends only on ∇log p, not the partition function).
- **Status**: supported
- **Falsification criteria**: Construct a pair (p,q) with p≠q where D(q;p)=0; or find an affine transformation h where D(q;p)≠D(h#q;h#p); or show the divergence requires normalization of p.
- **Proof**: [E01, E02]
- **Dependencies**: none
- **Tags**: score-based divergence, affine invariance, non-negativity, black-box VI

## C02: Closed-form BaM updates
- **Statement**: The BaM objective L_BaM(q) = D̂_{q_t}(q;p) + (2/λ_t) KL(q_t; q) has a unique global minimum in the Gaussian family Q that can be computed in closed form: Σ_{t+1} = 2V[I + (I + 4UV)^{1/2}]^{-1} and μ_{t+1} = (λ_t/(1+λ_t)) μ_t + (1/(1+λ_t))(Σ_{t+1}ḡ + z̄), where U and V are PSD matrices derived from batch statistics.
- **Status**: supported
- **Falsification criteria**: Find an input (U≥0, V>0) for which the stated formula does not satisfy the quadratic equation ΣUΣ + Σ = V; or show the solution is not positive definite.
- **Proof**: [E01, E02, E03, E04]
- **Dependencies**: C01
- **Tags**: closed-form update, quadratic matrix equation, proximal point, Gaussian variational family

## C03: BaM recovers GSM as a special case
- **Statement**: In the limit B=1 and λ_t → ∞, the BaM updates reduce exactly to the Gaussian Score Matching (GSM) updates of Modi et al. (2023): Σ_{t+1}g_t g_t^T Σ_{t+1} + Σ_{t+1} = Σ_t + (μ_t - z_t)(μ_t - z_t)^T and μ_{t+1} = Σ_{t+1}g_t + z_t.
- **Status**: supported
- **Falsification criteria**: Show that the B=1, λ→∞ limit of BaM updates differs from Equations (42) and (23) of Modi et al. (2023).
- **Proof**: [E01]
- **Dependencies**: C02
- **Tags**: GSM, special case, limiting behavior, B=1

## C04: Exponential convergence for Gaussian targets
- **Statement**: For Gaussian target p = N(μ*, Σ*) in the infinite-batch limit (B→∞) with fixed λ>0, the normalized errors ε_t = Σ*^{-1/2}(μ_t - μ*) and Δ_t = Σ*^{-1/2}Σ_t Σ*^{-1/2} - I satisfy: ||ε_t|| ≤ (1-δ)^t ||ε_0|| and ||Δ_t|| ≤ (1-δ)^t ||Δ_0|| + t(1-δ)^{t-1}||ε_0||², where β = min(α, (1+λ)/(1+λ+||ε_0||²)), δ = λβ/(1+λ), and α is the minimum eigenvalue of Σ*^{-1/2}Σ_0 Σ*^{-1/2}.
- **Status**: supported
- **Falsification criteria**: Construct a Gaussian target and initial conditions where the stated error bounds are violated in the infinite-batch limit.
- **Proof**: [E01]
- **Dependencies**: C02
- **Tags**: convergence, exponential decay, Gaussian target, proximal stability, learning rate robustness

## C05: BaM outperforms ADVI on convergence speed
- **Statement**: BaM with appropriately chosen batch size converges to lower KL divergence (or lower relative mean error) in fewer gradient evaluations than ADVI on Gaussian targets, non-Gaussian sinh-arcsinh targets, hierarchical Bayesian models from PosteriorDB, and deep generative models (CIFAR-10 with D=256).
- **Status**: supported
- **Falsification criteria**: Find a benchmark where ADVI achieves equal or lower KL/MSE at the same or fewer gradient evaluations than BaM.
- **Proof**: [E01, E02, E03, E04]
- **Dependencies**: C02, C04
- **Tags**: empirical comparison, ADVI, convergence speed, gradient evaluations

## C06: BaM benefits from larger batch sizes; ADVI and GSM do not
- **Statement**: For BaM, increasing the batch size B improves convergence speed and stability (e.g., larger B=15,40,150 for D=16,64,256 converge faster than B=2). For ADVI and GSM, increasing batch size yields marginal or no improvement.
- **Status**: supported
- **Falsification criteria**: Show that ADVI or GSM achieves substantially faster convergence with larger batch sizes, or that BaM does not benefit from batch size increases.
- **Proof**: [E01, E02, E03, E04]
- **Dependencies**: C05
- **Tags**: batch size, parallelization, scalability, deep generative
