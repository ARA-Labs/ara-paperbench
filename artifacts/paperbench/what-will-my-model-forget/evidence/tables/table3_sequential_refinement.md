# Table 3: Sequential Model Refinement Results
- **Source**: Table 3, Section 5.2
- **Caption**: "Edit success rate (Succ.) and Exact Match Drop Ratio (EM Drop %) of model refinement while sequentially fixing errors in DTest_R. Lower EM Drop % indicates reduced forgetting. Bold numbers indicate lowest forgetting achieved by methods other than utilizing ground truth forgetting (GT Forget), which is computationally inefficient in practice."

## BART0Large — Full FT / P3-Test

| Methods | Succ. (%) | EM Drop (%) |
|---------|-----------|------------|
| Vanilla FT | 90.4 | 9.274 |
| Replay w/ Random | 91.7 | 5.769 |
| Replay w/ Threshold | 91.3 | 4.646 |
| Replay w/ Trainable Logit | 91.4 | 1.826 |
| **Replay w/ Representation** | **91.7** | **1.634** |
| Replay w/ GT Forget | 92.2 | 0.895 |
| MIR | 91.4 | 5.024 |
| OCS | 91.8 | 3.573 |

## FLAN-T5Large — LoRA / MMLU

| Methods | Succ. (%) | EM Drop (%) |
|---------|-----------|------------|
| Vanilla FT | 67.4 | 5.463 |
| Replay w/ Random | 71.7 | 3.267 |
| Replay w/ Threshold | 78.3 | 1.489 |
| Replay w/ Trainable Logit | 76.1 | 2.565 |
| **Replay w/ Representation** | **73.9** | **0.301** |
| Replay w/ GT Forget | 76.1 | 0.189 |
| MIR | 69.6 | 2.656 |
| OCS | 71.7 | 0.984 |

## FLAN-T5Large — Full FT / MMLU

| Methods | Succ. (%) | EM Drop (%) |
|---------|-----------|------------|
| Vanilla FT | 82.6 | 3.302 |
| Replay w/ Random | 82.6 | 1.129 |
| Replay w/ Threshold | 82.6 | 0.631 |
| Replay w/ Trainable Logit | 82.6 | 0.898 |
| **Replay w/ Representation** | **82.6** | **0.582** |
| Replay w/ GT Forget | 82.6 | 0.560 |
| MIR | 82.6 | 1.117 |
| OCS | 82.6 | 0.675 |

## FLAN-T53B — LoRA / MMLU

| Methods | Succ. (%) | EM Drop (%) |
|---------|-----------|------------|
| Vanilla FT | 78.3 | 4.384 |
| Replay w/ Random | 80.0 | 1.910 |
| Replay w/ Threshold | 81.7 | 1.198 |
| Replay w/ Trainable Logit | 82.5 | 1.516 |
| **Replay w/ Representation** | **83.3** | **0.138** |
| Replay w/ GT Forget | 85.0 | 0.030 |
| MIR | 80.0 | 1.681 |
| OCS | 81.7 | 1.435 |
