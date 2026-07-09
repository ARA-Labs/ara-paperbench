# Table 2: Toxicity, Perplexity, and F1 After Interventions or DPO

- **Source**: Table 2, Section 3.3
- **Caption**: "Toxicity, perplexity (PPL), and F1 after interventions or DPO. We scale our toxic vectors such that the resulting perplexity is comparable to that of GPT2 (No Op). †: Not an intervention."
- **Experimental conditions**: Toxicity measured via Perspective API on 1,199 "challenge" prompts from RealToxicityPrompts; PPL measured on Wikitext-2; F1 measured with 2,000 Wikipedia sentence prompts.

| Method | Vector | Toxic | PPL | F1 |
|--------|--------|-------|-----|-----|
| NO OP | N/A | 0.453 | 21.7 | 0.193 |
| SUBTRACT | WTOXIC | 0.245 | 23.56 | 0.193 |
| SUBTRACT | MLP.V19 | 0.305 | 23.30 | 0.192 |
| SUBTRACT | SVD.UTOXIC[0] | 0.268 | 23.48 | 0.193 |
| DPO† | N/A | 0.208 | 23.34 | 0.195 |

**Notes**:
- All subtraction interventions scale α to match DPO perplexity.
- DPO† is marked as "not an intervention" (it is a fine-tuned model, not an inference-time modification).
- Lowest toxicity achieved by DPO (0.208); all interventions also reduce toxicity vs. No Op (0.453).
