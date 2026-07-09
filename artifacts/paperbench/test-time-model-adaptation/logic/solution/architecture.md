---
# System Architecture: Forward-Optimization Adaptation (FOA)

## Component Graph

```
[Test Batch X_t] ──→ [Prompt Sampler (CMA-ES)] ──→ [Prompt Embeddings {p^(t)_k}^K_{k=1}]
                                                              │
[Source Statistics {μ^S_i, σ^S_i}^N_{i=0}] ─────────→ [Fitness Calculator] ←── [ViT Forward Pass]
        (precomputed once)                                    │
                                                    [CMA Distribution Update]
                                                    (m^(t), Σ^(t), τ^(t))
                                                              │
                                                    [Select Best Prompt p*]
                                                              │
[Test Batch X_t] + [p*] ──→ [ViT Forward Pass] ──→ [CLS Feature e^0_N]
                                                              │
[EMA Statistics μ_N(t)] ←───────────────────────────────────┘
        │
[Activation Shifter] ──→ [ê^0_N = e^0_N + γ·d_t] ──→ [MLP Head] ──→ [Prediction Ŷ_t]
```

## Components

### 1. Source Statistics Computer (One-Time, Pre-TTA)
- **Purpose**: Compute and store per-layer CLS token mean and standard deviation from source in-distribution data
- **Inputs**: Source samples D_S = {x_q}^Q_{q=1} (Q ≥ 32 unlabeled ImageNet-1K validation images), frozen ViT-Base
- **Outputs**: {μ^S_i, σ^S_i}^N_{i=0} stored in memory (one-time computation)
- **Key design choice**: Computed without prompt insertion; only needs Q=32 samples for ImageNet
- **Interacts with**: Fitness Calculator, Activation Shifter

### 2. Prompt Sampler / CMA-ES Optimizer
- **Purpose**: Maintain and update a multivariate normal distribution over prompt space; sample K candidate prompts per batch
- **Inputs**: Current CMA state (m^(t), Σ^(t), τ^(t)); fitness values {v_k}^K_{k=1}
- **Outputs**: K candidate prompts {p^(t)_k}^K_{k=1}; updated CMA state
- **Key design choice**: CMA-ES (pycma library) preferred over SGD because it is derivative-free; population size K=28 by default; prompts p ∈ R^{d × Np} with Np=3, d=768 for ViT-Base
- **Interacts with**: ViT Model, Fitness Calculator

### 3. ViT Model (Frozen)
- **Purpose**: Transform prompt-augmented input embeddings through N transformer layers; produce CLS token features and predictions
- **Inputs**: [p^(t)_k; X_t embeddings] — prompt concatenated with patch embeddings
- **Outputs**: CLS token features {e^0_i}^N_{i=1} at each layer; prediction probabilities ŷ
- **Key design choice**: All model weights are FROZEN — no gradient computation required; compatible with quantized (8-bit, 6-bit) or hard-coded models
- **Interacts with**: Prompt Sampler, Fitness Calculator, Activation Shifter

### 4. Fitness Calculator
- **Purpose**: Score each candidate prompt via the unsupervised fitness function combining entropy and activation discrepancy
- **Inputs**: Prediction probabilities {ŷ_k}, CLS features {e^0_{i,k}} for each candidate k; source statistics {μ^S_i, σ^S_i}^N_{i=0}
- **Outputs**: Fitness value v_k for each candidate prompt k (lower = better)
- **Formula**: v_k = Σ_{x∈X_t} Σ_c −ŷ_c log ŷ_c + λ Σ_{i=1}^{N} [||μ_i(X_t) − μ^S_i||_2 + ||σ_i(X_t) − σ^S_i||_2]
- **Interacts with**: ViT Model, Prompt Sampler

### 5. Back-to-Source Activation Shifter
- **Purpose**: Directly shift final-layer CLS features from OOD domain toward source domain without backpropagation
- **Inputs**: CLS feature e^0_N from final ViT layer; source statistics μ^S_N; running EMA estimate μ_N(t)
- **Outputs**: Shifted feature ê^0_N = e^0_N + γ·d_t where d_t = μ^S_N − μ_N(t)
- **Key design choice**: EMA update μ_N(t) = α·μ_N(X_t) + (1−α)·μ_N(t−1) with α=0.1 enables stable single-sample operation; γ=1.0 for exact center alignment
- **Interacts with**: ViT Model, MLP Head

### 6. MLP Head (Frozen)
- **Purpose**: Map shifted CLS feature to class probabilities
- **Inputs**: Shifted CLS feature ê^0_N
- **Outputs**: Final prediction probabilities Ŷ_t
- **Interacts with**: Activation Shifter

## Data Flow Summary

**Initialization** (one-time before TTA):
1. Feed Q source samples through frozen ViT → compute {μ^S_i, σ^S_i}^N_{i=0}
2. Initialize CMA: m^(0) = 0, Σ^(0) = I, τ^(0) = 1

**Per-batch adaptation** (online, for each test batch X_t):
1. Sample K prompts from CMA distribution
2. For each of K candidates: forward pass [p_k; X_t] → compute fitness v_k
3. Update CMA distribution using {v_k}^K_{k=1}
4. Select best prompt (lowest v_k)
5. Forward pass with best prompt → e^0_N
6. Update EMA: μ_N(t) = α·μ_N(X_t) + (1−α)·μ_N(t−1)
7. Compute shifting direction d_t = μ^S_N − μ_N(t)
8. Shift: ê^0_N = e^0_N + γ·d_t
9. Predict: Ŷ_t = Head(ê^0_N)
