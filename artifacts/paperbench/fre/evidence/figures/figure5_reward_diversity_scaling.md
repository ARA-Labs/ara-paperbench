# Figure 5: Reward Diversity Scaling (AntMaze Bar Chart)

- **Source**: Figure 5, Section 5.3
- **Caption**: "The general capabilities of a FRE agent scales with diversity of random functions used in training. FRE-all represents an agent trained on a uniform mixture of three random reward families, while each other column represents a specific agent trained on only a subset of the three. The robust FRE-all agent displays the largest total score, and competitive performance among all evaluation tasks, showing that the FRE encoding can combine reward function distributions without losing performance."
- **Axis labels**: X-axis: FRE variant (FRE-all, FRE-goals, FRE-lin, FRE-mlp, FRE-lin-mlp, FRE-goal-mlp, FRE-goal-lin); Y-axis: Normalized score [0, 100]; Grouped bars per task category.
- **Data extracted from figure (matches Table 4):**

| FRE Variant | Goal-Reaching | Directional | Random-Simplex | Path-All | Total |
|-------------|---------------|-------------|----------------|----------|-------|
| FRE-all | 48.8 ± 6 | 55.2 ± 8 | 21.3 ± 4 | 63.8 ± 10 | 47.3 ± 7 |
| FRE-goals | 66.0 ± 4 | 6.6 ± 13 | 23.5 ± 6 | 8.3 ± 11 | 26.1 ± 8 |
| FRE-lin | 6.0 ± 1 | 55.5 ± 6 | 14.4 ± 3 | 50.5 ± 9 | 31.6 ± 5 |
| FRE-mlp | 24.0 ± 6 | −6.6 ± 14 | 18.5 ± 6 | 65.4 ± 5 | 25.3 ± 8 |
| FRE-lin-mlp | 8.0 ± 4 | 47.9 ± 6 | 14.8 ± 4 | 58.5 ± 7 | 32.3 ± 5 |
| FRE-goal-mlp | 52.0 ± 6 | 5.1 ± 25 | 19.7 ± 5 | 58.6 ± 23 | 33.8 ± 15 |
| FRE-goal-lin | 54.0 ± 12 | 67.1 ± 5 | 10.7 ± 3 | 55.8 ± 8 | 46.9 ± 7 |

**Key finding**: FRE-all achieves the highest total score (47.3 ± 7) and competitive per-task scores, demonstrating smooth scaling with reward diversity.
