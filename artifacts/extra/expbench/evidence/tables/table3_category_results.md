# Table 3: Category-Level Benchmark Scores (Select Categories)
- **Source**: Table 3, Section 4.1
- **Caption**: "Average benchmark scores of various models and agents across select task categories; see Supp. D for complete list. Evaluation performed against EXP-Bench."
- **Conditions**: Same as Table 1; categories shown: Applications, RL; Agent column omitted in original (implied OH for top block, IA for bottom block based on context)

| Category | Agent | Model | D | I | E | C | I·E | All✓ | All✓·E |
|----------|-------|-------|---|---|---|---|-----|-------|--------|
| Applications | (OH) | Nova Pro | 19.2 | 23.9 | 19.0 | 0.0 | 13.9 | 0.0 | 0.0 |
| Applications | (OH) | o3-mini | 9.0 | 8.0 | 0.0 | 0.0 | 8.3 | 0.0 | 0.0 |
| Applications | (OH) | 3.5 Haiku | 19.2 | 24.5 | 8.3 | 5.6 | 8.3 | 0.0 | 0.0 |
| Applications | (OH) | 3.7 Sonnet | 9.0 | 26.8 | 30.8 | 7.7 | 8.3 | 2.8 | 0.0 |
| Applications | (IA) | Nova Pro | 0.0 | 9.8 | 5.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Applications | (IA) | 3.5 Haiku | 0.0 | 18.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Applications | (OH) | DeepSeek R1 | 3.1 | 4.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| RL | (OH) | 3.7 Sonnet | 18.3 | 48.2 | 27.3 | 21.2 | 17.6 | 2.0 | 3.0 |
| RL | (OH) | o3-mini | 23.5 | 34.8 | 15.7 | 2.0 | 27.5 | 3.9 | 0.0 |
| RL | (OH) | 3.5 Haiku | 27.7 | 41.4 | 11.5 | 0.0 | 17.6 | 0.0 | 0.0 |
| RL | (IA) | 3.5 Haiku | 3.3 | 27.5 | 17.4 | 0.0 | 2.4 | 0.0 | 0.0 |
| RL | (OH) | DeepSeek R1 | 5.0 | 10.3 | 0.0 | 0.0 | 2.0 | 0.0 | 0.0 |
| RL | (IA) | Nova Pro | 0.0 | 8.6 | 9.7 | 0.0 | 0.0 | 0.0 | 0.0 |
| RL | (OH) | Nova Pro | 17.9 | 28.9 | 0.0 | 0.0 | 13.7 | 0.0 | 0.0 |

**Notes**:
- RL category: several OH models achieve up to ≈41% on I metric (averaged over 36 tasks)
- RL is the highest-performing category for implementation correctness
