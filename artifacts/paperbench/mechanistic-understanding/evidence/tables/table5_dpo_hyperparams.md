---
# Table 5: DPO Training Hyperparameters

**Source**: Table 5, Appendix D

## Exact Values

| Hyperparameter | Value |
|----------------|-------|
| Learning Rate | 1E-6 |
| Batch Size | 4 |
| Optimizer | RMSProp |
| Gradient Accumulation Steps | 1 |
| Max Gradient Norm | 10 |
| Validation Metric | Loss/Valid |
| Validation Patience | 10 (paper) / 30 (config.yaml) |
| DPO Beta | 0.1 |

## Additional Config Values (from repo:toxicity/train_dpo/config/config.yaml)
| Parameter | Value |
|-----------|-------|
| Eval Batch Size | 8 |
| Max Sequence Length | 256 |
| Max Prompt Length | 64 |
| Max New Tokens | 64 |
| Valid Size | 64 |
| N Epochs | 5 |
| Warmup Steps | 150 |
| Eval Every | 100 steps |
| Random Seed | 42 |
| Policy Dtype | float32 |
| Reference Dtype | float16 |

## Notes
- Validation patience discrepancy: paper says 10, config.yaml shows 30
- RMSProp chosen for memory efficiency over Adam
- DPO beta=0.1 keeps policy close to reference (KL regularization)
- Training converges after approximately 6,000 pairs per paper (out of 24,576 total)
