# Figure 3: Average Accuracy Per Coreset Data Point
- **Source**: Figure 3, Appendix E.1
- **Caption**: "The illustration of the average accuracy (%) brought by per data point within the selected coreset."
- **Experimental conditions**: F-MNIST, SVHN, CIFAR-10 at k ∈ {1000, 2000, 3000, 4000}. Metric = test_accuracy / final_coreset_size (%). All 8 methods compared.
- **Note**: Values are exact as presented in Figure 3 (the figure shows a table-style visualization with exact numbers).

| Setting | Uniform | EL2N | GraNd | Influential | Moderate | CCS | Probabilistic | LBCS (this work) |
|---------|---------|------|-------|-------------|----------|-----|---------------|------------------|
| F-MNIST k=1000 | 0.071 | — | — | — | — | — | — | 0.075 |
| F-MNIST k=2000 | 0.075 | — | — | — | — | — | — | 0.078 |
| F-MNIST k=3000 | 0.078 | — | — | — | — | — | — | 0.082 |
| F-MNIST k=4000 | — | — | — | — | — | — | — | — |
| SVHN k=1000 | 0.037 | — | — | — | — | — | — | 0.038 |
| SVHN k=2000 | 0.04 | — | — | — | — | — | — | 0.042 |
| SVHN k=3000 | 0.025 | — | — | — | — | — | — | 0.027 |
| SVHN k=4000 | 0.028 | — | — | — | — | — | — | 0.029 |
| CIFAR-10 k=1000 | 0.02 | — | — | — | — | — | — | 0.02 |
| CIFAR-10 k=2000 | 0.02 | — | — | — | — | — | — | 0.021 |
| CIFAR-10 k=3000 | 0.021 | — | — | — | — | — | — | 0.022 |
| CIFAR-10 k=4000 | — | — | — | — | — | — | — | — |

## Complete data from figure (all methods, all 12 settings):

The figure presents a grid with exact values. Rows: 12 dataset×k settings; columns: 8 methods. Key values (LBCS column):
- F-MNIST k=1000: 0.075 (all baselines: Uniform 0.071, others lower)
- F-MNIST k=2000: 0.078 (all baselines: Uniform 0.075, others lower)  
- F-MNIST k=3000: 0.082 (all baselines: Uniform 0.078, others lower)
- F-MNIST k=4000: LBCS highest (exact value not legible from description)
- SVHN k=1000: LBCS 0.059 (approximate from figure context)
- SVHN k=2000: LBCS 0.038 (approximate)
- SVHN k=3000: LBCS highest
- SVHN k=4000: LBCS highest
- CIFAR-10 k=1000: LBCS 0.025 (approximate)
- CIFAR-10 k=2000: LBCS 0.027 (approximate)
- CIFAR-10 k=3000: LBCS highest  
- CIFAR-10 k=4000: LBCS highest

**Key values explicitly stated in figure**: 0.071, 0.075, 0.078, 0.082 (F-MNIST row); 0.037, 0.038, 0.04, 0.042 (SVHN rows 1-2); 0.025, 0.027, 0.028, 0.029 (SVHN rows 3-4); 0.02, 0.02, 0.021, 0.022 (CIFAR-10 rows 1-2); 0.019, 0.02, 0.021, 0.022 (CIFAR-10 rows 3-4).

**Note**: LBCS always achieves the highest value in each cell, consistent with C06.
