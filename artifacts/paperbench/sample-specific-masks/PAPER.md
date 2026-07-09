---
title: "Sample-specific Masks for Visual Reprogramming-based Prompting"
authors: ["Chengyi Cai", "Zesheng Ye", "Lei Feng", "Jianzhong Qi", "Feng Liu"]
year: 2024
venue: "ICML 2024 (Proceedings of the 41st International Conference on Machine Learning)"
doi: "arXiv:2406.03150v1"
ara_version: "1.0"
domain: "Visual Reprogramming / Transfer Learning / Prompting"
keywords: ["visual reprogramming", "sample-specific masks", "prompting", "transfer learning", "approximation error", "convolutional neural network", "label mapping", "pre-trained models", "PAC learning", "watermarking"]
claims_summary:
  - "Shared masks in existing VR methods cause suboptimal generalization: different images require different mask placements, and a single shared mask increases training loss for many individual samples"
  - "SMM is theoretically guaranteed to have lower approximation error than shared-mask VR methods because Fshr(f'P) ⊆ Fsmm(f'P) (Proposition 4.3)"
  - "SMM empirically outperforms all shared-mask baselines (Pad, Narrow, Medium, Full watermarking) on most datasets for ResNet-18, ResNet-50, and ViT-B32"
  - "Three-channel sample-specific masks outperform single-channel variants, especially on datasets with varying color palettes"
  - "Patch-wise interpolation is more computationally efficient than bilinear or bicubic interpolation for upscaling generated masks"
abstract: "Visual reprogramming (VR) is a prompting technique that aims to re-purpose a pre-trained model (e.g., a classifier on ImageNet) to target tasks (e.g., medical data prediction) by learning a small-scale pattern added into input images instead of tuning considerable parameters within the model. The location of the pattern within input samples is usually determined by a pre-defined mask shared across all samples. In this paper, we show that the shared mask potentially limits VR's generalization and increases its approximation error due to the lack of sample-level adaptation. Motivated by this finding, we design a new framework for VR called sample-specific multi-channel masks (SMM). Specifically, SMM employs a lightweight ConvNet and patch-wise interpolation to generate sample-specific three-channel masks instead of a shared and pre-defined mask. Since we generate different masks for individual samples, SMM is theoretically shown to reduce approximation error for the target tasks compared with existing state-of-the-art VR methods. We also empirically demonstrate its performance gain on both ResNet and ViT. The success of SMM further highlights the broader applicability of VR in leveraging the latent knowledge of pre-trained models for various target tasks."
---

# Sample-specific Masks for Visual Reprogramming-based Prompting

## Overview

Visual Reprogramming (VR) adapts a frozen pre-trained classifier to new target tasks by learning a small additive noise pattern in the input space. Prior VR methods apply a single shared binary mask (determining where the pattern is added) uniformly across all samples. This paper demonstrates that different images prefer different mask placements and that a shared mask provably increases approximation error. The proposed **SMM (Sample-specific Multi-channel Masks)** framework replaces the fixed binary mask with a lightweight CNN that generates a distinct three-channel continuous mask for each input image, combined with a patch-wise interpolation module for efficient upscaling. SMM is theoretically grounded via PAC learning (Proposition 4.3: Fshr ⊆ Fsmm implies lower approximation error) and empirically validated across 11 datasets on ResNet-18, ResNet-50, and ViT-B32, achieving consistent performance gains over all shared-mask baselines while adding fewer than 0.23% extra parameters relative to the pre-trained model.

The key novelty is sample-level adaptivity: the shared learnable pattern δ provides dataset-wide structure, while the CNN-generated mask fmask(r(xi)|ϕ) allows per-image adaptation of where that pattern is applied, resulting in the composite transformation `fin(xi) = r(xi) + δ ⊙ fmask(r(xi)|ϕ)`.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations of shared-mask failure → gaps → key insight enabling SMM |
| [claims.md](logic/claims.md) | 6 falsifiable claims (C01–C06) |
| [concepts.md](logic/concepts.md) | 10 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 6 verification plans (E01–E06) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: mask generator + patch-wise interpolation + VR pipeline |
| [solution/algorithm.md](logic/solution/algorithm.md) | SMM training algorithm (Algorithm 1), ILM (Algorithm 4), complexity |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions for SMM validity |
| [solution/heuristics.md](logic/solution/heuristics.md) | 5 convergence and design tricks |
| [related_work.md](logic/related_work.md) | 12 typed dependency entries |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/smm.py](src/execution/smm.py) | Core SMM: MaskGenerator CNN + PatchWiseInterpolation + SMMForward | C01–C04 |
| [execution/label_mapping.py](src/execution/label_mapping.py) | ILM, FLM, RLM label mapping algorithms | C03 |
| [execution/baselines.py](src/execution/baselines.py) | Pad, Narrow, Medium, Full watermarking baselines | C01, C03 |
| [configs/training.md](src/configs/training.md) | Training hyperparameters (LR, milestones, batch sizes) | — |
| [configs/model.md](src/configs/model.md) | Mask generator architecture configurations | — |
| [environment.md](src/environment.md) | Hardware, deps, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 8 tables + 1 figure |
| [tables/table1_resnet_main_results.md](evidence/tables/table1_resnet_main_results.md) | Table 1: ResNet-18 & ResNet-50 accuracy on 11 datasets (5 methods) |
| [tables/table2_vit_main_results.md](evidence/tables/table2_vit_main_results.md) | Table 2: ViT-B32 accuracy on 11 datasets (5 methods) |
| [tables/table3_ablation_masking.md](evidence/tables/table3_ablation_masking.md) | Table 3: Ablation study on masking variants (ResNet-18) |
| [tables/table4_parameter_statistics.md](evidence/tables/table4_parameter_statistics.md) | Table 4: Mask generator parameter size statistics |
| [tables/table5_interpolation_comparison.md](evidence/tables/table5_interpolation_comparison.md) | Table 5: Patch-wise vs bilinear vs bicubic interpolation efficiency |
| [tables/table6_dataset_info.md](evidence/tables/table6_dataset_info.md) | Table 6: Dataset sizes and class counts |
| [tables/table10_label_mapping_comparison.md](evidence/tables/table10_label_mapping_comparison.md) | Table 10: SMM improvement across all label mapping methods |
| [tables/table_stanfordcars.md](evidence/tables/table_stanfordcars.md) | StanfordCars (Table 12): ineffective VR case |
| [figures/figure4_patch_size_ablation.md](evidence/figures/figure4_patch_size_ablation.md) | Figure 4: Accuracy vs patch size on EuroSAT, Flowers102, CIFAR100, SVHN |
