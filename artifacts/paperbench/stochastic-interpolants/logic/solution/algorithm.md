# Algorithm

## Mathematical Formulation

### Stochastic Interpolant (with coupling)
$$I_t = \alpha_t x_0 + \beta_t x_1 + \gamma_t z, \quad t \in [0,1]$$

where:
- $(x_0, x_1) \sim \rho(x_0, x_1) = \rho_1(x_1)\rho_0(x_0|x_1)$ (data-dependent coupling)
- $z \sim \mathcal{N}(0, I_d)$, independent of $(x_0, x_1)$
- Boundary conditions: $\alpha_0 = \beta_1 = 1$, $\alpha_1 = \beta_0 = \gamma_0 = \gamma_1 = 0$

### Data-Dependent Base Construction
$$x_0 = m(x_1) + \sigma\zeta, \quad \zeta \sim \mathcal{N}(0, I_d)$$

**Inpainting**: $x_0 = \xi \circ x_1 + (1 - \xi) \circ \zeta$, $\alpha_t = t$, $\beta_t = 1-t$

**Super-resolution**: $x_0 = \mathcal{U}(\mathcal{D}(x_1)) + \sigma\zeta$, $\alpha_t = 1-t$, $\beta_t = t$

### Velocity Regression Objective (Eq. 22)
$$\hat{\mathcal{L}}_b(\hat{b}) = \frac{1}{n_b} \sum_{i=1}^{n_b} \left[ |\hat{b}_{t_i}(I_{t_i})|^2 - 2\dot{I}_{t_i} \cdot \hat{b}_{t_i}(I_{t_i}) \right]$$

where $\dot{I}_t = \dot{\alpha}_t x_0 + \dot{\beta}_t x_1$ (for $\gamma_t=0$).

### Score Identity (Eq. 6)
$$\nabla \log \rho_t(x) = -\gamma_t^{-1} g_t(x), \quad g_t(x) = \mathbb{E}[z | I_t = x]$$

### Transport Cost Bound (Proposition 3.1)
$$\mathbb{E}_{x_0 \sim \rho_0}\left[|X_{t=1}(x_0) - x_0|^2\right] \leq \int_0^1 \mathbb{E}[|\dot{I}_t|^2]dt$$

For super-resolution coupling: $\mathbb{E}[|\dot{I}_t|^2] = \mathbb{E}[|x_1 - x_0|^2] = d\sigma^2$

## Pseudocode

### Algorithm 1: Training

```
Input: Interpolant coefficients αₜ, βₜ; velocity model b̂; batch size nᵦ
repeat:
    for i = 1, ..., nᵦ do:
        Draw x₁ᵢ ~ ρ₁(x₁)
        Draw ζⁱ ~ N(0, Id)
        Draw tᵢ ~ U(0, 1)
        Compute x₀ᵢ = m(x₁ᵢ) + σζⁱ      # task-specific: inpainting or super-res
        Compute Iₜᵢ = αₜᵢ·x₀ᵢ + βₜᵢ·x₁ᵢ
        Compute İₜᵢ = α̇ₜᵢ·x₀ᵢ + β̇ₜᵢ·x₁ᵢ  # = x₁-x₀ for both tasks
    end for
    Compute empirical loss:
        L̂ᵦ(b̂) = nᵦ⁻¹ Σᵢ [|b̂ₜᵢ(Iₜᵢ)|² - 2İₜᵢ · b̂ₜᵢ(Iₜᵢ)]
    Take gradient step (Adam) on L̂ᵦ(b̂) to update b̂
until converged
return b̂
```

### Algorithm 2: Sampling (Forward Euler)

```
Input: model b̂, corrupted sample x₀ = m(x₁_test) + σζ, N ∈ ℕ
Draw ζ ~ N(0, Id)
Initialize X̂₀ = m(x₁_test) + σζ
for n = 0, ..., N-1 do:
    X̂ₙ₊₁ = X̂ₙ + N⁻¹ · b̂ₙ/ₙ(X̂ₙ)
end for
return X̂_N  # clean sample
```

### Sampling (Dopri Adaptive Solver, used in practice)

```
Input: model b̂, initial condition X₀ = x₀ ~ ρ₀(·|x₁_test)
Solve: dXₜ/dt = b̂ₜ(Xₜ, ξ), X₀ given
using Dormand-Prince (Dopri) adaptive ODE solver from torchdiffeq
return X₁
```

## Complexity Analysis

- **Training**: O(nᵦ × U-Net forward/backward pass) per step. U-Net cost depends on image resolution and architecture depth.
- **Sampling (Forward Euler)**: O(N × U-Net forward pass). N function evaluations.
- **Sampling (Dopri)**: Adaptive; number of function evaluations depends on tolerance and trajectory smoothness. Dependent coupling typically requires fewer evaluations due to simpler trajectories.
- **Memory**: Batch of images at training resolution (256×256 or 512×512) × C × batch_size.
