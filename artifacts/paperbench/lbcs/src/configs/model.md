# Model Configuration

## Proxy Network: LeNet (F-MNIST inner loop and evaluation)
- **Architecture**: Standard LeNet (LeCun et al. 1998)
- **Input**: 28×28 grayscale images
- **Use**: Both proxy (coreset selection) and evaluation (post-selection training) for F-MNIST
- **Source**: §5.2 ("we employ a LeNet for F-MNIST")

## Proxy Network: CNN for SVHN (inner loop / coreset selection)
- **Architecture** (from Appendix Table 5, left column):
  ```
  32×32 RGB Images
  3×3 Conv2d + ReLU
  3×3 Conv2d + ReLU
  2×2 Max-pool
  Dense 8192→1024 + ReLU
  Dense 1024→256 + ReLU
  Dense 256→10
  ```
- **Use**: Inner loop proxy for SVHN coreset selection
- **Source**: Appendix D.2 (Table 5, left column)

## Evaluation Network: CNN for SVHN (trained on coreset)
- **Architecture** (from Appendix Table 5, center column):
  ```
  32×32 RGB Images
  3×3 Conv2d + ReLU
  3×3 Conv2d + ReLU
  2×2 Max-pool
  3×3 Conv2d + ReLU
  3×3 Conv2d + ReLU
  2×2 Max-pool
  Dense 2048→1024 + ReLU
  Dense 1024→512 + ReLU
  Dense 512→10
  ```
- **Use**: Evaluation after coreset selection for SVHN
- **Source**: Appendix D.2 (Table 5, center column)

## Proxy Network: CNN for CIFAR-10 (inner loop / coreset selection)
- **Architecture** (from Appendix Table 5, right column):
  ```
  32×32 RGB Images
  5×5 Conv2d + ReLU
  2×2 Max-pool
  3×3 Conv2d + ReLU
  2×2 Max-pool
  3×3 Conv2d + ReLU
  3×3 Conv2d + ReLU
  2×2 Max-pool
  Dense 512→64
  Dense 64→10
  ```
- **Use**: Inner loop proxy for CIFAR-10 coreset selection
- **Source**: Appendix D.2 (Table 5, right column)

## Evaluation Network: ResNet-18 (CIFAR-10 post-selection)
- **Architecture**: Standard ResNet-18
- **Use**: Trained on selected CIFAR-10 coreset; evaluated on CIFAR-10 test set
- **Source**: §5.2 ("a ResNet-18 network for CIFAR-10")

## Proxy + Evaluation Network: ResNet-50 (ImageNet-1k)
- **Architecture**: Standard ResNet-50
- **Use**: Both inner-loop proxy and post-selection evaluation for ImageNet-1k
- **Library**: VISSL (Goyal et al. 2021)
- **Source**: §5.4 ("The network structures for the inner loop and training on the coreset after coreset selection are ResNet-50")

## Proxy + Evaluation: 2-Block CNN (MNIST-S, §5.1 and Appendix C.3)
- **Architecture**: Two blocks of {Conv2d → Dropout → MaxPool → ReLU}
- **Use**: Both proxy and evaluation for MNIST-S experiments (§5.1) and Figure 1 experiments (Appendix C.3)
- **Source**: §5.1 ("a convolutional neural network stacked with two blocks of convolution, dropout, max-pooling, and ReLU activation")

## Cross-Architecture Evaluation: ViT-small (SVHN, Appendix E.5)
- **Architecture**: ViT-small (Dosovitskiy et al. 2021)
- **Use**: Post-selection evaluation on SVHN (coreset selected by CNN proxy)
- **Source**: Appendix E.5

## Cross-Architecture Evaluation: WideResNet/W-NET (SVHN, Appendix E.5)
- **Architecture**: WideResNet (Zagoruyko & Komodakis 2016)
- **Use**: Post-selection evaluation on SVHN (coreset selected by CNN proxy)
- **Source**: Appendix E.5
