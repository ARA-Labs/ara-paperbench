# Table 1: Couplings

**Source**: Table 1, §3 (page 3)
**Caption**: Couplings. Standard formulations of flows and diffusions construct generative models built upon an independent coupling. (Lee et al., 2023) learn qφ(x₀|x₁) jointly with the velocity to define the coupling during training, but instead sample from ρ₀ = N(0, Id) for generation. (Tong et al., 2023) and (Pooladian et al., 2023) build couplings by running mini-batch optimal transport algorithms (Cuturi, 2013). Here we focus on couplings enabled by our generic formalism, which bears similarities with (Liu et al., 2023a; Somnath et al., 2023).
**Claims**: C01

| Coupling PDF ρ(x₀, x₁) | Base PDF | Description |
|---|---|---|
| ρ₁(x₁)ρ₀(x₀) | x₀ ~ N(0, Id) | Independent |
| ρ(x₀\|x₁)ρ₁(x₁) | x₀ ~ qφ(x₀\|x₁) | Learned conditional |
| mb-OT(x₁, x₀) | x₀ ~ N(0, Id) | Minibatch OT |
| ρ₁(x₁)ρ₀(x₀\|x₁) | x₀ ~ ρ₀(x₀\|x₁) | **Dependent-coupling (this work)** |
