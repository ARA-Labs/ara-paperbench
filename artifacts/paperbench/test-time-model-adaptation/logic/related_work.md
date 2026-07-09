---
# Related Work

## RW01: Wang et al., 2021 (TENT)
- **DOI**: arXiv:2006.10164
- **Type**: baseline
- **Delta**:
  - What changed: FOA replaces SGD-based entropy minimization with CMA-ES-based prompt optimization + activation discrepancy fitness
  - Why: TENT requires backpropagation (infeasible on quantized/edge devices) and suffers high ECE (18.5% vs. FOA 3.2%) due to noisy entropy signal under severe corruption
- **Claims affected**: C01, C04
- **Adopted elements**: Entropy term in fitness function (Eq. 5, first term)

## RW02: Hansen, 2016 (CMA-ES)
- **DOI**: arXiv:1604.00772
- **Type**: imports
- **Delta**:
  - What changed: FOA applies CMA-ES to unsupervised online TTA with low-dimensional prompt optimization and a custom fitness function
  - Why: CMA-ES is a robust derivative-free optimizer for non-convex black-box problems; conventional CMA uses supervised fitness on offline datasets
- **Claims affected**: C01, C02, C04, C05
- **Adopted elements**: CMA-ES algorithm for distribution parameter updates; population size formula K = 4 + 3 × log(dim); pycma library

## RW03: Niu et al., 2023 (SAR)
- **DOI**: ICLR 2023
- **Type**: baseline
- **Delta**:
  - What changed: FOA eliminates backpropagation entirely; SAR uses sharpness-aware optimizer with selective sample filtering
  - Why: SAR still requires backward passes and cannot run on quantized models
- **Claims affected**: C01, C07
- **Adopted elements**: Comparison benchmark; non-i.i.d. evaluation protocol

## RW04: Dosovitskiy et al., 2021 (ViT)
- **DOI**: ICLR 2021
- **Type**: imports
- **Delta**:
  - What changed: FOA uses ViT as the backbone model architecture; adds prompt tokens before first transformer layer
  - Why: ViT's global attention mechanism allows location-invariant prompt tokens to influence all patch representations
- **Claims affected**: C01, C02
- **Adopted elements**: ViT-Base architecture; CLS token mechanism; patch embedding structure

## RW05: Jia et al., 2022 (Visual Prompt Tuning)
- **DOI**: ECCV 2022
- **Type**: imports
- **Delta**:
  - What changed: FOA adapts prompt tuning concept from supervised fine-tuning to online unsupervised TTA; uses CMA-ES instead of backpropagation to optimize prompts
  - Why: Visual prompt tuning requires labeled data and backward passes; FOA needs neither
- **Claims affected**: C01, C05
- **Adopted elements**: Continuous input prompt embedding concept; prepending prompts to input sequence

## RW06: Hendrycks & Dietterich, 2019 (ImageNet-C)
- **DOI**: ICLR 2019
- **Type**: bounds
- **Delta**:
  - What changed: Provides the primary evaluation benchmark for FOA
  - Why: ImageNet-C with 15 corruption types and 5 severity levels is the standard for TTA evaluation
- **Claims affected**: C01, C02, C03, C04, C05, C06, C07
- **Adopted elements**: Benchmark dataset; corruption taxonomy; severity level 5 evaluation protocol

## RW07: Wang et al., 2022 (CoTTA)
- **DOI**: CVPR 2022
- **Type**: baseline
- **Delta**:
  - What changed: FOA replaces teacher-student with augmentation-consistency via CMA prompt optimization; eliminates backpropagation
  - Why: CoTTA requires up to 16,836 MB memory at BS=64; FOA uses only 832 MB
- **Claims affected**: C03
- **Adopted elements**: Comparison baseline

## RW08: Iwasawa & Matsuo, 2021 (T3A)
- **DOI**: NeurIPS 2021
- **Type**: baseline
- **Delta**:
  - What changed: FOA adds explicit model-feedback-based optimization (CMA with fitness); T3A only adjusts prototypes without forward-pass feedback
  - Why: T3A's limited learning capacity (56.9% accuracy) vs. FOA's 66.3% on ImageNet-C
- **Claims affected**: C01, C02
- **Adopted elements**: Gradient-free TTA category; quantized model applicability

## RW09: Boudiaf et al., 2022 (LAME)
- **DOI**: CVPR 2022
- **Type**: baseline
- **Delta**:
  - What changed: FOA learns prompts via CMA; LAME only adjusts output logits
  - Why: LAME performs worse than NoAdapt on ImageNet-C due to label-shift sensitivity
- **Claims affected**: C01
- **Adopted elements**: Gradient-free TTA baseline

## RW10: Yuan et al., 2022 (PTQ4ViT)
- **DOI**: ECCV 2022
- **Type**: imports
- **Delta**:
  - What changed: FOA uses PTQ4ViT for post-training quantization to obtain 8-bit and 6-bit ViT models
  - Why: PTQ4ViT is a state-of-the-art post-training quantization method for ViTs; uses twin uniform quantization
- **Claims affected**: C02, C03
- **Adopted elements**: Quantization tool; 8-bit and 6-bit ViT models; 32 training samples for calibration

## RW11: Malladi et al., 2023 (MeZO)
- **DOI**: NeurIPS 2023
- **Type**: imports
- **Delta**:
  - What changed: FOA uses CMA-ES rather than zeroth-order gradient estimation; FOA targets online unsupervised TTA rather than offline supervised fine-tuning
  - Why: Zeroth-order methods have slow convergence for large models; CMA-ES is more sample-efficient for prompt-sized optimization
- **Claims affected**: C04
- **Adopted elements**: Motivation for forward-only optimization of language/vision models

## RW12: Liu et al., 2021b (PTQ for ViT)
- **DOI**: NeurIPS 2021
- **Type**: imports
- **Delta**:
  - What changed: Provides the memory scaling factor (0.25×) used to estimate 8-bit ViT memory from 32-bit measurements
  - Why: 8-bit quantization reduces each parameter from 32-bit float to 8-bit integer, giving 4× reduction
- **Claims affected**: C02, C03
- **Adopted elements**: Memory estimation formula: Memory(8-bit) = 0.25 × Memory(32-bit)
