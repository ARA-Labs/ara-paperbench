---
# Table 2: Toxicity, Perplexity, and F1 after Interventions or DPO

**Source**: Table 2, Section 3.3
**Note**: Vectors scaled so resulting PPL ≈ GPT2 (No Op) baseline. †: DPO is not an intervention but a fine-tuned model.

## Exact Values

| Method | Vector | Toxic | PPL | F1 |
|--------|--------|-------|-----|-----|
| No Op | N/A | 0.453 | 21.7 | 0.193 |
| Subtract | $W_{\text{Toxic}}$ | 0.245 | 23.56 | 0.193 |
| Subtract | $\text{MLP.v}_{770}^{19}$ | 0.305 | 23.30 | 0.192 |
| Subtract | $\text{SVD.U}_{\text{Toxic}}[0]$ | 0.268 | 23.48 | 0.193 |
| DPO† | N/A | 0.208 | 23.34 | 0.195 |

## Notes
- Toxic: Perspective API TOXICITY attribute, averaged over REALTOXICITYPROMPTS challenge set (1,199 prompts, 20 tokens each)
- PPL: Perplexity on Wikitext-2-raw-v1 test set
- F1: Token-overlap F1 using 2,000 Wikipedia sentences as prompts (20 tokens generated)
- Subtraction scale values: W_Toxic=50, MLP.v_{770}^{19}=20, SVD.UToxic[0]=100 (from run_evaluations.py config)
- Applied at layer 23 (last MLP layer) as forward hook
- DPO achieves lowest toxicity (0.208); all methods maintain similar F1 (~0.193–0.195)
- All interventions and DPO slightly increase perplexity compared to no-op (21.7 → ~23.3–23.6)
