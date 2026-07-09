---
# Figure 4: Linear Shift of Residual Streams Out of Toxic Regions

- **Source**: Figure 4, Section 5.2
- **Caption**: "Linear shift of residual streams out of toxic regions. Each point is a residual stream sampled from either x^19_GPT or x^19_DPO, using REALTOXICITYPROMPTS, projected onto 1) δ̄^19_x, the mean difference in residual streams, and 2) the principle component of the residual streams. Dotted lines indicate samples from the same prompt. Colors indicate whether each point activates MLP^19_770."
- **Conditions**: 50 samples (30 shown in figure per model, from pca.sync.py); residual streams at layer 19 mid (after attention, before MLP); projected onto 2D: (mean δx direction, first PC). Activation thresholds: High = activation >15, Low = activation >0, None = activation ≤0.

## Axis Labels
- **X-axis**: "Shift Component" (projection onto mean δx = x_DPO - x_GPT2)
- **Y-axis**: "Principle Component" (first PC of all residual streams)
- **Color encoding**: High (>15): red; Low (>0): orange; None: green
- **Marker encoding**: GPT2 = circles (o), DPO = triangles (^)
- **Lines**: Dotted lines connect GPT2 and DPO residual streams from the same prompt

## Qualitative Data (from figure description, not extractable as exact coordinates)

| Property | GPT2 | DPO |
|----------|------|-----|
| Most points activate MLP.v19_770 | Yes (many red/orange) | No (mostly green) |
| Shift along X-axis (Shift Component) | Reference cluster | Consistently shifted right/positive relative to GPT2 |
| Activation level | Mix of High and Low | Predominantly None |
| Paired shift direction | — | Consistent (dotted lines roughly parallel) |

**Key finding**: There is a consistent linear shift from GPT2 to DPO residual streams along the mean difference direction (δx). DPO residual streams have substantially fewer high-activation (red) and low-activation (orange) points and more non-activating (green) points, confirming that the offset learned by DPO moves the residual stream out of the γ(MLP.k^19_770) activation region.
