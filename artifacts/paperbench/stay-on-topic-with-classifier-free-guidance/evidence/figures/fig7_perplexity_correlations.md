---
# Figure 7: Perplexity Correlations (CFG vs Instruction-Tuned)
- **Source**: Figure 7 (Tables 7a and 7b in paper), Section 5.2
- **Caption**: (a) "Correlation between the perplexities of each model on P3." (b) "Correlation between the perplexity and similarity between Instruction-Tuned and CFG."
- **Model**: Falcon-7b-Base (base) and Falcon-7b-Instruct
- **Dataset**: P3 dataset (32,902 sampled datapoints)

**Figure 7a — Perplexity Correlation Matrix (Pearson r):**

| | PPL p(y\|x) | PPL cfg | PPL instruct |
|---|-------------|---------|--------------|
| PPL p(y\|x) | 1.0 | 0.94 | 0.83 |
| PPL cfg | 0.94 | 1.0 | 0.7 |
| PPL instruct | 0.83 | 0.7 | 1.0 |

**Figure 7b — Spearman Correlation: Perplexity vs CFG/Instruct Similarity:**

| Distribution | rs (Spearman correlation with CFG-Instruct similarity) | p-value |
|--------------|-------------------------------------------------------|---------|
| PPL p(y\|x) | 0.01 | 0.2 (not significant) |
| PPL cfg | -0.04 | <.001 (significant) |
| PPL instruct | 0.04 | <.001 (significant) |

**Key findings**:
- Models mostly agree on difficulty of input sentences (high perplexity correlation across all three models: r ≥ 0.70)
- CFG and instruction-tuning have similar top-p overlaps only on prompts where both have high perplexity (hard prompts)
- Small but significant Spearman correlation (rs=0.05) between prompt length and Instruct/CFG agreement (longer prompts → more agreement)
- Overall: vanilla P(y|x) is more similar to instruction-tuning than CFG is (per Figure 16 in Appendix F)
