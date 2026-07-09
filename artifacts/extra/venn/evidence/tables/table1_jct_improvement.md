# Table 1: Average JCT Improvement Over Random Matching by Workload
- **Source**: Table 1, Section 5.2
- **Caption**: "Summary of improvements on average JCT over random matching on different CL workloads."
- **Conditions**: Event-driven simulation; 50 concurrent jobs; Poisson arrival with 30-min avg inter-arrival; 4 device eligibility categories; starvation prevention enabled (ε=2).

| Workload | FIFO | SRSF | Venn |
|----------|------|------|------|
| Even     | 1.38× | 1.69× | 1.87× |
| Small    | 1.48× | 1.68× | 1.78× |
| Large    | 1.64× | 1.57× | 1.72× |
| Low      | 1.55× | 1.66× | 1.88× |
| High     | 1.42× | 1.41× | 1.63× |

**Notes:**
- Baseline = optimized random matching (1.0×)
- Even: sampled from all jobs. Small: below-average total demand. Large: above-average total demand. Low: below-average per-round demand. High: above-average per-round demand.
