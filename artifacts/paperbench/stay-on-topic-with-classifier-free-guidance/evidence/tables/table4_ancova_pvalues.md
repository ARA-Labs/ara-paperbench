---
# Table 4 (Appendix C.2): ANCOVA P-Values for FLOPs/Accuracy Analysis
- **Source**: Table 4 (labeled in Appendix C.2), Section 4
- **Caption**: "ANCOVA p-value results for plots shown in Figure 11. We calculate ANCOVA on log-transformed variables and calculate significance at p=.01."
- **Analysis**: ANCOVA regression comparing CFG group (model + CFG) vs vanilla group (2x model, no CFG) on log-FLOP vs accuracy relationship
- **Significance threshold**: p = 0.01

| Task | p-value | Win (if significant) |
|------|---------|---------------------|
| Lambada | 0.000 | CFG |
| WinoGrande | 0.003 | Vanilla |
| SciQ | 0.008 | CFG |
| TriviaQA | 0.008 | Vanilla |
| HellaSwag | 0.012 | p > .01 |
| PiQA | 0.030 | p > .01 |
| ARC-c | 0.216 | p > .01 |
| BoolQ | 0.345 | p > .01 |
| ARC-e | 0.355 | p > .01 |

**Summary**: 5/9 tasks have p > 0.01 (statistically insignificant difference between CFG and 2x vanilla); 2 tasks favor CFG (Lambada, SciQ); 2 tasks favor vanilla (WinoGrande, TriviaQA).
