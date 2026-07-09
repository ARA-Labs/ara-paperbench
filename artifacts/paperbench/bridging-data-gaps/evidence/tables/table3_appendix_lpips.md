---
# Table 3: Additional Intra-LPIPS Results (Appendix)
- **Source**: Table 3, Appendix A.1
- **Caption**: "The Intra-LPIPS (↑) results for both DDPM-based strategies and GAN-based baselines are presented for 10-shot image generation tasks. The best results are marked as bold."
- **Experimental conditions**: 10-shot target datasets; FFHQ source domain; 1,000 generated images per method; additional results for Sketches and Amedeo Modigliani's paintings (not in Table 1)

| Methods | FFHQ → Sketches | FFHQ → Amedeo's paintings |
|---------|----------------|--------------------------|
| TGAN | 0.394±0.023 | 0.548±0.026 |
| TGAN+ADA | 0.427±0.022 | 0.560±0.019 |
| EWC | 0.430±0.018 | 0.594±0.028 |
| CDC | 0.454±0.017 | 0.620±0.029 |
| DCL | 0.461±0.021 | 0.616±0.043 |
| DDPM-PA | 0.495±0.024 | 0.626±0.022 |
| DDPM-TAN (Ours) | 0.544±0.025 | 0.620±0.021 |
