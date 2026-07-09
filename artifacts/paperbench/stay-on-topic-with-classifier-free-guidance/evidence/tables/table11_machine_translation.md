# Machine Translation BLEU Scores
- **Source**: Table 11, Appendix D.1
- **Caption**: "BLEU scores for different γ for machine translation tasks. In the case of 1-shot and mt0, we experiment with γ values between 1 and 1.1 since we see a rapid decline at even slightly higher values. All models are evaluated 0-shot unless otherwise specified."
- **Conditions**: WMT14 fr-en dataset; metric: BLEU score

| Model | γ=1 | γ=1.05 | γ=1.10 | γ=1.25 |
|-------|-----|--------|--------|--------|
| Bloom-3B (0-shot) | 14.16 | — | 15.81 | 14.16 |
| RedPajama-Incite-3B (0-shot) | 15.04 | — | 17.24 | 17.78 |
| Bloom-3B 1-shot | 29.84 | 29.19 | 28.53 | — |
| mT0 (0-shot) | 29.77 | 29.41 | 27.79 | — |

**Notes**:
- For Bloom-3B and RedPajama-Incite-3B (0-shot): tested at γ ∈ {1, 1.10, 1.25}
- For Bloom-3B 1-shot and mT0: tested at γ ∈ {1, 1.05, 1.10} due to rapid decline at higher values
- Best 0-shot results: RedPajama at γ=1.25 (17.78 BLEU), Bloom-3B at γ=1.10 (15.81 BLEU)
- mT0 (prompt-tuned) shows no significant CFG improvement; declines even at γ=1.05
