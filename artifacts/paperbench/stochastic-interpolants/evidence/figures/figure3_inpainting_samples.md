# Figure 3: Image Inpainting Samples

**Source**: Figure 3, §4.1 (page 8)
**Caption**: Image inpainting: ImageNet-256×256 and ImageNet-512×512. Top panels: Six examples of image in-filling at resolution 256×256, where left columns display masked images, center corresponds to in-filled model samples, and right shows full reference images. Bottom panels: Four examples at resolution 512×512.
**Claims**: C03
**Type**: Qualitative visualization (no numerical data points)

## Description

### ImageNet-256×256 examples (top panels, 6 examples)
Each example shows a triplet:
1. **Left**: Base distribution sample x₀ (known pixels from x₁, masked regions as colorful Gaussian noise static)
2. **Center**: Model output X_{t=1} obtained by integrating probability flow ODE (8)
3. **Right**: Ground truth image x₁

### ImageNet-512×512 examples (bottom panels, 4 examples)
Same triplet format at higher resolution.

## Key observations from the figure
- Masked areas shown as "colorful static" (independent Gaussian noise per channel, per §4.1)
- Generated textures in masked regions differ from ground truth but are visually coherent with surrounding context
- Model does NOT aim to recover exact ground truth — outputs valid samples from the conditional density ρ₁(x₁|x₀, ξ)
- This is highlighted as an advantage of probabilistic models over MSE-trained deterministic models

## Sample summary

| Resolution | Number of examples shown | Layout |
|-----------|--------------------------|--------|
| 256×256 | 6 | Left: masked x₀; Center: model output; Right: ground truth |
| 512×512 | 4 | Left: masked x₀; Center: model output; Right: ground truth |

## Quantitative results
See [tables/table2_inpainting_fid.md](../tables/table2_inpainting_fid.md) for FID-50k numbers.
