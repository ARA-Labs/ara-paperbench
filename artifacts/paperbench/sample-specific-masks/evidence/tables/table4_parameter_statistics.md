# Table 4: Mask Generator Parameter Size Statistics

- **Source**: Table 4, Appendix A.2
- **Caption**: "Statistics of Mask Generator Parameter Size"
- **Conditions**: fmask CNN architecture as described in Appendix A.2; reprogramming parameters = size of δ pattern

| PRE-TRAINED MODEL | INPUT IMAGE SIZE | fmask CNN LAYERS | EXTRA PARAMETERS OF fmask | OUR EXTRA PARAMS ÷ REPROGRAMMING PARAMS | OUR EXTRA PARAMS ÷ PRE-TRAINED MODEL PARAMS |
|-------------------|-----------------|-----------------|--------------------------|----------------------------------------|---------------------------------------------|
| RESNET-18 | 224×224×3 | 5 | 26,499 | 17.60% | 0.23% |
| RESNET-50 | 224×224×3 | 5 | 26,499 | 17.60% | 0.10% |
| VIT-B32 | 384×384×3 | 6 | 102,339 | 23.13% | 0.12% |

**Notes**:
- Reprogramming parameters = number of parameters in δ (= H×W×3 for each model: 224×224×3 = 150,528 for ResNet; 384×384×3 = 442,368 for ViT)
- 5-layer CNN used for ResNet-18 and ResNet-50; 6-layer CNN used for ViT-B32
- Input image size column shows the size fed into fmask (= pre-trained model input size after bilinear upsampling)
- Note: ResNet-18 input shown as "224×224×2" in the original paper table, but this appears to be a typo; the mask generator input is 224×224×3 (3-channel image)
