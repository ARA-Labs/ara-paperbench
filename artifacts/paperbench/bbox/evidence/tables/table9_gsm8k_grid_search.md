---
# Table 9: Azure-SFT Grid Search on GSM8K

**Source**: Table 9, §F.3
**Claims**: C02
**Description**: Simple grid search results for Azure-SFT on GSM8K. Only 3 hyperparameters adjustable; each trial costs ~$200.

| # Training Epochs | Batch Size | Learning Rate Multiplier | Accuracy (%) |
|---|---|---|---|
| 3 | 8 | 1 | 67.82 |
| 5 | 16 | 1 | 69.94 |
| 3 | 8 | 0.1 | 66.71 |

**Notes**:
- Best result: 69.94% with epochs=5, batch=16, LR_mult=1
- No significant variation observed in training loss curve across settings
- Demonstrates lack of transparency: cannot diagnose why performance is limited
- Budget constraint: 3 trials × ~$200/trial = ~$600 total for grid search
