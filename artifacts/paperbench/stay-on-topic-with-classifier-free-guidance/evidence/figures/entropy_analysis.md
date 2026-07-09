# Entropy Analysis: CFG vs Vanilla vs Instruction-Tuned

- **Source**: Figure 6 (panels a and b), Section 5.1–5.2
- **Caption**: "We show into how CFG alters the logit distribution of the vanilla prompted model, P(y|x). CFG lowers the entropy to a level roughly similar to instruction-tuned model variant. CFG shares roughly 50% of the tokens in top-p=0.9 as the vanilla P(y|x) model."
- **Conditions**: Falcon-7b-Base (vanilla, unconditional, CFG γ=1.5) and Falcon-7b-Instruct; 32,902 P3 samples; entropy H(p) = -Σ_k p_k log p_k

## Figure 6a: Mean Logit Entropy by Distribution Type

| Distribution | Mean Entropy | Notes |
|-------------|-------------|-------|
| Unconditional P(x) | ≈5.8 (estimated from figure) | Highest entropy; no prompt conditioning |
| Vanilla prompted P(y\|x) | 5.4 | Baseline conditional generation |
| CFG γ=1.5 | 4.7 | Significantly lower than vanilla |
| Instruction-tuned P_instruct(y\|x) | ≈4.7 (similar to CFG) | Similar entropy to CFG |

Note: Exact values for unconditional and instruct entropy are read from Figure 6a. The paper explicitly states: "CFG entropy distribution is significantly lower across generation time-steps vanilla prompting, with a mean of 4.7 vs. 5.4."

## Figure 6b: Top-p=90% Token Count Overlap

| Comparison | Top-p=90% Overlap Fraction | Notes |
|-----------|---------------------------|-------|
| CFG vs Vanilla P(y\|x) | ≈50% | "CFG shares roughly 50% of the tokens in top-p=0.9 as the vanilla P(y|x) model" |
| CFG vs Instruction-tuned | <30% | Largely non-overlapping; different token selection |
| Vanilla P(y\|x) vs Instruction-tuned | >50% (estimated) | Vanilla more similar to instruct than CFG is |

## Perplexity Correlation (Table 7 in paper, Figure 7)

| Comparison | Spearman rs (sim) | p-value |
|-----------|-------------------|---------|
| PPL P(y\|x) vs CFG/Instruct similarity | 0.01 | 0.2 (not significant) |
| PPL CFG vs CFG/Instruct similarity | -0.04 | <.001 (significant) |
| PPL instruct vs CFG/Instruct similarity | 0.04 | <.001 (significant) |

## Perplexity Cross-Correlation (Figure 7a)

| | PPL P(y\|x) | PPL CFG | PPL instruct |
|--|------------|---------|-------------|
| PPL P(y\|x) | 1.0 | 0.94 | 0.83 |
| PPL CFG | 0.94 | 1.0 | 0.7 |
| PPL instruct | 0.83 | 0.7 | 1.0 |
