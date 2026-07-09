# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_model_performance.md](tables/table1_model_performance.md) | Table 1, §4.1 | C01 | LCA distance (↓) and Top-1 accuracy (↑) for ResNet18, ResNet50, CLIP_RN50, CLIP_RN50x4 across all 6 datasets, showing that VLMs have lower LCA (better mistakes) and higher OOD accuracy despite lower ID Top-1. |
| [tables/table2_correlation.md](tables/table2_correlation.md) | Table 2, §4.1 | C01 | R² and PEA of ID LCA/Top1 vs OOD Top1/Top5 across all 75 models (and VMs-only/VLMs-only subgroups), demonstrating LCA superiority over Top-1 for cross-modal OOD prediction. |
| [tables/table3_mae_prediction.md](tables/table3_mae_prediction.md) | Table 3, §4.2 | C01 | MAE (↓) comparison of OOD error prediction across 5 methods (ID Top1, AC, Aline-D, Aline-S, ID LCA) on 5 OOD datasets, showing ID LCA achieves best MAE on ImgN-S, ImgN-A, and ObjectNet. |
| [tables/table4_kmeans_latent.md](tables/table4_kmeans_latent.md) | Table 4, §4.3.1 | C02 | PEA statistics (mean, min, max, std) across 75 latent hierarchies from K-means vs WordNet baseline vs Top-1 baseline, demonstrating robustness of latent hierarchy LCA. |
| [tables/table5_soft_labels_wordnet.md](tables/table5_soft_labels_wordnet.md) | Table 5, §4.3.2 | C03 | Top-1 accuracy for 6 backbone models (baseline vs LCA soft loss + interpolation) on 6 datasets with WordNet hierarchy, showing consistent OOD improvements without ID accuracy degradation. |
| [tables/table6_soft_labels_latent.md](tables/table6_soft_labels_latent.md) | Table 6, §4.3.2 | C02, C03 | Top-1 accuracy for ResNet-18 linear probe with latent hierarchies from 4 source models vs WordNet, showing VLM-sourced hierarchies produce better soft labels. |
| [tables/table7_simulation.md](tables/table7_simulation.md) | Table 7, Appendix C | C04 | Simulation results over 100 trials: ID Top-1 error, ID LCA distance, OOD Top-1 error for causal-feature model f vs confounding-feature model g, validating LCA as OOD predictor. |
| [tables/table8_lca_elca.md](tables/table8_lca_elca.md) | Table 8, Appendix D.3 | C01 | LCA and ELCA measurements for ResNet18, ResNet50, CLIP_RN50, CLIP_RN50x4 across all 6 datasets, showing both metrics track OOD performance. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure1_correlation_plot.md](figures/figure1_correlation_plot.md) | Figure 1, §1 | C01 | Scatter plot data showing divergent VM/VLM trends with ID Top-1 (left) vs unified single trend with ID LCA distance (right) for ObjectNet OOD accuracy across ~75 models. |
| [figures/figure5_full_correlation.md](figures/figure5_full_correlation.md) | Figure 5, §4.1 | C01 | Eight-panel correlation plots (Top-1 and LCA vs OOD Top-1 and Top-5 for ImgN-S/R/A/ObjectNet) across 75 models, quantitatively supporting the LCA-on-the-Line framework. |
