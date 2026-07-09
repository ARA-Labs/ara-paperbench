---
# Table 4: FID and Intra-LPIPS vs. Similarity Guidance Scale γ
- **Source**: Table 4, Appendix A.2
- **Caption**: "This shows the change in FID (↓) and Intra-LPIPS (↑) results for FFHQ → Sunglasses as the γ value increases."
- **Experimental conditions**: LDM pre-trained backbone; FFHQ → Sunglasses 10-shot transfer; 1,000 images for Intra-LPIPS, 10,000 for FID; rows ordered by increasing γ; γ=5 is optimal (FID minimum 18.13); specific γ values for rows 1,2,4,5 not explicitly stated in paper text (only γ=5 is stated explicitly)

| γ (increasing) | FID (↓) | Intra-LPIPS (↑) |
|---------------|---------|-----------------|
| (lower value) | 20.75 | 0.641±0.014 |
| (lower value) | 18.86 | 0.627±0.013 |
| 5 (optimal) | 18.13 | 0.613±0.011 |
| (higher value) | 24.12 | 0.603±0.017 |
| (higher value) | 29.48 | 0.592±0.017 |
