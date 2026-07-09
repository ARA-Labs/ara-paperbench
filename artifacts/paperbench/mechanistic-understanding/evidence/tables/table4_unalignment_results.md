# Table 4: Un-aligning GPT2DPO

- **Source**: Table 4, Section 5.3
- **Caption**: "Un-aligning GPT2DPO. By scaling toxic key vectors, and thus increasing the regions that elicit toxicity, we are able to undo the alignment learned from DPO and reactivate toxicity."
- **Method**: Scale top-7 MLP key vectors (by cosine similarity to WToxic) by 10×
- **Evaluation**: 1,199 RealToxicityPrompts challenge prompts (toxicity); Wikitext-2 (perplexity); 2,000 Wikipedia sentences (F1)

| METHOD | TOXIC | PPL | F1 |
|--------|-------|-----|-----|
| GPT2DPO | 0.208 | 23.34 | 0.195 |
| SCALE MLP.kTOXIC | 0.458 | 23.30 | 0.195 |
| GPT2 | 0.453 | 21.7 | 0.193 |

**Notes**:
- Scaling 7 key vectors by 10× restores toxicity from 0.208 to 0.458 (near original GPT2 level of 0.453).
- Perplexity is essentially unchanged (23.30 vs. 23.34 for GPT2DPO), unlike subtraction interventions.
- F1 is unchanged at 0.195.
- Un-alignment requires only 7 weight modifications, no retraining.
