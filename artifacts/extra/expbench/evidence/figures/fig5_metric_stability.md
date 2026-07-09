# Figure 5: Metric Stability Analysis
- **Source**: Figure 5, Section 4.2
- **Caption**: "Stability Analysis." (figure label in paper)
- **Conditions**: Per-task scores for individual metrics (C, E) vs. conjunctive metrics (C·D, I·E) across all evaluated tasks and agent configurations
- **Axis labels**: X-axis: Judge Metric (C·D, I·E, and individual variants); Y-axis: Average Score (%)

## Qualitative Findings (exact numerical values not extractable from paper)

| Metric | Variance | Reason for Variance Level |
|--------|----------|--------------------------|
| C (conclusion alone) | High | Agents can produce plausible but unfounded conclusions without valid experimental foundation |
| E (execution alone) | High | Incorrect or mock implementations may still execute, introducing overestimation bias |
| C·D (conclusion × design) | Substantially lower | Filters out conclusions not grounded in valid design plans |
| I·E (implementation × execution) | Substantially lower | Discounts executions that do not fulfill setup requirements |

**Key finding**: Conjunctive metrics (C·D, I·E) reduce score variability, producing more reliable signals of agent performance and reducing sensitivity to annotation leniency or spurious correctness. The figure shows C·D and I·E as more stable bars compared to C and E individually.

**Note**: Exact per-metric variance numbers are not reported in the paper; the finding is qualitative based on visual inspection of Figure 5.
