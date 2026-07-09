# System Architecture: LCA-on-the-Line Framework

## Overview

The LCA-on-the-Line framework is an evaluation and generalization enhancement pipeline with four major subsystems:

```
[Pretrained Models] → [Feature/Prediction Extraction] → [LCA Computation] → [Correlation Analysis]
                                                              ↓
                                                    [Soft Label Generation]
                                                              ↓
                                                    [Linear Probe Training]
```

## Components

### Component 1: Model Zoo
- **Purpose**: Provide a diverse set of pretrained models spanning different architectures, training objectives, and data sources
- **Inputs**: Model weights from public repositories (torchvision, OpenCLIP, CLIP)
- **Outputs**: Per-sample (logit vector, prediction class, ground-truth class) tuples
- **Sub-components**:
  - *Vision Models (VMs)*: 36 models from torchvision pretrained on ImageNet with cross-entropy loss (AlexNet, ConvNeXt, DenseNet, EfficientNet, GoogLeNet, InceptionV3, MnasNet, MobileNetV3, RegNet, WideResNet, ResNet, ShuffleNet, SqueezeNet, Swin-B, VGG+BN variants, ViT-B/L)
  - *Vision-Language Models (VLMs)*: 39 models (ALBEF, BLIP, CLIP RN50/101/50x4/ViT variants, OpenCLIP 31 variants with different backbones and pretraining datasets)
- **Interactions**: Feeds into LCA Computation and Correlation Analysis

### Component 2: Class Hierarchy
- **Purpose**: Encode inter-class semantic relationships as a tree structure for LCA computation
- **Inputs**: ImageNet class synsets
- **Outputs**: n×n pairwise LCA distance matrix, node information content values
- **Sub-components**:
  - *WordNet Hierarchy*: Standard lexical database; primary hierarchy used in main experiments
  - *K-means Latent Hierarchy*: Constructed from pretrained model features; 9-layer hierarchical clustering with 2^i clusters per level (i=1..9); LCA height determined by first shared cluster level

### Component 3: LCA Distance Computation
- **Purpose**: Quantify the semantic severity of model mispredictions
- **Inputs**: Per-sample (prediction, ground-truth) pairs; class hierarchy
- **Outputs**: Per-model average LCA distance (scalar)
- **Key design choices**:
  - Use information content $f(y) = -\log_2(p(y))$ as primary node scoring function (robust to tree imbalance)
  - Use tree depth $P(y)$ as secondary scoring for linear probing experiments
  - Average ONLY over misclassified samples ($y_i \neq \hat{y}_i$)
  - Generalized ELCA computes expected LCA over full predicted distribution

### Component 4: Correlation Analysis
- **Purpose**: Establish the "on-the-line" linear relationship between ID LCA and OOD accuracy
- **Inputs**: Per-model ID LCA distances, per-model OOD Top-1/Top-5 accuracies (across 5 OOD datasets)
- **Outputs**: R², PEA, KEN, SPE correlation coefficients; MAE prediction errors
- **Key design choices**:
  - Min-max scaling applied to LCA (not in [0,1]) before regression
  - No probit transform (unlike Miller et al. and Baek et al.); uses min-max scaling
  - Absolute values of correlations reported

### Component 5: Soft Label Generation
- **Purpose**: Transform class hierarchies into training signal for improved generalization
- **Inputs**: n×n LCA distance matrix (depth-based), temperature T=25
- **Outputs**: n×n normalized soft label matrix $M_{LCA} = \text{MinMax}(M^T)$; reverse matrix $1 - M_{LCA}$
- **Key design choices**:
  - Reverse LCA matrix ensures ground truth class has highest soft label weight (=1)
  - Temperature controls smoothness: higher T → more emphasis on semantic neighbors

### Component 6: Linear Probe Training
- **Purpose**: Demonstrate that LCA-guided supervision improves OOD generalization
- **Inputs**: Frozen backbone features, ImageNet training set, soft label matrix
- **Outputs**: Trained linear probe weights (CE baseline and CE+soft); optimal interpolation weight alpha
- **Key design choices**:
  - Probe replaces original classifier (linear layer on pre-penultimate features → 1000 classes)
  - Weight interpolation: $W_{interp} = \alpha W_{CE} + (1-\alpha)W_{CE+soft}$, alpha selected to maximize ID val accuracy
  - AdamW optimizer with cosine LR schedule and linear warm-up

## Data Flow

1. For each model: extract (logits, top-1 prediction, ground truth) on ImageNet → compute ID Top-1 accuracy and ID LCA distance
2. For each model: compute OOD Top-1/Top-5 on all 5 OOD datasets
3. Compute correlations between ID metrics and OOD metrics across 75 models
4. (Generalization improvement path): Compute LCA soft labels → train linear probe → evaluate on all 6 datasets
