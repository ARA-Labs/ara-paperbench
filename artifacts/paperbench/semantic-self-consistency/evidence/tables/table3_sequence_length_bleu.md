---
# Table 3: Sequence Length, Accuracy Increase, and BLEU Score
- **Source**: Table 3, Appendix/Discussion section
- **Caption**: "Comparison of Sequence Length, Accuracy Increase, and BLEU Score across datasets and models"
- **Experimental conditions**: Average sequence length in tokens; accuracy increase (%) is semantic method improvement over SC baseline; BLEU scores averaged per model-dataset pair.

| Dataset | Model | Avg. Seq. Length | Avg. Accuracy Increase (%) | Avg. BLEU Score |
|---------|-------|-----------------|--------------------------|----------------|
| AQuA-RAT | GPT 3.5 | 102.40 | 7.30 | 0.342 |
| AQuA-RAT | Mistral | 53.24 | 3.80 | 0.031 |
| AQuA-RAT | Llama 2 | 49.58 | 0.00 | 0.045 |
| AQuA-RAT | Llama 3 | 56.21 | 1.49 | 0.185 |
| AQuA-RAT | GPT-4o mini | 83.65 | 1.36 | 0.358 |
| SVAMP | GPT 3.5 | 49.71 | 0.85 | 0.440 |
| SVAMP | Mistral | 52.92 | 1.50 | 0.152 |
| SVAMP | Llama 2 | 52.29 | 0.65 | 0.213 |
| SVAMP | Llama 3 | 83.45 | 0.505 | 0.300 |
| SVAMP | GPT-4o mini | 80.32 | 1.19 | 0.547 |
| StrategyQA | GPT 3.5 | 92.66 | 3.145 | 0.289 |
| StrategyQA | Mistral | 50.68 | -4.955 | 0.227 |
| StrategyQA | Llama 2 | 60.39 | 9.82 | 0.075 |
| StrategyQA | Llama 3 | 77.84 | 4.075 | 0.141 |
| StrategyQA | GPT-4o mini | 88.91 | -2.44 | 0.327 |

**Key finding**: Positive correlation observed between Avg. Seq. Length and Avg. Accuracy Increase. BLEU score shows no correlation with accuracy improvement.
