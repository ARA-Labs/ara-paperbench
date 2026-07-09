# Claims

## C01: LCA-on-the-Line — ID LCA distance linearly predicts OOD accuracy across VMs and VLMs
- **Statement**: The in-distribution LCA distance (using information content) on ImageNet strongly and linearly correlates with OOD Top-1 accuracy for both VMs and VLMs combined (R²>0.7, PEA>0.7) on all four severely shifted OOD datasets (ImageNet-S, ImageNet-R, ImageNet-A, ObjectNet), while in-distribution Top-1 accuracy fails to unify both families (R²≈0 on ImageNet-A for all 75 models combined).
- **Status**: supported
- **Falsification criteria**: If the Pearson correlation (|PEA|) between ID LCA distance and OOD Top-1 accuracy falls below 0.7 for any of the four severely shifted OOD datasets when evaluated on 75 mixed VM+VLM models, or if ID Top-1 accuracy shows comparable or higher correlation than LCA on those same datasets, this claim is refuted.
- **Proof**: [E01]
- **Dependencies**: None
- **Tags**: LCA distance, OOD generalization, correlation, cross-modal evaluation, Accuracy-on-the-Line

## C02: Latent hierarchies via K-means clustering provide robust LCA-based OOD predictors
- **Statement**: Class taxonomies constructed from pretrained model features using 9-layer K-means clustering yield LCA distances that still correlate with OOD performance (mean PEA > 0.66 across 75 source models on ImageNet-S/R/A/ObjectNet), though slightly lower than WordNet-based LCA. This enables LCA evaluation on datasets without predefined hierarchies.
- **Status**: supported
- **Falsification criteria**: If the mean PEA between latent-hierarchy LCA distance and OOD Top-1 accuracy across 75 source models falls below 0.5 on more than one of the four severely shifted OOD datasets, or if the variance is so high that the minimum PEA falls below 0.3, this claim is refuted.
- **Proof**: [E03]
- **Dependencies**: C01
- **Tags**: K-means, latent hierarchy, taxonomy construction, robustness

## C03: LCA soft labels improve OOD generalization without sacrificing ID accuracy
- **Statement**: Augmenting the standard cross-entropy loss with an auxiliary LCA soft label loss (and applying linear weight interpolation) consistently improves OOD Top-1 accuracy across all tested backbones (ResNet-18/50, ViT-B/L, ConvNext, Swin Transformer) on at least 3/4 severely shifted OOD datasets without reducing ID ImageNet Top-1 accuracy compared to cross-entropy-only baseline.
- **Status**: supported
- **Falsification criteria**: If any backbone shows degraded OOD performance on 2 or more OOD datasets compared to the CE-only baseline when using the "no ID accuracy drop" setting, this claim is refuted. If ID accuracy consistently drops (>0.5%) when maintaining OOD improvements, this claim is weakened.
- **Proof**: [E04]
- **Dependencies**: C01
- **Tags**: soft labels, linear probing, OOD generalization improvement, taxonomy alignment, weight interpolation

## C04: Models with lower LCA distance (better mistakes) tend to generalize better to OOD data
- **Statement**: In a controlled simulation with known data-generating processes, a model trained on hierarchy-supporting transferable causal features (lower LCA distance) achieves better OOD accuracy than a model trained on non-hierarchy-supporting confounding features (higher LCA distance), even when the confounding-feature model achieves better ID Top-1 accuracy. This provides causal justification for the LCA-OOD correlation.
- **Status**: supported
- **Falsification criteria**: In the simulation described in Appendix C, if the model using confounding features (model g) achieves equal or better OOD accuracy than the model using causal features (model f), this claim is refuted.
- **Proof**: [E06]
- **Dependencies**: C01
- **Tags**: simulation, causal features, transferable features, confounding features

## C05: Taxonomy-aligned prompt engineering for VLMs improves OOD generalization
- **Statement**: For zero-shot VLM prediction, providing the full hierarchical taxonomy relationship in the prompt (e.g., "A, which is a type of B, which is a type of C") significantly improves Top-1 accuracy and reduces cross-entropy loss on all tested OOD datasets compared to baseline prompts that only name the class, and outperforms partial hierarchy information (Stack Parent) or incorrect hierarchy information (Shuffle Parent).
- **Status**: supported
- **Falsification criteria**: If the Taxonomy Parent prompt does not outperform Baseline (class-name only) on at least 4/5 datasets (including OOD), or if Shuffle Parent performs comparably to Taxonomy Parent, this claim is refuted.
- **Proof**: [E05]
- **Dependencies**: C01
- **Tags**: prompt engineering, VLM, zero-shot, taxonomy alignment, CLIP
