---
title: "What Will My Model Forget? Forecasting Forgotten Examples in Language Model Refinement"
authors: ["Xisen Jin", "Xiang Ren"]
year: 2024
venue: "ICML 2024"
doi: "arXiv:2402.01865"
ara_version: "1.0"
domain: "Continual Learning / Language Model Refinement"
keywords: ["catastrophic forgetting", "model refinement", "continual learning", "language models", "example forgetting", "logit-change transfer", "representation learning", "replay-based methods", "BART0", "FLAN-T5"]
claims_summary:
  - "Representation-based forecasting (inner products of learned encodings) achieves the best forgetting prediction F1 across nearly all model/dataset/tuning configurations"
  - "Logit-change transfer explains why learning one example causes forgetting of another; a trainable logit-based forecasting model captures this on BART0 but fails on FLAN-T5"
  - "Replaying examples predicted to be forgotten by the forecasting model reduces catastrophic forgetting substantially compared to random replay"
abstract: "Language models deployed in the wild make errors. However, simply updating the model with the corrected error instances causes catastrophic forgetting---the updated model makes errors on instances learned during the instruction tuning or upstream training phase. Randomly replaying upstream data yields unsatisfactory performance and often comes with high variance and poor controllability. To this end, we try to forecast upstream examples that will be forgotten due to a model update for improved controllability of the replay process and interpretability. We train forecasting models given a collection of online learned examples and corresponding forgotten upstream pre-training examples. We propose a partially interpretable forecasting model based on the observation that changes in pre-softmax logit scores of pretraining examples resemble that of online learned examples, which performs decently on BART but fails on T5 models. We further show a black-box classifier based on inner products of example representations achieves better forecasting performance over a series of setups. Finally, we show that we reduce forgetting of upstream pretraining examples by replaying examples that are forecasted to be forgotten, demonstrating the practical utility of forecasting example forgetting."
---

# What Will My Model Forget? Forecasting Forgotten Examples in Language Model Refinement

## Overview

This paper studies the problem of **forecasting which upstream pretraining examples will be forgotten** when a pretrained language model (PTLM) is fine-tuned to correct a single prediction error (model refinement). The key insight is the "logit-change transfer" phenomenon: the change in pre-softmax logit scores of an online-learned example proportionally transfers to upstream pretraining examples, causing their predictions to flip. The authors build two forecasting models—a partially interpretable logit-based model and a black-box representation-based model—and show that replaying the forecasted-to-be-forgotten examples during model refinement significantly reduces catastrophic forgetting compared to random replay.

The representation-based forecasting model (inner products of learned example encodings, augmented with a frequency prior) achieves the best F1 across 7 of 8 model/dataset/tuning configurations and reduces EM Drop Ratio from ~9.3% to ~1.6% on BART0 and from 0.3–4.4% to 0.1–0.6% on FLAN-T5 models.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → logit-change transfer insight |
| [claims.md](logic/claims.md) | 6 falsifiable claims (C01–C06) |
| [concepts.md](logic/concepts.md) | 10 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 5 verification plans (E01–E05) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: forecasting model pipeline with encoder + kernel/classifier |
| [solution/algorithm.md](logic/solution/algorithm.md) | NTK-based logit transfer + representation forecasting, margin/BCE loss |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions: model type, scale, task domain |
| [solution/heuristics.md](logic/solution/heuristics.md) | 6 convergence and design tricks |
| [related_work.md](logic/related_work.md) | 12 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/forecasting.py](src/execution/forecasting.py) | Logit-based and representation-based forecasting models | C01, C02, C03 |
| [execution/model_refinement.py](src/execution/model_refinement.py) | Model refinement with targeted replay loop | C04, C05 |
| [configs/training.md](src/configs/training.md) | Fine-tuning and replay hyperparameters | — |
| [configs/model.md](src/configs/model.md) | Forecasting model architecture configuration | — |
| [environment.md](src/environment.md) | Hardware, dependencies, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 8 tables + 2 figures |
