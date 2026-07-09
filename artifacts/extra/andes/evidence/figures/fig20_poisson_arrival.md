# Figure 20: Poisson Arrival Distribution
- **Source**: Figure 20, Section 6.4
- **Caption**: "Poisson arrival."
- **Model**: Llama 3.1 70B; Multi-Round ShareGPT dataset; 20-minute trace duration
- **Systems**: Andes, vLLM, LQSF, Sarathi-Serve
- **X-axis**: Request rate (req/s), range approximately 1.0–1.4 req/s
- **Y-axis**: Average QoE

## Key Observation (§6.4)
"Andes still consistently delivers higher average QoE compared to baselines, particularly under high request rates."

| Request Rate (req/s) | Andes QoE (≈) | vLLM QoE (≈) | Observation |
|---------------------|--------------|-------------|-------------|
| ~1.0 | ≈ 0.95–1.0 | ≈ 0.90–0.95 | Small gap at low rates |
| ~1.2 | ≈ 0.90–0.95 | ≈ 0.75–0.85 | Gap widens |
| ~1.4 | ≈ 0.85–0.90 | ≈ 0.60–0.75 | Significant gap at high rates |

**Note**: Exact per-data-point values estimated from context; not stated in paper text. Results shown as line plot.
