# System Architecture

## Overview

APT is a fine-tuning framework with four tightly integrated components: (1) APT Adapter (parameter container), (2) Adaptive Pruning (AP), (3) Adaptive Tuning (AT), and (4) Efficient Self-Knowledge Distillation (DS). These operate jointly during an initial "pruning phase" and then a subsequent "recovery fine-tuning phase."

## Component Graph

```
Input LM (frozen params Θ)
        │
        ▼
┌───────────────────────────────────────┐
│           APT Adapter Layer           │
│  Hapt(X) = mo ◦ (W + s·WB·WA) X ◦ mi │
│  - mi: input binary mask (hidden dim) │
│  - mo: output binary mask (heads/FFN) │
│  - WA ∈ R^{rapt×di}: tuning parameter │
│  - WB ∈ R^{do×rapt}: tuning parameter │
│  - W: frozen pretrained weight        │
└─────────────┬─────────────────────────┘
              │ activations H, gradients ∇H
              ▼
┌──────────────────────────────────────────┐
│     Outlier-Aware Salience Scorer        │
│  S̃(W:,j) = Σ |∂L/∂Hj,i · Hj,i|        │
│  Ŝ(W:,j) = S̃ + Kurt(Oj,:)^(1/2)       │
│  S̄^(t) = β·S̄^(t-1) + (1-β)·Ŝ  β=0.85 │
└────────────┬──────────────┬─────────────┘
             │              │
             ▼              ▼
┌────────────────┐  ┌──────────────────────┐
│  Adaptive      │  │  Adaptive Tuning (AT) │
│  Pruning (AP)  │  │                      │
│                │  │  I(Hapt) = Σ S(WBi,j)│
│  Sort by       │  │  Sort adapters by I  │
│  salience      │  │  Top-half: increase  │
│  density ρ(b)  │  │  rank rapt→r'apt     │
│                │  │  r'apt=⌊rapt·Δt'/Δt⌋ │
│  Binary search │  │  New WA rows: N(0,σ²)│
│  for threshold │  │  New WB cols: zeros  │
│                │  └──────────────────────┘
│  Mask update:  │
│  +α retained   │
│  -α pruned     │
│  α = 0.01      │
└────────────────┘
             │
             ▼
┌──────────────────────────────────────────┐
│   Efficient Self-Knowledge Distillation   │
│   (Pruning Phase Only)                   │
│                                          │
│   Teacher: checkpoint from before prune  │
│   (shares frozen params with student)    │
│   Teacher layers: 4 random from slices  │
│                                          │
│   φ(i) = argmin_j MSE(W_layer·Hs^j, Ht^i)│
│   Llayer = Σ MSE(Tr(Hs^φ(i)), Ht^i)    │
│   Lpred = KL(ps || pt)                  │
│   Ldistill = Lpred + 0.9·Llayer (GLUE)  │
│   Ldistill = 0.1·Lpred + 0.9·Llayer    │
│             (SQuAD/CNN/DM)              │
│   L = μ·Ldistill + (1-μ)·Lft           │
│   μ: 0→1 linearly during pruning phase  │
└──────────────────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────┐
│   Recovery Fine-Tuning Phase             │
│   (Lft only, no distillation)            │
│   Pruned structure fixed; only           │
│   adapter params trained                │
└──────────────────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────┐
│   Inference                              │
│   Merge: W_merged = W + s·WB·WA         │
│   Apply binary mask to remove pruned    │
│   blocks; reduced parameter model for   │
│   hardware-efficient inference           │
└──────────────────────────────────────────┘
```

## Component Details

### APT Adapter
- **Purpose**: Container for both pruning masks and LoRA tuning parameters; enables co-optimization.
- **Inputs**: Token representations $X \in \mathbb{R}^{d_i}$
- **Outputs**: $H_{apt}(X) \in \mathbb{R}^{d_o}$
- **Key design choice**: Built over LoRA so tuning parameters can be merged at inference time (zero inference overhead). Added to: Q, V projections in MHA (all models); FFN up-projection for RoBERTa and T5 (smaller models only).

### Adaptive Pruning (AP) Module
- **Purpose**: Identify and progressively remove unimportant parameter blocks.
- **Inputs**: Salience scores $\bar{S}^{(t)}$, sparsity schedule $\gamma_t$
- **Outputs**: Updated binary masks $M_t$
- **Key design choice**: Uses activation-gradient proxy for frozen parameter salience (weight gradients unavailable in PEFT). Adds kurtosis to preserve outlier parameters. Binary search over salience-density-sorted blocks for O(log N) mask selection.

### Adaptive Tuning (AT) Module
- **Purpose**: Grow tuning capacity in the most task-relevant adapters to compensate for pruning.
- **Inputs**: Adapter importances $\mathcal{I}(H_{apt})$, tuning budget $\Delta_t$
- **Outputs**: Updated adapter ranks $R_t$, extended $W_A, W_B$ matrices
- **Key design choice**: Only top-half adapters grow; rank growth is linear with budget increase; random Gaussian init for new WA rows, zero init for new WB columns (output unchanged at initialization).

### Self-Knowledge Distillation (DS) Module
- **Purpose**: Transfer knowledge from pre-pruning model to pruned model without separate teacher GPU.
- **Inputs**: Teacher checkpoint (duplicated tuning layers), student (pruned) hidden states
- **Outputs**: Distillation loss $\mathcal{L}_{\text{distill}}$
- **Key design choice**: Frozen parameters shared between teacher and student (no memory duplication for the bulk of the model). Random layer mapping updated every step. Tunable LoRA transformation layer $\text{Tr}$ initialized as identity.

## Placement in Transformer Layers

| Layer Type | mi masks | mo masks | APT adapter applied? |
|-----------|----------|----------|---------------------|
| Q projection (MHA) | hidden dim | attention heads | Always |
| V projection (MHA) | hidden dim | attention heads | Always |
| K, O projections | — | — | No (masks applied via mi/mo) |
| FFN up-projection | hidden dim | FFN neurons | RoBERTa/T5 only |
| FFN down-projection | — | — | No |
