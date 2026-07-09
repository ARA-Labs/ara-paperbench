# Figure 1: Correlation Between LCA Distance and OOD Performance
- **Source**: Figure 1, Section 1 (Introduction)
- **Caption**: "Correlation between LCA distance and out-of-distribution (OOD) performance in Vision and Vision-Language Models (VLMs). In both panels, the X-axis represents the top-1 accuracy on ObjectNet (OOD test dataset). The Y-axes depict the top-1 accuracy (left-axis) and LCA distance (right-axis) on ImageNet (ID test dataset). The left plot reveals a divergent trend where Vision Models (VMs) show a trade-off between OOD and ID accuracy, while VLMs tend to maintain higher OOD accuracy regardless of ID performance. The right plot demonstrates a unified, strong positive correlation between LCA distance and OOD accuracy for both VMs and VLMs."
- **Axis labels**:
  - X-axis (both panels): ImageNet-ObjectNet Top-1 OOD accuracy
  - Y-axis (left panel): ImageNet ID Top-1 accuracy
  - Y-axis (right panel): ImageNet ID LCA distance

## Left Panel (Accuracy-on-the-Line, two separate trends)
Description: Scatter plot showing two distinct linear trends (one for VMs, one for VLMs) when plotting ImageNet ID Top-1 accuracy vs ObjectNet OOD Top-1 accuracy. Exact scatter coordinates not tabulated in paper; representative points from Table 1:

| Model | ObjectNet Top1 (OOD) | ImageNet Top1 (ID) | Family |
|-------|---------------------|-------------------|--------|
| ResNet18 | 0.272 | 0.698 | VM |
| ResNet50 | 0.316 | 0.733 | VM |
| CLIP_RN50 | 0.398 | 0.579 | VLM |
| CLIP_RN50x4 | 0.504 | 0.641 | VLM |

**Key observation**: VLMs (right cluster) achieve higher ObjectNet accuracy than VMs with similar or higher ImageNet accuracy → two divergent trends.

## Right Panel (LCA-on-the-Line, unified single trend)
Description: Scatter plot showing a single unified downward-sloping linear trend when plotting ImageNet ID LCA distance vs ObjectNet OOD Top-1 accuracy. Representative points from Table 1:

| Model | ObjectNet Top1 (OOD) | ImageNet LCA distance (ID) | Family |
|-------|---------------------|--------------------------|--------|
| ResNet18 | 0.272 | 6.643 | VM |
| ResNet50 | 0.316 | 6.539 | VM |
| CLIP_RN50 | 0.398 | 6.327 | VLM |
| CLIP_RN50x4 | 0.504 | 6.166 | VLM |

**Key observation**: All 75 models (VMs and VLMs) fall on a single negative-slope line — lower LCA distance (better mistakes) → higher OOD accuracy. R²=0.915, PEA=0.956 (from Table 2, ObjNet column).
