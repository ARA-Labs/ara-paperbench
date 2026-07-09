# Table 5: Interpolation Method Efficiency Comparison

- **Source**: Table 5, Appendix A.3
- **Caption**: "Comparison of Patch-wise Interpolation and Other Interpolation Methods"
- **Conditions**: Batch size = 256 images; upsampling from CNN output size (H/8 × W/8) to full resolution; single A100 GPU

## ResNet-18/50 (input 224×224, upsampling 28×28 → 224×224)

| Method | NUMBER OF PIXEL ACCESSES (×10^6) | TIME PER BATCH (s) | REQUIRE BACKPROPAGATION |
|--------|----------------------------------|---------------------|------------------------|
| BILINEAR INTERPOLATION | 0.602 | 0.062 ±0.001 | YES |
| BICUBIC INTERPOLATION | 2.408 | 0.195 ±0.013 | YES |
| OURS (PATCH-WISE) | 0.151 | 0.026 ±0.004 | NO |

## ViT-B32 (input 384×384, upsampling 48×48 → 384×384)

| Method | NUMBER OF PIXEL ACCESSES (×10^6) | TIME PER BATCH (s) | REQUIRE BACKPROPAGATION |
|--------|----------------------------------|---------------------|------------------------|
| BILINEAR INTERPOLATION | 1.769 | 0.165 ±0.009 | YES |
| BICUBIC INTERPOLATION | 7.078 | 0.486 ±0.026 | YES |
| OURS (PATCH-WISE) | 0.442 | 0.069 ±0.004 | NO |
