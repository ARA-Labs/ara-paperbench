# Table 9: Ablation of Loss Function
- **Source**: Table 9, Appendix B.4
- **Caption**: "We compare ViT-B/32 FARE models trained with the original squared ℓ₂-norm formulation (Eq. (3)), and using the ℓ₁-norm instead."
- **Conditions**: ViT-B/32; FARE fine-tuning at ε=4/255; LR=1e-5, WD=1e-4 (final chosen hyperparameters); 2 epochs on ImageNet.

| Loss used in Eq. (3) | ImageNet clean | ImageNet 2/255 | ImageNet 4/255 | Avg Zero-shot clean | Avg Zero-shot 2/255 | Avg Zero-shot 4/255 |
|---------------------|---------------|---------------|---------------|--------------------|--------------------|---------------------|
| ‖·‖₂² | 51.1 | 29.6 | 14.8 | 48.6 | 33.7 | 21.9 |
| ‖·‖₁ | 51.2 | 30.1 | 15.1 | 48.6 | 33.9 | 21.9 |
