---
# Table 4: Un-aligning GPT2_DPO by Scaling Toxic Key Vectors

**Source**: Table 4, Section 5.3

## Exact Values

| Method | Toxic | PPL | F1 |
|--------|-------|-----|-----|
| GPT2$_{\text{DPO}}$ | 0.208 | 23.34 | 0.195 |
| Scale MLP.k$_{\text{Toxic}}$ | 0.458 | 23.30 | 0.195 |
| GPT2 | 0.453 | 21.7 | 0.193 |

## Notes
- Un-alignment: top-7 key vectors with highest cosine similarity to W_Toxic scaled by 10x
- Toxicity reverts from 0.208 (aligned) to 0.458, which is nearly identical to original GPT2 (0.453)
- Perplexity remains unchanged at ~23.30 (vs 23.34 for aligned; vs 21.7 for original GPT2)
- F1 remains at 0.195 (unchanged from aligned)
- Key insight: scaling key vectors enlarges activation regions without directly modifying residual stream, hence no PPL impact
- Implementation: unalign.py config: probe_path=checkpoints/probe.pt, num_value_vecs=7, scale=10
