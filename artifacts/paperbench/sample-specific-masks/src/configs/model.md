# Model Configuration

## Pre-trained Backbone: ResNet-18
- **Value**: ResNet-18 pre-trained on ImageNet-1K (torchvision standard weights)
- **Input size**: 224×224×3
- **Output classes**: 1000 (ImageNet-1K)
- **Parameters**: ~11.2M (frozen during VR training)
- **Rationale**: Standard benchmark backbone following Chen et al. (2023)
- **Source**: Section 5

## Pre-trained Backbone: ResNet-50
- **Value**: ResNet-50 pre-trained on ImageNet-1K (torchvision standard weights)
- **Input size**: 224×224×3
- **Output classes**: 1000 (ImageNet-1K)
- **Parameters**: ~25.6M (frozen during VR training)
- **Rationale**: Larger backbone to test scalability of SMM
- **Source**: Section 5

## Pre-trained Backbone: ViT-B32
- **Value**: ViT-B/32 pre-trained on ImageNet-1K
- **Input size**: 384×384×3
- **Output classes**: 1000 (ImageNet-1K)
- **Parameters**: ~88.2M (frozen during VR training)
- **Rationale**: Tests applicability of SMM to transformer-based architectures
- **Source**: Section 5

## Mask Generator: 5-layer CNN (for ResNet-18/50)
- **Layer 1**: Conv2d(in=3, out=8, kernel=3, padding=1, stride=1) → BatchNorm2d(8) → ReLU → MaxPool2d(kernel=2, stride=2)
- **Layer 2**: Conv2d(in=8, out=16, kernel=3, padding=1, stride=1) → BatchNorm2d(16) → ReLU → MaxPool2d(kernel=2, stride=2)
- **Layer 3**: Conv2d(in=16, out=32, kernel=3, padding=1, stride=1) → BatchNorm2d(32) → ReLU → MaxPool2d(kernel=2, stride=2)
- **Layer 4**: Conv2d(in=32, out=64, kernel=3, padding=1, stride=1) → BatchNorm2d(64) → ReLU
- **Layer 5**: Conv2d(in=64, out=3, kernel=3, padding=1, stride=1)
- **Number of MaxPool layers**: l=3
- **Output size**: 28×28×3 (for 224×224 input)
- **Total parameters**: 26,499
- **Ratio to reprogramming parameters**: 17.60%
- **Ratio to ResNet-18 parameters**: 0.23%
- **Ratio to ResNet-50 parameters**: 0.10%
- **Source**: Section 3.2, Appendix A.2, Table 4

## Mask Generator: 6-layer CNN (for ViT-B32)
- **Layer 1**: Conv2d(in=3, out=8, kernel=3, padding=1, stride=1) → BatchNorm2d(8) → ReLU → MaxPool2d(kernel=2, stride=2)
- **Layer 2**: Conv2d(in=8, out=16, kernel=3, padding=1, stride=1) → BatchNorm2d(16) → ReLU → MaxPool2d(kernel=2, stride=2)
- **Layer 3**: Conv2d(in=16, out=32, kernel=3, padding=1, stride=1) → BatchNorm2d(32) → ReLU → MaxPool2d(kernel=2, stride=2)
- **Layer 4**: Conv2d(in=32, out=64, kernel=3, padding=1, stride=1) → BatchNorm2d(64) → ReLU
- **Layer 5**: Conv2d(in=64, out=128, kernel=3, padding=1, stride=1) → BatchNorm2d(128) → ReLU
- **Layer 6**: Conv2d(in=128, out=3, kernel=3, padding=1, stride=1)
- **Number of MaxPool layers**: l=3
- **Output size**: 48×48×3 (for 384×384 input)
- **Total parameters**: 102,339
- **Ratio to reprogramming parameters**: 23.13%
- **Ratio to ViT-B32 parameters**: 0.12%
- **Source**: Section 3.2, Appendix A.2, Table 4

## Patch-wise Interpolation
- **Default patch size**: 8 (= 2^l with l=3)
- **Tested patch sizes**: {1, 2, 4, 8, 16} (= 2^0 through 2^4)
- **Operation**: Nearest-neighbor upsampling via direct pixel copying; no learnable parameters
- **Source**: Section 3.3, Section 5 "Impact of Patch Size", Figure 4

## Shared Learnable Pattern δ
- **Shape (ResNet)**: 224×224×3 = 150,528 parameters
- **Shape (ViT)**: 384×384×3 = 442,368 parameters
- **Initialization**: All zeros
- **Source**: Section 3.4, Algorithm 1
