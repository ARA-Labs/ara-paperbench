---
# Algorithm: TAN Training (Algorithm 1)

## Mathematical Formulation

### Forward Diffusion Process
$$q(x_t|x_0) = \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t}x_0, (1-\bar{\alpha}_t)I)$$
$$x_t = \sqrt{\bar{\alpha}_t}x_0 + \sqrt{1-\bar{\alpha}_t}\epsilon, \quad \epsilon \sim \mathcal{N}(0, I)$$

where $\alpha_t := 1-\beta_t$, $\bar{\alpha}_t := \prod_{i=0}^{t}(1-\beta_i)$.

### Standard DDPM Loss
$$\mathcal{L}_{sample}(\theta) := \mathbb{E}_{t,x_0,\epsilon}\|\epsilon - \epsilon_\theta(x_t, t)\|^2 \quad \text{(Eq. 1)}$$

### Domain Distance (KL Divergence)
$$D_{KL}(p_{\theta_S,\phi}(x_{t-1}^S|x_t),\, p_{\theta_T,\phi}(x_{t-1}^T|x_t)) = \mathbb{E}_{t,x_0,\epsilon}\left[C_1\|\nabla_{x_t}\log p_\phi(y=S|x_t) - \nabla_{x_t}\log p_\phi(y=T|x_t)\|^2\right] \quad \text{(Eq. 5)}$$

where $C_1 = \gamma/2$ is a constant.

### Similarity-Guided Loss (without adversarial noise)
$$\min_\psi\, \mathbb{E}_{t,x_0,\epsilon}\left\|\epsilon_t - \epsilon_{\theta,\psi}(x_t, t) - \hat{\sigma}_t^2\gamma\nabla_{x_t}\log p_\phi(y=T|x_t)\right\|^2 \quad \text{(Eq. 6)}$$

where $\hat{\sigma}_t = (1-\bar{\alpha}_{t-1})\sqrt{\frac{1}{1-\bar{\alpha}_t}}$.

### Min-Max Objective (Full TAN)
$$\min_\psi\max_\epsilon\, \mathbb{E}_{t,x_0}\left\|\epsilon - \epsilon_\theta(x_t, t) - \sigma_t^2\gamma\nabla_{x_t}\log p_\phi(y=T|x_t)\right\|^2 \quad \text{(Eq. 7)}$$

### Inner Maximization — PGD Adversarial Noise
$$\epsilon^{j+1} = \text{Norm}\left(\epsilon^j + \omega\nabla_{\epsilon^j}\left\|\epsilon^j - \epsilon_\theta\!\left(\sqrt{\bar{\alpha}_t}x_0 + \sqrt{1-\bar{\alpha}_t}\epsilon^j,\, t\right)\right\|^2\right), \quad j=0,\ldots,J-1 \quad \text{(Eq. 8)}$$

where $\text{Norm}(\cdot)$ normalizes to maintain $\epsilon^{j+1}_{mean}=0$, $\epsilon^{j+1}_{std}=I$.

### Full Outer Objective
$$\mathcal{L}(\psi) \equiv \mathbb{E}_{t,x_0}\left\|\epsilon^* - \epsilon_{\theta,\psi}(x_t^*, t) - \hat{\sigma}_t^2\gamma\nabla_{x_t^*}\log p_\phi(y=T|x_t^*)\right\|^2 \quad \text{(Eq. 9)}$$

subject to:
$$\epsilon^* = \arg\max_\epsilon \left\|\epsilon - \epsilon_\theta\!\left(\sqrt{\bar{\alpha}_t}x_0 + \sqrt{1-\bar{\alpha}_t}\epsilon,\, t\right)\right\|^2, \quad \epsilon^*_{mean}=0,\; \epsilon^*_{std}=I \quad \text{(Eq. 10)}$$

where $x_t^* = \sqrt{\bar{\alpha}_t}x_0 + \sqrt{1-\bar{\alpha}_t}\epsilon^*$.

### Adaptor Layer Formulation
$$x_t^l = \theta_l(x^{l-1}) + \psi_l(x^{l-1})$$
$$\psi_l(x^{l-1}) = f(x^{l-1}W_{down})W_{up}$$

## Pseudocode

```
Algorithm 1: Training DPMs with TAN
Require: binary classifier pϕ, pre-trained DPMs εθ, learning rate η
         hyperparameters: γ (similarity guidance), J (PGD steps), ω (PGD step size)
         adaptor parameters ψ initialized to 0

1: repeat
2:   x0 ~ q(x0)                           # sample from 10-shot target dataset
3:   t ~ Uniform({1, ..., T})              # random timestep
4:   ε ~ N(0, I)                           # initial noise ε0
5:
6:   # === INNER MAXIMIZATION (PGD) ===
7:   for j = 0, ..., J-1 do
8:     xt_j = sqrt(ᾱt)*x0 + sqrt(1-ᾱt)*εj
9:     grad_ε = ∇εj ||εj - εθ(xt_j, t)||²   # gradient of loss w.r.t. noise
10:    εj+1 = Norm(εj + ω * grad_ε)          # gradient ascent + normalize
11:  end for
12:  ε* = εJ                                 # worst-case noise
13:
14:  # === OUTER MINIMIZATION ===
15:  x*t = sqrt(ᾱt)*x0 + sqrt(1-ᾱt)*ε*
16:  sim_grad = ∇x*t log pϕ(y=T | x*t)      # classifier gradient (frozen pϕ)
17:  correction = σ̂²t * γ * sim_grad
18:  target_noise = ε* - correction
19:  predicted_noise = εθ,ψ(x*t, t)          # forward pass through frozen θ + trainable ψ
20:  L(ψ) = ||target_noise - predicted_noise||²
21:
22:  # === UPDATE ===
23:  ψ = ψ - η * ∇ψ L(ψ)                    # only adaptor parameters updated
24:
25: until converged (300 iterations)
```

## Step-by-Step Explanation

1. **Sample** a target image x0, timestep t, and initial noise ε0 ~ N(0,I).
2. **Inner PGD loop (lines 7-11)**: Perform J=10 gradient ascent steps to find the worst-case noise — the noise that maximizes the model's denoising loss. Each step: compute gradient of ||ε - εθ(xt,t)||² with respect to ε, update ε in gradient ascent direction with step size ω=0.02, normalize to preserve Gaussian statistics.
3. **Compute worst-case noised image** x*t = √ᾱt·x0 + √(1-ᾱt)·ε*.
4. **Compute similarity gradient**: Query frozen binary classifier for pϕ(y=T|x*t); compute gradient of log probability w.r.t. x*t.
5. **Compute corrected target**: Subtract similarity correction from ε* to get the adjusted noise prediction target.
6. **Forward pass**: Run augmented model εθ,ψ(x*t, t) = εθ(x*t, t) + εψ(x*t, t).
7. **Compute loss**: Squared L2 distance between corrected target and predicted noise.
8. **Backprop through ψ only**: Gradient flows to adaptor parameters; pre-trained θ is frozen.

## Complexity Analysis
- **Per-iteration cost**: O(J × forward_pass) for inner PGD + O(1 × forward_pass) for outer step
- **Parameter cost**: Adaptor modules add ~1.3% (DDPM) / ~1.6% (LDM) of original parameter count
- **Total iterations**: ~300 (vs. ~5000 for full fine-tuning methods)
- **Wall-clock**: 3 GPU hours (DDPM-TAN, ×8 A100) vs. 7.5 GPU hours (baseline, 5000 iter)
- **Memory**: 9 GB (TAN) vs. 20 GB (baseline direct fine-tuning)
