# Constraints and Limitations

## Boundary Conditions (Where the Solution Works)

### BC1: Marginal consistency of coupling
The coupling ρ(x₀,x₁) = ρ₁(x₁)ρ₀(x₀|x₁) must satisfy:
$$\int \rho_0(x_0|x_1)\rho_1(x_1)dx_1 = \rho_0(x_0)$$
The choice x₀ = m(x₁) + σζ (σ>0) automatically satisfies this if m(x₁) is deterministic given x₁.

### BC2: Non-degenerate base distribution
For the score identity (eq. 6) to hold, γₜ ≠ 0 is required. In experiments γₜ = 0, so the score identity is NOT available, and only the velocity field is learned and used.

### BC3: σ > 0 for super-resolution
Must have σ > 0 to ensure x₀ is not concentrated on a lower-dimensional manifold (image of the downsampling/upsampling map). σ = 0 would cause the base density to be singular.

### BC4: Corrupted observation at inference
The data-dependent coupling requires that m(x₁) be available at inference time. For inpainting, the partial image is given; for super-resolution, the low-resolution image is given. If m(x₁) is not available (unconditional generation scenario), this framework reverts to independent coupling.

## Known Limitations

### L1: No exact numerical value for σ reported
The paper states σ > 0 for super-resolution but does not report the exact value used. The transport cost analysis uses σ, but the specific experimental value is not specified in paper text.

### L2: No inference-time correction / MCMC
The inpainting approach "does not necessitate any inference time corrections, such as the replacement method or MCMC" (§4.1). This may result in mild inconsistencies with known pixel values in borderline cases, though the generative model is statistically valid.

### L3: Requires clean coupling knowledge at training and inference
Unlike learned couplings (Lee et al., 2023), the coupling ρ₀(x₀|x₁) must be explicitly specified (not learned). For tasks without a known corruption model, this approach is not directly applicable.

### L4: Batch size and dataset scale constraints
The minibatch OT approach of Tong/Pooladian et al. becomes uninformative at dataset scale; our approach avoids this but requires the coupling to be task-designed rather than optimized from data.

### L5: FID evaluation uses 50k samples
Results use FID-50k, which may not capture mode-level quality differences; FID depends on the Inception network and is known to favor certain image statistics.

### L6: Inpainting mask is random at training but fixed at test
Training uses randomly generated masks (p=0.3); performance may vary for different mask patterns at test time. No adaptation for specific mask types is discussed.
