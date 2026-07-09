---
# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_intra_lpips.md](tables/table1_intra_lpips.md) | Table 1, §5.3 | C01, C03 | Main Intra-LPIPS (↑) results across 5 adaptation tasks and 8 methods (TGAN through LDM-TAN); shows TAN achieves best diversity on most tasks with only 1.3–1.6% parameter rate. |
| [tables/table2_fid.md](tables/table2_fid.md) | Table 2, §5.3 | C02 | FID (↓) results on FFHQ→Babies and FFHQ→Sunglasses for 7 methods; shows TAN achieves FID=20.06 on Sunglasses, dramatically outperforming the prior best of 34.75 (DDPM-PA). |
| [tables/table3_appendix_lpips.md](tables/table3_appendix_lpips.md) | Table 3, Appendix A.1 | C01 | Additional Intra-LPIPS results on FFHQ→Sketches and FFHQ→Amedeo's paintings; DDPM-TAN achieves 0.544±0.025 on Sketches, far outperforming all baselines. |
| [tables/table4_gamma_sensitivity.md](tables/table4_gamma_sensitivity.md) | Table 4, Appendix A.2 | C05 | FID and Intra-LPIPS vs. γ (similarity guidance scale) for FFHQ→Sunglasses; optimal at γ=5 (FID=18.13), showing U-shaped FID curve with overfitting at higher γ. |
| [tables/table5_omega_sensitivity.md](tables/table5_omega_sensitivity.md) | Table 5, Appendix A.2 | C05 | FID and Intra-LPIPS vs. ω (PGD step size) for FFHQ→Sunglasses; optimal at ω=0.02 (FID=18.13), stable in range [0.01, 0.03]. |
| [tables/table6_iteration_sensitivity.md](tables/table6_iteration_sensitivity.md) | Table 6, Appendix A.2 | C03, C05 | FID and Intra-LPIPS vs. number of training iterations for FFHQ→Sunglasses; FID reaches minimum at 300 iterations, stabilizes and slightly increases beyond 400. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure1_lpips_transfer.md](figures/figure1_lpips_transfer.md) | Figure 1, §1 | C04 | LPIPS distances during FFHQ→Sunglasses fine-tuning for two fixed-noise images across training iterations; demonstrates divergent transfer rates — one image overfits while the other underfits at the same iteration. |
| [figures/figure4_ablation.md](figures/figure4_ablation.md) | Figure 4, §5.4 | C05 | Ablation study FID scores for 4 model variants on FFHQ→10-shot Sunglasses at 300 iterations; shows progressive FID improvement from baseline (38.65) → adaptor (41.88) → w/o adversarial (26.41) → full TAN (20.06). |
