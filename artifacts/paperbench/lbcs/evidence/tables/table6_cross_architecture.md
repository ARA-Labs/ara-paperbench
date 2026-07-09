# Table 8 (Appendix E.5): Cross-Architecture Evaluation on SVHN
- **Source**: Appendix Table 8, Appendix E.5
- **Caption**: "Mean and standard deviation (std.) of test accuracy (%) on SVHN with various predefined coreset sizes and networks. The best mean test accuracy in each case is in bold."
- **Conditions**: SVHN; CNN (left column of Appendix Table 5) used as proxy for all methods; post-selection evaluation with ViT-small (Dosovitskiy et al. 2021) and WideResNet/W-NET (Zagoruyko & Komodakis 2016); other settings same as §5.2.

## ViT-small

| k | Uniform | EL2N | GraNd | Influential | Moderate | CCS | Probabilistic | LBCS (ours) |
|---|---------|------|-------|-------------|----------|-----|---------------|-------------|
| 1000 | 28.5±3.1 | 22.7±3.5 | 24.0±2.2 | 31.5±1.8 | 32.8±1.5 | 31.7±1.6 | 29.6±0.3 | 33.9±0.8 |
| 2000 | 46.6±2.7 | 40.9±2.6 | 38.8±0.6 | 42.2±1.7 | 45.5±2.3 | 46.1±1.8 | 46.6±2.0 | 47.5±2.2 |
| 3000 | 50.0±2.2 | 46.7±3.0 | 47.9±2.4 | 50.8±0.7 | 51.0±2.9 | 50.4±1.6 | 50.5±1.9 | 51.3±0.6 |
| 4000 | 54.0±3.3 | 49.9±2.8 | 50.8±0.9 | 53.3±0.9 | 54.9±1.9 | 56.2±2.1 | 55.3±1.5 | 57.7±0.4 |

## WideResNet (W-NET)

| k | Uniform | EL2N | GraNd | Influential | Moderate | CCS | Probabilistic | LBCS (ours) |
|---|---------|------|-------|-------------|----------|-----|---------------|-------------|
| 1000 | 78.8±1.5 | 67.9±2.7 | 70.5±3.0 | 79.3±2.8 | 80.0±0.4 | 79.8±0.9 | 80.1±1.3 | 80.3±1.2 |
| 2000 | 87.2±1.2 | 69.5±3.3 | 73.4±2.6 | 87.1±0.8 | 88.0±0.3 | 88.7±0.6 | 87.0±1.0 | 87.8±1.1 |
| 3000 | 89.1±0.9 | 76.6±1.2 | 78.8±3.2 | 90.3±0.7 | 90.3±0.4 | 90.2±0.4 | 89.3±0.6 | 90.7±0.5 |
| 4000 | 90.2±1.9 | 80.3±1.9 | 83.4±1.7 | 90.9±1.1 | 90.8±0.5 | 91.1±1.0 | 90.6±0.5 | 91.4±0.9 |
