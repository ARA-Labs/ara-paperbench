# Figure 4: Linear Shift of Residual Streams Out of Toxic Regions

- **Source**: Figure 4, Section 5.2
- **Caption**: "Linear shift of residual streams out of toxic regions. Each point is a residual stream sampled from either x^19_GPT or x^19_DPO, using REALTOXICITYPROMPTS, projected onto 1) δ̄^19_x, the mean difference in residual streams, and 2) the principle component of the residual streams. Dotted lines indicate samples from the same prompt. Colors indicate whether each point activates MLP^19_770."
- **Experimental conditions**: Residual streams at layer 19 (ℓ=19, after attention, before MLP) from GPT2 and GPT2DPO on RealToxicityPrompts challenge set. 2D projection: x-axis = mean shift direction $\bar{\delta}^{19}_x$; y-axis = first principal component of residual streams. Color coding: High activation (>15) = one color, Low activation (>0) = second color, None = third color. Points from same prompt connected by dotted lines.

## Key Observations (Qualitative from Scatter Plot)

| Property | Description |
|----------|-------------|
| GPT2 points (pre-DPO) | Clustered in region with frequent High/Low activations of MLP.v19_770 |
| GPT2DPO points (post-DPO) | Consistently shifted along x-axis (δ̄^19_x direction); predominantly "None" activation |
| Shift direction | Consistent linear shift; all GPT2DPO points shifted ~same amount in x-axis direction |
| Activation change | GPT2: many High/Low activation points; GPT2DPO: predominantly None activation |
| Dotted lines | Connect paired prompts; show consistent shift magnitude and direction across prompts |

**Notes**:
- Exact coordinate values not reported in paper text; figure is a scatter plot.
- Key finding: Residual streams from GPT2DPO show a consistent, approximately linear shift in the $\bar{\delta}^{19}_x$ direction, moving away from the activation region of MLP.v19_770.
- See Appendix B (Figure 6) for similar results at layers 12, 18, and 13.
