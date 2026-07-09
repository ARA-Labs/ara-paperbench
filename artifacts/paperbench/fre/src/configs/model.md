# Model Configuration

## RL Network Architecture (Actor, Critic, Value)
- **Value**: [512, 512, 512] (3 hidden layers of 512 units each)
- **Rationale**: Large enough to represent complex multi-task value functions conditioned on z.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3

## Decoder Network Architecture
- **Value**: [512, 512, 512] (3 hidden layers of 512 units each)
- **Rationale**: Matched to RL network size for consistency; sufficient capacity for reward prediction.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3

## Encoder Architecture (Transformer)
- **Value**: [256, 256, 256, 256] (4 transformer layers, 256 hidden dim each)
- **Rationale**: 4-layer transformer provides sufficient depth for permutation-invariant set encoding; 256 dim balances capacity and efficiency.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3

## Encoder Attention Heads
- **Value**: 4
- **Rationale**: Multi-head attention enables the transformer encoder to attend to different aspects of the reward-state pairs simultaneously.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3

## Number of Reward Embeddings (Discretization Bins)
- **Value**: 32
- **Rationale**: Scalar rewards in [-1,1] are discretized into 32 bins; each bin has a learned embedding vector.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Section 4.1 Practical Implementation; Rubric §04d679d0

## Reward Embedding Dimension
- **Value**: 128
- **Rationale**: Embedding dimension for the 32 discretized reward bins; provides sufficient capacity to represent reward structure for downstream encoding.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A, Table 3

## Random MLP Reward Architecture
- **Value**: (state_dim → 32 → 1), tanh activation between layers, output clipped to [-1, 1]
- **Rationale**: 2-layer MLP as universal function approximator with bounded output range; size 32 hidden units balances expressivity and computational cost.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix B; Section 4.2

## Random MLP Initialization
- **Value**: Normal distribution scaled by average dimension of respective layer (i.e., scale = 1/sqrt((in_dim + out_dim)/2))
- **Rationale**: Ensures reasonable reward magnitude at initialization without extreme saturation.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix B

## AntMaze XY Discretization (Observation Preprocessing)
- **Value**: XY coordinates discretized into 32 bins
- **Rationale**: Converts continuous XY position to discrete bins for more structured policy conditioning; consistent across FRE, GC-IQL, GC-BC, OPAL.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix C.1

## ExORL Physics Augmentation (Walker)
- **Value**: Append [horizontal_velocity(), torso_upright(), torso_height()] to state for encoder input only
- **Rationale**: Walker velocity/run rewards depend on physics states not directly in observation; physics augmentation enables encoder to compute true reward functions.
- **Search range**: Not applicable
- **Sensitivity**: high (required for velocity evaluation tasks)
- **Source**: Appendix C.2

## ExORL Physics Augmentation (Cheetah)
- **Value**: Append [speed()] to state for encoder input only
- **Rationale**: Cheetah velocity reward depends on physics speed state.
- **Search range**: Not applicable
- **Sensitivity**: high (required for velocity evaluation tasks)
- **Source**: Appendix C.2

## ExORL Goal Distance Threshold
- **Value**: 0.1 (Euclidean distance between normalized state vectors)
- **Rationale**: State dimensions normalized by standard deviation within dataset; threshold of 0.1 after normalization.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix C.2

## AntMaze Goal Distance Threshold
- **Value**: 2.0 (Euclidean distance to target XY position)
- **Rationale**: Ant robot size and maze scale make distance-2 a reasonable proximity threshold.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix C.1

## AntMaze Starting Position
- **Value**: Center of maze (not original bottom-left position)
- **Rationale**: Center placement allows more diverse behavior during training and evaluation.
- **Search range**: Not applicable
- **Sensitivity**: low
- **Source**: Appendix C.1
