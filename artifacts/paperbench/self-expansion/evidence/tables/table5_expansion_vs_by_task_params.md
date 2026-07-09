# Table 5: Comparison of Added Parameters and Accuracy — SEMA vs. Expansion-by-Task
- **Source**: Table 5, Appendix C.2
- **Caption**: "Comparison of added parameters and accuracy with different expansion strategies. 'Expansion by Task' is a naive implementation of SEMA's variant that adds one set of adapters (at all layers allowing expansion) for every new task. SEMA only expands if a distribution shift is detected by the representation descriptor."
- **Experimental conditions**: CIFAR-100 (10 tasks), ImageNet-R (20 tasks), ImageNet-A (20 tasks), VTAB (5 tasks); ViT-B/16-IN1K. Params measured in millions (M). A_N = average accuracy after final task.

| Dataset | Expansion by Task Params (M) | Expansion by Task A_N | SEMA Params (M) | SEMA A_N |
|---------|------------------------------|----------------------|-----------------|---------|
| CIFAR-100 | 1.066 | 86.86 | 0.645 | 86.98 |
| ImageNet-R | 1.904 | 74.08 | 0.617 | 74.53 |
| ImageNet-A | 1.904 | 52.80 | 0.560 | 53.32 |
| VTAB | 0.647 | 89.09 | 0.554 | 89.64 |
