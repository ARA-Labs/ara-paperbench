---
# Table 6: PPLM Hyperparameters

**Source**: Table 6, Appendix D

## Exact Values

| Hyperparameter | Value |
|----------------|-------|
| Step Size | 0.4 |
| Temperature | 1 |
| Top K | 10 |
| Num Iterations | 50 |
| Window Length | 0 |
| Horizon Length | 1 |
| Decay | False |
| Gamma | 1 |
| GM Scale | 0.95 |
| KL Scale | 0.1 |

## Notes
- PPLM used to generate toxic (negative) continuations for DPO training data
- W_Toxic serves as PPLM attribute classifier
- GM Scale = geometric mean scale (balance between LM and attribute guidance)
- KL Scale = KL divergence penalty to prevent degenerate outputs
- Total: 24,576 pairwise (toxic, non-toxic) examples generated
