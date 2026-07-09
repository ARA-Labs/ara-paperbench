# Figure 19: QoE Gain Estimation Time Horizon (Δt) Sensitivity
- **Source**: Figure 19, Section 6.4
- **Caption**: (Implied) Average QoE vs Δt values.
- **Axis labels**: x-axis = Δt (implied); y-axis = Avg QoE.
- **Model**: Llama 3.1 70B, 8×A100
- **Dataset**: Multi-Round ShareGPT
- **Systems**: Andes, vLLM, LQSF, Sarathi-Serve

## Key Observations

| Observation | Value |
|-------------|-------|
| Andes QoE sensitivity to Δt | "roughly consistent for various Δt values" |
| Andes vs baselines | Significantly outperforms all baselines across all Δt values |
| Tuning recommendation | Best Δt depends on model and request input/output distribution; requires pre-deployment tuning |

*Note: Exact Δt range and per-Δt QoE values are not numerically tabulated in the paper text.*
