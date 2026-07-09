---
# Table 2: Training Hyperparameters for AllegroKuka Tasks

- **Source**: Table 2, Appendix B.1
- **Caption**: "Training hyperparameters for AllegroKuka tasks"
- **Conditions**: Allegro Hand (16 DoF) + Kuka arm (7 DoF); recurrent (LSTM) policy

| Hyperparameter | Value |
|---|---|
| Discount factor, γ | 0.99 |
| λ (GAE) | 0.95 |
| Learning rate | 1e-4 |
| KL threshold for LR update | 0.016 |
| Grad norm | 1.0 |
| Entropy coefficient | (blank in paper — task-dependent: 0 for Regrasping/Throw, 0.005 for Reorientation) |
| Clipping factor ε | 0.1 |
| Mini-batch size | num_envs · 4 |
| Critic coefficient λ' | 4.0 |
| Horizon length | (blank in paper) |
| LSTM Sequence length | (blank in paper) |
| Bounds loss coefficient | 0.0001 |
| Mini epochs | (blank in paper) |

**Policy Architecture**:
- Mean network: LSTM (1 layer, 768 hidden units)
- Observation preprocessor: MLP with hidden dimensions 768 × 512 × 256, ELU activation
- σ (log std): fixed learnable vector independent of input observation
