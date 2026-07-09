# Figure 5: Correlating OOD Top-1/Top-5 Accuracy Across 75 Models
- **Source**: Figure 5, Section 4.1
- **Caption**: "Correlating OOD Top-1/Top-5 accuracy (VM+VLM, 75 models) on 4 ImageNet-OOD datasets visualizing Table 2. The plots clearly demonstrate that the in-distribution LCA distance has a stronger correlation with the model's OOD performance across all OOD datasets than accuracy-on-the-line (Miller et al., 2021). Each plot's x-axis represents the OOD dataset metric (with OOD Top-1 in the top row, and OOD Top-5 accuracy in the bottom row) and y-axis represents ImageNet ID test Top-1 accuracy (left) and LCA (right); Red line (Pink dots: VMs and Red dots: VLMs) represents in-distribution classification accuracy (Top-1); Green line (Green dots: VMs and Blue dots: VLMs) denotes in-distribution taxonomic distance (LCA). As interpreted in Figure 1, accuracy-on-the-line only explains generalization of models within similar settings (VMs or VLMs), but does not unify both settings."
- **Axis labels**:
  - Columns: ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, ObjectNet
  - Rows: OOD Top-1 accuracy, OOD Top-5 accuracy
  - Y-axis: ImageNet ID Top-1 accuracy (red line) or ID LCA distance (green line)

## Extracted Correlation Values (from Table 2)
All values are absolute correlations (R², PEA) for 75 combined VM+VLM models:

### OOD Top-1 Accuracy

| ID Metric | ImgN-S R² | ImgN-S PEA | ImgN-R R² | ImgN-R PEA | ImgN-A R² | ImgN-A PEA | ObjNet R² | ObjNet PEA |
|-----------|---------|----------|---------|----------|---------|----------|---------|----------|
| ID Top-1 (red line) | 0.075 | 0.275 | 0.020 | 0.140 | 0.009 | 0.094 | 0.273 | 0.522 |
| ID LCA (green line) | 0.816 | 0.903 | 0.779 | 0.883 | 0.704 | 0.839 | 0.915 | 0.956 |

### OOD Top-5 Accuracy

| ID Metric | ImgN-S R² | ImgN-S PEA | ImgN-R R² | ImgN-R PEA | ImgN-A R² | ImgN-A PEA | ObjNet R² | ObjNet PEA |
|-----------|---------|----------|---------|----------|---------|----------|---------|----------|
| ID Top-1 (red line) | 0.052 | 0.229 | 0.004 | 0.060 | 0.013 | 0.115 | 0.262 | 0.512 |
| ID LCA (green line) | 0.811 | 0.901 | 0.738 | 0.859 | 0.799 | 0.894 | 0.924 | 0.961 |

**Key finding**: In every cell, ID LCA dramatically outperforms ID Top-1 in correlation with OOD accuracy (except for ImageNet-v2, not shown here).
