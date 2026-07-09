# Heuristics

## H01: Strided Training (Freeze Encoder Before Policy Training)
- **Rationale**: TD learning for multi-task Q-functions requires a stationary mapping from reward functions to latent vectors z. If the encoder is updated simultaneously with Q/V/π, the Q-function targets become non-stationary, leading to divergence or slow convergence.
- **Sensitivity**: high
- **Bounds**: Encoder must fully converge before policy training begins. Encoder training steps: 150K (AntMaze), 1M (ExORL/Kitchen).
- **Code ref**: [src/execution/fre.py]
- **Source**: Section 4.3, Algorithm 1

## H02: Reward Discretization into 32 Bins
- **Rationale**: Discretizing scalar rewards into discrete bins and embedding them via a learned embedding table provides richer representations than passing raw scalars to the transformer, enabling the encoder to learn nonlinear distinctions between reward magnitudes.
- **Sensitivity**: medium
- **Bounds**: 32 bins; rewards assumed in approximately [-1, 1]. Values clipped before binning.
- **Code ref**: [src/execution/fre.py]
- **Source**: Section 4.1 Practical Implementation; Rubric item 04d679d0

## H03: Sparse Binary Mask for Random Linear Rewards (p=0.9 zeroing)
- **Rationale**: Biasing the random linear prior toward sparse functions (most dimensions zeroed) encourages simpler, more interpretable reward functions that generalize better. A fully dense random vector in high-dimensional spaces would concentrate mass on less interpretable reward functions.
- **Sensitivity**: medium
- **Bounds**: Mask probability = 0.9 (each dimension zeroed with probability 0.9). Applied to all domains.
- **Code ref**: [src/execution/fre.py]
- **Source**: Section 4.2, Appendix B

## H04: Exclude XY Positions from Linear Rewards on AntMaze
- **Rationale**: The XY coordinate dimensions in AntMaze have different scale from other state dimensions, causing instability in random linear reward generation (rewards can be dominated by XY terms, reducing diversity).
- **Sensitivity**: medium
- **Bounds**: XY positions explicitly excluded from linear reward generation for AntMaze. Applied to antmaze-large-diverse-v2 only.
- **Code ref**: [src/execution/fre.py]
- **Source**: Appendix B

## H05: HER-Style Goal Sampling Distribution (0.2/0.5/0.3 split)
- **Rationale**: Using a mixture of current-state (0.2), future-trajectory (0.5), and fully-random (0.3) goals produces a diversity of goal-reaching difficulties and avoids goals that are trivially unreachable from training transitions.
- **Sensitivity**: low
- **Bounds**: Probabilities: current=0.2, future=0.5, random=0.3. Must ensure at least one encoder sample contains the goal state.
- **Code ref**: [src/execution/fre.py]
- **Source**: Appendix B; HER (Andrychowicz et al., 2017)

## H06: Discount Factor γ = 0.88 (Lower than Standard 0.99)
- **Rationale**: A lower discount factor is appropriate for the diverse multi-task offline setting, where long-horizon credit assignment across highly varied reward functions may lead to instability. Shorter effective horizons improve TD stability.
- **Sensitivity**: medium
- **Bounds**: γ = 0.88 for all domains and all tasks.
- **Code ref**: [src/execution/iql.py]
- **Source**: Appendix A, Table 3
