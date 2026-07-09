# Table 5: Ablation — NCE Loss vs. MLM Loss
- **Source**: Table 5, Section 4.5
- **Caption**: "Accuracy (%) of BBOX-ADAPTER fine-tuned with two types of loss: MLM loss and ranking-based NCE loss."
- **Conditions**: gpt-3.5-turbo generator; StrategyQA and GSM8K; Ground-Truth setting; beam_size=3

| Loss | StrategyQA 0.1B Acc. (%) | StrategyQA 0.3B Acc. (%) | GSM8K 0.1B Acc. (%) | GSM8K 0.3B Acc. (%) |
|------|--------------------------|--------------------------|---------------------|---------------------|
| MLM  | 61.52 | 60.41 | 70.56 | 70.81 |
| NCE  | 71.62 | 71.18 | 72.06 | 73.86 |

## Delta (NCE - MLM)
| | StrategyQA 0.1B | StrategyQA 0.3B | GSM8K 0.1B | GSM8K 0.3B |
|--|----------------|----------------|------------|------------|
| NCE advantage | +10.10 | +10.77 | +1.50 | +3.05 |
