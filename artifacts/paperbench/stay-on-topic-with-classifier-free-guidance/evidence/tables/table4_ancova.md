# ANCOVA P-Value Results: CFG vs 2x-Size Vanilla Model
- **Source**: Table 4, Appendix C.2 (referred to as Table 6 / Table 9 with noted paper error), Section 4
- **Caption**: "ANCOVA p-value results for plots shown in Figure 11. We calculate ANCOVA on log-transformed variables and calculate significance at p=.01."
- **Conditions**: ANCOVA comparing regression lines of CFG-model group vs vanilla-model group on log(FLOP) vs accuracy plots

| Task | p-value | Win |
|------|---------|-----|
| Lambada | 0.000 | CFG |
| WinoGrande | 0.003 | Vanilla |
| SciQ | 0.008 | CFG |
| TriviaQA | 0.008 | Vanilla |
| HellaSwag | 0.012 | p > .01 |
| PiQA | 0.030 | p > .01 |
| ARC-c | 0.216 | p > .01 |
| BoolQ | 0.345 | p > .01 |
| ARC-e | 0.355 | p > .01 |

**Note**: Tasks with p > .01 (HellaSwag, PiQA, ARC-c, BoolQ, ARC-e = 5 tasks) show statistically insignificant difference between CFG and 2x-size vanilla at the p=0.01 threshold. 2 tasks favor CFG (Lambada, SciQ), 2 favor vanilla (WinoGrande, TriviaQA).
