# Figure 17: Overhead-Aware Refiner Ablation
- **Source**: Figure 17, Section 6.4
- **Caption**: "Overhead-aware refiner is critical to optimize QoE."
- **Axis labels**: Top panel: x-axis = Duration (%); y-axis = Avg QoE. Bottom panel: x-axis = Duration (%); y-axis = Preemption per request.
- **Model**: Llama 3.1 70B, 8×A100
- **Dataset**: Multi-Round ShareGPT
- **Setup**: Default cyclic burst load; burst intensity = 2×; burst duration varied [25%, 30%, 35%, 40%, 45%].
- **Systems**: Andes (with overhead-aware refiner), Andes without overhead-awareness, vLLM

## Key Observations

| Observation | Value |
|-------------|-------|
| Burst duration range tested | 25%, 30%, 35%, 40%, 45% |
| Andes without overhead: preemptions per request trend | Increases steeply with burst duration |
| Andes with overhead: QoE | Consistently high across all durations |
| Andes without overhead: QoE | Significantly degrades as burst duration increases |
| vLLM: QoE | Low baseline across all durations |

*Note: Exact QoE values and preemption counts per duration tick are not numerically tabulated in the paper text; directional trends are described.*
