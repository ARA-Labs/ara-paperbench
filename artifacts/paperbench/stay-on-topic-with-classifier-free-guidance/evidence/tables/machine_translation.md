# Table 11: Machine Translation BLEU Scores
- **Source**: Table 11, Appendix D.1
- **Caption**: "BLEU scores for different γ for machine translation tasks. In the case of 1-shot and mt0, we experiment with γ values between 1 and 1.1 since we see a rapid decline at even slightly higher values. All models are evaluated 0-shot unless otherwise specified."
- **Condition**: WMT14 fr-en dataset; BLEU metric; 0-shot unless noted

| Model | γ=1 | γ=1.05 | γ=1.10 | γ=1.25 |
|-------|-----|--------|--------|--------|
| Bloom-3B (0-shot) | 14.16 | — | 15.81 | 14.16 |
| RedPajama-Incite-3B (0-shot) | 15.04 | — | 17.24 | 17.78 |
| Bloom-3B 1-shot | 29.84 | 29.19 | 28.53 | — |
| mT0 (0-shot) | 29.77 | 29.41 | 27.79 | — |

**Notes:**
- Bloom-3B 0-shot best at γ=1.10 (15.81 vs 14.16 baseline)
- RedPajama 0-shot best at γ=1.25 (17.78 vs 15.04 baseline)
- Bloom-3B 1-shot declines monotonically with increasing γ
- mT0 declines with any CFG — prompt-tuned model shows no benefit
- Dashes (—) indicate value not tested at that γ
