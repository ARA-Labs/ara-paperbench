---
# Algorithm Specification

## 1. NysNewton-CG (NNCG) — Algorithm 4

### Mathematical Formulation

At each iteration k, NNCG solves:
```
(H_L(w_k) + μI) d_k = ∇L(w_k)
```
using preconditioned CG with the Nyström preconditioner, then takes:
```
w_{k+1} = w_k - η_k d_k
```
where η_k satisfies Armijo condition: L(w_k - η_k d_k) ≤ L(w_k) - α η_k (∇L(w_k)^T d_k).

### Nyström Preconditioner (Algorithm 5)
Given symmetric H ∈ ℝ^{p×p} and sketch size s:
1. Draw S = randn(p, s), orthogonalize: Q = qr_econ(S)
2. Compute sketch: Y = HQ
3. Shift for stability: ν = √p · eps(||Y||₂), Y_ν = Y + νQ
4. Cholesky: C = chol(Q^T Y_ν), then B = Y C^{-1}
5. Thin SVD: [V̂, Σ, ~] = svd(B, 0); Λ̂ = max{0, Σ² - νI}
6. **Output**: V̂ ∈ ℝ^{p×s}, Λ̂ ∈ ℝ^{s×s}

The preconditioner and its inverse are:
```
P = (λ̂_s + μ) V̂(Λ̂ + μI)V̂^T + (I - V̂V̂^T)
P^{-1} = (λ̂_s + μ) V̂(Λ̂ + μI)^{-1}V̂^T + (I - V̂V̂^T)
```

### NyströmPCG (Algorithm 6)
Solve (A + μI)x = b where A = H_L(w):
- Standard PCG loop using P^{-1} as preconditioner
- Termination: ||r||₂ < ε or k > M iterations

### Armijo Line Search (Algorithm 7)
Starting from t = η, while L(w - td) > L(w) - α·t·(∇L^T d): t ← β·t

### Pseudocode (NNCG main loop)
```
Initialize: d_{-1} = 0
for k = 0,...,K-1:
  if k mod F == 0:
    [U, Λ̂] = RandomizedNyströmApproximation(H_L(w_k), s)
  d_k = NyströmPCG(H_L(w_k), ∇L(w_k), d_{k-1}, U, Λ̂, s, μ, ε, M)
  η_k = Armijo(L, w_k, ∇L(w_k), -d_k, η)
  w_{k+1} = w_k - η_k · d_k
return w_K
```

### Complexity
- Hessian-vector product: O((n_res + n_bc)p) per product (Pearlmutter 1994)
- NyströmPCG per iteration: O(sp + CG_iters × p) 
- Preconditioner update (every F steps): O(s · HVP_cost)
- NNCG per step: O((n_res + n_bc) · p) — dominates for large n_res

### Per-Iteration Timing (measured)
| PDE | L-BFGS | NNCG | Ratio |
|-----|--------|------|-------|
| Convection | 4.6e-2 s | 2.5e-1 s | 5.43× |
| Reaction | 3.6e-2 s | 7.2e-1 s | 20× |
| Wave | 9.0e-2 s | 2.9e1 s | 322× |
Note: Wave involves second derivatives, requiring more HVP computation.

---

## 2. GDND (Gradient-Damped Newton Descent) — Algorithm 1

### Mathematical Formulation (Theoretical Algorithm)

**Phase I** (GD, K_GD steps, step size η_GD = 1/β_L):
```
w_{k+1} = w_k - η_GD ∇L(w_k)
```

**Phase II** (Damped Newton, K_DN steps, step size η_DN = 5/6, damping γ = μ):
```
w̃_{k+1} = w̃_k - η_DN (H_L(w̃_k) + γI)^{-1} ∇L(w̃_k)
```

### Theoretical Guarantees (Theorem 8.5)

Under PŁ*-condition with constant μ over a ball around w₀:
- Phase I with K_GD = (β_L/μ) log(4·max{2β_L,1}·L(w₀)/(μρ²)) iterations outputs w_loc in an ε_loc-neighborhood of a minimizer.
- Phase II then satisfies: L(w̃_k) ≤ (1 - 1/(2(1+ε)²))^k L(w_loc)

**Key**: Phase II convergence rate is independent of the condition number κ_L(S).

After K_DN ≥ 3 log(L(w_loc)/ε) iterations: L(w̃_{K_DN}) ≤ ε.

---

## 3. L-BFGS Preconditioned Hessian (Algorithms 2 & 3)

### Purpose
Compute spectral density of the preconditioned Hessian H̃_k^T H_L H̃_k where H_k = H̃_k H̃_k^T ≈ H_L^{-1}.

### L-BFGS Unrolling (Algorithm 2)
Given stored {y_i, s_i, ρ_i}^{k-1}_{i=k-m}:
1. ỹ_{k-1} = ρ_{k-1} y_{k-1}; ṽ_{k-1} = s_{k-1}; s̃_{k-1} = √ρ_{k-1} s_{k-1}
2. For i = k-2,...,k-m: compute ỹ_i, ṽ_i, s̃_i via recursive formula
3. Forms matrices Ỹ, Ṡ, Ṽ ∈ ℝ^{p×m}

### Matrix-Vector Product with Preconditioned Matrix (Algorithm 3)
To compute v̂ = H̃_k^T H_L H̃_k v:
1. Split v into (v₁, v₂) of sizes (p, m)
2. v' = √γ(v₁ - Ṽ Ỹ^T v₁) + Ṡv₂
3. v'' = H_L v' (HVP)
4. v''' = stack(√γ(v'' - Ỹ Ṽ^T v''), Ṡ^T v'')

Then apply SLQ to H̃_k^T H_L H̃_k using Algorithm 3 as matrix-vector product routine.
