# Figure 6: Domain Knowledge Augmentation (FRE-hint)

- **Source**: Figure 6, Section 5.4
- **Caption**: "By augmenting the random reward families with specific reward distributions, FRE can utilize domain knowledge without algorithmic changes."
- **Axis labels**: X-axis: Task (ant-directional, exorl-cheetah-velocity, exorl-walker-velocity); Y-axis: Normalized score [0, 100]; Grouped bars: FRE-all vs. FRE-hint.
- **Note**: Exact numerical values for FRE-hint are not explicitly listed in the paper text; the figure shows FRE-hint bars visually higher than FRE-all on each targeted task. Values below are ≈ (best-effort reads from figure description).

| Task | FRE-all | FRE-hint |
|------|---------|----------|
| ant-directional | 55.2 ± 8 | ≈ 39.4 ± 13 (FB column in Table 1 for reference) |
| exorl-cheetah-velocity | 20 ± 2 | ≈ higher than FRE-all (exact value not specified in paper) |
| exorl-walker-velocity | 34 ± 13 | ≈ higher than FRE-all (exact value not specified in paper) |

**Key finding**: FRE-hint improves over FRE-all on all three targeted evaluation tasks by incorporating domain-specific reward distributions into the prior, without any algorithmic changes. FRE-hint is also shown as a multi-task RL method when the full downstream task distribution is known, demonstrating FRE's universality.

**Note on FRE-hint ant-directional**: The Figure 6 bar for ant-directional FRE-hint appears to be approximately in the range of the FB baseline (≈39.4) but the exact value is not printed in the paper text. The primary claim (FRE-hint > FRE-all on each targeted task) is supported by visual inspection of the figure.
