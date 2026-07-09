---
# Table 3: Training Hyperparameters for Shadow Hand

- **Source**: Table 3, Appendix B.2
- **Caption**: "Training hyperparameters for Shadow Hand"
- **Conditions**: 24-DoF Shadow Hand; MLP policy

| Hyperparameter | Value |
|---|---|
| Discount factor, γ | 0.99 |
| λ (GAE) | 0.95 |
| Learning rate | 5e-4 |
| KL threshold for LR update | 0.016 |
| Grad norm | 1.0 |
| Entropy coefficient | (blank in paper — 0.005 from §5 text) |
| Clipping factor ε | 0.1 |
| Mini-batch size | num_envs · 4 |
| Critic coefficient λ' | 4.0 |
| Horizon length | (blank in paper; 16 steps from §5) |
| Bounds loss coefficient | 0.0001 |
| Mini epochs | (blank in paper) |

**Policy Architecture**:
- MLP with hidden layer dimensions 512 × 512 × 256 × 128, ELU activation
