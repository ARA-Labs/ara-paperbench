---
# Table 1: Accuracy Comparison — CPW and SCW vs. SC Baseline
- **Source**: Table 1, Section 5.1
- **Caption**: "Accuracy comparison of CPW and cosine similarity on different datasets and models, with SciBERT embeddings for AQuA-RAT and SVAMP and RoBERTa encodings for StrategyQA."
- **Conditions**: k=10 samples, temperature=0.8, SciBERT featurizer for AQuA-RAT/SVAMP, RoBERTa featurizer for StrategyQA; deltas relative to SC baseline shown in parentheses

| Dataset | Method/Metric | Llama 2 7B | Mistral 7B | GPT 3.5 | Llama 3 8B | GPT-4o mini |
|---------|--------------|-----------|-----------|---------|-----------|------------|
| AQuA-RAT | Top prob sample | 21.65 | 24.34 | 53.63 | 43.02 | 79.22 |
| AQuA-RAT | SC baseline | 24.80 | 25.60 | 59.40 | 45.28 | 83.07 |
| AQuA-RAT | CPW | 24.60 (-0.2) | 29.00 (+3.4) | 68.00 (+8.6) | 46.06 (+0.78) | 82.68 (-0.39) |
| AQuA-RAT | SCW | 25.00 (+0.2) | 29.80 (+4.2) | 65.40 (+6.0) | 47.48 (+2.2) | 86.18 (+3.11) |
| SVAMP | Top prob sample | 31.90 | 65.18 | 77.42 | 70.55 | 85.62 |
| SVAMP | SC baseline | 46.50 | 68.50 | 79.80 | 73.33 | 89.80 |
| SVAMP | CPW | 47.40 (+0.9) | 69.80 (+1.3) | 81.00 (+1.2) | 74.67 (+1.34) | 89.60 (-0.2) |
| SVAMP | SCW | 46.90 (+0.4) | 70.20 (+1.7) | 80.30 (+0.5) | 73.00 (-0.33) | 92.38 (+2.98) |
| StrategyQA | Top prob sample | 46.79 | 64.27 | 63.21 | 60.32 | 75.32 |
| StrategyQA | SC baseline | 48.91 | 67.98 | 66.81 | 63.32 | 79.18 |
| StrategyQA | CPW | 55.02 (+6.11) | 60.70 (-7.28) | 65.21 (-1.6) | 63.32 (+0.0) | 73.80 (-5.38) |
| StrategyQA | SCW | 62.44 (+13.53) | 65.35 (-2.63) | 74.70 (+7.89) | 71.47 (+8.15) | 79.68 (+0.5) |
