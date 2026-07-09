# Table 6: Comparison with MEND on FLAN-T5Large LoRA (Single Error)
- **Source**: Table 6, Appendix A
- **Caption**: "Comparison of edit success rate and EM Drop % between replay-based model refinement and MEND on FLAN-T5Large with LoRA fine-tuning when fixing a single error."

| Method | Edit Succ. (%) | EM Drop (%) |
|--------|---------------|------------|
| Vanilla FT | 95.7 | 0.099 |
| Replay w/ Random | 95.7 | 0.105 |
| Replay w/ Representation | 95.7 | 0.079 |
| Replay w/ GT Forget | 95.7 | 0.075 |
| MEND | 93.1 | 0.060 |
| MEND w/o Forget Objective | 93.1 | 0.610 |

Note: MEND achieves lower EM Drop than all replay methods, but at a cost of lower edit success rate (93.1% vs. 95.7%). The forget objective in MEND is crucial — removing it causes EM Drop to increase to 0.610%.
