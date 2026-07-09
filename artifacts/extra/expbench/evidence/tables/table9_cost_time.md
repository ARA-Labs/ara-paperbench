# Table 9: Cost–Time Summary Statistics
- **Source**: Table 9, Appendix I.2
- **Caption**: "Cost-time summary statistics for all evaluated agents and models. OH = OpenHands, IA = IterativeAgent. Med = median, Std = standard deviation, T = time (minutes), C = cost (USD)."
- **Conditions**: 461 tasks; 40-minute soft timeout (occasionally exceeded); cost reflects backbone LLM token usage only (input + output), excluding agent-internal LLM API usage and compute costs; low time/cost may indicate agent failure to complete experiment

## Time Statistics (minutes)

| Agent | Model | Avg T | Med T | Q1 T | Q3 T | Std T | Min T | Max T |
|-------|-------|-------|-------|------|------|-------|-------|-------|
| OH | o3-mini | 24.89 | 23.24 | 13.93 | 33.60 | 16.74 | 1.70 | 47.72 |
| OH | 3.7 Sonnet | 33.53 | 29.64 | 16.67 | 37.72 | 10.03 | 2.55 | 74.04 |
| OH | Nova Pro | 17.82 | 15.03 | 11.85 | 24.06 | 9.37 | 0.64 | 74.33 |
| OH | 3.5 Haiku | 25.17 | 24.23 | 13.26 | 32.72 | 17.38 | 1.21 | 37.85 |
| OH | DeepSeek R1 | 32.24 | 31.40 | 19.09 | 38.69 | 11.82 | 0.97 | 60.77 |
| IA | 3.5 Haiku | 30.24 | 26.13 | 19.63 | 38.24 | 54.62 | 0.30 | 402.84 |
| IA | Nova Pro | 30.09 | 26.31 | 19.51 | 38.09 | 27.61 | 0.17 | 360.52 |

## Cost Statistics (USD)

| Agent | Model | Avg C | Med C | Q1 C | Q3 C | Std C | Min C | Max C |
|-------|-------|-------|-------|------|------|-------|-------|-------|
| OH | o3-mini | 0.55 | 0.35 | 0.17 | 1.11 | 0.56 | 0.01 | 1.34 |
| OH | 3.7 Sonnet | 10.15 | 7.53 | 3.04 | 14.20 | 6.30 | 0.03 | 19.83 |
| OH | Nova Pro | 1.09 | 0.77 | 0.33 | 2.18 | 0.93 | 0.00 | 2.99 |
| OH | 3.5 Haiku | 0.68 | 0.42 | 0.15 | 2.68 | 1.47 | 0.01 | 3.24 |
| OH | DeepSeek R1 | 1.55 | 1.28 | 0.83 | 2.49 | 1.70 | 0.00 | 4.08 |
| IA | 3.5 Haiku | 2.82 | 1.86 | 0.52 | 4.23 | 2.90 | 0.02 | 5.09 |
| IA | Nova Pro | 3.93 | 3.26 | 0.91 | 5.31 | 3.65 | 0.02 | 6.96 |

**Notes**:
- IA models often consumed full 40-minute timeout; OH models frequently stopped early
- IA Haiku and IA Nova Pro have large Std T and Max T due to occasional timeout non-compliance
- OH+o3-mini achieves best cost-performance tradeoff (rank 1, lowest avg cost among competitive models)
- OH+3.7 Sonnet is slowest and most expensive (rank 2, Avg C = $10.15)
- Little correlation found between runtime/cost and overall performance
