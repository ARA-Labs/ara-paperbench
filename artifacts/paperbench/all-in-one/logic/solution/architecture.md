---
# System Architecture

## Overview

The Simformer is a score-based diffusion model that uses a transformer architecture to learn the joint distribution p(θ, x) and estimate the scores needed to sample arbitrary conditional distributions. The system consists of four main components: the Tokenizer, the Transformer Score Model, the Training Loop (denoising score-matching), and the Sampling Engine (reverse SDE + optional guided diffusion).

## Component Graph

```
Simulator
    │
    ▼
(θ, x) pairs ──────────────────────────────────────────────┐
                                                            │
                    ┌───────────────────────┐               │
                    │      Tokenizer        │               │
                    │  - ID embedding       │               │
                    │  - Value embedding    │◄──────────────┘
                    │  - Metadata embedding │ (for fn-valued params)
                    │  - Condition state    │
                    └──────────┬────────────┘
                               │  [tokens: (d × token_dim)]
                               ▼
                ┌──────────────────────────────────┐
                │   Transformer Score Model         │
                │   - N layers (6 default, 8 LV/HH)│
                │   - 4 heads, attention size 10    │
                │   - Token dim: 50                 │
                │   - FF hidden dim: 150            │
                │   - Diffusion time: 128-dim RGFE  │
                │   + Attention Mask M_E            │
                └──────────────┬───────────────────┘
                               │  [scores: d scalars]
                               ▼
              ┌────────────────────────────────────────┐
              │         Training / Sampling             │
              │                                        │
              │  Training: Denoising Score-Matching    │
              │  - Random M_C (5 mask distributions)   │
              │  - Add noise to unobserved vars        │
              │  - MSE loss on unobserved scores only  │
              │                                        │
              │  Sampling: Reverse SDE                 │
              │  - Euler-Maruyama, 500 steps default   │
              │  - Observed vars: kept constant        │
              │  - Unobserved vars: reverse diffused   │
              │  + Optional: Guided Diffusion (Alg. 1) │
              └────────────────────────────────────────┘
```

## Component Descriptions

### Tokenizer
- **Purpose**: Convert each variable in (θ, x) to a fixed-size token vector
- **Inputs**: Scalar values, integer variable IDs, condition mask M_C, optional metadata (index set for function-valued params)
- **Outputs**: Sequence of d tokens, each of dimension token_dim=50
- **Implementation**:
  - ID embedding: learnable embedding table, one vector per unique variable ID
  - Value embedding: scalar value repeated token_dim times → vector [v, v, ..., v]
  - Metadata embedding (optional): random Fourier embedding of index set → learnable linear projection → d-dim vector (128-dim RFE for time indices)
  - Condition state embedding: if observed → learnable vector; if unobserved → zero vector
  - Final token: concatenation of [id_emb; value_emb; metadata_emb; cond_emb] → projected to token_dim

### Transformer Score Model
- **Purpose**: Process the sequence of tokens and output one scalar score per variable, representing the score of the diffusion process at noise level t
- **Inputs**: Token sequence (d × token_dim), diffusion time t, attention mask M_E
- **Outputs**: d scalar scores (one per variable)
- **Key design choices**:
  - Standard encoder-only transformer (Vaswani et al., 2017) with modifications
  - Diffusion time t embedded via 128-dim random Gaussian Fourier embedding → linear projection → added to each feed-forward block output
  - Output head: single linear layer projecting each token to 1 scalar
  - Attention mask M_E controls which tokens attend to which (encodes simulator dependency structure)

### Attention Mask (M_E)
- **Purpose**: Encode known dependency structure of the simulator
- **Types**:
  - Dense: every token attends to every other token (full matrix of ones)
  - Undirected: symmetric adjacency matrix of undirected graphical model + diagonal
  - Directed: adjacency matrix of DAG + diagonal; dynamically updated per condition mask using Webb et al. (2018) algorithm
- **Inputs**: Graphical model structure, current condition mask M_C (for directed case)
- **Outputs**: Binary (d × d) mask

### Training Loop
- **Purpose**: Train the score model via denoising score-matching
- **Inputs**: Simulator samples (θ, x), SDE parameters (σ_max, σ_min for VESDE)
- **Procedure per step**:
  1. Sample (θ, x) batch from simulator (batch size 1000)
  2. Sample condition mask M_C from one of 5 distributions
  3. Sample noise level t ∼ Uniform(1e-5, 1)
  4. Add noise to unobserved variables: x̂_t^MC = (1−MC)·x̂_t + MC·x̂_0
  5. Compute loss on unobserved variables only; update with Adam optimizer

### Sampling Engine (Reverse SDE)
- **Purpose**: Generate samples from any desired conditional distribution
- **Inputs**: Trained score model, observation values + condition mask M_C, SDE parameters
- **Procedure**:
  1. Initialize unobserved variables from terminal noise distribution p_T
  2. Run Euler-Maruyama reverse SDE for 500 steps (default)
  3. Keep observed variables fixed at their conditioning values throughout
  4. Optional: modify score with guided diffusion for interval constraints

### Guided Diffusion Module (Algorithm 1)
- **Purpose**: Enable conditioning on soft constraints and intervals
- **Inputs**: Constraint function c(x̂) ≤ 0, scaling function s(t)=1/σ(t)², self-recurrence steps r
- **Score modification**: s̃(x̂_t,t) = s_φ(x̂_t,t) + ∇_x̂_t log σ(−s(t)·c(x̂_0~))
  where x̂_0~ = (x̂_{t+1} + σ(t+1)²·s) / μ(t+1) is the denoised estimate
- **Self-recurrence**: After each step, optionally re-noise the future point and re-run (r times); improves accuracy at r× computational cost
