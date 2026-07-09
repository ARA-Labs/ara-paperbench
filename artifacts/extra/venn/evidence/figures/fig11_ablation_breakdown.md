# Figure 11: Ablation — Per-Component JCT Improvement
- **Source**: Figure 11, Section 5.3
- **Caption**: "Average JCT improvement breakdown." (Two sub-figures: (a) Low workload, (b) High workload)
- **Axis labels**: x-axis: Scheduler variant; y-axis: Avg. JCT Improvement (×) relative to Random Matching

## (a) Low Workload

| Scheduler Variant | Avg. JCT Improvement |
|-------------------|---------------------|
| Random            | 1.0                 |
| FIFO              | 1.55                |
| Venn w/o sched    | 1.62                |
| Venn w/o match    | 1.79                |
| Venn (full)       | 1.88                |

## (b) High Workload

| Scheduler Variant | Avg. JCT Improvement |
|-------------------|---------------------|
| Random            | 1.0                 |
| FIFO              | 1.42                |
| Venn w/o sched    | 1.42                |
| Venn w/o match    | 1.63                |
| Venn (full)       | 1.63                |

**Key Findings**:
- IRS scheduling (Venn w/o match) provides the larger share of improvement in both workloads.
- Tier-based matching (the difference between Venn w/o match and full Venn) adds +0.09× under Low contention but +0.00× under High contention, confirming C03.
- Under High contention, matching is not beneficial (scheduling delay dominates).
