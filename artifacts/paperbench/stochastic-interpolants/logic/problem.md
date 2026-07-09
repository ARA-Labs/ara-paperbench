# Problem Specification

## Observations

### O1: Standard generative models use data-agnostic base densities
- **Statement**: Flow matching, rectified flow, and stochastic interpolants conventionally set the base density ρ₀ to a standard Gaussian N(0, Id), regardless of the structure of the target density ρ₁.
- **Evidence**: §1 "the choice of Gaussian base represents an absence of prior knowledge about the problem structure, and existing works have yet to fully explore the strength of base densities adapted to the target"
- **Implication**: The transport from a generic Gaussian to a structured target density may be unnecessarily complex, leading to curved trajectories that require many ODE steps to integrate accurately.

### O2: Independent coupling induces high transport costs for structured problems
- **Statement**: For inverse problems (inpainting, super-resolution), starting from an independent Gaussian base creates crossing trajectories and high kinetic energy E[|İₜ|²] compared to starting from a corrupted version of the target.
- **Evidence**: Fig. 2 (right panel) shows complex crossing trajectories for independent coupling on a GMM-to-GMM transport; Proposition 3.1 establishes E[|Xₜ₌₁(x₀)-x₀|²] ≤ ∫E[|İₜ|²]dt
- **Implication**: The upper bound on transport cost in (15) is strictly larger for independent couplings than for well-designed dependent couplings.

### O3: Inverse problems have natural data-dependent structure
- **Statement**: In inpainting and super-resolution, we always observe a degraded/partial version of the target x₁ at inference time. This corrupted observation m(x₁) can be used to define the base distribution.
- **Evidence**: §4.1 "the missing areas of the image are defined at time zero as independent normal random variables"; §4.2 "x₀ = U(D(x₁)) + σζ"
- **Implication**: Setting x₀ = m(x₁) + σζ (corrupted target + small noise) creates a base proximal to the target, drastically simplifying transport.

### O4: Existing coupling methods have practical limitations
- **Statement**: Minibatch OT methods (Pooladian et al., 2023; Tong et al., 2023) become uninformative on large datasets; learned conditional methods (Lee et al., 2023) introduce bias by sampling from an independent Gaussian at inference; Schrödinger bridge methods (De Bortoli et al., 2021) require costly iterative SDE solving.
- **Evidence**: §2 "for large datasets, may become uninformative as to the true coupling"; "introduces a potential bias"; "costly in practice"
- **Implication**: A flexible, deterministic, simulation-free method for data-dependent couplings is needed.

## Gaps

### G1: No unified framework for data-dependent base densities in flow-based models
- **Statement**: Existing stochastic interpolant and flow matching formulations lack a principled way to define and use ρ(x₀,x₁) = ρ₁(x₁)ρ₀(x₀|x₁) with provable correctness guarantees.
- **Caused by**: O1, O4
- **Existing attempts**: Score-based diffusion with conditioning (Saharia et al., 2022), Schrödinger bridges (De Bortoli et al., 2021), I²SB (Liu et al., 2023a)
- **Why they fail**: Diffusion methods tie the base density to the noise schedule; Schrödinger bridges require expensive iterative algorithms; existing methods don't cleanly separate coupling design from velocity learning.

### G2: Training objective unclear for correlated (x₀, x₁) pairs
- **Statement**: When x₀ and x₁ are correlated, it is not obvious whether the standard quadratic regression objective for the velocity field remains valid and unbiased.
- **Caused by**: O1, O3
- **Existing attempts**: OT-conditioned flow matching modifies the training distribution but keeps the same loss
- **Why they fail**: No formal proof that the regression objective in (7) is valid under arbitrary joint density ρ(x₀,x₁).

## Key Insight

- **Insight**: The transport equation ∂ₜρₜ(x) + ∇·(bₜ(x)ρₜ(x)) = 0 and the quadratic regression objective Lb(b̂) hold for ANY joint coupling ρ(x₀,x₁) with the correct marginals—not just independent couplings. The velocity field is always the conditional expectation bₜ(x) = E(İₜ|Iₜ=x), regardless of whether (x₀,x₁) are correlated.
- **Derived from**: O2, O3, G2
- **Enables**: Designing x₀ = m(x₁) + σζ as a task-specific degradation of x₁, plugging it into the same training loop as before, and obtaining a generative model that starts near the target.

## Assumptions

- A1: The joint density ρ(x₀,x₁) has finite second moments and correct marginals (eq. 2–3).
- A2: The corrupted observation m(x₁) is known or observable at inference time.
- A3: The noise coefficient σ > 0 is chosen small enough to keep transport costs low but large enough to avoid lower-dimensional manifold degeneracies.
- A4: The velocity field can be approximated well by a neural network (U-Net) trained via SGD.
- A5: ImageNet class labels are available and used as conditional information ξ.
