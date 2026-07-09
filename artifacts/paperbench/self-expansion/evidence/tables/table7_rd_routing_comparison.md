# Table 7: Learned Weighting Router vs. RD-based Routing
- **Source**: Table 7, Appendix C.3
- **Caption**: "Comparison between routing with the expandable weighting router and RD-based routing."
- **Experimental conditions**: ViT-B/16-IN1K; all benchmarks. Each cell: A_N (left) / Ā (right).

| Method | CIFAR-100 A_N | CIFAR-100 Ā | 5-Task IN-R A_N | 5-Task IN-R Ā | 10-Task IN-R A_N | 10-Task IN-R Ā | 20-Task IN-R A_N | 20-Task IN-R Ā | ImageNet-A A_N | ImageNet-A Ā | VTAB A_N | VTAB Ā |
|--------|--------------|-------------|-----------------|---------------|------------------|----------------|------------------|----------------|----------------|-------------|---------|--------|
| SEMA | 91.37 | 86.98 | 84.75 | 79.78 | 83.56 | 78.00 | 81.75 | 74.53 | 64.53 | 53.32 | 91.26 | 89.64 |
| RD-based routing | 90.91 | 83.61 | 84.46 | 79.50 | 82.76 | 76.63 | 81.02 | 74.13 | 61.80 | 50.36 | 90.83 | 88.53 |
