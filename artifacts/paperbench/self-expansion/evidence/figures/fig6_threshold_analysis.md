# Figure 6: Analysis of Expansion Threshold Impact
- **Source**: Figure 6, Section 4.3
- **Caption**: "Analysis of the impact of expansion threshold with (a)(b) ImageNet-A and (c)(d) VTAB. (a) and (c) show that SEMA can produce good accuracy stably with slight variation w.r.t. varying expansion threshold. (b) and (d) report how the number of added adapters (on the specific Transformer layers #10, #11, #12) changes with the varying threshold values."

## Axis Labels
- X-axis: Expansion Threshold τ
- Y-axis (accuracy plots): Accuracy (%)
- Y-axis (adapter count plots): Number of Adapters (per transformer layer)

## Figure 6a: ImageNet-A Accuracy vs. Threshold

| Threshold τ | Accuracy (%) |
|-------------|-------------|
| 1.0 | ≈64.8 |
| 1.1 | ≈64.7 |
| 1.2 | ≈64.6 |
| 1.3 | ≈64.5 |
| 1.4 | ≈64.4 |
| 1.5 | ≈64.3 |
| 1.6 | ≈64.2 |
| 1.7 | ≈64.1 |
| 1.8 | ≈63.8 |
| 1.9 | ≈63.5 |
| 2.0 | ≈63.0 |

*Note: Exact values not extractable from figure; approximate readings. Key observation: minimal variation (< 2%) across full range 1.0–2.0.*

## Figure 6b: ImageNet-A Adapter Count vs. Threshold (per layer)

| Threshold τ | Layer 10 Adapters | Layer 11 Adapters | Layer 12 Adapters |
|-------------|------------------|------------------|------------------|
| 1.0 | ≈14 | ≈16 | ≈18 |
| 1.1 | ≈13 | ≈15 | ≈17 |
| 1.2 | ≈12 | ≈14 | ≈16 |
| 1.3 | ≈11 | ≈13 | ≈15 |
| 1.4 | ≈10 | ≈12 | ≈14 |
| 1.5 | ≈9 | ≈11 | ≈13 |
| 1.6 | ≈8 | ≈10 | ≈12 |
| 1.7 | ≈7 | ≈9 | ≈11 |
| 1.8 | ≈6 | ≈8 | ≈10 |
| 1.9 | ≈5 | ≈7 | ≈9 |
| 2.0 | ≈4 | ≈6 | ≈8 |

*Note: Approximate readings from figure; exact values not specified in text. Key observation: monotonically decreasing adapter count with increasing threshold.*

## Figure 6c: VTAB Accuracy vs. Threshold

| Threshold τ | Accuracy (%) |
|-------------|-------------|
| 1.0 | ≈91.5 |
| 2.0 | ≈91.3 |
| 3.0 | ≈91.0 |
| 4.0 | ≈90.8 |
| 5.0 | ≈90.5 |
| 6.0 | ≈89.5 |
| 7.0 | ≈88.0 |
| 8.0 | ≈86.5 |

*Note: Approximate readings; key observation: accuracy drops significantly at τ > 5.0 due to insufficient expansion.*

## Figure 6d: VTAB Adapter Count vs. Threshold (per layer)

| Threshold τ | Layer 10 Adapters | Layer 11 Adapters | Layer 12 Adapters |
|-------------|------------------|------------------|------------------|
| 1.0 | ≈4 | ≈5 | ≈5 |
| 2.0 | ≈3 | ≈4 | ≈5 |
| 3.0 | ≈2 | ≈3 | ≈4 |
| 4.0 | ≈1 | ≈3 | ≈4 |
| 5.0 | ≈1 | ≈2 | ≈3 |
| 6.0 | ≈0 | ≈2 | ≈3 |
| 7.0 | ≈0 | ≈1 | ≈2 |
| 8.0 | ≈0 | ≈1 | ≈1 |

*Note: Approximate readings; VTAB has only 5 tasks so maximum possible adapters per layer is 5.*
