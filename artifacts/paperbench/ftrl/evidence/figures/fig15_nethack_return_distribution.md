---
# Figure 15: NetHack Return Distribution

**Source**: Figure 15, Appendix D
**Claims**: C04

## Description
Return distribution (histogram/density) for each tested method in NetHack. Mean return is denoted by dashed red line. Shows the full distribution, not just mean, to understand whether high mean scores depend on lucky outlier runs.

## Key Observations by Method

| Method | Distribution Characteristics | Mean (dashed line) |
|--------|------------------------------|-------------------|
| From scratch | Concentrated at low returns (consistent poor performance) | ~776 |
| Vanilla fine-tuning | Slightly higher but still concentrated low | ~647 |
| Fine-tuning + EWC | Wider spread, some medium returns | ~3976 |
| Fine-tuning + BC | Moderate variance; spread to moderate-high returns | ~7610 |
| Fine-tuning + KS | **Highest variance**; some runs reach >50,000 (outlier peaks); significant tail of ~1000 return runs | ~10588 |

## Notes
- Fine-tuning + KS high variance attributed to game stochasticity: "if the first level happens to contain many monsters that are difficult to defeat, that episode may end earlier than expected"
- The mean of 10588 is achieved despite a significant fraction of unlucky low-return (~1000) runs
- Fine-tuning + KS has observed returns as high as 50,000 (exceptional lucky runs)
- Training from scratch and vanilla fine-tuning have consistently low returns with narrow distribution
