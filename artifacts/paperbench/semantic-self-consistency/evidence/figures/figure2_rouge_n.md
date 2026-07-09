---
# Figure 2: Average ROUGE-N Score Comparison Among Models
- **Source**: Figure 2, Appendix H.1
- **Caption**: "Average Rouge-N Scores across StrategyQA, AQuA-RAT, and SVAMP for Different Models"
- **Axis labels**: X = Model name; Y = Rouge-N Score (range ≈ 0.3 to 0.8)
- **Conditions**: Average ROUGE-N score across all three datasets (StrategyQA, AQuA-RAT, SVAMP) per model

| Model | Average Rouge-N Score |
|-------|----------------------|
| LLAMA (Llama 3 8B) | 0.569 |
| GPT 3.5 | 0.636 |
| GPT-4o mini | 0.741 |
| Mistral | 0.597 |
| LLAMA2-7B | 0.342 |

**Notes**:
- GPT-4o mini achieves the highest ROUGE-N score (0.741) despite not always being the highest-accuracy model.
- GPT-3.5 underperforms on ROUGE (0.636) relative to its accuracy because it generates more comprehensive, less formulaic responses that diverge from terse reference annotations.
- Llama 2 7B has the lowest ROUGE-N score (0.342), likely related to its shorter and less structured chain-of-thought outputs.
