# Figure 16: Average QoE vs. Burst Duration
- **Source**: Figure 16, Section 6.3
- **Caption**: "Average QoE while varying burst duration."
- **Axis labels**: X-axis: Duration (%); Y-axis: Avg QoE [0.6, 1.0]
- **Conditions**: 4 models × 3 datasets = 12 sub-panels. Default burst intensity = 2. Systems: Andes, vLLM, LQSF, Sarathi-Serve.

## Key Quantitative Finding (explicitly stated in text, Section 6.3)

| Metric | Value | System Comparison |
|--------|-------|------------------|
| Peak QoE improvement over burst duration sweep | up to 3.5× | Andes vs. vLLM |

## Qualitative Observations
- Andes consistently provides higher average QoE across all models and request datasets as burst duration varies.
- All systems degrade more as burst duration increases; Andes degrades least.

**Note**: Per-panel exact data points are not tabulated in the paper text. The 3.5× figure is the single explicitly stated result from the burst duration experiments.
