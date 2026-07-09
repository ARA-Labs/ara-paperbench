# Table 14: Clean and Adversarial Embedding Loss
- **Source**: Table 14, Appendix C.4
- **Caption**: "We report mean clean and adversarial loss components of the CLIP models on the ImageNet validation set. We observe that FARE models have the most stable embeddings, while even the clean embedding of TeCoA shows already heavy distortion."
- **Conditions**: 500 images from ImageNet validation set; ε = 4/255; 100-step APGD attack for adversarial loss.
  - L_clean(x) = ||φ_FT(x) - φ_Org(x)||²₂ (Eq. 4)
  - L_adv(x) = max_{||z-x||∞≤4/255} ||φ_FT(z) - φ_Org(x)||²₂ (Eq. 5)

| Metric | CLIP | TeCoA2 | FARE2 | TeCoA4 | FARE4 |
|--------|------|--------|-------|--------|-------|
| E[L_clean(x)] | 0.0 | 236.9 | 32.7 | 292.7 | 47.6 |
| E[L_adv(x)] | 903.8 | 301.9 | 103.9 | 335.0 | 81.9 |
