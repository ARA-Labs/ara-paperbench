# Figure 6: Analysis of Impact of Expansion Threshold
- **Source**: Figure 6, Section 4.3
- **Caption**: "(a) and (c) show that SEMA can produce good accuracy stably with slight variation w.r.t. varying expansion threshold. (b) and (d) report how the number of added adapters changes with the varying threshold values."
- **Axes**: X = expansion threshold; Y = accuracy (%) or number of adapters
- **Series for adapter count**: 10th, 11th, 12th transformer layer (1-indexed)

## ImageNet-A: Accuracy vs Threshold (Figure 6a)

| Threshold | A_N (%) | Ā (%) |
|-----------|---------|-------|
| 1.0 | ≈ 64–65 | ≈ 53–54 |
| 1.1 | ≈ 64–65 | ≈ 53–54 |
| 1.2 | ≈ 64–65 | ≈ 53 |
| 1.3 | ≈ 64 | ≈ 52–53 |
| 1.4 | ≈ 64 | ≈ 52 |
| 1.5 | ≈ 63–64 | ≈ 52 |
| 1.6 | ≈ 63 | ≈ 51–52 |
| 1.7 | ≈ 62–63 | ≈ 51 |
| 1.8 | ≈ 62 | ≈ 51 |
| 1.9 | ≈ 61–62 | ≈ 50 |
| 2.0 | ≈ 61 | ≈ 50 |

**Note**: Values are approximate (≈) from figure reading. Actual default threshold for ImageNet-A is 1.0.

## VTAB: Accuracy vs Threshold (Figure 6c)

| Threshold | A_N (%) | Ā (%) |
|-----------|---------|-------|
| 1.0 | ≈ 91 | ≈ 89–90 |
| 2.0 | ≈ 91 | ≈ 89 |
| 3.0 | ≈ 90–91 | ≈ 88–89 |
| 4.0 | ≈ 90 | ≈ 88 |
| 5.0 | ≈ 90 | ≈ 88 |
| 6.0 | ≈ 89–90 | ≈ 87–88 |
| 7.0 | ≈ 88–89 | ≈ 86–87 |
| 8.0 | ≈ 87–88 | ≈ 85–86 |

**Key finding**: Accuracy is stable across thresholds 1.0–2.0 on ImageNet-A and 1.0–6.0 on VTAB; higher thresholds (fewer adapters) degrade accuracy, especially on VTAB.
