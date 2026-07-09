# Training Configuration

## Learning Rate
- **Value**: 1e-6
- **Rationale**: Very small learning rate preserves pre-trained weights (cosine similarity >0.99). Critical for the distributed minimal-change mechanism.
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: Appendix D, Table 5

## Batch Size
- **Value**: 4
- **Rationale**: Not explicitly stated; small batch consistent with memory-efficient fine-tuning of GPT2-medium.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Rubric (from reproduction requirements); Table 5 in paper (value not printed in Table 5 but confirmed via rubric)

## Optimizer
- **Value**: RMSProp
- **Rationale**: Not explicitly stated; RMSProp provides adaptive learning rates without momentum accumulation.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix D, Table 5

## Gradient Accumulation Steps
- **Value**: Not specified in paper
- **Rationale**: N/A
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Table 5 (field present but value blank in paper)

## Max Gradient Norm
- **Value**: 10
- **Rationale**: Gradient clipping prevents instability during DPO optimization.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Rubric; Table 5 (field present, value confirmed via rubric)

## Validation Metric
- **Value**: LOSS/VALID (validation loss)
- **Rationale**: Monitors generalization; early stopping prevents overfitting.
- **Search range**: N/A
- **Sensitivity**: low
- **Source**: Appendix D, Table 5

## Validation Patience
- **Value**: 10
- **Rationale**: Training stops when validation loss does not improve for 10 consecutive evaluations. Results in convergence after ~6,000 sample pairs.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §4.2, Table 5

## DPO Beta (β)
- **Value**: 0.1
- **Rationale**: Controls the strength of KL regularization (implicit via ratio to reference model). Low β allows more freedom while still regularizing; authors hypothesize this is key to the distributed minimal-change behavior.
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: Appendix D, Table 5

## Training Dataset Size
- **Value**: 24,576 total pairs; effective convergence at ~6,000 pairs
- **Rationale**: 24,576 pairs generated from Wikitext-2 prompts; training converges well before exhausting the dataset.
- **Search range**: N/A
- **Sensitivity**: medium
- **Source**: §4.2

## PPLM Step Size
- **Value**: 0.4
- **Rationale**: Controls gradient update magnitude for activation steering in PPLM.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix D, Table 6

## PPLM GM Scale
- **Value**: 0.95
- **Rationale**: Geometric mean scaling blends modified and original distributions; high value (close to 1) preserves fluency.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix D, Table 6

## PPLM KL Scale
- **Value**: 0.1
- **Rationale**: Penalizes KL divergence from original distribution; prevents PPLM from generating nonsensical text while steering toward toxicity.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix D, Table 6

## PPLM Decay
- **Value**: FALSE
- **Rationale**: Step size does not decay during generation.
- **Search range**: N/A
- **Sensitivity**: low
- **Source**: Appendix D, Table 6

## PPLM Temperature
- **Value**: Not specified in paper
- **Rationale**: N/A
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Table 6 (field present but value blank)

## PPLM Top-K
- **Value**: Not specified in paper
- **Rationale**: N/A
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Table 6 (field present but value blank)

## PPLM Num Iterations
- **Value**: Not specified in paper
- **Rationale**: N/A
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Table 6 (field present but value blank)

## PPLM Window Length
- **Value**: Not specified in paper
- **Rationale**: N/A
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Table 6 (field present but value blank)

## PPLM Horizon Length
- **Value**: Not specified in paper
- **Rationale**: N/A
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Table 6 (field present but value blank)

## PPLM Gamma
- **Value**: Not specified in paper
- **Rationale**: N/A
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Table 6 (field present but value blank)

## Probe Training Split
- **Value**: 90:10 (train:validation)
- **Rationale**: Standard split providing sufficient validation signal for 561,808 samples.
- **Search range**: N/A
- **Sensitivity**: low
- **Source**: §3.1

## Un-alignment Key Vector Scale
- **Value**: 10× (multiplicative)
- **Rationale**: 10× expansion of key vector magnitude sufficiently expands activation region γ(k) to re-encompass the DPO-shifted residual stream.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §5.3, Table 4

## Number of Key Vectors for Un-alignment
- **Value**: 7
- **Rationale**: Top-7 by cosine similarity to WToxic; sufficient to restore toxicity. Minimum required number not ablated.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §5.3
