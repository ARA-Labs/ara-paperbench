# Table 8: FLOP Counts for Forecasting Methods
- **Source**: Table 8, Appendix C
- **Caption**: "Number of FLOPs when forecasting forgotten examples among 3,600 upstream pretraining examples given one online learning example."
- **Conditions**: FLAN-T5Large, Full FT; 36 tasks × 100 examples = 3,600 upstream examples

| Method | # FLOPs |
|--------|---------|
| Representation | 1.35e10 |
| Trainable Logit | 2.15e11 |
| Ground Truth | 9.04e14 |

Note: Representation requires 1/6700 the FLOPs of Ground Truth. Trainable Logit requires 1/42 the FLOPs of Ground Truth.
