---
# Environment

## Python
- **Version**: Not specified in paper (standard deep learning Python ≥ 3.8 assumed)

## Framework
- **PyTorch**: Not specified in paper (standard PyTorch for ViT operations)
- **timm**: Used for loading pretrained ViT-Base weights (`https://github.com/pprp/timm`)

## Hardware
- **GPU**: Single NVIDIA RTX 3090 (used for wall-clock time and memory measurements in Table 8)
- **Memory benchmarking**: Conducted on RTX 3090 for processing 50,000 images of ImageNet-C
- **National Supercomputing Centre, Singapore**: Used for computational experiments (from Acknowledgments)

## Key Dependencies
- **pycma**: CMA-ES optimizer (`https://github.com/CMA-ES/pycma`) — version not specified
- **PTQ4ViT**: Post-training quantization for ViT (`https://github.com/hahnyuan/PTQ4ViT`) — version not specified
- **timm**: PyTorch Image Models for pretrained ViT weights — version not specified
- **LAME**: `https://github.com/fiveai/LAME`
- **T3A**: `https://github.com/matsuolab/T3A`
- **TENT**: `https://github.com/DequanWang/tent`
- **SAR**: `https://github.com/mr-eggplant/SAR`
- **CoTTA**: `https://github.com/qinenergy/cotta`
- **FOA code**: `https://github.com/mr-eggplant/FOA`

## Random Seeds
- Not specified in paper

## Model Weights
- **ViT-Base (full precision)**: From timm repository, trained on ImageNet-1K
  - URL: `https://storage.googleapis.com/vit_models/augreg/B_16-i21k-300ep-lr_0.001-aug_medium1-wd_0.1-do_0.0-sd_0.0--imagenet2012-steps_20k-lr_0.01-res_224.npz`
- **Quantized ViT-Base**: Produced via PTQ4ViT using 32 randomly selected ImageNet-1K training samples

## Datasets
- **ImageNet-1K**: Source training data and validation set (for source statistics); 1000 classes
- **ImageNet-C**: 50,000 images × 15 corruption types × 5 severity levels; evaluation at severity level 5
  - Corruption types: Gaussian noise, shot noise, impulse noise, defocus blur, glass blur, motion blur, zoom blur, snow, frost, fog, brightness, contrast, elastic transformation, pixelation, JPEG compression
- **ImageNet-R**: 30,000 images, 200 ImageNet classes (artistic renditions; from Flickr + MTurk)
- **ImageNet-V2**: 10,000 images (Matched Frequency subset), 1000 classes
- **ImageNet-Sketch**: 50,899 black-and-white sketch images, 1000 classes (~50 per class)
