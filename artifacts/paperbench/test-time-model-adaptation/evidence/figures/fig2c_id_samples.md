# Figure 2(c): Effects of Number of Source ID Samples Q
- **Source**: Figure 2(c), Section 4.3
- **Caption**: "Parameter sensitivity analyses of our FOA. Experiments are conducted on ImageNet-C (Gaussian Noise, level 5) with ViT-Base. (c) Effects of #ID Samples."
- **Dataset**: ImageNet-C Gaussian Noise, severity level 5
- **Model**: ViT-Base, full precision 32-bit, batch size 64
- **Axes**: X-axis: Number of Samples Q (16, 32, 64, 100, 200, 400, 800, 1600); Y-axis left: Accuracy (%); Y-axis right: ECE (%)

| Q | FOA Acc. (%) | NoAdapt Acc. (%) | FOA ECE (%) | NoAdapt ECE (%) |
|---|-------------|-----------------|-------------|-----------------|
| 16 | ≈60.0 | 56.8 | ≈5.0 | 7.5 |
| 32 | ≈61.5 | 56.8 | ≈2.5 | 7.5 |
| 64 | ≈61.5 | 56.8 | ≈2.5 | 7.5 |
| 100 | ≈61.5 | 56.8 | ≈2.5 | 7.5 |
| 200 | ≈61.5 | 56.8 | ≈2.5 | 7.5 |
| 400 | ≈61.5 | 56.8 | ≈2.5 | 7.5 |
| 800 | ≈61.5 | 56.8 | ≈2.5 | 7.5 |
| 1600 | ≈61.5 | 56.8 | ≈2.5 | 7.5 |

Notes:
- Intermediate values are approximate (≈) from figure; exact values not reported in text for all Q
- Paper states: "consistently achieves stable performance when #samples greater than 32"
- Performance stabilizes sharply at Q=32; Q=16 shows slight degradation
- FOA Acc. at Q=28 is 61.5% (Gaussian only) from Table 6 context (K=28 default)
