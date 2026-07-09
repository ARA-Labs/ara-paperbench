---
# Table 11: Average Deviation for K-Means Clusters

**Source**: Table 11, §M.1.3
**Claims**: C04
**Description**: Average deviation (distance to cluster centroid) for chosen cluster vs disregarded cluster in k-means (k=2) analysis. Lower deviation indicates tighter, more coherent cluster.

| Method | Model | Chosen cluster | Disregarded cluster |
|--------|-------|---------------|---------------------|
| SVAMP | LLAMA 2 | 2.037 | 2.567 |
| SVAMP | Mistral | 2.981 | 3.800 |
| SVAMP | GPT 3.5 | 4.428 | 4.513 |
| SVAMP | GPT 4o mini | 4.356 | 4.653 |
| SVAMP | LLAMA 3 | 4.562 | 4.569 |
| AQuA-RAT | LLAMA 2 | 0.838 | 0.670 |
| AQuA-RAT | Mistral | 0.871 | 0.598 |
| AQuA-RAT | GPT 3.5 | 3.649 | 3.684 |
| AQuA-RAT | GPT 4o mini | 2.134 | 3.082 |
| AQuA-RAT | LLAMA 3 | 3.235 | 3.163 |
| StrategyQA | LLAMA 2 | 2.741 | 3.215 |
| StrategyQA | Mistral | 1.962 | 2.487 |
| StrategyQA | GPT 3.5 | 4.283 | 4.751 |
| StrategyQA | GPT 4o mini | 1.869 | 2.935 |
| StrategyQA | LLAMA 3 | 2.864 | 3.124 |

## Notes
- In most SVAMP/StrategyQA cases, chosen cluster has lower deviation than disregarded cluster
- AQuA-RAT shows some reversed patterns (LLAMA 2, Mistral), consistent with k-means fragility
- Both clusters show comparable performance, explaining k-means' limited discriminative power
