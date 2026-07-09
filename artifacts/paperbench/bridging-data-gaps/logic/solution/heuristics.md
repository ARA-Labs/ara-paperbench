---
# Heuristics

## H01: Initialize all adaptor layer parameters to zero
- **Rationale**: Zero initialization ensures the adaptor module outputs zero at the start of training, so the augmented model xl_t = θl(x^(l-1)) + ψl(x^(l-1)) behaves identically to the pre-trained frozen model at initialization. This prevents the adaptor from disrupting the pre-trained model's denoising capability at the start of fine-tuning and provides a stable starting point.
- **Sensitivity**: high
- **Bounds**: Must be zero at initialization; any non-zero initialization risks corrupting pre-trained representations from the first step
- **Code ref**: [src/execution/tan_core.py]
- **Source**: §5.2 Configurations ("To ensure the adapter layer outputs are initialized to zero, we set all the extra layer parameters to zero.")

## H02: Similarity guidance scale γ = 5
- **Rationale**: γ controls the strength of the classifier gradient correction term. Too small → insufficient domain transfer; too large → overfitting (generated images become too similar to target training images or degrade to noise). γ=5 achieves minimum FID (18.13) on FFHQ→Sunglasses. Intra-LPIPS decreases monotonically with γ, indicating diversity decreases with larger γ.
- **Sensitivity**: high
- **Bounds**: Optimal at γ=5; performance degrades significantly above this value (FID rises to 24.12 and 29.48 at higher values; see Table 4)
- **Code ref**: [src/execution/tan_core.py]
- **Source**: §5.2 Configurations; Appendix A.2 Table 4

## H03: PGD step size ω = 0.02
- **Rationale**: ω is the "learning rate" for the inner maximization gradient ascent. Too small → insufficient noise perturbation (fails to find worst-case noise). Too large → overfitting in generated images (noise too aggressive). ω=0.02 achieves minimum FID (18.13); results are relatively stable in ω ∈ [0.01, 0.03].
- **Sensitivity**: medium
- **Bounds**: Stable range [0.01, 0.03]; optimal at 0.02. FID at ω=0.01 is 18.42, at ω=0.02 is 18.13, at ω=0.03 is 18.42 (Table 5)
- **Code ref**: [src/execution/tan_core.py]
- **Source**: §5.2 Configurations; Appendix A.2 Table 5

## H04: Number of PGD inner steps J = 10
- **Rationale**: J controls how many gradient ascent steps are used to approximate the worst-case noise. More steps → better approximation of the true inner maximum but higher computational cost. J=10 was chosen as a practical trade-off. Used uniformly across all experiments.
- **Sensitivity**: medium
- **Bounds**: Set to 10 for all experiments; no ablation over J is reported
- **Code ref**: [src/execution/tan_core.py]
- **Source**: §5.2 Configurations ("we assign J=10 and ω=0.02 for most transfer learning tasks")

## H05: Training for approximately 300 iterations
- **Rationale**: 300 iterations achieves minimum FID for FFHQ→Sunglasses (FID=18.13). Below ~250 iterations, underfitting occurs (high FID); above ~400 iterations, overfitting begins and Intra-LPIPS decreases. This is vastly fewer than the ~5,000 iterations required by prior methods, enabled by the adversarial noise selection targeting hard cases.
- **Sensitivity**: medium
- **Bounds**: Optimal at 300; stable plateau around 400; recommended range [250, 400] for FFHQ→Sunglasses. May need adjustment for other domain pairs.
- **Code ref**: [src/execution/tan_core.py]
- **Source**: Appendix A.2 Table 6; §5.3 ("our approach only necessitates approximately 300 iterations")
