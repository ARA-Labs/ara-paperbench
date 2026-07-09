# Algorithm: Batch and Match Variational Inference

## Mathematical Formulation

### Score-Based Divergence
$$D(q; p) = \mathbb{E}_{q}\left[\left\|\nabla_z \log \frac{q(z)}{p(z)}\right\|^2_{\text{Cov}(q)}\right]$$

For Gaussian q = N(ν, Ψ), this simplifies to:
$$D(q; p) = \text{tr}(\Gamma\Psi) + \text{tr}(C\Psi^{-1}) + \left\|\mu - \bar{z} - \Psi\bar{g}\right\|^2_{\Psi^{-1}} + \text{const}$$

where statistics are computed over batch samples.

### BaM Objective (Match Step)
$$\mathcal{L}_{\text{BaM}}(q) = \hat{D}_{q_t}(q; p) + \frac{2}{\lambda_t} \text{KL}(q_t; q)$$

where $\hat{D}_{q_t}(q;p)$ is the empirical score-based divergence estimated with samples from $q_t$.

### U and V Matrices
$$U = \lambda_t \Gamma + \frac{\lambda_t}{1+\lambda_t} \bar{g}\bar{g}^\top \quad (\text{PSD})$$
$$V = \Sigma_t + \lambda_t C + \frac{\lambda_t}{1+\lambda_t}(\mu_t - \bar{z})(\mu_t - \bar{z})^\top \quad (\text{PD})$$

### Quadratic Matrix Equation (Covariance Update)
$$\Sigma_{t+1} U \Sigma_{t+1} + \Sigma_{t+1} = V$$

**Closed-form solution** (Lemma B.1):
$$\Sigma_{t+1} = 2V \left[I + \left(I + 4UV\right)^{1/2}\right]^{-1}$$

**Low-rank solution** when $U = QQ^\top$, $Q \in \mathbb{R}^{D \times K}$ (Lemma B.3):
$$\Sigma_{t+1} = V - V^\top Q \left(2I + \left(Q^\top V Q + I\right)^{1/2}\right)^{-2} Q^\top V$$

### Mean Update
$$\mu_{t+1} = \frac{\lambda_t}{1+\lambda_t} \mu_t + \frac{1}{1+\lambda_t}\left(\Sigma_{t+1} \bar{g} + \bar{z}\right)$$

**Important**: Must be computed AFTER Σ_{t+1}.

## Pseudocode

```
Algorithm 1: Batch and Match VI
Input: T (iterations), B (batch size), λ_t (inverse regularization),
       s = ∇log p (score function), μ_0 ∈ R^D, Σ_0 ∈ S^D_{++}

for t = 0, ..., T-1:
  // Batch Step
  Sample z_b ~ N(μ_t, Σ_t) for b = 1, ..., B
  Compute g_b = s(z_b) for b = 1, ..., B
  
  z̄ = (1/B) Σ_b z_b
  C = (1/B) Σ_b (z_b - z̄)(z_b - z̄)^T
  ḡ = (1/B) Σ_b g_b
  Γ = (1/B) Σ_b (g_b - ḡ)(g_b - ḡ)^T
  
  // Compute U and V
  U = λ_t * Γ + (λ_t / (1+λ_t)) * outer(ḡ, ḡ)
  V = Σ_t + λ_t * C + (λ_t / (1+λ_t)) * outer(μ_t - z̄, μ_t - z̄)
  
  // Match Step: Covariance Update
  Σ_{t+1} = 2V @ inv(I + sqrtm(I + 4 * U @ V))
  
  // Match Step: Mean Update
  μ_{t+1} = (λ_t/(1+λ_t)) * μ_t + (1/(1+λ_t)) * (Σ_{t+1} @ ḡ + z̄)

Output: μ_T, Σ_T
```

## Convergence Analysis (Gaussian Target, Infinite Batch)

**Setup**: p = N(μ*, Σ*), B → ∞, fixed λ > 0.

**Normalized errors**:
- ε_t = Σ*^{-1/2}(μ_t - μ*) ∈ R^D
- Δ_t = Σ*^{-1/2}Σ_t Σ*^{-1/2} - I ∈ R^{D×D}

**Theorem 3.1** (Exponential Convergence):
Let α = min eigenvalue of Σ*^{-1/2}Σ_0 Σ*^{-1/2}. Define:
- β = min(α, (1+λ)/(1+λ+||ε_0||²)) ∈ (0,1]
- δ = λβ/(1+λ) ∈ (0,1)

Then for all t ≥ 0:
$$\|\varepsilon_t\| \leq (1-\delta)^t \|\varepsilon_0\|$$
$$\|\Delta_t\| \leq (1-\delta)^t \|\Delta_0\| + t(1-\delta)^{t-1}\|\varepsilon_0\|^2$$

**Key property**: Holds for ANY λ > 0 and ANY initialization (μ_0, Σ_0 ≻ 0). No requirement that λ scale with problem eigenvalues (unlike gradient methods).

**Corollary D.5** (One-step convergence): With B → ∞ then λ_0 → ∞: BaM converges exactly in one step.

## Complexity Analysis

| Operation | Cost | Notes |
|-----------|------|-------|
| Batch step (B score evaluations) | O(B · cost_of_score) | Parallelizable |
| Batch statistics (z̄, ḡ, C, Γ) | O(BD²) | Matrix outer products |
| U, V construction | O(D²) | |
| Full-rank covariance update | O(D³) | Matrix square root + inverse |
| Low-rank covariance update | O(D²B + B³) | When B << D via Lemma B.3 |
| Mean update | O(D²) | Matrix-vector product |

**Total per iteration**: O(D³) general; O(D²B + B³) when B << D (low-rank regime).

Note: Per Appendix E.2, gradient evaluations dominate for lower-dimensional settings (D ≤ 64). For D = 256, low-rank BaM and full-rank BaM have similar wallclock times.
