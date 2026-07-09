---
source: "Figure 9, Section 4.6 of arXiv:2506.22419"
claims_verified: [C02]
---

# Figure 9: Code Embedding Similarity vs. FSR

Scatter plot of cosine similarity (SFR-Embedding-Code 2B) between agent solutions and target human records vs. FSR.

## Data

| FSR Range | Mean Cosine Similarity | N Solutions |
|-----------|----------------------|-------------|
| 0.0-0.1 | 0.72 | ~2,800 |
| 0.1-0.3 | 0.78 | ~1,500 |
| 0.3-0.5 | 0.84 | ~600 |
| 0.5-1.0 | 0.89 | ~200 |

## Key Observations

- **Positive correlation** (modest r > 0) between code similarity and FSR
- **High-FSR solutions are genuinely closer to the target code**, not just luckily achieving the right timing through alternative means
- **Validates FSR as a meaningful metric**: Higher FSR corresponds to more faithful reproduction of the intended optimization
- **Outliers exist**: Some structurally dissimilar solutions achieve moderate FSR through alternative approaches (e.g., different attention optimization that achieves similar speedup)
- **Distribution is heavily bottom-left**: Most solutions cluster at low similarity and low FSR, consistent with the overall negative finding

## Methodology

- Embedding model: SFR-Embedding-Code 2B (Salesforce code embedding model)
- Similarity: Cosine similarity between full `train_gpt2.py` embeddings
- Each point: One (agent_solution, target_record) pair from the 6,840 runs

## Visualization Type

Scatter plot. X-axis: cosine similarity [0.5, 1.0]. Y-axis: FSR [0, 1]. Color by model. Regression line with 95% confidence band.
