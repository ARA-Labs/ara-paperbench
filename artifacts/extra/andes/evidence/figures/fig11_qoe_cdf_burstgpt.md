# Figure 11: QoE, TTFT, and TDS CDFs on BurstGPT
- **Source**: Figure 11, Section 6.2
- **Caption**: "QoE, TTFT, and TDS CDFs of requests in BurstGPT."
- **Model**: Phi-3.5-MoE 16×3.8B on 8× A100 GPUs
- **Trace**: 1-hour BurstGPT slice; Multi-Round ShareGPT dataset

## Key Scalar Values Extracted from Text (§6.2)

| Metric | vLLM (FCFS) | Andes |
|--------|-------------|-------|
| Average QoE | 0.88 | 0.99 |
| Average TTFT (s) | 10.5 | 1.8 |
| Average TDS (tokens/s) | 11.2 | 10.9 |
| Fraction with QoE ≥ 0.95 | 75% | 97% |

## Figure 11a: QoE CDF

| QoE Value | vLLM CDF (≈) | Andes CDF (≈) |
|-----------|-------------|--------------|
| 0.0 | ≈ 0.0 | ≈ 0.0 |
| 0.5 | ≈ 0.10 | ≈ 0.0 |
| 0.80 | ≈ 0.20 | ≈ 0.01 |
| 0.90 | ≈ 0.30 | ≈ 0.02 |
| 0.95 | ≈ 0.25 (25% below) → 75th pctile at 0.95 | ≈ 0.03 (3% below) → 97th pctile at 0.95 |
| 1.0 | ≈ 0.75 | ≈ 0.97 |

**Note**: CDF curve shapes estimated from context. Exact pointwise values not specified in paper text beyond the key statistics above.

## Figure 11b: TTFT CDF
- vLLM has a long tail extending to >10 s
- Andes CDF reaches 1.0 at much lower TTFT values (~few seconds)
- Key reference: vLLM average TTFT = 10.5 s; Andes average TTFT = 1.8 s

## Figure 11c: TDS CDF
- Both vLLM and Andes have most requests above reading speed (4.8 tokens/s)
- vLLM average TDS = 11.2 tokens/s; Andes average TDS = 10.9 tokens/s
- Andes marginally lower TDS (small reduction due to scheduling overhead)
