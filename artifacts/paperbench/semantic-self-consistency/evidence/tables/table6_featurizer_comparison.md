---
# Table 6: Featurizer Average Distance Comparison
- **Source**: Table 6, Appendix G.2
- **Caption**: "Featurizers finetuned on similar distributions tend to pack answers more tightly together"
- **Experimental conditions**: Arithmetic reasoning samples only (AQuA-RAT/SVAMP subset); average pairwise Euclidean distance between all embedding pairs (lower = tighter clusters = better fit).

| BERT-Model | avg distance (↓) | Delta vs RoBERTa |
|-----------|-----------------|-----------------|
| RoBERTa | 48.697 | — |
| MathBERT | 45.892 | -2.8 |
| SciBERT | 45.281 | -3.4 |

**Key finding**: SciBERT achieves the lowest average pairwise distance (45.281), followed by MathBERT (45.892), and RoBERTa (48.697). Domain-specific fine-tuning reduces inter-embedding distances, enabling better discrimination between similar and dissimilar reasoning paths.
