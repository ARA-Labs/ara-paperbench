---
# Figure 2(a): Effects of Population Size K on FOA Performance
- **Source**: Figure 2(a), Section 4.3
- **Caption**: "Effects of Population Size — Parameter sensitivity analyses of our FOA. Experiments are conducted on ImageNet-C (Gaussian Noise, level 5) with ViT-Base."
- **Conditions**: ViT-Base (full precision, 32-bit); ImageNet-C, Gaussian noise, severity level 5; batch size 64
- **Axes**: X-axis: Population size K ∈ {2, 3, ..., 28}; Y-axis (left): Accuracy (%); Y-axis (right): ECE (%)
- **Series**: Acc FOA (ours), Acc NoAdapt, ECE FOA (ours), ECE NoAdapt

## Key Data Points (Extracted from Figure 2a)

| K | FOA Acc. (%) | NoAdapt Acc. (%) | FOA ECE (%) | NoAdapt ECE (%) |
|---|-------------|-----------------|-------------|-----------------|
| 2 | ≈57.9 | ≈56.8 | ≈ (lower than TENT) | ≈7.5 |
| 6 | ≈60.8 | ≈56.8 | — | ≈7.5 |
| 9 | ≈61.5 | ≈56.8 | — | ≈7.5 |
| 12 | ≈62.0 | ≈56.8 | — | ≈7.5 |
| 15 | ≈62.3 | ≈56.8 | — | ≈7.5 |
| 18 | ≈62.2 | ≈56.8 | — | ≈7.5 |
| 21 | ≈62.2 | ≈56.8 | — | ≈7.5 |
| 24 | ≈62.2 | ≈56.8 | — | ≈7.5 |
| 27 | ≈62.3 | ≈56.8 | — | ≈7.5 |
| 28 | 61.5 | 56.8 | — | 7.5 |

**Key findings (from paper text)**:
- At K=2: FOA achieves 57.9% accuracy — outperforms both NoAdapt (56.8%) and T3A (56.4%)
- At K=6: FOA achieves 60.8% accuracy — surpasses gradient-based TENT (60.3%)
- Performance converges when K > 15
- NoAdapt baseline: 56.8% accuracy, 7.5% ECE (constant reference lines)
- All exact values from Figure 2a are approximate (≈) as they are read from a plot; exact values for K=2 (57.9%), K=6 (60.8%) explicitly stated in text
