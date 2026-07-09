# Algorithm

## Mathematical Formulation

### Perturbed Policy
$$\bar\pi(a|s) = \tilde\pi(a^m=0|s)\cdot\pi(a|s) + \tilde\pi(a^m=1|s)\cdot\pi_r(a|s)$$

The final action at time t:
$$a_t \odot a^m_t = \begin{cases} a_t & \text{if } a^m_t = 0 \\ a_{\text{random}} & \text{if } a^m_t = 1 \end{cases}$$

### Optimized Mask Network Objective
Original StateMask: $J(\theta) = \min |\eta(\pi) - \eta(\bar\pi)|$

By Theorem 3.3 (under Assumption 3.1): $\eta(\bar\pi) \leq \eta(\pi)$, therefore:
$$J(\theta) = \max\, \eta(\bar\pi)$$

Modified reward to prevent trivial solution (always output 0):
$$R'(s_t, a_t) = R(s_t, a_t) + \alpha \cdot a^m_t$$

### Sub-Optimality Bound (Theorem 3.6)
$$V^{\pi^*}(\rho) - V^{\pi'}(\rho) \leq O\!\left(\frac{\varepsilon}{(1-\gamma)^2} \left\|\frac{d^{\pi^*}}{d^{\hat\pi}_\rho}\right\|_\infty\right)$$

where $\varepsilon$ satisfies $\mathbb{E}_{s \sim d^{\pi'}_\mu}\left[\max_a A^{\pi'}(s,a)\right] < \varepsilon$.

### Mixed Initial Distribution
$$\mu(s) = \beta \cdot d^{\hat\pi}_\rho(s) + (1-\beta)\rho(s)$$

In practice, parameterized via reset probability $p$ (probability of initializing from critical state).

### RND Exploration Reward
$$R'(s_t, a_t) = R(s_t, a_t) + \lambda \left|f(s_{t+1}) - \hat{f}(s_{t+1})\right|^2$$

## Pseudocode

### Algorithm 1: Training the Mask Network

```
Input:  Target agent's policy π
Output: Mask network ˜πθ

Initialize weights θ for mask net ˜πθ
θ_old ← θ
for iteration = 1, 2, ... do
    Set initial state s_0 ~ ρ
    D ← ∅
    for t = 0 to T do
        Sample a_t ~ π(a_t | s_t)
        Sample a^m_t ~ ˜πθ_old(a^m_t | s_t)
        Compute actual action: a ← a_t ⊙ a^m_t
        (s_{t+1}, R'_t) ← env.step(a)
          where R'_t = R(s_t, a_t) + α · a^m_t
        Record (s_t, s_{t+1}, a^m_t, R'_t) in D
    end for
    Update θ_old ← θ using D via PPO algorithm
end for
```

### Algorithm 2: Refining the DRL Agent

```
Input:  Pre-trained policy π, trained mask network ˜πθ,
        default initial distribution ρ, reset probability p
Output: Refined policy π'

for iteration = 1, 2, ... do
    D ← ∅
    RAND_NUM ← Uniform(0, 1)
    if RAND_NUM < p then
        Run π to obtain trajectory τ of length K
        Identify most critical state s_t in τ via ˜πθ
           (s_t = argmax_t P(a^m=0|s_t))
        Set initial state s_0 ← s_t
    else
        Set initial state s_0 ~ ρ
    end if
    for t = 0 to T do
        Sample a_t ~ π(a_t | s_t)
        (s_{t+1}, R_t) ← env.step(a_t)
        Compute RND bonus R^RND_t = |f(s_{t+1}) - f̂(s_{t+1})|²
           (with normalization)
        Add (s_t, s_{t+1}, a_t, R_t + λ · R^RND_t) to D
    end for
    Optimize πθ w.r.t. PPO loss on D
    Optimize f̂θ w.r.t. MSE loss on D using Adam
end for
π' ← πθ
```

## Key Theoretical Results

**Theorem 3.3** (η(π̄) ≤ η(π)): Under Assumption 3.1 (pre-trained policy better than random), the perturbed policy's expected reward is upper-bounded by that of the target policy. Proof via Performance Difference Lemma (Kakade & Langford, 2002).

**Lemma 3.5** (MaskNet sampling ≡ better policy): The importance-weighted sampling of states via the mask network is equivalent to sampling from a state occupancy distribution induced by an improved policy ˆπ with η(ˆπ) ≥ η(π). Proof via reweighting: $d^{\hat\pi}_\rho(s,a) = d^\pi_\rho(s,a) \cdot w(s,a)$ where $w(s,a) \propto Q^\pi(s,a)$.

**Claim 1** (Tighter bound with explanation): By Assumption 3.4, η(ˆπ) ≥ η(π) implies $\|d^{\pi^*}/d^{\hat\pi}_\rho\|_\infty \leq \|d^{\pi^*}/d^\pi_\rho\|_\infty$, thus the sub-optimality bound under RICE's mixed distribution is tighter than under random explanation.

## Complexity
- Mask network training: O(N·T) per iteration (N environments rollouts, T timesteps), same order as original policy training.
- Critical state identification: O(T) per trajectory (single forward pass through mask network).
- RICE refining: O(N·T) per iteration (standard PPO) + O(d_f) for RND target/predictor forward pass.
