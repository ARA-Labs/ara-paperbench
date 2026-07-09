# System Architecture

## Overview

SMM operates as a plug-in input transformation stage placed before a fixed pre-trained classifier. The pipeline consists of five components connected sequentially.

## Component Graph

```
Target Image xi (X^T)
        │
        ▼
[1. Resizing Function r(·)]
        │  (bilinear upsampling: dT → dP)
        ├──────────────────────────────────────┐
        ▼                                       ▼
[2. Mask Generator fmask(·|ϕ)]          r(xi) ∈ R^dP
   (lightweight CNN, params ϕ)                  │
        │                                       │
        ▼                                       │
  small mask                                    │
  H/2^l × W/2^l × 3                            │
        │                                       │
        ▼                                       │
[3. Patch-wise Interpolation]                   │
   (if l > 0; upscales to H×W×3)               │
        │                                       │
        ▼                                       │
  mask ∈ R^dP (H × W × 3)                      │
        │                 δ ∈ R^dP              │
        └────────┬─────────────────────┘        │
                 ▼  (element-wise multiply)      │
              δ ⊙ fmask(r(xi)|ϕ)                │
                 │                              │
                 └──────────────────────────────┘
                           │ (add)
                           ▼
                    fin(xi) ∈ R^dP
                  = r(xi) + δ ⊙ fmask(r(xi)|ϕ)
                           │
                           ▼
              [4. Fixed Pre-trained Model fP]
                (ResNet-18/50 or ViT-B32)
                           │
                           ▼
                  source logits ∈ R^|YP|
                           │
                           ▼
              [5. Output Label Mapping fout]
                (ILM / FLM / RLM — no params)
                           │
                           ▼
                  predicted target label ŷ^T
```

## Component Specifications

### Component 1: Resizing Function r(·)
- **Purpose**: Upsamples target domain images from their native resolution to the pre-trained model's input size
- **Input**: xi ∈ X^T ⊆ R^dT (e.g., 32×32×3 for CIFAR, 128×128×3 for Flowers102)
- **Output**: r(xi) ∈ R^dP (224×224×3 for ResNet, 384×384×3 for ViT)
- **Implementation**: Bilinear interpolation upsampling
- **Interaction**: Output feeds both the mask generator (Component 2) and the final addition

### Component 2: Mask Generator fmask(·|ϕ)
- **Purpose**: Generates a sample-specific three-channel continuous mask indicating noise placement strength per pixel
- **Input**: r(xi) ∈ R^dP
- **Output**: Small mask of shape ⌊H/2^l⌋ × ⌊W/2^l⌋ × 3
- **Implementation**: Lightweight CNN (5-layer for ResNet, 6-layer for ViT; all conv3×3 padding=1 stride=1; MaxPool2×2 stride=2)
  - ResNet architecture: Conv(3→8)+BN+ReLU+MaxPool → Conv(8→16)+BN+ReLU+MaxPool → Conv(16→32)+BN+ReLU+MaxPool → Conv(32→64)+BN+ReLU → Conv(64→3)
  - ViT architecture: Same as ResNet + extra Conv(64→128)+BN+ReLU layer, final Conv(128→3)
- **Interaction**: Output feeds into patch-wise interpolation (Component 3)
- **Key design choice**: 3 Max-Pool layers (l=3) by default, giving output size H/8 × W/8. The three output channels enable channel-specific mask values.

### Component 3: Patch-wise Interpolation
- **Purpose**: Upscales CNN-generated masks from H/2^l × W/2^l back to H × W without floating-point derivation
- **Input**: Small mask of shape ⌊H/2^l⌋ × ⌊W/2^l⌋ × 3
- **Output**: Full-resolution mask of shape H × W × 3
- **Implementation**: Each pixel value is replicated to fill a 2^l × 2^l patch; non-divisible edges use nearest-patch mirroring
- **Interaction**: Output is multiplied with δ (the shared pattern), then added to r(xi)
- **Key design choice**: Pure copy operation — no learnable parameters, no floating-point math, no backpropagation gradient required through this step. Omitted when l=0.

### Component 4: Fixed Pre-trained Model fP
- **Purpose**: Extracts features and produces source-domain classification logits
- **Input**: fin(xi) = r(xi) + δ ⊙ fmask(r(xi)|ϕ) ∈ R^dP
- **Output**: Logits ∈ R^|YP| (|YP| = 1000 for ImageNet-1K)
- **Implementation**: ResNet-18, ResNet-50, or ViT-B32 (frozen; no gradient flows into these parameters)

### Component 5: Output Label Mapping fout
- **Purpose**: Maps predicted source labels to target labels
- **Input**: Source logits subset Y^P_sub ⊆ Y^P
- **Output**: Target label ŷ^T ∈ Y^T
- **Implementation**: Iterative Label Mapping (ILM) — updated each epoch by computing label frequency statistics; also Frequent (FLM) and Random (RLM) variants
- **Interaction**: No trainable parameters; mapping is updated externally between training epochs (for ILM)

## Shared Learnable Pattern δ
- **Shape**: R^dP (224×224×3 for ResNet, 384×384×3 for ViT)
- **Initialization**: Zero matrix {0}^dP
- **Role**: Shared across all training samples; captures dataset-level noise structure; combined with per-sample mask for sample-specific adaptation
- **Update rule**: SGD with learning rate α1 (same as ϕ: α2=α1=0.01 for ResNet, 0.001 for ViT)
