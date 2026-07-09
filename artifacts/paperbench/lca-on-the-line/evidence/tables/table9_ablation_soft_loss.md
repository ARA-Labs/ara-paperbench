---
# Table 9: Ablation Study on Soft Loss Labels for Linear Probing
- **Source**: Table 9, Appendix E.3
- **Caption**: "Ablation Study on Soft Loss Labels for Linear Probing from Section 4.3.2. CE-only: model trained with Cross-Entropy (CE) loss only; Soft Loss: soft label loss generated from hierarchy; Interpolation: linear interpolation in weight space; No ID Accuracy Drop: models that do not introduce accuracy drop on ImageNet; Pro-OOD: models that prefer improvement of OOD generalization even at cost of slight ID accuracy drop."
- **Conditions**: Hierarchy Source = WordNet; lambda=0.03, T=25, CE soft loss mode

| Model | Setting | ImgNet | ImgNet-V2 | ImgNet-S | ImgNet-R | ImgNet-A | ObjectNet |
|-------|---------|--------|-----------|---------|---------|---------|----------|
| ResNet 18 | CE-only | 69.4 | 56.4 | 19.7 | 31.9 | 1.1 | 27.0 |
| ResNet 18 | CE + interpolation | 69.4 | 56.6 | 19.9 | 32.7 | 1.3 | 27.4 |
| ResNet 18 | (Ours) CE + Soft Loss (no ID accuracy drop) | 69.5 | 56.5 | 19.7 | 32.4 | 1.1 | 27.3 |
| ResNet 18 | (Ours) CE + Soft Loss (pro-OOD) | 69.2 | 56.4 | 20.3 | 34.1 | 1.4 | 27.6 |
| ResNet 18 | (Ours) CE + Soft Loss + interpolation (no ID accuracy drop) | 69.4 | 56.9 | 20.7 | 33.8 | 1.2 | 28.0 |
| ResNet 18 | (Ours) CE + Soft Loss + interpolation (pro-OOD) | 68.0 | 55.9 | 21.2 | 35.1 | 1.4 | 28.6 |
| ResNet 50 | CE-only | 79.5 | 67.9 | 25.5 | 36.5 | 10.3 | 43.2 |
| ResNet 50 | CE + interpolation | 79.5 | 67.8 | 25.6 | 36.6 | 10.6 | 43.3 |
| ResNet 50 | (Ours) CE + Soft Loss (no ID accuracy drop) | 79.8 | 68.6 | 27.7 | 42.5 | 16.2 | 45.5 |
| ResNet 50 | (Ours) CE + Soft Loss (pro-OOD) | 79.8 | 68.6 | 27.7 | 42.5 | 16.2 | 45.5 |
| ResNet 50 | (Ours) CE + Soft Loss + interpolation (no ID accuracy drop) | 79.8 | 68.6 | 27.7 | 42.5 | 16.2 | 45.5 |
| ResNet 50 | (Ours) CE + Soft Loss + interpolation (pro-OOD) | 79.8 | 68.6 | 27.7 | 42.5 | 16.2 | 45.5 |
| VIT-B | CE-only | 75.8 | 62.9 | 27.0 | 40.5 | 8.0 | 27.6 |
| VIT-B | CE + interpolation | 75.7 | 62.4 | 27.0 | 40.5 | 8.2 | 27.7 |
| VIT-B | (Ours) CE + Soft Loss (no ID accuracy drop) | 75.8 | 62.7 | 26.9 | 40.4 | 8.2 | 27.8 |
| VIT-B | (Ours) CE + Soft Loss (pro-OOD) | 75.4 | 62.4 | 28.0 | 42.2 | 9.1 | 27.9 |
| VIT-B | (Ours) CE + Soft Loss + interpolation (no ID accuracy drop) | 75.9 | 62.8 | 27.6 | 41.5 | 8.6 | 28.1 |
| VIT-B | (Ours) CE + Soft Loss + interpolation (pro-OOD) | 75.4 | 62.4 | 28.0 | 42.2 | 9.1 | 27.9 |
| VIT-L | CE-only | 76.8 | 63.9 | 28.4 | 42.2 | 10.6 | 28.7 |
| VIT-L | CE + interpolation | 76.7 | 64.0 | 28.3 | 42.1 | 10.9 | 28.9 |
| VIT-L | (Ours) CE + Soft Loss (no ID accuracy drop) | 76.8 | 64.1 | 28.4 | 42.2 | 10.5 | 28.7 |
| VIT-L | (Ours) CE + Soft Loss (pro-OOD) | 76.7 | 63.6 | 29.4 | 43.9 | 11.7 | 29.0 |
| VIT-L | (Ours) CE + Soft Loss + interpolation (no ID accuracy drop) | 76.8 | 63.8 | 29.2 | 43.6 | 11.5 | 29.0 |
| VIT-L | (Ours) CE + Soft Loss + interpolation (pro-OOD) | 76.7 | 63.6 | 29.4 | 43.9 | 11.7 | 29.0 |
| ConvNext | CE-only | 82.0 | 70.6 | 28.7 | 42.4 | 21.8 | 44.4 |
| ConvNext | CE + interpolation | 82.0 | 70.8 | 28.8 | 42.3 | 22.2 | 44.7 |
| ConvNext | (Ours) CE + Soft Loss (no ID accuracy drop) | 82.0 | 70.7 | 28.7 | 42.3 | 21.9 | 44.6 |
| ConvNext | (Ours) CE + Soft Loss (pro-OOD) | 81.8 | 71.1 | 30.4 | 44.8 | 26.3 | 45.7 |
| ConvNext | (Ours) CE + Soft Loss + interpolation (no ID accuracy drop) | 82.1 | 71.0 | 30.0 | 44.3 | 25.2 | 45.5 |
| ConvNext | (Ours) CE + Soft Loss + interpolation (pro-OOD) | 81.8 | 71.1 | 30.4 | 44.8 | 26.3 | 45.7 |
| Swin Transformer | CE-only | 83.1 | 72.0 | 30.3 | 43.5 | 29.5 | 48.3 |
| Swin Transformer | CE + interpolation | 83.1 | 71.8 | 30.4 | 43.7 | 29.9 | 48.3 |
| Swin Transformer | (Ours) CE + Soft Loss (no ID accuracy drop) | 83.2 | 72.0 | 31.0 | 44.2 | 30.9 | 49.0 |
| Swin Transformer | (Ours) CE + Soft Loss (pro-OOD) | 83.0 | 71.8 | 31.6 | 45.5 | 33.3 | 49.4 |
| Swin Transformer | (Ours) CE + Soft Loss + interpolation (no ID accuracy drop) | 83.2 | 71.9 | 31.4 | 45.3 | 32.7 | 49.5 |
| Swin Transformer | (Ours) CE + Soft Loss + interpolation (pro-OOD) | 83.0 | 71.8 | 31.6 | 45.5 | 33.3 | 49.4 |
