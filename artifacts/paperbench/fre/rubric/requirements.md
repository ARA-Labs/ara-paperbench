# Rubric Requirements — fre
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 437

## Dataset and Model Acquisition

### R01: Code has been implemented such that the `antmaze-large-diver...
- **Rubric ID**: 595c44a3-25a3-4f38-80d1-d3376b12476e
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code has been implemented such that the `antmaze-large-diverse-v2` dataset from D4RL can be used for offline training of sequential decision making agents
- **Parent context**: The AntMaze dataset and environment have been setup

### R02: Code has been implemented such that the "kitchen-complete-v0...
- **Rubric ID**: 4eb72ad4-06cc-48ee-891f-a3851d850ea0
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code has been implemented such that the "kitchen-complete-v0" dataset from D4RL can be used for offline training of sequential decision making agents
- **Parent context**: The Kitchen dataset and environment have been setup

## Evaluation, Metrics & Benchmarking

### R03: Code has been implemented such that the D4RL Ant Maze enviro...
- **Rubric ID**: 5b3ccceb-d946-4ce3-96f1-6cb9c3ef8030
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the D4RL Ant Maze environment (https://github.com/Farama-Foundation/D4RL/blob/71a9549f2091accff93eeff68f1f3ab2c0e0a288/d4rl/locomotion/ant.py or equivalent) can be used for online evaluation of sequential decision making agents
- **Parent context**: The AntMaze dataset and environment have been setup

### R04: Code has been implemented such that environments from the `c...
- **Rubric ID**: 15a0dc98-8a9f-4173-a7a0-ba07770200f2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that environments from the `cheetah` domain from the custom DeepMind Control Suite ExORL environments (https://github.com/denisyarats/exorl/tree/main/custom_dmc_tasks) can be used for online evaluation of sequential decision making agents
- **Parent context**: The ExORL `cheetah` (RND) dataset and environment has been setup

### R05: Code has been implemented such that environments from the `w...
- **Rubric ID**: 534f0b86-f31e-4b6e-8bc3-50159bfdd0a3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that environments from the `walker` domain from custom DeepMind Control Suite ExORL environments (https://github.com/denisyarats/exorl/tree/main/custom_dmc_tasks) can be used for online evaluation of sequential decision making agents
- **Parent context**: The ExORL `walker` (RND) dataset and environment has been setup

### R06: Code has been implemented such that the D4RL Kitchen environ...
- **Rubric ID**: 190df881-45b2-409f-a204-e924be3eab79
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the D4RL Kitchen environment (https://github.com/Farama-Foundation/D4RL/tree/71a9549f2091accff93eeff68f1f3ab2c0e0a288/d4rl/kitchen or equivalent) can be used for online evaluation of sequential decision making agents
- **Parent context**: The Kitchen dataset and environment have been setup

### R07: Code has been implemented such that evaluation can be repeat...
- **Rubric ID**: 244667bf-831a-4d38-a8d0-18547ddb8189
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that evaluation can be repeated and averaged over twenty (20) episodes
- **Parent context**: The necessary evaluation has been run

### R08: Code has been implemented such that each evaluation can be r...
- **Rubric ID**: 6697fcce-1f11-4431-8221-ce30cc6154fe
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that each evaluation can be repeated and averaged over five (5) seeds, where each seed corresponds to multiple episodes being evaluated.
- **Parent context**: The necessary evaluation has been run

### R09: Code has been implemented such that when evaluating a FRE ag...
- **Rubric ID**: e3e36e0a-d276-4726-9e22-8754eb9f799a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that when evaluating a FRE agent, 32 state-reward pairs are sampled the from the evaluation task environment and passed through the corresponding FRE encoder to obtain the latent z for policy conditioning.
- **Parent context**: Code has been implemented for evaluating FRE agents

### R10: Code has been implemented such that, for evaluating a FRE ag...
- **Rubric ID**: c48319bf-ee1b-40e7-b5a8-54d124e8dca3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that, for evaluating a FRE agent, the z latent produced by the FRE encoder is used to condition a pre-trained implicit Q-learning policy.
- **Parent context**: Code has been implemented for evaluating FRE agents

### R11: Code has been implemented such that an agent pretrained via...
- **Rubric ID**: 7a33ccdc-e0c6-4da8-a392-9f9455bbbfc3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an agent pretrained via FRE can be evaluated on target tasks
- **Parent context**: Code has been implemented for evaluating FRE agents

### R12: Code has been implemented such that FB agents can be evaluat...
- **Rubric ID**: 0169f82d-aef1-4700-97b4-1a761fe4e633
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that FB agents can be evaluated using the https://github.com/facebookresearch/controllable_agent codebase or a fork of it
- **Parent context**: Code has been implemented for evaluating the necessary agent architectures

### R13: Code has been implemented such that SF agents can be evaluat...
- **Rubric ID**: c0b275fd-272b-4656-8895-206808a35713
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that SF agents can be evaluated using the https://github.com/facebookresearch/controllable_agent codebase or a fork of it
- **Parent context**: Code has been implemented for evaluating the necessary agent architectures

### R14: Code has been implemented such that, for evaluating OPAL age...
- **Rubric ID**: 8024564e-c86d-48ed-ad23-76553c6b350a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that, for evaluating OPAL agents, for a given episode, 10 random OPAL skills can be sampled from a unit gaussian.
- **Parent context**: Code has been implemented for evaluating OPAL agents

### R15: Code has been implemented such that, for evaluating OPAL age...
- **Rubric ID**: fac710db-d53e-4001-bdf2-8aed198f978d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that, for evaluating OPAL agents, for a given episode, the agent is evaluated on the target task separately conditioning on each skill sampled from the unit gaussian
- **Parent context**: Code has been implemented for evaluating OPAL agents

### R16: Code has been implemented such that, for evaluating OPAL age...
- **Rubric ID**: 2e132b5f-15a0-4774-9b6f-6e2538c5ef9f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that, for evaluating OPAL agents, for a given episode, the performance is taken to be the best performance across the 10 sampled skills for that episode.
- **Parent context**: Code has been implemented for evaluating OPAL agents

### R17: Code has been implemented such that an agent pretrained via...
- **Rubric ID**: c2300ee7-b5ac-4b80-a92f-276a7fdf4d2b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an agent pretrained via OPAL can be evaluated on target tasks
- **Parent context**: Code has been implemented for evaluating OPAL agents

### R18: Code has been implemented such that an agent pretrained via...
- **Rubric ID**: 93fa32e7-593d-4632-96a2-cff95ceedb47
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an agent pretrained via GC-BC can be evaluated on target goal-reaching tasks
- **Parent context**: Code has been implemented for evaluating GC-BC agents

### R19: Code has been implemented such that an agent pretrained via...
- **Rubric ID**: 24c19136-2671-489d-88b9-6a203e7df7e1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an agent pretrained via GC-IQL can be evaluated on target goal-reaching tasks tasks
- **Parent context**: Code has been implemented for evaluating GC-IQL agents

### R20: Code has been implemented such that when evaluating GC-IQL a...
- **Rubric ID**: d079bcac-1277-4ae5-933f-f3ccb9e28453
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that when evaluating GC-IQL agents, the goal state is made available to the agent at the beginning of the rollout
- **Parent context**: Code has been implemented for evaluating GC-IQL agents

### R21: Code has been implemented such that Ant Maze tasks are evalu...
- **Rubric ID**: e07c5e86-6c2c-4610-8d97-44531cbfaa06
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that Ant Maze tasks are evaluated online, i.e. the agent to evaluate and environment are instantiated and the agent acts in the environment
- **Parent context**: The necessary agents have been evaluated on the Ant Maze evaluation tasks

### R22: The `ant-goal-reaching` evaluation task has been implemented...
- **Rubric ID**: 66e8abac-44b0-4a9f-8975-8c3e23f44889
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `ant-goal-reaching` evaluation task has been implemented such that the agent is evaluated on the 5 reward functions outlined in addendum.md
- **Parent context**: The `ant-goal-reaching` evaluation task has been implemented as outlined in addendum.md and Appendix...

### R23: The `ant-goal-reaching` evaluation task has been implemented...
- **Rubric ID**: d9bf8c02-ce28-4005-87e9-913791e71807
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `ant-goal-reaching` evaluation task has been implemented such that the average cumulative reward across the 5 reward functions is used as the evaluation metric
- **Parent context**: The `ant-goal-reaching` evaluation task has been implemented as outlined in addendum.md and Appendix...

### R24: The `ant-goal-reaching` evaluation task has been implemented...
- **Rubric ID**: f5dc7467-50c8-46a1-ba2d-0ae10b43b9a0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `ant-goal-reaching` evaluation task has been implemented such that the goal is considered reached if an agent reaches within a distance of 2 from the target position.
- **Parent context**: The `ant-goal-reaching` evaluation task has been implemented as outlined in addendum.md and Appendix...

### R25: The `ant-goal-reaching` evaluation task has been implemented...
- **Rubric ID**: f4430c7e-445c-4492-bdd7-1cb1f766999f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `ant-goal-reaching` evaluation task has been implemented such that the agent receives a reward of -1 at each timestep until it successfully reaches the goal.
- **Parent context**: The `ant-goal-reaching` evaluation task has been implemented as outlined in addendum.md and Appendix...

### R26: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: ca9b0276-199e-45ec-9483-058caa982237
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-all can been evaluated on `ant-goal-reaching`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R27: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: d21d6d68-6dff-4eb6-80db-d4bbbfc7aa77
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-all has been evaluated over 5 seeds with 20 episodes per seed on `ant-goal-reaching`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R28: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: c9462682-e03b-4d73-81db-8134eafd600d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goals can been evaluated on `ant-goal-reaching`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R29: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 116f3620-7d86-4ed8-a7dd-e128f882c971
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goals has been evaluated over 5 seeds with 20 episodes per seed on `ant-goal-reaching`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R30: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 1f185bff-60dc-4033-9391-20b2824f02b8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin can been evaluated on `ant-goal-reaching`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R31: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: fdb27e83-9219-4995-a500-6f894b19c095
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin has been evaluated over 5 seeds with 20 episodes per seed on `ant-goal-reaching`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R32: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 3424489d-558d-4c6a-96ef-103b94526b1d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-mlp can been evaluated on `ant-goal-reaching`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R33: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 813a726d-fc10-4917-9af6-9d3da77f037a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-goal-reaching`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R34: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 406f3c3a-d123-4967-a0ea-2958f12300ab
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin-mlp can been evaluated on `ant-goal-reaching`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R35: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 0493ce85-421b-45b2-a53e-f8377110f667
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-goal-reaching`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R36: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 35803a76-441e-445e-a97f-0d8fd80d6353
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-mlp can been evaluated on `ant-goal-reaching`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R37: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 4d92c43b-7dae-4383-b1fb-314cb120cb98
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-goal-reaching`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R38: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: b3577421-5b7c-4889-875d-a82b188dce8e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-lin can been evaluated on `ant-goal-reaching`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R39: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 79652880-b782-4fca-bbff-b52a55d13fcd
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-lin has been evaluated over 5 seeds with 20 episodes per seed on `ant-goal-reaching`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R40: Code has been implemented such that an FB agent trained on `...
- **Rubric ID**: fa867daf-5b7c-44b9-8400-64fc4043fbda
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an FB agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-goal-reaching`
- **Parent context**: An FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R41: Code has been executed such that an FB agent trained on `ant...
- **Rubric ID**: 599da9c6-ab0f-43c4-a432-ce71d842b02f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-goal-reaching`
- **Parent context**: An FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R42: Code has been implemented such that an SF agent trained on `...
- **Rubric ID**: becd59d0-28dc-4be6-8496-6abd3ffd0ebd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an SF agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-goal-reaching`
- **Parent context**: An SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R43: Code has been executed such that an SF agent trained on `ant...
- **Rubric ID**: 3979ee05-5dc7-4691-8eb8-434b5fc65c48
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-goal-reaching`
- **Parent context**: An SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R44: Code has been implemented such that an OPAL agent trained on...
- **Rubric ID**: eab067af-c526-431d-b1e8-4a08f06b9e53
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an OPAL agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-goal-reaching`
- **Parent context**: An OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes...

### R45: Code has been executed such that an OPAL agent trained on `a...
- **Rubric ID**: b1395b9e-7452-4fe1-a4e6-73b7e8f35a5d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-goal-reaching`
- **Parent context**: An OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes...

### R46: Code has been implemented such that an GC-IQL agent trained...
- **Rubric ID**: 57058927-33c6-413b-a38a-b74428a85074
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an GC-IQL agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-goal-reaching`
- **Parent context**: A GC-IQL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episode...

### R47: Code has been executed such that an GC-IQL agent trained on...
- **Rubric ID**: f1df89e5-a4f0-4c58-aa76-dca210459be9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an GC-IQL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-goal-reaching`
- **Parent context**: A GC-IQL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episode...

### R48: Code has been implemented such that a GC-BC agent trained on...
- **Rubric ID**: 6bc39ee5-f085-4f4f-9619-6bd2d7063a00
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a GC-BC agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-goal-reaching`
- **Parent context**: A GC-BC agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes...

### R49: Code has been executed such that a GC-BC agent trained on `a...
- **Rubric ID**: fe30a1f7-dd62-4b98-bc6d-90aa7afa3825
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a GC-BC agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-goal-reaching`
- **Parent context**: A GC-BC agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes...

### R50: The `ant-directional` evaluation task has been implemented s...
- **Rubric ID**: 53a057fc-5ffd-4e73-8a7c-02aa42696f48
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `ant-directional` evaluation task has been implemented such that the agent is evaluated on the 4 reward functions outlined in addendum.md
- **Parent context**: The `ant-directional` evaluation task has been implemented as outlined in addendum.md

### R51: The `ant-directional` evaluation task has been implemented s...
- **Rubric ID**: e6193543-b632-4855-853e-40f64e39b1fe
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `ant-directional` evaluation task has been implemented such that the average cumulative reward across the 4 reward functions is used as the evaluation metric
- **Parent context**: The `ant-directional` evaluation task has been implemented as outlined in addendum.md

### R52: The `ant-directional` evaluation task has been implemented s...
- **Rubric ID**: 68f27cfa-dd32-4bf1-9062-904f70b929ad
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `ant-directional` evaluation task has been implemented such the reward is scaled by how much the agent's velocity aligns with the target direction, utilizing a dot product.
- **Parent context**: The `ant-directional` evaluation task has been implemented as outlined in addendum.md

### R53: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 448f277f-d512-44c2-8525-c01c6e0ca803
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-all can been evaluated on `ant-directional`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R54: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 32f02dcc-bff3-43a7-92e4-aa831cd4d35d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-all has been evaluated over 5 seeds with 20 episodes per seed on `ant-directional`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R55: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 474b4b95-7317-4987-aac5-d489853562ea
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-hint can been evaluated on `ant-directional`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R56: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 19d94a96-5dce-486b-85fa-ea0be685fe85
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-hint has been evaluated over 5 seeds with 20 episodes per seed on `ant-directional`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R57: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 52e140d7-ea50-4057-b624-5d558af8ec93
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goals can been evaluated on `ant-directional`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R58: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: b05ece5e-7867-4867-ae0d-6efadd9e596c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goals has been evaluated over 5 seeds with 20 episodes per seed on `ant-directional`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R59: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 099200fd-9f2c-4202-9dd7-7dcf50122f2f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin can been evaluated on `ant-directional`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R60: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: ad275ec2-4fb6-47e0-9b6d-8f20e8df9d60
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin has been evaluated over 5 seeds with 20 episodes per seed on `ant-directional`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R61: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 71b720f2-1787-4940-b8be-ba7ae5c64c48
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-mlp can been evaluated on `ant-directional`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R62: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 16e1778f-88ec-4050-a7cf-841be12a6bd2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-directional`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R63: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 172274db-cd1f-40b5-a3a1-cfede0780664
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin-mlp can been evaluated on `ant-directional`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R64: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 4de68bc0-fc38-4052-b0ac-521a9893f488
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-directional`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R65: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 40b673b0-0638-4d93-8be7-f20b8aac6cad
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-mlp can been evaluated on `ant-directional`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R66: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 9e6051ed-5185-4e9e-a9fe-4b1538310a24
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-directional`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R67: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 5532df06-3a7b-4a47-9306-f7ef6bb77208
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-lin can been evaluated on `ant-directional`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R68: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 3f2d0ba9-ed70-408d-b395-e8f3eb846624
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-lin has been evaluated over 5 seeds with 20 episodes per seed on `ant-directional`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R69: Code has been implemented such that an FB agent trained on `...
- **Rubric ID**: 3587539b-7f64-49b5-b3bf-8201548f4775
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an FB agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-directional`
- **Parent context**: An FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R70: Code has been executed such that an FB agent trained on `ant...
- **Rubric ID**: e1e1ed7f-fedb-4ec9-b30a-b6be0f853d38
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-directional`
- **Parent context**: An FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R71: Code has been implemented such that an SF agent trained on `...
- **Rubric ID**: 7e63b8ff-7d60-4113-9ae6-5238d01bdbe0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an SF agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-directional`
- **Parent context**: An SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R72: Code has been executed such that an SF agent trained on `ant...
- **Rubric ID**: 56c078eb-5e16-4a6c-bcbf-3c8cf842d1cd
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-directional`
- **Parent context**: An SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R73: Code has been implemented such that an OPAL agent trained on...
- **Rubric ID**: c41d6c2c-6809-43e3-876c-15988826703f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an OPAL agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-directional`
- **Parent context**: An OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes...

### R74: Code has been executed such that an OPAL agent trained on `a...
- **Rubric ID**: 31143ebe-3946-4f45-a6f1-c17f6a252265
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-directional`
- **Parent context**: An OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes...

### R75: The `ant-random-simplex` evaluation task has been implemente...
- **Rubric ID**: 8a6209c8-4cb5-4e2f-8401-64089b88b171
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `ant-random-simplex` evaluation task has been implemented such that the agent is evaluated on the 5 seeded opensimplex height and velocity preferences as outlined in addendum.md
- **Parent context**: The `ant-random-simplex` evaluation task has been implemented as outlined in addendum.md

### R76: The `ant-random-simplex` evaluation task has been implemente...
- **Rubric ID**: 2ff868ca-cb09-4867-8ba2-46340e1039a2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `ant-random-simplex` evaluation task has been implemented such that the average cumulative reward across the 5 seeded tasks is used as the evaluation metric
- **Parent context**: The `ant-random-simplex` evaluation task has been implemented as outlined in addendum.md

### R77: The `ant-random-simplex` evaluation task has been implemente...
- **Rubric ID**: 60cad4b9-d5ae-46ee-a6a9-dd7f8f6c89b7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `ant-random-simplex` evaluation task has been implemented such the agent gets baseline negative reward (-1) at each step, a bonus if it stands in higher 'height' regions, and an additional bonus for moving in the local 'preferred' velocity direction indicated by the noise field.
- **Parent context**: The `ant-random-simplex` evaluation task has been implemented as outlined in addendum.md

### R78: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 2839bbbb-e381-4cae-8100-998b50f220f0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-all can been evaluated on `ant-random-simplex`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R79: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: b738bad3-4d91-4029-8005-dcf9cd7cb2ea
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-all has been evaluated over 5 seeds with 20 episodes per seed on `ant-random-simplex`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R80: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: d1b9d52c-9a8b-464d-b7fc-1f66dd079e4c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goals can been evaluated on `ant-random-simplex`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R81: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 0810257e-aff0-4aca-815a-80761e346e2b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goals has been evaluated over 5 seeds with 20 episodes per seed on `ant-random-simplex`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R82: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 3377b462-0b2f-4d2b-a819-8d38f08cfcd2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin can been evaluated on `ant-random-simplex`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R83: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 8de00d0e-55ac-4112-ad30-06e22470457f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin has been evaluated over 5 seeds with 20 episodes per seed on `ant-random-simplex`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R84: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: d430077d-68c8-4869-9f1d-7ff1989ada70
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-mlp can been evaluated on `ant-random-simplex`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R85: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 1b1bb40a-180f-4c76-8724-1416e00b8c81
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-random-simplex`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R86: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 18ed0467-9ef8-4ba2-b9fc-560ed3cc88cf
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin-mlp can been evaluated on `ant-random-simplex`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R87: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 6ac8e446-6758-4374-997b-3cb030b5ba31
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-random-simplex`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R88: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 201ad6e9-c09b-474b-90cd-cdb65bd69491
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-mlp can been evaluated on `ant-random-simplex`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R89: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: ccadbc78-e6b1-4124-91ba-a03529bcd13a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-random-simplex`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R90: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 4c731f80-30f2-4371-8b7b-3eeba5d66ab6
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-lin can been evaluated on `ant-random-simplex`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R91: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: c3d92133-77da-4676-ae89-5c30633d0433
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-lin has been evaluated over 5 seeds with 20 episodes per seed on `ant-random-simplex`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R92: Code has been implemented such that an FB agent trained on `...
- **Rubric ID**: 2da828b8-831b-4ec4-b093-2a2094c0add3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an FB agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-random-simplex`
- **Parent context**: An FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R93: Code has been executed such that an FB agent trained on `ant...
- **Rubric ID**: 3ed0cb01-b80f-41a6-924d-68f4df2bfa0c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-directional`
- **Parent context**: An FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R94: Code has been implemented such that an SF agent trained on `...
- **Rubric ID**: 0843355d-de6c-46f2-805a-f241b92265bb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an SF agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-random-simplex`
- **Parent context**: An SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R95: Code has been executed such that an SF agent trained on `ant...
- **Rubric ID**: c3c7b10d-e1ce-468b-87b4-2b5562b9753d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-random-simplex`
- **Parent context**: An SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R96: Code has been implemented such that an OPAL agent trained on...
- **Rubric ID**: e2afb0ab-77d2-48ef-bc80-db13d6f87c85
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an OPAL agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-random-simplex`
- **Parent context**: An OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes...

### R97: Code has been executed such that an OPAL agent trained on `a...
- **Rubric ID**: 51faccc9-4564-4ecd-92c4-dce51c619138
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-random-simplex`
- **Parent context**: An OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes...

### R98: The `ant-path-center` evaluation task has been implemented a...
- **Rubric ID**: 2c3f2517-10b4-4a39-bda7-3984790987a7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The `ant-path-center` evaluation task has been implemented as outlined in addendum.md
- **Parent context**: The necessary agents have been evaluated on the `ant-path-center` evaluation task

### R99: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 42a4428a-2309-4ecb-a832-a6de7c6c6667
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-all can been evaluated on `ant-path-center`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R100: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 069e26a9-f025-4dd1-b587-cdad05e82d1e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-all has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-center`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R101: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: b1e109c5-768a-41b5-aa9c-b406b3c875e1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goals can been evaluated on `ant-path-center`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R102: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 1b0ef2bb-0e39-4c70-853e-816f4e10d429
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goals has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-center`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R103: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 9128e117-2ae5-4011-871a-029e14d46db2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin can been evaluated on `ant-path-center`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R104: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: d4dcc933-61a3-4af3-aae0-962430b6c15f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-center`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R105: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: c58a7007-5978-4dd9-8da2-733474eb6f6f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-mlp can been evaluated on `ant-path-center`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R106: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: b3a4a1c3-ceb4-4b3c-ba5e-22f67210609a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-center`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R107: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 4bae6b40-8d28-41ec-8d7e-663a54175960
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin-mlp can been evaluated on `ant-path-center`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R108: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: d044f326-1ab1-4aa5-8f3d-2795fcda2d64
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-center`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R109: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: fd65d129-1bc4-4da2-8986-3efa5d3a72cd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-mlp can been evaluated on `ant-path-center`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R110: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: c7ca7150-7e34-4251-8fc5-e731020a8d26
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-center`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R111: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: fad601e1-0c67-4b47-99d4-7acfe6453219
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-lin can been evaluated on `ant-path-center`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R112: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: ab275099-337d-4693-86e4-71ef8dc784af
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-lin has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-center`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R113: Code has been implemented such that an FB agent trained on `...
- **Rubric ID**: a23d0d26-a12a-46c7-b741-706d6cbc6753
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an FB agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-path-center`
- **Parent context**: An FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R114: Code has been executed such that an FB agent trained on `ant...
- **Rubric ID**: 208a3900-8429-4542-acfb-0e0dc771948d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-directional`
- **Parent context**: An FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R115: Code has been implemented such that an SF agent trained on `...
- **Rubric ID**: b1978052-7248-43e1-b2fc-0bf002e9e104
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an SF agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-path-center`
- **Parent context**: An SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R116: Code has been executed such that an SF agent trained on `ant...
- **Rubric ID**: cb6cf3a6-8e4c-42fb-bb9a-7a9d28b753eb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-center`
- **Parent context**: An SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R117: Code has been implemented such that an OPAL agent trained on...
- **Rubric ID**: f55032a4-8fdf-42c3-bd20-965c1251e206
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an OPAL agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-path-center`
- **Parent context**: An OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes...

### R118: Code has been executed such that an OPAL agent trained on `a...
- **Rubric ID**: d48e1545-f0d6-4355-b55c-9576491052bd
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-center`
- **Parent context**: An OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes...

### R119: The `ant-path-loop` evaluation task has been implemented as...
- **Rubric ID**: 8a61c6b3-2e7c-445a-8f92-e9bee61d5735
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The `ant-path-loop` evaluation task has been implemented as outlined in addendum.md
- **Parent context**: The necessary agents have been evaluated on the `ant-path-loop` evaluation task

### R120: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: f83bcd10-6d64-4681-8a08-b5ae823239c1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-all can been evaluated on `ant-path-loop`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R121: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 58b77f28-5fd8-42a7-b623-67cb5cb583de
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-all has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-loop`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R122: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 71cabbee-4b99-494c-bc68-2fcd4fde9c3b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goals can been evaluated on `ant-path-loop`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R123: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: acf4e73f-9f48-4868-8106-cc50a042544f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goals has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-loop`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R124: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: a4929297-e3df-4c5e-bc39-9aadce85309c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin can been evaluated on `ant-path-loop`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R125: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: a02d8fb3-587f-449f-9d20-16da975b3303
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-loop`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R126: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 6da729f0-398f-4c28-90f5-e570f318a4b7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-mlp can been evaluated on `ant-path-loop`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R127: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 444792aa-8de9-4806-8034-b54271e8367b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-loop`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R128: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: a2146a9c-d5cf-44b6-bf50-6c65f0213cb6
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin-mlp can been evaluated on `ant-path-loop`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R129: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 4d7ce037-a59d-498d-a5ea-4b5552d5d9b5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-loop`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R130: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 7b8d648c-d256-42f3-a95a-65278333437c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-mlp can been evaluated on `ant-path-loop`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R131: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: c313d0d9-90f0-428f-8b7f-3bf2ffe8c6a0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-loop`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R132: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 172583d7-a2e5-445c-a05f-1108f7b6a92a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-lin can been evaluated on `ant-path-loop`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R133: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: eab3ad1d-03b7-48c6-8ceb-16d18a3fd288
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-lin has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-loop`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R134: Code has been implemented such that an FB agent trained on `...
- **Rubric ID**: 9c0ec0c7-2558-403c-8d06-01ddf9f188ec
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an FB agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-path-loop`
- **Parent context**: An FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R135: Code has been executed such that an FB agent trained on `ant...
- **Rubric ID**: 46dd6087-a973-4b8e-99c3-b1719c231971
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-directional`
- **Parent context**: An FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R136: Code has been implemented such that an SF agent trained on `...
- **Rubric ID**: 48b5fc95-9e8b-467c-827c-4ea77366d642
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an SF agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-path-loop`
- **Parent context**: An SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R137: Code has been executed such that an SF agent trained on `ant...
- **Rubric ID**: 0d565a3e-dfc3-4194-bca7-eadc9fcb946d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-loop`
- **Parent context**: An SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R138: Code has been implemented such that an OPAL agent trained on...
- **Rubric ID**: 18d94c00-8ae3-4817-bfc1-c738121f1fe1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an OPAL agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-path-loop`
- **Parent context**: An OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes...

### R139: Code has been executed such that an OPAL agent trained on `a...
- **Rubric ID**: 16905fa3-99bf-4659-bc25-4c994a4a1a64
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-loop`
- **Parent context**: An OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes...

### R140: The `ant-path-edges` evaluation task has been implemented as...
- **Rubric ID**: f488ec49-0d0f-450f-84d6-e417da5481e7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The `ant-path-edges` evaluation task has been implemented as outlined in addendum.md
- **Parent context**: The necessary agents have been evaluated on the `ant-path-edges` evaluation task

### R141: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 7563ccd1-a6b2-4fdb-bf43-cd1f77879857
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-all can been evaluated on `ant-path-edges`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R142: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: a2605a3c-3303-41ee-8c61-5cee58369259
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-all has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-edges`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R143: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 6f38b438-da07-4841-8c0d-cee40721456b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goals can been evaluated on `ant-path-edges`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R144: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: e688938c-8991-4280-9e27-e58c10c96182
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goals has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-edges`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R145: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: f949e379-b6f0-4d0b-ad50-ae8879b8ab8a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin can been evaluated on `ant-path-edges`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R146: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 14068c03-da3d-4e72-9d1e-0cd783513935
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-edges`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R147: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 373f3845-c736-4dd1-ad88-d5e788523f03
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-mlp can been evaluated on `ant-path-edges`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R148: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: fede5443-8b54-4833-acf2-f53cda139c78
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-edges`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R149: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 909d13a6-b1bf-41aa-ab04-bc3bf9254650
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin-mlp can been evaluated on `ant-path-edges`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R150: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: f7b14f26-f3c7-4632-8069-137cc1ac0ff2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-lin-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-edges`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R151: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: c59574b9-432a-4d9d-9de8-2d1a7af9bc89
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-mlp can been evaluated on `ant-path-edges`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R152: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: 852706da-2ec6-4633-90ca-2d5c400434df
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-mlp has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-edges`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R153: Code has been implemented such that a FRE agent trained on `...
- **Rubric ID**: 3545d45c-ea17-4e35-bb97-bb16360f5c30
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-lin can been evaluated on `ant-path-edges`
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R154: Code has been executed such that a FRE agent trained on `ant...
- **Rubric ID**: aef98935-89aa-4272-8b2a-879a4947ac90
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as FRE-goal-lin has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-edges`.
- **Parent context**: A FRE agent trained on `antmaze-large-diverse-v2` with the prior reward distribution referred to as ...

### R155: Code has been implemented such that an FB agent trained on `...
- **Rubric ID**: d3ed7c0c-9e7a-454e-9e5d-bb4d55853115
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an FB agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-path-edges`
- **Parent context**: An FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R156: Code has been executed such that an FB agent trained on `ant...
- **Rubric ID**: 71e4572b-63f4-4444-8cd4-f8a5750f3ef3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-directional`
- **Parent context**: An FB agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R157: Code has been implemented such that an SF agent trained on `...
- **Rubric ID**: 82b053b3-9d81-4092-959a-d7c3a2dece32
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an SF agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-path-edges`
- **Parent context**: An SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R158: Code has been executed such that an SF agent trained on `ant...
- **Rubric ID**: f66b6567-15d1-4eb4-adeb-56039164f799
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-edges`
- **Parent context**: An SF agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes p...

### R159: Code has been implemented such that an OPAL agent trained on...
- **Rubric ID**: d9fca992-a961-4a06-8a11-e3fc20d84f66
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an OPAL agent trained on `antmaze-large-diverse-v2` can been evaluated on `ant-path-edges`
- **Parent context**: An OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes...

### R160: Code has been executed such that an OPAL agent trained on `a...
- **Rubric ID**: 78e86adc-8074-440d-a616-9666df4649cb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-path-edges`
- **Parent context**: An OPAL agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes...

### R161: Code has been implemented such that ExORL evaluation tasks a...
- **Rubric ID**: 1fc923e9-004a-47f9-aaaa-820343600023
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that ExORL evaluation tasks are evaluated online, i.e. the agent to evaluate and environment are instantiated and the agent acts in the environment
- **Parent context**: The necessary agents have been evaluated on the ExORL evaluation tasks

### R162: The `exorl-cheetah-velocity` evaluation task has been implem...
- **Rubric ID**: 355ad887-e94a-4c14-b291-4c5c71d91130
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-cheetah-velocity` evaluation task has been implemented such that the agent is evaluated on the 4 reward functions outlined in addendum.md
- **Parent context**: The `exorl-cheetah-velocity` evaluation task has been implemented as outlined in addendum.md and App...

### R163: The `exorl-cheetah-velocity` evaluation task has been implem...
- **Rubric ID**: 152a0cb1-280d-48fd-8b50-13a751d61780
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-cheetah-velocity` evaluation task has been implemented such that the average cumulative reward across the 4 reward functions is used as the evaluation metric
- **Parent context**: The `exorl-cheetah-velocity` evaluation task has been implemented as outlined in addendum.md and App...

### R164: The `exorl-cheetah-velocity` evaluation task has been implem...
- **Rubric ID**: fdc87d30-7749-4b8c-917f-f74a0fa1cd80
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-cheetah-velocity` evaluation task has been implemented such that at each step, the agent is assigned a reward of 1 if the agent's horizontal velocity is at least equal to the target velocity, with the reward otherwise linearly decaying towards 0 the lower the agent's velocity is with respect to the target velocity.
- **Parent context**: The `exorl-cheetah-velocity` evaluation task has been implemented as outlined in addendum.md and App...

### R165: The `exorl-cheetah-velocity` evaluation task has been implem...
- **Rubric ID**: 62a0721f-5638-451d-acc3-9d0ccadab91f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-cheetah-velocity` evaluation task has been implemented such that at each step, the agent is assigned a reward of 0 if the agent's horizontal velocity is in the direction opposite to the one specified by the target velocity.
- **Parent context**: The `exorl-cheetah-velocity` evaluation task has been implemented as outlined in addendum.md and App...

### R166: Code has been implemented such that a FRE agent trained on t...
- **Rubric ID**: 2392fdea-cf2d-4915-9db4-ad39e26cdea4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on the `cheetah` (RND) dataset with the prior reward distribution referred to as FRE-all can been evaluated on `exorl-cheetah-velocity`
- **Parent context**: A FRE agent trained on the `cheetah` (RND) dataset with the prior reward distribution referred to as...

### R167: Code has been executed such that a FRE agent trained on the...
- **Rubric ID**: 08e88294-c3b7-451d-98a3-3dbbd4567622
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on the `cheetah` (RND) dataset with the prior reward distribution referred to as FRE-all has been evaluated over 5 seeds with 20 episodes per seed on `exorl-cheetah-velocity`.
- **Parent context**: A FRE agent trained on the `cheetah` (RND) dataset with the prior reward distribution referred to as...

### R168: Code has been implemented such that a FRE agent trained on t...
- **Rubric ID**: 62aa743f-e54c-4796-8ce5-951ded8b20b4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on the `cheetah` (RND) dataset with the prior reward distribution referred to as FRE-hint can been evaluated on `exorl-cheetah-velocity`
- **Parent context**: A FRE agent trained on the `cheetah` (RND) dataset with the prior reward distribution referred to as...

### R169: Code has been executed such that a FRE agent trained on the...
- **Rubric ID**: 076e55aa-699b-4835-98b4-8ca4066bab21
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on the `cheetah` (RND) dataset with the prior reward distribution referred to as FRE-hint has been evaluated over 5 seeds with 20 episodes per seed on `exorl-cheetah-velocity`.
- **Parent context**: A FRE agent trained on the `cheetah` (RND) dataset with the prior reward distribution referred to as...

### R170: Code has been implemented such that an FB agent trained on t...
- **Rubric ID**: f3a91d55-4e45-481e-a8c6-475a418c94e7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an FB agent trained on the `cheetah` (RND) dataset can been evaluated on `exorl-cheetah-velocity`
- **Parent context**: An FB agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episodes ...

### R171: Code has been executed such that an FB agent trained on the...
- **Rubric ID**: 32648639-c6f5-47ae-bb9f-cf8a20f9a6c0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an FB agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episodes per seed on `exorl-cheetah-velocity`
- **Parent context**: An FB agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episodes ...

### R172: Code has been implemented such that an SF agent trained on t...
- **Rubric ID**: 381bc3f8-4e99-4d21-ba10-4eab4bb239fb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an SF agent trained on the `cheetah` (RND) dataset can been evaluated on `exorl-cheetah-velocity`
- **Parent context**: An SF agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episodes ...

### R173: Code has been executed such that an SF agent trained on the...
- **Rubric ID**: a412b218-687b-4964-9541-48a16a8f902b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an SF agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episodes per seed on `exorl-cheetah-velocity`
- **Parent context**: An SF agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episodes ...

### R174: Code has been implemented such that an OPAL agent trained on...
- **Rubric ID**: f97d5c45-21bc-4af4-89e5-83cb27124ca1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an OPAL agent trained on the `cheetah` (RND) dataset can been evaluated on `exorl-cheetah-velocity`
- **Parent context**: An OPAL agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episode...

### R175: Code has been executed such that an OPAL agent trained on th...
- **Rubric ID**: 915b1b79-d594-41b4-8674-f36047c03f4a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an OPAL agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episodes per seed on `exorl-cheetah-velocity`
- **Parent context**: An OPAL agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episode...

### R176: The `exorl-walker-velocity` evaluation task has been impleme...
- **Rubric ID**: f8a8ff9c-16c6-4ec5-8231-0c84b6586f85
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-walker-velocity` evaluation task has been implemented such that the agent is evaluated on the 4 reward functions outlined in addendum.md
- **Parent context**: The `exorl-walker-velocity` evaluation task has been implemented as outlined in addendum.md and Appe...

### R177: The `exorl-walker-velocity` evaluation task has been impleme...
- **Rubric ID**: 74f98f7f-fb30-4f2b-9c48-433396c9ea0d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-walker-velocity` evaluation task has been implemented such that the average cumulative reward across the 4 reward functions is used as the evaluation metric
- **Parent context**: The `exorl-walker-velocity` evaluation task has been implemented as outlined in addendum.md and Appe...

### R178: The `exorl-walker-velocity` evaluation task has been impleme...
- **Rubric ID**: d79ab8b4-25aa-44e7-876a-3623e1b26c77
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-walker-velocity` evaluation task has been implemented such that at each step, the agent is assigned a reward of 1 if the agent's horizontal velocity is at least equal to the target velocity, with the reward otherwise linearly decaying towards 0 the lower the agent's velocity is with respect to the target velocity.
- **Parent context**: The `exorl-walker-velocity` evaluation task has been implemented as outlined in addendum.md and Appe...

### R179: The `exorl-walker-velocity` evaluation task has been impleme...
- **Rubric ID**: 65369374-24af-429d-abfb-f8034d3cda58
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-walker-velocity` evaluation task has been implemented such that at each step, the agent is assigned a reward of 0 if the agent's horizontal velocity is in the direction opposite to the one specified by the target velocity.
- **Parent context**: The `exorl-walker-velocity` evaluation task has been implemented as outlined in addendum.md and Appe...

### R180: Code has been implemented such that a FRE agent trained on t...
- **Rubric ID**: 25b99cdd-8e28-471e-b811-737c12b68312
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on the `walker` (RND) dataset with the prior reward distribution referred to as FRE-all can been evaluated on `exorl-walker-velocity`
- **Parent context**: A FRE agent trained on the `walker` (RND) dataset with the prior reward distribution referred to as ...

### R181: Code has been executed such that a FRE agent trained on the...
- **Rubric ID**: 8d884b04-b9e3-451c-8026-9c802a4b5a79
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on the `walker` (RND) dataset with the prior reward distribution referred to as FRE-all has been evaluated over 5 seeds with 20 episodes per seed on `exorl-walker-velocity`.
- **Parent context**: A FRE agent trained on the `walker` (RND) dataset with the prior reward distribution referred to as ...

### R182: Code has been implemented such that a FRE agent trained on t...
- **Rubric ID**: 0431ce4a-43e6-409c-9dd0-66f9a91a484d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on the `walker` (RND) dataset with the prior reward distribution referred to as FRE-hint can been evaluated on `exorl-walker-velocity`
- **Parent context**: A FRE agent trained on the `walker` (RND) dataset with the prior reward distribution referred to as ...

### R183: Code has been executed such that a FRE agent trained on the...
- **Rubric ID**: ecf0ca0d-5753-44d4-a6fe-f31d3a990658
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on the `walker` (RND) dataset with the prior reward distribution referred to as FRE-hint has been evaluated over 5 seeds with 20 episodes per seed on `exorl-walker-velocity`.
- **Parent context**: A FRE agent trained on the `walker` (RND) dataset with the prior reward distribution referred to as ...

### R184: Code has been implemented such that an FB agent trained on t...
- **Rubric ID**: 978163bc-7af6-4ce9-b0c0-a890097cf1a1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an FB agent trained on the `walker` (RND) dataset can been evaluated on `exorl-walker-velocity`
- **Parent context**: An FB agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes p...

### R185: Code has been executed such that an FB agent trained on the...
- **Rubric ID**: e60f2dd7-99d4-447a-8011-2477425ea3ff
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an FB agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes per seed on `exorl-walker-velocity`
- **Parent context**: An FB agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes p...

### R186: Code has been implemented such that an SF agent trained on t...
- **Rubric ID**: 25babc37-5720-4aac-9c70-6cbc3127bebc
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an SF agent trained on the `walker` (RND) dataset can been evaluated on `exorl-walker-velocity`
- **Parent context**: An SF agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes p...

### R187: Code has been executed such that an SF agent trained on the...
- **Rubric ID**: 7c82fe04-ca0f-44f1-84c4-88f5a16f8c16
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an SF agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes per seed on `exorl-walker-velocity`
- **Parent context**: An SF agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes p...

### R188: Code has been implemented such that an OPAL agent trained on...
- **Rubric ID**: 5e391219-7b65-4545-8b89-fa68fb460079
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an OPAL agent trained on the `walker` (RND) dataset can been evaluated on `exorl-walker-velocity`
- **Parent context**: An OPAL agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes...

### R189: Code has been executed such that an OPAL agent trained on th...
- **Rubric ID**: 4ed668ae-0b4e-454a-a486-c37bec600d23
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an OPAL agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes per seed on `exorl-walker-velocity`
- **Parent context**: An OPAL agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes...

### R190: The `exorl-cheetah-goals` evaluation task has been implement...
- **Rubric ID**: 484d1b87-8cf0-4ccb-b962-424dda13c7e8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-cheetah-goals` evaluation task has been implemented such that the agent is evaluated on the 5 reward functions outlined in addendum.md
- **Parent context**: The `exorl-cheetah-goals` evaluation task has been implemented as outlined in addendum.md and Append...

### R191: The `exorl-cheetah-goals` evaluation task has been implement...
- **Rubric ID**: 9c9c3824-f636-469d-9290-ea6678e87219
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-cheetah-goals` evaluation task has been implemented such that the average cumulative reward across the 5 reward functions is used as the evaluation metric
- **Parent context**: The `exorl-cheetah-goals` evaluation task has been implemented as outlined in addendum.md and Append...

### R192: The `exorl-cheetah-goals` evaluation task has been implement...
- **Rubric ID**: cea75914-0d1a-4ece-908d-f3e106d121d7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-cheetah-goals` evaluation task has been implemented such that the goal is considered reached if an agent reaches within a distance of 0.1 from the target position.
- **Parent context**: The `exorl-cheetah-goals` evaluation task has been implemented as outlined in addendum.md and Append...

### R193: The `exorl-cheetah-goals` evaluation task has been implement...
- **Rubric ID**: e68e0cbb-02fd-44ca-81cd-6c32aa31d105
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-cheetah-goals` evaluation task has been implemented such that the agent receives a reward of -1 at each timestep until it successfully reaches the goal.
- **Parent context**: The `exorl-cheetah-goals` evaluation task has been implemented as outlined in addendum.md and Append...

### R194: The `exorl-cheetah-goals` evaluation task has been implement...
- **Rubric ID**: ab4b3fb8-eef0-4264-9725-36874589938d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-cheetah-goals` evaluation task has been implemented such that the "distance" is the euclidian distance between the current state and the target state.
- **Parent context**: The `exorl-cheetah-goals` evaluation task has been implemented as outlined in addendum.md and Append...

### R195: Code has been implemented such that a FRE agent trained on t...
- **Rubric ID**: 3b3c59cc-d09d-4ff4-b26e-f431477c49ee
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on the `cheetah` (RND) dataset with the prior reward distribution referred to as FRE-all can been evaluated on `exorl-cheetah-goals`
- **Parent context**: A FRE agent trained on the `cheetah` (RND) dataset with the prior reward distribution referred to as...

### R196: Code has been executed such that a FRE agent trained on the...
- **Rubric ID**: 196c3d18-16fd-4885-aaed-9356d456c254
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on the `cheetah` (RND) dataset with the prior reward distribution referred to as FRE-all has been evaluated over 5 seeds with 20 episodes per seed on `exorl-cheetah-goals`.
- **Parent context**: A FRE agent trained on the `cheetah` (RND) dataset with the prior reward distribution referred to as...

### R197: Code has been implemented such that an FB agent trained on t...
- **Rubric ID**: b01813a2-f291-421c-89e7-3759947ad902
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an FB agent trained on the `cheetah` (RND) dataset can been evaluated on `exorl-cheetah-goals`
- **Parent context**: An FB agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episodes ...

### R198: Code has been executed such that an FB agent trained on the...
- **Rubric ID**: a14a40d6-fc3e-414d-b933-0422e1be5d12
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an FB agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episodes per seed on `exorl-cheetah-goals`
- **Parent context**: An FB agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episodes ...

### R199: Code has been implemented such that an SF agent trained on t...
- **Rubric ID**: ef21a23b-6d3f-4eb5-9ac5-70e866712286
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an SF agent trained on the `cheetah` (RND) dataset can been evaluated on `exorl-cheetah-goals`
- **Parent context**: An SF agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episodes ...

### R200: Code has been executed such that an SF agent trained on the...
- **Rubric ID**: 950e4e31-dba8-438f-a3c2-22d88af6d61b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an SF agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episodes per seed on `exorl-cheetah-goals`
- **Parent context**: An SF agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episodes ...

### R201: Code has been implemented such that an OPAL agent trained on...
- **Rubric ID**: 11ad2689-7b95-4fff-9911-0e214be06223
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an OPAL agent trained on the `cheetah` (RND) dataset can been evaluated on `exorl-cheetah-goals`
- **Parent context**: An OPAL agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episode...

### R202: Code has been executed such that an OPAL agent trained on th...
- **Rubric ID**: a465ea35-ecc3-4b6a-a8f6-415a9283f42d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an OPAL agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episodes per seed on `exorl-cheetah-goals`
- **Parent context**: An OPAL agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episode...

### R203: Code has been implemented such that an GC-IQL agent trained...
- **Rubric ID**: 3421320a-fcd2-4cb6-8194-eef5b09366e1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an GC-IQL agent trained on the `cheetah` (RND) dataset can been evaluated on `exorl-cheetah-goals`
- **Parent context**: A GC-IQL agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episod...

### R204: Code has been executed such that an GC-IQL agent trained on...
- **Rubric ID**: 39e51d18-ab26-49d6-8c50-84409d2f2c55
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an GC-IQL agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episodes per seed on `exorl-cheetah-goals`
- **Parent context**: A GC-IQL agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episod...

### R205: Code has been implemented such that a GC-BC agent trained on...
- **Rubric ID**: 608692e5-818e-4e2f-bf13-d563dd219ad8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a GC-BC agent trained on the `cheetah` (RND) dataset can been evaluated on `exorl-cheetah-goals`
- **Parent context**: A GC-BC agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episode...

### R206: Code has been executed such that a GC-BC agent trained on `a...
- **Rubric ID**: 0020c065-4c18-4969-a23e-00c4b66b7fc7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a GC-BC agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-goal-reaching`
- **Parent context**: A GC-BC agent trained on the `cheetah` (RND) dataset has been evaluated over 5 seeds with 20 episode...

### R207: The `exorl-walker-goals` evaluation task has been implemente...
- **Rubric ID**: 8eceb966-2eef-4959-af07-67bb229ffff5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-walker-goals` evaluation task has been implemented such that the agent is evaluated on the 5 reward functions outlined in addendum.md
- **Parent context**: The `exorl-walker-goals` evaluation task has been implemented as outlined in addendum.md and Appendi...

### R208: The `exorl-walker-goals` evaluation task has been implemente...
- **Rubric ID**: e5ee2347-7bff-4863-ab55-02203ea0e12b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-walker-goals` evaluation task has been implemented such that the average cumulative reward across the 5 reward functions is used as the evaluation metric
- **Parent context**: The `exorl-walker-goals` evaluation task has been implemented as outlined in addendum.md and Appendi...

### R209: The `exorl-walker-goals` evaluation task has been implemente...
- **Rubric ID**: b640ce00-1af4-4581-a708-8f2c3ceebede
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-walker-goals` evaluation task has been implemented such that the goal is considered reached if an agent reaches within a distance of 0.1 from the target position.
- **Parent context**: The `exorl-walker-goals` evaluation task has been implemented as outlined in addendum.md and Appendi...

### R210: The `exorl-walker-goals` evaluation task has been implemente...
- **Rubric ID**: ebff729f-fb91-4e3b-8bce-0aa7557e252c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-walker-goals` evaluation task has been implemented such that the agent receives a reward of -1 at each timestep until it successfully reaches the goal.
- **Parent context**: The `exorl-walker-goals` evaluation task has been implemented as outlined in addendum.md and Appendi...

### R211: The `exorl-walker-goals` evaluation task has been implemente...
- **Rubric ID**: 9efc5692-574e-4b10-bf25-f5bb763bf5ea
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `exorl-walker-goals` evaluation task has been implemented such that the "distance" is the euclidian distance between the current state and the target state.
- **Parent context**: The `exorl-walker-goals` evaluation task has been implemented as outlined in addendum.md and Appendi...

### R212: Code has been implemented such that a FRE agent trained on t...
- **Rubric ID**: 464f7d18-70e3-4d87-8fd8-e5063a4a766c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on the `walker` (RND) dataset with the prior reward distribution referred to as FRE-all can been evaluated on `exorl-walker-goals`
- **Parent context**: A FRE agent trained on the `walker` (RND) dataset with the prior reward distribution referred to as ...

### R213: Code has been executed such that a FRE agent trained on the...
- **Rubric ID**: 201a0d18-9eb0-455f-8bc0-18ff18858f3c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on the `walker` (RND) dataset with the prior reward distribution referred to as FRE-all has been evaluated over 5 seeds with 20 episodes per seed on `exorl-walker-goals`.
- **Parent context**: A FRE agent trained on the `walker` (RND) dataset with the prior reward distribution referred to as ...

### R214: Code has been implemented such that an FB agent trained on t...
- **Rubric ID**: aef4f70c-8724-4f68-812c-50bbcf3a6716
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an FB agent trained on the `walker` (RND) dataset can been evaluated on `exorl-walker-goals`
- **Parent context**: An FB agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes p...

### R215: Code has been executed such that an FB agent trained on the...
- **Rubric ID**: 2d89f877-2993-40c9-89be-ac60d929c46f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an FB agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes per seed on `exorl-walker-goals`
- **Parent context**: An FB agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes p...

### R216: Code has been implemented such that an SF agent trained on t...
- **Rubric ID**: 9266176a-45ef-44f4-bd5a-f7d5ae83285d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an SF agent trained on the `walker` (RND) dataset can been evaluated on `exorl-walker-goals`
- **Parent context**: An SF agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes p...

### R217: Code has been executed such that an SF agent trained on the...
- **Rubric ID**: 7be56ff7-4b6e-42e7-90c3-6565c5dc0959
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an SF agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes per seed on `exorl-walker-goals`
- **Parent context**: An SF agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes p...

### R218: Code has been implemented such that an OPAL agent trained on...
- **Rubric ID**: e31c9c07-284c-4b8b-b40b-a8114e7a6928
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an OPAL agent trained on the `walker` (RND) dataset can been evaluated on `exorl-walker-goals`
- **Parent context**: An OPAL agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes...

### R219: Code has been executed such that an OPAL agent trained on th...
- **Rubric ID**: d867fa10-2dc6-4d4a-9c6b-f48129859950
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an OPAL agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes per seed on `exorl-walker-goals`
- **Parent context**: An OPAL agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes...

### R220: Code has been implemented such that an GC-IQL agent trained...
- **Rubric ID**: ab5ca13a-b32b-40de-901a-ea58ef9a42a3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an GC-IQL agent trained on the `walker` (RND) dataset can been evaluated on `exorl-walker-goals`
- **Parent context**: A GC-IQL agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episode...

### R221: Code has been executed such that an GC-IQL agent trained on...
- **Rubric ID**: 36c0aa54-3b7f-46f3-9ec0-262a84c80e8c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an GC-IQL agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes per seed on `exorl-walker-goals`
- **Parent context**: A GC-IQL agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episode...

### R222: Code has been implemented such that a GC-BC agent trained on...
- **Rubric ID**: 7736cd75-7071-4b8b-bda2-4f2bca3fc4b0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a GC-BC agent trained on the `walker` (RND) dataset can been evaluated on `exorl-walker-goals`
- **Parent context**: A GC-BC agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes...

### R223: Code has been executed such that a GC-BC agent trained on `a...
- **Rubric ID**: 7a49a6ad-d34a-434b-8724-7e649d7282ea
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a GC-BC agent trained on `antmaze-large-diverse-v2` has been evaluated over 5 seeds with 20 episodes per seed on `ant-goal-reaching`
- **Parent context**: A GC-BC agent trained on the `walker` (RND) dataset has been evaluated over 5 seeds with 20 episodes...

### R224: Code has been implemented such that Kitchen evaluation tasks...
- **Rubric ID**: ac9dc484-cddc-4e53-8731-71ed85288e30
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that Kitchen evaluation tasks are evaluated online, i.e. the agent to evaluate and environment are instantiated and the agent acts in the environment
- **Parent context**: The necessary agents have been evaluated on the `kitchen` evaluation task

### R225: The `kitchen` evaluation task has been implemented such that...
- **Rubric ID**: bb2371d7-b938-487a-94d5-be868b8b6d4c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `kitchen` evaluation task has been implemented such that the agent is evaluated on the 7 standard tasks of the Franka Kitchen environment: `bottom-burner`, `kettle`, `light-switch`, `microwave`, `slide-cabinet`, `hinge-cabinet`, `top-burner`
- **Parent context**: The `kitchen` evaluation task has been implemented as outlined in Section 5 and Appendix C.1

### R226: The `kitchen` evaluation task has been implemented such that...
- **Rubric ID**: 3fc9b62f-ca5e-4d7b-93a2-4617443cc987
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `kitchen` evaluation task has been implemented such that the sparse rewards from the 7 standard tasks of the Franka Kitchen environment are used as the reward functions
- **Parent context**: The `kitchen` evaluation task has been implemented as outlined in Section 5 and Appendix C.1

### R227: The `kitchen` evaluation task has been implemented such that...
- **Rubric ID**: 5272c7f4-83fa-431c-819c-16e5908a450f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The `kitchen` evaluation task has been implemented such that the average cumulative reward across the 7 standard tasks of the Franka Kitchen environment is used as the evaluation metric
- **Parent context**: The `kitchen` evaluation task has been implemented as outlined in Section 5 and Appendix C.1

### R228: Code has been implemented such that a FRE agent trained on t...
- **Rubric ID**: c46c155a-e146-4489-b4ea-d2aabe650195
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a FRE agent trained on the `kitchen-complete-v0` dataset with the prior reward distribution referred to as FRE-all can been evaluated on `kitchen`
- **Parent context**: A FRE agent trained on the `kitchen-complete-v0` dataset with the prior reward distribution referred...

### R229: Code has been executed such that a FRE agent trained on the...
- **Rubric ID**: a8265cc7-2215-4395-a8c0-44af2c0100fc
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a FRE agent trained on the `kitchen-complete-v0` dataset with the prior reward distribution referred to as FRE-all has been evaluated over 5 seeds with 20 episodes per seed on `kitchen`.
- **Parent context**: A FRE agent trained on the `kitchen-complete-v0` dataset with the prior reward distribution referred...

### R230: Code has been implemented such that an FB agent trained on t...
- **Rubric ID**: dafc9310-1d81-457e-9214-a55dc5ca1c33
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an FB agent trained on the `kitchen-complete-v0` dataset can been evaluated on `kitchen`
- **Parent context**: An FB agent trained on the `kitchen-complete-v0` dataset has been evaluated over 5 seeds with 20 epi...

### R231: Code has been executed such that an FB agent trained on the...
- **Rubric ID**: d367d317-48d7-4bd6-a3ed-51202ad133d1
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an FB agent trained on the `kitchen-complete-v0` dataset has been evaluated over 5 seeds with 20 episodes per seed on `kitchen`
- **Parent context**: An FB agent trained on the `kitchen-complete-v0` dataset has been evaluated over 5 seeds with 20 epi...

### R232: Code has been implemented such that an SF agent trained on t...
- **Rubric ID**: 09fdc2a7-a0c7-43b1-84c4-b640d2a2cd6e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an SF agent trained on the `kitchen-complete-v0` dataset can been evaluated on `kitchen`
- **Parent context**: An SF agent trained on the `kitchen-complete-v0` dataset has been evaluated over 5 seeds with 20 epi...

### R233: Code has been executed such that an SF agent trained on the...
- **Rubric ID**: 5e5ad647-67d4-40d4-b4bc-2d44a5b8067b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an SF agent trained on the `kitchen-complete-v0` dataset has been evaluated over 5 seeds with 20 episodes per seed on `kitchen`
- **Parent context**: An SF agent trained on the `kitchen-complete-v0` dataset has been evaluated over 5 seeds with 20 epi...

### R234: Code has been implemented such that an OPAL agent trained on...
- **Rubric ID**: a0dd5509-d456-4b47-a63b-7e8efe23e9f4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that an OPAL agent trained on the `kitchen-complete-v0` dataset can been evaluated on `kitchen`
- **Parent context**: An OPAL agent trained on the `kitchen-complete-v0` dataset has been evaluated over 5 seeds with 20 e...

### R235: Code has been executed such that an OPAL agent trained on th...
- **Rubric ID**: bef7996b-08e8-4a85-a8df-3303765c5385
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that an OPAL agent trained on the `kitchen-complete-v0` dataset has been evaluated over 5 seeds with 20 episodes per seed on `kitchen`
- **Parent context**: An OPAL agent trained on the `kitchen-complete-v0` dataset has been evaluated over 5 seeds with 20 e...

### R236: Code has been implemented such that a GC-IQL agent trained o...
- **Rubric ID**: 70b728c0-16d2-4395-9eaf-8e1ba2dc9431
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a GC-IQL agent trained on the `kitchen-complete-v0` dataset can been evaluated on `kitchen`
- **Parent context**: A GC-IQL agent trained on the `kitchen-complete-v0` dataset has been evaluated over 5 seeds with 20 ...

### R237: Code has been executed such that a GC-IQL agent trained on t...
- **Rubric ID**: 57109f90-2e89-4f42-a9fb-45d555079f9e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a GC-IQL agent trained on the `kitchen-complete-v0` dataset has been evaluated over 5 seeds with 20 episodes per seed on `kitchen`
- **Parent context**: A GC-IQL agent trained on the `kitchen-complete-v0` dataset has been evaluated over 5 seeds with 20 ...

### R238: Code has been implemented such that a GC-BC agent trained on...
- **Rubric ID**: 9ae46f69-3529-4400-9acf-0debe80f5b9a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that a GC-BC agent trained on the `kitchen-complete-v0` dataset can been evaluated on `kitchen`
- **Parent context**: A GC-BC agent trained on the `kitchen-complete-v0` dataset has been evaluated over 5 seeds with 20 e...

### R239: Code has been executed such that a GC-BC agent trained on th...
- **Rubric ID**: c78015f1-6eca-4e14-8313-1ec5ef024b1d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been executed such that a GC-BC agent trained on the `kitchen-complete-v0` dataset has been evaluated over 5 seeds with 20 episodes per seed on `kitchen`
- **Parent context**: A GC-BC agent trained on the `kitchen-complete-v0` dataset has been evaluated over 5 seeds with 20 e...

### R240: The outcome of the evaluation shows that on most goal-reachi...
- **Rubric ID**: 2f2d443f-aadb-455b-95e0-5bff35e369f9
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The outcome of the evaluation shows that on most goal-reaching tasks (at least 3 of ant-goal-reaching, exorl-cheetah-goals, exorl-walker-goals, kitchen), the performance of the FRE agent is significantly higher than the performance of the SF and FB baselines, as discussed in section 5.2 of the paper
- **Parent context**: The evaluation outcome shows or implies results that reproduce those shown in the paper in section 5...

### R241: The outcome of the evaluation shows that on most goal-reachi...
- **Rubric ID**: 081c9d9f-838d-4ac1-9564-ea7e0d0c54ca
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The outcome of the evaluation shows that on most goal-reaching tasks (at least 3 of ant-goal-reaching, exorl-cheetah-goals, exorl-walker-goals, kitchen), the performance of the FRE agent is not significantly lower than the performance of GC-IQL and GC-BC baselines, as discussed in section 5.2 of the paper
- **Parent context**: The evaluation outcome shows or implies results that reproduce those shown in the paper in section 5...

### R242: The outcome of the evaluation shows that the performance of...
- **Rubric ID**: 6ff5f645-a29c-4705-8d80-533f8269c8d2
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The outcome of the evaluation shows that the performance of the FRE agent is competitive (either top or joint top performance) on at least 4 of (ant-directional, ant-random-simplex, ant-path-loop, ant-path-edges, ant-path-center) when compared to all of the SF, FB, GC-IQL, GC-BC and OPAL baselines, as discussed in section 5.2 of the paper
- **Parent context**: The evaluation outcome shows or implies results that reproduce those shown in the paper in section 5...

### R243: The outcome of the evaluation shows that on average, the FRE...
- **Rubric ID**: 0a57fe73-6b37-400a-843f-53e66f8945a6
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The outcome of the evaluation shows that on average, the FRE agent significantly outperforms the OPAL agent, as discussed in section 5.2 of the paper.
- **Parent context**: The evaluation outcome shows or implies results that reproduce those shown in the paper in section 5...

### R244: The outcome of the evaluation shows that the FRE agent train...
- **Rubric ID**: 5f01970b-62b9-4c59-9cc4-1b81958f506a
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The outcome of the evaluation shows that the FRE agent trained with the FRE-all prior reward distribution achieves the highest average score compared to FRE agents trained with any of {FRE-goals, FRE-lin, FRE-mlp, FRE-lin-mlp, FRE-goal-mlp, FRE-goal-lin} prior reward distributions, as discussed in section 5.3 of the paper and shown in Table 4.
- **Parent context**: The evaluation outcome shows or implies results that reproduce those shown in the paper in section 5...

### R245: The outcome of the evaluation shows that the FRE agent train...
- **Rubric ID**: 4860910a-d4bf-4d67-b599-d9ede5491eb0
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The outcome of the evaluation shows that the FRE agent trained with the FRE-all prior reward distribution either outperforms or matches the performance of FRE agents trained with any of {FRE-goals, FRE-lin, FRE-mlp, FRE-lin-mlp, FRE-goal-mlp, FRE-goal-lin} prior reward distributions on all of the individual tasks (antmaze-goal-reaching, antmaze-directional, antmaze-random-simplex, and antmaze-path-all, which is the average performance on antmaze-path-loop, antmaze-path-edges and antmaze-path-center), as discussed in section 5.3 of the paper and shown in Table 4.
- **Parent context**: The evaluation outcome shows or implies results that reproduce those shown in the paper in section 5...

### R246: The outcome of the evaluation shows or implies that the FRE...
- **Rubric ID**: 2f455b0f-b596-4bd1-a793-64aa3bc493ed
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The outcome of the evaluation shows or implies that the FRE agent trained with the augmented FRE-hint prior reward distribution outperforms the FRE agent trained on the vanilla FRE prior reward distribution on all of {ant-directional, cheetah-velocity, walker-velocity} evaluation tasks, as shown in the paper in section 5.4 and Figure 6
- **Parent context**: The paper "Unsupervised Zero-Shot Reinforcement Learning via Functional Reward Encodings" has been r...

## Method Implementation

### R247: Code has been implemented such that the `cheetah` (RND) data...
- **Rubric ID**: bccaf966-1315-49b8-9d49-df1b0f30d109
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the `cheetah` (RND) dataset from ExORL (https://github.com/denisyarats/exorl)  can be used for offline training of sequential decision making agents
- **Parent context**: The ExORL `cheetah` (RND) dataset and environment has been setup

### R248: Code has been implemented such that the `walker` (RND) datas...
- **Rubric ID**: 2b14e66b-18a7-45ad-9dc9-94dd728cb448
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the `walker` (RND) dataset from ExORL (https://github.com/denisyarats/exorl) can be used for offline training of sequential decision making agents
- **Parent context**: The ExORL `walker` (RND) dataset and environment has been setup

### R249: The FRE implementation consists of an Encoder-Decoder networ...
- **Rubric ID**: ea36bca4-ce04-4d7c-a287-b1083812ecbf
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The FRE implementation consists of an Encoder-Decoder network, and a FRE-conditioned IQL policy
- **Parent context**: The FRE model architecture has been implemented

### R250: The FRE Encoder network has been implemented such that the i...
- **Rubric ID**: 04d679d0-0bca-4103-a118-76df6a2b2473
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The FRE Encoder network has been implemented such that the input scalar reward is discretized into 32 bins by rescaling the reward to [0,1] and then multiplying by 32 and flooring to the nearest integer
- **Parent context**: The FRE Encoder network has been implemented

### R251: The FRE Encoder network has been implemented such that the d...
- **Rubric ID**: 7297f42f-cad1-4777-8f1a-f8162637eed6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The FRE Encoder network has been implemented such that the discretized reward is is mapped to a continuous vector representation using a learned embedding table
- **Parent context**: The FRE Encoder network has been implemented

### R252: The FRE Encoder network has been implemented such that the t...
- **Rubric ID**: a9ad5a0c-8b63-4801-861e-50b22ee57859
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The FRE Encoder network has been implemented such that the the environment state projected into an embedding using a learned linear transformation
- **Parent context**: The FRE Encoder network has been implemented

### R253: The FRE Encoder network has been implemented such that for e...
- **Rubric ID**: 4afafbc9-4040-40dd-8d33-6506edc2678a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The FRE Encoder network has been implemented such that for each state, the reward embedding is concatenated to end of the state embedding before the set of reward-labeled states is passed through the encoder
- **Parent context**: The FRE Encoder network has been implemented

### R254: The FRE Encoder has been implemented such that it takes a se...
- **Rubric ID**: 90b8884f-8bdd-4027-a927-790015380e3b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The FRE Encoder has been implemented such that it takes a set of states labeled with their scalar rewards as input
- **Parent context**: The FRE Encoder network has been implemented

### R255: The FRE Encoder has been implemented such that it uses a per...
- **Rubric ID**: e812f3c1-5afa-4b52-8e07-0f878cb43f9e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The FRE Encoder has been implemented such that it uses a permutation invariant transformer as the main architecture.
- **Parent context**: The FRE Encoder network has been implemented

### R256: The FRE Encoder has been implemented such that the transform...
- **Rubric ID**: b57031ba-92a4-4b93-b32f-175b1cc678de
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The FRE Encoder has been implemented such that the transformer does not use a causal mask on its attention, such that each input token can attend to any other input token.
- **Parent context**: The FRE Encoder network has been implemented

### R257: The FRE encoder has been implemented such that positional em...
- **Rubric ID**: 17bdcdac-2c97-4f1e-b7a9-c50bd16d060e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The FRE encoder has been implemented such that positional embeddings are not used in the transformer
- **Parent context**: The FRE Encoder network has been implemented

### R258: The FRE Decoder has been implemented such that it uses a fee...
- **Rubric ID**: 0748e789-817a-4dbe-89e9-b98bc37689c4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The FRE Decoder has been implemented such that it uses a feedforward neural network as the main architecture.
- **Parent context**: The FRE decoder network has been implemented

### R259: The FRE Decoder has been implemented such that it independen...
- **Rubric ID**: 6a54735c-e526-48fb-bc87-4a3a116083f8
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The FRE Decoder has been implemented such that it independently predicts the reward for a single input state, given a shared latent encoding z
- **Parent context**: The FRE decoder network has been implemented

### R260: The FRE-conditioned policy network has been implemented such...
- **Rubric ID**: 6b6edf6b-bb31-4655-a24f-156f6dd5be12
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The FRE-conditioned policy network has been implemented such that it includes an actor, critic, value, and target critic network
- **Parent context**: The FRE-conditioned policy network has been implemented

### R261: The FRE-conditioned policy network has been implemented such...
- **Rubric ID**: 40d26271-b5b9-4c00-abe7-3f5fb4c231d4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The FRE-conditioned policy network has been implemented such that the RL components are conditioned on some latent variable z produced by the FRE encoder
- **Parent context**: The FRE-conditioned policy network has been implemented

### R262: The FRE-conditioned policy network has been implemented such...
- **Rubric ID**: 95ebb4b4-110a-421f-8ca4-185cacaaffd0
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The FRE-conditioned policy network has been implemented such that the actor predicts a Gaussian distribution over actions (mean and log std)
- **Parent context**: The FRE-conditioned policy network has been implemented

### R263: The GC-IQL model has been implemented such that it includes...
- **Rubric ID**: 4bbda5e1-08af-4448-be55-a74b27109b85
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The GC-IQL model has been implemented such that it includes an actor, critic, value, and target critic network
- **Parent context**: The GC-IQL model architecture has been implemented

### R264: The GC-IQL model has been implemented such that the actor pr...
- **Rubric ID**: d1495479-c0b0-44d3-b327-d3f2e380adc2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The GC-IQL model has been implemented such that the actor predicts a Gaussian distribution over actions (mean and log std)
- **Parent context**: The GC-IQL model architecture has been implemented

### R265: The GC-IQL model has been implemented such that it is goal-c...
- **Rubric ID**: 55e9351f-7627-4664-afac-e76327412716
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The GC-IQL model has been implemented such that it is goal-conditioned by concatenating the current observation with the desired goal before feeding into the networks
- **Parent context**: The GC-IQL model architecture has been implemented

### R266: The GC-BC model has been implemented such that it is a MLP w...
- **Rubric ID**: 83fd90f6-0652-485b-a977-a9bb84af9d0d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The GC-BC model has been implemented such that it is a MLP with three hidden layers of size 512
- **Parent context**: The GC-BC model architecture has been implemented

### R267: The GC-BC model has been implemented such that it predicts a...
- **Rubric ID**: 620a2b18-8964-4c29-86e0-fad951820c68
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The GC-BC model has been implemented such that it predicts a gaussian distribution over actions, with two outputs, a mean action and the log of the standard deviation
- **Parent context**: The GC-BC model architecture has been implemented

### R268: The GC-BC model has been implemented such that the log of th...
- **Rubric ID**: 714d7e4a-a799-460a-84f4-b78d6e065449
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The GC-BC model has been implemented such that the log of the standard deviation is clamped with a lower bound of -5
- **Parent context**: The GC-BC model architecture has been implemented

### R269: The GC-BC model has been implemented such that ReLU is appli...
- **Rubric ID**: d297b5ab-65b6-49f4-8f92-e9944afeb159
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The GC-BC model has been implemented such that ReLU is applied between each hidden layer
- **Parent context**: The GC-BC model architecture has been implemented

### R270: The GC-BC model has been implemented such that layer normali...
- **Rubric ID**: 424bb63c-fc0a-4c1c-9014-03c90a967ddc
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The GC-BC model has been implemented such that layer normalization is applied before each activation function
- **Parent context**: The GC-BC model architecture has been implemented

### R271: The OPAL method has been implemented such that it consists a...
- **Rubric ID**: b4c6e00e-7da1-43e5-8d56-18d3162980e0
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The OPAL method has been implemented such that it consists at minimum of an encoder $q_{\phi}(z\mid\tau)$ and a latent-conditioned decoder (primitive policy) $\pi_{\theta}(a\mid s,z)$
- **Parent context**: The OPAL model architecture has been implemented

### R272: The OPAL encoder has been implemented such that it reads a s...
- **Rubric ID**: 0389ff82-4e00-4553-9dd6-816d3f816df0
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The OPAL encoder has been implemented such that it reads a sub-trajectory of length $c$, consisting of $(s_{t}, a_{t})$ pairs, and produces parameters of a latent distribution (e.g. mean $\mu_{z}$ and log-standard-deviation $\sigma_{z}$).
- **Parent context**: The OPAL encoder architecture $q_{\phi}(z\mid\tau)$ has been implemented

### R273: The OPAL encoder has been implemented such that it uses a pe...
- **Rubric ID**: c41ecad0-c7ef-4af1-bb7a-7009167b2c54
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The OPAL encoder has been implemented such that it uses a permutation invariant transformer to process the $c$ timesteps and output the latent distribution parameters.
- **Parent context**: The OPAL encoder architecture $q_{\phi}(z\mid\tau)$ has been implemented

### R274: The OPAL encoder has been implemented such that it uses a pe...
- **Rubric ID**: 8f4e8195-602b-4832-a7ff-1467d72f1d20
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The OPAL encoder has been implemented such that it uses a permutation invariant transformer that does not use a causal mask on its attention, such that each input token can attend to any other input token.
- **Parent context**: The OPAL encoder architecture $q_{\phi}(z\mid\tau)$ has been implemented

### R275: The OPAL encoder has been implemented such that it uses a pe...
- **Rubric ID**: ce744ae1-4b2d-4344-a9f5-3dfdd13e3740
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The OPAL encoder has been implemented such that it uses a permutation invariant transformer does not use positional embeddings
- **Parent context**: The OPAL encoder architecture $q_{\phi}(z\mid\tau)$ has been implemented

### R276: The OPAL encoder has been implemented such that it represent...
- **Rubric ID**: 7b768bcc-eecd-4cfa-a226-4b9fd827ce2c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The OPAL encoder has been implemented such that it represents $q_{\phi}(z\mid\tau)$ as a Gaussian distribution parameterized by $(\mu_{z}^{\mathrm{enc}}, \sigma_{z}^{\mathrm{enc}})$ for the latent variable $z$.
- **Parent context**: The OPAL encoder architecture $q_{\phi}(z\mid\tau)$ has been implemented

### R277: The OPAL decoder has been implemented such that it is a late...
- **Rubric ID**: b6fbd20b-f697-4031-8f1e-48ec275608f9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The OPAL decoder has been implemented such that it is a latent-conditioned policy that takes current state $s$ and latent $z$, and outputs a Gaussian distribution over actions, parameterized by $(\mu_{a},\sigma_{a})$.
- **Parent context**: The OPAL decoder (primitive policy) $\pi_{\theta}(a\mid s,z)$ has been implemented

### R278: The OPAL decoder has been implemented as a feedforward netwo...
- **Rubric ID**: 34d188ba-9c5b-49ba-ad5e-b7100acbdb18
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The OPAL decoder has been implemented as a feedforward network (e.g., multi-layer perceptron with $L$ layers and hidden dimension $H$) or an autoregressive variant if used for sequential action prediction.
- **Parent context**: The OPAL decoder (primitive policy) $\pi_{\theta}(a\mid s,z)$ has been implemented

### R279: Code has been implemented such that when training the FRE en...
- **Rubric ID**: 15d902cd-80ef-4af9-8c10-7bed54c10d50
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training the FRE encoder-decoder, the variational lower bound outlined in equation (6) is used as the loss function to optimize, or equivalent implementations.
- **Parent context**: Code has been implemented for training FRE agents

### R280: Code has been implemented such that when training the FRE en...
- **Rubric ID**: 8b30922a-67a0-4ae8-98d5-3c14aa1c4529
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training the FRE encoder-decoder, the states sampled for decoding and the states sampled for encoding are sampled separately, such that the states used for decoding and the states used for encoding are different.
- **Parent context**: Code has been implemented for training FRE agents

### R281: Code has been implemented such that when training the FRE-co...
- **Rubric ID**: d922ee95-cda8-4ccc-bb4d-07af9a8ee238
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training the FRE-conditioned policy using implicit Q-learning, the critic is updated with an MSE loss to the Bellman target: r + discount * mask * next_value
- **Parent context**: Code has been implemented such that the FRE-conditioned policy is trained using implicit Q-learning,...

### R282: Code has been implemented such that when training the FRE-co...
- **Rubric ID**: 422ffe1f-c3f0-4562-ba99-05e5c69a4e87
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training the FRE-conditioned policy using implicit Q-learning, the value function is updated with an expectile regression objective on the critic's Q-values
- **Parent context**: Code has been implemented such that the FRE-conditioned policy is trained using implicit Q-learning,...

### R283: Code has been implemented such that when training the FRE-co...
- **Rubric ID**: 5ff98598-e932-4fa7-8d81-342c04348da5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training the FRE-conditioned policy using implicit Q-learning, the actor is updated via advantage-weighted regression (AWR)
- **Parent context**: Code has been implemented such that the FRE-conditioned policy is trained using implicit Q-learning,...

### R284: Code has been implemented such that when training the FRE-co...
- **Rubric ID**: 31e4d8ce-e490-4bba-b371-8a6a8e16e66e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training the FRE-conditioned policy using implicit Q-learning, after the critic update, the target critic is updated via a soft update rule from the critic params and previous target critic params.
- **Parent context**: Code has been implemented such that the FRE-conditioned policy is trained using implicit Q-learning,...

### R285: Code has been implemented such that when training the FRE-co...
- **Rubric ID**: f0ab7926-f357-41a2-b39d-3af3a94d4022
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training the FRE-conditioned policy using implicit Q-learning, the output z from the frozen encoder is concatenated to the current observation before feeding them into the actor, critic, target critic and value networks
- **Parent context**: Code has been implemented such that the FRE-conditioned policy is trained using implicit Q-learning,...

### R286: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 29cebba5-18e7-43e1-90d3-6424117ef1c2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent, reward functions are sampled from some prior reward distribution
- **Parent context**: Code has been implemented for training FRE agents

### R287: Code has been implemented such that when training a FRE-agen...
- **Rubric ID**: 4adeeba2-ffc3-4ed2-84a4-9f255c6706cc
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE-agent, the states are labeled with their associated reward as determined by the reward function sampled from the prior reward distribution
- **Parent context**: Code has been implemented for training FRE agents

### R288: Code has been implemented such that FB agents can be trained...
- **Rubric ID**: d3c7236a-5bab-4ed5-a07d-097d2b27a865
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that FB agents can be trained using the https://github.com/facebookresearch/controllable_agent codebase or a fork of it
- **Parent context**: Code has been implemented for training the necessary agent architectures

### R289: Code has been implemented such that SF agents can be trained...
- **Rubric ID**: f9a0f9f3-3224-4e5b-acd4-0ae6113bb505
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that SF agents can be trained using the https://github.com/facebookresearch/controllable_agent codebase or a fork of it
- **Parent context**: Code has been implemented for training the necessary agent architectures

### R290: Code has been implemented such that, to train OPAL agents, t...
- **Rubric ID**: 2507c345-a631-4170-89fe-ecf49b63c65f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that, to train OPAL agents, the OPAL autoencoding objective is used: maximizing log-likelihood of actions conditioned on latent $z$ and state, with a KL penalty to keep $q_\phi(z|\tau)$ close to $\rho_\omega(z|s_0)$.
- **Parent context**: Code has been implemented for training OPAL agents

### R291: Code has been implemented such that, to train OPAL agents, a...
- **Rubric ID**: 85fdbd9e-59b7-452f-bae7-0b771ecdf855
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that, to train OPAL agents, a low-level policy $\pi_\theta(a|s,z)$ can optionally be fine-tuned using latent-conditioned behavioral cloning on the same sub-trajectories (now labeled with $z$).
- **Parent context**: Code has been implemented for training OPAL agents

### R292: Code has been implemented such that when training GC-IQL age...
- **Rubric ID**: bb88edab-e4bf-490a-950b-72dd28682056
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training GC-IQL agents, the reward is 0 if the state==goal and -1 otherwise
- **Parent context**: Code has been implemented for training GC-IQL agents

### R293: Code has been implemented such that when training GC-IQL age...
- **Rubric ID**: 4712e793-7bdd-4035-9366-9f0d75a3ef51
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training GC-IQL agents, the critic is updated with an MSE loss to the Bellman target: r + discount * mask * next_value
- **Parent context**: Code has been implemented for training GC-IQL agents

### R294: Code has been implemented such that when training GC-IQL age...
- **Rubric ID**: 72e563cc-0eb9-48c6-b89e-45652db21c88
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training GC-IQL agents, the value function is updated with an expectile regression objective on the critic's Q-values
- **Parent context**: Code has been implemented for training GC-IQL agents

### R295: Code has been implemented such that when training GC-IQL age...
- **Rubric ID**: 28572598-c026-4643-a7b2-3e1105eefd4c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training GC-IQL agents, the actor is updated via advantage-weighted regression (AWR)
- **Parent context**: Code has been implemented for training GC-IQL agents

### R296: Code has been implemented such that when training GC-IQL age...
- **Rubric ID**: faa8f3bb-c478-47ad-b402-304d56c64e8d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training GC-IQL agents, after the critic update, the target critic is updated via a soft update rule from the critic params and previous target critic params.
- **Parent context**: Code has been implemented for training GC-IQL agents

### R297: Code has been implemented such that when training GC-IQL age...
- **Rubric ID**: 4da59d31-58f1-4fdf-8777-7a89fb85afdf
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training GC-IQL agents, the goal is concatenated to the current observation before feeding them into the actor, critic, target critic and value networks
- **Parent context**: Code has been implemented for training GC-IQL agents

### R298: Code has been implemented such that when training a GC-BC ag...
- **Rubric ID**: 4fd1ad12-90a5-468b-9b97-6580ca6e15f7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a GC-BC agent, hindsight relabeling is used to associate a goal state with each trajectory in the training set
- **Parent context**: Code has been implemented for training GC-BC agents

### R299: Code has been implemented such that when training a GC-BC ag...
- **Rubric ID**: 18d2e88d-002b-49dc-a5b9-dd002eb42bb4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a GC-BC agent, the trajectory's goal state is concatenated to the agent's input as a conditioning mechanism.
- **Parent context**: Code has been implemented for training GC-BC agents

### R300: Code has been implemented such that, when applying singleton...
- **Rubric ID**: 425c9fc8-538e-4143-abab-a33fa9e68d7f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that, when applying singleton goal-reaching reward functions to the trajectories of the `antmaze-large-diverse-v2` dataset, a goal is selected as a random state from the dataset with a probability of 0.2, a future state within the same trajectory with a probability of 0.5 and a completely random different state with a probability of 0.3
- **Parent context**: Code has been implemented such that singleton goal-reaching reward functions can be sampled and appl...

### R301: Code has been implemented such that when applying singleton...
- **Rubric ID**: 9d761158-1a97-467d-9390-5c34e5f0fbcf
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying singleton goal-reaching reward functions to the trajectoreis of the `antmaze-large-diverse-v2` dataset, a reward of -1 is assigned at every step unless the agent has reached the goal state.
- **Parent context**: Code has been implemented such that singleton goal-reaching reward functions can be sampled and appl...

### R302: Code has been implemented such that when applying random lin...
- **Rubric ID**: d2ad5f82-d2db-41c3-b970-e39b78fb8f63
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying random linear reward functions to the trajectories of the `antmaze-large-diverse-v2` dataset, the random vectors defining the functions are sampled from a uniform distribution bound between -1 and 1.
- **Parent context**: Code has been implemented such that random linear functions can be sampled and applied to the trajec...

### R303: Code has been implemented such that when applying random lin...
- **Rubric ID**: 76cccc3d-c5e9-4bba-acd1-806120e12801
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying random linear reward functions to the trajectories of the `antmaze-large-diverse-v2` dataset, a random binary mask with 0.9 probability of 0 is applied to the random vector defining the reward function.
- **Parent context**: Code has been implemented such that random linear functions can be sampled and applied to the trajec...

### R304: Code has been implemented such that when applying random lin...
- **Rubric ID**: abb3688b-9b8d-462a-8609-61b2c0769f79
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying random linear reward functions to the trajectories of the `antmaze-large-diverse-v2` dataset, a random binary mask with 0.9 probability of 0 is applied to the random vector defining the reward function.
- **Parent context**: Code has been implemented such that random linear functions can be sampled and applied to the trajec...

### R305: Code has been implemented such that when appying random MLP...
- **Rubric ID**: b8b9bd34-918e-45fb-a1bf-e8be3a65ec57
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of `antmaze-large-diverse-v2` dataset, the random MLPs consist of two linear layers, mapping from the state dimension to a hidden dimension of 32, and from 32 to and output dimension of 1.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R306: Code has been implemented such that when appying random MLP...
- **Rubric ID**: b2fddd01-5de1-41b6-baf4-e0aaa98df12e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of `antmaze-large-diverse-v2` dataset, the parameters of the random MLPs are sampled using a normal distribution scaled by the average dimension of the respective layer.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R307: Code has been implemented such that when appying random MLP...
- **Rubric ID**: 2f8b2fd8-e5ae-43b2-9ae9-eaebd81cca76
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of `antmaze-large-diverse-v2` dataset, a tanh activation function is used between the two linear layers.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R308: Code has been implemented such that when appying random MLP...
- **Rubric ID**: 98291113-8a01-4624-afcd-708d25c1f198
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of `antmaze-large-diverse-v2` dataset, the output of the MLPs is clipped between -1 and 1.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R309: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: b0d6d6b4-b7d7-4424-afc2-611090b447e5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-hint prior rewards distribution, the prior rewards distribution consists of all rewards corresponding to movement in a unit (x,y) direction.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-hint p...

### R310: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 61a28b5f-f2a6-4faa-a163-60b323098150
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-goals prior rewards distribution, only singleton goal-reaching reward functions are sampled and used for each training trajectory.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-goals ...

### R311: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 1cc28c97-59c7-4733-8a2e-45d44b367a2e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-lin prior rewards distribution, only random linear reward functions are sampled and used for each training trajectory.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-lin pr...

### R312: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: b08d7709-bb81-40f5-9a98-f48b7784cac3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-mlp prior rewards distribution, only random MLP reward functions are sampled and used for each training trajectory.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-mlp pr...

### R313: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: c9914ca1-9135-417d-be08-2c0772a1434b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-lin-mlp prior rewards distribution, there is an equal 0.5, 0.5 probability of sampling a random linear reward functions or a random mlp reward function for each training trajectory.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-lin-ml...

### R314: Code has been implemented such that an SF agent can be train...
- **Rubric ID**: 2cdf7237-9338-4c2b-8a83-d4ff80fc2b7d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that an SF agent can be trained on the Ant Maze `antmaze-large-diverse-v2` dataset
- **Parent context**: An SF agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset

### R315: Code has been implemented such that an GC-IQL agent can be t...
- **Rubric ID**: 3b6b5d48-afec-4ec3-b44f-3dd0119b28db
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that an GC-IQL agent can be trained on the Ant Maze `antmaze-large-diverse-v2` dataset
- **Parent context**: A GC-IQL agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset

### R316: Code has been implemented such that an GC-BC agent can be tr...
- **Rubric ID**: 1c9a402d-66ec-49db-88f3-9d2a1047bb8b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that an GC-BC agent can be trained on the Ant Maze `antmaze-large-diverse-v2` dataset
- **Parent context**: A GC-BC agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset

### R317: Code has been implemented such that, when applying singleton...
- **Rubric ID**: 9eec4876-cc5e-4748-9233-e2b38c2ee76e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that, when applying singleton goal-reaching reward functions to the trajectories of the ExORL `cheetah` (RND) dataset, a goal is selected as a random state from the dataset with a probability of 0.2, a future state within the same trajectory with a probability of 0.5 and a completely random different state with a probability of 0.3
- **Parent context**: Code has been implemented such that singleton goal-reaching reward functions can be sampled and appl...

### R318: Code has been implemented such that when applying singleton...
- **Rubric ID**: f97dff83-ed0b-4632-a8bd-07a70e7d1153
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying singleton goal-reaching reward functions to the trajectoreis of the ExORL `cheetah` (RND) dataset, a reward of -1 is assigned at every step unless the agent has reached the goal state.
- **Parent context**: Code has been implemented such that singleton goal-reaching reward functions can be sampled and appl...

### R319: Code has been implemented such that when applying random lin...
- **Rubric ID**: 25de5fa6-0439-4ff3-90ba-fcb19ba989a7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying random linear reward functions to the trajectories of the ExORL `cheetah` (RND) dataset, the random vectors defining the functions are sampled from a uniform distribution bound between -1 and 1.
- **Parent context**: Code has been implemented such that random linear functions can be sampled and applied to the trajec...

### R320: Code has been implemented such that when applying random lin...
- **Rubric ID**: 16c9bc52-89f6-4684-939f-e18d042bdea9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying random linear reward functions to the trajectories of the ExORL `cheetah` (RND) dataset, a random binary mask with 0.9 probability of 0 is applied to the random vector defining the reward function.
- **Parent context**: Code has been implemented such that random linear functions can be sampled and applied to the trajec...

### R321: Code has been implemented such that when applying random lin...
- **Rubric ID**: 59ba87e2-45ea-47ca-b97a-0346f531fb60
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying random linear reward functions to the trajectories of the ExORL `cheetah` (RND) dataset, a random binary mask with 0.9 probability of 0 is applied to the random vector defining the reward function.
- **Parent context**: Code has been implemented such that random linear functions can be sampled and applied to the trajec...

### R322: Code has been implemented such that when appying random MLP...
- **Rubric ID**: 9b800f88-cc3b-459d-b74f-90a64f5d0680
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of ExORL `cheetah` (RND) dataset, the random MLPs consist of two linear layers, mapping from the state dimension to a hidden dimension of 32, and from 32 to and output dimension of 1.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R323: Code has been implemented such that when appying random MLP...
- **Rubric ID**: 6ce5c5d8-9a04-4849-b7dc-003b567a045a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of ExORL `cheetah` (RND) dataset, the parameters of the random MLPs are sampled using a normal distribution scaled by the average dimension of the respective layer.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R324: Code has been implemented such that when appying random MLP...
- **Rubric ID**: 1d462431-8905-49eb-915d-004a2c91a148
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of ExORL `cheetah` (RND) dataset, a tanh activation function is used between the two linear layers.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R325: Code has been implemented such that when appying random MLP...
- **Rubric ID**: 96250516-ae2d-4f7e-a23e-9f39ce3def6f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of ExORL `cheetah` (RND) dataset, the output of the MLPs is clipped between -1 and 1.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R326: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 390a671a-f24d-4132-8971-005ccde1bcca
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the ExORL `cheetah` (RND) dataset using the FRE-hint prior rewards distribution, the prior rewards distribution consists of random initializations of reward functions rewarding the agent for moving in particular directions at particular speeds, forming a superset over the `exorl-cheetah-velocity` evaluation task.
- **Parent context**: A FRE agent has been trained on the ExORL `cheetah` (RND) dataset using the FRE-hint prior rewards d...

### R327: Code has been implemented such that an FB agent can be train...
- **Rubric ID**: 41b4a468-1be8-4629-b407-32282b33af31
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that an FB agent can be trained on the ExORL `cheetah` (RND) dataset
- **Parent context**: An FB agent has been trained on the ExORL `cheetah` (RND) dataset

### R328: Code has been implemented such that an OPAL agent can be tra...
- **Rubric ID**: 8c010722-eba2-499b-a633-a189df4dffd8
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that an OPAL agent can be trained on the ExORL `cheetah` (RND) dataset
- **Parent context**: An OPAL agent has been trained on the ExORL `cheetah` (RND) dataset

### R329: Code has been implemented such that an GC-IQL agent can be t...
- **Rubric ID**: 733cab32-1712-47d6-9db0-b06f6c6d2a24
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that an GC-IQL agent can be trained on the ExORL `cheetah` (RND) dataset
- **Parent context**: A GC-IQL agent has been trained on the ExORL `cheetah` (RND) dataset

### R330: Code has been implemented such that, when applying singleton...
- **Rubric ID**: c6e84c9a-f6b3-46a8-8c71-5d3c8412e7ee
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that, when applying singleton goal-reaching reward functions to the trajectories of the ExORL `walker` (RND) dataset, a goal is selected as a random state from the dataset with a probability of 0.2, a future state within the same trajectory with a probability of 0.5 and a completely random different state with a probability of 0.3
- **Parent context**: Code has been implemented such that singleton goal-reaching reward functions can be sampled and appl...

### R331: Code has been implemented such that when applying singleton...
- **Rubric ID**: d431628a-47c7-455b-b8a9-2fe4140cf9cb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying singleton goal-reaching reward functions to the trajectoreis of the ExORL `walker` (RND) dataset, a reward of -1 is assigned at every step unless the agent has reached the goal state.
- **Parent context**: Code has been implemented such that singleton goal-reaching reward functions can be sampled and appl...

### R332: Code has been implemented such that when applying random lin...
- **Rubric ID**: 85b2ac3b-353e-4e57-b72b-62b978d87bf6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying random linear reward functions to the trajectories of the ExORL `walker` (RND) dataset, the random vectors defining the functions are sampled from a uniform distribution bound between -1 and 1.
- **Parent context**: Code has been implemented such that random linear functions can be sampled and applied to the trajec...

### R333: Code has been implemented such that when applying random lin...
- **Rubric ID**: 8b2072db-4a70-4da4-9c35-8e3cb424f06f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying random linear reward functions to the trajectories of the ExORL `walker` (RND) dataset, a random binary mask with 0.9 probability of 0 is applied to the random vector defining the reward function.
- **Parent context**: Code has been implemented such that random linear functions can be sampled and applied to the trajec...

### R334: Code has been implemented such that when applying random lin...
- **Rubric ID**: d0abdeb0-751f-4dc5-86c5-107b0ea4ccf5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying random linear reward functions to the trajectories of the ExORL `walker` (RND) dataset, a random binary mask with 0.9 probability of 0 is applied to the random vector defining the reward function.
- **Parent context**: Code has been implemented such that random linear functions can be sampled and applied to the trajec...

### R335: Code has been implemented such that when appying random MLP...
- **Rubric ID**: d82b74a2-eb0d-41b8-9bd2-6da738987951
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of ExORL `walker` (RND) dataset, the random MLPs consist of two linear layers, mapping from the state dimension to a hidden dimension of 32, and from 32 to and output dimension of 1.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R336: Code has been implemented such that when appying random MLP...
- **Rubric ID**: be93b961-b705-4b4a-acf2-07cc02d9ed61
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of ExORL `walker` (RND) dataset, the parameters of the random MLPs are sampled using a normal distribution scaled by the average dimension of the respective layer.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R337: Code has been implemented such that when appying random MLP...
- **Rubric ID**: 54a70818-076a-4055-9796-a97fef49d0af
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of ExORL `walker` (RND) dataset, a tanh activation function is used between the two linear layers.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R338: Code has been implemented such that when appying random MLP...
- **Rubric ID**: 09b1a0d2-dc20-481e-9a0b-c4bde9fe4bed
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of ExORL `walker` (RND) dataset, the output of the MLPs is clipped between -1 and 1.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R339: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 20b53e62-fb49-41bf-8553-ac7a7a55a29d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the ExORL `walker` (RND) dataset using the FRE-all prior rewards distribution, there is an equal 0.33, 0.33, 0.33 probability of sampling a singleton goal-reaching reward function, a random linear reward functions or a random mlp reward function for each training trajectory.
- **Parent context**: A FRE agent has been trained on the ExORL `walker` (RND) dataset using the FRE-all prior rewards dis...

### R340: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: ff48b670-3096-4cf5-9fec-7a481540f46d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the ExORL `walker` (RND) dataset using the FRE-hint prior rewards distribution, the prior rewards distribution consists of random initializations of reward functions rewarding the agent for moving in particular directions at particular speeds, forming a superset over the `exorl-walker-velocity` evaluation task.
- **Parent context**: A FRE agent has been trained on the ExORL `walker` (RND) dataset using the FRE-hint prior rewards di...

### R341: Code has been implemented such that an FB agent can be train...
- **Rubric ID**: 36e66dbe-cb69-4d36-8bf8-60a29f3d08f0
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that an FB agent can be trained on the ExORL `walker` (RND) dataset
- **Parent context**: An FB agent has been trained on the ExORL `walker` (RND) dataset

### R342: Code has been implemented such that an SF agent can be train...
- **Rubric ID**: 0c8ac890-af63-4c26-b369-8296f7fdcd30
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that an SF agent can be trained on the ExORL `walker` (RND) dataset
- **Parent context**: An SF agent has been trained on the ExORL `walker` (RND) dataset

### R343: Code has been implemented such that an GC-IQL agent can be t...
- **Rubric ID**: 057833f3-bfae-4237-8b50-d360713cb0a9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that an GC-IQL agent can be trained on the ExORL `walker` (RND) dataset
- **Parent context**: A GC-IQL agent has been trained on the ExORL `walker` (RND) dataset

### R344: Code has been implemented such that an GC-BC agent can be tr...
- **Rubric ID**: bd31ca48-37ed-46dc-b12a-8283c37384dc
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that an GC-BC agent can be trained on the ExORL `walker` (RND) dataset
- **Parent context**: A GC-BC agent has been trained on the ExORL `walker` (RND) dataset

### R345: Code has been implemented such that, when applying singleton...
- **Rubric ID**: 2a86fe14-96c5-4940-8025-bac07f3ea724
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that, when applying singleton goal-reaching reward functions to the trajectories of the `kitchen-complete-v0` dataset, a goal is selected as a random state from the dataset with a probability of 0.2, a future state within the same trajectory with a probability of 0.5 and a completely random different state with a probability of 0.3
- **Parent context**: Code has been implemented such that singleton goal-reaching reward functions can be sampled and appl...

### R346: Code has been implemented such that when applying singleton...
- **Rubric ID**: 660e39bc-01ce-4487-819f-b192fcecd33e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying singleton goal-reaching reward functions to the trajectoreis of the `kitchen-complete-v0` dataset, a reward of -1 is assigned at every step unless the agent has reached the goal state.
- **Parent context**: Code has been implemented such that singleton goal-reaching reward functions can be sampled and appl...

### R347: Code has been implemented such that when applying random lin...
- **Rubric ID**: 29350167-f138-4491-84a2-fb69b3a42ee7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying random linear reward functions to the trajectories of the `kitchen-complete-v0` dataset, the random vectors defining the functions are sampled from a uniform distribution bound between -1 and 1.
- **Parent context**: Code has been implemented such that random linear functions can be sampled and applied to the trajec...

### R348: Code has been implemented such that when applying random lin...
- **Rubric ID**: c34f41d7-53a6-4ec3-b834-fc66c2971453
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying random linear reward functions to the trajectories of the `kitchen-complete-v0` dataset, a random binary mask with 0.9 probability of 0 is applied to the random vector defining the reward function.
- **Parent context**: Code has been implemented such that random linear functions can be sampled and applied to the trajec...

### R349: Code has been implemented such that when applying random lin...
- **Rubric ID**: 27c0c34f-ef21-413f-b9f2-eb930f369110
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when applying random linear reward functions to the trajectories of the `kitchen-complete-v0` dataset, a random binary mask with 0.9 probability of 0 is applied to the random vector defining the reward function.
- **Parent context**: Code has been implemented such that random linear functions can be sampled and applied to the trajec...

### R350: Code has been implemented such that when appying random MLP...
- **Rubric ID**: d62cd5d1-2d48-4511-bf4a-ba6f0ecabbde
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of `kitchen-complete-v0` dataset, the random MLPs consist of two linear layers, mapping from the state dimension to a hidden dimension of 32, and from 32 to and output dimension of 1.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R351: Code has been implemented such that when appying random MLP...
- **Rubric ID**: c87269a8-c3f8-4d69-b999-ca6d3582b78c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of `kitchen-complete-v0` dataset, the parameters of the random MLPs are sampled using a normal distribution scaled by the average dimension of the respective layer.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R352: Code has been implemented such that when appying random MLP...
- **Rubric ID**: 42273065-fd8b-4e08-b279-0384aa33430f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of `kitchen-complete-v0` dataset, a tanh activation function is used between the two linear layers.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R353: Code has been implemented such that when appying random MLP...
- **Rubric ID**: 194f8a3e-4da1-4384-92d6-7a7d58cdcccd
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when appying random MLP reward functions to the trajectories of `kitchen-complete-v0` dataset, the output of the MLPs is clipped between -1 and 1.
- **Parent context**: Code has been implemented such that random MLP functions can be sampled and applied to the trajector...

### R354: Code has been implemented such that an SF agent can be train...
- **Rubric ID**: 33f254f6-e00a-4c5a-8bbd-9349c4c01398
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that an SF agent can be trained on the `kitchen-complete-v0` dataset
- **Parent context**: An SF agent has been trained on the `kitchen-complete-v0` dataset

### R355: Code has been implemented such that an GC-BC agent can be tr...
- **Rubric ID**: 5d1739d9-997b-4fff-ae36-7fbdf7ff8071
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that an GC-BC agent can be trained on the `kitchen-complete-v0` dataset
- **Parent context**: A GC-BC agent has been trained on the `kitchen-complete-v0` dataset

### R356: Code has been implemented such that the additional physics i...
- **Rubric ID**: a92f411b-2e8f-444c-9af5-1dc116d8f281
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the additional physics information outlined in Appendix C.2 is appended to the environment state when evaluating the FRE agent on the ExORL `cheetah` and `walker` tasks
- **Parent context**: Code has been implemented for evaluating FRE agents

## Experimental Setup

### R357: The FRE encoder has been implemented using the hyper-paramet...
- **Rubric ID**: aa264dc2-4e1b-4301-9dd6-770c0d5c3081
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The FRE encoder has been implemented using the hyper-parameters specified in Appendix A
- **Parent context**: The FRE Encoder network has been implemented

### R358: The FRE Decoder has been implemented using the hyper-paramet...
- **Rubric ID**: 6d38f122-a3dd-464b-8a85-37f2fd538364
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The FRE Decoder has been implemented using the hyper-parameters specified in Appendix A
- **Parent context**: The FRE decoder network has been implemented

### R359: The FRE-conditioned policy has been implemented using the hy...
- **Rubric ID**: 143af012-ca25-4037-a318-f17f62e7e984
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The FRE-conditioned policy has been implemented using the hyper-parameters specified in Appendix A
- **Parent context**: The FRE-conditioned policy network has been implemented

### R360: The OPAL encoder has been implemented such that it uses a pe...
- **Rubric ID**: 431ad005-008b-4745-aa6a-db4c70ff16f1
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The OPAL encoder has been implemented such that it uses a permutation invariant transformer set up with the relevant hyper-parameters specified in Appendix A
- **Parent context**: The OPAL encoder architecture $q_{\phi}(z\mid\tau)$ has been implemented

### R361: Code has been implemented such that FRE training is strided:...
- **Rubric ID**: bad4958f-dcc0-4f8f-9328-198a6b1d58d1
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that FRE training is strided: In the first phase the encoder-decoder is trained. In the second phase, the encoder is kept frozen while its outputs are used to condition the IQL policy. The IQL policy is trained during this second phase. The decoder is not used in the second phase.
- **Parent context**: Code has been implemented for training FRE agents

### R362: Code has been implemented such that in general, training a F...
- **Rubric ID**: 3ef7f2f7-3243-4a49-815a-d2b38591b186
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that in general, training a FRE agent follows the steps outlined in algorithm 1.
- **Parent context**: Code has been implemented for training FRE agents

### R363: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 91a5d50c-97a3-4c35-ad49-35020d674b3b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent, the hyper-parameters outlined in Appendix A are used.
- **Parent context**: Code has been implemented for training FRE agents

### R364: Code has been implemented such that when training a GC-BC ag...
- **Rubric ID**: ae220267-1fb7-419b-ab43-f0f80371275b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a GC-BC agent, the negative log likelihood between the GC-BC agent's predicted action distribution and the ground truth action from the training dataset is used as the loss function to be optimized
- **Parent context**: Code has been implemented for training GC-BC agents

### R365: Code has been implemented such that when training a GC-BC ag...
- **Rubric ID**: afa01ba7-dc47-470c-9c89-408c2fbc8420
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a GC-BC agent, no reward information or reinforcement learning is used
- **Parent context**: Code has been implemented for training GC-BC agents

### R366: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: df64e51f-da9f-4fd0-9a2c-c8d6dbd53e96
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-all prior rewards distribution, the training and architecture hyperparameters specified in Appendix A are used.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-all pr...

### R367: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 8d4bd046-febb-441e-af20-03a543ae4cea
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-all prior rewards distribution, there is an equal 0.33, 0.33, 0.33 probability of sampling a singleton goal-reaching reward function, a random linear reward functions or a random mlp reward function for each training trajectory.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-all pr...

### R368: A FRE agent has been trained on the Ant Maze `antmaze-large-...
- **Rubric ID**: 64d49648-6eab-4147-b455-a606c2d70473
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-all prior rewards distribution
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-all pr...

### R369: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 6c4fce0f-cda0-443e-81a0-8dc320d5e107
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-hint prior rewards distribution, the training and architecture hyperparameters specified in Appendix A are used.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-hint p...

### R370: A FRE agent has been trained on the Ant Maze `antmaze-large-...
- **Rubric ID**: 6a19acfd-2ce1-43a8-b47c-2303f1329626
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-hint prior rewards distribution
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-hint p...

### R371: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 8cd85ad2-a145-4bb7-97c4-7cb1bbd40569
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-goals prior rewards distribution, the training and architecture hyperparameters specified in Appendix A are used.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-goals ...

### R372: A FRE agent has been trained on the Ant Maze `antmaze-large-...
- **Rubric ID**: b40be6bd-1225-4755-b60e-dd16f5e43665
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-goals prior rewards distribution
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-goals ...

### R373: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 61af561b-335b-47bb-a194-c47827bac7e9
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-lin prior rewards distribution, the training and architecture hyperparameters specified in Appendix A are used.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-lin pr...

### R374: A FRE agent has been trained on the Ant Maze `antmaze-large-...
- **Rubric ID**: a7667234-841f-4a08-8f9a-4b23cebb1c94
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-lin prior rewards distribution
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-lin pr...

### R375: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 6e6558f9-765b-463e-a170-becf47ed9f0c
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-mlp prior rewards distribution, the training and architecture hyperparameters specified in Appendix A are used.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-mlp pr...

### R376: A FRE agent has been trained on the Ant Maze `antmaze-large-...
- **Rubric ID**: e32669f0-98fb-4248-a7a1-54d73a66280b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-mlp prior rewards distribution
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-mlp pr...

### R377: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 03cec4d5-1fc2-488e-a786-975793861d3f
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-lin-mlp prior rewards distribution, the training and architecture hyperparameters specified in Appendix A are used.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-lin-ml...

### R378: A FRE agent has been trained on the Ant Maze `antmaze-large-...
- **Rubric ID**: 3c1fee00-9a97-483e-91a2-4937c4e814e6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-lin-mlp prior rewards distribution
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-lin-ml...

### R379: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 1b4a1806-0a39-400a-8b12-91a75db328e2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-goal-mlp prior rewards distribution, the training and architecture hyperparameters specified in Appendix A are used.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-goal-m...

### R380: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: d31b56be-b137-4f5f-a065-2bb280e18855
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-goal-mlp prior rewards distribution, there is an equal 0.5, 0.5 probability of sampling a singleton goal-reaching reward function or a random mlp reward function for each training trajectory.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-goal-m...

### R381: A FRE agent has been trained on the Ant Maze `antmaze-large-...
- **Rubric ID**: 7e2f3082-ede8-48f2-a9a7-b65457dcf704
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-goal-mlp prior rewards distribution
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-goal-m...

### R382: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 3963a475-7aeb-417b-9391-e5fbbd503cc1
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-goal-lin prior rewards distribution, the training and architecture hyperparameters specified in Appendix A are used.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-goal-l...

### R383: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 7d9b1fe6-0cd5-4751-8368-b6119eb535b0
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the Ant MazE `antmaze-large-diverse-v2` dataset using the FRE-goal-lin prior rewards distribution, there is an equal 0.5, 0.5 probability of sampling a singleton goal-reaching reward function or a random linear reward function for each training trajectory.
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-goal-l...

### R384: A FRE agent has been trained on the Ant Maze `antmaze-large-...
- **Rubric ID**: fcb3612a-7c05-44e2-b2c1-fee7f06ab6f2
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-goal-lin prior rewards distribution
- **Parent context**: A FRE agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset using the FRE-goal-l...

### R385: Code has been implemented such that an FB agent can be train...
- **Rubric ID**: 14d5ca37-69e4-419d-add4-b87fa29d5ffe
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that an FB agent can be trained on the Ant Maze `antmaze-large-diverse-v2` dataset
- **Parent context**: An FB agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset

### R386: An FB agent has been trained on the Ant Maze `antmaze-large-...
- **Rubric ID**: 6db428ff-d03c-4656-99a2-df1d2ed72393
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An FB agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset
- **Parent context**: An FB agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset

### R387: An SF agent has been trained on the Ant Maze `antmaze-large-...
- **Rubric ID**: 068a7499-5d33-4770-8b75-34d5d26f5089
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An SF agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset
- **Parent context**: An SF agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset

### R388: Code has been implemented such that an OPAL agent can be tra...
- **Rubric ID**: 3d7c6335-03c0-494f-88a7-6d8b7913f2b1
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that an OPAL agent can be trained on the Ant Maze `antmaze-large-diverse-v2` dataset
- **Parent context**: An OPAL agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset

### R389: An OPAL agent has been trained on the Ant Maze `antmaze-larg...
- **Rubric ID**: 617c421b-1bcd-4b92-9e4f-39f8e06c1cc4
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An OPAL agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset
- **Parent context**: An OPAL agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset

### R390: An GC-IQL agent has been trained on the Ant Maze `antmaze-la...
- **Rubric ID**: f4f6c096-cb80-43cc-a32b-d11b02b48264
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An GC-IQL agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset
- **Parent context**: A GC-IQL agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset

### R391: An GC-BC agent has been trained on the Ant Maze `antmaze-lar...
- **Rubric ID**: 65f07ab6-1d8b-43b6-bf2f-0f2f637504d0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An GC-BC agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset
- **Parent context**: A GC-BC agent has been trained on the Ant Maze `antmaze-large-diverse-v2` dataset

### R392: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 5508cfda-56f4-48fd-b0bd-a417a43743d3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the ExORL `cheetah` (RND) dataset using the FRE-all prior rewards distribution, the training and architecture hyperparameters specified in Appendix A are used.
- **Parent context**: A FRE agent has been trained on the ExORL `cheetah` (RND) dataset using the FRE-all prior rewards di...

### R393: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: a51dc0ea-9fd5-492b-9adc-cea1865dad5e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the ExORL `cheetah` (RND) dataset using the FRE-all prior rewards distribution, there is an equal 0.33, 0.33, 0.33 probability of sampling a singleton goal-reaching reward function, a random linear reward functions or a random mlp reward function for each training trajectory.
- **Parent context**: A FRE agent has been trained on the ExORL `cheetah` (RND) dataset using the FRE-all prior rewards di...

### R394: A FRE agent has been trained on the ExORL `cheetah` (RND) da...
- **Rubric ID**: 0b794c64-9483-4ca3-9097-901ed7a7c635
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A FRE agent has been trained on the ExORL `cheetah` (RND) dataset using the FRE-all prior rewards distribution
- **Parent context**: A FRE agent has been trained on the ExORL `cheetah` (RND) dataset using the FRE-all prior rewards di...

### R395: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 631eca30-68dd-413e-b88f-21e1782fc3ba
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the ExORL `cheetah` (RND) dataset using the FRE-hint prior rewards distribution, the training and architecture hyperparameters specified in Appendix A are used.
- **Parent context**: A FRE agent has been trained on the ExORL `cheetah` (RND) dataset using the FRE-hint prior rewards d...

### R396: A FRE agent has been trained on the ExORL `cheetah` (RND) da...
- **Rubric ID**: a2b00b9a-dc67-4a00-9540-5469b7640e5f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A FRE agent has been trained on the ExORL `cheetah` (RND) dataset using the FRE-hint prior rewards distribution
- **Parent context**: A FRE agent has been trained on the ExORL `cheetah` (RND) dataset using the FRE-hint prior rewards d...

### R397: An FB agent has been trained on the ExORL `cheetah` (RND) da...
- **Rubric ID**: a65e7075-f6cc-44e6-9854-5ec55a16a67e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An FB agent has been trained on the ExORL `cheetah` (RND) dataset
- **Parent context**: An FB agent has been trained on the ExORL `cheetah` (RND) dataset

### R398: Code has been implemented such that an SF agent can be train...
- **Rubric ID**: 56b2fd60-2110-4e3b-b7a9-8912e9b6593f
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that an SF agent can be trained on the ExORL `cheetah` (RND) dataset
- **Parent context**: An SF agent has been trained on the ExORL `cheetah` (RND) dataset

### R399: An SF agent has been trained on the ExORL `cheetah` (RND) da...
- **Rubric ID**: d16f1c7f-19b7-4385-a869-799c7f897486
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An SF agent has been trained on the ExORL `cheetah` (RND) dataset
- **Parent context**: An SF agent has been trained on the ExORL `cheetah` (RND) dataset

### R400: An OPAL agent has been trained on the ExORL `cheetah` (RND)...
- **Rubric ID**: 577c9728-b03f-4836-912b-242b0dab0836
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An OPAL agent has been trained on the ExORL `cheetah` (RND) dataset
- **Parent context**: An OPAL agent has been trained on the ExORL `cheetah` (RND) dataset

### R401: An GC-IQL agent has been trained on the ExORL `cheetah` (RND...
- **Rubric ID**: 6b8fdb2d-4089-4fd3-bf64-2c47c3acc811
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An GC-IQL agent has been trained on the ExORL `cheetah` (RND) dataset
- **Parent context**: A GC-IQL agent has been trained on the ExORL `cheetah` (RND) dataset

### R402: Code has been implemented such that an GC-BC agent can be tr...
- **Rubric ID**: 27fdf748-2d6c-4b43-bf65-3a7173f12a3e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that an GC-BC agent can be trained on the ExORL `cheetah` (RND) dataset
- **Parent context**: A GC-BC agent has been trained on the ExORL `cheetah` (RND) dataset

### R403: An GC-BC agent has been trained on the ExORL `cheetah` (RND)...
- **Rubric ID**: d27214c8-a231-46fb-af22-7db92d29a990
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An GC-BC agent has been trained on the ExORL `cheetah` (RND) dataset
- **Parent context**: A GC-BC agent has been trained on the ExORL `cheetah` (RND) dataset

### R404: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 11bd7539-4847-405c-ae7f-a0b616d73305
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the ExORL `walker` (RND) dataset using the FRE-all prior rewards distribution, the training and architecture hyperparameters specified in Appendix A are used.
- **Parent context**: A FRE agent has been trained on the ExORL `walker` (RND) dataset using the FRE-all prior rewards dis...

### R405: A FRE agent has been trained on the ExORL `walker` (RND) dat...
- **Rubric ID**: 9e20fc23-3d36-4bdb-8165-289b0d3b6952
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A FRE agent has been trained on the ExORL `walker` (RND) dataset using the FRE-all prior rewards distribution
- **Parent context**: A FRE agent has been trained on the ExORL `walker` (RND) dataset using the FRE-all prior rewards dis...

### R406: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 77f406ad-abab-4468-be37-d6ed28067dc7
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the ExORL `walker` (RND) dataset using the FRE-hint prior rewards distribution, the training and architecture hyperparameters specified in Appendix A are used.
- **Parent context**: A FRE agent has been trained on the ExORL `walker` (RND) dataset using the FRE-hint prior rewards di...

### R407: A FRE agent has been trained on the ExORL `walker` (RND) dat...
- **Rubric ID**: 39866a97-304e-47e8-b3fe-e263fc5cb643
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A FRE agent has been trained on the ExORL `walker` (RND) dataset using the FRE-hint prior rewards distribution
- **Parent context**: A FRE agent has been trained on the ExORL `walker` (RND) dataset using the FRE-hint prior rewards di...

### R408: An FB agent has been trained on the ExORL `walker` (RND) dat...
- **Rubric ID**: 9c9a94c6-dce1-417a-bd29-5e0e5ce0c541
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An FB agent has been trained on the ExORL `walker` (RND) dataset
- **Parent context**: An FB agent has been trained on the ExORL `walker` (RND) dataset

### R409: An SF agent has been trained on the ExORL `walker` (RND) dat...
- **Rubric ID**: 7a319144-0829-4662-bb5d-577dc3f22878
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An SF agent has been trained on the ExORL `walker` (RND) dataset
- **Parent context**: An SF agent has been trained on the ExORL `walker` (RND) dataset

### R410: Code has been implemented such that an OPAL agent can be tra...
- **Rubric ID**: 126dfc88-a0b1-4ba6-bc8c-bf9772c41a11
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that an OPAL agent can be trained on the ExORL `walker` (RND) dataset
- **Parent context**: An OPAL agent has been trained on the ExORL `walker` (RND) dataset

### R411: An OPAL agent has been trained on the ExORL `walker` (RND) d...
- **Rubric ID**: d463b992-ec5d-4ce0-9f05-a8b73bf2b605
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An OPAL agent has been trained on the ExORL `walker` (RND) dataset
- **Parent context**: An OPAL agent has been trained on the ExORL `walker` (RND) dataset

### R412: An GC-IQL agent has been trained on the ExORL `walker` (RND)...
- **Rubric ID**: 68fbf341-5861-4b78-9733-bd5579659789
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An GC-IQL agent has been trained on the ExORL `walker` (RND) dataset
- **Parent context**: A GC-IQL agent has been trained on the ExORL `walker` (RND) dataset

### R413: An GC-BC agent has been trained on the ExORL `walker` (RND)...
- **Rubric ID**: badabb41-0321-4828-a655-9f0251427dee
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An GC-BC agent has been trained on the ExORL `walker` (RND) dataset
- **Parent context**: A GC-BC agent has been trained on the ExORL `walker` (RND) dataset

### R414: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 2eb7183e-dfe1-433b-8f22-5afc08076539
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the `kitchen-complete-v0` dataset using the FRE-all prior rewards distribution, the training and architecture hyperparameters specified in Appendix A are used.
- **Parent context**: A FRE agent has been trained on the `kitchen-complete-v0` dataset using the FRE-all prior rewards di...

### R415: Code has been implemented such that when training a FRE agen...
- **Rubric ID**: 83202f54-a253-445f-87c5-b20c2073cf85
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when training a FRE agent on the `kitchen-complete-v0` dataset using the FRE-all prior rewards distribution, there is an equal 0.33, 0.33, 0.33 probability of sampling a singleton goal-reaching reward function, a random linear reward functions or a random mlp reward function for each training trajectory.
- **Parent context**: A FRE agent has been trained on the `kitchen-complete-v0` dataset using the FRE-all prior rewards di...

### R416: A FRE agent has been trained on the `kitchen-complete-v0` da...
- **Rubric ID**: 4c9cfa23-a8b8-478e-998e-a4a1f0a0d2f6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A FRE agent has been trained on the `kitchen-complete-v0` dataset using the FRE-all prior rewards distribution
- **Parent context**: A FRE agent has been trained on the `kitchen-complete-v0` dataset using the FRE-all prior rewards di...

### R417: Code has been implemented such that an FB agent can be train...
- **Rubric ID**: 7936e1fc-9a80-4a68-b0ca-d270b1807d1e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that an FB agent can be trained on the `kitchen-complete-v0` dataset
- **Parent context**: An FB agent has been trained on the `kitchen-complete-v0` dataset

### R418: An FB agent has been trained on the `kitchen-complete-v0` da...
- **Rubric ID**: 73895090-ddd8-49e8-b96f-2292783faf28
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An FB agent has been trained on the `kitchen-complete-v0` dataset
- **Parent context**: An FB agent has been trained on the `kitchen-complete-v0` dataset

### R419: An SF agent has been trained on the `kitchen-complete-v0` da...
- **Rubric ID**: 7c051e05-5a4c-4e5e-9532-79ae9d4b4d3d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An SF agent has been trained on the `kitchen-complete-v0` dataset
- **Parent context**: An SF agent has been trained on the `kitchen-complete-v0` dataset

### R420: Code has been implemented such that an OPAL agent can be tra...
- **Rubric ID**: f901be1c-2239-4d5c-b34c-9a839842fbe4
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that an OPAL agent can be trained on the `kitchen-complete-v0` dataset
- **Parent context**: An OPAL agent has been trained on the `kitchen-complete-v0` dataset

### R421: An OPAL agent has been trained on the `kitchen-complete-v0`...
- **Rubric ID**: 3d1b54ba-72e5-4bbd-9caf-f08ec6952a55
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An OPAL agent has been trained on the `kitchen-complete-v0` dataset
- **Parent context**: An OPAL agent has been trained on the `kitchen-complete-v0` dataset

### R422: Code has been implemented such that an GC-IQL agent can be t...
- **Rubric ID**: 5a20458c-8da5-4b52-a5a0-8dc6831385bf
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that an GC-IQL agent can be trained on the `kitchen-complete-v0` dataset
- **Parent context**: A GC-IQL agent has been trained on the `kitchen-complete-v0` dataset

### R423: An GC-IQL agent has been trained on the `kitchen-complete-v0...
- **Rubric ID**: d1249f99-5619-495f-9692-abfc733cc3fa
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An GC-IQL agent has been trained on the `kitchen-complete-v0` dataset
- **Parent context**: A GC-IQL agent has been trained on the `kitchen-complete-v0` dataset

### R424: An GC-BC agent has been trained on the `kitchen-complete-v0`...
- **Rubric ID**: 56f5605d-331a-4ca5-aeba-c747321616f9
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: An GC-BC agent has been trained on the `kitchen-complete-v0` dataset
- **Parent context**: A GC-BC agent has been trained on the `kitchen-complete-v0` dataset

### R425: Code has been implemented such that when evaluating GC-BC ag...
- **Rubric ID**: 3900f1ca-dbc3-4976-a397-847a0661c8c4
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when evaluating GC-BC agents, the goal state is made available to the agent at the beginning of the rollout
- **Parent context**: Code has been implemented for evaluating GC-BC agents

### R426: Code has been implemented such that during the evaluation of...
- **Rubric ID**: ed6854c2-5521-431a-9aa3-3b0efc4aaaf1
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that during the evaluation of Ant Maze tasks, trajectories are limited to a maximum of 2000 steps.
- **Parent context**: The necessary agents have been evaluated on the Ant Maze evaluation tasks

### R427: Code has been implemented such that during the evaluation of...
- **Rubric ID**: 73141dba-08d8-47a8-b616-ecd160f31f4a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that during the evaluation of ExORL tasks, trajectories are limited to a maximum of 1000 steps.
- **Parent context**: The necessary agents have been evaluated on the ExORL evaluation tasks

## Data Processing & Preparation

### R428: Code has been implemented such that the observation space's...
- **Rubric ID**: f9cc6afc-346e-4f24-b8c5-63ce36bb74b6
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the observation space's XY coordinates are discretized into 32 bins for input to FRE agents trained on Ant Maze dataset
- **Parent context**: Code has been implemented for training FRE agents

### R429: Code has been implemented such that the additional physics i...
- **Rubric ID**: 2ed48cb3-713f-44b0-b318-591d610cffd3
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the additional physics information outlined in Appendix C.2 is appended to the environment state when training the FRE encoder on the ExORL `cheetah` and `walker` (RND) datasets
- **Parent context**: Code has been implemented for training FRE agents

### R430: Code has been implemented such that, to train OPAL agents, s...
- **Rubric ID**: caaf32fc-df77-4d3b-8f74-de48997e4b97
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been implemented such that, to train OPAL agents, sub-trajectories of some length c can be sampled from the offline dataset (e.g. c=10), forming the data used to learn OPAL's encoder and decoder (primitive policy). No reward information is used at this stage.
- **Parent context**: Code has been implemented for training OPAL agents

### R431: Code has been implemented such that the observation space's...
- **Rubric ID**: f6c9dda4-677f-4781-ad6a-be15de0e20b0
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the observation space's XY coordinates are discretized into 32 bins for input to OPAL agents trained on Ant Maze dataset
- **Parent context**: Code has been implemented for training OPAL agents

### R432: Code has been implemented such that the observation space's...
- **Rubric ID**: d4fb400c-5b88-452f-b138-ca5f43f7313f
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the observation space's XY coordinates are discretized into 32 bins for input to GC-IQL agents trained on Ant Maze dataset
- **Parent context**: Code has been implemented for training GC-IQL agents

### R433: Code has been implemented such that the observation space's...
- **Rubric ID**: 9cbeb1b9-465f-414c-8287-69284c0d3b26
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the observation space's XY coordinates are discretized into 32 bins for input to GC-BC agents trained on Ant Maze dataset
- **Parent context**: Code has been implemented for training GC-BC agents

### R434: Code has been implemented such that the observation space's...
- **Rubric ID**: b2f98ca4-2805-4e7c-afa2-16f58c8fb4d4
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the observation space's XY coordinates are discretized into 32 bins for input to FRE agents evaluated on Ant Maze environments
- **Parent context**: Code has been implemented for evaluating FRE agents

### R435: Code has been implemented such that the observation space's...
- **Rubric ID**: c3dd8354-9247-4d2b-89fa-e46534fef3ee
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the observation space's XY coordinates are discretized into 32 bins for input to OPAL agents evaluated on Ant Maze environments
- **Parent context**: Code has been implemented for evaluating OPAL agents

### R436: Code has been implemented such that the observation space's...
- **Rubric ID**: 3eab10fb-3d76-484e-9ffb-16ab6b7fdeda
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the observation space's XY coordinates are discretized into 32 bins for input to GC-BC agents evaluated on Ant Maze environments
- **Parent context**: Code has been implemented for evaluating GC-BC agents

### R437: Code has been implemented such that the observation space's...
- **Rubric ID**: 1d10e358-68ab-4f7b-8343-9a92f71edd5e
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the observation space's XY coordinates are discretized into 32 bins for input to GC-IQL agents evaluated on Ant Maze environments
- **Parent context**: Code has been implemented for evaluating GC-IQL agents
