# Figure 2: Mean Activations for Toxic Vectors Before and After DPO

- **Source**: Figure 2, Section 5.2
- **Caption**: "Mean activations for toxic vectors before and after DPO."
- **Prompts**: 1,199 RealToxicityPrompts challenge prompts; 20 tokens generated per prompt.
- **X-axis**: Mean activation value m_i = σ(x^ℓ · k_i^ℓ)
- **Y-axis**: 5 toxic vectors (identified by layer and neuron index)
- **Models**: GPT2 (base) and GPT2DPO (DPO fine-tuned)

## Top-5 MLP.vToxic Vectors (by cosine similarity to W_Toxic)

| Vector ID | Layer | Neuron Index | GPT2 Mean Activation | GPT2DPO Mean Activation | Relative Change |
|-----------|-------|--------------|---------------------|------------------------|-----------------|
| MLP.v19_770 | 19 | 770 | ≈0.12 | ≈0.03 | Large drop |
| MLP.v12_771 | 12 | 771 | ≈0.09 | ≈0.02 | Large drop |
| MLP.v18_2669 | 18 | 2669 | ≈0.08 | ≈0.02 | Large drop |
| MLP.v13_668 | 13 | 668 | ≈0.07 | ≈0.02 | Large drop |
| MLP.v16_255 | 16 | 255 | ≈0.06 | ≈0.02 | Moderate drop |

**Key findings**:
- All 5 top toxic vectors show a substantial decrease in mean activation after DPO.
- GPT2DPO activations are consistently lower across all 5 vectors.
- The residual stream in GPT2DPO avoids the activation regions γ(MLP.kToxic).

**Note**: Values are approximate readings from bar chart. ≈ indicates visual estimation. Exact neuron indices are from the figure labels (L:19 Idx:770, L:12 Idx:771, L:18 Idx:2669, L:13 Idx:668, L:16 Idx:255).
