---
# Table 13: Sensitivity to Trade-off Parameter λ
- **Source**: Table 13, Appendix C
- **Caption**: "Sensitivity analyses regarding the trade-off parameter λ (see Eqn. (5)) in our FOA. We report results on ImageNet-C (Gaussian noise, severity level 5) using ViT-Base with batch size 64."
- **Conditions**: ViT-Base (full precision, 32-bit); batch size 64; ImageNet-C, Gaussian noise, severity level 5

| λ | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 |
|---|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Acc. (%, ↑) | 61.1 | 61.8 | 61.7 | 61.5 | 61.3 | 61.4 | 61.5 | 61.3 | 61.2 | 61.2 |
| ECE (%, ↓) | 5.9 | 3.2 | 2.6 | 2.5 | 2.6 | 2.9 | 3.3 | 3.8 | 4.0 | 4.4 |

**Notes**:
- Accuracy varies only from 61.1% to 61.8% across λ ∈ [0.1, 1.0] — low sensitivity
- ECE is more sensitive: best (2.5%) at λ=0.4, degrading to 5.9% at λ=0.1
- Best overall performance (accuracy + ECE) in range λ ∈ {0.3, 0.4, 0.5}
- Default λ = 0.4 (×BS/64 scaling) chosen accordingly
