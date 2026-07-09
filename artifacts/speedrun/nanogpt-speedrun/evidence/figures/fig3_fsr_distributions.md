---
source: "Figure 3, Section 4.1 of arXiv:2506.22419"
claims_verified: [C02, C06]
---

# Figure 3: FSR Distributions Across Models and Hint Levels

Distribution of Fraction of Speedup Recovered (FSR) across 19 records for each model and hint level combination.

## Summary Statistics

| Model | Hint Level | Median FSR | IQM FSR | Distribution Shape |
|-------|-----------|------------|---------|-------------------|
| o3-mini | L1 | 0.40 | 0.43 | Tight, centered ~0.35-0.43 |
| o3-mini | Zero-K | 0.10 | 0.16 | Wide, long left tail |
| DeepSeek-R1 | L1+L2+L3 | 0.35 | 0.46 | Wide bimodal (some high, many zero) |
| DeepSeek-R1 | Zero-K | 0.12 | 0.18 | Wide bimodal |
| Gemini-2.5-Pro | L1 | 0.18 | 0.22 | Moderate width, fewer buggy runs |
| Claude-3.7-Sonnet | L1 | 0.08 | 0.12 | Skewed toward 0, high variance |

## Key Observations

- **o3-mini**: Most consistent performer. Tightest distributions with smallest variance. L1 hints produce a reliable ~0.40 FSR.
- **DeepSeek-R1**: Bimodal -- either achieves high FSR or fails completely. High variance indicates "boom or bust" behavior.
- **Gemini-2.5-Pro**: Most conservative code generation. Lowest buggy fraction but also lower peak FSR.
- **Claude-3.7-Sonnet**: Majority of records achieve zero or near-zero FSR. High buggy fraction.

## Visualization Type

Violin/box plots, one per (model, hint_level) combination. Y-axis: FSR [0, 1].
