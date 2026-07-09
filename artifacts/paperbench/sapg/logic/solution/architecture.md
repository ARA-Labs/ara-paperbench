---
# System Architecture

## Overview

SAPG is built on top of PPO and introduces a multi-policy framework with a shared backbone and per-policy hanging parameters. The architecture has three main components: the policy network, the critic network, and the data aggregation module.

## Component Graph

```
N = 24,576 Parallel Environments (IsaacGym GPU Simulation)
          |
    Split into M=6 blocks of N/M environments each
          |
    ┌─────┴──────────────────────────────────────────┐
    │                                                 │
  Block 1: N/M envs              Blocks 2..M: N/M envs each
    │                                    │
  Leader Policy π₁               Follower Policies π₂..πM
  [Bθ + ϕ₁]                      [Bθ + ϕⱼ] (shared backbone)
    │                                    │
  Data D₁ (on-policy)             Data D₂..DM (on-policy each)
    │                                    │
    └───────── Importance Sampling ──────┘
                      │
              Subsample D' from ∪D₂..DM
              (|D'| = |D₁| for 50/50 split)
                      │
              Leader Update:
              L = Lon(π₁; D₁) + λ·Loff(π₁; D')
              + Lcritic_on + λ·Lcritic_off
                      │
              Follower j Update:
              L = Lon(πj; Dj) + λent(j-1)·H(πj)
              + Lcritic_on(πj; Dj)
                      │
              Shared gradient update:
              θ ← θ - η∇θL    (backbone actor)
              ψ ← ψ - η∇ψL    (backbone critic)
              ϕj ← ϕj - η∇ϕjLj  (per-policy hanging params)
```

## Components

### 1. Shared Actor Backbone (Bθ)
- **Purpose**: Encodes observations into a latent representation shared across all policies
- **Architecture (AllegroKuka)**: MLP with hidden dims 768×512×256 + ELU activation, feeding into a single-layer LSTM with 768 hidden units
- **Architecture (ShadowHand)**: MLP with hidden dims 512×512×256×128 + ELU activation
- **Architecture (AllegroHand)**: MLP with hidden dims 512×256×128 + ELU activation
- **Inputs**: Observation vector ot = [q, q̇, xt, vt, ωt, gt, zt] (AllegroKuka); [q, q̇, xt, vt, ωt] (easy tasks)
- **Outputs**: Latent state + conditioning on ϕj → action distribution mean
- **Key design choice**: Shared parameters ensure followers benefit from leader's learning; per-policy ϕj provides diversity

### 2. Per-Policy Hanging Parameters (ϕj)
- **Purpose**: Provide each policy a unique "identity" that differentiates its behavior while sharing the backbone
- **Dimension**: ϕj ∈ R32 for AllegroKuka tasks; ϕj ∈ R16 for ShadowHand/AllegroHand tasks
- **Update rule**: Only updated by policy j's own objective gradient
- **Inputs**: Concatenated with or injected into the backbone output
- **Key design choice**: Prevents full convergence of policies while enabling shared representation

### 3. Per-Policy Action Sigma (σj)
- **Purpose**: Learnable standard deviation for each policy's Gaussian action distribution
- **Implementation**: For AllegroKuka standard runs: single learnable vector independent of observation. For entropy regularization runs: per-block learnable sigma vector, enabling different entropy levels per follower.
- **Key design choice**: Separate sigmas allow different explore-exploit trade-offs across followers

### 4. Shared Critic Backbone (Cψ)
- **Purpose**: Estimates value function V(s) for advantage computation
- **Architecture**: Same backbone structure as actor, also conditioned on ϕj
- **Inputs**: State observation; per-policy ϕj
- **Outputs**: Scalar value estimate Vπj(s)
- **Update rule**: ψ updated by all policy objectives; ϕj used in critic is the same as actor

### 5. Data Aggregation Module
- **Purpose**: Collects data from all followers and subsamples for the leader's off-policy update
- **Operation**: After each rollout phase, collects D₁…DM; subsamples |D₁| transitions from ∪D₂..DM to form D' (equal on/off split); computes importance weights μ = πi,old/πj
- **Key design choice**: Equal 50/50 split prevents off-policy noise from overwhelming on-policy gradient

### 6. IsaacGym Environment Interface
- **Purpose**: GPU-accelerated simulation of 24,576 parallel instances
- **Tasks**: AllegroKuka (Allegro 16 DoF + Kuka 7 DoF = 23 DoF total), ShadowHand (24 DoF), AllegroHand (16 DoF)
- **Observation space**: q, q̇ ∈ R²³ (joint angles/velocities), xt ∈ R⁷ (object pose), vt (linear vel), ωt (angular vel), gt (goal), zt (auxiliary)
