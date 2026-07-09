# System Architecture

## Overview

NPSE/TSNPSE consists of four main components: (1) an SDE module that defines the forward noising process and computes transition scores, (2) a conditional score network with three independent embedding sub-networks, (3) a training pipeline that minimises the DSM objective, and (4) a sampling/density-evaluation pipeline based on the probability flow ODE.

## Component Graph

```
[Simulator p(x|θ)] ──────────────────────────┐
       │                                       │
[Prior p(θ)] ──► [Proposal ˜p^r(θ)] ──────────►[Training Dataset D]
                       ↑                       │
          [HPR Estimation] ◄── [ODE Sampler]   │
                   ↑                           ▼
          [Density Evaluator] ◄── [Score Network s_ψ(θ_t, x, t)]
                                         ▲
                              [SDE: VE or VP] ──► [Transition Score ∇ log p_{t|0}]
                              
[Score Network] ──► [ODE Sampler (RK45)] ──► [Posterior Samples θ ~ p(θ|x_obs)]
```

## Component Descriptions

### 1. SDE Module
- **Purpose**: Define forward noising process; compute transition log-density and its gradient.
- **Inputs**: θ_0, t; SDE type (VE or VP); hyperparameters (σ_min, σ_max or β_min, β_max).
- **Outputs**: θ_t ~ p_{t|0}(·|θ_0); ∇_{θ_t} log p_{t|0}(θ_t|θ_0) in closed form.
- **VE SDE**: f(θ_t,t)=0; g(t) = σ_min (σ_max/σ_min)^t √(2 log(σ_max/σ_min)); transition = N(θ_0, σ²_min (σ_max/σ_min)^{2t} I).
- **VP SDE**: f(θ_t,t) = -½β_t θ_t; g(t) = √β_t; β_t = β_min + t(β_max-β_min); transition = N(θ_0 exp(-∫β_s ds/2), I - I exp(-∫β_s ds)).

### 2. θ_t Embedding Network
- **Purpose**: Embed the noised parameter vector θ_t into a fixed-size representation.
- **Inputs**: θ_t ∈ R^d (standardised by subtracting empirical mean and dividing by std).
- **Outputs**: θ_emb ∈ R^{max(30, 4d)}.
- **Architecture**: 3-layer fully-connected MLP, 256 hidden units per layer, SiLU activations.

### 3. x Embedding Network
- **Purpose**: Embed the observation vector x into a fixed-size representation.
- **Inputs**: x ∈ R^p (standardised by subtracting empirical mean and dividing by std).
- **Outputs**: x_emb ∈ R^{max(30, 4p)}.
- **Architecture**: 3-layer fully-connected MLP, 256 hidden units per layer, SiLU activations.

### 4. t Sinusoidal Embedding
- **Purpose**: Embed the continuous time index t into a fixed-size representation.
- **Inputs**: t ∈ (0, 1].
- **Outputs**: t_emb ∈ R^64.
- **Formula**: `(t_emb)_i = sin(t / 10000^{(i-1)/31})` if i ≤ 32, else `cos(t / 10000^{((i-32)-1)/31})`.

### 5. Score Network
- **Purpose**: Combine embeddings and output the approximate posterior score.
- **Inputs**: Concatenation [θ_emb, x_emb, t_emb].
- **Outputs**: s_ψ(θ_t, x, t) ∈ R^d (approximating ∇_θ log p_t(θ_t|x)).
- **Architecture**: 3-layer fully-connected MLP, 256 hidden units per layer, SiLU activations.
- **Key design**: No normalisation constraint needed (does not need to be a normalising flow). No adversarial training.

### 6. Training Pipeline (DSM Objective)
- **Purpose**: Train score network by minimising Monte Carlo estimate of Eq. 7.
- **Inputs**: Dataset D = {(θ_0,i, x_i)}; SDE hyperparameters; λ_t weighting.
- **Procedure**: For each mini-batch, sample t ~ U(0,T), draw θ_t ~ p_{t|0}(·|θ_0), compute ||s_ψ - ∇ log p_{t|0}||², backpropagate.
- **Interactions**: Feeds into Score Network; receives samples from SDE Module.

### 7. ODE Sampler (Posterior Sampling)
- **Purpose**: Generate approximate posterior samples by solving time-reversal of probability flow ODE.
- **Inputs**: s_ψ(·, x_obs, ·); initial samples from π = N(0,I); ODE solver (RK45).
- **Outputs**: θ ~ p(θ|x_obs) approximately.
- **Interactions**: Uses Score Network output; feeds into HPR Estimation.

### 8. Density Evaluator (Instantaneous Change-of-Variables)
- **Purpose**: Evaluate log p_ψ(θ|x_obs) via Eq. 5 for HPR estimation and rejection sampling.
- **Inputs**: θ, s_ψ; ODE solution trace.
- **Outputs**: log p_ψ(θ|x_obs) (up to normalisation).
- **Interactions**: Feeds into HPR Estimation.

### 9. HPR Estimation and Truncated Proposal Sampler (TSNPSE only)
- **Purpose**: Define proposal prior ˜p^r(θ) for next round.
- **Procedure**: (1) Draw 20000 samples from ODE sampler; (2) evaluate log-densities via change-of-variables; (3) compute κ = ε=5×10⁻⁴ quantile; (4) rejection sample from prior with initial hypercube pre-rejection, then likelihood threshold κ.
- **Interactions**: Uses Density Evaluator; feeds Proposal samples to Training Pipeline.
