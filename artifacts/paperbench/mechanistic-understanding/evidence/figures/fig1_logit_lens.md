---
# Figure 1: Logit Lens — Probability of "shit" Token Across Layers

**Source**: Figure 1, Section 4
**Claims**: C06, C09

## Description
Mean probability of outputting " shit" (token ID 7510) at each intermediate layer, averaged over 295 prompts that originally elicit "shit" as next token. Logit lens applies unembedding layer to accumulated residual stream at each intermediate position (including mid-layers after attention, before MLP).

## Key Observations (from figure caption and text)

### Axis Information
- **X-axis**: Layer index (0–24 including final "F"); minor ticks = ℓ_mid layers (after attention, before MLP); major ticks = post-MLP layers
- **Y-axis**: Probability of " shit" token (0 to ~0.48)
- **Lines**: GPT2 (blue) vs GPT2_DPO (orange/red)

### Quantitative Observations

| Layer Range | GPT2 Mean Prob (" shit") | GPT2_DPO Mean Prob (" shit") | Notes |
|-------------|--------------------------|-------------------------------|-------|
| Layers 0–16 (early) | ~0.0 | ~0.0 | No promotion of toxic token |
| Layers 17–18 (pre-peak) | rising | lower than GPT2 | DPO suppression begins |
| Layer ~19 MLP (peak) | >0.4 maximum | substantially lower | Shaded grey area: strongest MLP promotion |
| Layer ~20 MLP | high | lower than GPT2 | Shaded grey area |
| Layer ~21 MLP | high | lower than GPT2 | Shaded grey area |
| Final layer (F) | high | lower than GPT2 | DPO consistently suppresses |

- **Y-axis upper bound**: 0.48 (set explicitly in logitlens.sync.py: `fig.ax.set_ylim(ymax=0.48)`)
- **GPT2 peak**: Maximum probability exceeds 0.4 at highlighted MLP layers (x-positions 37–42 on 49-point axis)
- **GPT2_DPO**: Maximum probability remains substantially below GPT2's peak across all layers
- **Shaded grey areas** (alpha=0.35): Layers 37-38, 39-40, 41-42 on combined axis correspond to MLP sub-layers of transformer layers ~19–21

### Data Extraction Details
- 295 prompts stored at `toxicity/figures/shit_prompts.npy`
- Batch size: 4
- Token " shit" = vocabulary index 7510 (confirmed in `logitlens.sync.py`)
- `cache.accumulated_resid(layer=-1, incl_mid=True, apply_ln=True)` used
- Y-axis upper limit set to 0.48 (`fig.ax.set_ylim(ymax=0.48)`)
- All shaded grey areas (alpha=0.35) correspond to MLP layers, not attention layers

## Notes
- Minor ticks (ℓ_mid positions) indicate state after attention heads but before MLP — these are where attention's contribution ends and MLP begins
- The figure demonstrates that the toxic token is primarily promoted by specific MLP layers, not attention
- Post-DPO, promotion of the toxic token is substantially reduced at all highlighted MLP layers
