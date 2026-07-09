# Environment

## Python
- **Version**: Not specified in paper. Use Python ≥ 3.8 (standard for PyTorch projects circa 2024).

## Framework
- **PyTorch**: Not specified. Use PyTorch ≥ 1.12.0 (standard for ViT/timm experiments in 2024).

## Hardware
- **GPU**: Single NVIDIA GeForce RTX 3090 (24 GB VRAM)
- **Count**: 1 GPU (all experiments in paper)
- **Parallelism note**: Adapter and RD training can be parallelised across multiple GPUs in principle; paper reports single-GPU sequential training in Table 8.

## Key Dependencies
- `timm` — ViT model loading and pre-trained weights
- `torch` — core deep learning framework
- `torchvision` — dataset loading (CIFAR-100)
- `numpy` — numerical utilities
- `scipy` — statistics utilities for z-score
- `Pillow` — image loading

## Baseline Implementations
- **SimpleCIL / ADAM**: https://github.com/zhoudw-zdw/RevisitingCIL
- **L2P, DualPrompt, CODA-P**: https://github.com/sun-hailong/LAMDA-PILOT (PILOT toolbox)
- **InfLoRA**: https://github.com/liangyanshuo/InfLoRA
- **SEMA (official)**: https://github.com/huiyiwang01/SEMA-CL
- **Convpass**: https://github.com/JieShibo/PETL-ViT/blob/main/convpass/vtab/convpass.py
- **AdaptFormer (functional adapter)**: https://github.com/ShoufaChen/AdaptFormer/blob/main/models/adapter.py

## Random Seeds
- **Seeds**: 5 independent runs with different seeds reported in Table 13 (mean ± std).
- **Data shuffling**: Same class order as Zhou et al. [90] (RevisitingCIL) used for all methods.
- **Specific seed values**: Not specified in paper.
