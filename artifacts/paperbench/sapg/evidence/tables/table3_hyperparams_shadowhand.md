---
# Table 3: Training Hyperparameters — ShadowHand Task
- **Source**: Table 3, Appendix B.2
- **Caption**: "Training hyperparameters for Shadow Hand"
- **Conditions**: MLP Gaussian policy; hidden layers 512×512×256×128 with ELU activation

| Hyperparameter | Value |
|----------------|-------|
| Discount factor, γ | 0.99 |
| GAE Lambda | 0.95 |
| Learning rate | 5e-4 |
| KL threshold for LR update | 0.016 |
| Grad norm | 1.0 |
| Entropy coefficient | Tuned from {0, 0.003, 0.005}; σ=0.005 optimal |
| Clipping factor ε | 0.1 |
| Mini-batch size | num_envs × 4 |
| Critic coefficient λ' | 4.0 |
| Horizon length | 16 (steps per env per update) |
| Bounds loss coefficient | 0.0001 |
| Mini epochs | Not specified in paper |
