# Training Configuration

## Hyperparameter: p (Reset Probability / Mixing Ratio)
- **Value**: Hopper=0.25, Walker2d=0.25, Reacher=0.50, HalfCheetah=0.50, Selfish Mining=0.25, CAGE Challenge 2=0.50, Autonomous Driving=0.25, Malware Mutation=0.50
- **Rationale**: Controls the fraction of episodes initialized from critical states. Values of 0.25 and 0.5 balance coverage diversity with exploitation of critical states (Appendix C.3).
- **Search range**: {0, 0.25, 0.5, 0.75, 1.0}
- **Sensitivity**: medium
- **Source**: Table 3, §4.2 Experiment V, Appendix C.3

## Hyperparameter: λ (RND Exploration Bonus Weight)
- **Value**: Hopper=0.001, Walker2d=0.01, Reacher=0.001, HalfCheetah=0.01, Selfish Mining=0.001, CAGE Challenge 2=0.01, Autonomous Driving=0.01, Malware Mutation=0.01
- **Rationale**: Balances the task reward and the RND exploration bonus. Any λ > 0 provides improvement; λ = 0.01 is the best default for most environments.
- **Search range**: {0, 0.001, 0.01, 0.1}
- **Sensitivity**: low
- **Source**: Table 3, §4.2 Experiment V, Appendix C.3, Figure 8

## Hyperparameter: α (Mask Network Blinding Bonus)
- **Value**: 0.0001 for all environments
- **Rationale**: Prevents trivial solution (mask never blinds agent). Low value avoids distorting task reward. Fidelity score is insensitive to α in {0.01, 0.001, 0.0001}.
- **Search range**: {0.01, 0.001, 0.0001}
- **Sensitivity**: low
- **Source**: Table 3, §4.2 Experiment V, Appendix C.3, Figure 9

## Hyperparameter: K (Top-K Critical Steps Percentage for Fidelity)
- **Value**: K ∈ {10%, 20%, 30%, 40%} (used for fidelity evaluation only, not for refining)
- **Rationale**: Evaluates fidelity score at multiple granularities to validate explanation quality.
- **Search range**: {10%, 20%, 30%, 40%}
- **Sensitivity**: medium (metric reporting parameter)
- **Source**: §4.2 Experiment I

## Hyperparameter: Fidelity Evaluation Trajectories
- **Value**: 500 trajectories per environment per seed
- **Rationale**: Sufficient sample size for stable fidelity score estimates.
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: §4.2 Experiment I

## Hyperparameter: Random Seeds
- **Value**: 3 random seeds per experiment (specific values not specified in paper)
- **Rationale**: Standard practice; mean and standard deviation reported across 3 seeds.
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: §4.2

## Hyperparameter: Mask Network Training Sample Budget (per environment)
- **Value**: Hopper=3×10^5, Walker2d=3×10^5, Reacher=3×10^5, HalfCheetah=3×10^5, Selfish Mining=1.5×10^6, CAGE Challenge 2=1×10^7, Autonomous Driving=2,443,260, Malware Mutation=32,349
- **Rationale**: Fixed sample budget used for efficiency comparison between StateMask and Ours.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Table 4, Appendix C.3

## Hyperparameter: Pre-training Steps (SAC, Experiment IV)
- **Value**: 1,000,000 steps (1M)
- **Rationale**: Training SAC until convergence/bottleneck in Hopper-v3.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: §4.2, Figure 3 caption

## Hyperparameter: Refining Steps (Experiment IV)
- **Value**: 1,000,000 steps (1M)
- **Rationale**: Same budget for all refining methods in Experiment IV.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: §4.2, Figure 3 caption

## Hyperparameter: Malware Mutation Reward Scaling (Design Flaw Fix)
- **Value**: Intermediate reward scaling coefficient = 3 (in fixed reward design)
- **Rationale**: Original intermediate rewards had high sparsity (near-zero values); scaling by 3 improves learning signal.
- **Search range**: Not specified
- **Sensitivity**: high
- **Source**: Appendix D.2

## Hyperparameter: Malware Mutation Big Reward
- **Value**: 10 (reward for successfully evading detection)
- **Rationale**: Terminal reward for successful evasion; large relative to intermediate rewards.
- **Search range**: Not specified
- **Sensitivity**: high
- **Source**: Appendix C.2

## Hyperparameter: Malware Mutation Max Steps
- **Value**: 10 (maximum mutation steps per episode)
- **Rationale**: Limits episode length for malware mutation task.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Appendix C.2

## Hyperparameter: CAGE Challenge 2 Episode Lengths
- **Value**: 30, 50, 100 (three lengths; final reward = sum of average rewards across all three)
- **Rationale**: Evaluates robustness of the blue agent across different episode horizons.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Appendix C.2

## Hyperparameter: Selfish Mining Whale Transaction Fee
- **Value**: 10 (fee for whale transactions); 0.01 (whale occurring probability); 1 (fee for normal transactions)
- **Rationale**: Models realistic blockchain transaction fee distribution with rare high-value transactions.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Appendix C.2

## Hyperparameter: Sparse MuJoCo Reward Threshold (SparseHopper, SparseWalker2d)
- **Value**: x > 0.6 (x-position threshold for receiving reward)
- **Rationale**: Sparse reward version from Mazoure et al. (2019); only rewards forward progress beyond threshold.
- **Search range**: Not specified
- **Sensitivity**: high
- **Source**: Appendix C.2

## Hyperparameter: Sparse MuJoCo Reward Threshold (SparseHalfCheetah)
- **Value**: x > 5.0 (x-position threshold for receiving reward)
- **Rationale**: Sparse reward version from Mazoure et al. (2019).
- **Search range**: Not specified
- **Sensitivity**: high
- **Source**: Appendix C.2
