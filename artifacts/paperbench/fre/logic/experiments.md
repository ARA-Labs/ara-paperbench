# Experiments

## E01: Main Zero-Shot Comparison on AntMaze, ExORL, and Kitchen
- **Verifies**: C01, C02, C03
- **Setup**:
  - Model: FRE (FRE-all prior), GC-IQL, GC-BC, FB, SF, OPAL
  - Hardware: Not specified in paper
  - Dataset: antmaze-large-diverse-v2 (D4RL), ExORL walker/cheetah RND, kitchen-complete-v0
  - System: FRE encoder training 150K steps (AntMaze) / 1M steps (ExORL/Kitchen); policy training 850K steps (AntMaze) / 1M steps (ExORL/Kitchen)
- **Procedure**:
  1. Load offline dataset for each domain (antmaze-large-diverse-v2, cheetah RND, walker RND, kitchen-complete-v0)
  2. Train FRE encoder-decoder using the FRE-all prior (uniform 1/3 mixture of goal, linear, MLP rewards) until convergence
  3. Freeze FRE encoder; train IQL policy conditioned on z for the remaining steps
  4. For each evaluation task, sample K=32 (state, reward) pairs and encode via frozen FRE encoder to obtain z
  5. Condition trained IQL policy on z; roll out for 2000 timesteps (AntMaze) or 1000 timesteps (ExORL)
  6. Average return over 20 episodes per seed, 5 seeds; normalize scores to [0, 100]
  7. Compare against FB (5120 eval samples), SF (5120 eval samples), GC-IQL, GC-BC, OPAL (10 skill rollouts per episode)
- **Metrics**: Normalized cumulative reward averaged over episodes and seeds; mean ± std across 5 seeds
- **Expected outcome**:
  - FRE significantly outperforms SF/FB baselines on goal-reaching tasks despite using far fewer evaluation samples
  - FRE achieves competitive scores relative to GC-IQL and GC-BC on goal-reaching tasks
  - FRE substantially outperforms GC-IQL and GC-BC on non-goal-reaching tasks (directional, simplex, path)
  - FRE overall average is higher than OPAL despite OPAL using privileged online rollouts for skill selection
- **Baselines**: FB (Touati & Ollivier 2021), SF (Barreto et al. 2017 + ICM features), GC-IQL (Kostrikov et al. 2021), GC-BC, OPAL (Ajay et al. 2020)
- **Dependencies**: none

## E02: Kitchen Zero-Shot Evaluation
- **Verifies**: C01, C02, C03
- **Setup**:
  - Model: FRE (FRE-all), GC-IQL, GC-BC, FB, SF, OPAL
  - Hardware: Not specified in paper
  - Dataset: kitchen-complete-v0 from D4RL
  - System: 7 evaluation subtasks (bottom-burner, kettle, light-switch, microwave, slide-cabinet, hinge-cabinet, top-burner); sparse rewards from D4RL Kitchen
- **Procedure**:
  1. Load kitchen-complete-v0 offline dataset; train all agents
  2. For FRE: train encoder-decoder 1M steps, then freeze and train IQL 1M steps
  3. At evaluation, encode each of the 7 kitchen sparse reward functions using K=32 samples
  4. Execute FRE-conditioned policy for each subtask for 20 episodes per seed, 5 seeds
  5. Average normalized cumulative reward across 7 subtasks
- **Metrics**: Normalized cumulative reward per subtask; average across 7 subtasks; mean ± std across 5 seeds
- **Expected outcome**:
  - FRE significantly outperforms GC-IQL and GC-BC on Kitchen despite Kitchen tasks being structured
  - FRE considerably outperforms OPAL (privileged) on Kitchen
  - FRE outperforms SF and FB baselines on Kitchen
- **Baselines**: GC-IQL, GC-BC, FB, SF, OPAL
- **Dependencies**: none

## E03: Reward Diversity Scaling Ablation (AntMaze)
- **Verifies**: C04
- **Setup**:
  - Model: FRE-all, FRE-goals, FRE-lin, FRE-mlp, FRE-lin-mlp, FRE-goal-mlp, FRE-goal-lin (7 variants)
  - Hardware: Not specified in paper
  - Dataset: antmaze-large-diverse-v2
  - System: Each agent receives the same total training budget; FRE-all has 1/3 as many goal-reaching samples as FRE-goals
- **Procedure**:
  1. Train 7 FRE agents, each with a different prior reward distribution (all subsets of {goal, linear, MLP})
  2. Keep all other hyperparameters identical (same total training budget)
  3. Evaluate each agent on AntMaze tasks: goal-reaching, directional, random-simplex, path-all
  4. Compute average total score across all tasks
  5. Compare per-task and total scores across all 7 variants
- **Metrics**: Normalized cumulative reward per task family; total score (average of all tasks); mean ± std across 5 seeds
- **Expected outcome**:
  - FRE-all achieves the highest total score among all 7 variants
  - FRE-all achieves competitive performance on each individual task (goal, directional, simplex, path)
  - FRE-goals achieves best goal-reaching score but fails on other tasks
  - FRE-lin achieves best directional score but fails on goal-reaching
  - No significant performance degradation from diversity (scaling is smooth)
- **Baselines**: Each FRE variant ablation serves as its own baseline
- **Dependencies**: E01

## E04: Domain Knowledge Augmentation (FRE-hint)
- **Verifies**: C05
- **Setup**:
  - Model: FRE-all (general), FRE-hint (domain-augmented)
  - Hardware: Not specified in paper
  - Dataset: antmaze-large-diverse-v2, ExORL cheetah/walker RND
  - System: FRE-hint augments the prior with domain-specific reward functions (directional rewards for AntMaze; velocity rewards for ExORL)
- **Procedure**:
  1. For AntMaze FRE-hint: augment prior with rewards corresponding to movement in unit (x,y) direction
  2. For ExORL FRE-hint (cheetah/walker): augment prior with velocity-based reward functions
  3. Train FRE-hint agent with augmented prior; evaluate on corresponding target tasks
  4. Compare FRE-hint vs. FRE-all on ant-directional, exorl-cheetah-velocity, exorl-walker-velocity
- **Metrics**: Normalized cumulative reward; mean ± std across 5 seeds
- **Expected outcome**:
  - FRE-hint outperforms FRE-all on the targeted task (directional, velocity) for which domain knowledge was provided
  - No algorithmic changes required; only the prior reward distribution changes
- **Baselines**: FRE-all
- **Dependencies**: E01

## E05: FRE Zero-Shot Generalization Visualization (AntMaze Qualitative)
- **Verifies**: C01
- **Setup**:
  - Model: FRE (FRE-all)
  - Hardware: Not specified in paper
  - Dataset: antmaze-large-diverse-v2
  - System: Various reward functions projected onto maze for visual inspection
- **Procedure**:
  1. Sample diverse reward functions from evaluation tasks (goal-reaching, directional, simplex)
  2. Visualize: (a) true reward heatmap, (b) random states used for encoding, (c) decoded reward prediction, (d) policy trajectory, (e) predicted value function
  3. Qualitatively assess whether the decoded reward matches the true reward and whether the policy trajectory maximizes value
- **Metrics**: Visual correspondence between true reward, decoded reward, policy behavior, and value function
- **Expected outcome**:
  - Decoder accurately reconstructs the reward function from 32 samples
  - Value function correctly captures expected returns from each position
  - Policy generally maximizes the value function; occasional failures in OOD states
- **Baselines**: none (qualitative)
- **Dependencies**: E01
