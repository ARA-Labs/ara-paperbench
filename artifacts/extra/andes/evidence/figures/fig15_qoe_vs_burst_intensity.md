# Figure 15: Average QoE vs. Burst Intensity
- **Source**: Figure 15, Section 6.3
- **Caption**: "Average QoE while varying burst intensity."
- **Systems**: Andes, vLLM, LQSF, Sarathi-Serve
- **Models**: Phi-3-mini 3.8B, Command R 32B, Phi-3.5-MoE 16×3.8B, Llama 3.1 70B
- **Datasets**: ShareGPT, ArXiv, Coding
- **Burst intensity range**: 1.5× to 2.5×; burst duration fixed at 35%

## Key Scalar Values from Text

| Metric | Value |
|--------|-------|
| Maximum QoE improvement (Andes vs. vLLM) | 4.7× |
| Maximum burst intensity Andes sustains at QoE ≥ 0.95 vs. vLLM | 2.6× more |
| GPU savings at same QoE = 0.95 | up to 61% |

## Qualitative Curve Descriptions (Figure 15)

All models × all datasets follow the same qualitative pattern:
- **Andes**: QoE remains near 1.0 at low intensity; degrades gradually at high intensity; consistently highest
- **LQSF**: Slight improvement over vLLM and Sarathi-Serve; still falls significantly below Andes
- **vLLM**: QoE degrades sharply with increasing intensity due to FCFS head-of-line blocking
- **Sarathi-Serve**: Performs poorly in some cases (ArXiv long inputs especially) due to chunked prefill increasing TTFT

**Note**: Exact per-cell (model, dataset, intensity, system) QoE values are not reported as numbers in the paper text; the results are presented as line plots in Figure 15. The 4.7× maximum and 2.6× burst capacity values are stated explicitly in §6.3.
