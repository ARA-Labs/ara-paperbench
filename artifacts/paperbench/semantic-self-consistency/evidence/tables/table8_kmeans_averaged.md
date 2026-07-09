---
# Table 8: K-Means Averaged Over 10 Runs

**Source**: Table 8, §G.3
**Claims**: C04
**Description**: K-means performance averaged over 10 runs with different random initializations, showing volatility based on initial cluster placement.

| Model | AQuA-RAT | SVAMP | SQA (StrategyQA) |
|-------|----------|-------|-----------------|
| Llama 2 | 24.16 | 42.47 | 47.60 |
| Llama 3 | 46.06 | 72.33 | 17.6 |
| Mistral | 24.83 | 62.52 | 23.73 |
| GPT 3.5 | 65.52 | 78.67 | 21.97 |
| GPT-4o mini | 83.46 | 89.62 | 36.68 |

## Clustering Quality Metrics
- Averaged silhouette score: 0.41 (moderate cluster distinction)
- Average proportion of correct answers in preponderant cluster: 60.5%
- Averaged over 10 random states for representative results

## Notes
- High volatility across random initializations
- Silhouette score of 0.41 indicates moderate but not strong separation
- Method shows diminishing returns vs standard SC on most configurations
