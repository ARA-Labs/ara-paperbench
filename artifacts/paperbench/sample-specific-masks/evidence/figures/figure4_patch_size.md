# Figure 4: Impact of Patch Size on SMM Accuracy
- **Source**: Figure 4, Section 5
- **Caption**: "Comparative results of different patch sizes (2^l). ResNet-18 is used as the pre-trained model as an example."
- **Axis labels**: X-axis: Patch Size of the Mask (values: 1, 2 shown; full range tested: {2^0, 2^1, 2^2, 2^3, 2^4} = {1, 2, 4, 8, 16}); Y-axis: Accuracy
- **Experimental conditions**: ResNet-18 pretrained on ImageNet-1K; SMM with varying number of MaxPool layers l ∈ {0,1,2,3,4} giving patch sizes {1,2,4,8,16}; 4 datasets shown; also compared against Narrow, Medium, Full watermarking baselines

## Data Points (Read from Figure 4 — approximate values from line plots)

### EuroSAT
| Method | Patch 1 | Patch 2 | Patch 4 | Patch 8 (default) | Patch 16 |
|--------|---------|---------|---------|-----------|----------|
| Watermarking (Narrow) | ≈0.828 | ≈0.828 | ≈0.828 | ≈0.828 | ≈0.828 |
| Watermarking (Medium) | ≈0.838 | ≈0.838 | ≈0.838 | ≈0.838 | ≈0.838 |
| Watermarking (Full) | ≈0.843 | ≈0.843 | ≈0.843 | ≈0.843 | ≈0.843 |
| Ours (SMM) | ≈0.89 | ≈0.91 | ≈0.92 | ≈0.922 | ≈0.91 |

### Flowers102
| Method | Patch 1 | Patch 2 | Patch 4 | Patch 8 (default) | Patch 16 |
|--------|---------|---------|---------|-----------|----------|
| Watermarking (Narrow) | ≈0.221 | ≈0.221 | ≈0.221 | ≈0.221 | ≈0.221 |
| Watermarking (Medium) | ≈0.226 | ≈0.226 | ≈0.226 | ≈0.226 | ≈0.226 |
| Watermarking (Full) | ≈0.232 | ≈0.232 | ≈0.232 | ≈0.232 | ≈0.232 |
| Ours (SMM) | ≈0.25 | ≈0.30 | ≈0.35 | ≈0.387 | ≈0.38 |

### CIFAR100
| Method | Patch 1 | Patch 2 | Patch 4 | Patch 8 (default) | Patch 16 |
|--------|---------|---------|---------|-----------|----------|
| Watermarking (Narrow) | ≈0.369 | ≈0.369 | ≈0.369 | ≈0.369 | ≈0.369 |
| Watermarking (Medium) | ≈0.349 | ≈0.349 | ≈0.349 | ≈0.349 | ≈0.349 |
| Watermarking (Full) | ≈0.338 | ≈0.338 | ≈0.338 | ≈0.338 | ≈0.338 |
| Ours (SMM) | ≈0.36 | ≈0.375 | ≈0.38 | ≈0.394 | ≈0.39 |

### SVHN
| Method | Patch 1 | Patch 2 | Patch 4 | Patch 8 (default) | Patch 16 |
|--------|---------|---------|---------|-----------|----------|
| Watermarking (Narrow) | ≈0.585 | ≈0.585 | ≈0.585 | ≈0.585 | ≈0.585 |
| Watermarking (Medium) | ≈0.711 | ≈0.711 | ≈0.711 | ≈0.711 | ≈0.711 |
| Watermarking (Full) | ≈0.783 | ≈0.783 | ≈0.783 | ≈0.783 | ≈0.783 |
| Ours (SMM) | ≈0.65 | ≈0.75 | ≈0.80 | ≈0.844 | ≈0.83 |

**Note**: Baseline (Narrow/Medium/Full) values are constant horizontal lines as they are independent of patch size. SMM values at patch_size=8 match Table 1 exactly. Intermediate values (patch=2,4,16) are approximate readings from the line plot.
