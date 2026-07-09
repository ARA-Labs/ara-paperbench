---
# Table 12: In-Distribution Performance (Clean ImageNet Validation)

**Source**: Table 12, §4.4
**Claims**: C06
**Description**: Accuracy (%) and ECE (%) on clean ImageNet-1K validation set (no corruption). ViT-Base as base model.

| Method | Acc (%) | Delta from NoAdapt | ECE (%) |
|---|---|---|---|
| NoAdapt | 85.17 | — | 9.6 |
| TENT | 84.80 | −0.37 | 3.9 |
| CoTTA | 83.91 | −1.26 | 1.8 |
| SAR | 84.52 | −0.65 | 0.9 |
| FOA (ours) | **85.11** | **−0.06** | 2.1 |

Notes:
- FOA shows minimal in-distribution accuracy degradation (−0.06%, best among all adapted methods)
- CoTTA shows largest forgetting (−1.26%)
- NoAdapt ECE (9.6%) is the highest; FOA ECE (2.1%) is much lower due to activation discrepancy regularization
- Success due to: (1) no model weight modification; (2) regularization back to source distribution
