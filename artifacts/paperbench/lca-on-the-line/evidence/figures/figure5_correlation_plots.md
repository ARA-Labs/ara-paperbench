---
# Figure 5: OOD Top-1/Top-5 Correlation with ID Top-1 and ID LCA (75 Models, 4 OOD Datasets)
- **Source**: Figure 5, Section 4.1
- **Caption**: "Correlating OOD Top-1/Top-5 accuracy (VM+VLM, 75 models) on 4 ImageNet-OOD datasets visualizing Table 2. The plots clearly demonstrate that the in-distribution LCA distance has a stronger correlation with the model's OOD performance across all OOD datasets than accuracy-on-the-line. Each plot's x-axis represents the OOD dataset metric and y-axis represents ImageNet ID test Top-1 accuracy (left) and LCA (right); Red line (Pink dots: VMs and Red dots: VLMs) represents in-distribution classification accuracy (Top-1); Green line (Green dots: VMs and Blue dots: VLMs) denotes in-distribution taxonomic distance (LCA)."
- **Panel layout**: 8 panels (2 rows × 4 columns)
  - Row 1 (OOD Top-1 on X-axis): ImageNet-S, ImageNet-R, ImageNet-A, ObjectNet
  - Row 2 (OOD Top-5 on X-axis): ImageNet-S, ImageNet-R, ImageNet-A, ObjectNet
  - For each panel: Y-axis = ImageNet ID Top-1 (red line) OR ImageNet ID LCA (green line)

## Quantitative Summary (from Table 2)

### OOD Top-1 Panels

| OOD Dataset | ID Top-1 R² | ID Top-1 PEA | ID LCA R² | ID LCA PEA |
|------------|------------|-------------|----------|-----------|
| ImageNet-S | 0.075 | 0.275 | 0.816 | 0.903 |
| ImageNet-R | 0.020 | 0.140 | 0.779 | 0.883 |
| ImageNet-A | 0.009 | 0.094 | 0.704 | 0.839 |
| ObjectNet | 0.273 | 0.522 | 0.915 | 0.956 |

### OOD Top-5 Panels

| OOD Dataset | ID Top-1 R² | ID Top-1 PEA | ID LCA R² | ID LCA PEA |
|------------|------------|-------------|----------|-----------|
| ImageNet-S | 0.052 | 0.229 | 0.811 | 0.901 |
| ImageNet-R | 0.004 | 0.060 | 0.738 | 0.859 |
| ImageNet-A | 0.013 | 0.115 | 0.799 | 0.894 |
| ObjectNet | 0.262 | 0.512 | 0.924 | 0.961 |

*Note: Exact per-model scatter plot coordinates for all 75 models are not tabulated in paper. The figure shows qualitative clustering of VM (pink/green dots) vs. VLM (red/blue dots) populations.*
