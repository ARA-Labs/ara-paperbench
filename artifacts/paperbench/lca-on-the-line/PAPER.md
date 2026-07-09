---
title: "LCA-on-the-Line: Benchmarking Out-of-Distribution Generalization with Class Taxonomies"
authors: [Jia Shi, Gautam Gare, Jinjin Tian, Siqi Chai, Zhiqiu Lin, Arun Vasudevan, Di Feng, Francesco Ferroni, Shu Kong]
year: 2024
venue: "ICML 2024 (Proceedings of the 41st International Conference on Machine Learning)"
doi: "arXiv:2407.16067"
ara_version: "1.0"
domain: "Out-of-distribution generalization, computer vision, model evaluation"
keywords: [LCA distance, OOD generalization, class taxonomy, WordNet, ImageNet, CLIP, effective robustness, soft labels, K-means clustering, vision-language models]
claims_summary:
  - "In-distribution LCA distance strongly linearly correlates with OOD accuracy across VMs and VLMs (R²>0.7, PEA>0.7) on severely shifted datasets, while Top-1 accuracy fails to unify both model families"
  - "Latent class hierarchies constructed via K-means clustering on pretrained model features produce LCA distances that robustly correlate with OOD performance (mean PEA>0.66 on 4/5 OOD datasets)"
  - "Aligning model predictions with class taxonomy via LCA soft labels or prompt engineering consistently improves OOD generalization without sacrificing ID accuracy"
abstract: "We tackle the challenge of predicting models' Out-of-Distribution (OOD) performance using in-distribution (ID) measurements without requiring OOD data. Existing evaluations with 'Effective Robustness', which use ID accuracy as an indicator of OOD accuracy, encounter limitations when models are trained with diverse supervision and distributions, such as class labels (Vision Models, VMs, on ImageNet) and textual descriptions (Visual-Language Models, VLMs, on LAION). VLMs often generalize better to OOD data than VMs despite having similar or lower ID performance. To improve the prediction of models' OOD performance from ID measurements, we introduce the Lowest Common Ancestor (LCA)-on-the-Line framework. This approach revisits the established concept of LCA distance, which measures the hierarchical distance between labels and predictions within a predefined class hierarchy, such as WordNet. We assess 75 models using ImageNet as the ID dataset and five significantly shifted OOD variants, uncovering a strong linear correlation between ID LCA distance and OOD top-1 accuracy. Our method provides a compelling alternative for understanding why VLMs tend to generalize better. Additionally, we propose a technique to construct a taxonomic hierarchy on any dataset using K-means clustering, demonstrating that LCA distance is robust to the constructed taxonomic hierarchy. Moreover, we demonstrate that aligning model predictions with class taxonomies, through soft labels or prompt engineering, can enhance model generalization."
---

# LCA-on-the-Line: Benchmarking Out-of-Distribution Generalization with Class Taxonomies

## Overview

This paper proposes **LCA-on-the-Line**, a framework that uses the Lowest Common Ancestor (LCA) distance—a taxonomic metric measuring semantic severity of model mispredictions—as a unified predictor of out-of-distribution (OOD) performance. The key insight is that models making "better mistakes" (predicting semantically close classes) learn more transferable features and generalize better to OOD datasets, regardless of whether they are Vision Models (VMs) trained on class labels or Vision-Language Models (VLMs) trained on captions.

The paper evaluates 75 models (36 VMs + 39 VLMs) on ImageNet (ID) and five severely shifted OOD datasets, demonstrating strong linear correlation between ID LCA distance and OOD Top-1 accuracy (R²>0.7, PEA>0.7) on 4/5 OOD datasets. This unifies VM and VLM evaluation under a single metric, whereas the standard Accuracy-on-the-Line (using Top-1 ID accuracy) fails for cross-modality comparison. The framework is extended to datasets without predefined hierarchies via K-means clustering, and applied to improve OOD generalization via LCA soft labels and prompt engineering.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight: Accuracy-on-the-Line fails across VM/VLM families |
| [claims.md](logic/claims.md) | 5 falsifiable claims (C01–C05) covering LCA correlation, latent hierarchies, and generalization improvement |
| [concepts.md](logic/concepts.md) | 9 key terms: LCA distance, ELCA, WordNet hierarchy, effective robustness, K-means latent hierarchy, soft labels, information content, taxonomy alignment, OOD generalization |
| [experiments.md](logic/experiments.md) | 6 verification plans (E01–E06): correlation study, MAE prediction, K-means robustness, soft label probing, prompt engineering, simulation |
| [solution/architecture.md](logic/solution/architecture.md) | LCA-on-the-Line system: hierarchy loading, prediction extraction, LCA computation, correlation analysis |
| [solution/algorithm.md](logic/solution/algorithm.md) | LCA distance computation (depth and information content), ELCA, K-means hierarchy construction, LCA alignment loss |
| [solution/constraints.md](logic/solution/constraints.md) | LCA not effective for visually similar datasets (ImageNet-v2); weaker on small-class datasets |
| [solution/heuristics.md](logic/solution/heuristics.md) | 5 convergence tricks: temperature=25, lambda=0.03, min-max scaling, 9-layer K-means, alpha interpolation |
| [related_work.md](logic/related_work.md) | 12 typed dependencies covering Accuracy-on-the-Line, Agreement-on-the-Line, LCA/taxonomy prior work, VLM studies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/lca_distance.py](src/execution/lca_distance.py) | LCA distance computation (depth and information content variants) | C01, C02 |
| [execution/lca_alignment_loss.py](src/execution/lca_alignment_loss.py) | LCA alignment loss (Algorithm 1) for soft label training | C03 |
| [execution/kmeans_hierarchy.py](src/execution/kmeans_hierarchy.py) | K-means based latent hierarchy construction (9-layer) | C02 |
| [execution/eval_metrics.py](src/execution/eval_metrics.py) | Correlation metrics (R², PEA, KEN, SPE) and MAE prediction | C01 |
| [configs/training.md](src/configs/training.md) | Linear probing hyperparameters: lr, batch size, optimizer, epochs | — |
| [configs/model.md](src/configs/model.md) | Model configurations: 36 VMs (torchvision) and 39 VLMs (CLIP/OpenCLIP) | — |
| [environment.md](src/environment.md) | Hardware (GTX 1080 Ti), dependencies (PyTorch, CLIP, OpenCLIP, NLTK) | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG covering problem discovery, metric exploration, dead ends, and applications |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 8 tables + 2 figures |
| [tables/table1_model_performance.md](evidence/tables/table1_model_performance.md) | LCA and Top-1 for ResNet18, ResNet50, CLIP_RN50, CLIP_RN50x4 across all datasets |
| [tables/table2_correlation.md](evidence/tables/table2_correlation.md) | R² and PEA of ID LCA/Top1 vs OOD Top1/Top5 for 75 models |
| [tables/table3_mae_prediction.md](evidence/tables/table3_mae_prediction.md) | MAE error prediction comparison across methods |
| [tables/table4_kmeans_latent.md](evidence/tables/table4_kmeans_latent.md) | PEA statistics for 75 latent hierarchies from K-means |
| [tables/table5_soft_labels_wordnet.md](evidence/tables/table5_soft_labels_wordnet.md) | Soft labeling with WordNet: 6 backbones on 6 datasets |
| [tables/table6_soft_labels_latent.md](evidence/tables/table6_soft_labels_latent.md) | Soft labeling with latent hierarchies on ResNet-18 |
| [tables/table7_simulation.md](evidence/tables/table7_simulation.md) | Simulation results: model f (causal) vs g (confounding) |
| [tables/table8_lca_elca.md](evidence/tables/table8_lca_elca.md) | LCA and ELCA measurements across datasets |
| [figures/figure1_correlation_plot.md](evidence/figures/figure1_correlation_plot.md) | Divergent Top-1 vs unified LCA correlation with ObjectNet OOD accuracy |
| [figures/figure5_full_correlation.md](evidence/figures/figure5_full_correlation.md) | Full 8-panel correlation plots: Top-1/LCA × Top-1/Top-5 for 4 OOD datasets |
