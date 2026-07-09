---
# Table 6: Featurizer Embedding Distance Comparison
- **Source**: Table 6, Appendix G.2
- **Caption**: "Featurizers finetuned on similar distributions tend to pack answers more tightly together"
- **Conditions**: Average pairwise Euclidean distance computed on arithmetic reasoning samples; lower distance = tighter clustering = better domain alignment; delta shown relative to RoBERTa

| BERT-Model | avg distance (↓) |
|-----------|----------------|
| RoBERTa | 48.697 |
| MathBERT | 45.892 (-2.8) |
| SciBERT | 45.281 (-3.4) |
