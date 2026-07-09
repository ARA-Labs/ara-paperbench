# Table 3: Ablation Studies on Masking Components

- **Source**: Table 3, Section 5
- **Caption**: "Ablation Studies (Mean % ± Std %, with ResNet-18 as an example, and the average results are highlighted in grey)"
- **Conditions**: ResNet-18 (ImageNet-1K); ILM output mapping; same hyperparameters as Table 1; 3 seeds
- **Variants**:
  - "ONLY δ" = fin(xi) = r(xi) + δ (full watermark, all-one M, no fmask)
  - "ONLY fmask" = fin(xi) = r(xi) + fmask(r(xi)) (no shared δ)
  - "SINGLE-CHANNEL f^s_mask" = fin(xi) = r(xi) + δ ⊙ f^s_mask(r(xi)) (averaged 1-channel mask)
  - "OURS" = full SMM (3-channel mask + shared δ)

| Dataset | ONLY δ | ONLY fmask | SINGLE-CHANNEL f^s_mask | OURS (SMM) |
|---------|--------|-----------|------------------------|------------|
| CIFAR10 | 68.9 ±0.4 | 59.0 ±1.6 | 72.6 ±2.6 | 72.8 ±0.7 |
| CIFAR100 | 33.8 ±0.2 | 32.1 ±0.3 | 38.0 ±0.6 | 39.4 ±0.6 |
| SVHN | 78.3 ±0.3 | 51.1 ±3.1 | 78.4 ±0.2 | 84.4 ±2.0 |
| GTSRB | 76.8 ±0.9 | 55.7 ±1.2 | 70.7 ±0.8 | 80.4 ±1.2 |
| FLOWERS102 | 23.2 ±0.5 | 32.2 ±0.4 | 30.2 ±0.4 | 38.7 ±0.7 |
| DTD | 29.0 ±0.7 | 27.2 ±0.5 | 32.7 ±0.5 | 33.6 ±0.4 |
| UCF101 | 24.4 ±0.9 | 25.7 ±0.3 | 28.0 ±0.3 | 28.7 ±0.8 |
| FOOD101 | 13.2 ±0.1 | 13.3 ±0.1 | 15.8 ±0.1 | 17.5 ±0.1 |
| SUN397 | 13.4 ±0.2 | 10.5 ±0.1 | 15.9 ±0.1 | 16.0 ±0.3 |
| EUROSAT | 84.3 ±0.5 | 89.2 ±0.9 | 90.6 ±0.5 | 92.2 ±0.2 |
| OXFORDPETS | 70.0 ±0.6 | 72.5 ±0.3 | 73.8 ±0.6 | 74.1 ±0.4 |
| **AVERAGE** | **46.85** | **42.59** | **49.70** | **52.53** |
