---
# Table 3: Comparisons on ImageNet-R/V2/Sketch — Accuracy and ECE
- **Source**: Table 3, Section 4.1
- **Caption**: "Comparisons with state-of-the-art methods on ImageNet-R/V2/Sketch with ViT-Base. BP is short for backward propagation and the bold number indicates the best result."
- **Conditions**: ViT-Base (full precision, 32-bit); batch size 64

| Method | BP | R Acc. | V2 Acc. | Sketch Acc. | Avg Acc. | R ECE | V2 ECE | Sketch ECE | Avg ECE |
|--------|-----|--------|---------|-------------|----------|-------|---------|------------|---------|
| NoAdapt | ✗ | 59.5 | 75.4 | 44.9 | 59.9 | 2.5 | 5.6 | 7.9 | 5.3 |
| LAME | ✗ | 59.0 | 75.2 | 44.4 | 59.6 | 2.5 | 5.0 | 9.7 | 5.7 |
| T3A | ✗ | 58.0 | 75.5 | 48.5 | 60.7 | 25.9 | 23.4 | 37.4 | 28.9 |
| TENT | ✓ | 63.9 | 75.2 | 49.1 | 62.7 | 7.2 | 4.5 | 22.8 | 11.5 |
| CoTTA | ✓ | 63.5 | 75.4 | 50.0 | 62.9 | 2.8 | 3.4 | 17.9 | 8.0 |
| SAR | ✓ | 63.3 | 75.1 | 48.7 | 62.4 | 3.0 | 2.7 | 16.5 | 7.4 |
| FOA (ours) | ✗ | 63.8 | 75.4 | 49.9 | 63.0 | 2.7 | 3.2 | 7.8 | 4.6 |

**Notes**: 
- Bold indicates best result per column
- FOA achieves best or comparable accuracy on all three benchmarks while achieving much lower ECE than gradient-based methods
- Avg ECE: average over the three benchmarks (R, V2, Sketch)
