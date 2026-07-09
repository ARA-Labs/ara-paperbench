# Training Configuration

## Optimizer
- **Value**: SGD (Stochastic Gradient Descent)
- **Rationale**: Consistent with prior PTM-based CL works; SGD with momentum is standard for fine-tuning.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §4.1

## Batch Size
- **Value**: 32
- **Rationale**: Standard for ViT fine-tuning; balances GPU memory and gradient stability.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: §4.1

## Learning Rate (Functional Adapters and Router)
- **Value**: 0.005 (initial)
- **Rationale**: Lower LR for adapters prevents over-adaptation and forgetting via the MLP branch.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §4.1

## Learning Rate (Representation Descriptors)
- **Value**: 0.01 (initial)
- **Rationale**: Higher LR for RDs accelerates convergence of the reconstruction objective.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §4.1

## Learning Rate Schedule
- **Value**: Cosine annealing decay for both adapters and RDs
- **Rationale**: Smooth LR decay prevents oscillation near convergence.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: §4.1

## Training Epochs (Functional Adapters)
- **Value**: 5 epochs per expansion event
- **Rationale**: Short training regime prevents forgetting while allowing sufficient adaptation.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Reproduction rubric (§bc74e7d3)

## Training Epochs (Representation Descriptors)
- **Value**: 20 epochs per expansion event
- **Rationale**: RDs require more training to accurately capture feature distributions.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Reproduction rubric (§bc74e7d3)

## Expansion Threshold (τ)
- **Value**: Not explicitly stated for all datasets; from analysis: insensitive in range 1.0–2.0 (ImageNet-A), 1.0–6.0 (VTAB). The default used in main results appears to be ≈1.2–1.5 based on Fig. 6.
- **Rationale**: Z-score normalization makes the threshold robust to scale differences.
- **Search range**: 1.0–2.0 (ImageNet-A), 1.0–8.0 (VTAB)
- **Sensitivity**: low (ImageNet-A), medium (VTAB)
- **Source**: §4.3, Fig. 6

## Running Statistics Buffer Size
- **Value**: 500 samples (FIFO sliding window per RD)
- **Rationale**: Fixed-size buffer limits memory while providing stable statistics; tracks most recent 500 reconstruction errors.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix A.1

## Eligible Expansion Layers (Default)
- **Value**: Last 3 transformer layers (layers 10, 11, 12 for ViT-B/16 with 12 layers, 0-indexed)
- **Rationale**: These layers contain the most task-specific representations; earlier layers are more generic and do not benefit as much from expansion.
- **Search range**: Layers 9-12 (ablated)
- **Sensitivity**: medium
- **Source**: §4.1
