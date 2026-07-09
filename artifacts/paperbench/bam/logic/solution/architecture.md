# System Architecture: Batch and Match (BaM)

## Component Overview

```
Target Distribution p(z)
    │ (score oracle: ∇log p)
    ▼
┌─────────────────────────────────────────┐
│              BaM Algorithm              │
│                                         │
│  ┌───────────────┐   ┌───────────────┐  │
│  │  Batch Step   │──▶│  Match Step   │  │
│  │ (Stochastic)  │   │ (Deterministic│  │
│  └───────────────┘   └───────────────┘  │
│         ▲                   │           │
│         └───────────────────┘           │
│              iterate T times            │
└─────────────────────────────────────────┘
    │
    ▼
Variational parameters (μ_T, Σ_T)
```

## Components

### Component 1: Score Oracle
- **Purpose**: Evaluate target score s(z) = ∇_z log p(z) at given points
- **Inputs**: Latent sample z ∈ R^D
- **Outputs**: Score vector s(z) ∈ R^D
- **Key design choice**: Only requires unnormalized log target; computable via automatic differentiation (JAX). Works for any differentiable probabilistic model.
- **Interactions**: Called B times per iteration by Batch Step

### Component 2: Batch Step
- **Purpose**: Draw samples from current variational approximation and compute sufficient statistics for score-matching objective
- **Inputs**: Current parameters (μ_t, Σ_t), batch size B, score oracle
- **Outputs**: Batch statistics (z̄, ḡ, C, Γ) ∈ R^D × R^D × R^{D×D} × R^{D×D}
- **Key design choice**: Uses samples from q_t (not from p) to estimate the biased divergence D̂_{q_t}(q;p); this is the "batch" in batch-and-match.
- **Computation**:
  - Sample z_1,...,z_B ~ N(μ_t, Σ_t)
  - Compute g_b = ∇log p(z_b) for each b
  - z̄ = (1/B) Σ z_b; ḡ = (1/B) Σ g_b
  - C = (1/B) Σ (z_b - z̄)(z_b - z̄)^T
  - Γ = (1/B) Σ (g_b - ḡ)(g_b - ḡ)^T
- **Interactions**: Calls Score Oracle B times; outputs to Match Step

### Component 3: U/V Matrix Construction
- **Purpose**: Form the matrices U and V for the quadratic matrix equation
- **Inputs**: Batch statistics (z̄, ḡ, C, Γ), current (μ_t, Σ_t), regularization λ_t
- **Outputs**: U ∈ S^D_{+} (PSD), V ∈ S^D_{++} (PD)
- **Formulas**:
  - U = λ_t Γ + (λ_t/(1+λ_t)) ḡḡ^T
  - V = Σ_t + λ_t C + (λ_t/(1+λ_t)) (μ_t - z̄)(μ_t - z̄)^T
- **Key design choice**: U is PSD (rank ≤ D+1 when B < D, due to low-rank structure of Γ and outer product of ḡ). V is PD (inherits positive definiteness from Σ_t).
- **Interactions**: Called by Match Step

### Component 4: Quadratic Matrix Equation Solver
- **Purpose**: Compute the closed-form positive-definite solution to ΣUΣ + Σ = V
- **Inputs**: U ∈ S^D_{+}, V ∈ S^D_{++}
- **Outputs**: Σ_{t+1} = 2V[I + (I + 4UV)^{1/2}]^{-1}
- **Key design choice**: Full-rank solver: O(D³) via matrix square root and inversion. Low-rank solver (Lemma B.3): O(D²B + B³) when U = QQ^T with Q ∈ R^{D×K}, K << D. Low-rank applies when B << D.
- **Interactions**: Core of Match Step; called once per iteration

### Component 5: Mean Update
- **Purpose**: Compute updated variational mean given updated covariance
- **Inputs**: μ_t, Σ_{t+1}, ḡ, z̄, λ_t
- **Outputs**: μ_{t+1} = (λ_t/(1+λ_t)) μ_t + (1/(1+λ_t)) (Σ_{t+1} ḡ + z̄)
- **Key design choice**: Mean update depends on updated covariance Σ_{t+1} (not Σ_t); order matters.
- **Interactions**: Must be called after Quadratic Solver; produces final iterate output

### Component 6: Learning Rate Schedule
- **Purpose**: Set λ_t per iteration based on problem type
- **Inputs**: Iteration t, batch size B, dimension D
- **Outputs**: λ_t > 0
- **Schedules**:
  - Gaussian targets: λ_t = BD (constant)
  - Non-Gaussian/posteriordb: λ_t = BD/(t+1) (decaying)
  - Deep generative (pilot-tuned): B=10 → λ=0.1; B=100 → λ=50; B=300 → λ=7500
- **Interactions**: Called by Match Step at each iteration

## Data Flow Summary

```
t=0: Initialize (μ_0, Σ_0) = (uniform[0,0.1], I)

For t = 0, ..., T-1:
  [Batch Step]:
    z_1,...,z_B ~ N(μ_t, Σ_t)
    g_b = ∇log p(z_b)  [B score evaluations]
    (z̄, ḡ, C, Γ) = sufficient_statistics(z_b, g_b)
    
  [U/V Construction]:
    U = λ_t * Γ + (λ_t/(1+λ_t)) * outer(ḡ, ḡ)
    V = Σ_t + λ_t * C + (λ_t/(1+λ_t)) * outer(μ_t - z̄, μ_t - z̄)
    
  [Match Step - Covariance]:
    Σ_{t+1} = 2V @ inv(I + sqrtm(I + 4*U@V))
    
  [Match Step - Mean]:
    μ_{t+1} = (λ_t/(1+λ_t))*μ_t + (1/(1+λ_t))*(Σ_{t+1}@ḡ + z̄)

Output: (μ_T, Σ_T)
```
