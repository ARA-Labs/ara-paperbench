# Table 7: Comparison of APT to Existing Baselines on BERT-base (Full GLUE)
- **Source**: Table 7, Appendix D.1
- **Caption**: "Comparison of APT to existing unstructured pruning baseline with using PEFT in conjunction. The best results are bold while the second-best ones are underlined."

| Density | Method | MNLI | QQP | QNLI | SST2 | CoLA | STS-B | MRPC | RTE | GLUE Avg. |
|---------|--------|------|-----|------|------|------|-------|------|-----|-----------|
| 50% | MaP | 83.6 | 87.8 | 91.5 | 91.0 | 60.1 | 89.8 | 90.7 | 67.2 | 82.7 |
| 50% | MvP | 82.3 | 87.3 | 90.8 | 90.8 | 57.7 | 89.4 | 91.1 | 67.2 | 82.1 |
| 50% | PST | 81.0 | 85.8 | 89.8 | 91.3 | 57.6 | 84.6 | 90.7 | 67.9 | 81.0 |
| 50% | LRP | 82.4 | 87.2 | 89.6 | 90.9 | 54.1 | 88.7 | 89.8 | 69.3 | 82.2 |
| 50% | APT | 82.8 | 90.1 | 90.1 | 92.7 | 59.6 | 88.3 | 91.8 | 70.4 | 83.2 |
| 10% | MaP | 78.2 | 83.2 | 84.1 | 85.4 | 27.9 | 82.3 | 80.5 | 50.1 | 71.4 |
| 10% | MvP | 80.1 | 84.4 | 87.2 | 87.2 | 28.6 | 84.3 | 84.1 | 57.6 | 74.2 |
| 10% | PST | 79.6 | 86.1 | 86.6 | 89.0 | 38.0 | 81.3 | 83.6 | 63.2 | 75.9 |
| 10% | LRP | 79.4 | 86.0 | 85.3 | 89.1 | 35.6 | 83.3 | 84.4 | 62.8 | 75.7 |
| 10% | APT | 78.8 | 89.4 | 85.5 | 90.0 | 30.9 | 86.3 | 88.2 | 65.3 | 76.8 |

*Note: Density = fraction of parameters RETAINED (10% density = 90% sparsity). MaP = Mask Pruning.*
*Note: All results on BERT-base model.*
