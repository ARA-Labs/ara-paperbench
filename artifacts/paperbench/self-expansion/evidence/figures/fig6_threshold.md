# Figure 6: Impact of Expansion Threshold
- **Source**: Figure 6, Section 4.3
- **Caption**: "Analysis of the impact of expansion threshold with (a)(b) ImageNet-A and (c)(d) VTAB. (a) and (c) show that SEMA can produce good accuracy stably with slight variation w.r.t. varying expansion threshold. (b) and (d) report how the number of added adapters changes with the varying threshold values."
- **Note**: Exact values not directly readable from paper text; values below are from description + approximate readings

## ImageNet-A: Threshold τ ∈ {1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0}

| Threshold τ | Approx. Accuracy AN (%) | Note |
|-------------|------------------------|------|
| 1.0 | ≈64-65 | More expansion, slightly higher accuracy |
| 1.2 | ≈64.53 | Default/reference value used in main results |
| 1.5 | ≈63-64 | Stable range |
| 2.0 | ≈62-63 | Fewer expansions, slightly lower accuracy |

**Key finding (ImageNet-A)**: Accuracy is stable (low sensitivity) across τ = 1.0–2.0. More adapters added at lower thresholds, consistent with accuracy trend.

## VTAB: Threshold τ ∈ {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0}

| Threshold τ | Approx. Accuracy AN (%) | Note |
|-------------|------------------------|------|
| 1.0 | ≈91-92 | Most expansion, highest accuracy |
| 2.0 | ≈91 | Near-optimal |
| 4.0 | ≈90-91 | Moderate sensitivity |
| 6.0 | ≈89-90 | Degrading |
| 8.0 | ≈88-89 | Under-expansion at high threshold |

**Key finding (VTAB)**: Accuracy degrades at high thresholds (≥6.0); low thresholds (1.0-2.0) are preferable. Adapter count decreases monotonically with increasing threshold for both datasets.

## Adapter Count per Layer (Layers 10, 11, 12)
- Lower thresholds → more adapters in all eligible layers
- Higher thresholds → fewer or zero adapters added beyond Task 1
- The last layer (12) typically receives the most adapters
