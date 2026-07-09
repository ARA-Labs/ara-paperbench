# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_lvlm_robustness.md](tables/table1_lvlm_robustness.md) | Table 1, §4.1 | C01, C07 | Clean and robust (ε=2/255, 4/255) performance of OpenFlamingo 9B and LLaVA-1.5 7B with 5 vision encoders across COCO, Flickr30k, TextVQA, VQAv2, showing FARE consistently outperforms TeCoA. |
| [tables/table2_transfer_attacks.md](tables/table2_transfer_attacks.md) | Table 2, §4.1 | C07 | CIDEr scores for adversarial COCO images (ε=4/255) transferred between OF and LLaVA models, showing cross-model transfer succeeds for CLIP but fails for robust encoders. |
| [tables/table3_targeted_attacks.md](tables/table3_targeted_attacks.md) | Table 3, §4.2 | C03 | Targeted ℓ∞ attack success counts (out of 25) for 6 target captions on LLaVA with 5 encoders at ε=2/255 and ε=4/255, demonstrating FARE4 is fully robust. |
| [tables/table4_zeroshot_classification.md](tables/table4_zeroshot_classification.md) | Table 4, §4.3 | C04 | Clean and adversarial (ε=2/255, 4/255) zero-shot accuracy across ImageNet and 13 datasets, showing FARE maintains 6.9-7.0% better clean accuracy than TeCoA on average. |
| [tables/table5_pope_hallucination.md](tables/table5_pope_hallucination.md) | Table 5, §4.4 | C05 | POPE hallucination benchmark F1-scores for LLaVA-1.5 7B with 5 encoders across random/popular/adversarial splits, showing FARE reduces hallucination vs TeCoA. |
| [tables/table6_sqai.md](tables/table6_sqai.md) | Table 6, §4.4 | C06 | SQA-I chain-of-thought reasoning accuracy for LLaVA with 5 vision encoders, showing FARE outperforms TeCoA by 2.3-2.4% and is near CLIP performance. |
| [tables/table7_jailbreak.md](tables/table7_jailbreak.md) | Table 7, §4.4 | C01 | Jailbreaking attack success counts for LLaVA with CLIP, TeCoA4, FARE4 across 4 harm categories and 4 attack strengths (0, 16/255, 32/255, 64/255). |
| [tables/table8_hparam_ablation.md](tables/table8_hparam_ablation.md) | Table 8, Appendix B.3 | C01, C04 | ViT-B/32 FARE hyperparameter ablation (LR × WD) showing LR=1e-5 yields better zero-shot generalization than LR=1e-4 at slight ImageNet robustness cost. |
| [tables/table9_loss_ablation.md](tables/table9_loss_ablation.md) | Table 9, Appendix B.4 | C02 | Ablation of ℓ₁ vs squared ℓ₂ loss in FARE for ViT-B/32, showing both perform comparably, validating the ℓ₂ design choice. |
| [tables/table10_vitb_comparison.md](tables/table10_vitb_comparison.md) | Table 10, Appendix B.5 | C01, C04 | Comparison of ViT-B/32 CLIP models including original Mao et al. TeCoA checkpoint and our re-trained TeCoA and FARE at ε=1/255, showing improved hyperparameters benefit TeCoA. |
| [tables/table11_attack_comparison.md](tables/table11_attack_comparison.md) | Table 11, Appendix B.7 | C01 | Comparison of ensemble attack pipeline vs Schlarmann & Hein (2023) single-precision attack, showing our attack is stronger (lower scores) and 7.7× faster. |
| [tables/table12_targeted_500iter.md](tables/table12_targeted_500iter.md) | Table 12, Appendix B.9 | C03 | Targeted attack success rates with 500 iterations (vs 10,000 in main paper) on CLIP-LLaVA, showing strong attacks require many iterations. |
| [tables/table13_llava13b.md](tables/table13_llava13b.md) | Table 13, Appendix C.3 | C01 | Clean performance of LLaVA-1.5 13B with 5 vision encoders, showing FARE generalizes to larger LLaVA models. |
| [tables/table14_embedding_loss.md](tables/table14_embedding_loss.md) | Table 14, Appendix C.4 | C02 | Mean clean and adversarial embedding loss (||φ_FT - φ_Org||²₂) for all 5 encoders on 500 ImageNet validation images, showing FARE best preserves original embeddings. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| (No separate quantitative figure files created; all quantitative data extracted in tables above) | — | — | Figure 1 (radar plot) and Figure 2 (qualitative examples) contain data already captured in Tables 1, 3, 4; Figures 3 and 5 are qualitative outputs with no additional quantitative data beyond Table 3. |
