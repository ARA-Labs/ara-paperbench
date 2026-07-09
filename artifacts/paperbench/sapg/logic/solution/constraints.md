---
# Constraints and Limitations

## Boundary Conditions

### BC1: Minimum environment count requirement
- **Condition**: SAPG's benefit over PPO requires N >> typical RL batch sizes.
- **Threshold**: The paper demonstrates benefit at N = 24,576 (approximately 2 orders of magnitude above PPO's original design of ~128 environments). Performance saturation was observed at ~25,000 for PPO.
- **Failure mode**: At small N (e.g., N ≤ 1,000), SAPG overhead (multiple policies, importance sampling variance) likely outweighs benefits; standard PPO is preferred.

### BC2: Importance sampling validity
- **Condition**: Off-policy correction μ = πi,old/πj is only valid when the policies are sufficiently close (bounded ratio).
- **Design mitigation**: Shared backbone θ between leader and followers keeps all policies within a similar region of policy space, preventing extreme IS ratios.
- **Failure mode**: If followers diverge too far from the leader (e.g., very large entropy coefficients), IS weights become extreme and destabilize training.

### BC3: Fixed reward function assumption
- **Condition**: SAPG optimizes a fixed reward function, unlike DexPBT which can mutate reward scales.
- **Implication**: SAPG cannot benefit from curriculum-style reward shaping that DexPBT uses. Despite this constraint, SAPG outperforms DexPBT on most tasks.
- **Note**: The success tolerance curriculum (regrasping δ from 7.5cm to 1cm) is part of the environment, not the RL algorithm.

### BC4: Off-policy ratio sensitivity
- **Condition**: Using all off-policy data (no subsampling) without equal 50/50 split degrades performance on simpler tasks.
- **Threshold**: Equal on/off-policy data ratio (λ=1 with subsampling) is the recommended setting.
- **Failure mode**: High off-policy ratio floods the gradient with noisy off-policy signal, drowning the more reliable on-policy gradient.

### BC5: Task-dependent entropy coefficient
- **Condition**: The optimal entropy coefficient σ depends on task difficulty and required exploration.
- **Values**: σ=0 for AllegroHand, Regrasping, Throw; σ=0.005 for ShadowHand and Reorientation.
- **Failure mode**: Using σ=0.005 on simpler tasks (e.g., AllegroHand) degrades performance — excessive exploration in tasks where refinement is more important is harmful.

### BC6: Symmetric aggregation failure mode
- **Condition**: If all M policies are updated with all others' data (symmetric), they converge in behavior.
- **Result**: Once policies execute identical actions, the benefit of data diversity is lost and SAPG reduces to vanilla PPO with unnecessary overhead.
- **Design mitigation**: Leader-follower asymmetry is essential to maintain diversity.

## Known Limitations

### L1: Wall-clock time not directly comparable
- The paper runs experiments on different machines; wall-clock time is not reported. Only sample count (number of environment steps) is used for comparison. Actual training takes ~48-60 hours on a single GPU.

### L2: Two Arms Reorientation missing PQL/SAPG(λ=0) results
- Table 1 does not report PQL and SAPG(λ_ent=0) results for Two Arms Reorientation (entries marked as "-"). This likely indicates these variants failed to achieve meaningful performance, but exact values are not provided.

### L3: No multi-GPU scaling results
- The paper focuses on single-GPU performance. Multi-GPU scaling (across multiple IsaacGym instances) is not evaluated.

### L4: LSTM sequence length and mini-epoch values not fully specified
- The hyperparameter tables in the appendix have some missing values (notably horizon length, LSTM sequence length, mini epochs) that appear blank in the published paper. The paper states "16 steps of experience per instance" for horizon length.

### L5: M=6 fixed without thorough ablation
- The number of policies M=6 is used throughout but not ablated. Optimal M may vary by task.

### L6: Limited to continuous action spaces
- The algorithm uses Gaussian policies, making it applicable to continuous control tasks. Discrete action domains are not addressed.
