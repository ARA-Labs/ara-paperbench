# Training Configurations

## NetHack: APPO Training Hyperparameters (Table 1)

### adam_learning_rate
- **Value**: 0.0001
- **Rationale**: Standard learning rate for APPO; matches Hambro et al. (2022c) Table 6 from Petrenko et al. (2020)
- **Search range**: Not specified
- **Sensitivity**: high
- **Source**: Table 1, Appendix B.1

### adam_beta1
- **Value**: 0.9
- **Rationale**: Standard Adam momentum coefficient
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Table 1, Appendix B.1

### adam_beta2
- **Value**: 0.999
- **Rationale**: Standard Adam second moment coefficient
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Table 1, Appendix B.1

### adam_eps
- **Value**: 0.0000001 (1e-7)
- **Rationale**: Epsilon for numerical stability in Adam; smaller than default (1e-8) but consistent with RL practice
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Table 1, Appendix B.1

### weight_decay
- **Value**: 0.0001
- **Rationale**: L2 regularization to prevent overfitting
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Table 1, Appendix B.1

### appo_clip_policy
- **Value**: 0.1
- **Rationale**: PPO clipping range; conservative clip to prevent large policy updates
- **Search range**: Not specified
- **Sensitivity**: high
- **Source**: Table 1, Appendix B.1

### appo_clip_baseline
- **Value**: 1.0
- **Rationale**: Clipping range for value function loss
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Table 1, Appendix B.1

### baseline_cost (value function coefficient)
- **Value**: 1.0
- **Rationale**: Weight of the value function loss term in the total APPO loss
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Rubric (task 4f5a51bb)

### discounting
- **Value**: 0.999999
- **Rationale**: Very high discount factor for a long-horizon game like NetHack (episodes can be very long)
- **Search range**: Not specified
- **Sensitivity**: high
- **Source**: Table 1, Appendix B.1

### entropy_cost
- **Value**: 0.001 (vanilla fine-tuning and training from scratch); 0.0 (when using EWC, BC, or KS)
- **Rationale**: Entropy encourages exploration; disabled when using KR methods to avoid conflicting objectives
- **Search range**: Not specified
- **Sensitivity**: high
- **Source**: Table 1, Appendix B.1; Section B.1

### grad_norm_clipping
- **Value**: 4
- **Rationale**: Gradient clipping to prevent exploding gradients in LSTM training
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Rubric (task d982052f)

### batch_size
- **Value**: 128
- **Rationale**: Batch size for APPO training
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Rubric (task 9b430504)

### penalty_step
- **Value**: 0.0
- **Rationale**: No per-step reward penalty
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Table 1, Appendix B.1

### penalty_time
- **Value**: 0.0
- **Rationale**: No per-time reward penalty
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Table 1, Appendix B.1

### reward_clip
- **Value**: +-10
- **Rationale**: Clip rewards to prevent gradient explosion from large reward spikes
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Rubric (task 1c251dfa)

### reward_scale
- **Value**: 1.0 (no scaling beyond clipping)
- **Rationale**: Rewards not scaled; clipping alone is sufficient
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Rubric (task cb0233d3)

### unroll_length
- **Value**: 32
- **Rationale**: Rollout length for APPO; short rollouts allow more frequent parameter updates
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Rubric (task 491ae6e3)

### critic_pretraining_steps (NetHack only)
- **Value**: 500M environment steps
- **Rationale**: Pre-train critic head only (with rest of model frozen) before full fine-tuning to stabilize value function
- **Search range**: Not specified
- **Sensitivity**: high
- **Source**: Section B.1 (Pre-training subsection)

### KS_auxiliary_loss_scale
- **Value**: 0.5
- **Rationale**: Weight of KS auxiliary loss relative to RL loss
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Section B.1 (Fine-tuning subsection)

### KS_exponential_decay
- **Value**: 0.99998 per training step
- **Rationale**: Gradually reduce KS constraint to allow policy improvement over time
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Section B.1 (Fine-tuning subsection)

### BC_auxiliary_loss_scale
- **Value**: 2.0 (NetHack)
- **Rationale**: Scale BC KL loss to match magnitude of RL loss
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Section B.1 (Fine-tuning subsection)

### EWC_regularization_coefficient
- **Value**: 2,000,000 (2 × 10⁶) for NetHack
- **Rationale**: Large coefficient needed due to scale of Fisher values
- **Search range**: Not specified
- **Sensitivity**: high
- **Source**: Section B.1 (Fine-tuning subsection)

---

## Montezuma's Revenge: PPO+RND Hyperparameters (Table 2)

### MaxStepPerEpisode
- **Value**: 4500
- **Source**: Table 2, Appendix B.2

### ExtCoef (extrinsic reward coefficient)
- **Value**: 2.0
- **Source**: Table 2, Appendix B.2

### LearningRate
- **Value**: 1e-4
- **Source**: Table 2, Appendix B.2

### NumEnv (parallel environments)
- **Value**: 128
- **Source**: Rubric (task 47d6c57d)

### NumStep (steps per rollout)
- **Value**: 128
- **Source**: Rubric (task 54d5e6d1)

### Gamma (extrinsic discount)
- **Value**: 0.999
- **Source**: Table 2, Appendix B.2

### IntGamma (intrinsic reward discount)
- **Value**: 0.99
- **Source**: Table 2, Appendix B.2

### Lambda (GAE parameter)
- **Value**: 0.95
- **Source**: Table 2, Appendix B.2

### StableEps
- **Value**: 1e-8
- **Source**: Table 2, Appendix B.2

### StateStackSize
- **Value**: 4
- **Source**: Rubric (task 1cc11bdb)

### PreProcHeight / PreProcWidth
- **Value**: 84 × 84
- **Source**: Rubric (tasks 23a7b10f, 45974989)

### UseGAE
- **Value**: True
- **Source**: Table 2, Appendix B.2

### UseNorm
- **Value**: False
- **Source**: Table 2, Appendix B.2

### UseNoisyNet
- **Value**: False
- **Source**: Table 2, Appendix B.2

### ClipGradNorm
- **Value**: 0.5
- **Source**: Table 2, Appendix B.2

### Entropy
- **Value**: 0.001
- **Source**: Table 2, Appendix B.2

### Epoch
- **Value**: 4
- **Source**: Rubric (task 4724cd08)

### MiniBatch
- **Value**: 4
- **Source**: Rubric (task f9554ef5)

### PPOEps
- **Value**: 0.1
- **Source**: Table 2, Appendix B.2

### IntCoef (intrinsic reward coefficient)
- **Value**: 1.0
- **Source**: Table 2, Appendix B.2

### StickyAction
- **Value**: True
- **Source**: Table 2, Appendix B.2

### ActionProb (sticky action probability)
- **Value**: 0.25
- **Source**: Table 2, Appendix B.2

### UpdateProportion
- **Value**: 0.25
- **Source**: Table 2, Appendix B.2

### LifeDone
- **Value**: False
- **Source**: Table 2, Appendix B.2

### ObsNormStep
- **Value**: 50
- **Source**: Rubric (task fbaf9172)

### UseGPU
- **Value**: True
- **Source**: Table 2, Appendix B.2

---

## RoboticSequence: SAC Hyperparameters (Table 3)

### learning_rate
- **Value**: 1e-3
- **Rationale**: Higher than default; found to work well in Continual World (Wołczyk et al., 2021) with hyperparameter tuning
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: Appendix B.3

### optimizer
- **Value**: Adam (Kingma & Ba, 2014)
- **Sensitivity**: low
- **Source**: Appendix B.3

### batch_size
- **Value**: 128
- **Sensitivity**: medium
- **Source**: Appendix B.3

### replay_buffer_size
- **Value**: 100,000
- **Sensitivity**: medium
- **Source**: Appendix B.3, C.3

### episodic_memory_size
- **Value**: 10,000 (10% of replay buffer)
- **Sensitivity**: medium
- **Source**: Appendix B.3, C.3

### max_steps_per_stage (T)
- **Value**: 200
- **Sensitivity**: medium
- **Source**: Appendix B.3

### success_reward_multiplier (β)
- **Value**: 1.5
- **Rationale**: Encourages early task completion; without it, policy avoids terminating to collect more rewards
- **Sensitivity**: medium
- **Source**: Appendix B.3

### EWC_actor_regularization_coefficient
- **Value**: 100
- **Sensitivity**: high
- **Source**: Table 3, Appendix B.3

### EWC_critic_regularization_coefficient
- **Value**: 0
- **Rationale**: Critic not regularized following Wolczyk et al. (2022)
- **Sensitivity**: low
- **Source**: Table 3, Appendix B.3

### BC_actor_regularization_coefficient
- **Value**: 1
- **Sensitivity**: high
- **Source**: Table 3, Appendix B.3

### BC_critic_regularization_coefficient
- **Value**: 0
- **Sensitivity**: low
- **Source**: Table 3, Appendix B.3

### n_seeds (RoboticSequence)
- **Value**: 20 (minimum), 90% confidence intervals reported
- **Source**: Appendix B.3
