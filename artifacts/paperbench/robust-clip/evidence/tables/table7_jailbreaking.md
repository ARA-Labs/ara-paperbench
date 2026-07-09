# Table 7: Jailbreaking Attacks Against LLaVA 1.5
- **Source**: Table 7, Section 4.4
- **Caption**: "We run the attack proposed by Qi et al. (2023) and report the success rates across harmful prompts of different categories. Lower numbers indicate more robust models. LLaVA 1.5 with TeCoA or FARE is significantly more robust than with original CLIP."
- **Conditions**: LLaVA-1.5 7B; jailbreaking attack from Qi et al. (2023); 5000 iterations, α=1/255; 40 harmful prompts across 4 categories (identity: 11, disinfo: 13, crime: 13, x-risk: 3); attack radii ε∈{0, 16/255, 32/255, 64/255}; success = model adheres to harmful prompt

| Model | ε | any (40) | identity (11) | disinfo (13) | crime (13) | x-risk (3) |
|-------|---|---------|---------------|--------------|------------|------------|
| CLIP | 0 (clean) | 12 / 40 | 4 / 11 | 5 / 13 | 1 / 13 | 2 / 3 |
| TeCoA4 | 0 (clean) | 14 / 40 | 3 / 11 | 8 / 13 | 1 / 13 | 2 / 3 |
| FARE4 | 0 (clean) | 13 / 40 | 3 / 11 | 8 / 13 | 1 / 13 | 1 / 3 |
| CLIP | 16/255 | 24 / 40 | 10 / 11 | 9 / 13 | 2 / 13 | 3 / 3 |
| TeCoA4 | 16/255 | 14 / 40 | 3 / 11 | 8 / 13 | 1 / 13 | 2 / 3 |
| FARE4 | 16/255 | 15 / 40 | 3 / 11 | 9 / 13 | 1 / 13 | 2 / 3 |
| CLIP | 32/255 | 28 / 40 | 11 / 11 | 11 / 13 | 3 / 13 | 3 / 3 |
| TeCoA4 | 32/255 | 14 / 40 | 2 / 11 | 9 / 13 | 1 / 13 | 2 / 3 |
| FARE4 | 32/255 | 16 / 40 | 3 / 11 | 10 / 13 | 1 / 13 | 2 / 3 |
| CLIP | 64/255 | 36 / 40 | 11 / 11 | 13 / 13 | 9 / 13 | 3 / 3 |
| TeCoA4 | 64/255 | 23 / 40 | 10 / 11 | 9 / 13 | 1 / 13 | 3 / 3 |
| FARE4 | 64/255 | 23 / 40 | 9 / 11 | 10 / 13 | 2 / 13 | 2 / 3 |
