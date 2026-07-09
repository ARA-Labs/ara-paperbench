# System Architecture: Knowledge-Retention-Augmented RL Fine-tuning

## Overview

The system augments standard RL fine-tuning with an auxiliary retention loss applied only to the actor (policy) network. The architecture is modular: any base RL algorithm (APPO, PPO+RND, SAC) can be used, with the retention module added as an additional loss term.

## Component Graph

```
┌─────────────────────────────────────────────────────────────┐
│                Pre-training Phase                            │
│  ┌──────────────┐     Behavioral Cloning      ┌──────────┐  │
│  │  Expert Data │ ─────────────────────────→  │  π* (θ*)  │  │
│  │  (NLD-AA /   │                             │  Actor   │  │
│  │  PPO agent / │                             │  Critic  │  │
│  │  SAC agent)  │                             └──────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                         Initialize θ ← θ*
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                Fine-tuning Phase                             │
│                                                              │
│  ┌──────────┐  rl_loss   ┌───────────────────────────────┐  │
│  │ RL Env   │──────────→ │         Total Loss             │  │
│  │(NetHack/ │  (PPO/     │  L = L_RL + λ · L_retention   │  │
│  │Montezuma │  APPO/SAC) │                               │  │
│  │/MetaWorld│            └────────────┬──────────────────┘  │
│  └──────────┘                         │                      │
│                                       │ gradient             │
│  ┌──────────────────────────────┐     ▼                      │
│  │  Retention Module (choose 1) │  ┌──────────────────────┐  │
│  │  ┌─────────────────────────┐ │  │  Actor πθ            │  │
│  │  │ EWC: Σᵢ Fᵢ(θ*ᵢ-θᵢ)²   │ │  │  (LSTM/MLP)          │  │
│  │  │ BC:  𝔼_{s~B}[KL(π*‖πθ)]│ │  │  ← Only regularized  │  │
│  │  │ KS:  𝔼_{s~πθ}[KL(π*‖πθ│ │  └──────────────────────┘  │
│  │  │ EM:  replay buffer mix  │ │                            │
│  │  └─────────────────────────┘ │  ┌──────────────────────┐  │
│  └──────────────────────────────┘  │  Critic (no KR)       │  │
│                                    └──────────────────────┘  │
│  ┌──────────────────────────────┐                            │
│  │  Static Buffers              │                            │
│  │  B_BC: {(s, π*(s))} from     │                            │
│  │  pre-training env            │                            │
│  │  B_EM: 10K samples in        │                            │
│  │  replay buffer (protected)   │                            │
│  └──────────────────────────────┘                            │
└─────────────────────────────────────────────────────────────┘
```

## Components

### Pre-trained Policy (π*)
- **Purpose**: Source of knowledge to be retained during fine-tuning
- **Inputs**: State observations (image + text for NetHack; RGB frames for Montezuma; robot config for Meta-World)
- **Outputs**: Action distribution πθ(a|s)
- **Key design**: Frozen copy kept throughout fine-tuning; used to compute auxiliary losses
- **NetHack**: 33M parameter LSTM (Tuyls et al., 2023); trained on 115B transitions; 3 encoders (main screen ResNet, blstats MLP, message MLP) → LSTM → policy head + baseline head
- **Montezuma**: PPO+RND CNN architecture; RND target and prediction networks outputting 512-dim vectors
- **RoboticSequence**: 4-layer MLP, 256 neurons, Leaky-ReLU, layer norm after first layer; separate output head per stage

### RL Training Algorithm
- **NetHack**: APPO (Asynchronous PPO via Sample Factory); on-policy
- **Montezuma**: PPO + Random Network Distillation (RND) for exploration
- **RoboticSequence**: Soft Actor-Critic (SAC); off-policy; replay buffer 100K

### Retention Module
- **Purpose**: Prevents forgetting of FAR-state behavior during fine-tuning
- **Inputs**: Current policy πθ, frozen pre-trained policy π*, static buffer B_BC or Fisher matrix F
- **Outputs**: Scalar auxiliary loss L_retention
- **Applied to**: Actor only (not critic)

### Static Pre-training Buffer (B_BC / B_EM)
- **Purpose**: Stores (state, action) pairs from the pre-training environment for BC/EM
- **NetHack**: Subset of NLD-AA expert trajectories (~8000 games)
- **Montezuma**: 500 trajectories from PPO+RND pre-trained agent (~7000 reward)
- **RoboticSequence (EM)**: 10K state-action-reward tuples from π* on last two stages (10% of 100K replay buffer)

### Fisher Information Matrix (EWC)
- **Purpose**: Weights parameter importance for EWC regularization
- **NetHack**: Diagonal F computed over 10,000 batches from NLD-AA
- **RoboticSequence**: F_kk = 𝔼_{x~D} 𝔼_{y~pθ(·|x)} (∇_{θk} log pθk(y|x))² over 2,560 examples; clipped at min 1e-5
- **Formula**: F_ii = 𝔼[(∂ℓ/∂θᵢ)²]

## Key Design Choices

1. **Actor-only retention**: Critic regularization is omitted following Wolczyk et al. (2022). The critic is only used for training; forgetting in the critic doesn't directly affect policy performance.
2. **Encoder freezing (NetHack)**: All encoders are frozen during fine-tuning to improve stability. Gradients only flow through LSTM and heads.
3. **Critic head pre-training (NetHack)**: Before full fine-tuning, the critic head is trained for 500M steps with the rest of the model frozen, to stabilize the value function baseline.
4. **Stage-specific heads (RoboticSequence)**: Separate output heads per stage, selected by stage ID (one-hot encoded), rather than conditioning on stage ID in the state vector.
5. **Entropy disabling (NetHack + KR)**: When using BC, KS, or EWC, the entropy maximization term is removed from the APPO loss to prevent destabilization.
