# Table 5: Ablation — NCE Loss vs MLM Loss
- **Source**: Table 5, Section 4.5
- **Caption**: "Accuracy (%) of BBOX-ADAPTER fine-tuned with two types of loss: MLM loss and ranking-based NCE loss."
- **Conditions**: gpt-3.5-turbo; test sets StrategyQA (229 samples) and GSM8K (1319 samples); adapter sizes 0.1B (deberta-v3-base) and 0.3B (deberta-v3-large); full-step beam search inference

| Loss | StrategyQA 0.1B | StrategyQA 0.3B | GSM8K 0.1B | GSM8K 0.3B |
|------|-----------------|-----------------|------------|------------|
| MLM  | 61.52           | 60.41           | 70.56      | 70.81      |
| NCE  | 71.62           | 71.18           | 72.06      | 73.86      |
