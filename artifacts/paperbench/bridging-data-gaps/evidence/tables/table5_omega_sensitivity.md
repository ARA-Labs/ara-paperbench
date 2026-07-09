---
# Table 5: FID and Intra-LPIPS vs. PGD Step Size ω
- **Source**: Table 5, Appendix A.2
- **Caption**: "This shows the change in FID (lower is better) and Intra-LPIPS (higher is better) results for FFHQ → Sunglasses as the ω value increases."
- **Experimental conditions**: LDM pre-trained backbone; FFHQ → Sunglasses 10-shot transfer; 1,000 images for Intra-LPIPS, 10,000 for FID; ω=0.02 is optimal (FID minimum 18.13); stable in range [0.01, 0.03]

| ω | FID (↓) | Intra-LPIPS (↑) |
|---|---------|-----------------|
| 0.01 | 18.42 | 0.616±0.020 |
| 0.02 | 18.13 | 0.613±0.011 |
| 0.03 | 18.42 | 0.613±0.016 |
| 0.04 | 19.11 | 0.614±0.013 |
| 0.05 | 19.48 | 0.623±0.015 |
