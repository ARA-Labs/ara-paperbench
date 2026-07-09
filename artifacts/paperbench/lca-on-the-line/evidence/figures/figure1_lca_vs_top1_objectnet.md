---
# Figure 1: LCA Distance vs. OOD Accuracy — Unified vs. Divergent Trends
- **Source**: Figure 1, Section 1 (Introduction)
- **Caption**: "Correlation between LCA distance and out-of-distribution (OOD) performance in Vision and Vision-Language Models (VLMs). In both panels, the X-axis represents the top-1 accuracy on ObjectNet (OOD test dataset). The Y-axes depict the top-1 accuracy (left-axis) and LCA distance (right-axis) on ImageNet (ID test dataset). The left plot reveals a divergent trend where Vision Models (VMs) show a trade-off between OOD and ID accuracy, while VLMs tend to maintain higher OOD accuracy regardless of ID performance. The right plot demonstrates a unified, strong positive correlation between LCA distance and OOD accuracy."
- **Axis labels**: X-axis = ObjectNet Top-1 accuracy; Left Y-axis = ImageNet Top-1 accuracy; Right Y-axis = ImageNet LCA distance
- **Key observations**:
  - Left panel (ID Top-1 vs. OOD): VMs form one linear cluster (positive slope); VLMs form a separate cluster above and to the right (higher OOD at similar or lower ID accuracy) — two separate trends
  - Right panel (ID LCA vs. OOD): Both VMs and VLMs align on a single negative-slope line (lower LCA = higher OOD accuracy) — unified trend

## Extracted Data Points (Table 1 models, ObjectNet OOD axis)

| Model | Family | ObjectNet Top1 (X) | ImageNet Top1 (Y_left) | ImageNet LCA (Y_right) |
|-------|--------|--------------------|------------------------|------------------------|
| ResNet18 | VM | 0.272 | 0.698 | 6.643 |
| ResNet50 | VM | 0.316 | 0.733 | 6.539 |
| CLIP_RN50 | VLM | 0.398 | 0.579 | 6.327 |
| CLIP_RN50x4 | VLM | 0.504 | 0.641 | 6.166 |

*(Full 75-model scatter plot data not tabulated in paper — Figure is qualitative illustration with quantitative data in Tables 1 and 2)*
