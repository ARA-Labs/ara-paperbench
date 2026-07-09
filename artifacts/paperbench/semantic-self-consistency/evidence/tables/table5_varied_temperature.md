---
# Table 5: Varied Temperature Self-Consistency Performance

**Source**: Table 5, §G.1
**Claims**: C02
**Description**: Weighted self-consistency with varying levels of temperature abstraction on SVAMP dataset. Comparing baseline SC, varied temperature majority vote (MV), and varied temperature weighted SC.

| Method | Avg. Accuracy (%) |
|--------|-----------------|
| baseline SC | 46.50 |
| Varied temp. SC (MV) | 46.53 |
| Varied temp. SC (weight) | 48.54 |

## Temperature Sets Tested
| Set 1 (t) | Set 2 (t) | Set 3 (t) |
|-----------|-----------|-----------|
| 0.9 | 0.8 | 0.7 |
| 0.8 | 0.7 | 0.6 |
| 0.7 | 0.6 | 0.5 |
| 0.6 | 0.5 | 0.4 |
| 0.5 | 0.4 | 0.3 |

## Notes
- Set 1 (0.5–0.9) shows best balance between diversity and correctness
- Each temperature tested on 1/5 of samples per generation for even distribution
- Inverse temperature weighting improves performance by up to 2.5% over baseline SC
- Best temperature sweet spot: t ∈ [0.5, 0.9]
