# Table 4: Un-aligning GPT2DPO

- **Source**: Table 4, Section 5.3
- **Caption**: "Un-aligning GPT2DPO. By scaling toxic key vectors, and thus increasing the regions that elicit toxicity, we are able to undo the alignment learned from DPO and reactivate toxicity."
- **Experimental conditions**: Same evaluation setup as Table 2: 1,199 RealToxicityPrompts challenge prompts (toxicity), Wikitext-2 (PPL), 2,000 Wikipedia sentences (F1). Un-alignment: top-7 MLP key vectors by cosine similarity to WToxic, scaled by 10×.

| Method | Toxic | PPL | F1 |
|--------|-------|-----|-----|
| GPT2DPO | 0.208 | 23.34 | 0.195 |
| SCALE MLP.kTOXIC | 0.458 | 23.30 | 0.195 |
| GPT2 | 0.453 | 21.7 | 0.193 |

**Notes**:
- Scaling 7 key vectors by 10× reverts toxicity from 0.208 to 0.458 (≈ original GPT2's 0.453).
- Perplexity after un-alignment (23.30) is nearly identical to GPT2DPO (23.34), unlike subtraction interventions which affect perplexity more.
- F1 is unchanged at 0.195 before and after un-alignment.
