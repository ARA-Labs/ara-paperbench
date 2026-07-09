# Figure 1: Logit Lens on GPT2 and GPT2DPO

- **Source**: Figure 1, Section 4
- **Caption**: "Logit lens on GPT2 and GPT2DPO. Given 295 prompts that originally elicit 'sh*t' as the next token, we plot the average probability of outputting 'sh*t' from intermittent layers by applying the unembedding layer. Minor ticks indicate ℓmid layers (after attention heads, before MLP). Shaded areas indicate layers that promote 'sh*t' the most, which all correspond to MLP layers."
- **Prompts**: 295 prompts from RealToxicityPrompts for which GPT2 outputs "sh*t" as next token.
- **X-axis**: Layer index (8 through 22, labeled as "F" for final at 22); minor ticks = ℓmid
- **Y-axis**: Average probability of token "sh*t" (range 0.0–0.4+)
- **Models**: GPT2 (base) and GPT2DPO (DPO fine-tuned)

## Extracted Data Points (approximate readings from figure)

| Layer | GPT2 Probability | GPT2DPO Probability | Notes |
|-------|-----------------|---------------------|-------|
| 1–16 | ≈0.0 | ≈0.0 | Near-zero for both models |
| 17 (ℓmid) | ≈0.02 | ≈0.01 | Minor increase |
| 17 (MLP) | ≈0.05 | ≈0.02 | MLP layer shaded (toxic) |
| 18 (ℓmid) | ≈0.08 | ≈0.03 | |
| 18 (MLP) | ≈0.15 | ≈0.05 | Shaded region |
| 19 (ℓmid) | ≈0.18 | ≈0.06 | |
| 19 (MLP) | ≈0.35 | ≈0.10 | Peak for GPT2; shaded |
| 20 (ℓmid) | ≈0.38 | ≈0.12 | |
| 20 (MLP) | ≈0.42 | ≈0.14 | Approximate maximum for GPT2 |
| 21 (ℓmid) | ≈0.40 | ≈0.13 | |
| 21 (MLP) | ≈0.41 | ≈0.13 | Shaded |
| 22 (F/final) | ≈0.40 | ≈0.13 | |

**Key findings**:
- Probability of "sh*t" is ~0.0 for layers 1–16 in both models.
- Largest increases occur at MLP layers (shaded regions), not attention layers.
- GPT2 reaches maximum probability > 0.4; GPT2DPO maximum < 0.2.
- GPT2DPO consistently lower than GPT2 at all layers from 17 onward.
- All shaded (highest-promotion) regions correspond to MLP sublayers, confirming MLP blocks drive toxic token promotion.

**Note**: Exact values are approximate readings from the figure; ≈ notation indicates visual estimation.
