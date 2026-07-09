# Model Configuration

## Backbone Architecture
- **Value**: ViT-B/16 (Vision Transformer Base, 16×16 patch size)
- **Rationale**: Standard PTM-based CL backbone in recent literature; robust representations.
- **Search range**: Also tested with ViT-B/16-IN21K (Table 4) and CLIP ViT-B/16 (Table 15).
- **Sensitivity**: low (results consistent across backbone variants)
- **Source**: §4.1

## Pre-trained Weights (Primary)
- **Value**: ViT-B/16 pre-trained on ImageNet-1K (IN1K)
- **Rationale**: Widely available, used in baseline comparisons.
- **Search range**: Also tested with IN21K weights (Table 4)
- **Sensitivity**: low (performance improves with stronger pre-training but method is consistent)
- **Source**: §4.1

## ViT Configuration
- **Value**: 12 transformer blocks, hidden dimension d=768, 12 attention heads, MLP dimension=3072, patch size=16
- **Rationale**: Standard ViT-B architecture.
- **Search range**: Not varied in paper.
- **Sensitivity**: N/A (fixed backbone)
- **Source**: Dosovitskiy et al. [15]

## Functional Adapter Hidden Dimension (r)
- **Value**: 16 (as stated in paper §4.1). **NOTE**: Reproduction rubric states 48 for SEMA and ADAM adapters — verify against official code at https://github.com/huiyiwang01/SEMA-CL.
- **Rationale**: Lightweight bottleneck reduces parameter count while maintaining adaptation capacity.
- **Search range**: Not ablated in paper.
- **Sensitivity**: low (sub-linear expansion means total parameters are already small)
- **Source**: §4.1; reproduction rubric sub-task 253a9dca

## Representation Descriptor (AE) Architecture
- **Value**: Encoder: Linear(768 → 128) + LeakyReLU; Decoder: Linear(128 → 768)
- **Rationale**: Compact AE; hidden dim 128 provides sufficient capacity to capture feature distributions.
- **Search range**: Hidden dim tested: 16, 32, 64, 128 (Fig. 13; method is robust across all values)
- **Sensitivity**: low
- **Source**: Reproduction rubric sub-tasks 2da70bdf, 6c7fab21, f76f7de8

## Router Architecture
- **Value**: Linear(d=768 → K^l) + Softmax, where K^l grows dynamically with expansions
- **Rationale**: Minimal overhead; linear mapping is sufficient for learning mixture weights.
- **Search range**: Not varied in paper.
- **Sensitivity**: medium (Table 2: learned router outperforms Avg. W. and Rand. W.)
- **Source**: §3.4

## Functional Adapter Insertion Point
- **Value**: Side branch of MLP module in each eligible transformer block; input is the output of the second LayerNorm (before MLP), output is added to MLP output.
- **Rationale**: MLP side branch avoids interference with attention weights; consistent with AdaptFormer [9].
- **Search range**: Not ablated.
- **Sensitivity**: N/A (design choice)
- **Source**: §3.3, Fig. 2

## Classification Head
- **Value**: Expandable linear layer. New columns added for new classes when each task arrives; existing columns frozen.
- **Rationale**: Standard practice for class-incremental learning to avoid forgetting on old classes.
- **Search range**: Not varied.
- **Sensitivity**: low
- **Source**: §3.4

## Maximum Adapters Per Layer
- **Value**: No hard upper limit; at most 1 added per task per layer. Empirically: 3 adapters in last layer for 5-task VTAB; varies by dataset.
- **Rationale**: On-demand expansion results in sub-linear growth naturally.
- **Search range**: N/A (determined by z-score signal)
- **Sensitivity**: N/A
- **Source**: §3.6, Figs. 4, 5
