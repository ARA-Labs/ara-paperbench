# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table2_main_results.md](tables/table2_main_results.md) | Table 2, §4.2 | C01, C06 | Main accuracy/True+Info results for CoT baseline, Azure-SFT, and three BBOX-ADAPTER variants across four QA datasets using gpt-3.5-turbo. |
| [tables/table3_plug_and_play.md](tables/table3_plug_and_play.md) | Table 3, §4.3 | C05 | Plug-and-play transfer results showing BBOX-ADAPTER (trained on gpt-3.5-turbo) applied without retraining to davinci-002 and Mixtral-8×7B on StrategyQA, GSM8K, TruthfulQA. |
| [tables/table4_cost_analysis.md](tables/table4_cost_analysis.md) | Table 4, §4.4 | C02, C03 | Training cost ($) and inference cost ($/1k questions) for gpt-3.5-turbo CoT, Azure-SFT, and BBOX-ADAPTER (single-step and full-step) on StrategyQA and GSM8K. |
| [tables/table5_ablation_loss.md](tables/table5_ablation_loss.md) | Table 5, §4.5 | C04 | Accuracy comparison between MLM loss and ranking-based NCE loss for 0.1B and 0.3B adapter sizes on StrategyQA and GSM8K. |
| [tables/table6_whitebox_extension.md](tables/table6_whitebox_extension.md) | Table 6, §4.7 | C01 | Accuracy (%) and GPU VRAM (GiB) for Mixtral-8×7B baseline, SFT-LoRA, and BBOX-ADAPTER on StrategyQA, measuring cost-efficiency of black-box adaptation on an open-source model. |
| [tables/table7_toxigen.md](tables/table7_toxigen.md) | Table 7, Appendix E | C01 | Toxic (%) and Toxicity Probability (%) for Mixtral-8×7B with and without BBOX-ADAPTER on ToxiGen, showing toxicity reduction as a secondary application. |
| [tables/table8_lora_hyperparams.md](tables/table8_lora_hyperparams.md) | Table 8, Appendix F.2 | — | Hyperparameter settings for the SFT-LoRA baseline used for fair comparison with BBOX-ADAPTER on Mixtral-8×7B. |
| [tables/table9_azure_sft_gridsearch.md](tables/table9_azure_sft_gridsearch.md) | Table 9, Appendix F.3 | C02 | Grid search results for Azure-SFT on GSM8K showing lack of transparency in the fine-tuning API and limited performance variation across hyperparameter settings. |
| [tables/table10_main_results_std.md](tables/table10_main_results_std.md) | Table 10, Appendix I.1 | C01, C06 | Main results with standard deviations, replicating Table 2 with error bars for gpt-3.5-turbo CoT, BBOX-ADAPTER variants across four datasets. |

## Figures

No quantitative figure data extracted (Figure 3 — beam size and iteration plots — contains bar/line charts without precise labeled data points that can be extracted from the paper text; Figure 4 is a qualitative case study; Figures 5–10 are loss/energy curves without tabulated values).
