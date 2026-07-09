---
# Figure 5: Cosine Similarity between δ_MLP.v and δ_x, and Mean Activations

**Source**: Figure 5, Section 5.2
**Claims**: C07

## Description
A 2×5 grid of subplots (10 panels) showing, for each of layers {0, 2, 4, 6, 8, 9, 11, 13, 15, 17}:
- **Blue histogram**: Distribution of cosine similarities between δ_MLP.v (shift in value vectors) and δ_x^{19_mid} (mean shift in residual stream at layer 19 mid-layer)
- **Orange histogram**: Distribution of mean activations of value vectors (from 1,199 REALTOXICITYPROMPTS prompts)

Both plotted as probability histograms on separate x-axes sharing the y-axis.

## Experimental Setup (from resid_diff_plot.sync.py)
- `layer_of_interest = 18` (used for delta_x; corresponds to layer 19 in paper notation since 0-indexed)
- `sublayers = [0, 2, 4, 6, 8, 9, 11, 13, 15, 17]` (the 10 layers analyzed)
- Delta residual: `x_DPO^{layer_mid} - x_GPT2^{layer_mid}` at position [:, -1, :]
- Delta MLP.v: `model.blocks[l].mlp.W_out - gpt2.blocks[l].mlp.W_out` (shape [d_mlp=4096, d_model=1024])
- Cosine similarity: `F.cosine_similarity(mlp_diffs[layer], mean_delta_x.unsqueeze(0), dim=1)` for each of 4096 vectors
- Mean activations: `blocks.{layer}.mlp.hook_post` over all prompts, averaged

## Key Observations

### Cosine Similarity Distribution by Layer

| Layer | Distribution Shape | Majority Cosine Sim | Interpretation |
|-------|-------------------|---------------------|----------------|
| 0 | Gaussian centered at 0 | ~0 | Random directions; no toxicity correlation |
| 2 | Gaussian centered at 0 | ~0 | Same pattern |
| 4 | Gaussian centered at 0 | ~0 | Same pattern |
| 6 | Slightly skewed negative | slightly < 0 | Beginning of directional shift |
| 8 | Skewed negative | negative | More vectors opposite to δ_x |
| 9 | Concentrated negative | negative | Increasing antipodal concentration |
| 11 | Concentrated negative | ≪ 0 | Strong negative cosine similarity |
| 13 | Concentrated near -1 | near -1 | Majority in opposite direction of δ_x |
| 15 | Concentrated near -1 | near -1 | Strong antipodal relationship |
| 17 | Concentrated near -1 | approaching -1 | Majority near -1 as layer approaches 19 |

### Mean Activation Distribution (All Layers)

| Metric | Value | Implication |
|--------|-------|-------------|
| Majority of mean activations | Negative (near 0) | Neurons inactive under GeLU |
| Distribution shape | Concentrated near 0, slightly negative side | Sparse neuron phenomenon |
| Layers affected | All layers 0–17 | Consistent sparsity throughout model |

### Causal Explanation Table

| Step | Observed Fact | Mechanistic Effect |
|------|--------------|-------------------|
| 1 | Most GeLU neurons inactive | Small negative activation values (not exactly 0) |
| 2 | DPO shifts value vectors opposite to δ_x | Negative cosine similarity: cos(δ_MLP.v, δ_x) < 0 |
| 3 | Inactive neurons multiply shifted vectors by negative scalar | Direction flips: negative × negative = positive |
| 4 | Cumulative effect across all layers | Sufficient total δ_x to bypass toxic activation regions γ(MLP.kToxic) |

## Appendix C
Figures 7-10 show the same pattern for layers 12, 14, 16, 18 (showing different reference layers for δ_x), confirming the mechanism is consistent across the model.
