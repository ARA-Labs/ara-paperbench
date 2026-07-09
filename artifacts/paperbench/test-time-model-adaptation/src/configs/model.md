---
# Model Configuration

## Base Architecture: ViT-Base
- **Value**: Vision Transformer Base (ViT-B/16) — patch size 16×16, embedding dimension d=768, 12 transformer layers (N=12), 12 attention heads, MLP hidden dim=3072, ~86M parameters
- **Rationale**: Standard large-scale vision model; hardware-friendly; widely used in TTA literature
- **Source**: timm repository; Dosovitskiy et al. (2021)
- **Weights URL**: `https://storage.googleapis.com/vit_models/augreg/B_16-i21k-300ep-lr_0.001-aug_medium1-wd_0.1-do_0.0-sd_0.0--imagenet2012-steps_20k-lr_0.01-res_224.npz`

## Prompt Configuration
- **Number of prompts (Np)**: 3
- **Prompt dimension (d)**: 768 (same as ViT-Base patch embedding dimension)
- **Prompt position**: Prepended to patch embeddings before the first transformer layer: [CLS, p_1, p_2, p_3, patch_1, ..., patch_m]
- **Initialization**: Uniform distribution
- **Optimization**: CMA-ES (not backpropagation)
- **Source**: Section 3.1; Section 4 (Implementation Details)

## Quantized Model Configurations

### 8-bit ViT-Base
- **Quantization method**: PTQ4ViT (post-training quantization)
- **Bit width**: 8-bit (weights and activations)
- **Calibration samples**: 32 randomly selected ImageNet-1K training samples
- **Memory**: Estimated as 0.25× of 32-bit model (Liu et al., 2021b)
- **Applicable TTA methods**: FOA (proposed), T3A, NoAdapt; gradient-based methods NOT applicable
- **Source**: Section 4 (Datasets and Models); Appendix B.2

### 6-bit ViT-Base
- **Quantization method**: PTQ4ViT
- **Bit width**: 6-bit (weights and activations)
- **Calibration samples**: 32 randomly selected ImageNet-1K training samples
- **Applicable TTA methods**: FOA (proposed), T3A, NoAdapt; gradient-based methods NOT applicable
- **Source**: Section 4 (Datasets and Models); Appendix B.2

## Alternative Model Architectures

### ResNet-50
- **Prompt mechanism**: Learnable 7×7 Conv layer applied to input image to generate prompt of same size; prompt added element-wise to image
- **Notes**: FOA shows limited gain on ResNet-50 (22.6%) compared to TENT (29.4%) — convolutions are local operators, making location-invariant prompts less effective
- **Source**: Section 4.4; Table 10

### VisionMamba
- **Prompt mechanism**: Learnable prompt embeddings concatenated with patch embeddings (same as ViT)
- **Notes**: FOA achieves comparable performance to TENT and SAR on VisionMamba (49.6% vs 49.2% TENT and 49.0% SAR on Gaussian noise level 5)
- **Source**: Section 4.4; Table 10; Zhu et al. (2024)

## CMA-ES Configuration
- **Library**: pycma (`https://github.com/CMA-ES/pycma`)
- **Initialization**: m^(0) = 0, Σ^(0) = I, τ^(0) = 1
- **Population size**: K = 28 = 4 + 3 × log(prompt_dim); prompt_dim = 768 × 3 = 2304
- **Source**: Algorithm 1; Section 4 (Implementation Details)

## Baseline Model Hyperparameters

### TENT
- **Optimizer**: SGD, momentum=0.9, lr=0.001
- **Trainable**: Affine parameters of all layer normalization layers (except Table 9 experiments)
- **Source**: `https://github.com/DequanWang/tent`; Appendix B.2

### SAR
- **Optimizer**: SGD, momentum=0.9, lr=0.001
- **Entropy threshold**: E0 = 0.4 × ln(C), C = number of classes
- **Trainable**: Affine parameters of layer normalization from blocks1 to blocks8 (ViT-Base)
- **Source**: `https://github.com/mr-eggplant/SAR`; Appendix B.2

### CoTTA
- **Optimizer**: SGD, momentum=0.9, lr=0.05
- **Augmentation threshold**: p_th = 0.1; 32 augmentations below threshold
- **Augmentations**: color jitter, random affine, Gaussian blur, random horizontal flip, Gaussian noise
- **Restoration probability**: 0.01; EMA factor α=0.999 for teacher update
- **Trainable**: All ViT-Base parameters
- **Source**: `https://github.com/qinenergy/cotta`; Appendix B.2

### LAME
- **kNN affinity**: k=5
- **Batch size**: 64
- **Source**: `https://github.com/fiveai/LAME`; Appendix B.2

### T3A
- **Number of supports M**: 20
- **Batch size**: 64
- **Source**: `https://github.com/matsuolab/T3A`; Appendix B.2
