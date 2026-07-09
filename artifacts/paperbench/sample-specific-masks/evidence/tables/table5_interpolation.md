# Table 5: Comparison of Patch-wise Interpolation and Other Interpolation Methods
- **Source**: Table 5, Appendix A.3
- **Caption**: "Comparison of Patch-wise Interpolation and Other Interpolation Methods"
- **Experimental conditions**: Batch size 256; single A100 GPU; metrics: (1) number of pixel accesses per image (fewer = better), (2) time per batch in seconds (mean ± std, fewer = better), (3) whether backpropagation is required during training

| MODEL GROUP | METRIC | BILINEAR INTERPOLATION | BICUBIC INTERPOLATION | OURS (PATCH-WISE) |
|-------------|--------|------------------------|----------------------|-------------------|
| RESNET-18/50 | NUMBER OF PIXEL ACCESSES (1E6) | 0.602 | 2.408 | 0.151 |
| RESNET-18/50 | TIME PER BATCH (S) | 0.062 ±0.001 | 0.195 ±0.013 | 0.026 ±0.004 |
| RESNET-18/50 | REQUIRE BACKPROPAGATION | YES | YES | NO |
| VIT-B32 | NUMBER OF PIXEL ACCESSES (1E6) | 1.769 | 7.078 | 0.442 |
| VIT-B32 | TIME PER BATCH (S) | 0.165 ±0.009 | 0.486 ±0.026 | 0.069 ±0.004 |
| VIT-B32 | REQUIRE BACKPROPAGATION | YES | YES | NO |
