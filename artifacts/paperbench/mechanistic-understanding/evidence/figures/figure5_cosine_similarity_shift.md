---
# Figure 5: Cosine Similarity Between δMLP.v and δ^19_x

- **Source**: Figure 5, Section 5.2
- **Caption**: "The cosine similarity between δMLP.v and δ^19_x. Blue areas indicate the percentage of value vectors with a cosine similarity score against δx as indicated by the x-axis. Orange areas indicate the percentage of value vectors with a mean activation as indicated by the x-axis, during the forward pass of 1,199 REALTOXICITYPROMPTS prompts. Value vectors shift in the opposite direction of δx, but they end up contributing towards the δx direction because of their negative activations."
- **Conditions**: δx = mean residual stream shift at layer 19 mid; δMLP.v = difference in value vector weights (DPO - GPT2) for each neuron; cosine similarity computed per-neuron; 1,199 REALTOXICITYPROMPTS prompts. Shown for layers 0, 2, 4, 6, 8, 10, 12, 14, 16, 18.

## Axis Labels (per subplot)
- **X-axis (cos sim subplot, blue)**: Cosine similarity range [-0.2, 0.2]
- **X-axis (mean activation subplot, orange)**: Mean activation range [-0.2, 0.2]
- **Y-axis**: Proportion of value vectors (range 0.00 to 0.24)

## Qualitative Data (extracted from figure description)

| Layer | Blue (cos sim) Distribution | Orange (mean activation) Distribution | Key Observation |
|-------|----------------------------|--------------------------------------|-----------------|
| 0 | Near-Gaussian centered ~0 | Predominantly negative (< 0) | No systematic shift yet |
| 2 | Near-Gaussian centered ~0 | Predominantly negative | Slight negative skew begins |
| 4 | Slight negative skew | Predominantly negative | Shift beginning |
| 6 | Negative skew present | Predominantly negative | Growing negative shift |
| 8 | More negative skew | Predominantly negative | — |
| 10 | Clearly negative-skewed | Predominantly negative | Majority cos sim < 0 |
| 12 | Majority at negative values | Predominantly negative | Most δMLP.v antipodal to δx |
| 14 | Strong negative peak | Predominantly negative | — |
| 16 | Peak strongly negative | Predominantly negative | Almost all vectors antipodal |
| 18 | Majority ~-0.1 to -0.2 | Predominantly negative | Most vectors shift opposite to δx |

**Key finding**: As layers approach layer 19 (the target toxic layer), the cosine similarity distribution shifts from approximately Gaussian centered at 0 (early layers) to predominantly negative (late layers approaching 19). This means value vector weight changes (δMLP.v) are predominantly antipodal to the residual stream shift (δx). Combined with the orange distributions showing predominantly negative mean activations, this explains why: activating an antipodal δMLP.v with a negative scale factor yields a positive contribution toward δx. Similar patterns hold for other toxic layers (Appendix C, Figures 7-10 for layers 12, 14, 16, 18).
