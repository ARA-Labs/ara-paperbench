# Problem Specification

## Observations

### O1: ELBO-based BBVI suffers from high-variance gradients
- **Statement**: Gradient estimates of the ELBO via the reparameterization trick are stochastic, leading to high variance particularly in high-dimensional settings and when using richer (full-covariance) variational families.
- **Evidence**: Section 1, §2.1; Dhaka et al. (2020, 2021) cited for empirical evidence; Figure 5.1 shows ADVI converges orders of magnitude slower than BaM.
- **Implication**: BBVI based on ELBO requires many iterations to converge and is sensitive to learning rate choices.

### O2: ELBO-based BBVI is sensitive to hyperparameters
- **Statement**: ADVI and related ELBO-based methods require careful tuning of learning rates; the score-based divergence variant is even more sensitive (different learning rates selected for each dimension: [0.01, 0.005, 0.001, 0.001] for D=4, 16, 64, 256).
- **Evidence**: Section 5.1, Appendix E.3; Dhaka et al. (2020, 2021).
- **Implication**: Practitioners must run grid searches over learning rates, adding computational overhead and brittleness.

### O3: GSM lacks a principled objective and requires heuristics for non-Gaussian targets
- **Statement**: GSM (Modi et al., 2023) solves score-matching equations exactly per sample but has no proper divergence, causing divergence (oscillation or instability) for highly non-Gaussian targets (e.g., s=1.8 sinh-arcsinh). GSM batch updates use ad hoc averaging.
- **Evidence**: Section 4; Figure 5.2 (reverse KL diverges for GSM at s=1.8).
- **Implication**: A principled score-based divergence with regularization is needed.

### O4: Full-covariance Gaussian VI is computationally tractable but underutilized
- **Statement**: Using full-covariance Gaussian approximations requires estimating O(D²) parameters but can provide better compression. Standard mean-field families miss correlations between latent variables.
- **Evidence**: Section 5.3; deep generative model experiment: BaM/ADVI with full covariance outperform AVI (factorized Gaussian).
- **Implication**: Methods that efficiently optimize full-covariance Gaussian families are desirable.

## Gaps

### G1: No affine-invariant, unnormalized-computable divergence for BBVI
- **Statement**: The KL divergence requires normalization constants; the Fisher divergence is not affine invariant; the weighted Fisher divergence with fixed M is not adapted to the variational family.
- **Caused by**: O1, O2, O3
- **Existing attempts**: KL divergence (ELBO), Fisher divergence, weighted Fisher divergence (Barp et al., 2019)
- **Why they fail**: KL requires normalized density; Fisher divergence lacks affine invariance (Theorem A.4); no method simultaneously has all three: unnormalized evaluation, affine invariance, closed-form optimization.

### G2: No BBVI algorithm with closed-form, non-gradient updates for full-covariance Gaussians with provable convergence
- **Statement**: Existing proximal BBVI methods either linearize (Khan et al., 2015, 2016) or cannot solve their proximal steps in closed form (Lambert et al., 2022). GSM solves updates exactly but without regularization, losing stability.
- **Caused by**: O1, O2, O3
- **Existing attempts**: GSM, KL-proximal BBVI (Theis & Hoffman, 2015), SPP methods
- **Why they fail**: Linearization introduces approximation error; no provable convergence for non-Gaussian targets; GSM is unstable without regularization.

## Key Insight

- **Insight**: Choosing the covariance matrix Cov(q) as the weight matrix in the weighted Fisher divergence yields an affine-invariant score-based divergence D(q;p) = E_q[||∇log(q/p)||²_{Cov(q)}] that admits a global closed-form minimum when combined with a KL-divergence regularizer, because the resulting stationarity condition is a quadratic matrix equation with a known positive-definite solution.
- **Derived from**: O1, O2, O3, O4
- **Enables**: A stochastic proximal point algorithm (BaM) with provably convergent, closed-form, non-gradient updates that are stable for any regularization strength λ>0.

## Assumptions

- A1: The log target density log p(z) is differentiable and its gradient ∇log p(z) can be efficiently evaluated (score oracle is available).
- A2: The target distribution p has positive density everywhere on R^D.
- A3: The variational family is Q = {N(μ, Σ) : μ ∈ R^D, Σ ∈ S^D_{++}}.
- A4: Gradient evaluations dominate computational cost (valid for lower-dimensional settings per Appendix E.2).
- A5: For deep generative models, the neural network parameters θ̂ are fixed (pre-trained) before running VI.
