---
source: "Figure 8, Section 4.5 of arXiv:2506.22419"
claims_verified: [C02]
---

# Figure 8: Search Tree Dynamics

Fraction of buggy, improved, and unimproved nodes as a function of search step, per model.

## Data

| Model | Step 1 Buggy% | Step 10 Buggy% | Step 20 Buggy% | Trend |
|-------|--------------|----------------|----------------|-------|
| o3-mini | 40% | 25% | 15% | Decreasing (effective self-correction) |
| DeepSeek-R1 | 45% | 30% | 25% | Decreasing (slower correction) |
| Gemini-2.5-Pro | 30% | 22% | 18% | Decreasing (most robust code) |
| Claude-3.7-Sonnet | 35% | 42% | 50% | **Increasing** (unique degradation) |

## Key Observations

- **o3-mini**: Buggy fraction decreases steadily; improved fraction increases. Most effective at learning from failed attempts and producing working code in later iterations.
- **DeepSeek-R1**: Buggy fraction decreases but remains higher than o3-mini. Self-correction is present but slower.
- **Gemini-2.5-Pro**: Lowest initial buggy fraction (most conservative/robust code generation), but also lower improved fraction (less ambitious edits).
- **Claude-3.7-Sonnet**: **Uniquely increasing buggy fraction** -- the only model that gets worse at self-correction over time. Later iterations produce more broken code than earlier ones. This suggests Claude may over-commit to failing strategies or introduce cascading errors through overly ambitious edits.

## Visualization Type

Stacked area chart, one panel per model. X-axis: search step (1-20). Y-axis: fraction of nodes. Three stacked areas: buggy (red), unimproved (yellow), improved (green).
