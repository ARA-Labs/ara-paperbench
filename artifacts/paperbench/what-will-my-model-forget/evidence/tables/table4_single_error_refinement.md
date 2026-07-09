# Table 4: Single-Error Model Refinement Results
- **Source**: Table 4, Section 5.2
- **Caption**: "Exact Match Drop ratio (%) when separately fixing single errors in D^Test_R. Bold numbers indicate lowest forgetting."

**Experimental conditions**: Each error in D^Test_R is fixed independently (not sequentially); EM Drop Ratio averaged over all D^Test_R test examples.

| Model | BART0Large (P3-Test, Full FT) | FLAN-T5Large (MMLU, Full FT) | FLAN-T5Large (MMLU, LoRA) | FLAN-T53B (MMLU, LoRA) |
|-------|-------------------------------|------------------------------|---------------------------|------------------------|
| Tuning | Full FT | Full FT | LoRA | LoRA |
| Vanilla FT | 8.045 | 0.149 | 0.099 | 0.030 |
| Replay w/ Random | 3.938 | 0.068 | 0.105 | −0.018 |
| Replay w/ Threshold | 2.649 | 0.024 | 0.100 | 0.001 |
| Replay w/ Trainable Logit | 2.250 | 0.081 | 0.113 | 0.004 |
| Replay w/ Representation | **2.191** | **−0.026** | **0.079** | **−0.020** |
| Replay w/ GT Forget | 0.401 | −0.056 | 0.075 | −0.011 |
