# Figure 4: Accuracy vs Patch Size Ablation

- **Source**: Figure 4, Section 5
- **Caption**: "Comparative results of different patch sizes (2^l). ResNet-18 is used as the pre-trained model as an example."
- **Conditions**: ResNet-18 (ImageNet-1K); SMM (Ours); patch sizes 2^l for l ∈ {0,1,2,3,4}; ILM; same training setup as Table 1
- **X-axis**: Patch size (2^l), values: 1, 2, 4, 8, 16
- **Y-axis**: Accuracy (proportion/fraction, shown in figures as 0–1 scale)
- **Comparison baselines**: Watermarking Narrow, Watermarking Medium, Watermarking Full

## EuroSAT Dataset (y-axis range: 0.80–1.00)

| Patch Size (2^l) | Ours (SMM) Accuracy | Narrow | Medium | Full |
|-----------------|---------------------|--------|--------|------|
| 1 (l=0) | ≈0.88 | ≈0.83 | ≈0.84 | ≈0.84 |
| 2 (l=1) | ≈0.90 | ≈0.83 | ≈0.84 | ≈0.84 |
| 4 (l=2) | ≈0.91 | ≈0.83 | ≈0.84 | ≈0.84 |
| 8 (l=3) | ≈0.92 | ≈0.83 | ≈0.84 | ≈0.84 |
| 16 (l=4) | ≈0.92 | ≈0.83 | ≈0.84 | ≈0.84 |

## Flowers102 Dataset (y-axis range: 0.20–0.50)

| Patch Size (2^l) | Ours (SMM) Accuracy | Narrow | Medium | Full |
|-----------------|---------------------|--------|--------|------|
| 1 (l=0) | ≈0.32 | ≈0.22 | ≈0.23 | ≈0.23 |
| 2 (l=1) | ≈0.36 | ≈0.22 | ≈0.23 | ≈0.23 |
| 4 (l=2) | ≈0.38 | ≈0.22 | ≈0.23 | ≈0.23 |
| 8 (l=3) | ≈0.39 | ≈0.22 | ≈0.23 | ≈0.23 |
| 16 (l=4) | ≈0.38 | ≈0.22 | ≈0.23 | ≈0.23 |

## CIFAR100 Dataset (y-axis range: 0.35–0.43)

| Patch Size (2^l) | Ours (SMM) Accuracy | Narrow | Medium | Full |
|-----------------|---------------------|--------|--------|------|
| 1 (l=0) | ≈0.37 | ≈0.37 | ≈0.35 | ≈0.34 |
| 2 (l=1) | ≈0.38 | ≈0.37 | ≈0.35 | ≈0.34 |
| 4 (l=2) | ≈0.39 | ≈0.37 | ≈0.35 | ≈0.34 |
| 8 (l=3) | ≈0.39 | ≈0.37 | ≈0.35 | ≈0.34 |
| 16 (l=4) | ≈0.38 | ≈0.37 | ≈0.35 | ≈0.34 |

## SVHN Dataset (y-axis range: 0.52–0.91)

| Patch Size (2^l) | Ours (SMM) Accuracy | Narrow | Medium | Full |
|-----------------|---------------------|--------|--------|------|
| 1 (l=0) | ≈0.72 | ≈0.59 | ≈0.71 | ≈0.78 |
| 2 (l=1) | ≈0.80 | ≈0.59 | ≈0.71 | ≈0.78 |
| 4 (l=2) | ≈0.83 | ≈0.59 | ≈0.71 | ≈0.78 |
| 8 (l=3) | ≈0.84 | ≈0.59 | ≈0.71 | ≈0.78 |
| 16 (l=4) | ≈0.84 | ≈0.59 | ≈0.71 | ≈0.78 |

**Notes**: All data points marked with ≈ are best-effort readings from the bar chart in Figure 4 of the paper. Watermarking baseline values are constant across patch sizes (they do not use patch-wise interpolation). The key pattern: SMM accuracy consistently increases from patch size 1 to 8, then plateaus or slightly declines at 16.
