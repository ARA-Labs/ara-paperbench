# Environment

- **Python**: Not specified in paper (standard PyTorch environment assumed)
- **Framework**: PyTorch (version not specified)
- **Hardware**: NVIDIA GTX3090 GPUs
- **Key dependencies**:
  - PyTorch (version not specified)
  - VISSL library (Goyal et al. 2021) — used for ImageNet-1k experiments only
  - torchvision — for dataset loading (F-MNIST, SVHN, CIFAR-10, MNIST)
- **Random seeds**: Not specified in paper (experiments repeated 10 times for §5.2, 20 times for §5.1; mean ± std reported)
- **Repetitions**: 10 repetitions for main comparison experiments (§5.2); 20 repetitions for §5.1; 1 run for ImageNet-1k (§5.4) due to computational cost
- **Code availability**: Provided in supplementary material; to be made public after acceptance
- **Baseline implementations**: Reproduced from published code repositories:
  - EL2N/GraNd: https://github.com/mansheej/data_diet
  - Influential: https://shuoyang-1998.github.io/assets/code/code_datasetptuning.zip
  - Moderate: https://github.com/tmllab/Moderate-DS
  - CCS: https://github.com/haizhongzheng/Coverage-centric-coreset-selection
  - Probabilistic: https://github.com/x-zho14/Probabilistic-Bilevel-Coreset-Selection
