# Algorithm

## Mathematical Formulation

### Information Bottleneck Objective

Given reward function lookup table $L_\eta := \{(s^e, \eta(s^e)) : s^e \in \mathcal{D}\}$ and random variables $L^e_\eta$ (encoder context, $K$ samples), $L^d_\eta$ (decoder target, $K'$ samples), and latent $Z$:

$$\max I(L^d_\eta; Z) - \beta I(L^e_\eta; Z) \tag{2}$$

### Variational Lower Bound (Training Objective)

$$\mathcal{L}_\text{FRE} = \mathbb{E}_{\eta, L^e_\eta, L^d_\eta, z \sim p_\theta(z|L^e_\eta)}\!\left[\sum_{k=1}^{K'} \log q_\theta(\eta(s^d_k) \mid s^d_k, z) - \beta \, D_\text{KL}(p_\theta(z \mid L^e_\eta) \,\|\, \mathcal{N}(0, I))\right] \tag{6}$$

Implemented as:
$$\mathcal{L}_\text{FRE} = -\text{MSE}(\hat{r}, r) - \beta \, D_\text{KL}(\mathcal{N}(\mu_\theta, \sigma_\theta) \| \mathcal{N}(0, I))$$

### Bellman Update (IQL)

$$Q(s, a, z) \leftarrow \eta(s) + \gamma \cdot \text{mask} \cdot \mathbb{E}_{s' \sim p(s'|s,a)}[V(s', z)] \tag{9}$$

### Value Update (Expectile Regression)
$$\mathcal{L}_V = \mathbb{E}_{(s,a) \sim \mathcal{D}}[L_\tau^\text{exp}(Q_{\bar\theta}(s,a,z) - V_\phi(s,z))]$$

where $L_\tau^\text{exp}(u) = |\tau - \mathbf{1}[u < 0]| u^2$ with $\tau=0.8$.

### Actor Update (AWR)
$$\mathcal{L}_\pi = -\mathbb{E}_{(s,a) \sim \mathcal{D}}\!\left[\exp\!\left(\frac{Q_{\bar\theta}(s,a,z) - V_\phi(s,z)}{\beta_\text{AWR}}\right) \log \pi_\psi(a \mid s, z)\right]$$

with $\beta_\text{AWR}=3.0$.

## Pseudocode

```
Algorithm 1: Functional Reward Encodings (FRE)

Input: offline dataset D, prior p(eta)

# === Phase 1: Train encoder-decoder ===
while not converged:
    eta ~ p(eta)                            # sample reward function
    {s^e_k} ~ D (K samples)                # encoder context states
    {s^d_k} ~ D (K' samples)               # decoder target states (disjoint)
    # label states
    r^e_k = eta(s^e_k) for k=1..K
    r^d_k = eta(s^d_k) for k=1..K'
    # discretize encoder rewards and embed
    tokens = concat(linear(s^e_k), reward_emb(discretize(r^e_k)))
    # encode via permutation-invariant transformer
    h = MeanPool(Transformer(tokens))
    mu, log_sigma = linear_heads(h)
    z ~ N(mu, exp(log_sigma))
    # decode and compute loss
    r_hat_k = Decoder(s^d_k, z)
    L = MSE(r_hat_k, r^d_k) + beta * KL(N(mu, sigma) || N(0,I))
    update encoder and decoder parameters

# === Phase 2: Train policy (encoder frozen) ===
freeze encoder
while not converged:
    eta ~ p(eta)
    {s^e_k} ~ D (K samples)
    z ~ p_theta(z | {s^e_k, eta(s^e_k)})   # frozen encoder
    (s, a, s') ~ D                          # sample transitions
    r = eta(s)                              # label reward
    # IQL updates (all networks conditioned on z)
    update Q(s,a,z) via Bellman backup
    update V(s,z) via expectile regression (tau=0.8)
    update target_Q via soft update (rate=0.001)
    update pi(a|s,z) via AWR (temperature=3.0)
```

## Complexity Analysis
- **Encoder forward pass**: O(K² · d) for self-attention over K tokens of dim d
- **Decoder forward pass**: O(d²) for 3-layer MLP
- **Policy forward pass**: O(d²) for 3-layer MLP; same for Q and V
- **Memory**: Linear in batch size; K encoder tokens held in memory per training step

## Reward Discretization Detail
```
def discretize_reward(r, n_bins=32):
    r_norm = (r + 1.0) / 2.0          # shift to [0, 1]
    r_clipped = clip(r_norm, 0, 1)
    bin_idx = floor(r_clipped * n_bins)  # integer in {0,...,31}
    return min(bin_idx, n_bins - 1)
```
