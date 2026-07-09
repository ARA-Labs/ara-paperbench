---
title: "SAPG: Split and Aggregate Policy Gradients"
authors: ["Jayesh Singla", "Ananye Agarwal", "Deepak Pathak"]
year: 2024
venue: "arXiv"
doi: "arXiv:2407.20230"
ara_version: "1.0"
domain: "Reinforcement Learning / Robot Learning"
keywords: ["policy gradients", "PPO", "on-policy RL", "massively parallel simulation", "importance sampling", "dexterous manipulation", "IsaacGym", "population-based training", "off-policy correction", "large-scale RL"]
claims_summary:
  - "PPO performance saturates with increasing parallel environments due to IID sampling redundancy"
  - "SAPG (leader-follower with importance-sampled aggregation) achieves 12-66%+ higher asymptotic performance than DexPBT on hard dexterous manipulation tasks"
  - "Leader-follower aggregation outperforms symmetric aggregation; entropy regularization boosts performance on harder tasks"
abstract: "Despite extreme sample inefficiency, on-policy reinforcement learning, aka policy gradients, has become a fundamental tool in decision-making problems. With the recent advances in GPU-driven simulation, the ability to collect large amounts of data for RL training has scaled exponentially. However, we show that current RL methods, e.g. PPO, fail to ingest the benefit of parallelized environments beyond a certain point and their performance saturates. To address this, we propose a new on-policy RL algorithm that can effectively leverage large-scale environments by splitting them into chunks and fusing them back together via importance sampling. Our algorithm, termed SAPG, shows significantly higher performance across a variety of challenging environments where vanilla PPO and other strong baselines fail to achieve high performance."
---

# SAPG: Split and Aggregate Policy Gradients

## Overview

SAPG identifies a fundamental limitation of on-policy RL (specifically PPO) at massive scale: when tens of thousands of parallel environments all sample from the same Gaussian policy, the resulting data is redundant because most sampled actions cluster near the distribution mean. Naively increasing batch size yields diminishing returns — PPO performance saturates beyond ~25,000 environments.

The solution is a divide-and-conquer framework: N environments are split into M blocks, each running a separate policy. A designated "leader" policy aggregates data from all "follower" policies via importance-sampled off-policy updates, while followers update using only their own on-policy data. Diversity among followers is enforced through (a) latent conditioning on per-policy hanging parameters ϕⱼ and (b) different entropy regularization coefficients. Evaluated on 6 dexterous manipulation tasks in IsaacGym with 24,576 parallel environments, SAPG outperforms PPO, DexPBT, and PQL on most tasks, achieving up to 66% higher success rate than DexPBT on reorientation and more than double the successes on two-arm reorientation.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight: PPO data redundancy at large scale |
| [claims.md](logic/claims.md) | 6 falsifiable claims (C01–C06) |
| [concepts.md](logic/concepts.md) | 10 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 6 verification plans (E01–E06) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: leader-follower policy graph with shared backbone |
| [solution/algorithm.md](logic/solution/algorithm.md) | SAPG algorithm, importance-sampling loss, pseudocode |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and known limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | 5 convergence tricks |
| [related_work.md](logic/related_work.md) | 9 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/sapg.py](src/execution/sapg.py) | Core SAPG losses (Eq 2–9): on-policy PPO, off-policy IS correction, critic targets | C01, C02 |
| [execution/policy.py](src/execution/policy.py) | Shared backbone + hanging parameter network architecture | C03, C04 |
| [configs/training.md](src/configs/training.md) | Training hyperparameters for AllegroKuka, ShadowHand, AllegroHand | — |
| [configs/model.md](src/configs/model.md) | Model architecture configs (LSTM/MLP, layer dims, latent dim) | — |
| [environment.md](src/environment.md) | Hardware, dependencies, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 1 table + 4 figures |
| [tables/table1_main_results.md](evidence/tables/table1_main_results.md) | Table 1: Final performance at 2e10 samples for all methods/tasks |
| [figures/fig2_ppo_batch_saturation.md](evidence/figures/fig2_ppo_batch_saturation.md) | Figure 2: PPO asymptotic performance vs batch size (Shadow Hand, Allegro Kuka Throw) |
| [figures/fig5_performance_curves.md](evidence/figures/fig5_performance_curves.md) | Figure 5: Training curves for SAPG, PPO, PBT, PQL across 6 tasks |
| [figures/fig6_ablation_curves.md](evidence/figures/fig6_ablation_curves.md) | Figure 6: Ablation study curves across 5 tasks |
