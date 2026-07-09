# ANCOVA P-Value Results for FLOP Analysis

- **Source**: Table 4, Appendix C.2
- **Caption**: "ANCOVA p-value results for plots shown in Figure 11. We calculate ANCOVA on log-transformed variables and calculate significance at p=.01."
- **Conditions**: ANCOVA regression comparing CFG models (2× FLOPs) vs vanilla models (1× FLOPs) across model families (GPT-2, Pythia, LLaMA); significance threshold p=0.01

| Task | p-value | Winner (p<0.01) |
|------|---------|-----------------|
| Lambada | 0.000 | CFG |
| WinoGrande | 0.003 | Vanilla |
| SciQ | 0.008 | CFG |
| TriviaQA | 0.008 | Vanilla |
| HellaSwag | 0.012 | p > .01 (insignificant) |
| PiQA | 0.030 | p > .01 (insignificant) |
| ARC-c | 0.216 | p > .01 (insignificant) |
| BoolQ | 0.345 | p > .01 (insignificant) |
| ARC-e | 0.355 | p > .01 (insignificant) |

## Summary
- 5 tasks with p > 0.01: HellaSwag, PiQA, ARC-c, BoolQ, ARC-e (no significant difference between CFG and 2× vanilla)
- 2 tasks favor CFG (p < 0.01): Lambada (p=0.000), SciQ (p=0.008)
- 2 tasks favor Vanilla (p < 0.01): WinoGrande (p=0.003), TriviaQA (p=0.008)
