---
source: "Figure 6, Section 4.2 of arXiv:2506.22419"
claims_verified: [C02, C06, C08]
---

# Table 6: Per-Record FSR by Model (Multi-AIDE + L1 Hints)

Mean FSR grouped by record range, showing monotonic difficulty increase.

| Record Range | Innovation Type | o3-mini FSR | DeepSeek-R1 FSR | Gemini-2.5-Pro FSR | Claude-3.7-Sonnet FSR |
|-------------|----------------|-------------|-----------------|--------------------|-----------------------|
| 1-5 | Optimizer + early arch | 0.45 | 0.38 | 0.25 | 0.15 |
| 6-11 | Architecture + precision | 0.20 | 0.15 | 0.10 | 0.05 |
| 12-15 | FlexAttention + advanced | 0.05 | 0.03 | 0.02 | 0.01 |
| 16-19 | Hardware-specific | 0.03 | 0.02 | 0.01 | 0.00 |

## Key Observations

- **Sharp cliff at Record 12 (FlexAttention)**: Requires knowledge beyond typical model training data (PyTorch nightly API, custom block masking). FSR drops to near-zero for all models.
- **Difficulty correlates with innovation type**: Standard optimizer/architecture changes (early records) are easier than hardware-specific kernel optimizations (late records).
- **All models converge to zero**: By records 16+, no model makes meaningful progress regardless of hint level.
- **o3-mini advantage concentrated in early records**: The gap between o3-mini and other models is largest for records 1-5 where optimization patterns are more standard.
