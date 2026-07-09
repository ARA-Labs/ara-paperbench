---
# Table 2: FID Results on FFHQ → Babies and Sunglasses (10-shot)
- **Source**: Table 2, Section 5.3
- **Caption**: "FID (↓) results of each method on 10-shot FFHQ → Babies and Sunglasses. The best results are marked as bold."
- **Experimental conditions**: 10-shot target datasets; FFHQ source domain; reference datasets: Sunglasses (2,500 images), Babies (2,700 images); FID computed with 10,000 generated images (per Appendix A.2)
- **Note**: The paper uses "ADMT" as the label for DDPM-PA in Table 2; the "Our method" row corresponds to TAN (DDPM-TAN/LDM-TAN combined result shown as 46.70 Babies, 20.06 Sunglasses)

| Methods | Babies | Sunglasses |
|---------|--------|------------|
| TGAN | 104.79 | 55.61 |
| ADA | 102.58 | 53.64 |
| EWC | 87.41 | 59.73 |
| CDC | 74.39 | 42.13 |
| DCL | 52.56 | 38.01 |
| ADMT | 48.92 | 34.75 |
| Our method (TAN) | 46.70 | 20.06 |
