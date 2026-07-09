---
# Figure 4: Ablation Study — FID Scores for TAN Component Variants
- **Source**: Figure 4, §5.4
- **Caption**: "This figure shows our ablation study with all models trained for 300 iterations on a 10-shot sunglasses dataset measured with FID (↓): the first line - baseline (direct fine-tuning model), second line - Adaptor (fine-tuning only few extra parameters), third line - DPMs-TAN w/o A (only using similarity-guided training), and final line - DPMs-TAN (our method)."
- **Axis labels**: Rows = model variants; value = FID (↓, lower is better)
- **Experimental conditions**: FFHQ → 10-shot Sunglasses; 300 training iterations for all variants; same fixed noise inputs for image generation; FID computed as primary metric

## Extracted Data Points

| Model Variant | FID (↓) | Description |
|---------------|---------|-------------|
| Baseline (direct fine-tuning) | 38.65 | Full DDPM fine-tuning, all parameters updated, standard DDPM loss |
| Adaptor only | 41.88 | Only adaptor layers trained, standard DDPM loss (no similarity guidance, no adversarial noise) |
| DPMs-TAN w/o A (w/o adversarial noise) | 26.41 | Adaptor + similarity-guided training only (no adversarial noise selection) |
| DPMs-TAN (full method) | 20.06 | Adaptor + similarity-guided training + adversarial noise selection |

**Note**: The paper also reports a slightly different value in §5.4 text: "decreases from 41.88 (with direct adaptation) to 26.41 (with similarity-guided training) and then to 20.66 (with DPMs-TAN)". The figure caption shows 20.06. The caption value 20.06 is used as primary evidence as it corresponds to the figure; 20.66 appears to be a typo in the body text. Both values are recorded for reproducers.
