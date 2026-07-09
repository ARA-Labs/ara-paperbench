# Table 4: Mask Generator Parameter Statistics
- **Source**: Table 4, Appendix A.2
- **Caption**: "Statistics of Mask Generator Parameter Size"
- **Conditions**: Default patch_size=8, channels=3

| PRE-TRAINED MODEL | INPUT IMAGE SIZE | fmask CNN LAYERS | EXTRA PARAMS (fmask) | fmask PARAMS ÷ REPROG PARAMS | fmask PARAMS ÷ PRETRAINED PARAMS |
|-------------------|-----------------|-------------------|----------------------|-------------------------------|----------------------------------|
| RESNET-18 | 224×224×3 | 5 | 26,499 | 17.60% | 0.23% |
| RESNET-50 | 224×224×3 | 5 | 26,499 | 17.60% | 0.10% |
| VIT-B32 | 384×384×3 | 6 | 102,339 | 23.13% | 0.12% |

**Note**: "Reprogramming parameters" = size of shared pattern δ. For ResNet: 224×224×3 = 150,528 params. For ViT: 384×384×3 = 442,368 params.
