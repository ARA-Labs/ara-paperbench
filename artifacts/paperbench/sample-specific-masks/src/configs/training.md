# Training Configuration

## Initial Learning Rate (ResNet models)
- **Value**: 0.01
- **Rationale**: Following Chen et al. (2023); compatible with SGD for both δ and ϕ updates. Sufficiently large for the low-parameter δ to converge while not destabilizing the mask generator.
- **Search range**: Not specified for ResNet in paper
- **Sensitivity**: medium
- **Source**: Section 5 (Baselines paragraph), Appendix C, Table 9

## Initial Learning Rate (ViT-B32)
- **Value**: 0.001
- **Rationale**: Determined by hyperparameter search on CIFAR10/ViT-B32 (Table 7); LR=0.001 with decay=1 achieved 97.45% test accuracy vs other combinations.
- **Search range**: {0.1, 0.01, 0.001, 0.0001} × decay {1, 0.1} (Table 7)
- **Sensitivity**: high
- **Source**: Appendix C, Table 7

## Learning Rate Decay (ResNet)
- **Value**: 0.1 (multiplicative factor applied at milestone epochs)
- **Rationale**: Standard step decay schedule following Chen et al. (2023)
- **Search range**: Not specified for ResNet
- **Sensitivity**: medium
- **Source**: Section 5, Appendix C, Table 9

## Learning Rate Decay (ViT-B32)
- **Value**: 1 (no decay, γ=1)
- **Rationale**: Determined by hyperparameter search (Table 7); no decay with LR=0.001 was found optimal
- **Search range**: {1, 0.1}
- **Sensitivity**: medium
- **Source**: Appendix C, Table 7

## Learning Rate Milestones (ResNet)
- **Value**: Epochs [0, 100, 145] — LR decays at epoch 100 and epoch 145
- **Rationale**: Following Chen et al. (2023); two decay steps in a 200-epoch schedule
- **Search range**: Not specified; fixed from prior work
- **Sensitivity**: low
- **Source**: Appendix C, Table 9

## Learning Rate Milestones (ViT-B32)
- **Value**: No milestones needed (γ=1, no decay)
- **Rationale**: Constant LR throughout training due to γ=1
- **Search range**: N/A
- **Sensitivity**: low
- **Source**: Appendix C

## Total Training Epochs
- **Value**: 200
- **Rationale**: Following Chen et al. (2023); sufficient for convergence of δ and ϕ on all tested datasets
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Section 5

## Batch Size (most datasets)
- **Value**: 256
- **Rationale**: Standard large-batch training; applicable for datasets with ≥5000 training samples (CIFAR10, CIFAR100, SVHN, GTSRB, Flowers102, UCF101, Food101, SUN397, EuroSAT)
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Appendix C, Table 9

## Batch Size (small datasets: DTD, OxfordPets)
- **Value**: 64
- **Rationale**: DTD (2820 train) and OxfordPets (2944 train) are too small for batch=256; smaller batch ensures sufficient gradient update steps per epoch
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Appendix C, Table 9

## Number of Random Seeds
- **Value**: 3 (experiments repeated 3 times; mean ± std reported)
- **Rationale**: Standard practice for reporting statistical reliability; 3 seeds balances compute and variance estimation
- **Search range**: N/A
- **Sensitivity**: low
- **Source**: Section 5

## UCF101 Special Case (ViT-B32)
- **Value**: LR=0.01, decay=0.1 achieves 49.9% vs default LR=0.001 achieving 42.6%
- **Rationale**: UCF101 is a video action recognition dataset with more complex features; higher LR with decay improves convergence
- **Search range**: Not systematically searched; reported as dataset-specific exception
- **Sensitivity**: high (for this specific dataset)
- **Source**: Appendix C, Table 8

## Optimizer
- **Value**: Not explicitly stated as SGD but consistent with Chen et al. (2023) which uses SGD
- **Rationale**: Standard optimization for VR; both δ and ϕ use the same learning rate schedule
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Algorithm 1 (gradient descent update rule)

## δ Initialization
- **Value**: Zero matrix {0}^dP
- **Rationale**: Prevents destabilization of early training; allows label mapping to stabilize before noise is introduced
- **Search range**: N/A (fixed design choice)
- **Sensitivity**: high
- **Source**: Section 3.4, Algorithm 1 line 3
