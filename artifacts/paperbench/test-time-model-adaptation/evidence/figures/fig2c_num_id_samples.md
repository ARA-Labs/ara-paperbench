---
# Figure 2(c): Effects of Number of Source ID Samples Q
- **Source**: Figure 2(c), Section 4.3
- **Caption**: "Effects of #ID Samples — Parameter sensitivity analyses of our FOA. Experiments are conducted on ImageNet-C (Gaussian Noise, level 5) with ViT-Base."
- **Conditions**: ViT-Base (full precision, 32-bit); ImageNet-C, Gaussian noise, severity level 5; batch size 64; K=28; Np=3
- **Axes**: X-axis: Number of source ID samples Q ∈ {16, 32, 64, 100, 200, 400, 800, 1600}; Y-axis (left): Accuracy (%); Y-axis (right): ECE (%)
- **Series**: Acc FOA (ours), Acc NoAdapt, ECE FOA (ours), ECE NoAdapt

## Key Data Points (Extracted from Figure 2c)

| Q | FOA Acc. (%) | NoAdapt Acc. (%) | FOA ECE (%) | NoAdapt ECE (%) |
|---|-------------|-----------------|-------------|-----------------|
| 16 | ≈59.5 | ≈56.8 | ≈5.5 | ≈7.5 |
| 32 | ≈61.5 | ≈56.8 | ≈2.6 | ≈7.5 |
| 64 | ≈61.5 | ≈56.8 | ≈2.5 | ≈7.5 |
| 100 | ≈61.6 | ≈56.8 | ≈2.5 | ≈7.5 |
| 200 | ≈61.5 | ≈56.8 | ≈2.5 | ≈7.5 |
| 400 | ≈61.5 | ≈56.8 | ≈2.5 | ≈7.5 |
| 800 | ≈61.5 | ≈56.8 | ≈2.5 | ≈7.5 |
| 1600 | ≈61.5 | ≈56.8 | ≈2.5 | ≈7.5 |

**Key findings (from paper text)**:
- FOA achieves "stable performance when #samples greater than 32, regarding both the accuracy and ECE"
- Q=16 shows some instability; Q ≥ 32 is sufficient
- FOA "does not need to collect too many in-distribution samples, which are easy to obtain in practice"
- All values are approximate (≈) — read from a line plot; Q=32 threshold explicitly stated in text
