# Figure 3a: NetHack Performance (Average Return over Training Steps)
- **Source**: Figure 3a, Section 4
- **Caption**: "Performance on (a) NetHack. The FPC is driven by imperfect cloning gap."
- **Axis labels**: X = training steps (environment steps); Y = average return (in-game score)
- **Conditions**: Human Monk scenario; APPO; 5 seeds per method; shaded regions = confidence intervals

## Data Points (approximate, read from Figure 3a)

| Training Steps | Pre-trained π* (frozen) | From Scratch | Vanilla Fine-tuning | Fine-tuning + EWC | Fine-tuning + BC | Fine-tuning + KS |
|----------------|------------------------|-------------|---------------------|------------------|-----------------|-----------------|
| 0 | ≈5000 | ≈0 | ≈5000 | ≈5000 | ≈5000 | ≈5000 |
| 100M | ≈5000 | ≈1000 | ≈2000 | ≈3000 | ≈4000 | ≈5500 |
| 200M | ≈5000 | ≈2000 | ≈1500 | ≈3500 | ≈5000 | ≈7000 |
| 300M | ≈5000 | ≈3000 | ≈1000 | ≈4000 | ≈6000 | ≈8500 |
| 400M | ≈5000 | ≈4000 | ≈1000 | ≈4000 | ≈7000 | ≈10000 |
| 500M | ≈5000 | ≈5000 | ≈1000 | ≈3500 | ≈7500 | ≈11000 |

**Key findings**:
- Fine-tuning + KS achieves highest final score, surpassing pre-trained SOTA (~5K) by ~2×
- Fine-tuning + BC is second-best, also surpasses pre-trained baseline
- Vanilla fine-tuning collapses to ~1K early in training and fails to recover
- EWC temporarily maintains performance but deteriorates after ~300M steps
- Final evaluation (Table 4): Fine-tuning + KS = 10,588 ± 672
