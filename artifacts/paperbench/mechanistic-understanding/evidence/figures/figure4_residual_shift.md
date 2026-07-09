# Figure 4: Linear Shift of Residual Streams Out of Toxic Regions

- **Source**: Figure 4, Section 5.2
- **Caption**: "Linear shift of residual streams out of toxic regions. Each point is a residual stream sampled from either x^{19}_{GPT} or x^{19}_{DPO}, using REALTOXICITYPROMPTS, projected onto 1) δ̄^{19}_x, the mean difference in residual streams, and 2) the principle component of the residual streams. Dotted lines indicate samples from the same prompt. Colors indicate whether each point activates MLP^{19}_{770}."
- **X-axis**: Projection onto mean residual stream shift direction δ̄^{19}_x
- **Y-axis**: Projection onto principal component of residual streams
- **Color coding**:
  - High activation (> 15): Points that strongly activate MLP.v19_770
  - Low activation (> 0): Points with some activation
  - None: Points with zero or negative activation

## Key Observations (qualitative, from figure description)

| Observation | Description |
|-------------|-------------|
| GPT2 clusters | Residual streams cluster in region with high/low activation of MLP.v19_770 |
| GPT2DPO clusters | Residual streams shift linearly in the δ̄x direction, landing in "None" activation region |
| Dotted lines | Connect same-prompt residual streams between GPT2 and GPT2DPO; all arrows point consistently in same direction |
| Activation drop | GPT2DPO points predominantly "None" activation; GPT2 points include "High" and "Low" activation |
| Shift direction | Consistent leftward/downward shift (in δ̄x direction) from GPT2 to GPT2DPO |

**Key findings**:
- The shift from GPT2 to GPT2DPO residual streams is approximately linear (consistent direction across all prompts).
- GPT2DPO residual streams at layer 19 consistently avoid the high-activation region of MLP.v19_770.
- The direction of shift is δ̄^{19}_x — the mean difference between GPT2DPO and GPT2 residual streams.

**Note**: Figure 4 is a 2D scatter plot. Exact coordinate values are not extractable from the paper; the qualitative findings are described above.
