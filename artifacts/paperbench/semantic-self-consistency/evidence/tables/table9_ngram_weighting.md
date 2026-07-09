---
# Table 9: N-Gram Weighting Results (n=2)

**Source**: Table 9, §H.2
**Claims**: C01
**Description**: Weighting results based on N-gram overlap with n=2 on AQuA-RAT and SVAMP. Shows poor performance demonstrating that lexical overlap alone is insufficient for reasoning quality assessment.

| Model | AQuA-RAT | SVAMP |
|-------|----------|-------|
| Llama 2 | 15.5 | 32.8 |
| Mistral | 16.7 | 47.1 |
| GPT 3.5 | 25.3 | 63.9 |

## Notes
- All values far below SC baseline (Llama 2: 24.8/46.5; Mistral: 25.6/68.5; GPT 3.5: 59.4/79.8)
- Low accuracy and high randomness in result distribution
- Higher values of n worsened results further
- Demonstrates that semantic embedding is necessary; pure lexical overlap is ineffective
