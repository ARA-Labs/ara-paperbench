# Experiments

## E01: Theoretical validation of regression objective under dependent coupling
- **Verifies**: C01, C02
- **Setup**:
  - Model: Analytical / Gaussian mixture model (no neural network)
  - Hardware: CPU
  - Dataset: 2D Gaussian mixture model (GMM) with 3 modes
  - System: Stochastic interpolant with dependent coupling ρ(x₀,x₁)=ρ₁(x₁)ρ₀(x₀|x₁)
- **Procedure**:
  1. Define a 3-mode GMM source and target density in 2D.
  2. Define three coupling schemes: (a) independent coupling, (b) conditional velocity with discrete ξ, (c) data-dependent coupling ρ₀(x₀|x₁).
  3. For each coupling, compute the stochastic interpolant Iₜ = αₜx₀ + βₜx₁ with αₜ=1-t, βₜ=t.
  4. Verify that the transport equation ∂ₜρₜ + ∇·(bₜρₜ)=0 holds with bₜ(x)=E(İₜ|Iₜ=x).
  5. Compare E[|İₜ|²] for independent vs dependent coupling to verify the transport cost bound (Proposition 3.1).
- **Metrics**: Visual comparison of probability flow trajectories; expected kinetic energy E[|İₜ|²] at each time t.
- **Expected outcome**:
  - Dependent coupling produces simpler, non-crossing trajectories compared to independent coupling.
  - The dependent coupling kinetic energy E[|İₜ|²] is strictly smaller than the independent coupling kinetic energy.
  - The velocity regression objective is valid (minimizer equals bₜ) for all three coupling types.
- **Baselines**: Independent coupling (standard stochastic interpolant), conditionally-independent velocity with class labels.
- **Dependencies**: none

## E02: Inpainting FID on ImageNet-256
- **Verifies**: C03
- **Setup**:
  - Model: U-Net velocity model (Dim=256, DimMults=(1,1,2,3,4), ResNet block groups=8, learned_sinusoidal_cond=True, learned_sinusoidal_dim=32, attn_dim_head=64, attn_heads=4, random_fourier_features=False)
  - Hardware: Multi-GPU setup (Lightning Fabric parallelism)
  - Dataset: ImageNet (256×256 resolution), training and validation sets
  - System: (a) Uncoupled interpolant baseline; (b) Dependent coupling inpainting model
- **Procedure**:
  1. **Dependent coupling — training data preparation per sample**: Randomly tile each ImageNet training image into 64 equal-sized tiles (8×8 grid); select each tile to enter the mask with probability p=0.3. The mask takes the same value for all channels at each spatial location (single-channel mask broadcast). Construct x₀ = ξ∘x₁ + (1-ξ)∘ζ with ζ~N(0,I) (separate independent noise per channel for masked pixels). Append mask ξ as extra channel(s) to model input. Also append a channel uniformly filled with the integer class label value as additional conditioning.
  2. **Uncoupled baseline — training data preparation**: Draw x₀~N(0,I) independently of x₁. Sample tᵢ~U(0,1). Append class-label channel to model input.
  3. **Interpolant**: Compute Iₜ = t·x₀ + (1-t)·x₁ and İₜ = x₁-x₀ (since α̇ₜ=1, β̇ₜ=-1 with αₜ=t, βₜ=1-t).
  4. **Training**: Use Adam optimizer, initial lr=2e-4, StepLR scheduler (γ=0.99 every N=1000 steps), no weight decay, gradient norm clipping at 10,000 (global L2 norm). Batch size=32; train for 200,000 gradient steps. Loss: L̂_b = n_b⁻¹ Σ[|b̂ₜ(Iₜ)|² - 2İₜ·b̂ₜ(Iₜ)].
  5. **Output masking**: Apply mask to velocity output so unmasked (known) pixels receive zero velocity. Velocity model acts only on image channels, not appended mask or class channels.
  6. **Sampling (evaluation)**: Apply same 64-tile mask procedure (p=0.3, same value for all channels). Construct x₀ from test image. Append class-label channel. Integrate: X̂_{n+1} = X̂_n + N⁻¹·b̂_{n/N}(X̂_n) (in practice: Dopri adaptive solver from torchdiffeq). Apply velocity mask at each step.
  7. Compute FID-50k on ImageNet validation set using Fréchet Inception Distance (FID) comparing generated and real feature distributions via an Inception network.
- **Metrics**: FID-50k (lower is better).
- **Expected outcome**:
  - Dependent coupling achieves lower FID-50k than the uncoupled interpolant baseline.
  - Dependent coupling FID is substantially below the baseline value.
- **Baselines**: Uncoupled Interpolant (Gaussian base, independent coupling).
- **Dependencies**: none

## E03: Super-resolution FID on ImageNet 64×64→256×256
- **Verifies**: C04
- **Setup**:
  - Model: U-Net velocity model (same architecture as E02)
  - Hardware: Multi-GPU setup (Lightning Fabric parallelism)
  - Dataset: ImageNet (256×256 high-res target; 64×64 low-res input), train and validation sets
  - System: Dependent coupling super-resolution model
- **Procedure**:
  1. **Training data preparation per sample**: Take ImageNet training image x₁∈R^{C×256×256}. Downsample by cropping to 64×64 using nearest-neighbor interpolation (D: 256×256→64×64). Upsample back to 256×256 via nearest-neighbor (U: 64×64→256×256). Add Gaussian noise: x₀ = U(D(x₁)) + σζ, ζ~N(0,I_d). Set conditioning variable ξ = U(D(x₁)). Append ξ (upsampled low-res image, same 3 channels) to interpolant input along channel dimension. Also append a channel uniformly filled with the integer class label value as additional conditioning. The corrupted image x₀ is appended to x₁ along channel dimension when building the full model input.
  2. **Interpolant**: Sample tᵢ~U(0,1). Compute Iₜ = (1-t)·x₀ + t·x₁ and İₜ = x₁-x₀ (αₜ=1-t, βₜ=t).
  3. **Training**: Use Adam optimizer, initial lr=2e-4, StepLR scheduler (γ=0.99 every N=1000 steps), no weight decay, gradient norm clipping at 10,000. Batch size=32; 200,000 gradient steps. Loss: L̂_b = n_b⁻¹ Σ[|b̂ₜ(Iₜ)|² - 2İₜ·b̂ₜ(Iₜ)].
  4. **Velocity masking**: Velocity field acts only on the image channels (first C=3 channels), NOT on the appended low-resolution image channels or appended class channel.
  5. **Sampling (evaluation)**: From ImageNet val image x₁_test: downsample by cropping to 64×64 then upsample to 256×256 via nearest-neighbor. Append class-label channel. Construct x₀ = U(D(x₁_test)) + ζ (σ=1). Append corrupted image x₀ to x₁_test along channel dimension. Integrate: X̂_{n+1} = X̂_n + N⁻¹·b̂_{n/N}(X̂_n) (in practice: Dopri solver).
  6. Compute FID-50k against 50k random training samples (train FID) and 50k validation samples (valid FID) using Fréchet Inception Distance.
- **Metrics**: FID-50k train and FID-50k valid (lower is better).
- **Expected outcome**:
  - Dependent coupling achieves lower FID-50k than all prior methods including I²SB.
  - Valid FID is lower than the best published prior result (I²SB valid FID).
- **Baselines**: Improved DDPM, SR3, ADM, Cascaded Diffusion, I²SB (see Table 3 for exact values).
- **Dependencies**: none

## E04: Qualitative trajectory comparison on GMM transport
- **Verifies**: C05
- **Setup**:
  - Model: Analytical transport (exact velocity, no neural network)
  - Hardware: CPU
  - Dataset: 2D Gaussian Mixture Model (3 modes) as both source and target
  - System: Three variants: (1) data-dependent coupling, (2) conditional velocity with ξ∈{0,1,2}, (3) unconditional + independent coupling
- **Procedure**:
  1. Define 3-mode GMM source ρ₀ and target ρ₁ in 2D.
  2. For dependent coupling: ρ(x₀,x₁) = ρ₁(x₁)ρ₀(x₀|x₁), compute exact probability flow trajectories.
  3. For conditional velocity: ρ(x₀,x₁) = ρ₀(x₀)ρ₁(x₁), condition bₜ(x,ξ) on mode index ξ.
  4. For independent coupling: ρ(x₀,x₁) = ρ₀(x₀)ρ₁(x₁), unconditional bₜ(x).
  5. Visualize trajectories Xₜ for t ∈ [0,1] for each variant.
- **Metrics**: Visual complexity of trajectories; presence of crossing; presence of auxiliary modes in intermediate density ρₜ.
- **Expected outcome**:
  - Dependent coupling: simple, non-crossing trajectories; no auxiliary modes in ρₜ.
  - Conditional velocity: three separated flows Xₜ^ξ, each simple but requiring knowledge of ξ.
  - Independent coupling: complex, crossing trajectories with auxiliary intermediate modes.
- **Baselines**: Independent coupling (right panel of Fig. 2).
- **Dependencies**: none
