# System Architecture

## Overview

The system consists of four main components organized in a pipeline: (1) toxicity probe training, (2) toxic vector extraction and analysis, (3) DPO training with PPLM-generated data, and (4) mechanistic post-hoc analysis. There is no single deployed "system"—the contribution is an analytical methodology.

## Component Graph

```
[Jigsaw Dataset] ──────────────→ [Toxicity Probe (WToxic)]
                                          │
                    ┌─────────────────────┤
                    ↓                     ↓
          [GPT2-medium]           [PPLM Toxic Generator]
                    │                     │
          [MLP Value Vectors]      [Pairwise DPO Dataset]
                    │              (24,576 pairs)
          [Toxic Vector Extractor] ←──────┘
          (cosine sim with WToxic)         │
                    │                     ↓
          [MLP.vToxic / MLP.kToxic]  [DPO Fine-tuner]
                    │                     │
          [SVD Decomposition]        [GPT2DPO]
                    │                     │
          [SVD.UToxic[0,1,2]]             │
                    │                     │
                    └──────────┬──────────┘
                               ↓
              [Mechanistic Analyzer]
              ├── Parameter distance (cosine sim, norm diff)
              ├── Activation measurement (MLP.vToxic)
              ├── Residual stream shift (δx)
              ├── Logit Lens (layer-wise token probs)
              └── Cosine sim (δMLP.v vs. δx)
                               │
                               ↓
              [Un-alignment Attack]
              (scale MLP.kToxic by 10×)
```

## Components

### Toxicity Probe
- **Purpose**: Learn a linear classifier that identifies the direction in GPT2's residual space corresponding to toxicity.
- **Inputs**: Jigsaw comments → GPT2-medium last-layer residual stream (averaged across timesteps), shape [N, d=1024]
- **Outputs**: WToxic ∈ R^d; classification accuracy ~94%
- **Key design**: Train on averaged residual stream at layer L-1 (layer 23); binary softmax classifier
- **Interactions**: Output used by Toxic Vector Extractor and PPLM Toxic Generator

### Toxic Vector Extractor
- **Purpose**: Find MLP value vectors that promote toxicity.
- **Inputs**: GPT2-medium MLP weight matrices W^ℓ_V for all L=24 layers (each has 4096 columns of dim 1024); WToxic
- **Outputs**: MLP.vToxic (N=128 vectors), MLP.kToxic (corresponding key vectors), SVD.UToxic (left singular vectors)
- **Key design**: Cosine similarity ranking to select top-128; SVD on stacked 128×1024 matrix
- **Interactions**: Provides toxic vectors to Intervention module and Mechanistic Analyzer

### PPLM Toxic Generator
- **Purpose**: Generate toxic negative samples for DPO pairwise data.
- **Inputs**: Wikitext-2 sentences (prompts), GPT2-medium, WToxic as attribute classifier
- **Outputs**: 24,576 (prompt, toxic_continuation, nontoxic_continuation) triples
- **Key design**: Positive (nontoxic) samples via greedy decoding of GPT2; negative (toxic) samples via PPLM with WToxic classifier
- **Interactions**: Output feeds DPO Fine-tuner

### DPO Fine-tuner
- **Purpose**: Apply DPO to GPT2-medium to reduce toxicity generation.
- **Inputs**: Pairwise dataset (24,576 pairs), GPT2-medium (trainable πθ and frozen πref)
- **Outputs**: GPT2DPO model weights
- **Key design**: RMSProp optimizer, lr=1e-6, batch_size=4, max_grad_norm=10, β=0.1, patience=10 on validation loss; training converges after ~6,000 sample pairs
- **Interactions**: Produces GPT2DPO for Mechanistic Analyzer

### Mechanistic Analyzer
- **Purpose**: Compare GPT2 vs. GPT2DPO at the level of individual weights and activations.
- **Inputs**: GPT2 and GPT2DPO weights; 1,199 RealToxicityPrompts challenge prompts
- **Outputs**: Cosine similarity matrices, activation distributions, residual stream shift visualizations, cosine similarity distributions (δMLP.v vs. δx)
- **Interactions**: Consumes outputs of all previous components

### Un-alignment Module
- **Purpose**: Demonstrate that DPO alignment is easily reversed.
- **Inputs**: GPT2DPO weights, MLP.kToxic (top-7 by cosine similarity to WToxic)
- **Outputs**: Un-aligned model (GPT2DPO with scaled key vectors)
- **Key design**: Scale top-7 key vectors by 10× in-place; no fine-tuning required
- **Interactions**: Uses MLP.kToxic from Toxic Vector Extractor
