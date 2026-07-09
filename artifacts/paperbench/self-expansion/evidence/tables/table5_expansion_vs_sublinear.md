# Table 5: Comparison of Expansion-by-Task vs SEMA Parameters and Accuracy
- **Source**: Table 5, Appendix C.2
- **Caption**: "Comparison of added parameters and accuracy with different expansion strategies."
- **Note**: "Expansion by Task" adds one set of adapters (at all layers allowing expansion) for every new task regardless of distribution shift. Settings: CIFAR-100 (10 tasks), ImageNet-R (20 tasks), ImageNet-A (20 tasks), VTAB (5 tasks).

| Dataset | Expansion by Task Params (M) | Expansion by Task Ā | SEMA Params (M) | SEMA Ā |
|---------|------------------------------|---------------------|-----------------|--------|
| CIFAR-100 | 1.066 | 86.86 | 0.645 | 86.98 |
| ImageNet-R | 1.904 | 74.08 | 0.617 | 74.53 |
| ImageNet-A | 1.904 | 52.80 | 0.560 | 53.32 |
| VTAB | 0.647 | 89.09 | 0.554 | 89.64 |
