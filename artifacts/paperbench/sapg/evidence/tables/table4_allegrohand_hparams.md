---
# Table 4: Training Hyperparameters for Allegro Hand

- **Source**: Table 4, Appendix B.3
- **Caption**: "Training hyperparameters for Shadow Hand" (note: the paper labels this as Shadow Hand but the section is B.3 AllegroHand — this is the AllegroHand table per the appendix structure)
- **Conditions**: 16-DoF Allegro Hand; MLP policy

| Hyperparameter | Value |
|---|---|
| Discount factor, γ | 0.99 |
| λ (GAE) | 0.95 |
| Learning rate | 5e-4 |
| KL threshold for LR update | 0.016 |
| Grad norm | 1.0 |
| Entropy coefficient | (blank in paper — 0 from §5 text) |
| Clipping factor ε | 0.2 |
| Mini-batch size | num_envs · 4 |
| Critic coefficient λ' | 4.0 |
| Horizon length | (blank in paper; 16 steps from §5) |
| Bounds loss coefficient | 0.0001 |
| Mini epochs | (blank in paper) |

**Policy Architecture**:
- MLP with hidden layer dimensions 512 × 256 × 128, ELU activation

**Note**: AllegroHand differs from ShadowHand in: (1) MLP size (3 layers vs 4 layers), (2) clipping factor ε=0.2 vs 0.1.
