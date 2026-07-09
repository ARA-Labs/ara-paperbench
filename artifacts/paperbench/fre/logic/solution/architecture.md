# System Architecture

## Overview
FRE consists of three interacting components: (1) an FRE Encoder, (2) an FRE Decoder, and (3) an FRE-conditioned IQL Policy. Training is strided: encoder-decoder trains first, then the encoder is frozen and the policy trains.

## Component Graph

```
Offline Dataset D
      |
      |--- Sample {s^e_k} ---------> [FRE Encoder] --> z ~ N(mu, sigma)
      |--- Sample eta(s^e_k) ------/                        |
      |                                                      |
      |--- Sample {s^d_k} ---------> [FRE Decoder] <--------+
           Sample eta(s^d_k)              |
                                         MSE Loss (Phase 1)
                                         
z (frozen) + s + a --> [IQL Q-Network] --> Q(s,a,z)
z (frozen) + s     --> [IQL V-Network] --> V(s,z)
z (frozen) + s     --> [IQL Actor]     --> pi(a|s,z)
```

## FRE Encoder: `p_theta(z | {s^e_k, eta(s^e_k)})`
- **Purpose**: Compress K (state, reward) pairs into a latent task vector z
- **Inputs**: K state vectors `s^e_k ∈ R^{state_dim}`, K scalar rewards `eta(s^e_k) ∈ R`
- **Outputs**: Mean `mu ∈ R^{latent_dim}`, log-std `log_sigma ∈ R^{latent_dim}` → z ~ N(mu, sigma)
- **Architecture**:
  - Reward discretization: scalar → int in {0,...,31} → learned embedding (32 × emb_dim)
  - State projection: linear(state_dim → emb_dim)
  - Token = concat(state_emb, reward_emb) → K tokens of dim 2*emb_dim
  - Transformer: 4 layers, 256 hidden dim, multi-head attention, NO causal mask, NO positional encoding
  - Mean pool over K final token representations → two linear heads → (mu, log_sigma)
- **Key design choice**: Permutation invariance by removing causal masking and positional encodings

## FRE Decoder: `q_theta(eta(s^d) | s^d, z)`
- **Purpose**: Predict reward for individual decoder states given shared latent z
- **Inputs**: Single state `s^d ∈ R^{state_dim}`, latent `z ∈ R^{latent_dim}`
- **Outputs**: Predicted scalar reward `r_hat ∈ R`
- **Architecture**: Feedforward MLP [512, 512, 512] with input = concat(s^d, z)
- **Loss**: MSE between predicted and true rewards on decoder states
- **Key design choice**: Decoder states are sampled independently of encoder states

## IQL Policy: `pi(a | s, z)`, `Q(s, a, z)`, `V(s, z)`
- **Purpose**: Learn to maximize expected return for tasks within the prior reward distribution
- **Inputs**: State `s`, action `a`, frozen latent `z`
- **Architecture**: All networks are MLPs [512, 512, 512] with input = concat(s, z)
- **Actor**: Outputs Gaussian distribution (mean, log_std) over actions
- **Critic**: Two Q-networks (double Q-learning); updated with Bellman target
- **Value network**: Expectile regression with tau=0.8
- **Target critic**: Soft update with rate 0.001
- **Key design choice**: z is frozen during policy training; z is sampled once per reward function and fixed for all transitions in that batch

## Training and Inference Protocol

### Phase 1 — Encoder-Decoder Training (strided)
1. Sample eta ~ p(eta)
2. Sample K states {s^e_k} ~ D uniformly
3. Encode: z ~ p_theta(z | {s^e_k, eta(s^e_k)})
4. Sample K' decoder states {s^d_k} ~ D (disjoint from encoder states)
5. Compute FRE ELBO loss; update encoder and decoder

### Phase 2 — Policy Training (encoder frozen)
1. Freeze encoder weights
2. Sample eta ~ p(eta); encode K states → z (frozen encoder)
3. Sample transitions (s, a, s') from D; compute r = eta(s)
4. Train IQL: Q, V, pi with input = concat(s, z) [or concat(s,a,z) for Q]

### Evaluation (zero-shot)
1. Sample K=32 states from environment; annotate with test reward function eta_eval
2. Encode → z_eval via frozen FRE encoder
3. Execute pi(a|s, z_eval) without any gradient updates
