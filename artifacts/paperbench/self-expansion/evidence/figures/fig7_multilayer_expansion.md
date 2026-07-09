# Figure 7: Analysis of Multi-Layer Expansion
- **Source**: Figure 7, Section 4.3
- **Caption**: "Analysis of the effect of multi-layer expansion, with (a)(b) ImageNet-A and (c)(d) VTAB. By enabling automatic self-expansion on multiple transformer layers, SEMA can achieve better performance than restricting that on a single layer."

## Axis Labels
- X-axis: Transformer layers with module expansion (11-12, 10-12, 9-12)
- Y-axis (accuracy): Accuracy (%)
- Y-axis (adapter count): Number of Added Adapters

## Figure 7a: ImageNet-A Accuracy vs. Expansion Layers

| Expansion Layers | A_N (%) | Ā (%) |
|-----------------|---------|-------|
| 11-12 (last 2) | ≈62.5 | ≈51.5 |
| 10-12 (last 3) | 64.53 | 53.32 |
| 9-12 (last 4) | ≈65.0 | ≈53.8 |

*Note: 10-12 values are from Table 1/Table 2 (SEMA default). Others are approximate from figure.*

## Figure 7b: ImageNet-A Adapter Count vs. Expansion Layers

| Expansion Layers | Last Layer (Layer 12) Adapters | Total Adapters |
|-----------------|-------------------------------|----------------|
| 11-12 (last 2) | ≈8 | ≈14 |
| 10-12 (last 3) | ≈8 | ≈18 |
| 9-12 (last 4) | ≈8 | ≈24 |

*Note: Approximate readings; key observation: early layer expansion significantly increases total adapters without proportional accuracy gain.*

## Figure 7c: VTAB Accuracy vs. Expansion Layers

| Expansion Layers | A_N (%) | Ā (%) |
|-----------------|---------|-------|
| 11-12 (last 2) | ≈89.5 | ≈87.8 |
| 10-12 (last 3) | 91.26 | 89.64 |
| 9-12 (last 4) | ≈91.4 | ≈90.0 |

*Note: 10-12 values from Table 1 (SEMA default). Others are approximate.*

## Figure 7d: VTAB Adapter Count vs. Expansion Layers

| Expansion Layers | Last Layer (Layer 12) Adapters | Total Adapters |
|-----------------|-------------------------------|----------------|
| 11-12 (last 2) | ≈3 | ≈5 |
| 10-12 (last 3) | ≈3 | ≈6 |
| 9-12 (last 4) | ≈3 | ≈8 |

*Note: Approximate readings from figure.*
