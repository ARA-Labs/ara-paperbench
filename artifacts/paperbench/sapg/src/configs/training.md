---
# Training Hyperparameters

## AllegroKuka Tasks (Appendix B.1, Table 2)

### Discount Factor (γ)
- **Value**: 0.99
- **Rationale**: Standard value for long-horizon tasks; high γ ensures rewards far in the future are valued.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix B.1, Table 2

### GAE Lambda (λ_GAE)
- **Value**: 0.95
- **Rationale**: Generalized Advantage Estimation parameter balancing bias vs variance.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix B.1, Table 2

### Learning Rate
- **Value**: 1e-4
- **Rationale**: Smaller learning rate used for complex LSTM-based AllegroKuka tasks to ensure stability.
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: Appendix B.1, Table 2

### KL Threshold for LR Update
- **Value**: 0.016
- **Rationale**: If KL divergence exceeds this threshold, learning rate is reduced adaptively to prevent destructive updates.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix B.1, Table 2

### Gradient Norm Clipping
- **Value**: 1.0
- **Rationale**: Prevents gradient explosion from combined on/off-policy gradients.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix B.1, Table 2

### Entropy Coefficient (σ)
- **Value**: 0 (Regrasping, Throw); 0.005 (Reorientation); tuned from {0, 0.003, 0.005}
- **Rationale**: Encourages follower diversity; harder tasks benefit from more exploration.
- **Search range**: {0, 0.003, 0.005}
- **Sensitivity**: medium
- **Source**: §5.2, Appendix B

### Clipping Factor (ε)
- **Value**: 0.1
- **Rationale**: Conservative PPO trust region for complex manipulation tasks.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix B.1, Table 2

### Mini-batch Size
- **Value**: num_envs × 4
- **Rationale**: Large mini-batches suitable for GPU training; scales with number of environments.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix B.1, Table 2

### Critic Coefficient (λ')
- **Value**: 4.0
- **Rationale**: Scales the critic loss relative to the actor loss; higher weight on value function learning.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix B.1, Table 2

### Horizon Length
- **Value**: 16 steps per environment instance
- **Rationale**: Each environment collects 16 steps before a PPO update; balances freshness of data vs update frequency.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §5.2 ("We collect 16 steps of experience per instance of the environment before every PPO update.")

### LSTM Sequence Length
- **Value**: Not specified in paper (table entry appears blank)
- **Rationale**: Sequence length for LSTM policy training.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix B.1, Table 2

### Bounds Loss Coefficient
- **Value**: 0.0001
- **Rationale**: Penalizes actions outside valid bounds.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix B.1, Table 2

### Mini Epochs
- **Value**: Not specified in paper (table entry appears blank)
- **Rationale**: Number of passes over collected data per PPO update.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix B.1, Table 2

### Number of Policies (M)
- **Value**: 6 (1 leader + 5 followers)
- **Rationale**: Used for both SAPG and DexPBT throughout all experiments.
- **Search range**: Not ablated in paper
- **Sensitivity**: medium
- **Source**: §5.2

### Number of Parallel Environments (N)
- **Value**: 24,576
- **Rationale**: Two orders of magnitude larger than PPO's original setting (~128 envs); representative of GPU-driven massively parallel simulation.
- **Search range**: Varied in Fig. 2 experiments: {~1500, 3125, 6250, 12500, 25000, 50000, 100000}
- **Sensitivity**: high
- **Source**: §5

### Number of Seeds
- **Value**: 5
- **Rationale**: Statistical significance via mean and standard error across seeds.
- **Search range**: N/A
- **Sensitivity**: N/A
- **Source**: §5.2

---

## ShadowHand Tasks (Appendix B.2, Table 3)

### Discount Factor (γ)
- **Value**: 0.99
- **Source**: Appendix B.2, Table 3

### GAE Lambda (λ_GAE)
- **Value**: 0.95
- **Source**: Appendix B.2, Table 3

### Learning Rate
- **Value**: 5e-4
- **Rationale**: Higher learning rate than AllegroKuka; simpler MLP policy converges faster.
- **Source**: Appendix B.2, Table 3

### KL Threshold for LR Update
- **Value**: 0.016
- **Source**: Appendix B.2, Table 3

### Gradient Norm
- **Value**: 1.0
- **Source**: Appendix B.2, Table 3

### Entropy Coefficient (σ)
- **Value**: 0.005 (ShadowHand)
- **Source**: §5.2

### Clipping Factor (ε)
- **Value**: 0.1
- **Source**: Appendix B.2, Table 3

### Mini-batch Size
- **Value**: num_envs × 4
- **Source**: Appendix B.2, Table 3

### Critic Coefficient (λ')
- **Value**: 4.0
- **Source**: Appendix B.2, Table 3

### Horizon Length
- **Value**: 16 steps
- **Source**: §5.2

### Bounds Loss Coefficient
- **Value**: 0.0001
- **Source**: Appendix B.2, Table 3

### Mini Epochs
- **Value**: Not specified in paper
- **Source**: Appendix B.2, Table 3

---

## AllegroHand Tasks (Appendix B.3, Table 4)

### Discount Factor (γ)
- **Value**: 0.99
- **Source**: Appendix B.3, Table 4

### GAE Lambda (λ_GAE)
- **Value**: 0.95
- **Source**: Appendix B.3, Table 4

### Learning Rate
- **Value**: 5e-4
- **Source**: Appendix B.3, Table 4

### KL Threshold for LR Update
- **Value**: 0.016
- **Source**: Appendix B.3, Table 4

### Gradient Norm
- **Value**: 1.0
- **Source**: Appendix B.3, Table 4

### Entropy Coefficient (σ)
- **Value**: 0 (AllegroHand)
- **Source**: §5.2

### Clipping Factor (ε)
- **Value**: 0.2
- **Rationale**: More permissive trust region than AllegroKuka and ShadowHand.
- **Source**: Appendix B.3, Table 4

### Mini-batch Size
- **Value**: num_envs × 4
- **Source**: Appendix B.3, Table 4

### Critic Coefficient (λ')
- **Value**: 4.0
- **Source**: Appendix B.3, Table 4

### Horizon Length
- **Value**: 16 steps
- **Source**: §5.2

### Bounds Loss Coefficient
- **Value**: 0.0001
- **Source**: Appendix B.3, Table 4

### Mini Epochs
- **Value**: Not specified in paper
- **Source**: Appendix B.3, Table 4
