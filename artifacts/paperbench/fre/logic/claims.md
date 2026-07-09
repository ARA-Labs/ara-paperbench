# Claims

## C01: FRE achieves competitive zero-shot performance across diverse reward families using only 32 samples
- **Statement**: An FRE agent pre-trained on a mixture of random unsupervised reward functions can solve novel downstream tasks in zero-shot by encoding 32 (state, reward) samples, achieving performance competitive with or better than methods using 5120 samples (FB, SF) and methods specialized for specific task types (GC-IQL, GC-BC, OPAL).
- **Status**: supported
- **Falsification criteria**: FRE performs statistically significantly worse than all baselines on a majority of evaluation tasks, or requires more than 32 samples to match baseline performance.
- **Proof**: [E01, E02]
- **Dependencies**: C02, C03
- **Tags**: zero-shot, evaluation, generalization, sample-efficiency

## C02: FRE outperforms SF/FB baselines on goal-reaching tasks despite using 160× fewer evaluation samples
- **Statement**: On goal-reaching evaluations (ant-goal-reaching, exorl-walker-goals, exorl-cheetah-goals, kitchen), FRE with K=32 encoding samples significantly outperforms SF and FB methods that use K=5120 samples, demonstrating that functional encoding is more sample-efficient than linear regression adaptation.
- **Status**: supported
- **Falsification criteria**: SF or FB achieve equal or higher scores on goal-reaching tasks when given 32 samples (matching FRE's budget).
- **Proof**: [E01]
- **Dependencies**: C01
- **Tags**: goal-reaching, sample-efficiency, comparison, successor-features

## C03: FRE generalizes to non-goal-reaching structured rewards while maintaining goal-reaching competitiveness
- **Statement**: The same FRE agent trained with the FRE-all mixture prior achieves competitive goal-reaching performance AND solves directional, simplex, and path tasks, whereas GC-IQL and GC-BC score near zero on non-goal-reaching tasks.
- **Status**: supported
- **Falsification criteria**: FRE performance on goal-reaching tasks is significantly lower than GC-IQL/GC-BC, OR FRE fails to improve on directional/simplex tasks relative to GC-IQL/GC-BC.
- **Proof**: [E01]
- **Dependencies**: C01
- **Tags**: generalization, multi-task, goal-reaching, directional

## C04: Performance scales smoothly with reward diversity; FRE-all dominates all reward-subset ablations
- **Statement**: An FRE agent trained on all three reward families (FRE-all) achieves the highest total score and competitive per-task scores compared to agents trained on any strict subset of reward families, demonstrating that disparate reward families can be jointly encoded without interference.
- **Status**: supported
- **Falsification criteria**: Any single-family agent (FRE-goals, FRE-lin, or FRE-mlp) outperforms FRE-all in total score, suggesting negative transfer from reward diversity.
- **Proof**: [E03]
- **Dependencies**: C01
- **Tags**: ablation, reward-diversity, scaling, generalization

## C05: Domain-specific reward priors (FRE-hint) further improve performance on targeted task distributions
- **Statement**: Augmenting the random reward prior with task-specific distributions (e.g., directional movement rewards for AntMaze, velocity rewards for ExORL) improves FRE performance on corresponding downstream tasks without requiring algorithmic changes.
- **Status**: supported
- **Falsification criteria**: FRE-hint does not improve over FRE-all on the targeted task types for which the domain knowledge was incorporated.
- **Proof**: [E04]
- **Dependencies**: C01, C04
- **Tags**: domain-knowledge, reward-prior, FRE-hint, multi-task
