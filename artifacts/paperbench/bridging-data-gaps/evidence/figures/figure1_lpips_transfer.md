---
# Figure 1: LPIPS Distances During FFHQ → Sunglasses Fine-tuning
- **Source**: Figure 1, §1
- **Caption**: "Two sets of images generated from corresponding fixed noise inputs at different stages of fine-tuning DDPM from FFHQ to 10-shot Sunglasses. The perceptual distance (LPIPS [32]) with the training target image is shown on each generated image. When the bottom image successfully transfers to the target domain, the top image has already suffered from overfitting."
- **Axis labels**: x-axis — Training iteration (reference point: 1000); y-axis — LPIPS distance to target image
- **Experimental conditions**: DDPM fine-tuned from FFHQ to 10-shot Sunglasses; fixed noise inputs used throughout training; two example images shown at the same training iteration stages

## Extracted LPIPS Data Points (from figure captions on images)

| Image | LPIPS at iteration (stage 1) | LPIPS at iteration (stage 2) |
|-------|------------------------------|------------------------------|
| Top image (overfitting case) | 0.547 | 0.589 |
| Bottom image (successful transfer) | 0.546 | 0.574 |

| Image | LPIPS (stage 3) | LPIPS (stage 4) |
|-------|-----------------|-----------------|
| Top image (overfitting) | 0.421 | 0.568 |
| Bottom image (success) | 0.408 | 0.557 |

| Image | LPIPS (stage 5) | LPIPS (stage 6) |
|-------|-----------------|-----------------|
| Top image (overfitting) | 0.401 | 0.566 |
| Bottom image (success) | 0.394 | 0.466 |

**Note**: The figure shows LPIPS values labeled on individual generated images at different training stages. Top row (overfitting): LPIPS values shown are 0.547, 0.589, 0.421, 0.568, 0.401, 0.566. Bottom row (underfitting/success): LPIPS values shown are 0.546, 0.574, 0.408, 0.557, 0.394, 0.466. Lower LPIPS = more similar to target (successful transfer); very low LPIPS for top image indicates overfitting. The label "1000 Transfer Iteration" appears at approximately the midpoint of the figure.
