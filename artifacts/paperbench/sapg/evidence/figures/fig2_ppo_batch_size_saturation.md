---
# Figure 2: PPO Batch Size Saturation
- **Source**: Figure 2, §1
- **Caption**: "Performance vs batch size plot for PPO runs (blue curve) across two environments. The curve shows how PPO training runs can not take benefit of large batch size resulting from massively parallelized environments and their asymptotic performance saturates after a certain point. The dashed red line is the performance of our method, SAPG, with more details in the results section."

## Axis Information
- **X-axis**: Batch size (number of parallel environments), range approximately 1,500 to 100,000
- **Y-axis (Shadow Hand)**: Asymptotic performance (episode reward), range approximately 2,000–12,000
- **Y-axis (Allegro Kuka Throw)**: Asymptotic performance (episode successes), range approximately 0–30

## Extracted Data Points (Best-Effort from Figure)

### Shadow Hand — PPO Asymptotic Performance vs Batch Size
| Batch Size (approx.) | Asymptotic Episode Reward (approx.) |
|----------------------|--------------------------------------|
| ≈1,500 | ≈5,000 |
| ≈3,125 | ≈7,000 |
| ≈6,250 | ≈9,500 |
| ≈12,500 | ≈10,500 |
| ≈25,000 | ≈11,000 |
| ≈50,000 | ≈10,800 |
| ≈100,000 | ≈10,500 |

### Shadow Hand — SAPG Reference Line (dashed red)
| Batch Size | SAPG Asymptotic Performance |
|------------|-----------------------------|
| All batch sizes | ≈12,800 (constant reference) |

### Allegro Kuka Throw — PPO Asymptotic Performance vs Batch Size
| Batch Size (approx.) | Asymptotic Episode Successes (approx.) |
|----------------------|----------------------------------------|
| ≈1,500 | ≈5 |
| ≈3,125 | ≈10 |
| ≈6,250 | ≈16 |
| ≈12,500 | ≈18 |
| ≈25,000 | ≈19 |
| ≈50,000 | ≈18 |
| ≈100,000 | ≈17 |

### Allegro Kuka Throw — SAPG Reference Line (dashed red)
| Batch Size | SAPG Asymptotic Performance |
|------------|-----------------------------|
| All batch sizes | ≈30 (constant reference) |

**Note**: All data points are approximate (≈) readings from the figure; exact values not provided in paper text. The key qualitative finding is the saturation plateau in PPO and the higher SAPG reference line.
