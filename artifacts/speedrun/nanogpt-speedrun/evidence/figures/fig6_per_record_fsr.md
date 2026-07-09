---
source: "Figure 6, Section 4.2 of arXiv:2506.22419"
claims_verified: [C02, C08]
---

# Figure 6: FSR vs. Record Index

FSR as a function of record index, showing monotonic difficulty increase across all models.

## Trend Summary

| Record Range | Description | Best Model FSR | Difficulty |
|-------------|-------------|----------------|-----------|
| 1-3 | Optimizer changes (RoPE, Muon) | ~0.50-0.60 | Easy |
| 4-5 | Architecture changes (multi-component) | ~0.30-0.40 | Moderate |
| 6-8 | Distributed + systems (cuDNN, U-Net) | ~0.15-0.25 | Hard |
| 9-11 | Precision + FlexAttention intro | ~0.05-0.15 | Very Hard |
| 12-15 | FlexAttention optimization + advanced | ~0.02-0.05 | Extremely Hard |
| 16-19 | Hardware-specific (FP8, custom CUDA) | ~0.00-0.03 | Near-Impossible |

## Key Observations

- **Monotonic difficulty increase**: FSR consistently decreases with record index for all models
- **Record 12 cliff**: FlexAttention integration is a sharp difficulty boundary. Requires unfamiliar API knowledge beyond typical training data.
- **Difficulty taxonomy**: Standard optimizer tweaks (records 1-3) are feasible; multi-component architecture changes (records 4-8) are partially feasible; systems/hardware engineering (records 9+) is essentially infeasible for current agents.
- **Model ordering preserved**: o3-mini > DeepSeek-R1 > Gemini-2.5-Pro > Claude-3.7-Sonnet at every record range.

## Visualization Type

Line chart, x-axis: record index (1-19), y-axis: FSR. Multiple colored lines for different models. Shaded confidence bands.
