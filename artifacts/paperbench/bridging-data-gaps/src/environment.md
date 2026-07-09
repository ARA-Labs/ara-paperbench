---
# Environment

## Python
- **Version**: Not specified in paper

## Framework
- **PyTorch version**: Not specified in paper
- **Base DPM framework**: DDPM (Ho et al. 2020 [9]) and LDM (Rombach et al. 2022 [23]); GAN baselines on StyleGAN2 [12] codebase

## Hardware
- **GPU type**: NVIDIA A100
- **GPU count**: 8 (×8 NVIDIA A100)
- **Memory per GPU**: Not specified in paper; DDPM-TAN uses 9 GB total (vs. 20 GB for direct fine-tuning baseline on 1 GPU)
- **Note**: Baseline (direct fine-tuning) uses batch size 5 on 1 GPU; DDPM-TAN uses batch size 40 on ×8 A100

## Key Dependencies
- DDPM pre-trained model (compatible with Ho et al. 2020 architecture)
- LDM pre-trained model (from Rombach et al. 2022)
- StyleGAN2 codebase for GAN baselines
- LPIPS metric implementation (Zhang et al. 2018 [32])
- FID metric implementation
- PyTorch (version not specified)
- torchvision (for ImageNet pre-trained classifier backbone)

## Random Seeds
- **Value**: Not specified in paper

## Source Datasets
- FFHQ (Flickr-Faces-HQ) — source domain for face-related tasks
- LSUN Church — source domain for building/scene-related tasks

## Target Datasets (10-shot)
- FFHQ-based: Babies (~2,700 images reference for FID), Sunglasses (~2,500 images reference for FID), Raphael's paintings, Amedeo Modigliani's paintings, Sketches
- LSUN Church-based: Haunted Houses, Landscape drawings
