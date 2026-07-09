---
# Figure 6: Montezuma's Revenge Room 7 Success Rate

**Source**: Figure 6, §5
**Claims**: C01, C02, C03

## Description
Success rate in Room 7 throughout fine-tuning for all methods. Room 7 is the first room observed during pre-training; its success rate measures how much pre-trained FAR-state knowledge is retained.

Success = achieving at least one of: earn a coin as a reward, acquire a new item, or exit the room through a different passage.

## Data Points (Qualitative, Approximate)
- **X-axis**: Environment steps (0 to ~1e8)
- **Y-axis**: Success rate in Room 7 (0 to 1)

| Method | Initial (~0 steps) | At ~2e7 steps | Final (~1e8 steps) |
|--------|-------------------|--------------|-------------------|
| Pre-trained π* (frozen) | ~0.8 | ~0.8 | ~0.8 (baseline) |
| Fine-tuning + BC | ~0.8 | ~0.75 | ~0.75 (stable) |
| Fine-tuning + EWC | ~0.8 | ~0.70 | ~0.70 (stable) |
| Vanilla fine-tuning | ~0.8 | ~0.55 (drop) | ~0.65 (partial recovery) |

## Key Observations
- Vanilla fine-tuning Room 7 success rate drops to ~0.55 after ~2e7 steps (FPC manifesting)
- BC and EWC maintain fairly constant success rate (~0.75-0.80), rarely fluctuating more than ±0.10
- Vanilla fine-tuning starts recovering after ~20M steps when agent first re-enters Room 7
- Vanilla fine-tuning does not reach the performance of π* even after recovery
- KS is not shown (underperforms for state coverage gap)
