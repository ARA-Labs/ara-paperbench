# Figure 16: Average QoE vs. Burst Duration
- **Source**: Figure 16, Section 6.3
- **Caption**: "Average QoE while varying burst duration."
- **Systems**: Andes, vLLM, LQSF, Sarathi-Serve
- **Models**: Phi-3-mini 3.8B, Command R 32B, Phi-3.5-MoE 16×3.8B, Llama 3.1 70B
- **Datasets**: ShareGPT, ArXiv, Coding
- **Burst duration range**: ~25%–45% of cycle; burst intensity fixed at 2.0×

## Key Scalar Values from Text (§6.3)

| Metric | Value |
|--------|-------|
| Maximum QoE improvement (Andes vs. vLLM, burst duration sweep) | 3.5× |

## Qualitative Pattern
- Andes consistently provides higher average QoE across all models and datasets
- QoE generally decreases with increasing burst duration for all systems
- Andes degradation is much slower than baselines
- LQSF shows slight improvement over vLLM; Sarathi-Serve variable

**Note**: Exact per-cell QoE values are shown as line plots in Figure 16; numerical values per data point are not reported in the paper text.
