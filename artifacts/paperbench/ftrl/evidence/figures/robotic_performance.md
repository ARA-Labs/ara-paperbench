# Figure 3c: RoboticSequence Performance (Overall Success Rate over Training Steps)
- **Source**: Figure 3c, Section 4
- **Caption**: "Performance on (c) RoboticSequence. FPC is driven by state coverage gap."
- **Axis labels**: X = training steps (up to ~2e6); Y = success rate (fraction of episodes completing all 4 stages)
- **Conditions**: SAC; 4-stage sequence (hammer→push→peg-unplug-side→push-wall); 20 seeds; 90% confidence intervals; KS omitted

## Data Points (approximate, read from Figure 3c)

| Training Steps | From Scratch | Vanilla Fine-tuning | Fine-tuning + EWC | Fine-tuning + EM | Fine-tuning + BC |
|----------------|-------------|---------------------|------------------|-----------------|-----------------|
| 0 | ≈0 | ≈0 | ≈0 | ≈0 | ≈0 |
| 200K | ≈0 | ≈0 | ≈0.05 | ≈0.05 | ≈0.30 |
| 500K | ≈0 | ≈0 | ≈0.20 | ≈0.25 | ≈0.60 |
| 1M | ≈0.05 | ≈0.05 | ≈0.40 | ≈0.50 | ≈0.80 |
| 1.5M | ≈0.10 | ≈0.10 | ≈0.50 | ≈0.65 | ≈0.80 |
| 2M | ≈0.15 | ≈0.15 | ≈0.55 | ≈0.70 | ≈0.80 |

**Key findings**:
- Fine-tuning + BC achieves ~80% success rate at ~1M steps and plateaus there
- Fine-tuning + EM is close second (~70% at end)
- Fine-tuning + EWC outperforms vanilla FT and from scratch (~55% at end)
- Vanilla FT ≈ from scratch (both ~15% at end); no positive transfer from pre-training
- BC is first to achieve positive success rate; fastest learning curve
