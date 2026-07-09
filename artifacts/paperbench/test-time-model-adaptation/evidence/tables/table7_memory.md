# Table 7: Run-Time Memory Usage (MB)
- **Source**: Table 7, Section 4.4
- **Caption**: "Comparison w.r.t. run-time memory (MB) usage. Results obtained via ViT-Base (32/8-bit) on ImageNet-C (Gaussian, level 5). FOA-I V1/V2 denote storing features/images for interval update under batch size (BS) 1. The memory for 8-bit ViT is an ideal estimation by 0.25× memory of 32-bit ViT per Liu et al. (2021b)."
- **Model**: ViT-Base 32-bit and 8-bit
- **Measurement**: Run-time memory (MB)

| Method | BP | BS=1 | BS=4 | BS=8 | BS=16 | BS=32 | BS=64 |
|--------|-----|------|------|------|-------|-------|-------|
| NoAdapt | ✗ | — | — | — | — | — | 1,550 |
| TENT | ✓ | — | — | — | — | — | 5,165 |
| CoTTA | ✓ | 1,792 | 2,312 | 3,282 | 5,226 | 9,105 | 16,836 |
| FOA (32-bit) | ✗ | — | — | — | — | — | 832 |
| FOA (8-bit) | ✗ | — | — | — | — | — | 208 (estimated: 0.25 × 832) |

Note: FOA-I V1 (stores features) and FOA-I V2 (stores images) variants for BS=1 with different interval lengths I={1,4,8,16,32,64} are described in the paper but exact MB values for all cells are not fully reported in the text; partial values: FOA requires 3 MB extra memory over NoAdapt at BS=4 (stated in §4.4).
