---
# Table 1: Main Intra-LPIPS Results for 10-Shot Image Generation
- **Source**: Table 1, Section 5.3
- **Caption**: "The Intra-LPIPS (↑) results for both DDPM-based strategies and GAN-based baselines are presented for 10-shot image generation tasks. These tasks involve adapting from the source domains of FFHQ and LSUN Church. The 'Parameter Rate' column provides information regarding the proportion of parameters fine-tuned in comparison to the pre-trained model's parameters. The best results are marked as bold."
- **Experimental conditions**: 10-shot target datasets; FFHQ and LSUN Church source domains; 1,000 generated images per method for Intra-LPIPS evaluation; all GAN baselines use StyleGAN2 codebase

| Methods | Parameter Rate | FFHQ → Babies | FFHQ → Sunglasses | FFHQ → Raphael's paintings | LSUN Church → Haunted houses | LSUN Church → Landscape drawings |
|---------|---------------|----------------|-------------------|---------------------------|------------------------------|----------------------------------|
| TGAN | 100% | 0.510±0.026 | 0.550±0.021 | 0.533±0.023 | 0.585±0.007 | 0.601±0.030 |
| TGAN+ADA | 100% | 0.546±0.033 | 0.571±0.034 | 0.546±0.037 | 0.615±0.018 | 0.643±0.060 |
| EWC | 100% | 0.560±0.019 | 0.550±0.014 | 0.541±0.023 | 0.579±0.035 | 0.596±0.052 |
| CDC | 100% | 0.583±0.014 | 0.581±0.011 | 0.564±0.010 | 0.620±0.029 | 0.674±0.024 |
| DCL | 100% | 0.579±0.018 | 0.574±0.007 | 0.558±0.033 | 0.616±0.043 | 0.626±0.021 |
| DDPM-PA | 100% | 0.599±0.024 | 0.604±0.014 | 0.581±0.041 | 0.628±0.029 | 0.706±0.030 |
| DDPM-TAN (Ours) | 1.3% | 0.592±0.016 | 0.613±0.023 | 0.621±0.068 | 0.648±0.010 | 0.723±0.020 |
| LMD-TAN (Ours) | 1.6% | 0.601±0.018 | 0.613±0.011 | 0.592±0.048 | 0.653±0.010 | 0.738±0.026 |
