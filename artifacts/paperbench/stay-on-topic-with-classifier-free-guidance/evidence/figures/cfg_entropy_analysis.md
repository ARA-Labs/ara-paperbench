# Figure 6: CFG Effect on Logit Distribution Entropy and Top-p Overlap
- **Source**: Figure 6, Section 5.1
- **Caption**: "We show into how CFG alters the logit distribution of the vanilla prompted model, P(y|x). CFG lowers the entropy to a level roughly similar to instruction-tuned model variant. CFG shares roughly 50% of the tokens in top-p=0.9 as the vanilla P(y|x) model."
- **Model**: Falcon-7b-Base (CFG and vanilla) and Falcon-7b-Instruct; P3 dataset (32,902 samples)

## Figure 6a: Mean Entropy Values
- **Axis labels**: X = condition; Y = entropy H(p) = -Σ p_k log p_k (computed via scipy)

| Condition | Mean Entropy |
|-----------|-------------|
| Vanilla P(y\|x) (γ=1) | ≈ 5.4 |
| Unprompted P(x) | higher than vanilla (exact value not given numerically) |
| CFG γ=1.5 | ≈ 4.7 |
| Instruction-tuned P_instruct(y\|x) | similar to CFG (exact value not given numerically) |

**Key finding**: CFG (γ=1.5) mean entropy 4.7 vs vanilla P(y|x) mean entropy 5.4 — a significant reduction.

## Figure 6b: Top-p=90% Vocabulary Overlap
- **Axis labels**: X = generation time-step (token index); Y = number of tokens overlapping in top-p=90%

| Comparison | Approximate Top-p Overlap |
|------------|--------------------------|
| CFG vs vanilla P(y\|x) | ≈ 50% overlap |
| CFG vs unprompted P(x) | lower than 50% |
| CFG vs instruct | ≈ < 30% overlap (not ≈ 50%) |

**Key finding**: Despite similar entropy levels, CFG and instruction-tuned model have < 30% vocabulary overlap in top-p=0.9, indicating distinct mechanisms.
