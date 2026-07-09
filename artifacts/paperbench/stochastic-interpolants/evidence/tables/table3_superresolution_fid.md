# Table 3: FID-50k for Super-resolution (64×64 → 256×256)

**Source**: Table 3, §4.2 (page 7)
**Caption**: FID-50k for Super-resolution, 64×64 to 256×256. FIDs for baselines taken from (Saharia et al., 2022; Ho et al., 2022a; Liu et al., 2023a).
**Claims**: C04
**Dataset**: ImageNet (256×256 high resolution; 64×64 low resolution input)
**Metric**: FID-50k train and FID-50k valid (lower is better)
**Note**: "–" indicates the value was not reported for that model in the original sources.

| Model | Train FID-50k | Valid FID-50k |
|---|---|---|
| Improved DDPM (Nichol & Dhariwal, 2021) | 12.26 | — |
| SR3 (Saharia et al., 2022) | 11.30 | 5.20 |
| ADM (Dhariwal & Nichol, 2021) | 7.49 | 3.10 |
| Cascaded Diffusion (Ho et al., 2022a) | 4.88 | 4.63 |
| I²SB (Liu et al., 2023a) | — | 2.70 |
| **Dependent Coupling (Ours)** | **2.13** | **2.05** |

## Notes
- Baseline FID values sourced from original papers (Saharia et al., 2022; Ho et al., 2022a; Liu et al., 2023a).
- Our method sets new SOTA on both train and valid FID-50k.
- Train FID: comparing generated samples against 50k random training set images.
- Valid FID: comparing generated samples against 50k validation set images.
- The model uses x₀ = U(D(x₁)) + σζ as base, with nearest-neighbor downsampling/upsampling.
