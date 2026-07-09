# Claims

## C01: Quadratic regression remains valid for dependent couplings
- **Statement**: The velocity field bₜ(x) = E(İₜ|Iₜ=x) is the unique minimizer of the quadratic objective Lb(b̂) = ∫E[|b̂ₜ(Iₜ)|² - 2İₜ·b̂ₜ(Iₜ)]dt for ANY joint density ρ(x₀,x₁) with the correct marginals—dependent or independent.
- **Status**: supported
- **Falsification criteria**: Find a dependent coupling for which the minimizer of Lb is not bₜ(x) = E(İₜ|Iₜ=x), or for which the transport equation (5) fails to hold.
- **Proof**: [E01]
- **Dependencies**: none
- **Tags**: theory, regression, velocity field, transport equation

## C02: Dependent couplings reduce transport cost upper bound
- **Statement**: For the coupling x₀ = m(x₁) + σζ with αt=1-t, βt=t, the transport cost bound E[|Xₜ₌₁(x₀)-x₀|²] ≤ ∫E[|İₜ|²]dt equals dσ², which is strictly less than the independent-coupling bound 2E[|x₁|²] + dσ².
- **Status**: supported
- **Falsification criteria**: Demonstrate a case where the dependent coupling bound is ≥ the independent coupling bound when m(x₁) is proximal to x₁.
- **Proof**: [E01]
- **Dependencies**: C01
- **Tags**: theory, transport cost, optimal transport, Wasserstein

## C03: Dependent coupling inpainting outperforms uncoupled baseline on ImageNet
- **Statement**: Training on ImageNet with the data-dependent inpainting coupling (x₀ = ξ∘x₁ + (1-ξ)∘ζ, αt=t, βt=1-t) achieves FID-50k of 1.13, compared to 1.35 for the uncoupled baseline.
- **Status**: supported
- **Falsification criteria**: Reproduce the experiment and obtain FID-50k ≥ 1.35 for dependent coupling or ≤ 1.13 for the uncoupled baseline.
- **Proof**: [E02]
- **Dependencies**: C01
- **Tags**: inpainting, ImageNet, FID, empirical

## C04: Dependent coupling super-resolution achieves SOTA FID on ImageNet 64→256
- **Statement**: The dependent coupling model trained on ImageNet 64×64→256×256 super-resolution achieves FID-50k of 2.13 (train) and 2.05 (validation), surpassing the previous best I²SB (2.70 valid).
- **Status**: supported
- **Falsification criteria**: Reproduce the experiment and obtain validation FID-50k ≥ 2.70 for the dependent coupling model.
- **Proof**: [E03]
- **Dependencies**: C01, C02
- **Tags**: super-resolution, ImageNet, FID, SOTA, empirical

## C05: Data-dependent couplings simplify transport trajectories qualitatively
- **Statement**: Dependent couplings (ρ(x₀,x₁) = ρ₁(x₁)ρ₀(x₀|x₁)) produce simpler, non-crossing probability flow trajectories compared to independent couplings on GMM-to-GMM transport, with no formation of auxiliary intermediate modes.
- **Status**: supported
- **Falsification criteria**: Demonstrate that dependent coupling probability flows exhibit crossing trajectories or intermediate auxiliary modes on the GMM example in Figure 2.
- **Proof**: [E04]
- **Dependencies**: C02
- **Tags**: transport, GMM, trajectory, qualitative
