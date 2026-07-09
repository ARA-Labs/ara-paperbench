# Table 2: Toxicity, Perplexity, and F1 After Interventions or DPO

- **Source**: Table 2, Section 3.3 and Section 5
- **Caption**: "Toxicity, perplexity (PPL), and F1 after interventions or DPO. We scale our toxic vectors such that the resulting perplexity is comparable to that of GPT2 (No Op). †: Not an intervention."
- **Evaluation**: 1,199 RealToxicityPrompts challenge prompts (toxicity); Wikitext-2 (perplexity); 2,000 Wikipedia sentences (F1)
- **Toxicity**: Measured with Perspective API

| METHOD | VECTOR | TOXIC | PPL | F1 |
|--------|--------|-------|-----|-----|
| NO OP | N/A | 0.453 | 21.7 | 0.193 |
| SUBTRACT | WTOXIC | 0.245 | 23.56 | 0.193 |
| SUBTRACT | MLP.v19 | 0.305 | 23.30 | 0.192 |
| SUBTRACT | SVD.UTOXIC[0] | 0.268 | 23.48 | 0.193 |
| DPO† | N/A | 0.208 | 23.34 | 0.195 |

**Notes**:
- α (scale for subtraction) is chosen per-vector to match perplexity of GPT2DPO (≈23.34).
- DPO (†) is marked as "not an intervention" — it is fine-tuning, not a forward-pass modification.
- DPO achieves the lowest toxicity (0.208) while maintaining the highest F1 (0.195) and comparable perplexity (23.34).
