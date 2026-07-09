# Training Configuration

## Encoder Training Steps
- **Value**: 150,000 (AntMaze); 1,000,000 (ExORL Walker, ExORL Cheetah, Kitchen)
- **Rationale**: Encoder must converge before policy training begins (strided training). ExORL/Kitchen datasets require more steps due to larger effective dataset size and higher-dimensional tasks.
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: Appendix A, Table 3

## Policy Training Steps
- **Value**: 850,000 (AntMaze); 1,000,000 (ExORL Walker, ExORL Cheetah, Kitchen)
- **Rationale**: Sufficient training for IQL to converge on frozen task representations across diverse reward functions.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3

## Optimizer
- **Value**: Adam
- **Rationale**: Standard choice for deep RL; adaptive learning rates handle varied gradient magnitudes from multi-task objectives.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix A, Table 3

## Learning Rate
- **Value**: 0.0001
- **Rationale**: Conservative learning rate appropriate for stable offline RL training.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3

## Discount Factor (γ)
- **Value**: 0.88
- **Rationale**: Lower than standard 0.99 to improve stability across diverse multi-task reward functions in offline setting.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3

## IQL Expectile (τ)
- **Value**: 0.8
- **Rationale**: Standard IQL expectile that balances pessimism vs. coverage in value function estimation.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3

## AWR Temperature
- **Value**: 3.0
- **Rationale**: Controls sharpness of advantage-weighted policy update; higher value = softer BC-like update.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3

## Target Update Rate
- **Value**: 0.001
- **Rationale**: Slow soft target update for stability of Bellman targets in offline RL.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3

## KL Weight (β)
- **Value**: 0.01
- **Rationale**: Light regularization; allows z to retain most task information while enforcing approximate unit Gaussian prior.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3

## Ratio of Goal-Reaching Rewards
- **Value**: 0.33 (for FRE-all)
- **Rationale**: Uniform mixture across three reward families prevents any single family from dominating the latent space.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3; Section 5

## Ratio of Linear Rewards
- **Value**: 0.33 (for FRE-all)
- **Rationale**: Uniform mixture; see above.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3

## Ratio of Random MLP Rewards
- **Value**: 0.33 (for FRE-all)
- **Rationale**: Uniform mixture; see above.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3

## Reward Pairs to Encode (K)
- **Value**: 32 (at evaluation; training uses 32 as well per Algorithm 1)
- **Rationale**: Small K ensures efficient zero-shot adaptation; contrasts with FB/SF using 5120 samples.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Table 1 footnote; Section 5.2

## Reward Pairs to Decode (K')
- **Value**: 8 (disjoint from K encoder states)
- **Rationale**: Held-out states ensure the encoder generalizes rather than memorizes.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3; Section 4.1

## AntMaze Evaluation Episode Length
- **Value**: 2000 timesteps
- **Rationale**: Long enough for Ant to navigate the large maze.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix C.1

## ExORL Evaluation Episode Length
- **Value**: 1000 timesteps
- **Rationale**: Standard DMControl episode length.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix C.2

## Evaluation Episodes per Seed
- **Value**: 20
- **Rationale**: Sufficient for low-variance estimates; standard in offline RL evaluation.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Section 5.2

## Number of Seeds
- **Value**: 5
- **Rationale**: Standard for statistical significance in RL benchmarks.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Section 5.2
