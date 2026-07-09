# Environment

- **Python**: Not specified in paper
- **Framework**: PyTorch (implied by torchvision models and GPU training; exact version not specified)
- **Hardware**: Single NVIDIA A100 GPU (Section 5: "Experiments are run with three seeds on a single A100 GPU")
- **Key dependencies**:
  - torchvision (for ResNet-18, ResNet-50 pre-trained weights; standard datasets CIFAR10, CIFAR100, SVHN, GTSRB)
  - PIL/pillow (image resizing)
  - numpy (array operations)
  - sklearn (t-SNE visualization for Figure 6)
  - Standard PyTorch dependencies (torch, torchvision)
  - Exact versions: Not specified in paper
- **Random seeds**: 3 seeds used per experiment; exact seed values not specified in paper
- **Dataset splits**: Following Chen et al. (2023); detailed split information in Appendix C / Table 6
- **Code repository**: https://github.com/tmlr-group/SMM
- **Dataset image sizes**:
  - CIFAR10, CIFAR100, SVHN, GTSRB: 32×32 (original)
  - Flowers102, DTD, UCF101, Food101, SUN397, EuroSAT, OxfordPets: 128×128 (as used)
  - All resized to 224×224 (ResNet) or 384×384 (ViT) during training
