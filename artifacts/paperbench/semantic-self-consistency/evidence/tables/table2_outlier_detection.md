---
# Table 2: Outlier Detection Performance
- **Source**: Table 2, Section 5.2
- **Caption**: "Outlier detection performance on SVAMP, AQuA-RAT, and StrategyQA. Performance increase over baseline of n > 1% featured in bold. Encoded based on SciBERT for mathematical reasoning and RoBERTa for commonsense."
- **Conditions**: k=10, temperature=0.8; KNN: n_neighbors=5, ball_tree, euclidean, 90% threshold; Isolation Forest: n_estimators=200, contamination=auto; SVM: linear, nu=0.01, gamma=scale

| Dataset | Method | Llama 2 Best / Average | Mistral Best / Average | GPT 3.5 Best / Average | Llama 3 Best / Average | GPT4o mini Best / Average |
|---------|--------|----------------------|----------------------|----------------------|----------------------|--------------------------|
| AQuA-RAT | SC baseline | 24.8 / 24.8 | 25.6 / 25.6 | 59.4 / 59.4 | 45.28 / 45.28 | 83.07 / 83.07 |
| AQuA-RAT | Isolation Forest | 28.45 / 26.04 | 26.61 / 25.97 | 65.27 / 63.73 | 72.25 / 68.59 | 70.86 / 69.78 |
| AQuA-RAT | K-nearest neighbors | 25.40 / 25.37 | 25.91 / 25.66 | 62.81 / 60.04 | 68.10 / 66.74 | 71.65 / 70.81 |
| AQuA-RAT | One-class SVM | 26.70 / 24.25 | 28.45 / 26.08 | 59.55 / 59.26 | 68.39 / 65.91 | 70.87 / 69.23 |
| SVAMP | SC baseline | 46.5 / 46.5 | 68.5 / 68.5 | 79.8 / 79.8 | 73.33 / 73.33 | 89.80 / 89.80 |
| SVAMP | Isolation Forest | 45.94 / 45.60 | 68.84 / 68.34 | 84.65 / 84.28 | 84.44 / 81.75 | 84.44 / 81.76 |
| SVAMP | K-nearest neighbors | 45.85 / 45.71 | 68.84 / 68.52 | 84.64 / 84.42 | 82.57 / 81.85 | 82.57 / 81.85 |
| SVAMP | One-class SVM | 44.94 / 43.30 | 67.23 / 65.33 | 85.23 / 84.54 | 82.11 / 80.70 | 82.11 / 80.70 |
| StrategyQA | SC baseline | 48.91 / 48.91 | 67.98 / 67.98 | 66.81 / 66.81 | 63.32 / 63.32 | 79.18 / 79.18 |
| StrategyQA | Isolation Forest | 49.34 / 49.01 | 68.70 / 68.13 | 70.07 / 69.01 | 70.80 / 69.37 | 79.91 / 79.56 |
| StrategyQA | K-nearest neighbors | 49.49 / 49.09 | 69.00 / 68.61 | 68.65 / 68.57 | 69.43 / 69.10 | 80.64 / 80.28 |
| StrategyQA | One-class SVM | 49.85 / 48.98 | 69.43 / 68.81 | 68.73 / 68.27 | 70.45 / 69.23 | 81.02 / 80.65 |
