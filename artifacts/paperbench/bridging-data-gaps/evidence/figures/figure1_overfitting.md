---
# Figure 1: Divergent Transfer Pacing During DDPM Fine-tuning

**Source**: Figure 1, §1 (Introduction)
**Task**: DDPM fine-tuning from FFHQ to 10-shot Sunglasses
**Supporting claims**: C03
**Description**: Two sets of images generated from fixed noise inputs at different stages of fine-tuning. LPIPS perceptual distance with the training target image is shown on each generated image. Demonstrates that random non-targeted noise causes unbalanced transfer pacing.

## Extracted LPIPS Values

The figure shows LPIPS distances at different fine-tuning stages (exact iteration numbers not labeled; relative ordering shown):

### Image 1 (Top — eventually overfits):
| Stage | LPIPS Distance |
|-------|---------------|
| Early | 0.547 |
| Middle-early | 0.589 |
| Middle | 0.546 |
| Middle-late | 0.574 |
| Late | 0.421 |
| Final | 0.568 |

**Status**: "Transfer Success — Overfitting" (caption label)
**Note**: LPIPS values fluctuate and then plateau; the image overfits to the target

### Image 2 (Bottom — successfully transfers):
| Stage | LPIPS Distance |
|-------|---------------|
| Early | 0.408 |
| Middle-early | 0.557 |
| Middle | 0.401 |
| Middle-late | 0.566 |
| Late | 0.394 |
| Final | 0.466 |

**Status**: "Transfer Success — Underfitting" for some stages, then successful transfer
**Note**: The bottom image successfully transfers to target domain at ~1,000 iterations

## Axis: "1000 Transfer Iteration" (label shown at bottom of figure)

## Key Observation
When the bottom image successfully transfers to the target domain, the top image has already overfit. This demonstrates the fundamental problem of non-targeted random Gaussian noise in DPMs: different images require different numbers of iterations, making it impossible to find a single iteration count that works for all images without causing overfitting or underfitting.
