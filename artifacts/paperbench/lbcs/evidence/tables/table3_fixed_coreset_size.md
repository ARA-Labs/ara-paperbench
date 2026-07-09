# Table 3: Baselines Evaluated at LBCS-Found Coreset Sizes
- **Source**: Table 3, Section 5.2
- **Caption**: "Mean and standard deviation of test accuracy (%) on different benchmarks with coreset sizes achieved by the proposed LBCS."
- **Experimental conditions**: All baselines are re-run with coreset size fixed to LBCS's achieved sizes (from Table 2). 10 repetitions. Same network architectures as Table 2. The coreset sizes used for each row are listed in the rightmost column (from LBCS Table 2 values).

| Dataset | Uniform | EL2N | GraNd | Influential | Moderate | CCS | Probabilistic | LBCS (ours) | LBCS coreset size used |
|---------|---------|------|-------|-------------|----------|-----|---------------|-------------|------------------------|
| F-MNIST (≈957) | 76.5±1.8 | 71.3±3.1 | 70.8±1.1 | 78.2±0.9 | 76.3±0.5 | 75.4±1.1 | 79.2±0.9 | 79.7±0.5 | 1935* |
| F-MNIST (≈1915) | 79.8±2.1 | 73.2±1.3 | 71.2±1.5 | 80.0±1.9 | 79.7±0.5 | 80.3±0.6 | 81.7±0.7 | 82.8±0.4 | 2832* |
| F-MNIST (≈2832) | 81.2±1.3 | 75.0±1.6 | 73.2±1.1 | 81.0±0.7 | 81.4±0.3 | 82.5±0.7 | 83.4±0.6 | 84.0±0.4 | 3746* |
| F-MNIST (≈3745) | 82.8±1.5 | 77.0±2.2 | 75.1±1.6 | 82.1±1.0 | 82.2±0.4 | 83.6±1.0 | 83.8±0.5 | 84.5±0.3 | — |
| SVHN (≈970) | 66.7±2.6 | 57.2±0.5 | 60.6±1.7 | 70.3±1.2 | 68.4±1.8 | 65.1±1.1 | 67.6±1.3 | 70.6±0.3 | 1902* |
| SVHN (≈1902) | 75.7±1.8 | 65.0±0.7 | 67.0±1.2 | 75.5±0.9 | 77.7±1.2 | 75.9±1.4 | 76.1±0.7 | 78.3±0.7 | 2713* |
| SVHN (≈2713) | 79.5±2.6 | 72.3±0.5 | 74.8±1.1 | 80.0±1.9 | 81.4±1.1 | 81.1±1.0 | 80.5±0.4 | 82.3±0.8 | 3805* |
| SVHN (≈3804) | 83.6±1.2 | 75.5±1.8 | 78.2±1.3 | 82.8±1.6 | 83.6±0.6 | 84.2±0.3 | 83.5±1.2 | 84.6±0.6 | — |
| CIFAR-10 (≈970) | 46.8±1.2 | 36.7±1.1 | 41.4±1.9 | 44.8±1.5 | 46.2±1.9 | 45.4±1.0 | 47.8±1.1 | 48.3±1.2 | 1955* |
| CIFAR-10 (≈1955) | 58.0±1.3 | 48.3±1.9 | 52.5±1.2 | 57.6±1.9 | 57.4±0.8 | 58.6±1.4 | 59.4±1.2 | 60.4±1.0 | 2914* |
| CIFAR-10 (≈2914) | 65.5±1.9 | 55.0±3.2 | 67.7±1.8 | 67.2±1.0 | 68.2±2.1 | 66.5±1.0 | 68.0±0.8 | 69.5±0.9 | 3736* |
| CIFAR-10 (≈3736) | 70.6±2.4 | 58.8±1.9 | 72.8±1.1 | 70.2±3.5 | 73.0±1.2 | 72.8±0.9 | 73.4±0.5 | 73.4±0.5 | — |

**Notes**:
- Values marked with * in "LBCS coreset size used" column indicate the exact integer coreset sizes used for rows above (from Table 2 LBCS mean values). These are the sizes applied to all baselines in that row.
- The paper presents Table 3 with row headers showing the LBCS-achieved sizes; the exact mapping is: F-MNIST rows use sizes 1935, 2832, 3746, (4th row not labeled); SVHN rows use 1902, 2713, 3805; CIFAR-10 rows use 1955, 2914, 3736.
- LBCS consistently achieves the best accuracy in all 12 rows.
