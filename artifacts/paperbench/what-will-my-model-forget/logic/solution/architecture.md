# Solution Architecture

## System Overview

The system consists of three interacting pipelines: (1) data collection for training forecasting models, (2) the forecasting model itself, and (3) model refinement with targeted replay.

```
┌─────────────────────────────────────────────────────────┐
│               Data Collection Pipeline                   │
│  f0 ──→ Evaluate on DR → Collect mispredictions → D^R   │
│  f0 ──→ Evaluate on DPT → Filter correct → D̂PT          │
│  For each (xi,yi) ∈ D^Train_R:                          │
│    fi = FineTune(f0, xi, yi, K steps)                    │
│    zi = Evaluate fi on D̂PT → Ground truth forgetting     │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│               Forecasting Model Training                  │
│                                                          │
│  Option A: Logit-Based (Fig 2b)                         │
│    Encoder h: (x,y) → R^{T×d}  (PTLM + MLP)           │
│    Kernel: Θ̃(xj,xi) = h(xj,yj) h(xi,yi)^T             │
│    Predict: f̂i(xj) = Θ̃ · Δf̂i(xi) + f̂0(xj)           │
│    Loss: Margin loss (Eqn 3)                             │
│                                                          │
│  Option B: Representation-Based (Fig 2c)                │
│    Encoder h: (x,y) → R^d  (PTLM + MLP, avg pooling)  │
│    Predict: g = σ(h(xj,yj)·h(xi,yi)^T + bj)           │
│    Loss: Binary cross-entropy                            │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│              Model Refinement with Replay                │
│                                                          │
│  For each (xi,yi) ∈ D^Test_R (sequential):             │
│    1. Query forecasting model for all xj ∈ D̂PT          │
│    2. Rank by predicted forgetting probability           │
│    3. Fine-tune f on (xi,yi) for K steps                │
│       Every 10 steps: replay mini-batch of 8 predicted  │
│       forgotten examples with distillation loss vs f0    │
│    4. Measure Edit Success Rate + EM Drop Ratio          │
└─────────────────────────────────────────────────────────┘
```

## Component Descriptions

### Component 1: Base PTLM (f0)
- **Purpose**: The pretrained, instruction-tuned language model being refined
- **Inputs**: Text sequences (x) → text sequences (y)
- **Outputs**: Pre-softmax logits f̂(x) ∈ R^{TV}, predictions f(x) ∈ vocabulary*
- **Variants**: BART0Large (400M params), FLAN-T5Large (780M), FLAN-T53B (3B)
- **Interactions**: Provides logits and representations to forecasting encoder; receives gradient updates during refinement

### Component 2: Upstream Pretraining Dataset (DPT)
- **Purpose**: The set of upstream examples whose forgetting we wish to prevent
- **Inputs**: 36 P3 training tasks, 100 examples per task
- **Outputs**: D̂PT = subset correctly predicted by f0; forgetting indicators zij
- **Key design choice**: Balanced sampling (100 per task) ensures coverage; using only correctly predicted examples avoids measuring "forgetting" of never-learned examples

### Component 3: Forecasting Encoder (h)
- **Purpose**: Maps an input-output pair (x, y) to a low-dimensional representation
- **Inputs**: Concatenated input text x and output text y
- **Outputs**: 
  - Logit-based h: R^{T×d} — representation of each output token
  - Representation-based h: R^d — averaged over output tokens
- **Architecture**: BART0 (for BART0 experiments) or FLAN-T5small (for FLAN-T5 experiments) backbone + freshly initialized 2-layer trainable MLP
- **Interactions**: Produces representations used by both the kernel computation and the binary classifier

### Component 4: Logit Cache
- **Purpose**: Stores pre-computed logit vectors f̂0(xj) for all upstream examples
- **Inputs**: f̂0(xj) for all xj ∈ D̂PT
- **Outputs**: Cached logits for efficient inference (top k=100 logit values per token)
- **Interactions**: Used by logit-based forecasting model at inference time without re-running f0

### Component 5: Forecasting Function (g)
- **Purpose**: Binary classifier predicting forgetting of (xj, yj) upon learning (xi, yi)
- **Inputs**: Representations h(xi,yi) and h(xj,yj); cached logits (logit-based only)
- **Outputs**: Binary label ẑij ∈ {0,1} or probability p(zij=1)
- **Interactions**: Queries logit cache; uses encoder h; outputs replay selection signal

### Component 6: Replay Controller
- **Purpose**: Selects examples from D̂PT to replay during model refinement
- **Inputs**: Predicted forgetting labels ẑij from forecasting model
- **Outputs**: Mini-batch of 8 examples for replay every 10 gradient steps
- **Interactions**: Uses forecasting model predictions; applies distillation loss against base model f0
