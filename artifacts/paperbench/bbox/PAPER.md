---
title: "BBOX-ADAPTER: Lightweight Adapting for Black-Box Large Language Models"
authors: ["Haotian Sun", "Yuchen Zhuang", "Wei Wei", "Chao Zhang", "Bo Dai"]
year: 2024
venue: "ICML 2024 (Proceedings of the 41st International Conference on Machine Learning)"
doi: "arXiv:2402.08219v2"
ara_version: "1.0"
domain: "LLM Adaptation, Black-Box Fine-Tuning"
keywords: ["black-box LLM", "adapter", "energy-based model", "noise contrastive estimation", "online adaptation", "beam search", "plug-and-play", "GPT-3.5", "cost efficiency", "AI feedback"]
claims_summary:
  - "BBOX-ADAPTER improves black-box LLM performance by up to 6.77% on downstream QA tasks without accessing model parameters or output probabilities"
  - "Ranking-based NCE loss outperforms MLM loss baseline by up to ~10% accuracy on StrategyQA/GSM8K"
  - "BBOX-ADAPTER reduces training cost by 31.30x and inference cost by 1.84x compared to supervised fine-tuning (SFT)"
  - "A single trained adapter transfers to other black-box LLMs in plug-and-play fashion, improving davinci-002 by 6.85% and Mixtral-8x7B by 4.50% on average"
  - "AI feedback without ground-truth labels achieves performance competitive with ground-truth-supervised training"
abstract: "Adapting state-of-the-art Large Language Models (LLMs) like GPT-4 and Gemini for specific tasks is challenging. Due to the opacity in their parameters, embeddings, and even output probabilities, existing fine-tuning adaptation methods are inapplicable. Consequently, adapting these black-box LLMs is only possible through their API services, raising concerns about transparency, privacy, and cost. To address these challenges, we introduce BBOX-ADAPTER, a novel lightweight adapter for black-box LLMs. BBOX-ADAPTER distinguishes target and source domain data by treating target data as positive and source data as negative. It employs a ranking-based Noise Contrastive Estimation (NCE) loss to promote the likelihood of target domain data while penalizing that of the source domain. Furthermore, it features an online adaptation mechanism, which incorporates real-time positive data sampling from ground-truth, human, or AI feedback, coupled with negative data from previous adaptations. Extensive experiments demonstrate BBOX-ADAPTER's effectiveness and cost efficiency. It improves model performance by up to 6.77% across diverse tasks and domains, while reducing training and inference costs by 31.30x and 1.84x, respectively."
---

# BBOX-ADAPTER: Lightweight Adapting for Black-Box Large Language Models

## Overview

BBOX-ADAPTER is a novel lightweight adapter framework for adapting state-of-the-art black-box LLMs (e.g., GPT-3.5-turbo, Gemini) to specific downstream tasks without accessing internal model parameters, high-dimensional representations, or output token probabilities. The core idea is to frame black-box LLM adaptation as a sampling problem from an energy-based model (EBM): a small adapter (0.1B–0.3B parameters, implemented as DeBERTa or BERT) learns a scalar energy function that scores generated outputs. It is trained using a ranking-based Noise Contrastive Estimation (NCE) loss, distinguishing target-domain (positive) from source-domain (negative) text. At inference, the black-box LLM acts as a proposal generator while the adapter acts as a scorer, enabling sentence-level beam search. An online adaptation loop iteratively updates the adapter using candidates from its own adapted inferences.

BBOX-ADAPTER achieves up to 6.77% accuracy gains over the unadapted base model on four QA benchmarks, reduces training cost 31.30× versus Azure SFT, and supports plug-and-play transfer to unseen LLMs without retraining.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight motivating BBOX-ADAPTER |
| [claims.md](logic/claims.md) | 8 falsifiable claims (C01–C08) |
| [concepts.md](logic/concepts.md) | 10 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 7 verification plans (E01–E07) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: black-box LLM + EBM adapter + online loop |
| [solution/algorithm.md](logic/solution/algorithm.md) | NCE loss gradient + beam search + online adaptation pseudocode |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions: black-box API access, text-only outputs |
| [solution/heuristics.md](logic/solution/heuristics.md) | 6 convergence tricks (spectral norm, beam size, temperature, etc.) |
| [related_work.md](logic/related_work.md) | 12 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/ebm_adapter.py](src/execution/ebm_adapter.py) | EBM adapter, NCE loss, beam search inference | C01, C02, C03, C04 |
| [execution/online_adaptation.py](src/execution/online_adaptation.py) | Online adaptation loop (Algorithm 1) | C01, C06 |
| [configs/training.md](src/configs/training.md) | Adapter training hyperparameters (lr, batch, steps, optimizer) | — |
| [configs/model.md](src/configs/model.md) | Adapter backbone and LLM configurations | — |
| [environment.md](src/environment.md) | Hardware, Python/PyTorch/HuggingFace deps, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 14-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 8 tables + 0 extracted quantitative figures |
| [tables/table2_main_results.md](evidence/tables/table2_main_results.md) | Main results adapting GPT-3.5-turbo across 4 datasets |
| [tables/table3_plug_and_play.md](evidence/tables/table3_plug_and_play.md) | Plug-and-play transfer to davinci-002 and Mixtral-8×7B |
| [tables/table4_cost_analysis.md](evidence/tables/table4_cost_analysis.md) | Training/inference cost comparison (StrategyQA, GSM8K) |
| [tables/table5_ablation_loss.md](evidence/tables/table5_ablation_loss.md) | NCE vs MLM loss ablation (StrategyQA, GSM8K) |
| [tables/table6_whitebox_extension.md](evidence/tables/table6_whitebox_extension.md) | Mixtral-8×7B white-box extension (accuracy + VRAM) |
| [tables/table7_toxigen.md](evidence/tables/table7_toxigen.md) | ToxiGen toxicity reduction results |
| [tables/table8_lora_hyperparams.md](evidence/tables/table8_lora_hyperparams.md) | SFT-LoRA hyperparameter configuration |
| [tables/table9_azure_sft_gridsearch.md](evidence/tables/table9_azure_sft_gridsearch.md) | Azure-SFT grid search on GSM8K |
| [tables/table10_main_results_std.md](evidence/tables/table10_main_results_std.md) | Main results with standard deviation |
