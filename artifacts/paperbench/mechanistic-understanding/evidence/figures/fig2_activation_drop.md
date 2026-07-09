---
# Figure 2: Mean Activations for MLP.vToxic Vectors Before and After DPO

**Source**: Figure 2, Section 5.2
**Claims**: C06

## Description
Bar chart showing mean activation values m_i^l = σ(x^l · k_i^l) for the top-5 MLP.vToxic vectors in GPT2 vs GPT2_DPO. Measured over 1,199 REALTOXICITYPROMPTS challenge set prompts × 20 generated tokens = 23,980 data points per vector.

## Top-5 MLP.vToxic Vectors (from activation_drop.sync.py)
The top-5 vectors by cosine similarity to W_Toxic correspond to the first 5 entries in `vectors_of_interest`:
1. Layer 19, Idx 770 (MLP.v_{770}^{19}) — most toxic
2. Layer 12, Idx 771 (MLP.v_{771}^{12})
3. Layer 18, Idx 2669 (MLP.v_{2669}^{18})
4. Layer 13, Idx 668 (MLP.v_{668}^{13})
5. Layer 16, Idx 255 (MLP.v_{255}^{16})

(Corresponding to Table 1 rows 2–6)

## Key Observations

### Mean Activation Values (from Section 5.2 and Figure 2)

| MLP Vector | Layer | Idx | GPT2 Mean Activation | GPT2_DPO Mean Activation | Direction |
|------------|-------|-----|---------------------|--------------------------|-----------|
| MLP.v_{770}^{19} | 19 | 770 | higher | lower (significant drop) | ↓ after DPO |
| MLP.v_{771}^{12} | 12 | 771 | higher | lower | ↓ after DPO |
| MLP.v_{2669}^{18} | 18 | 2669 | higher | lower | ↓ after DPO |
| MLP.v_{668}^{13} | 13 | 668 | higher | lower | ↓ after DPO |
| MLP.v_{255}^{16} | 16 | 255 | higher | lower | ↓ after DPO |

Note: Exact numerical activation values are not reported in the paper; the figure shows a consistent drop for all 5 vectors. The drop in activation is the direct evidence that GPT2_DPO's residual stream avoids toxic activation regions γ(MLP.k_Toxic).

## Experimental Setup
- `sample_size = tokenized_prompts.shape[0]` = 1,199 prompts
- `batch_size = 4`
- 20 autoregressive generation steps per prompt
- Activation accessed via `blocks.{layer}.mlp.hook_post[:, -1, idx]`
- Mean computed using `np.mean()` across all 23,980 activation values
- Plotting: seaborn catplot with kind="bar", hue by model (GPT2 vs DPO)
