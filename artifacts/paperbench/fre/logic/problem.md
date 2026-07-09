# Problem Specification

## Observations

### O1: Large unlabeled offline datasets exist but lack reward annotations
- **Statement**: Large offline RL datasets such as ExORL (Yarats et al., 2022) consist of trajectories collected by exploratory policies without any reward labels or task intent.
- **Evidence**: ExORL benchmark contains trajectories from DMControl tasks with no reward signal; D4RL AntMaze and Kitchen provide state-action data with limited task coverage.
- **Implication**: Reward annotation is expensive; any general pre-training method must work from raw trajectory data alone.

### O2: Prior zero-shot RL methods impose linear reward structure constraints
- **Statement**: Successor Feature (SF) methods (Barreto et al., 2017; Borsa et al., 2018) and Forward-Backward (FB) methods (Touati & Ollivier, 2021; Touati et al., 2022) learn value functions only in the linear span of state features, restricting generalization to non-linear reward functions.
- **Evidence**: FB/SF performance collapses on non-goal-reaching tasks (directional, simplex, path tasks) as shown in Table 1 of the paper.
- **Implication**: Linear reward structure is a fundamental limitation for general zero-shot RL.

### O3: Goal-conditioned methods cannot solve non-goal-reaching tasks
- **Statement**: GC-IQL and GC-BC score near zero on directional, random-simplex, and structured-path tasks (Table 1), since they specialize in goal-conditioned policies.
- **Evidence**: ant-directional: GC-IQL=4.8±14, GC-BC=6.5±16 vs. FRE=55.2±8; ant-random-simplex: GC-IQL=9.7±2, GC-BC=8.5±10 vs. FRE=21.3±4.
- **Implication**: A general zero-shot agent must handle arbitrary reward structures beyond goal-reaching.

### O4: At test time, reward annotations are available only as a small sample
- **Statement**: Downstream tasks are specified as reward functions η : S → ℝ, but only a small number of (s, η(s)) tuples are available. FRE uses K=32 samples; FB/SF methods use 5120.
- **Evidence**: Section 3 problem setting; Table 1 footnote specifying evaluation sample counts.
- **Implication**: Test-time task identification must be efficient in sample count.

## Gaps

### G1: No method simultaneously handles goal-reaching AND arbitrary reward functions
- **Statement**: Existing zero-shot RL methods either handle goal-reaching well (GC-IQL, GC-BC) or structured linear rewards (FB, SF), but not both.
- **Caused by**: O2, O3
- **Existing attempts**: FB unifies tasks through linearized value functions; OPAL learns skills via behavioral cloning but lacks zero-shot adaptation.
- **Why they fail**: Linear function approximation in SF/FB limits coverage; goal-conditioning restricts the reward family to {reach state g}.

### G2: No domain-agnostic prior over reward functions for unsupervised pre-training
- **Statement**: Without knowing downstream tasks, we need a prior p(η) that broadly spans possible objectives without requiring domain-specific task annotations.
- **Caused by**: O1, O4
- **Existing attempts**: Random MDP reward functions are too unstructured (No Free Lunch); manually designed task sets require human effort.
- **Why they fail**: Purely random functions lead to incompressible representations; structured priors require domain knowledge.

### G3: Offline RL with multi-task non-stationary reward encoding is unstable
- **Statement**: Jointly training a task encoder and policy via TD learning leads to non-stationarity in the Q-function targets, since z changes during training.
- **Caused by**: O1 (offline setting), G1
- **Existing attempts**: End-to-end training of encoder and policy.
- **Why they fail**: Changing encoder outputs break the assumption of a stationary reward signal required for convergent TD learning.

## Key Insight

- **Insight**: A reward function η : S → ℝ can be fully characterized by its values on a finite set of states drawn from the offline dataset. By training a permutation-invariant encoder to compress these (s, η(s)) pairs into a latent z that can predict η on held-out states, we obtain a universal and data-scalable task representation that supports both pre-training (over random η) and zero-shot inference (encoding any new η from K samples).
- **Derived from**: O1, O2, O3, O4
- **Enables**: (1) Training an FRE-conditioned policy on a diverse mixture of unsupervised reward functions, and (2) zero-shot identification of any downstream task by encoding K=32 annotated samples through the frozen FRE encoder.

## Assumptions

- A1: Downstream reward functions are approximately "compressible" from a modest number of state-reward samples (K=32 is sufficient for encoding).
- A2: The offline dataset covers states relevant to downstream tasks (i.e., distribution shift between training and test states is manageable).
- A3: The prior reward distribution (singleton goals, random linear, random MLP) sufficiently spans the space of downstream rewards encountered at test time.
- A4: Offline RL (IQL) can learn good multi-task policies given fixed (frozen) task embeddings z.
