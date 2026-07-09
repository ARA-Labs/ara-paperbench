# Figure 4a: vLLM Average TTFT vs. Burst Duration
- **Source**: Figure 4a, Section 2.2
- **Caption**: "vLLM's average TTFT and TDS while varying the duration of the load surge in our 20-minute trace. TTFT target is set to 1.3 s, as recommended by Google for web page loading [5]."
- **Axis labels**: X-axis: Burst duration (min); Y-axis: Average TTFT (s)
- **Target line**: 1.3 s (Google-recommended TTFT target)
- **Model**: Phi-3.5-MoE 16×3.8B on 8× A100
- **Experimental conditions**: 20-minute synthetic trace with cyclic burst; average rate set to system throughput; burst rate varied by duration.

| Burst Duration (min) | Average TTFT (s) | Notes |
|---------------------|-----------------|-------|
| 0 (no burst) | ≈1.3 | ≈ at target line |
| 2 | ≈3 | Above target |
| 4 | ≈5 | Well above target |
| 6 | ≈7 | Well above target |
| 8 | ≈8.5 | Well above target |
| 10 | ≈9 | Well above target |
| 12 | ≈9.5 | Approximate plateau |

**Note**: Exact data points are approximate (≈) as the figure is a line plot in the paper and exact values are not tabulated in the text. The paper states "average TTFT of 10.4 seconds" for the full BurstGPT trace (not this synthetic trace). The figure demonstrates that TTFT is "significantly inflated due to head-of-line blocking, even under moderate load surges."
