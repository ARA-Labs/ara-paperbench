---
# Table 6: FID and Intra-LPIPS vs. Training Iterations
- **Source**: Table 6, Appendix A.2
- **Caption**: "This shows the change in FID (lower is better) and Intra-LPIPS (higher is better) results for FFHQ → Sunglasses as the number of training iterations increases."
- **Experimental conditions**: LDM pre-trained backbone; FFHQ → Sunglasses 10-shot transfer; 1,000 images for Intra-LPIPS, 10,000 for FID; optimal at 300 iterations (FID=18.13); exact iteration values not stated in paper — table has 9 rows representing increasing iterations with 300 being the optimum at row 7 (inferred from paper text)

| Iteration (increasing order) | FID (↓) | Intra-LPIPS (↑) |
|-------------------------------|---------|-----------------|
| (early) | 111.32 | 0.650±0.071 |
| (early) | 93.82 | 0.666±0.020 |
| (early) | 58.27 | 0.666±0.015 |
| (early) | 31.08 | 0.654±0.017 |
| (early) | 19.51 | 0.635±0.014 |
| (near optimal) | 18.34 | 0.624±0.011 |
| 300 (optimal) | 18.13 | 0.613±0.011 |
| (post-optimal) | 21.17 | 0.604±0.016 |
| (post-optimal) | 21.17 | 0.608±0.019 |
