# Evidence Index

## Figures
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/fig5_1_gaussian_targets.md](figures/fig5_1_gaussian_targets.md) | Figure 5.1, §5.1 | C05, C06 | Forward KL divergence vs. number of gradient evaluations for BaM, ADVI, GSM, Score, Fisher on Gaussian targets at D=4, 16, 64, 256; shows BaM converges orders of magnitude faster than ADVI. |
| [figures/fig5_2_nongaussian_targets.md](figures/fig5_2_nongaussian_targets.md) | Figure 5.2, §5.1 | C01, C05 | Forward KL divergence vs. gradient evaluations for sinh-arcsinh non-Gaussian targets (D=10) varying skew s and tail τ; shows BaM faster convergence and GSM instability at high skew. |
| [figures/fig5_3_posteriordb.md](figures/fig5_3_posteriordb.md) | Figure 5.3, §5.2 | C05, C06 | Relative posterior mean error vs. gradient evaluations for three PosteriorDB models (arK D=7, GP D=13, 8-schools D=10) comparing BaM, GSM, ADVI at B=8 and B=32. |
| [figures/fig5_4_deep_generative.md](figures/fig5_4_deep_generative.md) | Figure 5.4, §5.3 | C05, C06 | Image reconstruction MSE vs. iterations for CIFAR-10 deep generative model (D=256) at batch sizes B=10, 100, 300 for BaM, ADVI, GSM, and Amortized VI. |
| [figures/figE1_wallclock.md](figures/figE1_wallclock.md) | Figure E.1, App. E.2 | C06 | Wallclock timing comparison of BaM, ADVI, GSM for Gaussian targets at D=4, 16, 64, 128, 256; shows gradient evaluations dominate cost for D≤64. |
| [figures/figE3_gaussian_reverse_kl.md](figures/figE3_gaussian_reverse_kl.md) | Figure E.3, App. E.3 | C05, C06 | Reverse KL divergence vs. gradient evaluations for Gaussian targets at D=4, 16, 64, 256; consistent with forward KL results in Figure 5.1. |
| [figures/figE4_nongaussian_reverse_kl.md](figures/figE4_nongaussian_reverse_kl.md) | Figure E.4, App. E.4 | C05 | Reverse KL divergence vs. gradient evaluations for non-Gaussian sinh-arcsinh targets; GSM reverse KL diverges at s=1.8 confirming instability. |
| [figures/figE6_posteriordb_sd_error.md](figures/figE6_posteriordb_sd_error.md) | Figure E.6, App. E.5 | C05, C06 | Relative posterior standard deviation error for PosteriorDB models; similar trends as mean error except hierarchical model where BaM has larger SD error. |
