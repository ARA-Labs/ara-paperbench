---
title: "Semantic Self-Consistency: Enhancing Language Model Reasoning via Semantic Weighting"
authors: ["Tim Knappe", "Ryan Li", "Ayush Chauhan", "Kaylee Chhua", "Kevin Zhu", "Sean O'Brien"]
year: 2024
venue: "NeurIPS 2024"
doi: "arXiv:2410.07839v2"
ara_version: "1.0"
domain: "LLM reasoning, natural language processing"
keywords: ["self-consistency", "chain-of-thought", "semantic weighting", "LLM reasoning", "embedding", "outlier detection", "centroid proximity weighting", "cosine similarity", "BERT", "few-shot prompting"]
claims_summary:
  - "Semantic Consensus Weighting (SCW) using cosine similarity of reasoning-path embeddings generally outperforms standard self-consistency majority vote across datasets and models"
  - "Centroid Proximity Weighting (CPW) improves over self-consistency on arithmetic datasets (AQuA-RAT, SVAMP) but underperforms on commonsense reasoning (StrategyQA)"
  - "Embedding-based outlier removal (Isolation Forest, KNN, One-class SVM) applied before self-consistency voting improves or matches baseline across diverse model-dataset pairs"
abstract: "While large language models (LLMs) have rapidly improved their performance on a broad number of tasks, they still often fall short on reasoning tasks. As LLMs become more integrated in diverse real-world tasks, advancing their reasoning capabilities is crucial to their effectiveness in nuanced, complex problems. Wang et al.'s self-consistency framework reveals that sampling multiple rationales before taking a majority vote reliably improves model performance across various closed-answer reasoning tasks. Standard methods based on this framework aggregate the final decisions of these rationales but fail to utilize the semantic information detailed in the step-by-step reasoning paths. Our work introduces semantic self-consistency, enhancing this approach by incorporating and analyzing both the reasoning paths of these rationales in addition to their final decisions before taking a majority vote. These methods not only improve the reliability of reasoning paths but also cause more robust performance on complex reasoning tasks."
---

# Semantic Self-Consistency: Enhancing Language Model Reasoning via Semantic Weighting

## Overview

This paper extends the self-consistency framework (Wang et al., 2023) by introducing semantic weighting of LLM reasoning paths before taking a majority vote. Instead of treating all sampled rationales equally, the proposed methods embed each reasoning path using a fine-tuned BERT-based featurizer and apply either centroid-proximity weighting (CPW), cosine-similarity-based consensus weighting (SCW), or embedding-space outlier removal (KNN, Isolation Forest, One-class SVM) to up-weight or filter semantically consistent responses.

Experiments on AQuA-RAT (arithmetic), SVAMP (algebraic), and StrategyQA (commonsense) across five generator models (GPT-3.5, GPT-4o mini, Llama 2 7B, Llama 3 8B, Mistral 7B) demonstrate that SCW broadly improves over the self-consistency baseline, while CPW is effective on arithmetic tasks but not on commonsense reasoning. Outlier detection methods show consistent marginal gains, particularly on StrategyQA. The work is published at NeurIPS 2024.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight |
| [claims.md](logic/claims.md) | 6 falsifiable claims (C01–C06) |
| [concepts.md](logic/concepts.md) | 10 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 4 verification plans (E01–E04) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: generator → featurizer → weighting/filtering → majority vote |
| [solution/algorithm.md](logic/solution/algorithm.md) | CPW and SCW algorithms, outlier removal formulas, complexity |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and known limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | 5 convergence and configuration tricks |
| [related_work.md](logic/related_work.md) | 8 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/semantic_self_consistency.py](src/execution/semantic_self_consistency.py) | CPW, SCW, and outlier-removal implementations | C01, C02, C03 |
| [configs/training.md](src/configs/training.md) | Inference/sampling parameters with rationale | — |
| [configs/model.md](src/configs/model.md) | Generator and featurizer model configurations | — |
| [environment.md](src/environment.md) | Hardware, dependencies, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 9 tables + 3 figures |
| [tables/table1_semantic_consistency.md](evidence/tables/table1_semantic_consistency.md) | CPW and SCW vs SC baseline across all models and datasets |
| [tables/table2_outlier_detection.md](evidence/tables/table2_outlier_detection.md) | Outlier detection best/average accuracy across all models and datasets |
| [tables/table3_seq_length_bleu.md](evidence/tables/table3_seq_length_bleu.md) | Sequence length, accuracy increase, BLEU score per model/dataset |
| [tables/table4_accuracy_deviation.md](evidence/tables/table4_accuracy_deviation.md) | Accuracy deviation (%) across models and datasets |
| [tables/table5_varied_temp.md](evidence/tables/table5_varied_temp.md) | Weighted self-consistency with varying temperature |
| [tables/table6_featurizer_distance.md](evidence/tables/table6_featurizer_distance.md) | Average embedding distance per featurizer model |
| [tables/table7_kmeans.md](evidence/tables/table7_kmeans.md) | K-means outlier detection performance (k=2) |
| [tables/table8_kmeans_avg.md](evidence/tables/table8_kmeans_avg.md) | K-means averaged over 10 runs |
| [tables/table9_ngram.md](evidence/tables/table9_ngram.md) | N-gram weighting results (n=2) |
| [figures/figure2_rouge_n.md](evidence/figures/figure2_rouge_n.md) | Rouge-N scores across models |
