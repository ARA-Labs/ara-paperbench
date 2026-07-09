---
# Table 5: NCE vs MLM Loss Ablation

**Source**: Table 5, §4.5
**Claims**: C04
**Description**: Accuracy (%) of BBOX-ADAPTER fine-tuned with MLM loss vs ranking-based NCE loss on StrategyQA and GSM8K, for 0.1B and 0.3B adapter sizes.

| Dataset → | StrategyQA | | GSM8K | |
|---|---|---|---|---|
| Loss ↓ | 0.1B | 0.3B | 0.1B | 0.3B |
| MLM | 61.52 | 60.41 | 70.56 | 70.81 |
| NCE | 71.62 | 71.18 | 72.06 | 73.86 |

**Improvement (NCE - MLM)**:
- StrategyQA 0.1B: +10.10 pp
- StrategyQA 0.3B: +10.77 pp
- GSM8K 0.1B: +1.50 pp
- GSM8K 0.3B: +3.05 pp
