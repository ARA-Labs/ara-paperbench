# Related Work

## RW01: Touati & Ollivier, 2021 (Forward-Backward Representations)
- **DOI**: arXiv:2103.07945
- **Type**: baseline
- **Delta**:
  - What changed: FRE replaces the linearized value function assumption of FB with a learned functional encoding over arbitrary reward distributions.
  - Why: FB can only represent tasks in the linear span of learned state representations; FRE encodes nonlinear reward functions directly from samples.
- **Claims affected**: C01, C02, C03
- **Adopted elements**: Problem framing of zero-shot RL; evaluation on ExORL benchmarks.

## RW02: Touati et al., 2022 (Does Zero-Shot RL Exist?)
- **DOI**: arXiv:2209.14935
- **Type**: imports
- **Delta**:
  - What changed: FRE provides a practical solution to the zero-shot RL problem posed in this work.
  - Why: This work formally defines the zero-shot RL setting and provides FB/SF baselines.
- **Claims affected**: C01, C02
- **Adopted elements**: Zero-shot RL problem formulation; ExORL Walker/Cheetah evaluation protocol; FB and SF as primary baselines.

## RW03: Kostrikov et al., 2021 (IQL)
- **DOI**: arXiv:2110.06169
- **Type**: imports
- **Delta**:
  - What changed: FRE conditions IQL on latent task vector z; otherwise uses standard IQL for offline policy learning.
  - Why: IQL avoids out-of-distribution action queries, crucial for offline RL stability.
- **Claims affected**: C01
- **Adopted elements**: Expectile regression for value function, AWR actor update, target network soft update, all hyperparameters (tau=0.8, AWR temperature=3.0, target rate=0.001).

## RW04: Barreto et al., 2017 (Successor Features)
- **DOI**: NeurIPS 2017
- **Type**: baseline
- **Delta**:
  - What changed: FRE does not require pre-defined state features or a linear task structure; functional encoding generalizes beyond the linear span.
  - Why: SF methods are limited to tasks expressible as linear combinations of pre-specified features.
- **Claims affected**: C01, C02
- **Adopted elements**: General framework of task-conditioned value functions.

## RW05: Ajay et al., 2020 (OPAL)
- **DOI**: arXiv:2010.13611
- **Type**: baseline
- **Delta**:
  - What changed: FRE encodes reward functions rather than trajectory chunks; FRE uses offline RL (IQL) rather than behavioral cloning; FRE supports zero-shot task identification.
  - Why: OPAL lacks a mechanism for zero-shot reward-based task adaptation.
- **Claims affected**: C01, C03
- **Adopted elements**: Offline unsupervised skill learning paradigm; permutation-invariant transformer architecture (re-implemented in FRE codebase).

## RW06: Alemi et al., 2016 (Deep VIB)
- **DOI**: arXiv:1612.00410
- **Type**: imports
- **Delta**:
  - What changed: FRE applies the VIB framework to reward function encoding rather than supervised classification.
  - Why: Provides the variational lower bound derivation for the information bottleneck objective.
- **Claims affected**: C01
- **Adopted elements**: Variational information bottleneck objective; KL divergence penalty to unit Gaussian; reparameterization trick.

## RW07: Vaswani et al., 2017 (Transformer)
- **DOI**: NeurIPS 2017
- **Type**: imports
- **Delta**:
  - What changed: FRE uses transformer without causal masking or positional encodings to achieve permutation invariance over (state, reward) sets.
  - Why: Standard transformers use causal/positional structure; FRE requires set processing.
- **Claims affected**: C01
- **Adopted elements**: Multi-head self-attention, layer normalization, feedforward sublayers. Architecture: 4 layers, 256 hidden dim.

## RW08: Garnelo et al., 2018 (Neural Processes)
- **DOI**: arXiv:1807.01622
- **Type**: extends
- **Delta**:
  - What changed: FRE uses a probabilistic encoder with an information bottleneck penalty and a fixed K; neural processes use a deterministic encoder and variable K.
  - Why: The information bottleneck adds regularization that encourages compact, generalizable task representations.
- **Claims affected**: C01
- **Adopted elements**: Concept of encoding a context set to predict function values at query points.

## RW09: Fu et al., 2020 (D4RL)
- **DOI**: arXiv:2004.07219
- **Type**: imports
- **Delta**:
  - What changed: FRE uses D4RL datasets (antmaze-large-diverse-v2, kitchen-complete-v0) without requiring their original task-specific reward labels.
  - Why: Standard offline RL benchmark providing diverse locomotion and manipulation data.
- **Claims affected**: C01, C02, C03
- **Adopted elements**: antmaze-large-diverse-v2, kitchen-complete-v0 datasets; evaluation environment code.

## RW10: Yarats et al., 2022 (ExORL)
- **DOI**: arXiv:2201.13425
- **Type**: imports
- **Delta**:
  - What changed: FRE uses ExORL datasets as unlabeled pre-training data and evaluates on velocity/goal tasks without access to reward labels during training.
  - Why: ExORL provides non-expert exploration data from DMControl, ideal for unsupervised pre-training.
- **Claims affected**: C01, C02
- **Adopted elements**: Walker RND and Cheetah RND offline datasets; walker/cheetah evaluation protocol (velocity, goal tasks); physics state augmentation for reward encoding.
