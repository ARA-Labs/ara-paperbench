# Related Work

## RW01: Tuyls et al., 2023
- **DOI**: arXiv:2307.09423
- **Type**: baseline
- **Delta**:
  - What changed: This work fine-tunes the model from Tuyls et al. (2023) with knowledge retention; Tuyls et al. report only offline BC pre-training (5218 ± - on Human Monk)
  - Why: Show that online fine-tuning with KR can 2× the offline-only SOTA
- **Claims affected**: C01, C03, C04
- **Adopted elements**: 33M LSTM architecture, pre-trained weights, NLD-AA dataset, Human Monk evaluation protocol

## RW02: Kirkpatrick et al., 2017
- **DOI**: PNAS 114(13):3521–3526
- **Type**: imports
- **Delta**:
  - What changed: EWC was proposed for supervised continual learning; this paper applies it to RL fine-tuning actor-only
  - Why: EWC is a natural baseline for parameter regularization-based retention
- **Claims affected**: C04
- **Adopted elements**: Fisher-diagonal-weighted L2 regularization formula, concept of parameter importance

## RW03: Schmitt et al., 2018
- **DOI**: arXiv:1803.03835
- **Type**: imports
- **Delta**:
  - What changed: Kickstarting originally applied KL from a teacher policy to accelerate learning (not preserve prior knowledge); this paper uses it as a knowledge retention method during fine-tuning
  - Why: KS naturally prevents the policy from deviating from π* on states the online policy visits
- **Claims affected**: C04, C05
- **Adopted elements**: KL divergence auxiliary loss on online data; teacher-student distillation framework

## RW04: Rebuffi et al., 2017
- **DOI**: CVPR 2017
- **Type**: imports
- **Delta**:
  - What changed**: iCaRL proposed replay-based continual learning for classification; this paper uses the BC-style replay (buffer of (s, π*(s)) pairs) for RL actor retention
  - Why: Replay is a proven effective retention strategy; adapting it to RL requires using action distributions instead of class labels
- **Claims affected**: C04
- **Adopted elements**: Replay buffer structure; behavioral cloning on stored examples

## RW05: Wołczyk et al., 2021
- **DOI**: NeurIPS 2021 (Continual World)
- **Type**: imports
- **Delta**:
  - What changed: Continual World focuses on multi-task continual RL (retaining performance on all tasks); this paper focuses on single-task fine-tuning (only downstream task performance matters)
  - Why: Provides the RoboticSequence environment infrastructure, SAC implementation, EWC/BC implementations, and forward transfer metric
- **Claims affected**: C01, C02, C04
- **Adopted elements**: Meta-World task sequences, SAC with CL methods, forward transfer metric definition, actor-only regularization principle

## RW06: Baker et al., 2022 (VPT)
- **DOI**: arXiv:2206.11795
- **Type**: extends
- **Delta**:
  - What changed: VPT uses a regularization term during fine-tuning but doesn't analyze it as FPC mitigation; pre-trains on video data using inverse dynamics model
  - Why: Related to imperfect cloning gap (pre-training on passive video then fine-tuning with RL)
- **Claims affected**: C01, C03
- **Adopted elements**: Conceptual motivation for retention during RL fine-tuning; disabling entropy during fine-tuning

## RW07: Wulfmeier et al., 2023
- **DOI**: arXiv (Foundations for Transfer in RL)
- **Type**: bounds
- **Delta**:
  - What changed: Wulfmeier et al. claim (§3.5) that forgetting is not a factor in standard transfer RL; this paper shows the opposite empirically
  - Why: The claim is based on supervised learning intuition; RL's feedback loop changes the dynamics
- **Claims affected**: C01, C05
- **Adopted elements**: Taxonomy of knowledge modalities in transfer RL; motivation for studying fine-tuning

## RW08: Haarnoja et al., 2018a
- **DOI**: ICML 2018
- **Type**: imports
- **Delta**:
  - What changed: Standard SAC used as the base RL algorithm for RoboticSequence experiments
  - Why: SAC is off-policy (enables EM) and well-suited for continuous control
- **Claims affected**: C02, C04
- **Adopted elements**: SAC algorithm, automatic entropy tuning, replay buffer training

## RW09: Petrenko et al., 2020 (Sample Factory)
- **DOI**: arXiv:2006.11751
- **Type**: imports
- **Delta**:
  - What changed: APPO implementation used for NetHack fine-tuning; enables >500M steps/day on single A100
  - Why: NetHack requires massive sample efficiency; APPO provides the throughput
- **Claims affected**: C01, C03, C04
- **Adopted elements**: APPO algorithm, asynchronous training infrastructure, hyperparameter defaults (Table 6 in Petrenko et al.)

## RW10: Burda et al., 2018 (RND)
- **DOI**: ICLR 2018
- **Type**: imports
- **Delta**:
  - What changed: RND is used as an exploration bonus for Montezuma's Revenge; critical for solving the sparse-reward environment
  - Why: Without intrinsic motivation, PPO cannot explore beyond the first few rooms
- **Claims affected**: C02, C04
- **Adopted elements**: Random network distillation architecture (target + predictor), intrinsic motivation via prediction error

## RW11: Hambro et al., 2022 (Dungeons and Data)
- **DOI**: NeurIPS 2022 Datasets and Benchmarks
- **Type**: baseline
- **Delta**:
  - What changed: Provides NLD-AA dataset used for BC pre-training in NetHack; also provides prior baselines (From Scratch + KS: 2090, From Scratch + BC: 2809) to compare against
  - Why: Establishes evaluation protocol and baseline methods for NetHack
- **Claims affected**: C04
- **Adopted elements**: NLD-AA dataset, evaluation protocol, baseline results for comparison

## RW12: Kornblith et al., 2019 (CKA)
- **DOI**: ICML 2019
- **Type**: imports
- **Delta**:
  - What changed: CKA used to measure representation drift during fine-tuning; previously used in supervised continual learning analysis
  - Why: Provides a quantitative measure of how much internal representations change, enabling analysis of where and when forgetting occurs in the network
- **Claims affected**: C06
- **Adopted elements**: CKA formula with linear kernel, layer-wise representation similarity analysis
