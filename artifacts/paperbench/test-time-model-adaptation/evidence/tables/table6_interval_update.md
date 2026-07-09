---
# Table 6: FOA-I Interval Update Strategy (Single Sample Adaptation)

**Source**: Table 6, §4.4
**Claims**: C01
**Description**: Accuracy and ECE for FOA-I with different update intervals I on ImageNet-C (Gaussian noise, level 5) with ViT-Base.

| Method | Acc. (%) | ECE (%) |
|---|---|---|
| NoAdapt (BS=64) | 56.8 | 7.5 |
| TENT (BS=64) | 60.3 | 13.7 |
| FOA-I (I=4) | **62.1** | 3.3 |
| FOA-I (I=8) | 62.2 | 2.6 |
| FOA-I (I=16) | 62.1 | 2.8 |
| FOA-I (I=32) | 61.9 | 2.7 |
| FOA-I (I=64) | 61.5 | 2.5 |

Notes:
- FOA-I = FOA with interval update strategy; prompts updated every I samples
- BS=1 for all FOA-I variants (single sample adaptation scenario)
- FOA-I (I=4) outperforms TENT (BS=64) in accuracy: 62.1% > 60.3%
- Smaller intervals (e.g., I=4) yield better performance due to more CMA iterations
- FOA-I provides a way to apply FOA when batch size is limited to 1
