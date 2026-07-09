# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_efficiency_comparison.md](tables/table1_efficiency_comparison.md) | Table 1, §1 | C01, C02 | Qualitative efficiency comparison matrix of all PEFT, pruning, and combined methods showing training/inference time and memory directional changes. |
| [tables/table2_roberta_t5_main.md](tables/table2_roberta_t5_main.md) | Table 2, §5.4 | C01, C02, C03 | Main results for RoBERTa-base and T5-base at 60% sparsity comparing task performance and normalized training/inference efficiency across all baselines. |
| [tables/table3_llama2_7b_main.md](tables/table3_llama2_7b_main.md) | Table 3, §5.4 | C06, C07 | LLaMA2-7B results at 30% sparsity on Open LLM Leaderboard tasks comparing APT, LoRA, LoRA+Prune, and LLMPruner. |
| [tables/table4_ablation_roberta.md](tables/table4_ablation_roberta.md) | Table 4, §5.6 | C04, C05 | Ablation study on RoBERTa-base removing adaptive pruning, salience scoring, adaptive tuning, and self-distillation components. |
| [tables/table5_ablation_llama.md](tables/table5_ablation_llama.md) | Table 5, §5.6 | C04, C05, C06 | LLaMA2-7B ablation results under 30% and 50% sparsity settings for adaptive pruning, kurtosis, and adaptive tuning components. |
| [tables/table6_hyperparameters.md](tables/table6_hyperparameters.md) | Table 6, §A | — | Complete hyperparameter settings (LR, batch size, epochs, distill epochs) for all datasets used in APT experiments. |
| [tables/table7_bert_baselines.md](tables/table7_bert_baselines.md) | Table 7, §D.1 | C01 | BERT-base comparison to PST and LRP baselines at 50% and 10% parameter density across full GLUE benchmark. |
| [tables/table8_glue_detailed.md](tables/table8_glue_detailed.md) | Table 8, §D.2 | C01, C03 | Detailed RoBERTa pruning results across 7 GLUE tasks comparing APT to LoRA+Distill baseline at 40% sparsity. |
| [tables/table9_llama_7b_13b.md](tables/table9_llama_7b_13b.md) | Table 9, §D.3 | C06, C07 | LLaMA2 7B and 13B comparison at 30% sparsity on Open LLM Leaderboard tasks for all baselines. |
| [tables/table10_distillation_ablation.md](tables/table10_distillation_ablation.md) | Table 10, §G | C03 | Distillation strategy ablation comparing APT self-distillation to traditional KD approaches on RoBERTa SST2. |
| [tables/table11_raw_efficiency_roberta_t5.md](tables/table11_raw_efficiency_roberta_t5.md) | Table 11, §I | C01, C02, C03 | Raw efficiency metrics (TTA in seconds, memory in MB, inference time in ms) for RoBERTa-base and T5-base. |
| [tables/table12_raw_efficiency_llama.md](tables/table12_raw_efficiency_llama.md) | Table 12, §I | C06, C07 | Raw efficiency metrics (training time in seconds, memory in MB, inference time in ms) for LLaMA2-7B on Alpaca. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure3_pareto_curves.md](figures/figure3_pareto_curves.md) | Figure 3, §5.5 | C08 | Pareto curves of task performance vs inference speedup and memory reduction for RoBERTa, T5, and LLaMA2-7B showing APT's Pareto dominance over baselines. |
