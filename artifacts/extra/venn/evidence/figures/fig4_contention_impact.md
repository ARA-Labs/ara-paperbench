# Figure 4: Impact of Resource Contention on Test Accuracy
- **Source**: Figure 4, Section 2.3
- **Caption**: "Impact of resource contention."
- **Axis labels**: x-axis: Round; y-axis: Avg. Test Accuracy (range ≈0.40–0.80)
- **Conditions**: ResNet-18, 100 clients per round, FEMNIST dataset; device pool evenly partitioned among jobs; random device-to-job matching.

## Extracted Data Points (approximate, read from figure)

| Number of Jobs | Approximate Final Accuracy (after sufficient rounds) |
|----------------|------------------------------------------------------|
| 1 job          | ≈ 0.80                                               |
| 5 jobs         | ≈ 0.72                                               |
| 10 jobs        | ≈ 0.65                                               |
| 20 jobs        | ≈ 0.57                                               |

**Key Finding**: As the number of concurrent CL jobs increases from 1 to 20, final test accuracy degrades by approximately 0.23 accuracy points (≈29% relative degradation), demonstrating that resource contention reduces participant diversity and harms model quality.

*Note: Exact round-by-round values are not tabulated in the paper; the above are best-effort readings from Figure 4. Values marked ≈.*
