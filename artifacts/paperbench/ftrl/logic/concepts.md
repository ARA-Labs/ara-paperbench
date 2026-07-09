# Concepts

## Forgetting of Pre-trained Capabilities (FPC)
- **Notation**: FPC
- **Definition**: The phenomenon by which a pre-trained RL agent loses its competence on parts of the state space not visited during the initial phase of fine-tuning, due to gradient interference in the function approximator when training on initially-visited states. Formally: let π* be the pre-trained policy, πθ(t) the fine-tuned policy at time t. FPC occurs when ∃S_FAR ⊆ S such that J(πθ(t), S_FAR) < J(π*, S_FAR) for t > 0 during the early fine-tuning phase, where J measures performance on a state subset.
- **Boundary conditions**: Requires a feedback loop between policy and state visitation (RL setting). Does not occur in i.i.d. supervised learning if only downstream performance is evaluated.
- **Related concepts**: State Coverage Gap, Imperfect Cloning Gap, Catastrophic Forgetting, CLOSE/FAR partition

## State Coverage Gap
- **Notation**: SCG
- **Definition**: A specific instance of FPC where the pre-trained policy π* is competent on FAR states but not on CLOSE states (i.e., π* was trained only on FAR). During fine-tuning where the agent must first traverse CLOSE to reach FAR, gradient updates on CLOSE cause π* to lose its FAR competence before it can be utilized.
- **Boundary conditions**: Requires that the pre-trained policy was trained on a subset of the downstream task's state space (specifically FAR), and that CLOSE states must be mastered before FAR states are reachable.
- **Related concepts**: Forgetting of Pre-trained Capabilities, Imperfect Cloning Gap, CLOSE/FAR partition

## Imperfect Cloning Gap
- **Notation**: ICG
- **Definition**: A specific instance of FPC where the pre-trained policy π* is a perturbed or approximate version of an optimal policy, causing slight suboptimality on CLOSE states. This slight suboptimality creates a compounding distribution shift: the agent visits CLOSE far more frequently than FAR, and gradient updates on CLOSE cause forgetting of FAR competence.
- **Boundary conditions**: Occurs when pre-training uses behavioral cloning from a superior agent (e.g., rule-based bot), offline datasets, or reward structure differs between pre-training and fine-tuning. More severe when the approximation error (cloning gap) is larger.
- **Related concepts**: Forgetting of Pre-trained Capabilities, State Coverage Gap, Behavioral Cloning

## CLOSE / FAR State Partition
- **Notation**: S_CLOSE, S_FAR where S = S_CLOSE ∪ S_FAR
- **Definition**: An approximate partition of the downstream task's state space into CLOSE (states reachable from the initial state distribution with high probability early in training) and FAR (states reachable only after mastering CLOSE). In NetHack: CLOSE = Level 1 states; FAR = Level 2+ states. In Montezuma's Revenge: CLOSE = Rooms 1–6; FAR = Room 7+. In RoboticSequence: CLOSE = {hammer, push} stages; FAR = {peg-unplug-side, push-wall} stages.
- **Boundary conditions**: Partition is approximate and task-dependent. In procedurally generated environments (NetHack), it is a statistical characterization, not a strict partition.
- **Related concepts**: State Coverage Gap, Imperfect Cloning Gap

## Elastic Weight Consolidation (EWC)
- **Notation**: L_EWC(θ) = Σᵢ Fᵢ(θ*ᵢ - θᵢ)²
- **Definition**: A regularization-based knowledge retention method that penalizes changes to parameters deemed important for prior tasks, weighted by the diagonal of the Fisher Information Matrix F. θ* are the pre-trained weights, θ are the current weights, and Fᵢ = 𝔼[(∂ℓ/∂θᵢ)²] estimated from the pre-training data.
- **Boundary conditions**: Applied only to actor parameters (not critic). Fisher matrix computed over 10,000 batches from NLD-AA for NetHack, or 2,560 examples from replay buffer for RoboticSequence. Regularization coefficient 2×10⁶ for NetHack, 100 for RoboticSequence.
- **Related concepts**: Behavioral Cloning Loss, Kickstarting, Fisher Information Matrix

## Behavioral Cloning Loss (BC)
- **Notation**: L_BC(θ) = 𝔼_{s~B_BC}[D_KL(π*(s) ‖ πθ(s))]
- **Definition**: A distillation-based knowledge retention method that minimizes the KL divergence between the pre-trained policy π* and current policy πθ, computed over a static buffer B_BC = {(s, π*(s)) : s ∈ S_BC} of states from the pre-training environment. Unlike KS, the expectation is over a static pre-training data buffer, not online data.
- **Boundary conditions**: Requires access to pre-training data. Applied only to actor. KL coefficient: 2.0 for NetHack (no decay); tuned per-environment for others. Actor reg coefficient: 1.0 for RoboticSequence.
- **Related concepts**: Kickstarting, Elastic Weight Consolidation, Episodic Memory

## Kickstarting (KS)
- **Notation**: L_KS(θ) = 𝔼_{s~πθ}[D_KL(π*(s) ‖ πθ(s))]
- **Definition**: A distillation-based knowledge retention method similar to BC but with the expectation computed over data gathered by the current online policy πθ (not a static buffer). This means KS only enforces that the current policy matches π* on states the current policy currently visits.
- **Boundary conditions**: Effective for imperfect cloning gap (e.g., NetHack) where FAR states are eventually visited by the fine-tuned policy. Fails for state coverage gap because it applies the KL loss on CLOSE states that π* was never trained on, interfering with CLOSE learning. Scaled by 0.5 with exponential decay 0.99998 per train step in NetHack.
- **Related concepts**: Behavioral Cloning Loss, Imperfect Cloning Gap, State Coverage Gap

## Episodic Memory (EM)
- **Notation**: B_EM ⊂ B_replay, |B_EM| = 0.1 × |B_replay|
- **Definition**: A replay-based knowledge retention method that populates the RL replay buffer with trajectories from the pre-training environment and protects them from being overwritten during fine-tuning. Old samples constitute 10% of the total replay buffer. Only applicable with off-policy algorithms (SAC).
- **Boundary conditions**: Only compatible with off-policy RL algorithms that maintain a replay buffer (SAC). Cannot be trivially applied to on-policy algorithms (PPO, APPO) as they may become unstable with off-policy data. Replay buffer size: 100K; EM size: 10K samples.
- **Related concepts**: Behavioral Cloning Loss, Soft Actor-Critic

## Asynchronous Proximal Policy Optimization (APPO)
- **Notation**: APPO
- **Definition**: A highly parallelizable, asynchronous variant of PPO used for NetHack training. Enables >500M environment steps in 24 hours on a single A100 GPU. Key hyperparameters: clip_policy=0.1, clip_baseline=1.0, discounting=0.999999, entropy_cost=0.001, hidden_dim=1738 (LSTM), batch_size=128, unroll_length=32.
- **Boundary conditions**: On-policy algorithm; episodic memory cannot be directly applied. KS uses online data buffer B_θ.
- **Related concepts**: Kickstarting, Behavioral Cloning Loss

## Forward Transfer
- **Notation**: FT = (AUC - AUC_b) / (1 - AUC_b), where AUC = (1/T)∫₀ᵀ p(t)dt
- **Definition**: A metric quantifying how much faster a fine-tuned model learns compared to a randomly initialized model. AUC is the area under the success rate curve for the fine-tuned model; AUC_b is the corresponding area for a model trained from scratch. FT > 0 means fine-tuning helps; FT = 0 means no benefit over scratch; FT < 0 means fine-tuning hurts.
- **Boundary conditions**: Defined for RoboticSequence experiments in the paper. Measures speed of learning, not final performance.
- **Related concepts**: CLOSE/FAR partition, Forgetting of Pre-trained Capabilities

## Central Kernel Alignment (CKA)
- **Notation**: CKA(K, L) = HSIC(K, L) / √(HSIC(K,K) · HSIC(L,L))
- **Definition**: A similarity metric for comparing neural network representations. Given activation matrices X ∈ ℝⁿˣᵖ¹ and Y ∈ ℝⁿˣᵖ², CKA computes normalized HSIC (Hilbert-Schmidt Independence Criterion) with linear kernels. Used to quantify how much the fine-tuned network's internal representations drift from the pre-trained network's representations at each layer.
- **Boundary conditions**: Linear kernel used in all paper experiments. Higher CKA = more similar representations. Early layers change less than late layers (consistent with prior supervised learning studies).
- **Related concepts**: Forgetting of Pre-trained Capabilities, representation shift
