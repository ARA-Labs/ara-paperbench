# Table 9: LLaMA2 7B and 13B 30% Sparsity Pruning Results
- **Source**: Table 9, Appendix D.3
- **Caption**: "LLaMA2 7B and 13B 30% sparsity pruning results with GPT4-generated Alpaca dataset, evaluated on the Open LLM leaderboard few-shot tasks."

| Model | Method | ARC | HellaSwag | MMLU | TruthfulQA | Avg. |
|-------|--------|-----|-----------|------|------------|------|
| LLaMA2 7B | (base, no FT) | 53.1 | 77.7 | 43.8 | 39.0 | 53.4 |
| LLaMA2 7B | LoRA | 55.6 | 79.3 | 46.9 | 49.9 | 57.9 |
| LLaMA2 7B | LoRA+Prune | 46.8 | 65.2 | 23.9 | 46.2 | 45.5 |
| LLaMA2 7B | LLMPruner | 39.2 | 67.0 | 24.9 | 40.6 | 42.9 |
| LLaMA2 7B | APT | 45.4 | 71.1 | 36.9 | 46.6 | 50.0 |
| LLaMA2 13B | (base, no FT) | 59.4 | 82.1 | 55.8 | 37.4 | 58.7 |
| LLaMA2 13B | LoRA | 60.8 | 82.8 | 56.0 | 46.5 | 61.5 |
| LLaMA2 13B | LoRA+Prune | 56.4 | 79.1 | 50.7 | 42.1 | 57.1 |
| LLaMA2 13B | LLMPruner | 46.8 | 74.0 | 24.7 | 34.8 | 45.1 |
| LLaMA2 13B | APT | 49.5 | 75.8 | 52.5 | 44.7 | 55.6 |

*Note: ARC = 25-shot, HellaSwag = 10-shot, MMLU = 5-shot, TruthfulQA = 0-shot.*
*Note: APT 13B maintains 90.0% of LoRA performance (55.6/61.5 = 90.4%).*
*Note: APT outperforms LLMPruner on all tasks for both 7B and 13B.*
