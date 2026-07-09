# Figure 16: Average QoE vs Burst Duration
- **Source**: Figure 16, Section 6.3
- **Caption**: "Average QoE while varying burst duration."
- **Axis labels**: x-axis = Duration (%); y-axis = Avg QoE.
- **Layout**: 4 models (rows) × 3 datasets (columns) = 12 subplots.
- **Systems compared**: Andes, vLLM, LQSF, Sarathi-Serve
- **Setup**: Cyclic burst load pattern; default burst intensity = 2×; burst duration varied.

## Key Extracted Values

| Metric | Value | Source |
|--------|-------|--------|
| Andes max QoE improvement vs vLLM under varying burst duration | up to 3.5× | Section 6.3 text |
| Andes consistency | Higher average QoE across all models and datasets | Section 6.3 text |

*Note: Individual per-subplot data points at each duration value are not numerically tabulated in the paper text.*
