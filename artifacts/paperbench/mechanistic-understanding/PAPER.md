---
title: "A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity"
authors: ["Andrew Lee", "Xiaoyan Bai", "Itamar Pres", "Martin Wattenberg", "Jonathan K. Kummerfeld", "Rada Mihalcea"]
year: 2024
venue: "arXiv"
doi: "arXiv:2401.01967v1"
ara_version: "1.0"
domain: "Mechanistic Interpretability / LLM Alignment"
keywords: ["DPO", "toxicity", "mechanistic interpretability", "alignment", "GPT2", "MLP value vectors", "jailbreak", "residual stream", "RLHF", "un-alignment"]
claims_summary:
  - "Toxicity is encoded in specific MLP value vectors in GPT2-medium, identifiable via cosine similarity with a trained probe vector"
  - "DPO does not remove toxic capability but learns a distributed residual-stream offset that bypasses toxic activation regions"
  - "DPO alignment can be trivially reversed by scaling as few as 7 toxic key vectors by 10×, recovering pre-alignment toxicity without affecting perplexity"
abstract: "While alignment algorithms are now commonly used to tune pre-trained language models towards a user's preferences, we lack explanations for the underlying mechanisms in which models become 'aligned', thus making it difficult to explain phenomena like jailbreaks. In this work we study a popular algorithm, direct preference optimization (DPO), and the mechanisms by which it reduces toxicity. Namely, we first study how toxicity is represented and elicited in a pre-trained language model, GPT2-medium. We then apply DPO with a carefully crafted pairwise dataset to reduce toxicity. We examine how the resulting model averts toxic outputs, and find that capabilities learned from pre-training are not removed, but rather bypassed. We use this insight to demonstrate a simple method to un-align the model, reverting it back to its toxic behavior."
---

# A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity

## Overview

This paper provides the first mechanistic explanation of how Direct Preference Optimization (DPO) suppresses undesirable behavior—specifically toxicity—in a pre-trained language model. Working with GPT2-medium, the authors (1) extract toxic vectors from MLP blocks using a trained linear probe, (2) apply DPO with a PPLM-generated pairwise dataset, and (3) show that DPO does not erase toxic capabilities but instead learns a distributed residual-stream offset that steers activations away from "toxic regions" in the hidden space. This offset is spread across many minimally-shifted value vectors in earlier MLP layers, preserving overall language quality while suppressing toxicity. The mechanistic insight directly explains why aligned models are vulnerable to jailbreaks: the toxic vectors remain intact and can be reactivated by scaling their corresponding key vectors.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight |
| [claims.md](logic/claims.md) | 6 falsifiable claims (C01–C06) |
| [concepts.md](logic/concepts.md) | 11 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 6 verification plans (E01–E06) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: probe extraction → DPO training → mechanistic analysis |
| [solution/algorithm.md](logic/solution/algorithm.md) | DPO loss, MLP decomposition, activation region bypass |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and known limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | 5 convergence tricks and design choices |
| [related_work.md](logic/related_work.md) | 12 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/toxic_probe.py](src/execution/toxic_probe.py) | Linear toxicity probe training on Jigsaw dataset | C01 |
| [execution/toxic_vectors.py](src/execution/toxic_vectors.py) | MLP toxic vector extraction and SVD decomposition | C01 |
| [execution/interventions.py](src/execution/interventions.py) | Residual stream subtraction interventions | C02 |
| [execution/dpo_training.py](src/execution/dpo_training.py) | DPO fine-tuning loop with PPLM data construction | C03 |
| [execution/unalignment.py](src/execution/unalignment.py) | Key-vector scaling to undo DPO alignment | C06 |
| [configs/training.md](src/configs/training.md) | DPO training hyperparameters | — |
| [configs/model.md](src/configs/model.md) | GPT2-medium architecture configuration | — |
| [environment.md](src/environment.md) | Hardware, dependencies, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 14-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 4 tables + 5 figures |
| [tables/table1_toxic_vector_tokens.md](evidence/tables/table1_toxic_vector_tokens.md) | Top toxic tokens per vector |
| [tables/table2_intervention_results.md](evidence/tables/table2_intervention_results.md) | Toxicity/PPL/F1 for interventions and DPO |
| [tables/table3_generation_examples.md](evidence/tables/table3_generation_examples.md) | Top-k and continuations before/after intervention |
| [tables/table4_unalignment_results.md](evidence/tables/table4_unalignment_results.md) | Un-alignment results via key vector scaling |
| [tables/table5_dpo_hyperparameters.md](evidence/tables/table5_dpo_hyperparameters.md) | DPO training hyperparameters |
| [tables/table6_pplm_hyperparameters.md](evidence/tables/table6_pplm_hyperparameters.md) | PPLM generation hyperparameters |
| [figures/figure1_logit_lens.md](evidence/figures/figure1_logit_lens.md) | Logit lens probability of "sh*t" across layers |
| [figures/figure2_mean_activations.md](evidence/figures/figure2_mean_activations.md) | Mean activations for top-5 toxic vectors |
| [figures/figure4_residual_shift.md](evidence/figures/figure4_residual_shift.md) | Residual stream shift out of toxic regions at layer 19 |
| [figures/figure5_cosine_similarity.md](evidence/figures/figure5_cosine_similarity.md) | Cosine similarity between δMLP.v and δx per layer |
