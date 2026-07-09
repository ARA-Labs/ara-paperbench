---
# Figure 6: Logit Entropy Analysis (CFG vs Vanilla vs Instruction-Tuned)
- **Source**: Figure 6, Section 5.1
- **Caption**: (a) "Entropy of logits for the vanilla prompted distribution P(y|x), the unprompted distribution, P(x), the CFG-γ=1.5 distribution and an instruction-tuned model Pinstruct(y|x)." (b) "Number of tokens overlapping in top-p=90% of vocabulary distributions between that of: CFG, that of the vanilla prompted model, p(y|x), and that of the unprompted model, P(x)."
- **Model**: Falcon-7b-Base (base) and Falcon-7b-Instruct; replicated on Redpajama-3b and Open-Assistant dataset
- **Dataset**: P3 dataset (32,902 sampled datapoints)
- **Condition**: γ=1.5 for CFG

**Figure 6a — Entropy Values:**

| Distribution | Mean Entropy (nats) | Notes |
|--------------|---------------------|-------|
| Unconditional P(x) | higher than vanilla | Highest entropy (least focused) |
| Vanilla P(y\|x) | 5.4 | Standard conditional generation |
| CFG γ=1.5 | 4.7 | Reduced entropy; similar to instruct |
| Instruction-Tuned Pinstruct(y\|x) | ≈4.7 | Similar level to CFG |

**Key finding (Section 5.1)**: "CFG entropy distribution is significantly lower across generation time-steps vanilla prompting, with a mean of 4.7 vs. 5.4."

**Figure 6b — Top-p=0.9 Vocabulary Overlap:**

| Comparison | Top-p=0.9 Overlap Fraction |
|------------|---------------------------|
| CFG vs Vanilla P(y\|x) | ≈50% shared tokens |
| CFG vs Uncond P(x) | lower than 50% |

**Key finding (Section 5.2)**: "CFG shares roughly 50% of the tokens in top-p=0.9 as the vanilla P(y|x) model." Despite similar entropies, CFG and instruction-tuned model vocabulary distributions are largely non-overlapping (less than 30% overlap per Section 5.2 text).

**Note**: Exact data points are not tabulated in the paper; values extracted from figure captions and text descriptions. ≈ marks approximate readings.
