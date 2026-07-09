# Table 4: JCT Improvement on Biased Workloads
- **Source**: Table 4, Section 5.4
- **Caption**: "Average JCT improvement on four biased workloads."
- **Conditions**: Event-driven simulation; biased workloads where a majority of jobs require one specific resource type (e.g., Compute-heavy = half of jobs require Compute-rich resources, rest evenly distributed); uniform job demands.

| Workload        | FIFO  | SRSF  | Venn  |
|-----------------|-------|-------|-------|
| General         | 1.46× | 1.78× | 1.94× |
| Compute-heavy   | 1.73× | 2.08× | 2.23× |
| Memory-heavy    | 1.68× | 2.05× | 2.27× |
| Resource-heavy  | 1.65× | 1.90× | 2.01× |

**Notes:**
- Baseline = optimized random matching (1.0×).
- Biased workloads create longer queues in one resource category, making contention-aware scheduling more impactful.
- "Resource-heavy" workload has jobs skewed toward High-performance resources.
