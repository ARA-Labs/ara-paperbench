# Related Work

## RW01: Cheng et al., 2023 (StateMask)
- **DOI**: Proc. NeurIPS 2023
- **Type**: extends
- **Delta**:
  - What changed: RICE simplifies StateMask's primal-dual objective to vanilla PPO with blinding bonus; adds mixed initial distribution and RND for refining instead of critical-state-only reset.
  - Why: Primal-dual optimization is computationally expensive; critical-state-only reset causes overfitting.
- **Claims affected**: C01, C02, C03
- **Adopted elements**: Binary mask network architecture; state importance scoring via P(a^m=0|s); fidelity score metric definition.

## RW02: Uchendu et al., 2023 (JSRL)
- **DOI**: Proc. ICML 2023
- **Type**: baseline
- **Delta**:
  - What changed: RICE replaces random curriculum frontier selection with explanation-guided critical state selection.
  - Why: Random frontiers do not guarantee positive returns or useful exploration.
- **Claims affected**: C01, C02
- **Adopted elements**: Roll-in concept (using pre-trained policy to set exploration start point); transformation of JSRL to a refining method by initializing πe = πg.

## RW03: Kakade & Langford, 2002
- **DOI**: Proc. ICML 2002
- **Type**: imports
- **Delta**:
  - What changed: RICE uses the Performance Difference Lemma to bound sub-optimality via state distribution mismatch coefficient.
  - Why: Provides rigorous theoretical foundation for the mixed initial distribution benefit.
- **Claims affected**: C01
- **Adopted elements**: Performance Difference Lemma; approximate policy gradient framework.

## RW04: Burda et al., 2018 (RND)
- **DOI**: Proc. ICLR 2018 (arXiv:1810.12894)
- **Type**: imports
- **Delta**:
  - What changed: RICE applies RND as the exploration bonus starting from mixed initial states, rather than from default start.
  - Why: RND is effective in large/continuous state spaces where count-based methods fail.
- **Claims affected**: C02, C05
- **Adopted elements**: Random Network Distillation architecture (target + predictor); intrinsic reward formulation R_int = |f(s') − f̂(s')|².

## RW05: Schulman et al., 2017 (PPO)
- **DOI**: arXiv:1707.06347
- **Type**: imports
- **Delta**:
  - What changed: RICE uses PPO as the base refining algorithm for both mask network training and policy refinement.
  - Why: PPO's monotonicity guarantees and clip-based stability make it suitable for both phases.
- **Claims affected**: C02, C03
- **Adopted elements**: PPO loss (clipped surrogate objective); advantage estimation; value network.

## RW06: Chang et al., 2023 (PPO++)
- **DOI**: arXiv:2306.11816
- **Type**: baseline
- **Delta**:
  - What changed: RICE replaces random visited-state selection with explanation-guided selection, providing theoretical improvement in distribution mismatch coefficient.
  - Why: Not all visited states are informative; random selection provides no guarantee.
- **Claims affected**: C01, C02
- **Adopted elements**: Mixed initial distribution concept (combining default + visited states).

## RW07: Agarwal et al., 2022 (Reincarnating RL)
- **DOI**: Proc. NeurIPS 2022
- **Type**: bounds
- **Delta**:
  - What changed: RICE addresses a specific case of reincarnating RL — breaking bottlenecks rather than general policy transfer.
  - Why: Provides broader motivation for reusing pre-trained policies.
- **Claims affected**: C01
- **Adopted elements**: Cost motivation (millions of dollars for re-training); prior computation reuse framework.

## RW08: Ecoffet et al., 2019/2021 (Go-Explore)
- **DOI**: arXiv:1901.10995; Nature 2021
- **Type**: imports
- **Delta**:
  - What changed: RICE borrows the environment state restoration mechanism but selects frontiers via explanation rather than return-based archive.
  - Why: Systematic state restoration is needed to reset to critical states in RICE.
- **Claims affected**: C02
- **Adopted elements**: Environment reset function to restore states; "first return, then explore" philosophy.

## RW09: Ho & Ermon, 2016 (GAIL)
- **DOI**: Proc. NeurIPS 2016
- **Type**: imports
- **Delta**:
  - What changed: RICE uses GAIL as a bridge to convert non-PPO pretrained agents (SAC) to PPO-compatible policy networks for refining.
  - Why: Enables algorithm-agnostic refining by obtaining a PPO-compatible approximation of any policy.
- **Claims affected**: C06
- **Adopted elements**: Adversarial imitation learning to distill policy behavior into a new network.
