---
# Problem Specification

## Observations

### O1: GPU-driven simulation enables orders-of-magnitude more parallel environments
- **Statement**: GPU-based physics engines (IsaacGym, PhysX, MuJoCo 3.0) enable simulating tens of thousands of environments in parallel on a single GPU — two or more orders of magnitude beyond the ~100-128 environments PPO was originally developed for.
- **Evidence**: §1, §3; SAPG experiments run 24,576 parallel environments on a single GPU.
- **Implication**: RL algorithms should theoretically benefit greatly from these larger batches, but this benefit is not automatically realized.

### O2: PPO performance saturates beyond ~25,000 parallel environments
- **Statement**: Plotting PPO asymptotic performance vs. batch size (number of environments) shows a curve that flattens — performance stops improving and may degrade, despite higher simulation capacity being available.
- **Evidence**: Figure 2 (Shadow Hand and Allegro Kuka Throw); the dashed red line shows SAPG achieving higher performance, proving the ceiling is not inherent to the task.
- **Implication**: The bottleneck is not simulation capacity but the data utilization mechanism inside PPO.

### O3: IID sampling from a Gaussian policy yields redundant data at large scale
- **Statement**: When actions are sampled IID from a Gaussian policy across many environments, most sampled actions concentrate near the distribution mean. With hundreds of thousands of environments, many environments execute nearly identical actions, leading to duplicated experience.
- **Evidence**: §4 (motivation paragraph); mathematical reasoning from properties of Gaussian distributions.
- **Implication**: Increasing the number of parallel environments does not proportionally increase the diversity of collected experience.

### O4: On-policy methods achieve higher asymptotic performance than off-policy methods at scale
- **Statement**: Off-policy methods (PQL) are more sample-efficient early in training but plateau at lower asymptotic performance than on-policy methods on hard tasks; on-policy methods are better at latching onto high-reward trajectories.
- **Evidence**: Figure 5 (AllegroKuka tasks: PQL near zero, PPO near zero, but PBT/SAPG achieve high success); §6.2.
- **Implication**: A solution should preserve the on-policy property while increasing data diversity.

## Gaps

### G1: No mechanism for on-policy RL to exploit massive parallelism efficiently
- **Statement**: PPO and other standard on-policy RL algorithms have no principled way to use the diversity potential of thousands of parallel environments — they treat all environments as IID samples of a single policy.
- **Caused by**: O1, O2, O3
- **Existing attempts**: Simply increasing batch size proportional to environment count.
- **Why they fail**: Data redundancy prevents learning signal from growing proportionally; performance saturates (O2).

### G2: Population-based training (DexPBT) wastes data from sub-optimal policies
- **Statement**: DexPBT divides environments across multiple policies and uses hyperparameter mutation to find good policies, but data from "worse" policies is discarded — only the best policy's weights are propagated.
- **Caused by**: O1, O3
- **Existing attempts**: DexPBT [24] — population-based training with hyperparameter mutation.
- **Why they fail**: Data from policies that found high-reward trajectories but with sub-optimal hyperparameters is lost; each policy is only updated on its own data.

### G3: Off-policy importance sampling historically impractical for on-policy methods
- **Statement**: While importance sampling (IS) can in principle allow use of off-policy data in policy gradient methods, it has been avoided in practice because with limited compute it is better to use fully on-policy data, and IS estimates can be high variance.
- **Caused by**: O3
- **Existing attempts**: Off-policy actor-critic [5], IMPALA [6], P3O [7].
- **Why they fail**: In the small-scale setting, the cost of diversity does not outweigh variance reduction. In large-scale settings this trade-off reverses.

## Key Insight

- **Insight**: In the large-scale GPU simulation setting, enough on-policy data is available that it becomes beneficial to deliberately diversify beyond IID sampling by running multiple policies concurrently and aggregating their data via importance-sampled off-policy updates — the diversity benefit outweighs the IS variance cost.
- **Derived from**: O1, O2, O3, O4
- **Enables**: The SAPG leader-follower framework where a single "leader" policy is updated using its own on-policy data plus importance-sampled data from M−1 "follower" policies running on separate environment blocks, each with different exploration behavior enforced via entropy regularization.

## Assumptions

- A1: GPU-accelerated simulation provides sufficient parallelism (≥10k environments) for SAPG's diversity mechanism to matter.
- A2: The importance sampling ratio is well-behaved (bounded) because follower policies share a backbone with the leader, staying within a reasonable "trust region."
- A3: Off-policy 1-step critic targets are a sufficient approximation for the follower trajectories (exact n-step returns are only used for the on-policy leader data).
- A4: Asymptotic performance is the primary metric of interest; sample efficiency is secondary (data is cheap at scale).
- A5: A fixed reward function is used (unlike DexPBT which mutates reward scales); SAPG must achieve good performance under this constraint.
