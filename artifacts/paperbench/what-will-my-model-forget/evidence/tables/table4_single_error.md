# Table 4: Single Error Fixing — EM Drop Ratio
- **Source**: Table 4, Section 5.2
- **Caption**: "Exact Match Drop ratio (%) when separately fixing single errors in DTest_R. Bold numbers indicate lowest forgetting."

| Model | BART0Large | FLAN-T5Large | FLAN-T5Large | FLAN-T53B |
|-------|-----------|-------------|-------------|----------|
| Dataset DR | P3-Test | MMLU | MMLU | MMLU |
| Tuning | Full FT | LoRA | Full FT | LoRA |
| Vanilla FT | 8.045 | 0.099 | 0.149 | 0.030 |
| Replay w/ Random | 3.938 | 0.105 | 0.068 | −0.018 |
| Replay w/ Threshold | 2.649 | 0.100 | 0.024 | 0.001 |
| Replay w/ Trainable Logit | 2.250 | 0.113 | 0.081 | 0.004 |
| **Replay w/ Representation** | **2.191** | **0.079** | **−0.026** | **−0.020** |
| Replay w/ GT Forget | 0.401 | 0.075 | −0.056 | −0.011 |
