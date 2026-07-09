# Figure 3b: Montezuma's Revenge Performance (Average Return over Training Steps)
- **Source**: Figure 3b, Section 4
- **Caption**: "Performance on (b) Montezuma's Revenge. FPC is driven by state coverage gap."
- **Axis labels**: X = training steps (environment steps, up to ~5e7); Y = average return
- **Conditions**: PPO+RND; pre-trained from Room 7 onward; fine-tuned on full game from Room 1; 5 seeds; KS omitted (underperforms)

## Data Points (approximate, read from Figure 3b)

| Training Steps | From Scratch (PPO) | Vanilla Fine-tuning | Fine-tuning + EWC | Fine-tuning + BC |
|----------------|-------------------|---------------------|------------------|-----------------|
| 0 | ≈0 | ≈7000 | ≈7000 | ≈7000 |
| 5M | ≈500 | ≈4000 | ≈6500 | ≈6500 |
| 10M | ≈1000 | ≈2500 | ≈5500 | ≈6000 |
| 20M | ≈1500 | ≈2000 | ≈5000 | ≈5500 |
| 30M | ≈2000 | ≈3000 | ≈5000 | ≈5800 |
| 40M | ≈2500 | ≈3500 | ≈5000 | ≈6000 |
| 50M | ≈3000 | ≈4000 | ≈5000 | ≈6000 |

**Key findings**:
- Fine-tuning + BC achieves highest average return (~6000) at end of training
- Fine-tuning + EWC converges faster than vanilla FT but saturates at ~5000
- Vanilla FT performance drops sharply at ~5–10M steps (initial forgetting) before recovering when agent enters Room 7 at ~20M steps
- BC diverges from vanilla FT at ~20M steps when agent first enters Room 7
- All fine-tuning methods outperform training from scratch by end of training
