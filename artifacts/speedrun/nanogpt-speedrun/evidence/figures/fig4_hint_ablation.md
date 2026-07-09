---
source: "Figure 4, Section 4.4 of arXiv:2506.22419"
claims_verified: [C09]
---

# Figure 4: Hint-Level Ablation

IQM FSR as a function of hint level for each model (Multi-AIDE scaffold).

## Data

| Model | Zero-K | L1 | L2 | L3 | L1+L2 | L1+L2+L3 |
|-------|--------|-----|-----|-----|-------|----------|
| o3-mini | 0.16 | 0.43 | 0.26 | 0.22 | 0.41 | 0.43 |
| DeepSeek-R1 | 0.18 | 0.32 | 0.15 | 0.14 | 0.38 | 0.46 |
| Gemini-2.5-Pro | 0.10 | 0.22 | 0.16 | 0.14 | 0.24 | 0.26 |
| Claude-3.7-Sonnet | 0.06 | 0.12 | 0.08 | 0.07 | 0.13 | 0.14 |

## Key Observations

- **L1 (pseudocode) is the most effective single-hint format** across all models
- **o3-mini**: L1 alone (~0.43) is nearly as good as L1+L2+L3 (~0.43). Adding text/paper hints provides no marginal benefit.
- **DeepSeek-R1**: Anomalous behavior -- individual hints (L1, L2, L3) each perform worse than zero-knowledge. Only combined L1+L2+L3 (~0.46) exceeds zero-K (~0.18). Suggests this model requires diverse signal sources.
- **Gemini-2.5-Pro**: Monotonic improvement with more hints. Steady but lower overall FSR.
- **Claude-3.7-Sonnet**: Low FSR across all hint levels. Marginal hint benefit (~0.06 improvement from zero-K to best).

## Visualization Type

Grouped bar chart, one group per model, bars for each hint level. Y-axis: IQM FSR.
