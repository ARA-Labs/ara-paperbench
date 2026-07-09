# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_jct_improvement.md](tables/table1_jct_improvement.md) | Table 1, §5.2 | C01 | Average JCT speedup (×) over random matching for FIFO, SRSF, and Venn across five workload scenarios (Even, Small, Large, Low, High). |
| [tables/table2_jct_by_demand.md](tables/table2_jct_by_demand.md) | Table 2, §5.3 | C01, C02 | Venn's average JCT improvement broken down by job total-demand percentile (25th, 50th, 75th) across five workloads, showing smaller jobs benefit most. |
| [tables/table3_jct_by_resource.md](tables/table3_jct_by_resource.md) | Table 3, §5.3 | C01, C02 | Venn's average JCT improvement broken down by device eligibility type (General, Compute-rich, Memory-rich, High-performance) across five workloads. |
| [tables/table4_biased_workloads.md](tables/table4_biased_workloads.md) | Table 4, §5.4 | C01, C02 | Average JCT improvement for FIFO, SRSF, and Venn on four biased workloads where job resource requirements are skewed toward one category. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/fig3_toy_example.md](figures/fig3_toy_example.md) | Figure 3, §2.3 | C02 | Toy example comparing Random Matching (avg JCT=12), SRSF (avg JCT=11), and Optimal (avg JCT=9.3) scheduling for 3 CL jobs with overlapping eligibility. |
| [figures/fig4_contention_impact.md](figures/fig4_contention_impact.md) | Figure 4, §2.3 | C01 | Average test accuracy vs. training round for 1, 5, 10, and 20 concurrent CL jobs sharing a device pool, showing accuracy degradation with contention. |
| [figures/fig10_overhead.md](figures/fig10_overhead.md) | Figure 10, §5.2 | C04 | Venn scheduling latency (ms) vs. number of jobs (up to 1000) and job groups (up to 100), demonstrating negligible overhead. |
| [figures/fig11_ablation_breakdown.md](figures/fig11_ablation_breakdown.md) | Figure 11, §5.3 | C02, C03 | Per-component JCT improvement ablation for Low and High workloads: Random, FIFO, Venn w/o sched, Venn w/o match, Venn. |
| [figures/fig14_fairness_knob.md](figures/fig14_fairness_knob.md) | Figure 14, §5.5 | C06 | Two panels: (a) average JCT improvement vs. ε; (b) percentage of jobs meeting fair-share JCT vs. ε, illustrating the performance-fairness tradeoff. |
