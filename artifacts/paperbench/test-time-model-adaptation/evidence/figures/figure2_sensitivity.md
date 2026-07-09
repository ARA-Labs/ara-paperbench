---
# Figure 2: Parameter Sensitivity Analyses

- **Source**: Figure 2, §4.3
Claims: C08, C03
Description: Sensitivity of FOA to key hyperparameters. Experiments on ImageNet-C Gaussian noise, level 5 with ViT-Base. Both accuracy (%, left axis) and ECE (%, right axis) plotted for FOA vs. NoAdapt baseline.

## (a) Effects of Population Size K

X-axis: K ∈ {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 18, 21, 24, 27}
Y-axis (left): Accuracy (%); Y-axis (right): ECE (%)
Accuracy range: approximately 50.0 – 62.5%

Key data points (from text/Table 8):
| K | FOA Acc (%) | Reference |
|---|---|---|
| 2 | 57.9 | §4.3 "at K=2, FOA outperforms...57.9%" |
| 6 | 60.8 | §4.3 "with K=6, FOA surpasses...60.8%" |
| ≥15 | ~61.5 (converged) | §4.3 "converges when K>15" |
| 28 | 61.5 | Table 8 "FOA (K=28): Gauss. noise" |

Baselines shown as horizontal lines:
- NoAdapt Acc: 56.8% (Gaussian noise, Table 2)
- T3A Acc: 56.4% (Gaussian noise, Table 2)
- TENT Acc: 60.3% (Gaussian noise, Table 2)

Observation: FOA at K=2 (57.9%) > NoAdapt (56.8%) and T3A (56.4%); at K=6 (60.8%) > TENT (60.3%).

## (b) Effects of Number of Prompts Np

X-axis: Np ∈ {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Y-axis (left): Accuracy (%); Y-axis (right): ECE (%)
Accuracy range: approximately 50.0 – 62.5%

Observation:
- Low sensitivity across all Np values (minor variations)
- Np=5 and Np=7 marginally better than others
- Default Np=3 used throughout main experiments

## (c) Effects of Number of ID Samples Q

X-axis: Q ∈ {16, 32, 64, 100, 200, 400, 800, 1600}
(Note: paper text lists {16, 32, 64, 100, 200, 400, 800, 1600} but figure x-axis labels show 64, 100, 200, 400, 800, 1600)
Y-axis (left): Accuracy (%); Y-axis (right): ECE (%)
Accuracy range: approximately 50.0 – 62.5%

Key observation:
- Performance stable for Q ≥ 32 (both accuracy and ECE)
- Q < 32 may lead to unstable source statistics estimates
- "32 samples are sufficient for ImageNet" (§3.1)
