---
# Related Work

## RW01: Ho et al., 2020 (DDPM)
- **DOI**: NeurIPS 2020
- **Type**: imports
- **Delta**:
  - What changed: TAN adds adaptor modules + adversarial noise + similarity guidance on top of DDPM
  - Why: Enable few-shot transfer without modifying base diffusion training objective fundamentally
- **Claims affected**: C01, C02, C03, C04
- **Adopted elements**: DDPM forward/reverse process formulation (Eq. 1, 3); U-Net architecture; DDPM training loss; variance schedule

## RW02: Song et al., 2020 (DDIM)
- **DOI**: arXiv:2010.02502
- **Type**: imports
- **Delta**:
  - What changed: TAN builds on DDPM training but benefits from DDIM-style faster inference
  - Why: DDIM provides faster sampling at test time
- **Claims affected**: C03
- **Adopted elements**: Reverse process formulation with σt parameter; η parameter variants

## RW03: Dhariwal & Nichol, 2021 (Classifier Guidance)
- **DOI**: NeurIPS 2021
- **Type**: imports
- **Delta**:
  - What changed: TAN uses classifier gradient for domain transfer guidance rather than class-conditional generation
  - Why: Classifier gradients on noised images provide a principled way to estimate domain gap
- **Claims affected**: C01, C04
- **Adopted elements**: Conditional reverse process formulation (Eq. 2, 15 in TAN appendix); use of ∇xt log pϕ(y|xt) as guidance signal

## RW04: Rombach et al., 2022 (LDM)
- **DOI**: CVPR 2022
- **Type**: imports
- **Delta**:
  - What changed: TAN extends its adaptor-based fine-tuning to LDMs (LDM-TAN), freezing the autoencoder
  - Why: LDMs enable higher-resolution and higher-quality generation; extending TAN to LDMs improves results
- **Claims affected**: C01, C02
- **Adopted elements**: Pre-trained LDM model weights; LDM architecture (U-Net in latent space + autoencoder)

## RW05: Zhu et al., 2022 (DDPM-PA)
- **DOI**: arXiv:2211.03264
- **Type**: baseline
- **Delta**:
  - What changed: TAN avoids comparing noisy intermediate images with target images; uses classifier gradient instead
  - Why: Blurry predicted images are inaccurate domain proxies leading to fuzzy/distorted outputs
- **Claims affected**: C01, C02, C04
- **Adopted elements**: Overall few-shot DPM transfer learning framework; experimental settings (10-shot, same source/target datasets)

## RW06: Ojha et al., 2021 (CDC)
- **DOI**: CVPR 2021
- **Type**: baseline
- **Delta**:
  - What changed: TAN works with DPMs instead of GANs; uses noised images for domain comparison instead of final clean images
  - Why: CDC requires final generated images for cross-domain consistency loss, incompatible with DPM training
- **Claims affected**: C01, C02
- **Adopted elements**: Experimental protocol (FFHQ/LSUN Church source, same target datasets); Intra-LPIPS metric definition

## RW07: Zhao et al., 2022 (DCL)
- **DOI**: CVPR 2022
- **Type**: baseline
- **Delta**:
  - What changed: TAN uses similarity guidance via classifier gradients rather than contrastive learning between source/target image pairs
  - Why: DCL also requires final generated images; contrastive loss needs clean image pairs
- **Claims affected**: C01, C02
- **Adopted elements**: Comparison benchmark; evaluation datasets

## RW08: Houlsby et al., 2019 (Adaptor for NLP)
- **DOI**: ICML 2019
- **Type**: imports
- **Delta**:
  - What changed: TAN applies adaptor bottleneck architecture to U-Net layers in DPMs instead of Transformer blocks in NLP
  - Why: Enables parameter-efficient fine-tuning; only 1.3–1.6% of parameters trained
- **Claims affected**: C03
- **Adopted elements**: Adaptor bottleneck design: Wdown → nonlinear → Wup; parallel residual connection to frozen model

## RW09: Karras et al., 2020 (StyleGAN2)
- **DOI**: CVPR 2020
- **Type**: baseline
- **Delta**:
  - What changed: All GAN baselines (TGAN, TGAN+ADA, EWC, CDC, DCL) run on StyleGAN2 codebase; TAN uses DDPM/LDM
  - Why: Provides fair comparison baseline for all GAN-based transfer methods
- **Claims affected**: C01, C02
- **Adopted elements**: Codebase for all GAN baselines; FFHQ dataset (source domain)

## RW10: Wang et al., 2018 (TGAN)
- **DOI**: ECCV 2018
- **Type**: baseline
- **Delta**:
  - What changed: TAN uses DPM framework instead of GAN; achieves better diversity with fewer parameters
  - Why: TGAN full fine-tuning (100% parameters) overfits in few-shot regime
- **Claims affected**: C01, C02, C03
- **Adopted elements**: Transfer learning pipeline concept (source → target fine-tuning)

## RW11: Karras et al., 2020 (TGAN+ADA)
- **DOI**: NeurIPS 2020
- **Type**: baseline
- **Delta**:
  - What changed: TAN uses adversarial noise selection rather than augmentation to prevent overfitting
  - Why: Data augmentation (ADA) applied to GANs; TAN's approach is specific to diffusion model noise mechanism
- **Claims affected**: C01, C02, C03
- **Adopted elements**: Baseline results; experimental comparison

## RW12: Liu et al., 2023 (Semantic Diffusion Guidance)
- **DOI**: WACV 2023
- **Type**: imports
- **Delta**:
  - What changed: TAN derives the KL divergence domain distance formula inspired by this work's approach to semantic guidance
  - Why: Provides theoretical framework for using classifier gradients to guide diffusion models
- **Claims affected**: C04
- **Adopted elements**: Inspiration for using classifier gradient as domain gap measure; conditional guidance formulation
