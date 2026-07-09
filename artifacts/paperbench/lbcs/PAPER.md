---
title: "Refined Coreset Selection: Towards Minimal Coreset Size under Model Performance Constraints"
authors: [Xiaobo Xia, Jiale Liu, Shaokun Zhang, Qingyun Wu, Hongxin Wei, Tongliang Liu]
year: 2024
venue: "arXiv / ICML 2024"
doi: "arXiv:2311.08675v2"
ara_version: "1.0"
domain: "Deep learning, data selection, coreset selection"
keywords: [coreset selection, bilevel optimization, lexicographic optimization, data efficiency, data pruning, refined coreset selection, black-box optimization, LexiFlow, label noise robustness, deep learning]
claims_summary:
  - "LBCS simultaneously minimizes coreset size and preserves model accuracy via lexicographic bilevel optimization, outperforming fixed-size baselines on F-MNIST/SVHN/CIFAR-10/ImageNet"
  - "The voluntary performance compromise ε in LBCS reduces model overfitting during coreset selection, improving generalization under noisy/imbalanced labels"
  - "LBCS achieves ε-convergence under the progressable and stable moving conditions, with lower time complexity than Probabilistic coreset (O(TK) vs O(TKC))"
abstract: "Coreset selection is powerful in reducing computational costs and accelerating data processing for deep learning algorithms. It strives to identify a small subset from large-scale data, so that training only on the subset practically performs on par with full data. Practitioners regularly desire to identify the smallest possible coreset in realistic scenes while maintaining comparable model performance, to minimize costs and maximize acceleration. Motivated by this desideratum, for the first time, we pose the problem of refined coreset selection (RCS), in which the minimal coreset size under model performance constraints is explored. Moreover, to address this problem, we propose an innovative method, which maintains optimization priority order over the model performance and coreset size, and efficiently optimizes them in the coreset selection procedure. Theoretically, we provide the convergence guarantee of the proposed method. Empirically, extensive experiments confirm its superiority compared with previous strategies, often yielding better model performance with smaller coreset sizes."
---

# Refined Coreset Selection: Towards Minimal Coreset Size under Model Performance Constraints

## Overview

This paper introduces the **Refined Coreset Selection (RCS)** problem, which asks: given a large dataset, what is the *smallest* subset (coreset) such that training on it yields acceptable model accuracy? Prior coreset selection methods fixed the coreset size in advance and only optimized for model performance. RCS adds a secondary objective — minimize coreset size — subject to the primary objective of comparable model performance.

The proposed method, **Lexicographic Bilevel Coreset Selection (LBCS)**, formalizes the two objectives via a lexicographic preference order (f1 = full-data loss, f2 = coreset size), embeds them in a bilevel optimization framework, and solves the outer loop using LexiFlow — a randomized direct search algorithm that compares candidate masks using lexicographic relations without needing analytic gradients. A convergence guarantee (ε-convergence) is provided, and experiments on F-MNIST, SVHN, CIFAR-10, and ImageNet-1k demonstrate that LBCS consistently delivers smaller coresets with equal or better model accuracy than seven baseline methods.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight (RCS motivation) |
| [claims.md](logic/claims.md) | 5 falsifiable claims (C01–C05) |
| [concepts.md](logic/concepts.md) | 10 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 6 verification plans (E01–E06) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: bilevel LBCS with LexiFlow outer loop |
| [solution/algorithm.md](logic/solution/algorithm.md) | LBCS Algorithm 1 + LexiFlow Algorithm 2, ε-convergence |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and known limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | 5 acceleration and robustness heuristics |
| [related_work.md](logic/related_work.md) | 10 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/lbcs.py](src/execution/lbcs.py) | LBCS + LexiFlow core implementation stub | C01, C02, C03 |
| [execution/baselines.py](src/execution/baselines.py) | Baseline coreset selectors (EL2N, GraNd, Moderate, etc.) | C01 |
| [configs/training.md](src/configs/training.md) | Inner/outer loop hyperparameters with rationale | — |
| [configs/model.md](src/configs/model.md) | Network architectures for proxy and evaluation | — |
| [environment.md](src/environment.md) | Hardware, deps, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 6 tables + 3 figures |
| [tables/table1_mnist_s_objectives.md](evidence/tables/table1_mnist_s_objectives.md) | Table 1: MNIST-S f1/f2 optimization by LBCS at k=200,400 |
| [tables/table2_main_results.md](evidence/tables/table2_main_results.md) | Table 2: Test accuracy and coreset size on F-MNIST/SVHN/CIFAR-10 |
| [tables/table3_lbcs_sizes.md](evidence/tables/table3_lbcs_sizes.md) | Table 3: All methods at LBCS-determined coreset sizes |
| [tables/table4_imagenet.md](evidence/tables/table4_imagenet.md) | Table 4: ImageNet-1k Top-5 accuracy |
| [tables/table5_ablation_search_times.md](evidence/tables/table5_ablation_search_times.md) | Table 7 (appendix): Ablation on search time T |
| [tables/table6_cross_architecture.md](evidence/tables/table6_cross_architecture.md) | Table 8 (appendix): ViT / W-NET cross-architecture on SVHN |
| [tables/table7_imperfect_supervision.md](evidence/tables/table7_imperfect_supervision.md) | Table 6 (appendix): Optimized coreset sizes under imperfect supervision |
| [tables/table8_continual_streaming.md](evidence/tables/table8_continual_streaming.md) | Tables 9–10 (appendix): Continual learning and streaming |
| [figures/fig1_trivial_solutions.md](evidence/figures/fig1_trivial_solutions.md) | Figure 1: f1/f2 trajectories for equations (3) and (4) |
| [figures/fig2_imperfect_supervision.md](evidence/figures/fig2_imperfect_supervision.md) | Figure 2: Accuracy under noisy labels and class imbalance |
| [figures/fig3_per_point_accuracy.md](evidence/figures/fig3_per_point_accuracy.md) | Figure 3: Average accuracy per coreset data point |
