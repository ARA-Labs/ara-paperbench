# Figure 4: vLLM Average TTFT and TDS vs Burst Duration
- **Source**: Figure 4, Section 2.2
- **Caption**: "vLLM's average TTFT and TDS while varying the duration of the load surge in our 20-minute trace. TTFT target is set to 1.3 s, as recommended by Google for web page loading. User reading/listening speeds are 4.8 and 3.3 tokens/s, derived from Figure 2."
- **Axis labels**: (a) x-axis = Burst duration (min); y-axis = Average TTFT (s). (b) x-axis = Burst duration (min); y-axis = Average TDS (tokens/s).
- **Model**: Phi-3.5-MoE 16×3.8B, 8×A100
- **Setup**: Synthetic 20-minute traces with load surges of varying durations; multi-Round ShareGPT dataset.

## Reference Lines
| Metric | Reference Value | Description |
|--------|----------------|-------------|
| Target TTFT | 1.3 s | Google web page loading recommendation |
| Reading speed | 4.8 tokens/s | User reading speed reference |
| Listening speed | 3.3 tokens/s | User listening speed reference |

## Key Observations (exact curve values not readable from text description)
| Observation | Value | Source |
|-------------|-------|--------|
| vLLM average TTFT at moderate burst (10 min duration) | ≈ significantly inflated above 1.3s | Figure 4a text |
| vLLM TDS at moderate burst | ≈ 11 tokens/s | Section 2.3 ("server generates 11 tokens/s under moderate load surges with burst duration 10 minutes") |
| Ideal preemption multiplier at 10-min burst | 2.3× | Section 2.3 (11/4.8 = 2.3) |

*Note: Exact per-burst-duration curve values for TTFT and TDS are not numerically tabulated in the paper text.*
