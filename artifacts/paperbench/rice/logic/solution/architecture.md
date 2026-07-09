# System Architecture

## Overview

RICE consists of two sequential phases operating on a pre-trained DRL policy π:
1. **Explanation Phase**: Train a mask network (Optimized StateMask) to identify critical states.
2. **Refining Phase**: Use critical states + default states as mixed initial distribution; refine policy with PPO + RND.

## Component Graph

```
Pre-trained Policy π
       │
       ▼
┌─────────────────────────────────────────┐
│  PHASE 1: Mask Network Training          │
│                                         │
│  [Mask Network ˜πθ]                     │
│    Input:  state s_t ∈ ℝ^d_s            │
│    Output: binary action a^m_t ∈ {0,1}  │
│    Same arch as target policy network   │
│                                         │
│  [Perturbed Policy π̄]                   │
│    a_t = at ⊙ a^m_t                     │
│    (a^m=0 → keep at; a^m=1 → random)   │
│                                         │
│  [Modified Reward]                      │
│    R′(s,a) = R(s,a) + α·a^m_t          │
│                                         │
│  [PPO Optimizer for ˜πθ]               │
│    Objective: J(θ) = max η(π̄)          │
└─────────────────────────────────────────┘
       │
       │  trained mask network ˜πθ
       ▼
┌─────────────────────────────────────────┐
│  PHASE 2: RICE Refining                  │
│                                         │
│  [Critical State Identifier]            │
│    Run π to get trajectory τ            │
│    Apply ˜πθ → importance scores        │
│    Select s* = argmax P(a^m=0|s_t)      │
│                                         │
│  [Mixed Initial Distribution Sampler]   │
│    With prob p: s0 ← s* (critical)      │
│    With prob (1-p): s0 ~ ρ (default)   │
│                                         │
│  [RND Module]                           │
│    Target network f: ℝ^d_s → ℝ^d_f     │
│    Predictor network f̂: ℝ^d_s → ℝ^d_f  │
│    Bonus: R^RND = |f(s') - f̂(s')|²     │
│    Normalized per-episode               │
│                                         │
│  [PPO Refining Agent]                   │
│    Total reward: R(s,a) + λ·R^RND(s')  │
│    Optimizes π using PPO loss           │
│    f̂ updated via MSE loss on D         │
│                                         │
│  Output: Refined policy π′             │
└─────────────────────────────────────────┘
```

## Design Rationale

1. **Simplified StateMask objective**: By Theorem 3.3 (η(π̄) ≤ η(π) under Assumption 3.1), maximizing η(π̄) is equivalent to the original min-|η(π)−η(π̄)| and enables vanilla PPO training.

2. **Binary blinding action**: The mask network outputs 0 (critical — preserve action) or 1 (non-critical — randomize action). State importance = P(a^m=0|s).

3. **Episode-level critical state selection**: From each sampled trajectory τ of length K, the single state with maximum importance score is selected as the critical state for reset.

4. **RND normalization**: The RND bonus is normalized per episode to maintain stable scale relative to the task reward.

5. **PPO as the base algorithm**: Leverages PPO's monotonic improvement guarantee for both mask network training and policy refining.

6. **Environment reset mechanism**: Implemented as in Go-Explore (Ecoffet et al., 2019) — requires simulator-based environment that supports state restoration. Compatible with goal/state-conditioned policies as a fallback.

## Component Interfaces

| Component | Input | Output |
|-----------|-------|--------|
| Mask Network | state s_t (obs vector) | P(a^m=0|s) ∈ [0,1] |
| Critical State Identifier | trajectory τ = {s_0,...,s_T}, trained ˜πθ | critical state s* |
| Mixed Distribution Sampler | s*, ρ, p ∈ [0,1] | initial state s_0 |
| RND Module | next state s_{t+1} | scalar bonus R^RND |
| PPO Refining Agent | (s_t, a_t, R_t + λ·R^RND, s_{t+1}) | updated policy π′ |
