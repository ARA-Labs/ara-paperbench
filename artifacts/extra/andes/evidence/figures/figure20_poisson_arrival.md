# Figure 20: Performance Under Poisson Arrival Distribution
- **Source**: Figure 20, Section 6.4
- **Caption**: (Implied) Average QoE vs request rate under Poisson arrivals.
- **Axis labels**: x-axis = Request Rate (req/s); y-axis = Avg QoE.
- **Model**: Llama 3.1 70B, 8×A100
- **Dataset**: Multi-Round ShareGPT
- **Setup**: Poisson arrival process; request rate varied from 1.0 to 1.4 req/s; 20-minute trace duration.
- **Systems**: Andes, vLLM, LQSF, Sarathi-Serve

## Key Extracted Values

| Request Rate (req/s) | Andes Avg QoE | vLLM Avg QoE | LQSF Avg QoE | Sarathi-Serve Avg QoE |
|---------------------|---------------|--------------|--------------|----------------------|
| 1.0 | ≈ high | ≈ lower | ≈ lower | ≈ lower |
| 1.2 | ≈ high | ≈ lower | ≈ lower | ≈ lower |
| 1.4 | ≈ high | ≈ lower | ≈ lower | ≈ lower |

*Note: Exact numerical QoE values per request rate are not tabulated in the paper text. Trend: "Andes still consistently delivers higher average QoE compared to baselines, particularly under high request rates."*
