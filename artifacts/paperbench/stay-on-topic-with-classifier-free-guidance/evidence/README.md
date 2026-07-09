---
# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/fig2a_zero_shot_arc_boolq_hellaswag.md](tables/fig2a_zero_shot_arc_boolq_hellaswag.md) | Figure 2a, §3.1 | C01, C02 | Zero-shot accuracy (γ=1 / γ=1.5) for ARC-c, ARC-e, BoolQ, HellaSwag across GPT-2, Pythia, and LLaMA model families. |
| [tables/fig2b_zero_shot_piqa_sciq_trivia_wino_lambada.md](tables/fig2b_zero_shot_piqa_sciq_trivia_wino_lambada.md) | Figure 2b, §3.1 | C01, C02 | Zero-shot accuracy (γ=1 / γ=1.5) for PIQA, SciQ, TriviaQA, WinoGrande, and Lambada across GPT-2, Pythia, and LLaMA model families, including the SOTA Lambada result for LLaMA-7B. |
| [tables/table2_codegen_humaneval_temp02.md](tables/table2_codegen_humaneval_temp02.md) | Table 2, §3.3.2 | C04 | HumanEval pass@k (k=1,10,100) for CodeGen-350M/2B/6B-mono at various CFG strengths with temperature=0.2. |
| [tables/table4_ancova_pvalues.md](tables/table4_ancova_pvalues.md) | Table 4 (Appendix C.2) | C02 | ANCOVA p-values comparing CFG vs vanilla 2x-model FLOPs/accuracy regression lines across 9 benchmark tasks. |
| [tables/table5_codegen350m_full.md](tables/table5_codegen350m_full.md) | Table 5, Appendix C.3 | C04 | Full CodeGen-350M-mono HumanEval pass@k results across all temperatures (0.2, 0.6, 0.8) and CFG strengths. |
| [tables/table6_codegen2b_full.md](tables/table6_codegen2b_full.md) | Table 6, Appendix C.3 | C04 | Full CodeGen-2B-mono HumanEval pass@k results across all temperatures and CFG strengths. |
| [tables/table7_codegen6b_full.md](tables/table7_codegen6b_full.md) | Table 7, Appendix C.3 | C04 | Full CodeGen-6B-mono HumanEval pass@k results across all temperatures and CFG strengths. |
| [tables/table11_bleu_machine_translation.md](tables/table11_bleu_machine_translation.md) | Table 11, Appendix D.1 | C01 | BLEU scores for machine translation (WMT14 fr-en) with Bloom-3B, RedPajama-3B, Bloom-3B 1-shot, and mT0 at various CFG strengths. |
| [tables/table12_gptj_code_confusion.md](tables/table12_gptj_code_confusion.md) | Table 12, Appendix D.2 | C04 | GPT-J code generation language confusion matrices and overall accuracy at γ=1, 1.25, 1.5, 1.75. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/fig5_human_preference.md](figures/fig5_human_preference.md) | Figure 5, §3.4 | C05 | Human preference study results showing 75% system-prompt preference for CFG at γ=3, with undegraded user-prompt relevance (52%) from 611 votes by 71 unique voters. |
| [figures/fig6_entropy_analysis.md](figures/fig6_entropy_analysis.md) | Figure 6, §5.1 | C06 | Logit entropy comparison showing CFG (mean 4.7) reduces entropy below vanilla (mean 5.4) to near instruction-tuned levels. |
| [figures/fig7_perplexity_correlations.md](figures/fig7_perplexity_correlations.md) | Figure 7, §5.2 | C06 | Perplexity correlation matrix between P(y|x), CFG, and instruction-tuned models, plus Spearman correlation between perplexity and CFG/Instruct similarity. |
