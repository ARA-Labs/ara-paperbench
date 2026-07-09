# Heuristics

## H01: Reversed interpolant coefficients for inpainting (αₜ=t, βₜ=1-t)
- **Rationale**: In the inpainting task, x₀ = ξ∘x₁ + (1-ξ)∘ζ contains the clean image in known regions and noise in masked regions. Setting αₜ=t and βₜ=1-t means Iₜ = t·x₀ + (1-t)·x₁. Since unmasked pixels are identical in x₀ and x₁, the velocity İₜ = x₁-x₀ is zero on unmasked pixels for all t. This structural property allows masking the network output to enforce fixed unmasked pixels without information leakage.
- **Sensitivity**: high — changing to αₜ=1-t, βₜ=t would require different output masking logic.
- **Bounds**: αₜ and βₜ must satisfy α₀=β₁=1, α₁=β₀=0 (boundary conditions of the interpolant). Both αₜ=t and αₜ=1-t satisfy this with appropriate swapping of x₀ and x₁ roles.
- **Code ref**: [src/execution/inpainting.py]
- **Source**: §4.1 "In the interpolant (20), we set αₜ = t and βₜ = 1 − t"

## H02: Zero-velocity masking for unmasked pixels
- **Rationale**: Since İₜ = x₁ - x₀ = 0 on unmasked pixels (where x₀ = x₁), the true velocity is zero there. Masking the neural network output to be zero on known regions encodes this structural information, reducing the effective learning problem to only the masked regions and preventing the model from "wasting capacity" predicting zero velocity.
- **Sensitivity**: medium — omitting this masking likely degrades performance as the model must learn to output zero on known regions.
- **Bounds**: The mask ξ must be consistent between x₀ construction, network conditioning, and output masking.
- **Code ref**: [src/execution/inpainting.py]
- **Source**: §4.1 "we can build this property into our neural network model, and mask the output"

## H03: Small Gaussian noise σ added to super-resolution base
- **Rationale**: Setting x₀ = U(D(x₁)) + σζ with σ>0 adds a small amount of Gaussian noise to the upsampled low-resolution image. Without noise (σ=0), the base distribution would be concentrated on the image of the downsampling-upsampling operator D∘U, a lower-dimensional manifold in the ambient space. Adding noise σζ smoothes the base density over all of R^{C×W×H}, making it well-defined and non-degenerate.
- **Sensitivity**: medium — σ must be small enough to keep transport cost low but large enough to regularize the base density.
- **Bounds**: σ > 0 strictly required. Exact value not specified in paper.
- **Code ref**: [src/execution/superresolution.py]
- **Source**: §4.2 "Working with σ > 0 alleviates the associated singularities"

## H04: Gradient norm clipping at 10,000 (L2 norm of all parameters)
- **Rationale**: Clip the global gradient norm (treating all parameters as one vector) at 10,000 to prevent catastrophic gradient updates during training of the large U-Net on ImageNet. This is PyTorch's default norm type for `clip_grad_norm_`.
- **Sensitivity**: low — a very high threshold that mainly catches rare gradient explosions.
- **Bounds**: Clipping value = 10,000 (the norm of the entire parameter vector).
- **Code ref**: [src/execution/stochastic_interpolant.py]
- **Source**: Appendix B "We clip gradient norms at 10,000 (this is the norm of the entire set of parameters taken as a vector, the default type of norm clipping in PyTorch library)"

## H05: StepLR learning rate decay (γ=0.99, N=1000 steps)
- **Rationale**: Gradual learning rate decay prevents oscillation around the final optimum while still enabling fast early convergence at lr=2e-4. The multiplicative factor 0.99 per 1000 steps is mild, giving roughly lr×0.99^200 ≈ 0.135·lr after 200,000 steps.
- **Sensitivity**: medium — affects final model quality; too aggressive decay would under-train.
- **Bounds**: Initial lr=2e-4; decay factor γ=0.99 every N=1000 gradient steps.
- **Code ref**: [src/execution/stochastic_interpolant.py]
- **Source**: Appendix B "starting at learning rate 2e-4 with the StepLR scheduler which scales the learning rate by γ = .99 every N = 1000 steps"

## H06: Image-shaped conditioning via channel concatenation
- **Rationale**: Appending the conditioning image ξ (upsampled low-res image for super-resolution, or mask for inpainting) as additional channels to the U-Net input, following Ho et al. (2022a). This gives the network spatial access to conditioning at all resolution levels of the U-Net. Class labels are embedded via the class conditioning mechanism of the U-Net (learnable embeddings).
- **Sensitivity**: medium — concatenation depth affects early-layer processing of conditioning.
- **Bounds**: Conditioning channels are concatenated to input; network output channels correspond only to the image (not conditioning).
- **Code ref**: [src/execution/superresolution.py]
- **Source**: Appendix B "we follow (Ho et al., 2022a) and append upsampled low-resolution images to the input xₜ at each time step"
