# Figure 15: Average QoE vs. Burst Intensity
- **Source**: Figure 15, Section 6.3
- **Caption**: "Average QoE while varying burst intensity."
- **Axis labels**: X-axis: Intensity (r), range [1.5, 2.0, 2.5]; Y-axis: Avg QoE [0.0, 1.0]
- **Conditions**: 4 models × 3 datasets = 12 sub-panels. Default burst duration = 35%. Systems: Andes, vLLM, LQSF, Sarathi-Serve.
- **Reference line**: Average QoE = 0.95

## Key Quantitative Findings (explicitly stated in text, Section 6.3)

| Metric | Value | System Comparison |
|--------|-------|------------------|
| Peak QoE improvement | 4.7× | Andes vs. vLLM |
| GPU resource savings | 61% | Andes vs. vLLM (to maintain QoE ≥ 0.95) |
| Max concurrent request increase | 2.6× | Andes vs. vLLM (at QoE ≥ 0.95) |
| Realized gain vs. ideal | 1.4× actual / 2.3× ideal ≈ 60% | Andes, Phi-3.5-MoE + ShareGPT |

## Qualitative Observations per Panel
- **All panels**: Andes consistently maintains higher average QoE than vLLM, LQSF, and Sarathi-Serve as intensity increases from 1.5 to 2.5.
- **Sarathi-Serve**: Performs poorly in some configurations due to chunked prefill increasing TTFT.
- **LQSF**: Shows slight improvement over vLLM but falls short of Andes due to not accounting for resource usage.

**Note**: Per-panel exact data points are not tabulated in the paper text. Values of ≈ would require reading from the multi-panel figure image. The explicitly stated numerical results above are exact as given in Section 6.3.
