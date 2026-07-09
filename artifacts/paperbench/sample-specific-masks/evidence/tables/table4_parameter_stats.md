# Table 4: Statistics of Mask Generator Parameter Size
- **Source**: Table 4, Appendix A.2
- **Caption**: "Statistics of Mask Generator Parameter Size"
- **Experimental conditions**: Parameter counts for fmask CNN across three pretrained backbones; "Reprogramming Parameters" = size of delta (shared pattern); "Pre-trained Model Parameters" = total frozen backbone params

| PRE-TRAINED MODEL | INPUT IMAGE SIZE | fmask CNN LAYERS | EXTRA PARAMETERS OF fmask | OUR EXTRA PARAMS ÷ REPROGRAMMING PARAMS | OUR EXTRA PARAMS ÷ PRE-TRAINED MODEL PARAMS |
|-------------------|------------------|------------------|---------------------------|----------------------------------------|---------------------------------------------|
| RESNET-18 | 224×224×3 | 5 | 26,499 | 17.60% | 0.23% |
| RESNET-50 | 224×224×3 | 5 | 26,499 | 17.60% | 0.10% |
| VIT-B32 | 384×384×3 | 6 | 102,339 | 23.13% | 0.12% |

**Notes**:
- Reprogramming parameters for ResNet = 224×224×3 = 150,528
- Reprogramming parameters for ViT = 384×384×3 = 442,368
- ResNet-18 total params ≈ 11.7M; ResNet-50 total params ≈ 25.6M; ViT-B32 total params ≈ 86M (inferred)
