# Table 5: Expansion-by-Task vs SEMA Parameter Efficiency
- **Source**: Table 5, Appendix C.2
- **Caption**: "Comparison of added parameters and accuracy with different expansion strategies. 'Expansion by Task' is a naive implementation of SEMA's variant that adds one set of adapters (at all layers allowing expansion) for every new task. SEMA only expands if a distribution shift is detected by the representation descriptor."
- **Note**: ImageNet-R here is 20-task split (10 classes/task); CIFAR-100 is 10-task; ImageNet-A is 20-task; VTAB is 5-task.

| Dataset | Expansion by Task Params (M) | Expansion by Task AN (%) | SEMA Params (M) | SEMA AN (%) |
|---------|------------------------------|--------------------------|-----------------|-------------|
| CIFAR-100 | 1.066 | 86.86 | 0.645 | 86.98 |
| ImageNet-R | 1.904 | 74.08 | 0.617 | 74.53 |
| ImageNet-A | 1.904 | 52.80 | 0.560 | 53.32 |
| VTAB | 0.647 | 89.09 | 0.554 | 89.64 |
