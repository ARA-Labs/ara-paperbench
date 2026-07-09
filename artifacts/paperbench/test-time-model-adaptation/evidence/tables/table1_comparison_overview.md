---
# Table 1: Comparison Overview — Prior TTA vs. FOA

**Source**: Table 1, §1 Introduction
**Claims**: C01, C02
**Description**: High-level comparison of prior gradient-based TTA (TENT) vs Forward-Optimization Adaptation on ViT-Base, BS=64, ImageNet-C level 5.

| Property | Prior TTA (TENT) | FOA — Full Precision (32-bit) | FOA — Quantized (8-bit) |
|---|---|---|---|
| Update model weights | Yes | No | No |
| Backward propagation | Yes | No | No |
| Model compatibility | Full precision (32-bit) | Full precision (32-bit) | Quantized: 8-bit, 6-bit, ... |
| Device compatibility | High-performance GPU | High-performance GPU | Low-power edge devices: smartphones, iPads, FPGAs, embodied robots |
| Accuracy | 59.6% | 66.3% | 63.5% |
| Run-time memory usage | 5,165 MB | 832 MB | 208 MB |

Notes:
- Memory for 8-bit ViT is an ideal estimation by 0.25× memory of 32-bit ViT per Liu et al. (2021b)
- Memory ratio: 5,165 / 208 ≈ 24.8× (cited as "up to 24-fold" in paper)
- Model: ViT-Base, BS=64, ImageNet-C severity level 5
