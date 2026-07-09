# Table 4: Correlation Measurement (PEA) Between LCA/Top1 and OOD Top1 Across 75 Latent Hierarchies
- **Source**: Table 4, Section 4.3.1
- **Caption**: "Correlation measurement (PEA) between LCA/Top1 and OOD Top1 across 75 latent hierarchies derived from K-means. Our latent hierarchy construction is robust across 75 different source pretrained models: For each source model, we extracted average class features and applied K-means clustering to construct a latent hierarchy. We then calculated the LCA distance based on each hierarchy, and aggregated the statistical metric of the 75 groups' Pearson correlation coefficient (PEA) to OOD performance (essentially 75 groups of data from Table 2). We observe that LCA reliably tracks OOD performance even when using different class taxonomies."
- **Conditions**: 75 latent hierarchies (one per source model); PEA computed between LCA distance (under each latent hierarchy) and OOD Top-1 across 75 evaluation models

| Element | OOD | ImgN-v2 PEA | ImgN-S PEA | ImgN-R PEA | ImgN-A PEA | ObjNet PEA |
|---------|-----|------------|----------|----------|----------|----------|
| Baseline Top1 | Top1 | 0.980 | 0.275 | 0.140 | 0.094 | 0.522 |
| WordNet LCA | Top1 | 0.582 | 0.903 | 0.883 | 0.839 | 0.956 |
| LCA Mean (75 latent hierarchies) | Top1 | 0.815 | 0.773 | 0.712 | 0.662 | 0.930 |
| LCA Min (75 latent hierarchies) | Top1 | 0.721 | 0.715 | 0.646 | 0.577 | 0.890 |
| LCA Max (75 latent hierarchies) | Top1 | 0.863 | 0.829 | 0.780 | 0.717 | 0.952 |
| LCA Std (75 latent hierarchies) | Top1 | 0.028 | 0.022 | 0.027 | 0.025 | 0.010 |
