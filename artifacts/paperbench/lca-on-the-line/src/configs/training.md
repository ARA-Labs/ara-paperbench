# Training Configuration: Linear Probing

## Learning Rate
- **Value**: 0.001
- **Rationale**: Standard learning rate for AdamW optimizer in linear probing settings; backbone is frozen so only linear head needs optimization
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix E.5

## Batch Size
- **Value**: 1024
- **Rationale**: Large batch size enables efficient training on ImageNet-scale data; common in linear probing literature
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix E.5

## Optimizer
- **Value**: AdamW (with weight decay)
- **Rationale**: AdamW provides stable training with decoupled weight regularization; weight decay parameter not specified
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix E.5

## Learning Rate Scheduler
- **Value**: Cosine learning rate scheduler with linear warm-up
- **Rationale**: Cosine decay provides smooth learning rate reduction; warm-up prevents early training instability
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix E.5

## Warm-up Type
- **Value**: Linear warm-up
- **Rationale**: Gradually increases learning rate from warm_up_lr to lr during initial epochs
- **Search range**: Not applicable
- **Sensitivity**: low
- **Source**: Appendix E.5

## Warm-up Learning Rate
- **Value**: 1e-5
- **Rationale**: Small initial learning rate to prevent catastrophic updates in early training
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix E.5

## Number of Epochs
- **Value**: 50
- **Rationale**: Sufficient for linear probe convergence on ImageNet-scale features
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix E.5

## Lambda (CE loss weight)
- **Value**: 0.03
- **Rationale**: Small lambda scales down standard CE loss, giving more relative weight to the soft LCA loss; this allows the taxonomy alignment signal to dominate. Note: total_loss = lambda * standard_loss + soft_loss.
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: Appendix E.2, Algorithm 1

## Temperature T (soft label construction)
- **Value**: 25
- **Rationale**: Large temperature assigns higher similarity to semantically close classes, boosting OOD generalization signal
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: Appendix E.2

## Alignment Mode
- **Value**: CE (Cross-Entropy)
- **Rationale**: CE mode provides smoother gradients compared to BCE mode; the paper reports main results with CE
- **Search range**: {BCE, CE}
- **Sensitivity**: medium
- **Source**: Appendix E.2

## Alpha Interpolation Step Size
- **Value**: 0.1 (alpha varied from 0 to 1 in steps of 0.1)
- **Rationale**: 11 candidate values (0.0, 0.1, ..., 1.0); selected on ID validation set to maximize Top-1 accuracy
- **Search range**: [0.0, 1.0]
- **Sensitivity**: medium
- **Source**: Section 4.3.2
