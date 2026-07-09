---
title: "Efficient Transfer Learning in Diffusion Models via Adversarial Noise"
authors: ["Xiyu Wang", "Baijiong Lin", "Daochang Liu", "Chang Xu"]
year: 2023
venue: "arXiv preprint"
doi: "arXiv:2308.11948v1"
ara_version: "1.0"
domain: "Generative Models / Few-Shot Image Generation"
keywords: ["diffusion probabilistic models", "transfer learning", "adversarial noise", "few-shot image generation", "adaptor module", "similarity-guided training", "DDPM", "LDM", "domain adaptation", "min-max optimization"]
claims_summary:
  - "TAN (DDPM-TAN and LDM-TAN) surpasses GAN-based and DDPM-based baselines on Intra-LPIPS diversity across most 10-shot adaptation tasks"
  - "TAN achieves significantly lower FID than all baselines on FFHQ→Sunglasses (20.06 vs 34.75 prior best)"
  - "TAN is highly parameter-efficient (1.3%/1.6% of parameters) and converges in ~300 iterations vs ~5000 for prior methods"
  - "Adversarial noise selection corrects noisy gradients in few-shot settings, improving convergence and coverage of target distribution"
abstract: "Diffusion Probabilistic Models (DPMs) have demonstrated substantial promise in image generation tasks but heavily rely on the availability of large amounts of training data. Previous works, like GANs, have tackled the limited data problem by transferring pre-trained models learned with sufficient data. However, those methods are hard to be utilized in DPMs since the distinct differences between DPM-based and GAN-based methods, showing in the unique iterative denoising process integral and the need for many timesteps with no-targeted noise in DPMs. In this paper, we propose a novel DPMs-based transfer learning method, TAN, to address the limited data problem. It includes two strategies: similarity-guided training, which boosts transfer with a classifier, and adversarial noise selection which adaptive chooses targeted noise based on the input image. Extensive experiments in the context of few-shot image generation tasks demonstrate that our method is not only efficient but also excels in terms of image quality and diversity when compared to existing GAN-based and DDPM-based methods."
---

# Efficient Transfer Learning in Diffusion Models via Adversarial Noise

## Overview

This paper introduces **TAN** (Transfer via Adversarial Noise), a parameter-efficient few-shot transfer learning method for Diffusion Probabilistic Models (DPMs). GAN-based transfer methods cannot be directly applied to DPMs due to the iterative denoising process: DPMs cannot produce clean images during training, only blurry intermediate predictions. TAN addresses two fundamental challenges — (1) estimating transfer direction without clean generated images, and (2) the non-targeted Gaussian noise causing unbalanced transfer rates across samples — through two components: **similarity-guided training** (using a binary classifier to measure source/target domain divergence via noised images) and **adversarial noise selection** (PGD-based min-max optimization to identify and minimize worst-case Gaussian noise). Transfer is performed via lightweight adaptor layers (only 1.3%/1.6% of parameters updated), converging in ~300 iterations versus ~5000 for prior methods, with 3 GPU hours and 9 GB memory versus 7.5 GPU hours and 20 GB.

TAN achieves state-of-the-art results on 10-shot image generation benchmarks (FFHQ and LSUN Church source domains), outperforming GAN-based methods (TGAN, TGAN+ADA, EWC, CDC, DCL) and the prior DPM-based method (DDPM-PA) on both Intra-LPIPS diversity and FID quality metrics. On FFHQ→Sunglasses, TAN achieves FID of 20.06 vs 34.75 for DDPM-PA.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight: why DPM transfer is hard and what enables TAN |
| [claims.md](logic/claims.md) | 4 falsifiable claims (C01–C04) covering quality, diversity, efficiency, gradient correction |
| [concepts.md](logic/concepts.md) | 12 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 5 verification plans (E01–E05) covering main claims |
| [solution/architecture.md](logic/solution/architecture.md) | System design: pre-trained U-Net + adaptor layers + binary classifier + PGD adversarial noise |
| [solution/algorithm.md](logic/solution/algorithm.md) | TAN training algorithm (Algorithm 1), PGD inner loop, complexity |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions: 10-shot regime, DPM-specific constraints |
| [solution/heuristics.md](logic/solution/heuristics.md) | 5 convergence tricks (γ, ω, J, adaptor init, iteration count) |
| [related_work.md](logic/related_work.md) | 12 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/tan_core.py](src/execution/tan_core.py) | Adaptor module + TAN training step + adversarial noise PGD + similarity-guided loss | C01, C02, C03, C04 |
| [configs/training.md](src/configs/training.md) | Learning rate, iterations, batch size, γ, J, ω | — |
| [configs/model.md](src/configs/model.md) | Adaptor bottleneck dimensions, c/d values for DDPM vs LDM | — |
| [environment.md](src/environment.md) | Hardware: 8× NVIDIA A100; PyTorch; key deps | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG covering motivation, dead ends, and design decisions |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 6 tables + 4 figures |
| [tables/table1_intra_lpips.md](evidence/tables/table1_intra_lpips.md) | Main Intra-LPIPS results across 5 adaptation tasks, 8 methods |
| [tables/table2_fid.md](evidence/tables/table2_fid.md) | FID results on FFHQ→Babies and Sunglasses |
| [tables/table3_appendix_lpips.md](evidence/tables/table3_appendix_lpips.md) | Additional Intra-LPIPS on Sketches and Amedeo's paintings |
| [tables/table4_gamma_sensitivity.md](evidence/tables/table4_gamma_sensitivity.md) | FID and Intra-LPIPS vs. γ hyperparameter |
| [tables/table5_omega_sensitivity.md](evidence/tables/table5_omega_sensitivity.md) | FID and Intra-LPIPS vs. ω hyperparameter |
| [tables/table6_iteration_sensitivity.md](evidence/tables/table6_iteration_sensitivity.md) | FID and Intra-LPIPS vs. training iterations |
| [figures/figure1_lpips_transfer.md](evidence/figures/figure1_lpips_transfer.md) | LPIPS distances during fine-tuning showing overfitting vs underfitting divergence |
| [figures/figure4_ablation.md](evidence/figures/figure4_ablation.md) | Ablation study FID scores for 4 model variants |
