---
# Algorithm: Forward-Optimization Adaptation (FOA)

## Mathematical Formulation

### ViT Forward Pass
For a plain ViT f_Θ(·) with N layers:
```
E_i = L_i(E_{i-1}),  i = 1, ..., N          (Eq. 1)
ŷ = Head(e^0_N)                               (Eq. 2)
```
where E_i = {e^j_i, j ∈ N, 0 ≤ j ≤ m} are patch embeddings at layer i, e^0_i is the CLS token, m is the number of image patches.

### Prompt Optimization Objective
Find optimal prompt p* that minimizes fitness:
```
p* = arg min_p L(f_Θ(p; x))                  (Eq. 4)
```
where p ∈ R^{d × Np}, Np = number of prompt embeddings, d = embedding dimension.

### Fitness Function (Eq. 5)
```
L(f_Θ(p; X_t)) = Σ_{x∈X_t} Σ_{c∈C} −ŷ_c log ŷ_c
                + λ Σ_{i=1}^{N} [||μ_i(X_t) − μ^S_i||_2 + ||σ_i(X_t) − σ^S_i||_2]
```
where:
- ŷ_c = c-th predicted probability for sample x
- μ_i(X_t), σ_i(X_t) = mean/std of CLS features at layer i over batch X_t
- μ^S_i, σ^S_i = precomputed source statistics at layer i
- λ = 0.4 × BS/64 (ImageNet-C/V2/Sketch); 0.2 × BS/64 (ImageNet-R)

### CMA-ES Sampling (Eq. 6)
```
p^(t)_k ~ m^(t) + τ^(t) N(0, Σ^(t)),  k = 1,...,K
```
where:
- m^(t) ∈ R^{d·Np}: mean vector of search distribution
- τ^(t) ∈ R+: step size (overall standard deviation)
- Σ^(t): covariance matrix (shape of distribution ellipsoid)
- K: population size (default 28)

### Back-to-Source Activation Shifting (Eqs. 7–9)
```
ê^0_N ← e^0_N + γ·d_t                        (Eq. 7)
d_t = μ^S_N − μ_N(t)                          (Eq. 8)
μ_N(t) = α·μ_N(X_t) + (1−α)·μ_N(t−1)        (Eq. 9)
```
where:
- γ = 1.0: step size for activation shifting
- d_t: shifting direction from OOD center to source center
- μ^S_N: mean of final layer CLS features over source samples D_S
- μ_N(t): EMA estimate of test distribution center at step t
- α = 0.1: EMA factor

## Pseudocode (Algorithm 1)

```
Algorithm: Forward-Optimization Adaptation (FOA)

Input:
  - Batches of test samples {X_t}^T_{t=1}
  - Model f_Θ(·) = Head(L_i(·))
  - Source ID statistics {μ^S_i, σ^S_i}^N_{i=0}  [precomputed, frozen]
  - Population size K

Initialization:
  m^(0) = 0,  Σ^(0) = I,  τ^(0) = 1

for t = 1, 2, ..., T do:
  # Step 1: Sample K candidate prompts from CMA distribution
  {p^t_k}^K_{k=1} ~ m^(t) + τ^(t) N(0, Σ^(t))  [Eq. 6]

  for k = 1, ..., K do:
    # Step 2: Forward pass with prompt k
    Compute all layers' CLS features {e^0_n}^N_{n=1}
      using Eq. 1 with input [p^t_k; X_t]

    # Step 3: Activation shifting
    Adjust e^0_N to source domain by Eq. 7

    # Step 4: Predict
    Ŷ^k_t = Head(e^0_N)

    # Step 5: Compute fitness
    v_k = L(f_Θ(p^t_k; X_t))  [Eq. 5]
  end for

  # Step 6: Update CMA distribution
  Update m^(t), Σ^(t), τ^(t) from {v_k}^K_{k=1}
    via CMA-ES algorithm (maximize likelihood of successful candidates)

  # Step 7: Select final prediction
  Ŷ_t = Ŷ^k*_t where k* = argmin_k v_k
end for

Output: Predictions {Ŷ_t}^T_{t=1}
```

## Complexity Analysis

- **Per-batch forward passes**: K (CMA candidates) + 1 (final selection) ≈ K+1 total
  - vs. TENT: 1 forward + 1 backward pass per batch
  - vs. CoTTA: up to 35 augmented forward passes + backward pass
- **Memory**: No backward graph storage; only CMA state (O(d²·Np²)) + feature statistics (O(N·d))
  - FOA (32-bit, BS=64): 832 MB vs. TENT 5,165 MB
- **CMA state dimension**: m^(t) ∈ R^{d·Np} = R^{768×3} = R^{2304} for ViT-Base
  - This is manageable for CMA (vs. full model parameter space of ~86M for ViT-Base)
- **Source statistics computation**: O(Q·N·d) one-time; negligible overhead
