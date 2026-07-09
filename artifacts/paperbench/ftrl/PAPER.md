---
title: "Fine-tuning Reinforcement Learning Models is Secretly a Forgetting Mitigation Problem"
authors:
  - "Maciej Wołczyk"
  - "Bartłomiej Cupiał"
  - "Mateusz Ostaszewski"
  - "Michał Bortkiewicz"
  - "Michał Zając"
  - "Razvan Pascanu"
  - "Łukasz Kuciński"
  - "Piotr Miłoś"
year: 2024
venue: "ICML 2024 (Proceedings of the 41st International Conference on Machine Learning)"
doi: "arXiv:2402.02868v3"
ara_version: "1.0"
domain: "Reinforcement Learning / Transfer Learning / Continual Learning"
keywords:
  - fine-tuning
  - reinforcement learning
  - catastrophic forgetting
  - knowledge retention
  - transfer learning
  - behavioral cloning
  - NetHack
  - Montezuma's Revenge
  - elastic weight consolidation
  - kickstarting
claims_summary:
  - "Forgetting of Pre-trained Capabilities (FPC) is a common and catastrophic problem in RL fine-tuning, caused by state distribution shift early in fine-tuning"
  - "Standard knowledge retention methods (EWC, BC, KS, EM) effectively mitigate FPC and unlock pre-trained benefits, yielding 2× SOTA on NetHack"
  - "Two specific FPC instances—state coverage gap and imperfect cloning gap—explain most observed transfer failures in RL"
abstract: "Fine-tuning is a widespread technique that allows practitioners to transfer pre-trained capabilities, as recently showcased by the successful applications of foundation models. However, fine-tuning reinforcement learning (RL) models remains a challenge. This work conceptualizes one specific cause of poor transfer, accentuated in the RL setting by the interplay between actions and observations: forgetting of pre-trained capabilities. Namely, a model deteriorates on the state subspace of the downstream task not visited in the initial phase of fine-tuning, on which the model behaved well due to pre-training. This way, we lose the anticipated transfer benefits. We identify conditions when this problem occurs, showing that it is common and, in many cases, catastrophic. Through a detailed empirical analysis of the challenging NetHack and Montezuma's Revenge environments, we show that standard knowledge retention techniques mitigate the problem and thus allow us to take full advantage of the pre-trained capabilities. In particular, in NetHack, we achieve a new state-of-the-art for neural models, improving the previous best score from 5K to over 10K points in the Human Monk scenario."
---

# Fine-tuning Reinforcement Learning Models is Secretly a Forgetting Mitigation Problem

## Overview

This paper identifies **Forgetting of Pre-trained Capabilities (FPC)** as a critical but underappreciated cause of poor knowledge transfer when fine-tuning reinforcement learning agents. Unlike supervised learning where data is i.i.d. and forgetting doesn't matter for downstream performance, RL creates a feedback loop: the agent's actions determine which states it visits, so early-stage training on easy ("CLOSE") states causes catastrophic forgetting of behavior on harder ("FAR") states that aren't yet reachable.

The paper formalizes two instances of FPC—**state coverage gap** (pre-trained policy is good on FAR but not on CLOSE, and forgets FAR while learning CLOSE) and **imperfect cloning gap** (small imperfections in the pre-trained policy cause distribution drift away from FAR)—and demonstrates that applying standard continual learning retention methods (EWC, BC, KS, EM) to the actor network resolves the problem. Applied to NetHack, fine-tuning with kickstarting achieves 10,588 ± 672 points, more than doubling the prior neural SOTA of 5,218.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight behind FPC |
| [claims.md](logic/claims.md) | 6 falsifiable claims (C01–C06) |
| [concepts.md](logic/concepts.md) | 10 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 6 verification plans (E01–E06) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: KR-augmented RL fine-tuning pipeline |
| [solution/algorithm.md](logic/solution/algorithm.md) | EWC, BC, KS, EM auxiliary losses with math |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and known limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | 8 convergence tricks from the paper |
| [related_work.md](logic/related_work.md) | 12 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [code/](src/code/) | **Full paper codebase** (Sample Factory fork + paper-specific experiments) | All |
| [code/sf_examples/nethack/](src/code/sf_examples/nethack/) | NetHack training, models (kickstarter, scaled, chaotic_dwarf), learner, wrappers | C01, C04, C05, C06 |
| [code/sf_examples/nethack/algo/learning/learner.py](src/code/sf_examples/nethack/algo/learning/learner.py) | Modified APPO learner with KR loss integration | C01, C04 |
| [code/sf_examples/nethack/models/kickstarter.py](src/code/sf_examples/nethack/models/kickstarter.py) | Kickstarting (KS) model implementation | C04 |
| [code/sf_examples/nethack/models/scaled.py](src/code/sf_examples/nethack/models/scaled.py) | Scaled model with EWC/BC support | C04 |
| [code/sf_examples/nethack/train_nethack.py](src/code/sf_examples/nethack/train_nethack.py) | NetHack training entry point | C01, C04 |
| [code/sf_examples/nethack/nethack_params.py](src/code/sf_examples/nethack/nethack_params.py) | NetHack hyperparameters | — |
| [code/sf_examples/mujoco/](src/code/sf_examples/mujoco/) | MuJoCo/RoboticSequence training code | C02, C03 |
| [code/sample_factory/](src/code/sample_factory/) | Sample Factory APPO framework (modified fork) | — |
| [code/README.md](src/code/README.md) | Repository setup and installation instructions | — |
| [execution/knowledge_retention.py](src/execution/knowledge_retention.py) | Standalone EWC, BC, KS, EM loss implementations | C01, C04 |
| [execution/robotic_sequence.py](src/execution/robotic_sequence.py) | RoboticSequence env wrapper + SAC integration | C02, C04 |
| [execution/train_robotic_sequence.py](src/execution/train_robotic_sequence.py) | RoboticSequence SAC training script | C02, C03 |
| [execution/train_nethack.py](src/execution/train_nethack.py) | NetHack fine-tuning training script | C01, C04 |
| [execution/train_montezuma.py](src/execution/train_montezuma.py) | Montezuma's Revenge PPO+RND training script | C05, C06 |
| [configs/training.md](src/configs/training.md) | Training hyperparameters for all three environments | — |
| [configs/model.md](src/configs/model.md) | Model architecture configurations | — |
| [environment.md](src/environment.md) | Hardware, dependencies, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 14-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 6 tables + 6 figures |
| [tables/nethack_full_eval.md](evidence/tables/nethack_full_eval.md) | Table 4: NetHack full evaluation, 1000 episodes, last checkpoint |
| [tables/nethack_prior_work.md](evidence/tables/nethack_prior_work.md) | Table 5: Score comparison against prior work |
| [tables/metaworld_kr_hyperparams.md](evidence/tables/metaworld_kr_hyperparams.md) | Table 3: Knowledge retention hyperparameters in Meta-World |
| [tables/nethack_model_hyperparams.md](evidence/tables/nethack_model_hyperparams.md) | Table 1: NetHack model hyperparameters |
| [tables/montezuma_hyperparams.md](evidence/tables/montezuma_hyperparams.md) | Table 2: Montezuma's Revenge hyperparameters |
| [tables/robotic_forward_transfer.md](evidence/tables/robotic_forward_transfer.md) | Table 6: Forward transfer vs. number of prefix tasks |
| [figures/nethack_performance.md](evidence/figures/nethack_performance.md) | Figure 3a: NetHack average return over training steps |
| [figures/montezuma_performance.md](evidence/figures/montezuma_performance.md) | Figure 3b: Montezuma's Revenge average return over training |
| [figures/robotic_performance.md](evidence/figures/robotic_performance.md) | Figure 3c: RoboticSequence success rate over training |
| [figures/montezuma_room7.md](evidence/figures/montezuma_room7.md) | Figure 6: Montezuma Room 7 success rate throughout fine-tuning |
| [figures/nethack_level4_sokoban.md](evidence/figures/nethack_level4_sokoban.md) | Figure 5: NetHack per-level evaluation (Level 4 + Sokoban) |
| [figures/robotic_stage_success.md](evidence/figures/robotic_stage_success.md) | Figure 7: RoboticSequence per-stage success rates |
