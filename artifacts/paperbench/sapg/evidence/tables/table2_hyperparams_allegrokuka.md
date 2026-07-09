---
# Table 2: Training Hyperparameters — AllegroKuka Tasks
- **Source**: Table 2, Appendix B.1
- **Caption**: "Training hyperparameters for AllegroKuka tasks"
- **Conditions**: LSTM-based recurrent Gaussian policy; observation MLP 768×512×256 with ELU; LSTM 1 layer 768 hidden; sigma is fixed learnable vector independent of observation

| Hyperparameter | Value |
|----------------|-------|
| Discount factor, γ | 0.99 |
| GAE Lambda | 0.95 |
| Learning rate | 1e-4 |
| KL threshold for LR update | 0.016 |
| Grad norm | 1.0 |
| Entropy coefficient | Tuned from {0, 0.003, 0.005} per task |
| Clipping factor ε | 0.1 |
| Mini-batch size | num_envs × 4 |
| Critic coefficient λ' | 4.0 |
| Horizon length | 16 (steps per env per update) |
| LSTM Sequence length | Not specified in paper |
| Bounds loss coefficient | 0.0001 |
| Mini epochs | Not specified in paper |

**Notes**: The paper's Table 2 lists "Entropy coefficient", "Horizon length", "LSTM Sequence length", and "Mini epochs" as rows but the corresponding values are not printed in the available paper text.
