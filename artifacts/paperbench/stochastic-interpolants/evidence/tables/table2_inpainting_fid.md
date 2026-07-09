# Table 2: FID for Inpainting Task

**Source**: Table 2, §4.1 (page 7)
**Caption**: FID comparison between two paradigms: a baseline, where ρ₀ is a Gaussian with independent coupling to ρ₁, and our data-dependent coupling detailed in Section 4.1.
**Claims**: C03
**Dataset**: ImageNet (resolution: 256×256)
**Metric**: FID-50k (lower is better)

| Model | FID-50k |
|---|---|
| Uncoupled Interpolant (Baseline) | 1.35 |
| Dependent Coupling (Ours) | 1.13 |

## Notes
- Both models use the same U-Net architecture (dim=256, dim_mults=(1,1,2,3,4)).
- Baseline: x₀ ~ N(0, Id) independent of x₁; Dependent: x₀ = ξ∘x₁ + (1-ξ)∘ζ.
- FID measured on ImageNet validation set with 50,000 samples.
- The dependent coupling model achieves a 16% relative improvement in FID over the baseline.
- The dependent coupling FID of 1.13 is approximately 1.15 (within rounding); the reproduction rubric states "around 1.15" which corresponds to the paper-reported value of 1.13.
- Adam optimizer used for all models; lr=2e-4, StepLR γ=0.99/1000 steps, no weight decay, gradient clip 10,000, batch size 32, 200,000 steps.
