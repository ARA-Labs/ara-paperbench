---
# Figure 2: PPO Performance vs. Batch Size (Saturation Plot)

- **Source**: Figure 2, Section 1 / Section 3
- **Caption**: "Performance vs batch size plot for PPO runs (blue curve) across two environments. The curve shows how PPO training runs can not take benefit of large batch size resulting from massively parallelized environments and their asymptotic performance saturates after a certain point. The dashed red line is the performance of our method, SAPG, with more details in the results section."
- **Axis labels**: X-axis: Batch size (number of parallel environments); Y-axis: Asymptotic performance
- **Curves**: Blue = PPO, Red dashed = SAPG (reference line)

## Shadow Hand — Asymptotic Performance vs. Batch Size

| Batch Size (approx.) | PPO Asymptotic Performance |
|---------------------|---------------------------|
| ≈1500 | ≈2000 |
| ≈3125 | ≈4000 |
| ≈6250 | ≈6000 |
| ≈12500 | ≈8000 |
| ≈25000 | ≈10000 |
| ≈50000 | ≈9500 |
| ≈100000 | ≈9000 |

Note: Values are approximate (≈) visual reads from Figure 2 (left panel). Exact values not provided in paper.

SAPG reference (dashed red line): above 12,000 (exact value from Table 1: SAPG λ=0.005 = 1.28e4 ± 2.80e2)

## Allegro Kuka Throw — Asymptotic Performance vs. Batch Size

| Batch Size (approx.) | PPO Asymptotic Performance |
|---------------------|---------------------------|
| ≈1500 | ≈2 |
| ≈3125 | ≈5 |
| ≈6250 | ≈10 |
| ≈12500 | ≈14 |
| ≈25000 | ≈17 |
| ≈50000 | ≈16 |
| ≈100000 | ≈15 |

Note: Values are approximate (≈) visual reads from Figure 2 (right panel). Exact values not provided in paper.

SAPG reference (dashed red line): approximately 23-24 successes (exact from Table 1: SAPG λ=0 = 23.7 ± 0.74)

**Key finding**: PPO performance plateaus after ~25,000 batch size despite higher performance being achievable, as evidenced by SAPG's dashed reference line exceeding the PPO plateau in both tasks.
