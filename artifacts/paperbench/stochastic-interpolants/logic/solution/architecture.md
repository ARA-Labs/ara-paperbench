# System Architecture

## Overview

The system consists of three major components: (1) the **Interpolant Constructor** that builds coupled (x₀, x₁) pairs and computes Iₜ, (2) the **Velocity Network** (U-Net) that approximates bₜ(x, ξ), and (3) the **ODE/SDE Solver** that integrates the probability flow at inference time.

## Components

### Component 1: Interpolant Constructor

- **Purpose**: Given a target sample x₁ and a coupling type, compute the base sample x₀ and the interpolant Iₜ at a random time t.
- **Inputs**:
  - x₁: target sample from ρ₁ (ImageNet image, C×W×H)
  - Coupling type: inpainting (mask ξ) or super-resolution (downsample/upsample m(x₁))
  - t ~ U(0,1): randomly sampled time
- **Outputs**:
  - x₀: base sample (corrupted/masked version of x₁)
  - Iₜ = αₜ·x₀ + βₜ·x₁: interpolant at time t
  - İₜ = α̇ₜ·x₀ + β̇ₜ·x₁: time derivative of interpolant
- **Key design choices**:
  - **Inpainting**: αₜ = t, βₜ = 1-t → İₜ = x₁ - x₀; unmasked pixels have zero derivative.
  - **Super-resolution**: αₜ = 1-t, βₜ = t → İₜ = x₁ - x₀; corrupted starting point.
  - **No noise term**: γₜ = 0 in all experiments; interpolant is deterministic given (x₀, x₁, t).

### Component 2: Velocity Network (U-Net)

- **Purpose**: Approximate the velocity field bₜ(x, ξ) via neural network b̂ₜ parameterized by θ.
- **Architecture**: U-Net from Ho et al. (2020b) / luciddrains's `denoising-diffusion-pytorch`
- **Inputs**:
  - Iₜ: interpolant image (C×W×H) concatenated with conditioning channels
  - t: scalar time (embedded via learned sinusoidal positional encoding)
  - ξ: conditioning variable (appended as channels of Iₜ, plus class label embedding)
- **Outputs**:
  - b̂ₜ(Iₜ, ξ): predicted velocity field (C×W×H)
- **Architecture details**:
  - `dim` = 256
  - `dim_mults` = (1, 1, 2, 3, 4)
  - `resnet_block_groups` = 8
  - `learned_sinusoidal_cond` = True
  - `learned_sinusoidal_dim` = 32
  - `attn_dim_head` = 64
  - `attn_heads` = 4
  - `random_fourier_features` = False
- **Masking for inpainting**: The velocity output is multiplied by (1-ξ) so unmasked pixels receive zero update; model only acts on the first C=3 image channels, not the appended conditioning channels.

### Component 3: ODE/SDE Solver

- **Purpose**: At inference time, integrate $\dot{X}_t = \hat{b}_t(X_t, \xi)$ from t=0 to t=1 to produce a sample from ρ₁.
- **Inputs**:
  - x₀ ~ ρ₀(·|x₁): initial condition from data-dependent base
  - b̂ₜ: learned velocity network
  - Integration method: Dopri (Dormand-Prince adaptive solver from `torchdiffeq`)
- **Outputs**:
  - X_{t=1} ≈ x₁: generated sample
- **Key design choices**:
  - Forward Euler is described in Algorithm 2 for simplicity; Dopri is used in practice.
  - SDE variants (forward SDE eq. 11, backward SDE eq. 13) are theoretically supported but focus is on deterministic ODE.
  - For inpainting: initial condition is x₀ = ξ∘x₁_test + (1-ξ)∘ζ.
  - For super-resolution: initial condition is x₀ = U(D(x₁_test)) + σζ.

## Component Interaction Graph

```
Training:
  ImageNet x₁ ──→ [Interpolant Constructor] ──→ Iₜ, İₜ ──→ [Velocity Network] ──→ b̂ₜ
                                                                                        │
                                                                           [Loss: |b̂ₜ(Iₜ)|² - 2İₜ·b̂ₜ(Iₜ)]
                                                                                        │
                                                                              [Adam Optimizer] ──→ update θ

Inference:
  x₁_test (degraded) ──→ [Coupling: compute x₀] ──→ [ODE Solver (Dopri)] ──→ X_{t=1} (restored image)
                                                            │
                                                     [Velocity Network b̂ₜ]
```
