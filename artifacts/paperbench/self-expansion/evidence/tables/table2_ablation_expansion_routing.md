# Table 2: Ablation Studies on Adapter Expansion and Composing
- **Source**: Table 2, Section 4.3
- **Caption**: "Ablation studies on adapter expansion and composing."
- **Experimental conditions**: ImageNet-A (20 tasks) and VTAB (5 tasks); ViT-B/16-IN1K backbone; same training hyperparameters as main experiments. Each cell: A_N (left) / Ā (right).

| Method | ImageNet-A A_N | ImageNet-A Ā | VTAB A_N | VTAB Ā |
|--------|----------------|-------------|---------|--------|
| SEMA | 64.53 | 53.32 | 91.26 | 89.64 |
| No Exp. | 61.20 | 49.90 | 86.21 | 83.66 |
| Avg. W. | 56.88 | 44.31 | 90.84 | 89.14 |
| Rand. W. | 62.95 | 49.77 | 88.87 | 85.17 |
| Top-1 Sel. | 62.00 | 50.56 | 90.83 | 88.61 |
| Rand. Sel. | 61.70 | 50.36 | 90.82 | 88.51 |
| Top-1 Sel. Inf. | 61.96 | 50.36 | 90.95 | 88.84 |
