# Algorithm

## Mathematical Formulation

### Forward SDE (Noising Process)
$$d\theta_t = f(\theta_t, t)\,dt + g(t)\,dw_t, \quad \theta_0 \sim p(\cdot|x)$$

### Reverse-Time SDE
$$d\bar{\theta}_t = \left[-f(\bar{\theta}_t, T-t) + g^2(T-t)\nabla_\theta \log p_{T-t}(\bar{\theta}_t|x)\right]dt + g(T-t)\,dw_t$$

### Probability Flow ODE
$$\frac{d\theta_t}{dt} = f(\theta_t, t) - \frac{1}{2}g^2(t)\nabla_\theta \log p_t(\theta_t|x)$$

### Denoising Score Matching (DSM) Objective
$$J^{\text{DSM}}_{\text{post}}(\psi) = \int_0^T \lambda_t\, \mathbb{E}_{p_{t|0}(\theta_t|\theta_0)\,p(x|\theta_0)\,p(\theta_0)}\!\left[\|s_\psi(\theta_t,x,t) - \nabla_{\theta_t}\log p_{t|0}(\theta_t|\theta_0)\|^2\right]dt$$

This objective is minimised when $s_\psi(\theta_t, x, t) = \nabla_\theta \log p_t(\theta_t|x)$ almost everywhere.

### TSNPSE Loss (r-th round)
$$J^{\text{TSNPSE-DSM}}_{\text{post}}(\psi) = \int_0^T \lambda_t\, \mathbb{E}_{p_{t|0}(\theta_t|\theta_0)\,p(x|\theta_0)\,\tilde{p}^r(\theta_0)}\!\left[\|s_\psi(\theta_t,x,t) - \nabla_{\theta_t}\log p_{t|0}(\theta_t|\theta_0)\|^2\right]dt$$

where $\tilde{p}^r(\theta) = \frac{1}{r}\sum_{s=0}^{r-1}\bar{p}^s(\theta)$ and $\bar{p}^r(\theta) \propto p(\theta)\cdot\mathbf{1}\{\theta \in \mathrm{HPR}_\varepsilon(p^{r-1}_\psi(\theta|x_\text{obs}))\}$.

## NPSE Pseudocode

```
Algorithm: NPSE
Input: prior p(θ), simulator p(x|θ), budget N, observation x_obs, SDE type
Output: sampler for p_ψ(θ|x_obs)

1. Sample {θ_i, x_i}_{i=1}^N ~ p(θ)p(x|θ)
2. Standardise θ and x using empirical mean and std
3. Train s_ψ(θ_t, x, t) by minimising MC estimate of J^DSM_post(ψ)
   - Adam optimiser, lr=1e-4
   - Batch size: 50 (N≤10k) or 500 (N=100k)
   - Max 3000 iterations; early stopping patience=1000 on 15% val split
4. Sample θ_0^{(j)} ~ N(0,I) for j=1,...,M
5. Solve time-reversal of probability flow ODE (RK45) with score = s_ψ(·, x_obs, ·)
6. Return samples {θ_T^{(j)}} ~ p_ψ(θ|x_obs)
```

## TSNPSE Pseudocode (Algorithm 1)

```
Algorithm: TSNPSE
Input: x_obs, prior p(θ) =: p̄^0(θ), simulator p(x|θ), budget N, rounds R
       (M = N/R simulations per round), dataset D = {}
Output: p_ψ(θ|x_obs) ≈ p(θ|x_obs)

For r = 1,...,R do:
  For i = 1,...,M do:
    Draw θ_i ~ p̄^{r-1}(θ), x_i ~ p(x|θ_i)
    Add (θ_i, x_i) to D
  End for
  
  Train s_ψ(θ_t, x, t) ≈ ∇_θ log p_t(θ_t|x) by minimising MC estimate of
  J^TSNPSE-DSM_post(ψ) on dataset D
  
  Compute p̄^r(θ) [HPR estimation]:
    1. Draw 20000 samples from p_ψ(·|x_obs) via ODE (RK45)
    2. Evaluate log-densities via instantaneous change-of-variables (Eq. 5)
    3. Compute κ = ε-th quantile of log-densities (ε = 5×10⁻⁴)
    4. p̄^r(θ) ∝ p(θ) · I{log p_ψ(θ|x_obs) ≥ κ}
End for

Return: p_ψ(θ|x_obs) sampler via time-reversal of probability flow ODE
```

## Truncated Proposal Sampling (Rejection Sampling)

```
To sample θ ~ ˜p^r(θ):
Repeat until M samples accepted:
  1. Sample θ ~ p(θ)
  2. [Cheap pre-rejection] Reject if θ not within empirical hypercube
     of 20000 posterior samples (per-dimension [min, max])
  3. [Expensive step] Compute log p_ψ(θ|x_obs) via ODE + change-of-variables
  4. Accept if log p_ψ(θ|x_obs) ≥ κ, else reject
```

## VE SDE Specifics

$$g(t) = \sigma_{\min}\left(\frac{\sigma_{\max}}{\sigma_{\min}}\right)^t\sqrt{2\log\frac{\sigma_{\max}}{\sigma_{\min}}}, \quad f(\theta_t,t)=0$$

$$p_{t|0}(\theta_t|\theta_0) = \mathcal{N}\!\left(\theta_0,\; \sigma^2_{\min}\left(\frac{\sigma_{\max}}{\sigma_{\min}}\right)^{2t}\!I\right)$$

$$\nabla_{\theta_t}\log p_{t|0}(\theta_t|\theta_0) = -\frac{\theta_t - \theta_0}{\sigma^2_{\min}(\sigma_{\max}/\sigma_{\min})^{2t}}$$

## VP SDE Specifics

$$f(\theta_t,t) = -\tfrac{1}{2}\beta_t\theta_t, \quad g(t)=\sqrt{\beta_t}, \quad \beta_t = \beta_{\min}+t(\beta_{\max}-\beta_{\min})$$

Let $\alpha_t = \exp\!\left(-\frac{1}{2}\int_0^t\beta_s\,ds\right) = \exp\!\left(-\frac{t}{2}\left(\beta_{\min} + \frac{t(\beta_{\max}-\beta_{\min})}{2}\right)\right)$. Then:

$$p_{t|0}(\theta_t|\theta_0) = \mathcal{N}(\alpha_t\theta_0,\; (1-\alpha_t^2)I)$$

$$\nabla_{\theta_t}\log p_{t|0}(\theta_t|\theta_0) = -\frac{\theta_t - \alpha_t\theta_0}{1-\alpha_t^2}$$

## Error Bounds (Theorem A.3)

Under assumptions A1'/B1, A2, A3, A4, the Wasserstein-2 distance between the approximate and true posterior satisfies:
- VP ODE: $W_2(\hat{\pi}_1, \tilde{\pi}_1) \leq \varepsilon_1 \cdot C_{\text{VP}}$
- VE ODE: $W_2(\hat{\pi}_1, \tilde{\pi}_1) \leq \varepsilon_1 \cdot C_{\text{VE}}$

where $\varepsilon_1 \propto \varepsilon_{\text{obs}}$ (L2 score approximation error) and constants depend on the Lipschitz properties of the velocity field.

## Complexity

- **Training**: O(N · T_iter) forward passes per round, where T_iter = min(3000, early_stop).
- **HPR estimation**: O(20000) ODE solves + Jacobian traces per round (expensive; each requiring multiple network forward passes + gradient computations).
- **Sampling**: O(M) ODE solves using RK45 (number of steps determined by solver tolerance).
- **Density evaluation**: O(1) ODE solve + augmented trace ODE; significantly more expensive than a single normalising flow forward pass.
