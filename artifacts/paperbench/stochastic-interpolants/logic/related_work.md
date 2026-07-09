# Related Work

## RW01: Albergo & Vanden-Eijnden, 2022
- **DOI**: arXiv:2209.15571
- **Type**: imports
- **Delta**:
  - What changed: This work introduces **data-dependent couplings** ρ(x₀,x₁)=ρ₁(x₁)ρ₀(x₀|x₁). Original stochastic interpolants only considered independent couplings ρ(x₀,x₁)=ρ₀(x₀)ρ₁(x₁).
  - Why: To adapt the base density to the structure of the target, reducing transport cost for inverse problems.
- **Claims affected**: C01, C02
- **Adopted elements**: Stochastic interpolant definition (eq. 1), transport equation framework, quadratic regression objective, probability flow ODE/SDE characterization.

## RW02: Albergo et al., 2023
- **DOI**: arXiv:2303.08797
- **Type**: imports
- **Delta**:
  - What changed: Extends to dependent couplings and conditional generation; provides new proofs with conditioning variables ξ (Appendix A).
  - Why: Unifying framework for flows and diffusions; dependent coupling is a strict generalization.
- **Claims affected**: C01, C02
- **Adopted elements**: Generalized interpolant with conditioning (Definition A.1), score identity, velocity/score regression objectives.

## RW03: Lipman et al., 2022
- **DOI**: arXiv:2210.02747
- **Type**: baseline
- **Delta**:
  - What changed: Flow matching uses an independent coupling (Gaussian base); this work generalizes to dependent couplings.
  - Why: Flow matching is a prominent related method; dependent coupling can be viewed as flow matching with a non-Gaussian, data-dependent base.
- **Claims affected**: C01
- **Adopted elements**: Simulation-free regression for velocity field.

## RW04: Liu et al., 2022 (Rectified Flow)
- **DOI**: arXiv:2209.03003
- **Type**: baseline
- **Delta**:
  - What changed: Rectified flow uses independent Gaussian base; this work designs the base from data.
  - Why: Rectified flow seeks straight trajectories via data; dependent coupling achieves straighter trajectories by design.
- **Claims affected**: C02
- **Adopted elements**: Straight-line interpolant idea.

## RW05: Pooladian et al., 2023
- **DOI**: arXiv:2304.14772
- **Type**: bounds
- **Delta**:
  - What changed: Minibatch OT builds couplings from batch-level optimal transport; this work uses task-designed deterministic couplings.
  - Why: Minibatch OT becomes uninformative at dataset scale; task-designed couplings are always informative.
- **Claims affected**: C02
- **Adopted elements**: Motivation for reduced transport cost via better couplings.

## RW06: Tong et al., 2023
- **DOI**: ICML Workshop 2023
- **Type**: bounds
- **Delta**:
  - What changed: Minibatch OT for flow matching; this work uses analytic data-dependent couplings.
  - Why: Avoid uninformative couplings at scale.
- **Claims affected**: C02
- **Adopted elements**: Minibatch OT coupling motivation.

## RW07: Lee et al., 2023
- **DOI**: arXiv:2301.12003
- **Type**: baseline
- **Delta**:
  - What changed: Lee et al. learn qφ(x₀|x₁) but sample from N(0,I) at inference; this work uses the actual dependent coupling at inference time, avoiding the bias.
  - Why: Sampling from the true ρ₀(x₀|x₁) at inference is consistent and unbiased.
- **Claims affected**: C01
- **Adopted elements**: Motivation for data-dependent base via learned conditional.

## RW08: Liu et al., 2023a (I²SB)
- **DOI**: arXiv:2302.05872
- **Type**: baseline
- **Delta**:
  - What changed: I²SB uses Schrödinger bridge diffusion bridges with known coupling; this work uses a simpler, more flexible stochastic interpolant formulation that separates bridging from coupling.
  - Why: Stochastic interpolants are simpler (no need to solve Schrödinger bridge equations) and more flexible.
- **Claims affected**: C04
- **Adopted elements**: Benchmark FID numbers for super-resolution (I²SB: 2.70 valid FID).

## RW09: De Bortoli et al., 2021
- **DOI**: NeurIPS 2021
- **Type**: baseline
- **Delta**:
  - What changed: Schrödinger bridge requires expensive iterative SDE solving; stochastic interpolants with dependent couplings are simulation-free.
  - Why: Computational efficiency; simulation-free training is a key advantage.
- **Claims affected**: C01
- **Adopted elements**: Schrödinger bridge as a coupling strategy.

## RW10: Saharia et al., 2022 (SR3)
- **DOI**: IEEE TPAMI 2022
- **Type**: baseline
- **Delta**:
  - What changed: SR3 uses score-based diffusion conditioned on low-res image; this work uses a deterministic ODE with data-dependent base.
  - Why: Simpler and better-performing approach for super-resolution.
- **Claims affected**: C04
- **Adopted elements**: Problem framing for super-resolution; FID benchmark (SR3: 11.30 train, 5.20 valid).

## RW11: Ho et al., 2020b (DDPM)
- **DOI**: NeurIPS 2020
- **Type**: imports
- **Delta**:
  - What changed: U-Net architecture from DDPM is reused as the velocity model; conditioning on class labels is inherited.
  - Why: Well-tested architecture for image generation; class conditioning is critical for ImageNet.
- **Claims affected**: C03, C04
- **Adopted elements**: U-Net architecture (dim=256, dim_mults=(1,1,2,3,4)), class label conditioning via embedding.

## RW12: Ho et al., 2022a (Cascaded Diffusion)
- **DOI**: JMLR 2022
- **Type**: baseline
- **Delta**:
  - What changed: Cascaded diffusion uses multiple diffusion stages; this work uses a single ODE with data-dependent coupling.
  - Why: Simpler single-stage approach; image-shaped conditioning strategy is adopted.
- **Claims affected**: C04
- **Adopted elements**: Channel concatenation for image-shaped conditioning; FID benchmark (Cascaded Diffusion: 4.88 train, 4.63 valid).
