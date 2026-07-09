# Table 7: Base LM EM Scores on Upstream Data
- **Source**: Table 7, Appendix B
- **Caption**: "EM scores of base LMs on upstream pretraining data (P3-Train) before performing updates."

| Model | EM Score |
|-------|----------|
| BART0Large | 50.50 |
| FLAN-T5Large | 47.47 |
| FLAN-T53B | 51.31 |

Note: BART0 is exclusively trained on P3-train, while FLAN-T5 models are trained on a mixture of other tasks with potentially different prompt formats. This explains higher EM of BART0Large compared to FLAN-T5Large.
