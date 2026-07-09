# Figure 14: Fairness Knob (ε) Effect
- **Source**: Figure 14, Section 5.5
- **Caption**: "(a) Venn's improvement over different ε. (b) Ratio of jobs meeting the fair-share JCT."
- **Axis labels (a)**: x-axis: ε value; y-axis: Avg. JCT Improvement (×)
- **Axis labels (b)**: x-axis: ε value; y-axis: Jobs with JCT < fair JCT (%)

## (a) Average JCT Improvement vs. ε (approximate, read from figure)

| ε     | Avg. JCT Improvement (≈) |
|-------|--------------------------|
| 0     | ≈ 1.88                   |
| 0.5   | ≈ 1.80                   |
| 1     | ≈ 1.72                   |
| 2     | ≈ 1.60                   |
| 4     | ≈ 1.50                   |

## (b) Percentage of Jobs Meeting Fair-Share JCT vs. ε

| ε     | Jobs with JCT ≤ fair-share JCT (%) |
|-------|------------------------------------|
| 0     | ≈ 40%                              |
| 1     | ≈ 55%                              |
| 2     | 69%                                |
| 4     | ≈ 80%                              |

**Key Findings**:
- At ε=2: exactly 69% of jobs meet fair-share JCT (stated precisely in paper).
- As ε increases: average JCT improvement decreases monotonically (performance cost of fairness).
- As ε increases: fairness coverage increases monotonically.
- The ε knob allows operators to choose their desired point on the JCT-vs-fairness Pareto frontier.

*Note: Panel (a) values are ≈ (best-effort readings from figure) except the stated ε=2 → 69% in panel (b).*
