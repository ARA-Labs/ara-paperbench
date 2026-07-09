---
source: "Figure 1, Section 1 of arXiv:2506.22419"
claims_verified: [C01]
---

# Figure 1: NanoGPT Speedrun Timeline

Timeline of NanoGPT speedrun records showing training time reduction from ~50 min to ~3 min.

## Data Points

| Record | Date (approx.) | Train Time (min) | Key Milestone |
|--------|----------------|-----------------|---------------|
| 1 | Jun 2024 | 49.5 | Baseline (standard GPT-2 + AdamW) |
| 3 | Jun 2024 | 23.1 | Muon optimizer introduced |
| 5 | Jul 2024 | 15.8 | Architectural overhaul (ReLU², vocab padding) |
| 10 | Aug 2024 | 8.0 | Precision engineering (bfloat16 + refined U-Net) |
| 12 | Aug 2024 | 5.3 | FlexAttention + 64K context |
| 15 | Sep 2024 | 4.0 | GQA + tightened sliding window |
| 21 | Oct 2024 | 3.1 | Final record |

## Visualization

- **Type**: Line chart with record index on x-axis, training time on y-axis (log scale)
- **Annotations**: Key innovations labeled at each major milestone
- **Key observation**: Diminishing returns -- early records achieve large absolute speedups, later records achieve smaller but harder-won improvements
- **Curve shape**: Roughly exponential decay; each phase contributes a roughly constant multiplicative factor (1.5-2.5x)
