# Figure 4: vLLM Average TTFT and TDS Under Varying Burst Duration
- **Source**: Figure 4, Section 2.2
- **Caption**: "vLLM's average TTFT and TDS while varying the duration of the load surge in our 20-minute trace. TTFT target is set to 1.3 s, as recommended by Google for web page loading [5]. User reading/listening speeds are 4.8 and 3.3 tokens/s, derived from Figure 2."
- **Model**: Phi-3.5-MoE 16×3.8B on 8× A100 GPUs
- **Trace**: Synthetic 20-minute traces with varying burst duration

## Figure 4a: Average TTFT vs. Burst Duration

| Burst Duration (min) | vLLM Average TTFT (s) | Target TTFT (s) |
|---------------------|-----------------------|-----------------|
| 0 (no burst) | ≈ 1.3 | 1.3 |
| ~2 | ≈ 2–3 (significantly inflated) | 1.3 |
| ~5 | ≈ 5–7 (approximate) | 1.3 |
| ~10 | ≈ 8–12 (approximate) | 1.3 |
| ~15 | ≈ 12–15 (approximate) | 1.3 |

**Reference value from text (§2.2)**: Average TTFT of 10.4 s on BurstGPT (1-hour trace); consistent with figure trend.

**Note**: Exact curve values cannot be read precisely from the figure description in the paper text. Values marked "≈" are best-effort estimates from context. The key observation stated in text: "TTFT is significantly inflated due to head-of-line blocking, even under moderate load surges."

## Figure 4b: Average TDS vs. Burst Duration

| Burst Duration (min) | vLLM Average TDS (tokens/s) | Reading Speed (tokens/s) | Listening Speed (tokens/s) |
|---------------------|----------------------------|--------------------------|---------------------------|
| 0 (no burst) | ≈ 11 | 4.8 | 3.3 |
| ~5 | ≈ 11 | 4.8 | 3.3 |
| ~10 | ≈ 11 | 4.8 | 3.3 |
| ~15 | ≈ 11 | 4.8 | 3.3 |

**Reference value from text (§2.2)**: vLLM average TDS = 11.2 tokens/s on BurstGPT.
**Key observation**: "TDS consistently exceeds any reasonable user token consumption speed, even under severe load surges."
