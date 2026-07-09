---
# Table 11 (Appendix D.1): BLEU Scores for Machine Translation
- **Source**: Table 11, Appendix D.1
- **Caption**: "BLEU scores for different γ for machine translation tasks. In the case of 1-shot and mt0, we experiment with γ values between 1 and 1.1 since we see a rapid decline at even slightly higher values. All models are evaluated 0-shot unless otherwise specified."
- **Dataset**: WMT14 fr-en
- **Metric**: BLEU score

**0-shot models (Bloom-3B and RedPajama-Incite-3B):**

| Model | γ = 1 | γ = 1.10 | γ = 1.25 |
|-------|-------|----------|----------|
| Bloom-3B | 14.16 | 15.81 | 14.16 |
| RedPajama-Incite-3B | 15.04 | 17.24 | 17.78 |

**1-shot / prompt-tuned models:**

| Model | γ = 1 | γ = 1.05 | γ = 1.10 |
|-------|-------|----------|----------|
| Bloom-3B 1-shot | 29.84 | 29.19 | 28.53 |
| mT0 | 29.77 | 29.41 | 27.79 |

**Notes**:
- Bloom-3B: multilingual model trained on 49 languages
- RedPajama-Incite-Base-3B: trained on 1.5T tokens of English text
- mT0: prompt-tuned sequence-to-sequence model; shows no significant gains (already at pinnacle of zero-shot performance)
- Best results: γ ∈ [1.1, 1.25] for 0-shot; 1-shot and mT0 show rapid decline even at slightly higher values
