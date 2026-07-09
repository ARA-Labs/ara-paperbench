---
title: "Test-Time Model Adaptation with Only Forward Passes"
authors: ["Shuaicheng Niu", "Chunyan Miao", "Guohao Chen", "Pengcheng Wu", "Peilin Zhao"]
year: 2024
venue: "International Conference on Machine Learning (ICML)"
doi: "arXiv:2404.01650"
ara_version: "1.0"
domain: "Test-Time Adaptation, Out-of-Distribution Generalization"
keywords:
  - test-time adaptation
  - forward-only optimization
  - CMA evolution strategy
  - prompt learning
  - activation shifting
  - quantized models
  - distribution shift
  - derivative-free optimization
  - edge deployment
  - vision transformer
claims_summary:
  - "FOA without backpropagation outperforms gradient-based TENT on full-precision 32-bit ViT on ImageNet-C (66.3% vs 59.6% accuracy)"
  - "FOA on 8-bit quantized ViT surpasses TENT on 32-bit ViT (63.5% vs 59.6%), with up to 24× memory reduction"
  - "Entropy-only CMA fitness is infeasible; activation discrepancy fitness enables stable CMA learning in unsupervised online TTA"
abstract: "Test-time adaptation has proven effective in adapting a given trained model to unseen test samples with potential distribution shifts. However, in real-world scenarios, models are usually deployed on resource-limited devices, e.g., FPGAs, and are often quantized and hard-coded with non-modifiable parameters for acceleration. In light of this, existing methods are often infeasible since they heavily depend on computation-intensive backpropagation for model updating that may be not supported. To address this, we propose a test-time Forward-Optimization Adaptation (FOA) method. In FOA, we seek to solely learn a newly added prompt (as model's input) via a derivative-free covariance matrix adaptation evolution strategy. To make this strategy work stably under our online unsupervised setting, we devise a novel fitness function by measuring test-training statistic discrepancy and model prediction entropy. Moreover, we design an activation shifting scheme that directly tunes the model activations for shifted test samples, making them align with the source training domain, thereby further enhancing adaptation performance. Without using any backpropagation and altering model weights, FOA runs on quantized 8-bit ViT outperforms gradient-based TENT on full-precision 32-bit ViT, while achieving an up to 24-fold memory reduction on ImageNet-C."
---

# Test-Time Model Adaptation with Only Forward Passes

## Overview

This paper introduces **Forward-Optimization Adaptation (FOA)**, a test-time adaptation method that operates entirely without backpropagation and without modifying model weights. This makes TTA feasible on resource-constrained and quantized edge devices (smartphones, FPGAs, 8-bit/6-bit models) where backpropagation is unsupported or prohibitively expensive.

FOA achieves adaptation through two complementary mechanisms: (1) **CMA-based prompt adaptation** inserts learnable input prompts optimized via the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) with a novel unsupervised fitness function combining prediction entropy and activation distribution discrepancy; (2) **Back-to-source activation shifting** directly adjusts the final-layer CLS token activations at inference time using exponential moving average statistics to align OOD features back to the source distribution. On ImageNet-C with ViT-Base, FOA (66.3% accuracy, 3.2% ECE) outperforms gradient-based SAR (62.7%, 7.0%) and TENT (59.6%, 18.5%), while using only 832 MB vs. 5,165 MB for TENT and 16,836 MB for CoTTA at batch size 64.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight motivating backpropagation-free TTA |
| [claims.md](logic/claims.md) | 7 falsifiable claims (C01–C07) |
| [concepts.md](logic/concepts.md) | 10 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 8 verification plans (E01–E08) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: CMA optimizer + prompt adapter + activation shifter |
| [solution/algorithm.md](logic/solution/algorithm.md) | FOA algorithm with CMA-ES, fitness function, activation shifting |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and known limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | 6 convergence tricks and design heuristics |
| [related_work.md](logic/related_work.md) | 12 typed dependency entries |

### Physical Layer (`/src`)

**Runnable Source Code** (`src/code/`) — the complete, unmodified repository from the paper authors. **Use this code for all reproduction tasks.** It includes the full evaluation pipeline, all TTA method implementations, data loaders, and experiment scripts.

| File | Description | Claims |
|------|-------------|--------|
| [code/README.md](src/code/README.md) | Project overview, setup instructions, and how to run experiments | — |
| [code/main.py](src/code/main.py) | **Main entry point**: evaluates any TTA method on any dataset (ImageNet-C/R/V2/Sketch) | C01–C07 |
| [code/main.sh](src/code/main.sh) | Example command-line invocation with all dataset paths | — |
| [code/tta_library/foa.py](src/code/tta_library/foa.py) | Core FOA implementation: CMA-ES prompt optimization + activation shifting + fitness evaluation | C01, C02, C03 |
| [code/tta_library/tent.py](src/code/tta_library/tent.py) | TENT baseline (BN affine entropy minimization) | C01 |
| [code/tta_library/sar.py](src/code/tta_library/sar.py) | SAR baseline (sharpness-aware entropy minimization) | C01 |
| [code/tta_library/cotta.py](src/code/tta_library/cotta.py) | CoTTA baseline (continuous TTA with augmentations) | C01 |
| [code/tta_library/t3a.py](src/code/tta_library/t3a.py) | T3A baseline (gradient-free, class prototypes) | C01 |
| [code/tta_library/lame.py](src/code/tta_library/lame.py) | LAME baseline (kNN logit correction, gradient-free) | C01 |
| [code/tta_library/foa_shift.py](src/code/tta_library/foa_shift.py) | FOA variant: activation shifting only (no prompt learning) | C05 |
| [code/tta_library/foa_bp.py](src/code/tta_library/foa_bp.py) | FOA variant: with backpropagation (for comparison) | C01 |
| [code/models/vpt.py](src/code/models/vpt.py) | PromptViT: Vision Transformer with learnable prompt injection | C01 |
| [code/dataset/selectedRotateImageFolder.py](src/code/dataset/selectedRotateImageFolder.py) | **Data loading**: `prepare_test_data()` for ImageNet-C (15 corruptions × 5 levels), R, V2, Sketch | — |
| [code/dataset/README.md](src/code/dataset/README.md) | Dataset download instructions (ImageNet-C from Zenodo, ImageNet-R, V2, Sketch) | — |
| [code/dataset/ImagenetV2.py](src/code/dataset/ImagenetV2.py) | ImageNet-V2 dataset loader (HuggingFace) | — |
| [code/dataset/ImageNetMask.py](src/code/dataset/ImageNetMask.py) | ImageNet-R 200-class subset mask | — |
| [code/calibration_library/metrics.py](src/code/calibration_library/metrics.py) | ECE (Expected Calibration Error) computation | C01 |
| [code/quant_library/](src/code/quant_library/) | PTQ4ViT quantization support (8-bit, 6-bit) | C02, C03 |
| [code/utils/cli_utils.py](src/code/utils/cli_utils.py) | Accuracy computation, progress meters | — |

**Reference Pseudocode** (`src/execution/`) — algorithm-level pseudocode for understanding the FOA method. For actual execution, use `src/code/` above.

| File | Description | Claims |
|------|-------------|--------|
| [execution/foa.py](src/execution/foa.py) | Pseudocode: FOA loop (CMA sampling, fitness, shifting) | C01, C02, C03 |
| [execution/fitness.py](src/execution/fitness.py) | Pseudocode: fitness function (Eq. 5) | C04, C05 |

**Configuration & Environment**

| File | Description |
|------|-------------|
| [configs/training.md](src/configs/training.md) | Batch size, population size, λ, α, γ, prompt count |
| [configs/model.md](src/configs/model.md) | ViT-Base, quantization config, prompt embedding config |
| [environment.md](src/environment.md) | Hardware, dependencies, seeds |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG covering key design decisions and dead ends |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 14 tables + 3 figures |
| [tables/table2_imagenetc_accuracy.md](evidence/tables/table2_imagenetc_accuracy.md) | Table 2: All-method accuracy on ImageNet-C (15 corruptions, severity 5) |
| [tables/table3_imagenet_rvs_accuracy.md](evidence/tables/table3_imagenet_rvs_accuracy.md) | Table 3: ImageNet-R/V2/Sketch accuracy and ECE |
| [tables/table4_quantized_accuracy.md](evidence/tables/table4_quantized_accuracy.md) | Table 4: 8-bit and 6-bit ViT accuracy on ImageNet-C |
| [tables/table5_ablation_components.md](evidence/tables/table5_ablation_components.md) | Table 5: Component ablation (entropy, act. discrepancy, act. shifting) |
| [tables/table6_foai_intervals.md](evidence/tables/table6_foai_intervals.md) | Table 6: FOA-I with different update intervals |
| [tables/table7_memory_usage.md](evidence/tables/table7_memory_usage.md) | Table 7: Run-time memory usage by method and batch size |
| [tables/table8_computation.md](evidence/tables/table8_computation.md) | Table 8: Computational complexity: FP/BP counts, time, memory |
| [tables/table9_design_choices.md](evidence/tables/table9_design_choices.md) | Table 9: Design choices — learnable params × optimizer × loss |
| [tables/table10_resnet_mamba.md](evidence/tables/table10_resnet_mamba.md) | Table 10: ResNet-50 and VisionMamba results |
| [tables/table11_noniid.md](evidence/tables/table11_noniid.md) | Table 11: Non-i.i.d. scenario performance (label/mixed shifts) |
| [tables/table12_indistribution.md](evidence/tables/table12_indistribution.md) | Table 12: In-distribution (clean ImageNet) accuracy and ECE |
| [tables/table13_lambda_sensitivity.md](evidence/tables/table13_lambda_sensitivity.md) | Table 13: Sensitivity to trade-off parameter λ |
| [tables/table16_ece_fullprecision.md](evidence/tables/table16_ece_fullprecision.md) | Table 16: Detailed ECE for full-precision ViT on ImageNet-C |
| [tables/table17_ece_quantized.md](evidence/tables/table17_ece_quantized.md) | Table 17: Detailed ECE for quantized ViT on ImageNet-C |
| [figures/fig2a_population_size.md](evidence/figures/fig2a_population_size.md) | Figure 2a: Accuracy/ECE vs. CMA population size K |
| [figures/fig2b_num_prompts.md](evidence/figures/fig2b_num_prompts.md) | Figure 2b: Accuracy/ECE vs. number of prompt embeddings Np |
| [figures/fig2c_num_id_samples.md](evidence/figures/fig2c_num_id_samples.md) | Figure 2c: Accuracy/ECE vs. number of source ID samples Q |
