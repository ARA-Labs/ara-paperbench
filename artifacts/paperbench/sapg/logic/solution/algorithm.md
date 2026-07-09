---
# Algorithm

## Mathematical Formulation

### Objective
Find a policy π*(a|s) maximizing J(π) = E_{s₀~ρ, aₜ~π(·|sₜ)}[Σₜ γᵗ r(sₜ, aₜ)]

### On-policy Loss (PPO Clipped Surrogate, Eq. 2)
$$L^{on}(\pi_\theta) = \mathbb{E}_{\pi_{old}}\left[\min\left(r_t(\pi_\theta), \text{clip}(r_t(\pi_\theta), 1-\epsilon, 1+\epsilon)\right) A^{\pi_{old}}\right]$$

where $r_t(\pi_\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{old}(a_t|s_t)}$

### Off-policy Loss (Eq. 3)
$$L^{off}(\pi_i; X) = \frac{1}{|X|}\sum_{j \in X} \mathbb{E}_{(s,a)\sim\pi_j}\left[\min\left(r_{\pi_i}(s,a), \text{clip}(r_{\pi_i}(s,a), \mu(1-\epsilon), \mu(1+\epsilon))\right) A^{\pi_{i,old}}(s,a)\right]$$

where $r_{\pi_i}(s,a) = \frac{\pi_i(s,a)}{\pi_j(s,a)}$ and $\mu = \frac{\pi_{i,old}(s,a)}{\pi_j(s,a)}$ (off-policy correction term)

**Note**: When i=j (on-policy case), $\mu = 1$ and Eq. 3 reduces to Eq. 2.

### Combined Actor Loss (Eq. 4)
$$L(\pi_i) = L^{on}(\pi_i) + \lambda \cdot L^{off}(\pi_i; X)$$

where λ=1 with 50/50 on/off-policy data subsampling for the leader.

### On-policy Critic Target — n-step Return (Eq. 5, n=3)
$$V^{target}_{on,\pi_j}(s_t) = \sum_{k=t}^{t+2} \gamma^{k-t} r_k + \gamma^3 V_{\pi_j,old}(s_{t+3})$$

### Off-policy Critic Target — 1-step Return (Eq. 6)
$$V^{target}_{off,\pi_j}(s'_t) = r_t + \gamma V_{\pi_j,old}(s'_{t+1})$$

### On-policy Critic Loss (Eq. 7)
$$L^{critic}_{on}(\pi_i) = \mathbb{E}_{(s,a)\sim\pi_i}\left[(V_{\pi_i}(s) - V^{target}_{on,\pi_i}(s))^2\right]$$

### Off-policy Critic Loss (Eq. 8)
$$L^{critic}_{off}(\pi_i; X) = \frac{1}{|X|}\sum_{j \in X} \mathbb{E}_{(s,a)\sim\pi_j}\left[(V_{\pi_i}(s) - V^{target}_{off,\pi_i}(s))^2\right]$$

### Combined Critic Loss (Eq. 9)
$$L^{critic}(\pi_i) = L^{critic}_{on}(\pi_i) + \lambda \cdot L^{critic}_{off}(\pi_i)$$

### Follower Loss with Entropy Regularization
$$L(\pi_i) = L^{on}(\pi_i) + \lambda_{ent}^{(i-1)} \cdot H(\pi_i(a|s)), \quad i \geq 2$$

where $H(\pi(a|s)) = -\mathbb{E}[\log \pi(a|s)]$ is the entropy of the action distribution.

## Pseudocode (Algorithm 1)

```
SAPG(M policies, N environments, η learning rate)

  Initialize shared actor backbone parameters θ
  Initialize shared critic backbone parameters ψ
  For i ∈ {1, ..., M}: initialize hanging parameters ϕᵢ
  Initialize N environments E₁, ..., E_N
  Initialize data buffers D₁, ..., D_M

  for iteration = 1, 2, ...:
    # Phase 1: Data Collection
    for j = 1, 2, ..., M:
      Dⱼ ← CollectData(E_{(j-1)·N/M : j·N/M}, θ, ψⱼ)
        # Roll out policy πⱼ (backbone θ + hanging params ϕⱼ)
        # for horizon_length = 16 steps in each of N/M environments

    # Phase 2: Leader Update
    L_total ← 0
    D' ← Subsample |D₁| transitions from ∪ⱼ₌₂ᴹ Dⱼ
      # importance weights: μ(s,a) = π₁,old(a|s) / πⱼ(a|s)
    L_total ← L_total + OffPolicyActorLoss(π₁, D')    # Eq. 3
    L_total ← L_total + OnPolicyActorLoss(π₁, D₁)     # Eq. 2
    L_total ← L_total + OffPolicyCriticLoss(π₁, D')   # Eq. 8
    L_total ← L_total + OnPolicyCriticLoss(π₁, D₁)    # Eq. 7

    # Phase 3: Follower Updates
    for j = 2, ..., M:
      L_total ← L_total + OnPolicyActorLoss(πⱼ, Dⱼ)   # Eq. 2
      L_total ← L_total + λent(j-1) · EntropyLoss(πⱼ) # follower entropy
      L_total ← L_total + OnPolicyCriticLoss(πⱼ, Dⱼ)  # Eq. 7

    # Phase 4: Parameter Updates (minibatch gradient descent)
    θ ← θ - η · ∇_θ L_total        # shared actor backbone
    ψ ← ψ - η · ∇_ψ L_total        # shared critic backbone
    for j = 1, ..., M:
      ϕⱼ ← ϕⱼ - η · ∇_{ϕⱼ} L_j    # per-policy hanging params
```

## Step-by-Step Explanation

1. **Data Collection**: Each of M=6 policies rolls out for 16 steps in its dedicated block of N/M = 4,096 environments simultaneously (on GPU).

2. **Importance Weight Computation**: For each follower transition (s, a) ~ πj, compute μ = π₁,old(a|s) / πj(a|s). This corrects for the distributional mismatch between the follower's data-collection policy and the leader's current update target.

3. **Off-policy Actor Loss**: Clips the importance-weighted ratio rπ₁ = π₁(a|s)/πj(a|s) around μ (not 1), maintaining the PPO trust-region flavor even for off-policy data.

4. **Off-policy Critic Loss**: Uses 1-step returns (not n-step) for off-policy transitions to avoid compounding bias from multi-step bootstrapping across a different policy's trajectory.

5. **Minibatch Updates**: All losses are optimized with minibatch gradient descent. Mini-batch size = num_envs × 4. Number of mini epochs not specified in paper.

## Complexity

- **Per iteration**: O(N × horizon_length) environment steps; O(M × N/M) = O(N) forward passes for data collection; O(N) for leader update (50/50 split); O(N) for follower updates.
- **Memory**: M sets of hanging parameters (small: M×32 or M×16 floats) + 1 shared backbone.
- **Communication**: Zero inter-process communication — all M policies share backbone via shared GPU memory.
