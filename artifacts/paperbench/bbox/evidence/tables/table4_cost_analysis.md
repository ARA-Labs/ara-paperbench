# Table 4: Performance and Cost Comparison
- **Source**: Table 4, Section 4.4
- **Caption**: "Comparison of performance and cost for the base model, SFT, and BBOX-ADAPTER on the StrategyQA and GSM8K datasets. The performance is shown as accuracy (%), while the costs ($) are reported in training and inference expenses per thousand questions. Note that the inference cost was calculated by aggregating the total token consumption statistics provided by Azure API and subsequently applying the cost per token (gpt-3.5-turbo-1106) as specified in the OpenAI official documentation. The 'single step' refers to a simplified approach wherein the base model generates a set of complete answers in a single step and the adapter then selects the best answer from these candidates as the final response."
- **Conditions**: gpt-3.5-turbo base; Azure-SFT; BBOX-ADAPTER single-step and full-step (beam_size=3)

| Adapter | StrategyQA Acc.(%) | StrategyQA Training Cost ($) | StrategyQA Inference Cost ($/1k Q) | GSM8K Acc.(%) | GSM8K Training Cost ($) | GSM8K Inference Cost ($/1k Q) |
|---------|-------------------|------------------------------|------------------------------------|----------------|--------------------------|-------------------------------|
| gpt-3.5-turbo | 66.59 | - | 0.41 | 67.51 | - | 1.22 |
| Azure-SFT (Peng et al., 2023) | 76.86 | 153.00 | 7.50 | 69.94 | 216.50 | 28.30 |
| BBOX-ADAPTER (Single-step) | 69.87 | 2.77 | 2.20 | 71.13 | 7.54 | 3.10 |
| BBOX-ADAPTER (Full-step) | 71.62 | 3.48 | 5.37 | 74.28 | 11.58 | 12.46 |
