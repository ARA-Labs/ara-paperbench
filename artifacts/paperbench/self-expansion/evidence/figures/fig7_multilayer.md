# Figure 7: Effect of Multi-Layer Expansion Range
- **Source**: Figure 7, Section 4.3
- **Caption**: "Analysis of the effect of multi-layer expansion, with (a)(b) ImageNet-A and (c)(d) VTAB. By enabling automatic self-expansion on multiple transformer layers, SEMA can achieve better performance than restricting that on a single layer."
- **Note**: Exact values not readable from paper text; qualitative trends reported

## ImageNet-A Results

| Layer Range | Approx. AN (%) | Approx. Ā (%) | Total Adapters (≈) | Last Layer Adapters (≈) |
|-------------|---------------|--------------|------------------|------------------------|
| 11-12 (last 2) | ≈62-63 | ≈51-52 | Fewer | Moderate |
| 10-12 (last 3) | ≈64.53 | ≈53.32 | Moderate | Moderate |
| 9-12 (last 4) | ≈65-66 | ≈53-54 | More | Similar |

## VTAB Results

| Layer Range | Approx. AN (%) | Approx. Ā (%) | Total Adapters (≈) | Last Layer Adapters (≈) |
|-------------|---------------|--------------|------------------|------------------------|
| 11-12 (last 2) | ≈89-90 | ≈88-89 | Fewer | Moderate |
| 10-12 (last 3) | ≈91.26 | ≈89.64 | Moderate | Moderate |
| 9-12 (last 4) | ≈91-92 | ≈89-90 | More | Similar |

**Key findings**:
- More eligible expansion layers → higher accuracy, more total adapters
- Earlier layers (9) add adapters without proportional accuracy gains
- Last layer consistently receives the most adapters
- Default (layers 10-12) provides the best balance of accuracy and efficiency
