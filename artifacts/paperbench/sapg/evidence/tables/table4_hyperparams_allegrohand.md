---
# Table 4: Training Hyperparameters — AllegroHand Task
- **Source**: Table 4, Appendix B.3
- **Caption**: "Training hyperparameters for Shadow Hand" (note: paper labels Table 4 as "Shadow Hand" but this section covers AllegroHand; likely a typo in the paper)
- **Conditions**: MLP Gaussian policy; hidden layers 512×256×128 with ELU activation

| Hyperparameter | Value |
|----------------|-------|
| Discount factor, γ | 0.99 |
| GAE Lambda | 0.95 |
| Learning rate | 5e-4 |
| KL threshold for LR update | 0.016 |
| Grad norm | 1.0 |
| Entropy coefficient | σ=0 optimal for AllegroHand |
| Clipping factor ε | 0.2 |
| Mini-batch size | num_envs × 4 |
| Critic coefficient λ' | 4.0 |
| Horizon length | 16 (steps per env per update) |
| Bounds loss coefficient | 0.0001 |
| Mini epochs | Not specified in paper |

**Note on entropy (Appendix B Note)**: In experiments with entropy-based exploration, each block of environments has its own learnable sigma vector, enabling policies for different blocks to have different entropies.
