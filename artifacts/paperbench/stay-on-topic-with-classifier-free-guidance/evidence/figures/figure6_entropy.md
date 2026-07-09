# CFG Effect on Logit Entropy and Vocabulary Distribution
- **Source**: Figure 6a and 6b, Section 5.1 and 5.2
- **Caption (6a)**: "Entropy of logits for the vanilla prompted distribution P(y|x), the unprompted distribution, P(x), the CFG-γ=1.5 distribution and an instruction-tuned model Pinstruct(y|x)."
- **Caption (6b)**: "Number of tokens overlapping in top-p=90% of vocabulary distributions between that of: CFG, that of the vanilla prompted model, p(y|x), and that of the unprompted model, P(x)."
- **Axis labels (6a)**: x-axis: generation timestep; y-axis: entropy H(p)
- **Axis labels (6b)**: x-axis: generation timestep; y-axis: number of overlapping tokens
- **Model**: Falcon-7b-Base (vanilla and CFG); Falcon-7b-Instruct (instruction-tuned baseline)
- **Dataset**: 32,902 samples from P3 dataset

## Figure 6a: Mean Entropy Values (stated in paper text, Section 5.1)

| Model Condition | Mean Entropy |
|----------------|-------------|
| Vanilla prompted P(y\|x) | 5.4 |
| CFG γ=1.5 | 4.7 |
| Instruction-tuned Pinstruct(y\|x) | ≈4.7 (similar to CFG, per Figure 6a) |
| Unprompted P(x) | Higher than vanilla (exact value not stated) |

**Key finding**: CFG entropy distribution is "significantly lower across generation time-steps vanilla prompting, with a mean of 4.7 vs. 5.4" (Section 5.1).

## Figure 6b: Top-p=90% Vocabulary Overlap

| Comparison | Overlap |
|-----------|---------|
| CFG vs Vanilla P(y\|x) | ~50% of tokens overlap (stated: "CFG shares roughly 50% of the tokens in top-p=0.9 as the vanilla P(y|x) model") |
| CFG vs Instruction-tuned | < 0.3 overlap (stated: "largely not overlapping" per Section 5.2; "top-p overlap of less than 0.3") |
| Vanilla vs Instruction-tuned | Higher overlap than CFG vs Instruct (vanilla is more similar to instruct than CFG is) |

## Perplexity Correlations (Figure 7a table in paper)

| | PPL p(y\|x) | PPL cfg | PPL instruct |
|---|------------|---------|-------------|
| PPL p(y\|x) | 1.0 | 0.94 | 0.83 |
| PPL cfg | 0.94 | 1.0 | 0.7 |
| PPL instruct | 0.83 | 0.7 | 1.0 |

## Spearman Correlation with CFG-Instruct Similarity (Figure 7b table in paper)

| Model | rs (sim) | p-val |
|-------|----------|-------|
| PPL p(y\|x) | 0.01 | 0.2 |
| PPL cfg | -0.04 | <.001 |
| PPL instruct | 0.04 | <.001 |
