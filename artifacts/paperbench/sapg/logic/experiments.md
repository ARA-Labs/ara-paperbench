---
# Experiments

## E01: PPO Batch Size Scaling Analysis
- **Verifies**: C01
- **Setup**:
  - Model: PPO with Gaussian policy (MLP or LSTM depending on task)
  - Hardware: Single GPU (sufficient for IsaacGym simulation)
  - Dataset: IsaacGym Shadow Hand and Allegro Kuka Throw environments
  - System: IsaacGym GPU-accelerated simulator
- **Procedure**:
  1. Select batch sizes spanning approximately {1500, 3125, 6250, 12500, 25000, 50000, 100000} environments (corresponding to varying numbers of parallel envs).
  2. For each batch size, train PPO to convergence (or a fixed compute budget) and record the asymptotic performance.
  3. Plot asymptotic performance (y-axis) vs. batch size (x-axis) for both Shadow Hand (episode rewards) and Allegro Kuka Throw (episode successes).
  4. Add a horizontal dashed line at SAPG's performance level for reference.
  5. Repeat across at least 3 seeds and report mean.
- **Metrics**: Asymptotic episode reward (Shadow Hand) or episode successes (Allegro Kuka Throw) as a function of number of parallel environments.
- **Expected outcome**:
  - PPO performance should plateau and stop improving after a certain batch size threshold; additional environments provide diminishing returns.
  - SAPG should exceed the PPO saturation ceiling, demonstrating that higher performance IS achievable with more environments when the algorithm is designed correctly.
  - NEVER include exact numbers here.
- **Baselines**: PPO with varying batch sizes.
- **Dependencies**: none

## E02: Main Performance Comparison on Hard Tasks (AllegroKuka Suite)
- **Verifies**: C02
- **Setup**:
  - Model: SAPG (M=6, recurrent LSTM policy, ϕ∈R32), DexPBT (M=6), PPO, PQL
  - Hardware: Single GPU (NVIDIA GPU supporting IsaacGym); ~48-60 hours per run
  - Dataset: AllegroKuka Regrasping, Throw, Reorientation, Two Arms Reorientation (IsaacGym)
  - System: N=24,576 parallel environments; 16 steps horizon; 5 seeds per method
- **Procedure**:
  1. Configure IsaacGym with 24,576 parallel AllegroKuka environments (Allegro Hand 16 DoF + Kuka arm 7 DoF).
  2. Train each method (SAPG, PPO, DexPBT, PQL) for approximately 2×10¹⁰ total environment steps.
  3. For SAPG: use M=6 policies, leader-follower scheme, ϕ∈R32, LSTM policy (768 hidden units), 50/50 on/off-policy data split for leader.
  4. For DexPBT: M=6 groups, each N/M environments, with hyperparameter mutation.
  5. Record episode successes (number of successes per episode) throughout training.
  6. Report mean ± standard error across 5 seeds at 2×10¹⁰ steps.
- **Metrics**: Episode successes (number of successful task completions per episode) at 2×10¹⁰ environment steps.
- **Expected outcome**:
  - SAPG should substantially outperform PPO and PQL (which are expected to achieve near-zero performance on hard tasks).
  - SAPG should outperform DexPBT (which directly optimizes success via reward mutation).
  - Performance gap should be larger on harder tasks (Reorientation, Two Arms Reorientation) than easier ones (Throw).
- **Baselines**: PPO, DexPBT, PQL
- **Dependencies**: none

## E03: Main Performance Comparison on Easy Tasks (ShadowHand, AllegroHand)
- **Verifies**: C02
- **Setup**:
  - Model: SAPG (M=6, MLP policy, ϕ∈R16), DexPBT (M=6), PPO, PQL
  - Hardware: Single GPU; ~48-60 hours per run
  - Dataset: ShadowHand (24 DoF, in-hand cube reorientation), AllegroHand (16 DoF, in-hand cube reorientation) from IsaacGym
  - System: N=24,576 parallel environments; 16 steps horizon; 5 seeds
- **Procedure**:
  1. Configure IsaacGym with 24,576 parallel environments for each task.
  2. Train SAPG with MLP policy (ShadowHand: 512×512×256×128, AllegroHand: 512×256×128), ϕ∈R16, entropy σ=0.005 for ShadowHand, σ=0 for AllegroHand.
  3. Train PPO, DexPBT, PQL under the same environment conditions.
  4. Collect episode rewards throughout training up to 2×10¹⁰ steps.
  5. Report mean ± standard error across 5 seeds.
- **Metrics**: Episode reward (not successes) at 2×10¹⁰ environment steps.
- **Expected outcome**:
  - PQL should be initially more sample-efficient (off-policy advantage early in training).
  - SAPG should achieve higher or comparable asymptotic performance to PQL on both tasks.
  - PPO and DexPBT should underperform SAPG and PQL asymptotically.
  - SAPG should outperform PPO by a substantial margin on AllegroHand; comparable to PQL on ShadowHand.
- **Baselines**: PPO, DexPBT, PQL
- **Dependencies**: none

## E04: Ablation Study on SAPG Design Choices
- **Verifies**: C03, C05, C06
- **Setup**:
  - Model: SAPG variants (described below)
  - Hardware: Single GPU
  - Dataset: AllegroKuka Regrasping, Throw, Reorientation; ShadowHand; AllegroHand
  - System: N=24,576 parallel environments; M=6; 5 seeds
- **Procedure**:
  1. Train the following SAPG variants on all 5 tasks:
     - Standard SAPG (leader-follower, λ=1, 50/50 data split)
     - SAPG with entropy coef σ=0.003
     - SAPG with entropy coef σ=0.005
     - SAPG with high off-policy ratio (no subsampling, use full off-policy dataset)
     - SAPG without off-policy update (followers train independently, no aggregation)
     - Symmetric SAPG (each policy updated with all others' data)
  2. Plot learning curves for each variant across all 5 tasks.
  3. Compare final performance at 2×10¹⁰ steps.
- **Metrics**: Episode successes (AllegroKuka) or episode rewards (ShadowHand, AllegroHand) at 2×10¹⁰ steps.
- **Expected outcome**:
  - Without off-policy updates should be among the worst performing variants.
  - Symmetric aggregation should underperform leader-follower (policies converge, losing diversity).
  - High off-policy ratio should hurt performance on simpler tasks (noise drowns out on-policy gradient).
  - Entropy regularization (σ=0.005) should give the best performance on Reorientation (up to ~16.5% better than σ=0), but no clear benefit or marginal harm on Throw, Regrasping, AllegroHand.
- **Baselines**: Standard SAPG (reference point for comparing ablations)
- **Dependencies**: E02, E03

## E05: State Space Diversity Analysis (PCA and MLP Reconstruction)
- **Verifies**: C04
- **Setup**:
  - Model: SAPG, PPO, random policy (as baseline)
  - Hardware: Single GPU
  - Dataset: AllegroKuka Regrasping, Throw, Reorientation environments
  - System: Same N=24,576 environments as main experiments
- **Procedure**:
  1. Collect batches of states visited during training for SAPG, PPO, and a randomly initialized (untrained) policy.
  2. **PCA metric**: Compute PCA on the collected state batch. Plot reconstruction error (variance unexplained) vs. number of principal components k (ranging from 1 to ~66). Lower reconstruction error for the same k = lower intrinsic dimensionality = less diverse.
  3. **MLP metric**: Train small feedforward autoencoder networks (2 layers, hidden sizes ranging from 8 to 64 neurons, ReLU activation, Adam optimizer, L2 reconstruction loss) on each algorithm's state batch. Plot training reconstruction error vs. hidden layer size. Higher error = harder to compress = more diverse distribution.
  4. Compare curves for SAPG, PPO, and random policy.
- **Metrics**: (a) PCA reconstruction error as function of number of components; (b) MLP training reconstruction error as function of hidden layer dimension.
- **Expected outcome**:
  - SAPG should have higher PCA reconstruction error for small k (slower decrease) than PPO, indicating states span more principal components.
  - SAPG should have higher MLP reconstruction error than PPO across hidden layer sizes, indicating harder-to-compress state distribution.
  - Random policy baseline provides a lower bound (uniform exploration, should span many dimensions but not necessarily in a task-relevant way).
- **Baselines**: PPO, random policy
- **Dependencies**: E02

## E06: Entropy Coefficient Sensitivity Study
- **Verifies**: C06
- **Setup**:
  - Model: SAPG with σ ∈ {0, 0.003, 0.005}
  - Hardware: Single GPU
  - Dataset: All 6 tasks
  - System: N=24,576 environments; M=6; 5 seeds
- **Procedure**:
  1. For each task and each entropy coefficient σ ∈ {0, 0.003, 0.005}, train SAPG to 2×10¹⁰ steps.
  2. Report final performance and learning curves.
  3. Identify which σ works best per task.
- **Metrics**: Episode successes (AllegroKuka) or episode rewards (ShadowHand, AllegroHand).
- **Expected outcome**:
  - σ=0 should work best for AllegroHand, Regrasping, and Throw.
  - σ=0.005 should work best for ShadowHand and Reorientation.
  - Entropy benefit should correlate with task requiring more exploration of complex state spaces.
- **Baselines**: SAPG with σ=0 (no entropy)
- **Dependencies**: E02, E03
