# Table 3: JCT Improvement by Device Eligibility Type
- **Source**: Table 3, Section 5.3
- **Caption**: "Breakdown of average JCT improvement across jobs that ask for General resources, Compute-rich resources, Memory-rich resources and High-performance resources. Venn benefits more on jobs that ask for scarcer resources."
- **Conditions**: Same as Table 1; Venn only; jobs grouped by their device eligibility category.

| Workload | General | Compute-rich | Memory-rich | High-performance |
|----------|---------|--------------|-------------|------------------|
| Even     | 1.5×    | 7.2×         | 5.3×        | 3.9×             |
| Small    | 0.9×    | 6.0×         | 2.8×        | 2.6×             |
| Large    | 0.9×    | 3.7×         | 1.8×        | 2.6×             |
| Low      | 0.8×    | 3.4×         | 2.1×        | 8.7×             |
| High     | 0.8×    | 2.2×         | 2.2×        | 5.6×             |

**Notes:**
- General resources are the most abundant (all devices eligible), so Venn provides little or no benefit there (values near or below 1×).
- High-performance and Compute-rich resources are scarcer; Venn provides the largest improvements for jobs requiring them.
