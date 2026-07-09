# Table 5: LLaMA2-7B Ablation Results Under 30% and 50% Sparsity
- **Source**: Table 5, Section 5.6
- **Caption**: "LLaMA 2 7B model ablation results under 30% and 50% sparsity settings. T.M. denotes relative training memory compare to LoRA-tuning."

| Sparsity | Method | T.M. | ARC | HellaSwag | MMLU | TruthfulQA | Avg. |
|---------|--------|------|-----|-----------|------|------------|------|
| 30% | APT | 75.8% | 45.4 | 71.1 | 36.9 | 46.6 | 50.0 |
| 0% (no prune) | w/o AP | 102.4% | 53.8 | 79.1 | 46.9 | 48.4 | 57.1 |
| 30% | w/o kurtosis | 75.9% | 47.2 | 39.7 | 23.0 | 42.3 | 38.1 |
| 30% | w/o AT | 76.1% | 44.2 | 70.1 | 40.8 | 45.1 | 50.0 |
| 50% | APT | 60.2% | 29.8 | 48.9 | 26.7 | 47.6 | 38.2 |
| 50% | w/o AT | 60.1% | 27.9 | 46.2 | 24.5 | 44.7 | 35.8 |

*Note: All training memory (T.M.) normalized to LoRA-tuning (100%) baseline.*
*Note: w/o AP at 0% sparsity means no pruning is applied; model size same as dense LoRA-tuned model.*
*Note: w/o kurtosis uses only activation-gradient salience without the kurtosis term.*
