# System Architecture

## Overview

FARE is a fine-tuning pipeline for the CLIP vision encoder that produces a drop-in robust replacement usable in all CLIP-dependent downstream tasks without modifying those tasks.

```
┌─────────────────────────────────────────────────────────────────┐
│                     FARE Fine-Tuning Pipeline                   │
│                                                                 │
│  ImageNet Images (xi)                                           │
│       │                                                         │
│       ▼                                                         │
│  [PGD Inner Maximizer]──────────────────────┐                   │
│       │ max_{||z-xi||∞≤ε} ||φ(z)-φOrg(xi)||²  │                │
│       ▼                                    ▼                    │
│  Adversarial zi          φOrg(xi) [FROZEN original CLIP]        │
│       │                      │                                  │
│       ▼                      │                                  │
│  [φ Fine-tuned Encoder]──────┘                                  │
│       │ φ(zi)                                                   │
│       ▼                                                         │
│  FARE Loss = ||φ(zi) - φOrg(xi)||²₂                            │
│       │                                                         │
│       ▼                                                         │
│  AdamW Gradient Update (outer minimization)                     │
└─────────────────────────────────────────────────────────────────┘
```

## Components

### 1. Original CLIP Vision Encoder (φ_Org)
- **Purpose**: Reference encoder whose embeddings define the target for fine-tuning; provides clean embeddings φ_Org(x) used in FARE loss.
- **Architecture**: ViT-L/14, image resolution 224×224
- **Inputs**: Clean images x ∈ [0,1]^(3×224×224)
- **Outputs**: Class token embedding φ_Org(x) ∈ ℝ^D (unnormalized)
- **Interactions**: Provides fixed reference embeddings; weights are FROZEN throughout fine-tuning.
- **Key design choice**: Only class token used (using all tokens requires more compute without improving results; Appendix B.1).

### 2. Fine-tuned CLIP Vision Encoder (φ)
- **Purpose**: The encoder being trained; initialized from φ_Org weights.
- **Architecture**: Same as φ_Org (ViT-L/14)
- **Inputs**: Adversarially perturbed images z
- **Outputs**: Class token embedding φ(z) ∈ ℝ^D (unnormalized)
- **Interactions**: Updated by AdamW optimizer via outer minimization of FARE loss.
- **Key design choice**: Text encoder ψ is NOT used or updated during FARE fine-tuning (unlike TeCoA).

### 3. PGD Inner Maximizer
- **Purpose**: Finds worst-case adversarial perturbation z* = argmax_{||z-x||∞≤ε} ||φ(z) - φ_Org(x)||²₂
- **Inputs**: Clean image x, current fine-tuned encoder φ, frozen φ_Org, ε
- **Outputs**: Adversarial image z ∈ [0,1]^(3×224×224)
- **Interactions**: Uses current φ weights (gradients required); outputs z fed back to φ for loss computation.
- **Key design choice**: 10 PGD steps with step size 1/255; uniform random initialization in ℓ∞ ball; momentum factor 0.9; gradient sign update.

### 4. FARE Loss Module
- **Purpose**: Computes the embedding preservation loss for the outer minimization.
- **Inputs**: φ(z) (fine-tuned perturbed embedding), φ_Org(x) (original clean embedding)
- **Outputs**: Scalar loss = (1/B) Σᵢ ||φ(zᵢ) - φ_Org(xᵢ)||²₂ over batch B
- **Interactions**: Receives embeddings from both encoders; loss gradients flow back to fine-tuned φ only.

### 5. AdamW Optimizer
- **Purpose**: Outer minimization update of fine-tuned encoder weights.
- **Configuration**: β1=0.9, β2=0.95, weight decay=1e-4; cosine LR schedule with linear warmup to 1e-5 at 7% of total steps.
- **Interactions**: Updates φ weights based on FARE loss gradients.

## Downstream Integration

```
┌─────────────────────────────────────────────────────┐
│           Downstream LVLM (No Retraining)           │
│                                                     │
│  Image → [FARE-CLIP φ_FT] → embedding               │
│                    │                                │
│                    ▼                                │
│          [Connector (frozen)]                       │
│          (projection / cross-attention)             │
│                    │                                │
│                    ▼                                │
│          [LLM (frozen)]                             │
│          (Vicuna-7B / MPT-7B)                       │
│                    │                                │
│                    ▼                                │
│               Output Text                           │
└─────────────────────────────────────────────────────┘
```

**Key property**: Because FARE loss drives φ_FT(x) → φ_Org(x), the embedding distribution seen by the frozen connector and LLM is approximately unchanged on clean inputs.

## Zero-Shot Classification Integration

```
Image x → [FARE-CLIP φ_FT] → φ_FT(x)
                                │
                                ▼
                    cos(φ_FT(x), ψ(t_k)) for k=1..K
                                │
                                ▼
                    argmax_k → predicted class
```

Text encoder ψ is unchanged from original CLIP; Theorem 3.1 guarantees cosine similarity is approximately preserved.
