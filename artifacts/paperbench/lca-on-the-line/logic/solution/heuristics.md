# Heuristics and Convergence Tricks

## H01: Temperature T=25 for soft label construction
- **Rationale**: A large temperature value assigns higher likelihood to semantically closer classes in the soft label matrix, boosting OOD generalization. Lower temperatures produce harder (more one-hot-like) soft labels that lose hierarchical signal. T=25 was found empirically to work well.
- **Sensitivity**: high
- **Bounds**: T must be positive. Higher T → softer labels → more hierarchical regularization but less ID accuracy signal. The paper uses T=25 specifically.
- **Code ref**: [src/execution/lca_alignment_loss.py]
- **Source**: Appendix E.2

## H02: Lambda=0.03 for balancing CE and soft loss
- **Rationale**: A smaller lambda scales down the standard cross-entropy loss relative to the soft LCA loss. This effectively gives more weight to the taxonomy alignment signal. Very small lambda prevents the CE loss from dominating and allows the model to learn from the full soft label distribution.
- **Sensitivity**: high
- **Bounds**: lambda ∈ (0, 1). Paper uses lambda=0.03. Note: total_loss = lambda * standard_loss + soft_loss, so lambda < 1 means soft_loss dominates numerically.
- **Code ref**: [src/execution/lca_alignment_loss.py]
- **Source**: Appendix E.2

## H03: Alpha interpolation for ID/OOD trade-off
- **Rationale**: Linear interpolation between CE-only weights and CE+soft weights allows selecting the optimal balance between ID accuracy preservation and OOD improvement. Alpha is selected on the ID validation set to avoid OOD data dependency.
- **Sensitivity**: medium
- **Bounds**: alpha ∈ {0.0, 0.1, 0.2, ..., 1.0}. alpha=1.0 corresponds to CE-only; alpha=0.0 corresponds to CE+soft only. The "no ID accuracy drop" setting uses the alpha that maximizes ID val Top-1; the "pro-OOD" setting may accept slight ID drops.
- **Code ref**: [src/execution/lca_alignment_loss.py]
- **Source**: Section 4.3.2, Table 9 (Appendix)

## H04: 9-layer K-means hierarchy (2^i clusters, i=1..9)
- **Rationale**: For 1000 ImageNet classes, 9 levels suffice since 2^9=512 < 1000 < 2^10=1024. Using hierarchical K-means (rather than full Ward-linkage) is computationally efficient and produces robust hierarchies. All class pairs share a base cluster level of 10 by default.
- **Sensitivity**: low
- **Bounds**: Number of levels n must satisfy 2^n < K (number of classes). For ImageNet: n=9. This produces a 9-level binary tree approximation of class relationships.
- **Code ref**: [src/execution/kmeans_hierarchy.py]
- **Source**: Appendix E.1

## H05: Min-max scaling for LCA before linear regression
- **Rationale**: LCA distance values are not bounded to [0,1] (unlike Top-1 accuracy). Min-max scaling is applied before fitting linear regressions to make the scale comparable and avoid artifacts. The paper uses min-max instead of the probit transform used by Miller et al. and Baek et al.
- **Sensitivity**: low
- **Bounds**: Applied only to LCA distance, not to Top-1 accuracy (already in [0,1]). Standard min-max: (x - min)/(max - min).
- **Code ref**: [src/execution/eval_metrics.py]
- **Source**: Section 4.2
