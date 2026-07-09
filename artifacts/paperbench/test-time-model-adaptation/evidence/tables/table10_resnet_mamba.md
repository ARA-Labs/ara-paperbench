---
# Table 10: FOA on ResNet-50 and VisionMamba
- **Source**: Table 10, Section 4.4
- **Caption**: "Effectiveness of FOA on ResNet and VisionMamba (Zhu et al., 2024). Results obtained on ImageNet-C (Gaussian noise, level 5). FOA† is modified from FOA by replacing CMA optimizer with SGD and updating the affine parameters of norm layers."
- **Conditions**: ImageNet-C, Gaussian noise, severity level 5; batch size 64

| Method | Need BP? | ResNet-50 Acc. (%) | ResNet-50 ECE (%) | VisionMamba Acc. (%) | VisionMamba ECE (%) |
|--------|----------|-------------------|-------------------|----------------------|---------------------|
| NoAdapt | ✗ | 3.0 | 19.7 | 40.9 | 3.8 |
| BN Adapt | ✗ | 16.0 | 1.3 | n/a | n/a |
| TENT | ✓ | 29.4 | 11.4 | 49.2 | 12.1 |
| SAR | ✓ | 30.7 | 3.4 | 49.0 | 11.4 |
| FOA (ours) | ✗ | 22.6 | 1.7 | 49.6 | 4.3 |
| FOA† | ✗* | 33.6 | 12.8 | 56.5 | 13.6 |

**Notes**:
- FOA† replaces CMA optimizer with SGD and updates affine parameters of norm layers (still effectively uses backpropagation for SGD)
- BN Adapt: not applicable (n/a) for VisionMamba as it uses layer normalization, not batch normalization
- FOA underperforms TENT on ResNet-50 (22.6% vs 29.4%) due to CNN locality limitation; input prompts less effective for convolutional architectures
- FOA achieves comparable performance to TENT and SAR on VisionMamba (49.6% vs 49.2% and 49.0%)
- FOA outperforms BN Adapt on ResNet-50 (22.6% vs 16.0% accuracy)
- ResNet-50 prompt: learnable 7×7 Conv layer generating prompt added to input image
