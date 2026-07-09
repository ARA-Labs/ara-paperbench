# Table 8: Ablation of Training Hyperparameters
- **Source**: Table 8, Appendix B.3
- **Caption**: "Ablation of training hyperparameters. We ablate weight decay (WD) and learning rate (LR) for a ViT-B CLIP vision encoder with the FARE fine-tuning method. The avg. zero-shot column is average accuracy across all zero-shot datasets from Sec. 4.3. First row (CLIP) is completely non-robust for both ImageNet and other datasets. The final setting yields best generalization to down-stream zero-shot tasks."
- **Conditions**: ViT-B/32 CLIP vision encoder; FARE fine-tuning at ε=4/255; 10 PGD steps; ImageNet clean accuracy and zero-shot average across 13 non-ImageNet datasets; ℓ∞ adversarial eval at 2/255 and 4/255

| Model | Vision Encoder | LR | WD | ImageNet clean | ImageNet 2/255 | ImageNet 4/255 | Avg. Zero-shot clean | Avg. Zero-shot 2/255 | Avg. Zero-shot 4/255 |
|-------|----------------|----|----|----------------|----------------|----------------|---------------------|---------------------|---------------------|
| CLIP | ViT-B/32 | — | — | 62.2 | 0.0 | 0.0 | 64.1 | 0.0 | 0.0 |
| FARE4-CLIP | ViT-B/32 | 1e-5 | 1e-3 | 51.1 | 29.6 | 14.8 | 48.6 | 33.7 | 21.8 |
| FARE4-CLIP | ViT-B/32 | 1e-5 | 1e-4 | 51.1 | 29.6 | 14.8 | 48.6 | 33.7 | 21.9 |
| FARE4-CLIP | ViT-B/32 | 1e-4 | 1e-4 | 51.7 | 34.2 | 20.2 | 44.4 | 33.3 | 23.8 |
| FARE4-CLIP | ViT-B/32 | 1e-4 | 1e-3 | 51.6 | 34.3 | 20.3 | 44.4 | 33.5 | 23.7 |
