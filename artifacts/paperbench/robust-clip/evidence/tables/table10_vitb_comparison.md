# Table 10: Comparison of ViT-B/32 CLIP Models for Image Classification
- **Source**: Table 10, Appendix B.5
- **Caption**: "In Mao et al. (2023) the supervised fine-tuning scheme TeCoA is introduced. They trained a ViT-B model for 10 epochs with ε = 1/255. In order to show that our selected hyperparameters work well for TeCoA as well, we fine-tune a TeCoA and a FARE ViT-B/32 for one epoch at ε = 1/255."
- **Conditions**: ViT-B/32 architecture; all models evaluated on clean and adversarial (ε=1/255, 2/255, 4/255) accuracy for ImageNet and avg. over 13 zero-shot datasets.

| Vision encoder | ε_train | Adv. Steps | Epochs | Source | ImageNet clean | ImageNet 1/255 | ImageNet 2/255 | ImageNet 4/255 | Avg Zero-shot clean | Avg Zero-shot 1/255 | Avg Zero-shot 2/255 | Avg Zero-shot 4/255 |
|----------------|---------|-----------|--------|--------|---------------|---------------|---------------|---------------|--------------------|--------------------|--------------------|--------------------|
| CLIP | — | — | — | OpenAI | 62.2 | 0.0 | 0.0 | 0.0 | 64.1 | 0.3 | 0.0 | 0.0 |
| TeCoA | 1/255 | — | 10 | Mao et al. (2023) | 54.6 | 35.8 | 20.1 | 3.4 | 50.3 | 38.2 | 27.1 | 9.8 |
| TeCoA | 1/255 | 10 | 2 | ours | 70.3 | 53.2 | 34.5 | 8.0 | 53.1 | 38.2 | 26.6 | 9.6 |
| FARE | 1/255 | 10 | 2 | ours | 62.1 | 32.9 | 12.2 | 0.2 | 60.5 | 38.0 | 20.1 | 2.9 |
