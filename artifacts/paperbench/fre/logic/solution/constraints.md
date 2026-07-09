# Constraints

## Boundary Conditions

### BC1: Offline-Only Training
- FRE requires an offline dataset D of state-action trajectories. No online environment interaction is permitted during pre-training.
- Failure mode: If the offline dataset has poor coverage of the state space relevant to downstream tasks, the encoder will be unable to generate informative z embeddings at test time.

### BC2: Fixed K=32 Encoding Budget
- The FRE encoder uses exactly K=32 (state, reward) samples to produce z at test time. Performance may degrade if the downstream reward function requires more samples for accurate estimation.
- Boundary: FB/SF methods use K=5120 samples via linear regression; FRE is designed for extreme sample efficiency but is not tested outside K=32 at evaluation.

### BC3: State-Space Reward Functions
- FRE assumes reward functions η: S → ℝ are functions of state (not joint state-action). Physics-based rewards (ExORL velocity/torso) require appending auxiliary physics state information to the observation for encoding.
- Extension: The paper notes reward functions may depend on (s, a) without loss of generality.

### BC4: Shared Environment Dynamics
- All downstream tasks must share the same MDP dynamics as the pre-training environment. FRE does not handle domain adaptation or transfer across different physical systems.

### BC5: Prior Coverage Assumption
- The random unsupervised reward prior p(η) must approximately span the space of downstream tasks. If a test task is fundamentally dissimilar to anything in the prior (e.g., a game-theoretic adversarial reward), FRE may fail to encode it accurately.
- No Free Lunch: Completely random functions lead to incompressible representations.

### BC6: Strided Training Required for Stability
- Joint training of encoder and IQL policy leads to non-stationary TD targets and unstable learning. The strided protocol (freeze encoder before policy training) is required.

## Known Limitations

### L1: Ad hoc reward prior
- The mixture of goal-reaching, linear, and MLP rewards is chosen empirically. There is no principled method to determine the optimal prior for a given domain.

### L2: No online setting
- FRE is formulated as offline RL only. Extension to online interaction is identified as future work.

### L3: AntMaze XY scale instability
- Random linear reward functions on AntMaze exclude XY dimensions due to scale differences causing training instability.

### L4: Out-of-distribution state failures
- In AntMaze evaluations, policy trajectories occasionally fail when encountering OOD states, consistent with standard offline RL limitations (Kumar et al., 2020).

### L5: Fixed latent dimensionality
- The latent dimension of z is fixed; it is not adjusted adaptively based on reward function complexity.
