# Figure 10: Venn Scheduling Overhead at Scale
- **Source**: Figure 10, Section 5.2
- **Caption**: "Venn introduces negligible overhead at scale."
- **Axis labels**: x-axis: Number of Jobs (up to 1000) / Number of Job Groups (up to 100); y-axis: Latency (ms), range ≈ 0.2–1.0 ms

## Approximate Data Points (best-effort readings from figure)

### Latency vs. Number of Jobs

| Number of Jobs | Latency (ms) |
|----------------|-------------|
| 100            | ≈ 0.2        |
| 250            | ≈ 0.3        |
| 500            | ≈ 0.5        |
| 750            | ≈ 0.7        |
| 1000           | ≈ 1.0        |

### Latency vs. Number of Job Groups

| Number of Job Groups | Latency (ms) |
|---------------------|-------------|
| 10                  | ≈ 0.2        |
| 25                  | ≈ 0.3        |
| 50                  | ≈ 0.5        |
| 80                  | ≈ 0.8        |
| 100                 | ≈ 1.0        |

**Key Finding**: Scheduling latency grows sub-linearly (consistent with max(O(m log m), O(n²)) complexity) and stays below ~1 ms even at 1000 jobs and 100 job groups. Values marked ≈.
