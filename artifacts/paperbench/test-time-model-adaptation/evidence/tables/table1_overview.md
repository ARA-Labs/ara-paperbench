# Table 1: Overview Comparison — Prior TTA vs FOA
- **Source**: Table 1, Section 1 (Introduction)
- **Caption**: "Comparison w.r.t. prior gradient-based Test-Time Adaptation (TTA) vs. our Forward-Optimization Adaptation. The memory usage and accuracy are measured via ViT-Base and batch size 64 on ImageNet-C (level 5). The memory of 8-bit ViT is an ideal estimation by 0.25× memory of 32-bit ViT per Liu et al. (2021b)."

| Aspect | Prior TTA (Gradient-based) | FOA (full precision, 32-bit) | FOA (quantized, 8-bit) |
|--------|---------------------------|------------------------------|------------------------|
| Update model weights | Yes | No | No |
| Backward propagation | Required | Not required | Not required |
| Model compatibility | Full precision models (32-bit) | Full precision models (32-bit) | Quantized models: 8-bit, 6-bit, ... |
| Device compatibility | High-performance GPU | High-performance GPU | Low-power edge devices: smartphones, iPads, FPGAs, embodied robots, ... |
| Accuracy (ImageNet-C level 5) | 59.6% (TENT, full precision, 32-bit) | 66.3% | 63.5% |
| Run-time memory usage (MB) | 5,165 (TENT, full precision, 32-bit) | 832 | 208 (estimated: 0.25 × 832) |
