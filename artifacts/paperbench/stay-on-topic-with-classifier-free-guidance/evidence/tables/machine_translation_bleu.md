# Machine Translation BLEU Scores

- **Source**: Table 11, Appendix D.1
- **Caption**: "BLEU scores for different γ for machine translation tasks. In the case of 1-shot and mt0, we experiment with γ values between 1 and 1.1 since we see a rapid decline at even slightly higher values. All models are evaluated 0-shot unless otherwise specified."
- **Conditions**: WMT14 fr-en dataset; BLEU metric; 0-shot unless noted

## 0-Shot Models

| Model | γ=1 | γ=1.10 | γ=1.25 |
|-------|-----|--------|--------|
| Bloom-3B | 14.16 | 15.81 | 14.16 |
| RedPajama-Incite-3B | 15.04 | 17.24 | 17.78 |

## 1-Shot and Instruction-Tuned Models

| Model | γ=1 | γ=1.05 | γ=1.10 |
|-------|-----|--------|--------|
| Bloom-3B 1-shot | 29.84 | 29.19 | 28.53 |
| mT0 | 29.77 | 29.41 | 27.79 |

## Notes
- 0-shot: γ=1.1–1.25 yields best results; higher γ rapidly degrades performance
- 1-shot and mT0: CFG provides no improvement; rapid degradation even at γ=1.05
- mT0 is a prompt-tuned seq2seq model; paper suggests it may already be at the pinnacle of 0-shot performance
