---
title: "APT: Adaptive Pruning and Tuning Pretrained Language Models for Efficient Training and Inference"
authors: ["Bowen Zhao", "Hannaneh Hajishirzi", "Qingqing Cao"]
year: 2024
venue: "ICML 2024 (Proceedings of the 41st International Conference on Machine Learning, PMLR 235)"
doi: "arXiv:2401.12200v2"
ara_version: "1.0"
domain: "Parameter-Efficient Fine-Tuning / Model Pruning / Language Models"
keywords:
  - adaptive pruning
  - adaptive tuning
  - parameter-efficient fine-tuning
  - structured pruning
  - LoRA
  - knowledge distillation
  - salience scoring
  - LLM compression
  - training efficiency
  - inference efficiency
claims_summary:
  - "APT maintains up to 98% task performance when pruning 60% of parameters in RoBERTa and T5 models"
  - "APT speeds up LM fine-tuning by up to 8× and reduces training memory by up to 70% compared to LoRA+Prune"
  - "APT preserves 86.4% of LLaMA models' performance with 70% parameters remaining while using only 30% of LLMPruner's training memory"
  - "Outlier-aware salience scoring (combining weight-gradient product with kurtosis) is essential for accurate large-LM pruning"
  - "Adaptive tuning (dynamic rank increase in salient layers) accelerates convergence and improves end-task accuracy"
abstract: "Fine-tuning and inference with large Language Models (LM) are generally known to be expensive. Parameter-efficient fine-tuning over pretrained LMs reduces training memory by updating a small number of LM parameters but does not improve inference efficiency. Structured pruning improves LM inference efficiency by removing consistent parameter blocks, yet often increases training memory and time. To improve both training and inference efficiency, we introduce APT that adaptively prunes and tunes parameters for the LMs. At the early stage of fine-tuning, APT dynamically adds salient tuning parameters for fast and accurate convergence while discarding unimportant parameters for efficiency. Compared to baselines, our experiments show that APT maintains up to 98% task performance when pruning 60% of the parameters in RoBERTa and T5 models. APT also preserves 86.4% of LLaMA models' performance with 70% parameters remaining. Furthermore, APT speeds up LMs' fine-tuning by up to 8× and reduces large LMs' memory training footprint by up to 70%."
---

# APT: Adaptive Pruning and Tuning Pretrained Language Models for Efficient Training and Inference

## Overview

APT addresses a fundamental tension in large language model deployment: parameter-efficient fine-tuning (PEFT) methods reduce training costs but leave inference cost unchanged, while structured pruning improves inference efficiency but typically increases training time and memory. APT resolves this by jointly and adaptively selecting which parameters to prune (via binary masks learned from an outlier-aware salience scoring function) and which adapter parameters to grow (by dynamically increasing ranks in salient APT adapter layers). The result is a system that simultaneously improves both training and inference efficiency with minimal task performance loss.

The key technical contributions are: (1) an APT adapter architecture extending LoRA with learnable binary pruning masks on input/output dimensions and dynamic rank adjustment; (2) an outlier-aware salience scoring function combining activation-gradient products with kurtosis to preserve outlier parameters important for task-specific capabilities; (3) a fast binary-search block selection algorithm for structured pruning of MHA heads, FFN neurons, and hidden dimensions simultaneously; (4) a self-knowledge distillation technique sharing frozen parameters between teacher and student to reduce distillation overhead; and (5) a cubic sparsity schedule for stable progressive pruning. Experiments on BERT, RoBERTa, T5, and LLaMA across GLUE, SQuAD, CNN/DM, and instruction-following tasks demonstrate consistent improvements over all baselines.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight motivating APT |
| [claims.md](logic/claims.md) | 8 falsifiable claims (C01–C08) |
| [concepts.md](logic/concepts.md) | 10 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 6 verification plans (E01–E06) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: APT adapter + pruning + tuning + distillation components |
| [solution/algorithm.md](logic/solution/algorithm.md) | APT algorithm with salience scoring, binary search, rank update, complexity |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and known limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | 7 convergence tricks with rationale |
| [related_work.md](logic/related_work.md) | 12 typed dependency entries |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/apt_adapter.py](src/execution/apt_adapter.py) | APT adapter forward pass with binary masks and dynamic rank | C01, C02 |
| [execution/salience.py](src/execution/salience.py) | Outlier-aware salience scoring + EMA update | C04, C05 |
| [execution/pruning.py](src/execution/pruning.py) | Binary search block selection and mask update | C01, C02 |
| [execution/distillation.py](src/execution/distillation.py) | Self-knowledge distillation loss with random layer mapping | C03 |
| [configs/training.md](src/configs/training.md) | Dataset-specific hyperparameters with rationale | — |
| [configs/model.md](src/configs/model.md) | Model configurations and adapter placement | — |
| [environment.md](src/environment.md) | Hardware, dependencies, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 14-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 12 tables + 3 figures |
| [tables/table1_efficiency_comparison.md](evidence/tables/table1_efficiency_comparison.md) | Table 1: Method efficiency comparison matrix |
| [tables/table2_roberta_t5_main.md](evidence/tables/table2_roberta_t5_main.md) | Table 2: Main results RoBERTa and T5 at 60% sparsity |
| [tables/table3_llama2_7b_main.md](evidence/tables/table3_llama2_7b_main.md) | Table 3: LLaMA2 7B 30% sparsity results |
| [tables/table4_ablation_roberta.md](evidence/tables/table4_ablation_roberta.md) | Table 4: Ablation study on RoBERTa-base |
| [tables/table5_ablation_llama.md](evidence/tables/table5_ablation_llama.md) | Table 5: LLaMA 2 7B ablation under 30% and 50% sparsity |
| [tables/table6_hyperparameters.md](evidence/tables/table6_hyperparameters.md) | Table 6: Full hyperparameter settings per dataset |
| [tables/table7_bert_baselines.md](evidence/tables/table7_bert_baselines.md) | Table 7: BERT comparison to PST and LRP baselines |
| [tables/table8_glue_detailed.md](evidence/tables/table8_glue_detailed.md) | Table 8: Detailed GLUE results vs LoRA+Distill |
| [tables/table9_llama_7b_13b.md](evidence/tables/table9_llama_7b_13b.md) | Table 9: LLaMA2 7B and 13B 30% sparsity results |
| [tables/table10_distillation_ablation.md](evidence/tables/table10_distillation_ablation.md) | Table 10: Distillation strategy ablation |
| [tables/table11_raw_efficiency_roberta_t5.md](evidence/tables/table11_raw_efficiency_roberta_t5.md) | Table 11: Raw efficiency metrics RoBERTa and T5 |
| [tables/table12_raw_efficiency_llama.md](evidence/tables/table12_raw_efficiency_llama.md) | Table 12: Raw efficiency metrics LLaMA2 7B |
| [figures/figure3_pareto_curves.md](evidence/figures/figure3_pareto_curves.md) | Figure 3: Task performance vs inference efficiency tradeoff curves |
