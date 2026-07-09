---
# Figure 2: PPO Asymptotic Performance vs Batch Size

- **Source**: Figure 2, §1 and §4
- **Caption**: "Performance vs batch size plot for PPO runs (blue curve) across two environments. The curve shows how PPO training runs can not take benefit of large batch size resulting from massively parallelized environments and their asymptotic performance saturates after a certain point. The dashed red line is the performance of our method, SAPG, with more details in the results section. It serves as evidence that higher performance is achievable with larger batch sizes."
- **Axis labels**:
  - X-axis: Batch size (approximate values: 25000, 50000, 75000, 100000)
  - Y-axis (Shadow Hand): Asymptotic performance (episode reward, range approximately 2000–12000)
  - Y-axis (Allegro Kuka Throw): Asymptotic performance (episode successes, scale not labeled in paper)
- **Note**: Exact numerical data points from the figure cannot be read precisely from the paper text; approximate readings provided below. Values marked "≈".

## Shadow Hand — PPO Asymptotic Performance vs Batch Size

| Batch Size (approx.) | PPO Asymptotic Performance (≈) |
|---|---|
| 25000 | ≈ 8000–9000 |
| 50000 | ≈ 10000–11000 (peak) |
| 75000 | ≈ 10000 (plateau/slight decline) |
| 100000 | ≈ 9500–10000 (saturation) |

**SAPG (dashed red line)**: ≈ 12000–13000 (above saturation plateau)

## Allegro Kuka Throw — PPO Asymptotic Performance vs Batch Size

| Batch Size (approx.) | PPO Asymptotic Performance (≈) |
|---|---|
| 25000 | ≈ 15–18 successes |
| 50000 | ≈ 17–19 successes (peak) |
| 75000 | ≈ 16–18 successes (plateau) |
| 100000 | ≈ 15–17 successes (saturation) |

**SAPG (dashed red line)**: ≈ 23–24 successes (above saturation plateau)

**Note**: These values are approximate (≈) readings from the described figure. Exact values available only by running the experiments. The key qualitative finding — PPO saturates while SAPG exceeds the saturation level — is clearly stated in the paper. Refer to Table 1 for exact final SAPG and PPO values at 24,576 environments.
