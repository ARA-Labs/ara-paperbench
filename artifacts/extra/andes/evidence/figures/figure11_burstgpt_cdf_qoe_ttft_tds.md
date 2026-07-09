# Figure 11: QoE, TTFT, and TDS CDFs on BurstGPT
- **Source**: Figure 11, Section 6.2
- **Caption**: "QoE, TTFT, and TDS CDFs of requests in BurstGPT."
- **Axis labels**: (a) x-axis = QoE; y-axis = CDF. (b) x-axis = TTFT (s); y-axis = CDF. (c) x-axis = TDS (#Token/s); y-axis = CDF.
- **Model**: Phi-3.5-MoE 16×3.8B, 8×A100
- **Dataset**: Multi-Round ShareGPT; one-hour BurstGPT trace

## Key Extracted Values

### Figure 11a: QoE CDF
| System | Average QoE | % Requests with QoE ≥ 0.95 |
|--------|-------------|---------------------------|
| Andes | 0.99 | 97% |
| vLLM | 0.88 | 75% |

### Figure 11b: TTFT
| System | Average TTFT (s) |
|--------|-----------------|
| Andes | 1.8 |
| vLLM | 10.5 |

### Figure 11c: TDS
| System | Average TDS (tokens/s) |
|--------|----------------------|
| Andes | 10.9 |
| vLLM | 11.2 |

*Note: Full CDF curve data points are not numerically tabulated in the paper text; only the summary statistics above are explicitly stated.*
