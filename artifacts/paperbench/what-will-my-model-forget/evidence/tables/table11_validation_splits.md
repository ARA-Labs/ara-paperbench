---
# Table 11: Performance on Validation Splits of Upstream Pretraining Tasks

**Source**: Table 11, Appendix  
**Claims**: C04  
**Description**: Performance (EM scores) on validation splits of upstream pretraining tasks in same setup as Table 3. Trends mostly align with Table 3 (EM Drop Ratio on DPT).

| Model | FLAN-T5Large | FLAN-T5Large | FLAN-T53B |
|-------|-------------|-------------|-----------|
| Tuning | LoRA | Full FT | LoRA |
| Vanilla FT | 41.06 | 43.25 | 46.64 |
| w/ Random | 42.78 | 43.91 | 47.47 |
| w/ Threshold | 43.92 | 44.56 | 48.56 |
| w/ Trainable Logit | 43.54 | 44.20 | 48.16 |
| w/ Representation | **44.83** | **44.67** | **49.25** |
| w/ GT Forget | **45.00** | 44.85 | 49.74 |
| MIR | 43.33 | 43.91 | 47.79 |
| OCS | 44.17 | 44.56 | 47.68 |

**Notes**:
- Comparison between methods aligns with Table 3, except MIR slightly outperforms OCS on FLAN-T53B LoRA
- Representation-based replay achieves highest EM among non-GT methods in all configurations
