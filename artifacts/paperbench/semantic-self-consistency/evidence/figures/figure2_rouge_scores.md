---
# Figure 2: Average Rouge-N Scores Across Models
- **Source**: Figure 2, Appendix H.1
- **Caption**: "Average Rouge-N Scores across StrategyQA, AQuA-RAT, and SVAMP for Different Models"
- **Axis labels**: X-axis: Model name; Y-axis: Rouge-N Score (0.3–0.8 range shown)
- **Experimental conditions**: Averaged across StrategyQA, AQuA-RAT, and SVAMP datasets.

| Model | Avg Rouge-N Score |
|-------|-----------------|
| LLAMA 2-7B | 0.569 |
| GPT 3.5 | 0.636 |
| GPT-4o mini | 0.741 |
| Mistral | 0.597 |
| LLAMA 3 (8B) | 0.342 |

**Notes from paper**: GPT-3.5 underperforms on ROUGE metrics (0.636) relative to its accuracy performance, because it generates more comprehensive responses that diverge from the compact reference annotations. Llama 2 7B and Mistral 7B achieve higher ROUGE scores due to writing style and higher text length. ROUGE score does not correlate with reasoning accuracy improvement (also visible in Table 3's BLEU scores). GPT-4o mini achieves the highest Rouge-N score (0.741).
