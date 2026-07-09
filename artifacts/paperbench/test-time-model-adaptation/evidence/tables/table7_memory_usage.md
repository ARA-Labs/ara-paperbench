---
# Table 7: Run-Time Memory Usage (MB)
- **Source**: Table 7, Section 4.4
- **Caption**: "Comparison w.r.t. run-time memory (MB) usage. Results obtained via ViT-Base (32/8-bit) on ImageNet-C (Gaussian, level 5). FOA-I V1/V2 denote storing features/images for interval update under batch size (BS) 1. The memory for 8-bit ViT is an ideal estimation by 0.25× memory of 32-bit ViT per Liu et al. (2021b)."
- **Conditions**: ViT-Base; ImageNet-C, Gaussian noise, severity level 5; single RTX 3090 GPU

## Standard Methods (Various Batch Sizes)

| Method | BP | BS=1 | BS=4 | BS=8 | BS=16 | BS=32 | BS=64 |
|--------|-----|------|------|------|-------|-------|-------|
| NoAdapt | ✗ | — | — | — | — | — | — |
| TENT | ✓ | 1,550 | 2,756 | — | — | — | 5,165 |
| CoTTA | ✓ | 1,792 | 2,312 | 3,282 | 5,226 | 9,105 | 16,836 |
| FOA (32-bit) | ✗ | — | — | — | — | — | 832 |
| FOA (8-bit) | ✗ | — | — | — | — | — | 208 |

## FOA-I Variants (BS=1, Interval-Based Updates)

| Method | I=1 | I=4 | I=8 | I=16 | I=32 | I=64 |
|--------|-----|-----|-----|------|------|------|
| FOA-I V1 (32-bit) | — | — | — | — | — | — |
| FOA-I V1 (8-bit) | — | — | — | — | — | — |
| FOA-I V2 (32-bit) | — | — | — | — | — | — |
| FOA-I V2 (8-bit) | — | — | — | — | — | — |

**Notes**:
- FOA requires only 832 MB vs TENT 5,165 MB and CoTTA 16,836 MB at BS=64 (32-bit) — approximately 6.2× and 20.2× reductions
- FOA (8-bit) uses 208 MB at BS=64 = 0.25 × 832 MB, achieving ~24.8× reduction vs TENT (32-bit)
- FOA uses ~3 MB extra memory vs NoAdapt at BS=4 (for feature statistics)
- Exact FOA-I V1/V2 cell values not individually specified in the paper; V1 stores CLS features, V2 stores images
- Exact NoAdapt memory values not individually specified in the paper text (listed as lower than all other methods)
