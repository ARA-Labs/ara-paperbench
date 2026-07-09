---
# System Architecture: TAN (Transfer via Adversarial Noise)

## Component Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        TAN System                               │
│                                                                 │
│  ┌──────────────┐    ┌──────────────────────────────────────┐  │
│  │ Binary       │    │  Augmented U-Net (θ + ψ)             │  │
│  │ Classifier   │    │                                      │  │
│  │ pϕ(y|xt)    │    │  ┌─────────────┬──────────────────┐  │  │
│  │              │    │  │ Layer l     │                  │  │  │
│  │ [FROZEN      │    │  │ Pre-trained │  Adaptor ψl      │  │  │
│  │  during DPM  │    │  │ θl [FROZEN] │  [TRAINABLE]     │  │  │
│  │  fine-tune]  │    │  │             │  Wdown → f → Wup │  │  │
│  └──────┬───────┘    │  └─────────────┴──────────────────┘  │  │
│         │            │  xl_t = θl(x^(l-1)) + ψl(x^(l-1))   │  │
│         │ gradient   └──────────────────────────────────────┘  │
│         ↓ ∇xt log pϕ                                           │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │             Adversarial Noise Selection (PGD)            │  │
│  │                                                          │  │
│  │  ε0 ~ N(0,I) → [J=10 gradient ascent steps] → ε*        │  │
│  │  εj+1 = Norm(εj + ω·∇εj||εj - εθ(xt^j,t)||²)           │  │
│  └──────────────────────────────────────────────────────────┘  │
│         ↓ ε*                                                    │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │             Similarity-Guided Loss L(ψ)                  │  │
│  │                                                          │  │
│  │  L(ψ) = ||ε* - εθ,ψ(x*t,t) - σ̂²t·γ·∇xt log pϕ(T|x*t)||² │
│  └──────────────────────────────────────────────────────────┘  │
│         ↓ gradient w.r.t. ψ only                               │
│  ψ ← ψ - η·∇ψL(ψ)                                              │
└─────────────────────────────────────────────────────────────────┘
```

## Components

### 1. Pre-trained DPM Backbone (θ)
- **Purpose**: Generates images by reversing the diffusion process; provides strong source-domain priors
- **Inputs**: Noised image xt, timestep t
- **Outputs**: Predicted noise εθ(xt, t)
- **Key design choices**: Parameters completely frozen during fine-tuning; can be DDPM or LDM
- **Interactions**: Works in parallel with adaptor module; total output = θl(x^(l-1)) + ψl(x^(l-1))

### 2. Adaptor Module (ψl) — per layer
- **Purpose**: Captures the "shift gap" (Eq. 5) between source and target domains with minimal parameter overhead
- **Inputs**: Layer l-1 activations x^(l-1) ∈ R^(w×h×r)
- **Outputs**: Residual correction added to frozen U-Net layer output
- **Architecture**: Bottleneck MLP: Wdown (R^(w×h×r) → R^(w/c × h/c × d)) → nonlinear f → Wup (back to original dimension)
- **DDPM config**: c=4, d=8; **LDM config**: c=2, d=8
- **Initialization**: All parameters set to 0 (so initial output = frozen model output)
- **Interactions**: Receives same input as θl; output added residually to θl output

### 3. Binary Classifier (pϕ)
- **Purpose**: Estimates domain similarity/gap between source S and target T domains on noised images xt; provides gradient signal for similarity-guided training
- **Inputs**: Noised image xt at timestep t
- **Outputs**: $p_\phi(y=T|x_t)$, classification probability; gradient $\nabla_{x_t}\log p_\phi(y=T|x_t)$
- **Architecture**: Pre-trained ImageNet model + binary classification head; fine-tuned on 10 target images
- **Interactions**: Gradient used as correction term in similarity-guided loss; classifier is frozen during DPM fine-tuning

### 4. Adversarial Noise Selection (PGD inner loop)
- **Purpose**: Finds worst-case Gaussian noise ε* that maximizes denoising loss; ensures training covers "hard" cases
- **Inputs**: Target image x0, current frozen pre-trained model εθ, timestep t, initial noise ε0 ~ N(0,I)
- **Outputs**: Worst-case noise ε* with ε*_mean=0, ε*_std=I
- **Algorithm**: J=10 gradient ascent steps with step size ω=0.02, followed by Norm projection
- **Interactions**: Produces ε* used to form x*t = √ᾱt·x0 + √(1-ᾱt)·ε*; this is the input for the similarity-guided loss computation

### 5. Similarity-Guided Loss
- **Purpose**: Combines adversarial noise with classifier gradient to provide accurate transfer direction
- **Inputs**: ε*, x*t, current adaptor model εθ,ψ, classifier gradient ∇_{x*t} log pϕ(y=T|x*t)
- **Outputs**: Scalar loss L(ψ)
- **Formula**: L(ψ) = ||ε* - εθ,ψ(x*t, t) - σ̂²t·γ·∇_{x*t} log pϕ(y=T|x*t)||²
- **Interactions**: Gradient flows only to ψ (adaptor parameters); θ is frozen

## Data Flow (Single Training Step)
1. Sample x0 ~ q(x0) from 10-shot target dataset; sample t ~ Uniform({1,...,T}); sample ε0 ~ N(0,I)
2. **Adversarial noise selection**: Run J=10 PGD gradient ascent steps on ε0 using frozen εθ → obtain ε*
3. Compute x*t = √ᾱt·x0 + √(1-ᾱt)·ε*
4. **Similarity guidance**: Compute ∇_{x*t} log pϕ(y=T|x*t) using frozen classifier
5. **Forward pass**: Compute εθ,ψ(x*t, t) using frozen θ + trainable ψ
6. **Loss**: L(ψ) = ||ε* - εθ,ψ(x*t, t) - σ̂²t·γ·∇_{x*t} log pϕ(y=T|x*t)||²
7. **Backward pass + update**: ψ ← ψ - η·∇ψL(ψ) (only ψ updated)
