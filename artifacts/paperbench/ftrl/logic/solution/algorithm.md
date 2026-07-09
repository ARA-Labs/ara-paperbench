# Algorithm: Knowledge Retention for RL Fine-tuning

## Mathematical Formulation

### Total Training Objective
$$\mathcal{L}(\theta) = \mathcal{L}_{RL}(\theta) + \lambda \cdot \mathcal{L}_{retention}(\theta)$$

where $\mathcal{L}_{RL}$ is the base RL loss (APPO/PPO/SAC objective) and $\mathcal{L}_{retention}$ is one of four knowledge retention losses.

### EWC Auxiliary Loss
$$\mathcal{L}_{EWC}(\theta) = \sum_i F^i (\theta^{*i} - \theta^i)^2$$

where:
- $\theta^*$ = pre-trained weights (frozen)
- $\theta$ = current weights
- $F^i$ = $i$-th diagonal element of Fisher Information Matrix
- $F_{ii} = \mathbb{E}\left[\left(\frac{\partial \ell}{\partial \theta_i}\right)^2\right]$

**NetHack**: $\lambda = 2 \times 10^6$, F estimated over 10,000 batches from NLD-AA  
**RoboticSequence**: $\lambda = 100$ (actor), $\lambda = 0$ (critic)

### Behavioral Cloning (BC) Auxiliary Loss
$$\mathcal{L}_{BC}(\theta) = \mathbb{E}_{s \sim \mathcal{B}_{BC}}\left[D_{KL}(\pi^*(s) \| \pi_\theta(s))\right]$$

$$\mathcal{B}_{BC} = \{(s, \pi^*(s)) : s \in \mathcal{S}_{BC}\}$$

**NetHack**: $\lambda_{BC} = 2.0$, no decay; states from NLD-AA (8000 Human Monk games)  
**RoboticSequence**: actor_coeff = 1, critic_coeff = 0  
**Montezuma**: KL weight coefficient tuned (see Figure 13)

### Kickstarting (KS) Auxiliary Loss
$$\mathcal{L}_{KS}(\theta) = \mathbb{E}_{s \sim \mathcal{B}_\theta}\left[D_{KL}(\pi^*(s) \| \pi_\theta(s))\right]$$

where $\mathcal{B}_\theta$ is the buffer of states gathered by the **current online policy** $\pi_\theta$.

**NetHack**: $\lambda_{KS} = 0.5 \cdot (0.99998)^t$ where $t$ is the training step

### Episodic Memory (EM)
$$\mathcal{B}_{replay} = \mathcal{B}_{online} \cup \mathcal{B}_{EM}$$
$$|\mathcal{B}_{EM}| = 0.1 \times |\mathcal{B}_{replay}| = 10,000 \text{ samples}$$

Samples from $\mathcal{B}_{EM}$ are protected (not overwritten during fine-tuning). SAC trains on mini-batches sampled from the combined buffer.

### RoboticSequence Augmented Reward
$$r'_t = \beta \cdot r_t \cdot (T - t), \quad \beta = 1.5, \quad T = 200$$

Applied only when the episode ends with success; encourages early task completion.

## Pseudocode

```
Algorithm: Knowledge-Retention RL Fine-tuning

Input: pre-trained policy π* (weights θ*), RL environment E,
       retention method M ∈ {EWC, BC, KS, EM},
       replay buffer B_BC from pre-training

# Preprocessing (NetHack only)
if environment == NetHack:
    freeze all parameters except critic head
    train critic head for 500M steps
    unfreeze all parameters except encoders

# Compute Fisher matrix (if M == EWC)
if M == EWC:
    F = compute_fisher(π*, training_data)
    F = clip(F, min=1e-5)  # RoboticSequence only

# Initialize fine-tuned policy
θ ← θ*

# Fine-tuning loop
for each training step t:
    # Collect experience with current policy πθ
    trajectories ← rollout(πθ, E)
    
    # Compute base RL loss
    L_RL ← compute_rl_loss(trajectories)  # PPO/APPO/SAC loss
    
    # Compute retention loss
    if M == EWC:
        L_ret ← Σᵢ Fᵢ(θ*ᵢ - θᵢ)²
    elif M == BC:
        batch ← sample(B_BC)
        L_ret ← E_{(s,a*)∈batch}[KL(π*(s) ‖ πθ(s))]
        λ = λ_BC  # fixed coefficient (2.0 for NetHack, no decay)
    elif M == KS:
        λ_t = λ_KS * 0.99998^t  # exponential decay (NetHack)
        L_ret ← E_{s∈trajectories}[KL(π*(s) ‖ πθ(s))]
    elif M == EM:
        # EM is implicit: B_replay contains B_EM (protected)
        L_ret ← 0  # no explicit aux loss; handled by replay buffer
    
    # Total loss (actor only for L_ret)
    L_total ← L_RL + λ · L_ret
    
    # Update parameters (actor + critic for L_RL; actor only for L_ret)
    θ ← θ - α · ∇_θ L_total

return πθ
```

## Complexity Analysis

- **EWC**: O(|θ|) extra memory for Fisher diagonal and θ*; O(|θ|) extra computation per step for regularization term
- **BC**: O(|B_BC|) extra memory; O(|batch|) extra forward passes per step through frozen π*
- **KS**: Same as BC but uses online data; no extra memory for buffer
- **EM**: O(|B_EM|) extra memory (10K samples ≈ 10% of replay buffer); no extra computation
- **Training time (NetHack)**: >500M environment steps per 24 hours on A100 GPU

## RoboticSequence Algorithm (Sequential Task)

```
Algorithm 1 (RoboticSequence):
Input: list of N environments E_k, policy π, time limit T
Returns: number of solved environments

i = 1; t = 1  {initialize env index, timestep counter}
while i ≤ N and t ≤ T do:
    take step in E_i using π
    if E_i is solved:
        i = i + 1; t = 1  {move to next env, reset timestep}
return i - 1
```
