# Figure 5: Cosine Similarity Between δMLP.v and δ19_x

- **Source**: Figure 5, Section 5.2
- **Caption**: "The cosine similarity between δMLP.v and δ^{19}_x. Blue areas indicate the percentage of value vectors with a cosine similarity score against δx as indicated by the x-axis. Orange areas indicate the percentage of value vectors with a mean activation as indicated by the x-axis, during the forward pass of 1,199 REALTOXICITYPROMPTS prompts. Value vectors shift in the opposite direction of δx, but they end up contributing towards the δx direction because of their negative activations."
- **X-axis (blue)**: Cosine similarity values from −0.2 to +0.2 (and beyond)
- **X-axis (orange)**: Mean activation values from −0.2 to +0.2
- **Y-axis**: Proportion of value vectors (0.00–0.24)
- **Layers shown**: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18 (10 subplots)
- **Prompts**: 1,199 RealToxicityPrompts challenge set

## Key Patterns Per Layer Group

| Layer(s) | Blue (cos sim) distribution | Orange (mean activation) distribution |
|----------|----------------------------|---------------------------------------|
| 0 | Approximately symmetric/Gaussian centered near 0 | Mostly negative, roughly centered near -0.05 |
| 2–4 | Slight shift toward negative cosine similarities | Predominantly negative activations |
| 6–8 | Majority of vectors begin shifting toward negative cos sim | Large proportion with negative activations |
| 10–12 | Growing proportion with cos sim < −0.1 | Most activations negative (< 0) |
| 14–16 | Majority of vectors with cos sim in range −0.1 to −0.2 | Predominantly negative activations |
| 18 | Largest proportion with most negative cosine similarities | Near-universal negative activations |

## Key Quantitative Observations

| Observation | Value |
|-------------|-------|
| Layer 0 distribution center (cos sim) | ≈ 0 (symmetric) |
| Layer 18 distribution mode (cos sim) | ≈ −0.15 to −0.20 |
| Proportion of vectors with negative activation (all layers) | Majority (> 50%) |
| Direction of δMLP.v relative to δx | Predominantly antipodal (negative cos sim) |

**Key findings**:
1. At layer 0, cosine similarities between δMLP.v and δ^{19}_x are near-zero (no systematic relationship).
2. As layers approach layer 19, the proportion of value vectors with negative cosine similarity with δ^{19}_x increases substantially.
3. Most value vectors have negative mean activations across all layers, confirming GeLU sparsity.
4. The negative activations explain why δMLP.v (antipodal to δx) ultimately contributes to the δx direction: m_i ≈ negative ⟹ m_i * δv_i flips direction.

**Note**: Exact proportions are approximate readings from multi-panel histogram. ≈ notation used throughout.
