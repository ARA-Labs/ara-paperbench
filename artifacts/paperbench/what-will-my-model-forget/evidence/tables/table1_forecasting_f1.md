# Table 1: Forecasting Example Forgetting F1 Scores
- **Source**: Table 1, Section 5.1
- **Caption**: "Average F1-score of forecasting example forgetting when fixing one error in DTest at a time. When fixing errors of base PTLMs, we either fine-tune LM heads only (Head), learn low-rank parameter updates (LoRA), or fine-tune entire model parameters (Full FT). Forgotten examples are minority among all pretraining examples. Bold numbers indicate the forecasting method that achieves the best performance."

| Language Model | BART0Large | BART0Large | FLAN-T5Large | FLAN-T5Large | FLAN-T5Large | FLAN-T53B | FLAN-T53B |
|----------------|-----------|-----------|-------------|-------------|-------------|----------|----------|
| Dataset DR | P3-Test | P3-Test | MMLU | MMLU | MMLU | MMLU | MMLU |
| LM Tuning Setup | Head | Full FT | Head | LoRA | Full FT | Head | LoRA |
| Threshold | 62.96 | 55.75 | 59.95 | 43.93 | 48.43 | 63.64 | 41.42 |
| Fixed Logit | 69.57 | 43.26 | 68.37 | 19.54 | 12.74 | 59.03 | 17.50 |
| Trainable Logit | 73.39 | 57.15 | 61.09 | 36.54 | 40.91 | 55.07 | 31.40 |
| Representation | **79.32** | **67.19** | 67.81 | **48.66** | **51.51** | **65.93** | **42.99** |
| w/o Prior | 77.92 | 66.53 | **67.21** | 47.11 | 50.38 | 63.98 | 41.60 |

Note: Bold indicates best performance per column. For FLAN-T5Large/Head, Fixed Logit (68.37) achieves highest F1, but Representation (67.81) is close. The paper text states representation achieves best in 7/8 configurations.
