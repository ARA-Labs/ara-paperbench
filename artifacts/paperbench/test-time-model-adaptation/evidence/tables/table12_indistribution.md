---
# Table 12: In-Distribution Performance (Clean ImageNet Validation Set)
- **Source**: Table 12, Section 4.4
- **Caption**: "Comparison w.r.t. in-distribution performance, i.e., on clean/original ImageNet validation set, with ViT as the base model."
- **Conditions**: ViT-Base (full precision, 32-bit); batch size 64; clean (uncorrupted) ImageNet-1K validation set

| Method | Acc. (%) | ECE (%) |
|--------|----------|---------|
| NoAdapt | 85.17 | 9.6 |
| TENT | 84.80 (−0.37) | 3.9 |
| CoTTA | 83.91 (−1.26) | 1.8 |
| SAR | 84.52 (−0.65) | 0.9 |
| FOA (ours) | 85.11 (−0.06) | 2.1 |

**Notes**:
- Numbers in parentheses show accuracy drop relative to NoAdapt baseline (85.17%)
- FOA suffers minimal in-distribution accuracy degradation (−0.06%), significantly less than TENT (−0.37%), CoTTA (−1.26%), and SAR (−0.65%)
- FOA does not modify model weights, preserving in-distribution performance
- FOA achieves lower ECE (2.1%) than NoAdapt (9.6%) on clean data due to activation discrepancy regularization
