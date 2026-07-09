# Model Configuration

## Policy Network (MuJoCo Environments — Stable-Baselines3 Default)
- **Architecture**: MLP (Multi-Layer Perceptron); exact hidden sizes not specified for MuJoCo in paper
- **Framework**: Stable-Baselines3 (Raffin et al., 2021)
- **Algorithm**: PPO
- **Observation normalization**: Yes for Walker2d-v3 and HalfCheetah-v3; not specified for others
- **Source**: §4.1, Appendix C.1

## Policy Network (Selfish Mining Environment)
- **Architecture**: 4-layer MLP with hidden sizes [128, 128, 128, 128]
- **Algorithm**: PPO
- **Input**: Current blockchain chain state
- **Output**: 3 discrete actions (Adopt l, Reveal l, Mine)
- **Source**: Appendix C.2

## Mask Network (All Environments)
- **Architecture**: Same architecture as the target agent's policy network (environment-specific)
- **Output**: Binary action a^m ∈ {0, 1} (0 = critical/preserve, 1 = non-critical/randomize)
- **Output activation**: Softmax over {0, 1} (interpreted as probability P(a^m=0|s))
- **Training**: PPO with modified reward R′ = R + α·a^m
- **Source**: §3.3, Algorithm 1, Appendix C.1

## RND Networks (All Environments)
- **Target network f**: Fixed randomly initialized MLP; input = state s, output ∈ ℝ^{d_f}
- **Predictor network f̂**: Trained MLP; same architecture as f; updated via MSE loss
- **d_f (output dimension)**: Not specified in paper
- **Optimizer for f̂**: Adam
- **Source**: §3.3, Algorithm 2

## Policy Network (Autonomous Driving — DI-drive Implementation)
- **Framework**: DI-drive (drive Contributors, 2021); PPO
- **Environment**: MetaDrive Macro-v1
- **Action space**: Normalized action a = [a1, a2] ∈ [−1, 1]^2 (steering + acceleration/brake)
- **Source**: Appendix C.2

## Environments — Version Specifications
| Environment | Version | Obs Normalization |
|-------------|---------|-------------------|
| Hopper | Hopper-v3 | No |
| Walker2d | Walker2d-v3 | Yes |
| Reacher | Reacher-v2 | No |
| HalfCheetah | HalfCheetah-v3 | Yes |
| SparseHopper | Hopper-v3 (sparse reward) | No |
| SparseWalker2d | Walker2d-v3 (sparse reward) | Yes |
| SparseHalfCheetah | HalfCheetah-v3 (sparse reward) | Yes |
| Selfish Mining | Custom (Bar-Zur et al., 2023) | Not specified |
| CAGE Challenge 2 | Cardiff champion (git/c) | Not specified |
| Autonomous Driving | MetaDrive Macro-v1 | Not specified |
| Malware Mutation | MalConv gym (git/a) | Not specified |
