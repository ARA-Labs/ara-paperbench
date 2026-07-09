---
# Model Configurations

## AllegroKuka Policy Network (LSTM-based, Appendix B.1)

### MLP Pre-processor
- **Architecture**: MLP with hidden layer dimensions 768 × 512 × 256
- **Activation**: ELU (Exponential Linear Unit) [Clevert et al., 2016]
- **Input**: Raw observation vector ot = [q, q̇, xt, vt, ωt, gt, zt], concatenated with hanging parameter ϕj
- **Output**: 256-dimensional embedding fed into LSTM

### LSTM Core
- **Layers**: 1
- **Hidden units**: 768
- **Input**: 256-dim MLP output (conditioned on ϕj)
- **Output**: 768-dim hidden state → action mean

### Action Distribution
- **Type**: Gaussian
- **Mean**: Output of LSTM (768 → action_dim linear layer)
- **Sigma**: Fixed learnable vector, independent of observation (not input-dependent)
- **Note**: When entropy regularization is active, each block has its own learnable sigma vector

### Critic Network
- **Architecture**: Same backbone structure as actor (MLP + LSTM), conditioned on ϕj
- **Output**: Scalar value estimate Vπj(s)

### Hanging Parameter Dimension
- **Value**: ϕj ∈ R32
- **Justification**: Complex tasks require larger latent conditioning dimension
- **Source**: §4.4

### Task Details
- **Robot**: Allegro Hand (16 DoF) + Kuka arm (7 DoF) = 23 total DoF
- **Observation dimensions**: q, q̇ ∈ R²³; xt ∈ R⁷; vt, ωt (velocities); gt (goal); zt (auxiliary)

---

## ShadowHand Policy Network (MLP-based, Appendix B.2)

### Architecture
- **Hidden layers**: 512 × 512 × 256 × 128
- **Activation**: ELU
- **Input**: Observation + hanging parameter ϕj
- **Output**: Action mean (Gaussian policy)

### Action Distribution
- **Type**: Gaussian
- **Sigma**: Fixed learnable vector (per-block when entropy regularization active)

### Hanging Parameter Dimension
- **Value**: ϕj ∈ R16
- **Source**: §4.4

### Task Details
- **Robot**: Shadow Hand, 24 DoF
- **Task**: In-hand cube reorientation to quaternion goal gt ∈ R⁴
- **Metric**: Episode reward (combination of orientation error + success bonus)

---

## AllegroHand Policy Network (MLP-based, Appendix B.3)

### Architecture
- **Hidden layers**: 512 × 256 × 128
- **Activation**: ELU
- **Input**: Observation + hanging parameter ϕj
- **Output**: Action mean (Gaussian policy)

### Action Distribution
- **Type**: Gaussian
- **Sigma**: Fixed learnable vector

### Hanging Parameter Dimension
- **Value**: ϕj ∈ R16
- **Source**: §4.4

### Task Details
- **Robot**: Allegro Hand, 16 DoF
- **Task**: In-hand cube reorientation
- **Metric**: Episode reward

---

## Multi-Policy System Configuration

### Number of Policies (M)
- **Value**: M = 6 (1 leader + 5 followers)

### Off-policy Lambda (λ)
- **Value**: 1 (with 50/50 data subsampling)

### n-step Returns
- **Value**: n = 3 for on-policy critic targets
- **Value**: n = 1 (1-step) for off-policy critic targets

### Diversity Module
- **Latent conditioning**: ϕj per policy (R32 or R16)
- **Entropy regularization**: Per-follower coefficient λent(j-1) ∈ {0, 0.003, 0.005}
