# Table 4: ImageNet-1k Top-5 Test Accuracy (§5.4)
- **Source**: Table 4, Section 5.4
- **Caption**: "Top-5 test accuracy (%) on ImageNet-1k. Partial results are from previous work (Xia et al., 2023). The best test accuracy in each case is in bold. For LBCS, we additionally report the optimized ratio of coreset selection."
- **Conditions**: ResNet-50 for both proxy and evaluation; SGD, lr=0.01, batch=256, momentum=0.9, weight_decay=0.001, 100 epochs; groups of G=100 for LBCS and Probabilistic; 1 run each; VISSL library.

| Method | k/n=70% | k/n=80% |
|--------|---------|---------|
| Uniform | 88.63 | 89.52 |
| EL2N | 89.82 | 90.34 |
| GraNd | 89.30 | 89.94 |
| Influential | — | — |
| Moderate | 89.94 | 90.65 |
| CCS | 89.45 | 90.51 |
| Probabilistic | 88.20 | 89.35 |
| **LBCS (ours)** | **89.98 (68.53%)** | **90.84 (77.82%)** |

**Note**: Dashes (—) for Influential at ImageNet-1k indicate results not available. The numbers in parentheses for LBCS are the optimized coreset selection ratios achieved after LBCS refinement.
