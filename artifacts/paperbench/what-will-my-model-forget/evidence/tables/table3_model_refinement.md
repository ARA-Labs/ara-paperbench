---
# Table 3: Edit Success Rate and EM Drop Ratio — Sequential Model Refinement

**Source**: Table 3, §5.2  
**Claims**: C04  
**Description**: Edit success rate (Succ., %) and Exact Match Drop Ratio (EM Drop, %) when sequentially fixing errors. Lower EM Drop = less forgetting. Bold = best non-GT method. GT Forget = upper bound (computationally infeasible in practice).

| Method | BART0Large Full FT Succ. | BART0Large Full FT EM Drop% | FLAN-T5Large LoRA Succ. | FLAN-T5Large LoRA EM Drop% | FLAN-T5Large Full FT Succ. | FLAN-T5Large Full FT EM Drop% | FLAN-T53B LoRA Succ. | FLAN-T53B LoRA EM Drop% |
|--------|--------------------------|------------------------------|-------------------------|---------------------------|----------------------------|-------------------------------|----------------------|------------------------|
| Vanilla FT | 90.4 | 9.274 | 67.4 | 5.463 | 82.6 | 3.302 | 78.3 | 4.384 |
| w/ Random | 91.7 | 5.769 | 71.7 | 3.267 | 82.6 | 1.129 | 80.0 | 1.910 |
| w/ Threshold | 91.3 | 4.646 | 78.3 | 1.489 | 82.6 | 0.631 | 81.7 | 1.198 |
| w/ Trainable Logit | 91.4 | **1.826** | 76.1 | 2.565 | 82.6 | 0.898 | 82.5 | 1.516 |
| w/ Representation | 91.7 | **1.634** | 73.9 | **0.301** | 82.6 | **0.582** | 83.3 | **0.138** |
| w/ GT Forget | 92.2 | 0.895 | 76.1 | 0.189 | 82.6 | 0.560 | 85.0 | 0.030 |
| MIR | 91.4 | 5.024 | 69.6 | 2.656 | 82.6 | 1.117 | 80.0 | 1.681 |
| OCS | 91.8 | 3.573 | 71.7 | 0.984 | 82.6 | 0.675 | 81.7 | 1.435 |

**Notes**:
- DR for BART0Large = P3-Test; DR for FLAN-T5 = MMLU
- All methods above 95% edit success rate immediately after single-error fix; sequential fixing reduces this
- Representation-based replay achieves lowest EM Drop in 3 of 4 configurations (bold)
- Trainable Logit achieves lowest non-GT EM Drop on BART0 Full FT among some configs (1.826%)
- MIR only marginally improves over Random due to large DPT and sparse forgotten examples
- GT Forget = computationally expensive upper bound
