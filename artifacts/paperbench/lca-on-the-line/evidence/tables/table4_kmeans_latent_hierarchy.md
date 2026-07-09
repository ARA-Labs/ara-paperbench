---
# Table 4: Correlation Between LCA/Top1 and OOD Top1 Across 75 Latent Hierarchies
- **Source**: Table 4, Section 4.3.1
- **Caption**: "Correlation measurement (PEA) between LCA/Top1 and OOD Top1 across 75 latent hierarchies derived from K-means. Our latent hierarchy construction is robust across 75 different source pretrained models."
- **Conditions**: 75 latent hierarchies (one per pretrained model); PEA = Pearson correlation coefficient; computed from K-means clustering of per-class average features at 9 levels; Baseline = ID Top1 PEA from Table 2

| Element | Source | ImgN-v2 PEA | ImgN-S PEA | ImgN-R PEA | ImgN-A PEA | ObjNet PEA |
|---------|--------|------------|-----------|-----------|-----------|-----------|
| Baseline | Top1 → Top1 | 0.980 | 0.275 | 0.140 | 0.094 | 0.522 |
| WordNet | LCA → Top1 | 0.582 | 0.903 | 0.883 | 0.839 | 0.956 |
| Mean (75 latent hierarchies) | LCA → Top1 | 0.815 | 0.773 | 0.712 | 0.662 | 0.930 |
| Min (75 latent hierarchies) | LCA → Top1 | 0.721 | 0.715 | 0.646 | 0.577 | 0.890 |
| Max (75 latent hierarchies) | LCA → Top1 | 0.863 | 0.829 | 0.780 | 0.717 | 0.952 |
| Std (75 latent hierarchies) | LCA → Top1 | 0.028 | 0.022 | 0.027 | 0.025 | 0.010 |
