---
# Figure 4: Linear Shift of Residual Streams Out of Toxic Regions (PCA)

**Source**: Figure 4, Section 5.2
**Claims**: C06, C07

## Description
2D scatter plot of residual streams from GPT2 and GPT2_DPO at layer 19, projected onto two axes:
1. X-axis: "Shift Component" — mean difference in residual streams δ̄_x^{19}
2. Y-axis: "Principle Component" — first principal component of all residual streams

Dotted lines connect residual streams from the same prompt (GPT2 → GPT2_DPO).
Colors indicate whether each point activates MLP.v_{770}^{19}: High (>15), Low (>0), None (≤0).

## Experimental Setup (from pca.sync.py)
- `sample_size = 50` prompts (first 50 from 1,199 REALTOXICITYPROMPTS)
- `batch_size = 4`
- `num_samples = 30` plotted in main figure
- Layer: 19 (most toxic layer)
- Residual accessed via `blocks.19.hook_resid_mid[:, -1, :]`
- PCA computed via `torch.pca_lowrank` on normalized concatenated residuals
- Normalization: subtract mean, divide by std (computed on combined GPT2 + DPO residuals)
- Projection matrix: `[diff_mean.unsqueeze(-1), V][:, :2]`

## Key Observations

### Geometric Structure

| Observation | GPT2 (circles) | GPT2_DPO (triangles) |
|-------------|----------------|----------------------|
| Position on shift component (x-axis) | Negative side | Positive side (shifted) |
| Activation of MLP.v_{770}^{19} | Predominantly High (>15) or Low (>0) | Predominantly None (≤0) |
| Connection via dotted lines | Consistent parallel shift | Parallel, not random scattering |

### Activation Thresholds and Color Coding

| Activation Level | Threshold | Color | Expected Model |
|-----------------|-----------|-------|----------------|
| High | > 15 | Red | Mostly GPT2 |
| Low | > 0 | Orange | Mostly GPT2 |
| None | ≤ 0 | Green | Mostly GPT2_DPO |

- Sample size: 30 prompts plotted (from first 50 of 1,199 REALTOXICITYPROMPTS)
- Consistent linear shift confirms δ_x as a distributed learned offset, not random noise

## Appendix B
Figure 6 shows similar patterns for layers 12, 18, and 13 (next three most toxic layers after 19), confirming the finding generalizes across layers.
