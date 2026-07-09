# Table 5: Network Structures
- **Source**: Table 5, Appendix D.2
- **Caption**: "The network structures of the models used in our experiments."
- **Experimental conditions**: Architectures used for inner-loop proxy models and final evaluation models.

| Layer | CNN for SVHN (inner loop) | CNN for SVHN (trained on coresets) | CNN for CIFAR-10 (inner loop) |
|-------|--------------------------|-----------------------------------|-------------------------------|
| Input | 32×32 RGB Images | 32×32 RGB Images | 32×32 RGB Images |
| 1 | 3×3 Conv2d, ReLU | 3×3 Conv2d, ReLU | 5×5 Conv2d, ReLU |
| 2 | 3×3 Conv2d, ReLU | 3×3 Conv2d, ReLU | 2×2 Max-pool |
| 3 | 2×2 Max-pool | 2×2 Max-pool | 3×3 Conv2d, ReLU |
| 4 | 3×3 Conv2d, ReLU | 3×3 Conv2d, ReLU | 2×2 Max-pool |
| 5 | 3×3 Conv2d, ReLU | 2×2 Max-pool | Dense 512→64, ReLU |
| 6 | 2×2 Max-pool | Dense 8192→1024, ReLU | Dense 64→10 |
| 7 | 3×3 Conv2d, ReLU | Dense 1024→256, ReLU | — |
| 8 | 3×3 Conv2d, ReLU | Dense 256→10 | — |
| 9 | 2×2 Max-pool | — | — |
| 10 | Dense 2048→1024, ReLU | — | — |
| 11 | Dense 1024→512, ReLU | — | — |
| 12 | Dense 512→10 | — | — |

**Notes**:
- LeNet architecture (LeCun et al., 1998) is used for F-MNIST for both inner loop and final training but is not detailed in Table 5 (standard architecture).
- ResNet-18 is used for CIFAR-10 final training (standard architecture, not in this table).
- ResNet-50 is used for ImageNet-1k (both inner loop and final training, standard architecture).
