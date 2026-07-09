---
# Table 6: Forward Transfer vs Prefix Length in RoboticSequence

**Source**: Table 6, Appendix F
**Caption**: Forward transfer on the pre-trained tasks depending on the number of prefix tasks in RoboticSequence.

| Prefix Len | push-wall (FT) | push-wall (EWC) | push-wall (BC) | peg-unplug-side (FT) | peg-unplug-side (EWC) | peg-unplug-side (BC) |
|-----------|---------------|----------------|---------------|---------------------|----------------------|---------------------|
| 1 | 0.18 [-0.19, 0.43] | 0.88 [0.84, 0.91] | 0.93 [0.89, 0.96] | 0.28 [0.01, 0.46] | 0.77 [0.58, 0.88] | 0.92 [0.88, 0.94] |
| 2 | 0.17 [-0.21, 0.44] | 0.65 [0.44, 0.82] | 0.97 [0.97, 0.98] | 0.15 [-0.08, 0.35] | 0.55 [0.37, 0.70] | 0.95 [0.94, 0.96] |
| 3 | 0.10 [-0.03, 0.23] | 0.64 [0.50, 0.75] | 0.98 [0.98, 0.98] | 0.03 [0.00, 0.06] | 0.41 [0.28, 0.54] | 0.95 [0.95, 0.95] |
| 4 | -0.00 [-0.16, 0.10] | 0.62 [0.48, 0.75] | 0.97 [0.97, 0.98] | 0.03 [-0.00, 0.08] | 0.46 [0.33, 0.59] | 0.94 [0.94, 0.95] |

## Notes
- Forward Transfer (FT) metric: (AUC_method - AUC_scratch) / (1 - AUC_scratch); higher is better
- Values shown as mean [90% CI] over ≥20 seeds
- **FT column**: Vanilla fine-tuning; forward transfer decreases monotonically as prefix length increases
- **BC column**: BC maintains high forward transfer (~0.93-0.98) regardless of prefix length
- **EWC column**: EWC degrades with more prefix tasks but consistently outperforms vanilla FT
- Negative FT (e.g., -0.00 for vanilla FT, prefix=4) indicates no benefit over training from scratch
- Prefix tasks are suffixes of: window-close, faucet-close, hammer, push
