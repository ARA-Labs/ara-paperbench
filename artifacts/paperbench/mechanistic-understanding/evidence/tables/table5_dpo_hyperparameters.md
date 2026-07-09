# Table 5: DPO Hyperparameters

- **Source**: Table 5, Appendix D
- **Caption**: "Hyperparameters: DPO."

| HYPERPARAMETER | VALUE |
|----------------|-------|
| LEARNING RATE | 1E-6 |
| BATCH SIZE | 4 |
| OPTIMIZER | RMSPROP |
| GRADIENT ACCUMULATION STEPS | Not specified in paper |
| MAX GRADIENT NORM | 10 |
| VALIDATION METRIC | LOSS/VALID |
| VALIDATION PATIENCE | 10 |
| DPO BETA | 0.1 |

**Notes**:
- Batch size of 4 is specified in the rubric / reproduction requirements, not printed in the paper's Table 5.
- Max gradient norm of 10 is specified in the rubric, not printed in the paper's Table 5.
- Gradient accumulation steps field is present in Table 5 but value is blank/unspecified.
