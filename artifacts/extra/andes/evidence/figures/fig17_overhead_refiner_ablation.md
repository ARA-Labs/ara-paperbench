# Figure 17: Overhead-Aware Refiner Ablation
- **Source**: Figure 17, Section 6.4
- **Caption**: "Overhead-aware refiner is critical to optimize QoE."
- **Model**: Llama 3.1 70B; Multi-Round ShareGPT dataset; default cyclic burst load (intensity=2.0×)
- **Systems**: vLLM, Andes (full), Andes without overhead-aware refiner
- **X-axis**: Burst duration (%)
- **Y-axes**: Average QoE (top), Average preemptions per request (bottom)

## Qualitative Descriptions from Paper

| System | QoE trend with increasing burst duration | Preemptions per request trend |
|--------|------------------------------------------|------------------------------|
| vLLM | Low baseline QoE; roughly flat | 0 (no preemptions; FCFS) |
| Andes (full) | High QoE; maintained stably | Controlled; moderate |
| Andes w/o overhead-aware refiner | Decreasing significantly with burst duration | Increasing sharply (excessive) |

## Key Observation (§6.4)
"Andes without the overhead-aware refiner makes scheduling decisions that are unaware of preemption overhead. As such, it incurs excessive preemptions with the increase of burst duration, which delays token generation for ongoing requests and thus significantly degrading QoE."

**Note**: Exact numerical QoE and preemption count values per burst duration data point are not stated in the paper text; results are presented as line plots.
