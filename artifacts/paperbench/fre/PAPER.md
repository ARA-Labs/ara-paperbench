---
title: "Unsupervised Zero-Shot Reinforcement Learning via Functional Reward Encodings"
authors: ["Kevin Frans", "Seohong Park", "Pieter Abbeel", "Sergey Levine"]
year: 2024
venue: "arXiv"
doi: "arXiv:2402.17135v1"
ara_version: "1.0"
domain: "Offline Reinforcement Learning / Zero-Shot RL"
keywords:
  - zero-shot reinforcement learning
  - offline reinforcement learning
  - functional reward encoding
  - variational autoencoder
  - implicit Q-learning
  - transformer encoder
  - multi-task RL
  - unsupervised RL
  - successor features
  - reward representation learning
claims_summary:
  - "FRE enables zero-shot adaptation to arbitrary downstream reward functions using only 32 (state, reward) samples at test time, outperforming SF/FB baselines that require 5120 samples"
  - "Training with diverse random reward families (FRE-all) yields higher average performance than any single reward family subset, demonstrating smooth scaling with reward diversity"
  - "A single FRE agent achieves competitive performance on both goal-reaching and structured reward tasks simultaneously, while prior methods specialize in one or the other"
abstract: "Can we pre-train a generalist agent from a large amount of unlabeled offline trajectories such that it can be immediately adapted to any new downstream tasks in a zero-shot manner? In this work, we present a functional reward encoding (FRE) as a general, scalable solution to this zero-shot RL problem. Our main idea is to learn functional representations of any arbitrary tasks by encoding their state-reward samples using a transformer-based variational auto-encoder. This functional encoding not only enables the pre-training of an agent from a wide diversity of general unsupervised reward functions, but also provides a way to solve any new downstream tasks in a zero-shot manner, given a small number of reward-annotated samples. We empirically show that FRE agents trained on diverse random unsupervised reward functions can generalize to solve novel tasks in a range of simulated robotic benchmarks, often outperforming previous zero-shot RL and offline RL methods."
---

# Unsupervised Zero-Shot Reinforcement Learning via Functional Reward Encodings

## Overview
FRE introduces a transformer-based variational autoencoder that encodes reward functions by their *functional form* — i.e., from samples of (state, reward) pairs — rather than requiring hand-specified task parameterizations. Given an unlabeled offline dataset, FRE (1) trains an encoder-decoder over a prior distribution of random unsupervised reward functions (goal-reaching, random linear, random MLP) to learn a compressed latent representation z for each reward function, and (2) trains an IQL-conditioned policy over this latent space. At test time, any new reward function is encoded from just 32 annotated samples, enabling zero-shot policy execution without further training.

The method is evaluated on AntMaze (antmaze-large-diverse-v2), ExORL (walker/cheetah RND), and D4RL Kitchen (kitchen-complete-v0). FRE matches or outperforms state-of-the-art baselines including FB, SF, GC-IQL, GC-BC, and OPAL across goal-reaching, directional, structured-path, and Kitchen subtask evaluations — the first method to perform consistently across all task families.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight |
| [claims.md](logic/claims.md) | 5 falsifiable claims (C01–C05) |
| [concepts.md](logic/concepts.md) | 10 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 5 verification plans (E01–E05) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: FRE encoder-decoder + IQL policy |
| [solution/algorithm.md](logic/solution/algorithm.md) | Information bottleneck VAE + strided training |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | 6 convergence and design heuristics |
| [related_work.md](logic/related_work.md) | 10 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/fre.py](src/execution/fre.py) | FRE encoder, decoder, reward sampling | C01, C02 |
| [execution/iql.py](src/execution/iql.py) | IQL training with FRE latent conditioning | C01, C03 |
| [configs/training.md](src/configs/training.md) | Training hyperparameters (Appendix A) | — |
| [configs/model.md](src/configs/model.md) | Encoder/decoder/policy architecture configs | — |
| [environment.md](src/environment.md) | Hardware, dependencies, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 2 tables + 2 figures |
| [tables/table1_main_results.md](evidence/tables/table1_main_results.md) | Main zero-shot RL comparison across all domains |
| [tables/table4_reward_subset_ablation.md](evidence/tables/table4_reward_subset_ablation.md) | AntMaze ablation over reward family subsets |
| [figures/figure5_reward_diversity_scaling.md](evidence/figures/figure5_reward_diversity_scaling.md) | Bar chart: reward diversity vs. task performance |
| [figures/figure6_domain_knowledge.md](evidence/figures/figure6_domain_knowledge.md) | Bar chart: FRE-hint vs. FRE-all on specific tasks |
