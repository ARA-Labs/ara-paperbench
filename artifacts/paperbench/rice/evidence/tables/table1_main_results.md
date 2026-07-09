# Table 1: Agent Refining Performance
- **Source**: Table 1, Section 4.3
- **Caption**: "Agent Refining Performance—'No Refine' indicates the target agent's performance before refining. For the first group of experiments (left), we fixed the explanation method to our method (mask network) and varied the refining methods. For the second group of experiments (right), we fixed the refining method to our method and varied the explanation methods. We report the mean value (standard deviations) of the final reward after refining. A higher value is better."
- **Note**: For CAGE Challenge 2, the reward is negative (less negative = better). For Reacher, values are negative (less negative = better). Malware Mutation reports evasion probability (%).

## Group 1: Fix Explanation (Ours); Vary Refining Methods

| Task | No Refine | PPO | JSRL | StateMask-R | Ours |
|------|-----------|-----|------|-------------|------|
| Hopper | 3559.44 (19.15) | 3638.75 (16.67) | 3635.08 (9.82) | 3652.06 (8.63) | 3663.91 (20.98) |
| Walker2d | 3768.79 (18.68) | 3965.63 (9.46) | 3963.57 (6.73) | 3966.96 (3.39) | 3982.79 (3.15) |
| Reacher | -5.79 (0.73) | -3.04 (0.04) | -3.23 (0.26) | -3.45 (0.32) | -2.66 (0.03) |
| HalfCheetah | 2024.09 (28.34) | 2133.31 (4.11) | 2128.04 (0.91) | 2085.28 (1.92) | 2138.89 (3.22) |
| Selfish Mining | 14.36 (0.24) | 14.93 (0.45) | 14.88 (0.51) | 14.53 (0.33) | 16.56 (0.63) |
| Cage Challenge 2 | -23.64 (0.27) | -23.58 (0.37) | -22.97 (0.57) | -26.98 (0.84) | -20.02 (0.32) |
| Auto Driving | 10.30 (2.25) | 13.37 (3.10) | 11.26 (3.66) | 7.62 (1.77) | 17.03 (1.65) |
| Malware Mutation | 42.20 (6.86) | 49.33 (8.59) | 43.10 (7.24) | 50.13 (8.14) | 57.53 (8.71) |

## Group 2: Fix Refining Method (Ours); Vary Explanation Methods

| Task | Random | StateMask | Ours |
|------|--------|-----------|------|
| Hopper | 3648.98 (39.06) | 3661.86 (19.95) | 3663.91 (20.98) |
| Walker2d | 3969.64 (6.38) | 3982.67 (5.55) | 3982.79 (3.15) |
| Reacher | -3.11 (0.42) | -2.69 (0.28) | -2.66 (0.03) |
| HalfCheetah | 2132.01 (0.76) | 2136.23 (0.49) | 2138.89 (3.22) |
| Selfish Mining | 15.09 (0.28) | 16.49 (0.46) | 16.56 (0.63) |
| Cage Challenge 2 | -25.94 (2.34) | -20.07 (1.33) | -20.02 (0.32) |
| Auto Driving | 11.72 (1.77) | 16.28 (2.33) | 17.03 (1.65) |
| Malware Mutation | 48.60 (7.60) | 57.16 (8.51) | 57.53 (8.71) |
