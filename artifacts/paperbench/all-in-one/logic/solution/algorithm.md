---
# Algorithm

## Mathematical Formulation

### Joint Distribution and Score
The Simformer targets the joint distribution $p(\hat{x}) = p(\theta, x)$ where $\hat{x} = (\theta, x) \in \mathbb{R}^d$. The score function at noise level $t$ is:

$$s(\hat{x}_t, t) = \nabla_{\hat{x}_t} \log p_t(\hat{x}_t)$$

### Variance Exploding SDE (VESDE)
$$f_\text{VESDE}(x, t) = 0, \quad g_\text{VESDE}(t) = \sigma_{\min} \cdot \left(\frac{\sigma_{\max}}{\sigma_{\min}}\right)^t \cdot \sqrt{2\log\frac{\sigma_{\max}}{\sigma_{\min}}}$$

Perturbation kernel: $p_t(x_t|x_0) = \mathcal{N}(x_t; x_0, \sigma(t)^2 I)$ where $\sigma(t)^2 = \sigma_{\min}^2 \left(\frac{\sigma_{\max}}{\sigma_{\min}}\right)^{2t}$

Parameters: $\sigma_{\max}=15$, $\sigma_{\min}=0.0001$, $t \in [10^{-5}, 1]$.

### Variance Preserving SDE (VPSDE)
$$f_\text{VPSDE}(x,t) = -\frac{1}{2}(\beta_{\min} + t(\beta_{\max}-\beta_{\min}))x, \quad g_\text{VPSDE}(t) = \sqrt{\beta_{\min} + t(\beta_{\max}-\beta_{\min})}$$

Parameters: $\beta_{\min}=0.01$, $\beta_{\max}=10$, $t \in [10^{-5}, 1]$.

### Training Loss (Denoising Score-Matching)
Given condition mask $M_C \in \{0,1\}^d$ and partially noisy sample $\hat{x}_t^{M_C} = (1-M_C)\cdot\hat{x}_t + M_C\cdot\hat{x}_0$:

$$\ell(\phi, M_C, t, \hat{x}_0, \hat{x}_t) = (1-M_C)\cdot\left(s_\phi^{M_E}(\hat{x}_t^{M_C}, t) - \nabla_{\hat{x}_t}\log p_t(\hat{x}_t|\hat{x}_0)\right)$$

$$\mathcal{L}(\phi) = \mathbb{E}_{M_C, t, \hat{x}_0, \hat{x}_t}\left[\|\ell(\phi, M_C, t, \hat{x}_0, \hat{x}_t)\|_2^2\right]$$

Loss is computed only over unobserved variables (where $M_C^{(i)}=0$).

### Reverse SDE (Euler-Maruyama Discretization)
At inference time, with step size $\Delta t = (T_{\max}-T_{\min})/T_{\text{steps}}$:
$$\hat{x}_{t_i} = \hat{x}_{t_{i+1}} - \left[f(\hat{x}_{t_{i+1}}, t_i) - g(t_i)^2 \cdot \tilde{s}\right]\Delta t - g(t_i)\sqrt{\Delta t}\cdot\epsilon, \quad \epsilon \sim \mathcal{N}(0,I)$$

Observed variables remain fixed: $\hat{x}_{t_i}^{(j)} = \hat{x}_0^{(j)}$ for all $j$ with $M_C^{(j)}=1$.

Default: 500 steps.

### Guided Diffusion Score Modification
For a constraint function $c(\hat{x}) \leq 0$ (e.g., $c(\hat{x}) = \hat{x} - u$ for upper bound $u$):
$$\tilde{s}(\hat{x}_t, t) = s_\phi(\hat{x}_t, t) + \nabla_{\hat{x}_t}\log\sigma\left(-s(t)\cdot c(\hat{x}_0^{\sim})\right)$$

where $\hat{x}_0^{\sim} = (\hat{x}_{t+1} + \sigma(t+1)^2 \cdot s_\phi(\hat{x}_{t+1}, t+1)) / \mu(t+1)$ is the denoised estimate, and $s(t) = 1/\sigma(t)^2$ for VESDE.

## Pseudocode

### Training Loop
```python
for epoch in range(num_epochs):
    theta, x = simulator.sample(batch_size)   # (B, d)
    x_hat = concatenate(theta, x)             # (B, d)
    
    # Sample condition mask
    M_C = sample_condition_mask(batch_size, d)  # one of 5 distributions
    
    # Sample noise level
    t = uniform(1e-5, 1.0, size=(B,))
    
    # Generate noisy sample (only for unobserved variables)
    x_noisy = add_noise(x_hat, t, sde)        # VESDE noise
    x_mixed = (1 - M_C) * x_noisy + M_C * x_hat   # keep observed clean
    
    # Compute attention mask (potentially updated for directed graph)
    M_E = compute_attention_mask(M_C, graph_type)
    
    # Score prediction
    score_pred = simformer(x_mixed, t, M_E)    # (B, d)
    score_target = compute_target_score(x_hat, x_noisy, t, sde)
    
    # Loss on unobserved variables only
    loss = mean(((1 - M_C) * (score_pred - score_target))**2)
    optimizer.step(loss)
```

### Sampling (Reverse SDE)
```python
def sample_conditional(simformer, x_obs, M_C, sde, n_steps=500):
    # Initialize unobserved variables from terminal noise
    x = sample_terminal_noise(d)                  # N(mu_T, sigma_T)
    x[M_C == 1] = x_obs[M_C == 1]               # set observed values
    
    t_schedule = linspace(T_max, T_min, n_steps)
    
    for t_curr, t_next in zip(t_schedule[:-1], t_schedule[1:]):
        dt = t_next - t_curr
        eps = randn_like(x)
        score = simformer(x, t_curr, M_E)         # score estimate
        
        # Euler-Maruyama reverse step (VESDE: f=0)
        x_unobs = x[M_C == 0]
        x_unobs = x_unobs + sde.g(t_curr)**2 * score[M_C==0] * abs(dt) \
                  + sde.g(t_curr) * sqrt(abs(dt)) * eps[M_C==0]
        x[M_C == 0] = x_unobs
        x[M_C == 1] = x_obs[M_C == 1]            # keep observed fixed
    
    return x
```

### General Guidance (Algorithm 1)
```python
def guided_sample(simformer, x_obs, M_C, c_fn, s_fn, sde, n_steps=500, r=0):
    x = sample_terminal_noise(d)
    x[M_C == 1] = x_obs[M_C == 1]
    
    t_schedule = linspace(T_max, T_min, n_steps)
    
    for t_curr, t_next in zip(t_schedule[:-1], t_schedule[1:]):
        dt = t_next - t_curr
        for _ in range(r + 1):
            eps = randn_like(x)
            s = simformer(x, t_curr, M_E)
            
            # Denoised estimate
            x0_tilde = (x + sde.sigma(t_curr)**2 * s) / sde.mu(t_curr)
            
            # Constraint guidance score
            s_guide = grad(lambda xh: log(sigmoid(-s_fn(t_curr) * c_fn(xh))))(x0_tilde)
            s_total = s + s_guide
            
            # Euler-Maruyama step
            x[M_C==0] += sde.g(t_curr)**2 * s_total[M_C==0] * abs(dt) \
                        + sde.g(t_curr) * sqrt(abs(dt)) * eps[M_C==0]
            x[M_C==1] = x_obs[M_C==1]
            
            if r > 0:  # self-recurrence: re-noise
                eps2 = randn_like(x)
                x[M_C==0] += sde.f(x, t_curr)[M_C==0]*dt + sde.g(t_curr)*sqrt(abs(dt))*eps2[M_C==0]
    
    return x
```

## Complexity Analysis
- **Training**: O(d² · L · B) per step, where d = number of variables (tokens), L = number of transformer layers, B = batch size. Quadratic in sequence length (standard transformer attention).
- **Sampling**: O(d² · L · T_steps) per sample, where T_steps = 500 default.
- **Memory**: Quadratic in d due to attention matrix; sparse attention masks reduce complexity for structured simulators.
- **Simulation budget**: ~10× fewer simulations needed vs NPE to achieve comparable posterior C2ST on benchmark tasks.
