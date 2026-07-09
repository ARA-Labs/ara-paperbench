# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_forecasting_f1.md](tables/table1_forecasting_f1.md) | Table 1, §5.1 | C01, C02, C03 | Binary F1 scores for all four forecasting methods (threshold, fixed logit, trainable logit, representation, w/o prior) across BART0Large/P3-Test, FLAN-T5Large/MMLU, FLAN-T53B/MMLU and three fine-tuning configurations (Head, LoRA, Full FT). |
| [tables/table2_ood_generalization.md](tables/table2_ood_generalization.md) | Table 2, §5.1 | C05 | In-domain (P3-TestID) and out-of-domain (P3-TestOOD) F1 scores for threshold, trainable logit, representation, and w/o prior methods on BART0, showing that only representation with prior generalizes OOD. |
| [tables/table3_sequential_refinement.md](tables/table3_sequential_refinement.md) | Table 3, §5.2 | C04 | Edit success rate and EM Drop Ratio (%) for sequential error-fixing across all models and replay strategies (Vanilla FT, Random, Threshold, Trainable Logit, Representation, GT Forget, MIR, OCS). |
| [tables/table4_single_error.md](tables/table4_single_error.md) | Table 4, §5.2 | C04 | EM Drop Ratio (%) for single-error fixing separately, showing benefit of forecasting-guided replay even for individual error corrections. |
| [tables/table5_complexity.md](tables/table5_complexity.md) | Table 5, §5.3 | C06 | Computational complexity formulas for each forecasting method under Head and Full FT settings. |
| [tables/table7_base_em.md](tables/table7_base_em.md) | Table 7, Appendix B | — | EM scores of base LMs on upstream P3-Train data before performing updates (BART0Large: 50.50, FLAN-T5Large: 47.47, FLAN-T53B: 51.31). |
| [tables/table8_flops.md](tables/table8_flops.md) | Table 8, Appendix C | C06 | Actual FLOP counts for forecasting 3,600 upstream examples given one online example under FLAN-T5Large Full FT (Representation: 1.35e10, Trainable Logit: 2.15e11, GT: 9.04e14). |
| [tables/table6_mend_comparison.md](tables/table6_mend_comparison.md) | Table 6, Appendix A | C04 | Comparison of replay-based methods vs. MEND on FLAN-T5Large LoRA for single error fixing, showing MEND achieves lower EM Drop but at cost of edit success rate. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure3_sequential_metrics.md](figures/figure3_sequential_metrics.md) | Figure 3, §5.1 | C01, C03 | Running average F1, Precision, and Recall over sequential refinement stream for FLAN-T5Large Full FT, showing representation-based achieves best F1/precision while all methods' recall decreases over time. |
| [figures/figure2a_logit_transfer.md](figures/figure2a_logit_transfer.md) | Figure 2(a), §3.2 | C03 | Logit values before and after fine-tuning for a specific example pair, demonstrating the logit-change transfer phenomenon where large changes in xi's tokens propagate to xj's tokens. |
