# Figure 15: Average QoE vs Burst Intensity
- **Source**: Figure 15, Section 6.3
- **Caption**: "Average QoE while varying burst intensity."
- **Axis labels**: x-axis = Intensity (r); y-axis = Avg QoE. Reference line at QoE = 0.95.
- **Layout**: 4 models (rows) × 3 datasets (columns) = 12 subplots.
- **Systems compared**: Andes, vLLM, LQSF, Sarathi-Serve
- **Setup**: Cyclic burst load pattern; default burst duration = 35%; burst intensity varied over [1.5, 2.0, 2.5]; average rate = system throughput at no burstiness.

## Key Extracted Values

| Metric | Value | Source |
|--------|-------|--------|
| Andes max QoE improvement vs vLLM | up to 4.7× | Section 6.3 text |
| Andes max burst intensity vs vLLM at QoE = 0.95 | up to 2.6× higher | Section 6.3 text |
| GPU savings (Andes vs vLLM at QoE = 0.95) | up to 61% | Section 6.3 text |

## Observed Trends (exact per-subplot curve values not numerically tabulated in paper)
| Observation | Details |
|-------------|---------|
| Andes maintains high QoE as intensity increases across all model/dataset combos | Confirmed in Figure 15 |
| Sarathi-Serve performs poorly in some cases | Chunked prefill interferes with TTFT |
| LQSF shows slight improvement over FCFS | Lacks resource-usage awareness |
| Gap between Andes and FCFS baselines widens with intensity | Head-of-line blocking worsens |

*Note: Individual data points for each subplot at each intensity value are not numerically tabulated in the paper text.*
