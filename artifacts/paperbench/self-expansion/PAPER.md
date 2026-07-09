---
title: "Self-Expansion of Pre-trained Models with Mixture of Adapters for Continual Learning"
authors: ["Huiyi Wang", "Haodong Lu", "Lina Yao", "Dong Gong"]
year: 2025
venue: "arXiv (CVPR 2025 version)"
doi: "arXiv:2403.18886v3"
ara_version: "1.0"
domain: "Continual Learning / Parameter-Efficient Fine-Tuning"
keywords:
  - continual learning
  - pre-trained models
  - adapter
  - mixture of experts
  - self-expansion
  - catastrophic forgetting
  - class-incremental learning
  - ViT
  - representation descriptor
  - stability-plasticity
claims_summary:
  - "SEMA achieves state-of-the-art CIL accuracy on CIFAR-100, ImageNet-R, ImageNet-A, and VTAB without memory rehearsal using ViT-B/16"
  - "SEMA expands model parameters at a sub-linear rate w.r.t. number of tasks, unlike task-specific methods that grow linearly"
  - "On-demand self-expansion with z-score-based detection improves over no-expansion (single adapter) baseline and all static routing strategies"
  - "The SEMA framework generalises across functional adapter types (Adapter, LoRA, Convpass) with comparable performance"
abstract: "Continual learning (CL) aims to continually accumulate knowledge from a non-stationary data stream without catastrophic forgetting of learned knowledge, requiring a balance between stability and adaptability. Relying on the generalizable representation in pre-trained models (PTMs), PTM-based CL methods perform effective continual adaptation on downstream tasks by adding learnable adapters or prompts upon the frozen PTMs. However, many existing PTM-based CL methods use restricted adaptation on a fixed set of these modules to avoid forgetting, suffering from limited CL ability. Periodically adding task-specific modules results in linear model growth rate and impaired knowledge reuse. We propose Self-Expansion of pre-trained models with Modularized Adaptation (SEMA), a novel approach to enhance the control of stability-plasticity balance in PTM-based CL. SEMA automatically decides to reuse or add adapter modules on demand in CL, depending on whether significant distribution shift that cannot be handled is detected at different representation levels. We design modular adapter consisting of a functional adapter and a representation descriptor. The representation descriptors are trained as a distribution shift indicator and used to trigger self-expansion signals. For better composing the adapters, an expandable weighting router is learned jointly for mixture of adapter outputs. SEMA enables better knowledge reuse and sub-linear expansion rate. Extensive experiments demonstrate the effectiveness of the proposed self-expansion method, achieving state-of-the-art performance compared to PTM-based CL methods without memory rehearsal."
---

# Self-Expansion of Pre-trained Models with Mixture of Adapters for Continual Learning

## Overview

SEMA (Self-Expansion of pre-trained models with Modularized Adaptation) addresses the stability-plasticity trade-off in continual learning by automatically deciding *when* and *where* (which ViT transformer layer) to add new adapter modules. The core innovation is the **modular adapter**: a paired (functional adapter, representation descriptor) unit. The representation descriptor is an autoencoder trained to reconstruct intermediate features; its z-score of reconstruction error serves as a novelty detector. When all existing descriptors in a layer flag novel patterns, one new adapter is added. A learned expandable router computes a soft weighted mixture over all active adapters. Because expansion is on-demand rather than per-task, the total parameter count grows sub-linearly with task count. SEMA achieves state-of-the-art rehearsal-free CIL results on CIFAR-100, ImageNet-R (5/10/20-task), ImageNet-A, and VTAB using ViT-B/16 backbones.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight: why fixed adapter pools and linear expansion fail |
| [claims.md](logic/claims.md) | 4 falsifiable claims (C01–C04) |
| [concepts.md](logic/concepts.md) | 9 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 6 verification plans (E01–E06) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: frozen ViT + expandable modular adapter modules + router per layer |
| [solution/algorithm.md](logic/solution/algorithm.md) | SEMA training loop, z-score expansion signal, mixture routing |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions: CIL setting, task-oriented expansion limits |
| [solution/heuristics.md](logic/solution/heuristics.md) | 6 convergence/design tricks |
| [related_work.md](logic/related_work.md) | 12 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/sema.py](src/execution/sema.py) | Core SEMA: functional adapter, RD autoencoder, router, z-score expansion | C01, C02, C03 |
| [configs/training.md](src/configs/training.md) | Training hyperparameters with rationale | — |
| [configs/model.md](src/configs/model.md) | Model architecture configurations | — |
| [environment.md](src/environment.md) | Hardware, deps, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 15 tables + 5 figures |
| [tables/table1_main_results.md](evidence/tables/table1_main_results.md) | Main CIL comparison (ViT-B/16-IN1K) |
| [tables/table2_ablation_composing.md](evidence/tables/table2_ablation_composing.md) | Ablation: expansion and adapter composing strategies |
| [tables/table3_adapter_variants.md](evidence/tables/table3_adapter_variants.md) | Ablation: functional adapter type variants |
| [tables/table4_in21k.md](evidence/tables/table4_in21k.md) | Main CIL comparison (ViT-B/16-IN21K) |
| [tables/table5_param_efficiency.md](evidence/tables/table5_param_efficiency.md) | Expansion-by-task vs SEMA: params and accuracy |
| [tables/table6_added_params.md](evidence/tables/table6_added_params.md) | Added parameters (M) per method |
| [tables/table7_rd_routing.md](evidence/tables/table7_rd_routing.md) | Learned router vs RD-based routing |
| [tables/table8_train_time.md](evidence/tables/table8_train_time.md) | Per-batch training time (seconds) |
| [tables/table9_inference_time.md](evidence/tables/table9_inference_time.md) | Per-image inference time (ms) |
| [tables/table10_50task.md](evidence/tables/table10_50task.md) | 50-task evaluation on ImageNet-R and ImageNet-A |
| [tables/table11_limited_data_vtab.md](evidence/tables/table11_limited_data_vtab.md) | Limited data on VTAB |
| [tables/table12_limited_data_ina.md](evidence/tables/table12_limited_data_ina.md) | Limited data on ImageNet-A |
| [tables/table13_multiple_seeds.md](evidence/tables/table13_multiple_seeds.md) | Mean ± std over 5 runs |
| [tables/table14_ranpac.md](evidence/tables/table14_ranpac.md) | SEMA+RanPAC combination results |
| [tables/table15_clip.md](evidence/tables/table15_clip.md) | Results with CLIP backbone |
| [figures/fig4_reconstruction_error.md](evidence/figures/fig4_reconstruction_error.md) | RD reconstruction errors during training showing expansion decisions |
| [figures/fig5_adapter_usage.md](evidence/figures/fig5_adapter_usage.md) | Adapter usage weights per task on VTAB |
| [figures/fig6_threshold.md](evidence/figures/fig6_threshold.md) | Accuracy and adapter count vs expansion threshold |
| [figures/fig7_multilayer.md](evidence/figures/fig7_multilayer.md) | Accuracy and adapter count vs expansion layer range |
| [figures/fig8_param_growth.md](evidence/figures/fig8_param_growth.md) | Added parameters (M) over tasks on ImageNet-A |
