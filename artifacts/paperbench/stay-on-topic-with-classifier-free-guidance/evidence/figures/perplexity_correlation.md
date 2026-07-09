# Figure 7: Perplexity Correlation Between Models on P3
- **Source**: Figure 7, Section 5.2
- **Caption**: "We seek to identify when CFG is similar to instruction-tuning. Models mostly agree on the difficulty of input sentences, and in cases where they do not, CFG and Instruction-tuning have similar top-p overlaps."
- **Model**: Falcon-7b-Base (vanilla and CFG γ=1.5), Falcon-7b-Instruct; P3 dataset (32,902 samples)

## Figure 7a: Perplexity Correlation Matrix

| | PPL p(y\|x) | PPL cfg | PPL instruct |
|---|------------|---------|-------------|
| PPL p(y\|x) | 1.0 | 0.94 | 0.83 |
| PPL cfg | 0.94 | 1.0 | 0.7 |
| PPL instruct | 0.83 | 0.7 | 1.0 |

## Figure 7b: Spearman Correlation — Perplexity vs. CFG/Instruct Similarity

| Model | rs (sim) | p-val |
|-------|----------|-------|
| PPL p(y\|x) | 0.01 | 0.2 |
| PPL cfg | -0.04 | <.001 |
| PPL instruct | 0.04 | <.001 |

**Key findings**:
- Perplexity correlations are high (0.94 between vanilla and CFG; 0.83 between vanilla and instruct)
- All three models mostly agree on which inputs are "hard"
- Spearman correlation between CFG perplexity and CFG/instruct similarity: rs = -0.04 (p<0.001) — significant but small negative correlation
- Harder phrases for instruction-tuned models are typically where CFG and instruction-tuned models align
