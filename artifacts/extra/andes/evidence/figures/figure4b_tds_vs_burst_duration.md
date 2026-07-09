# Figure 4b: vLLM Average TDS vs. Burst Duration
- **Source**: Figure 4b, Section 2.2
- **Caption**: "vLLM's average TTFT and TDS while varying the duration of the load surge in our 20-minute trace. User reading/listening speeds are 4.8 and 3.3 tokens/s, derived from Figure 2."
- **Axis labels**: X-axis: Burst duration (min); Y-axis: Average TDS (tokens/s)
- **Reference lines**: Reading speed = 4.8 tokens/s; Listening speed = 3.3 tokens/s
- **Model**: Phi-3.5-MoE 16×3.8B on 8× A100

| Burst Duration (min) | Average TDS (tokens/s) | Notes |
|---------------------|----------------------|-------|
| 0 (no burst) | ≈11–12 | Well above reading speed |
| 2 | ≈11 | Well above reading speed |
| 4 | ≈11 | Approximately constant |
| 6 | ≈11 | Approximately constant |
| 8 | ≈11 | Approximately constant |
| 10 | ≈11 | Approximately constant |
| 12 | ≈11 | Approximately constant |

**Key stated value**: "vLLM's average TDS is 11.2 tokens/s" (Section 2.2, BurstGPT trace). The figure demonstrates that TDS "consistently exceeds any reasonable user token consumption speed, even under severe load surges."
