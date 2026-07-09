# Table 6: FOA-I Interval Update Strategy for Single Sample Adaptation
- **Source**: Table 6, Section 4.4
- **Caption**: "Effectiveness of FOA with interval update strategy (different intervals I), termed FOA-I, for single sample adaptation. We report results on ImageNet-C (Gaussian, level 5) with Vit-Base."
- **Model**: ViT-Base, full precision 32-bit
- **Dataset**: ImageNet-C Gaussian noise, severity level 5

| Method | Acc. (%) | ECE (%) |
|--------|----------|---------|
| NoAdapt (BS=64) | 56.8 | 7.5 |
| TENT (BS=64) | 60.3 | 13.7 |
| FOA-I (I=4) | 62.1 | 3.3 |
| FOA-I (I=8) | 62.2 | 2.6 |
| FOA-I (I=16) | 62.1 | 2.8 |
| FOA-I (I=32) | 61.9 | 2.7 |
| FOA-I (I=64) | 61.5 | 2.5 |
