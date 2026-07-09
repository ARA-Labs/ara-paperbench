# Table 6: Hyperparameters Used in APT Experiments
- **Source**: Table 6, Appendix A
- **Caption**: "Hyperparameters used in APT experiments"
- **Note**: Some cells in the original Table 6 are not fully populated in the paper text. Values labeled as "Not specified" were not readable from the paper text.

| Hyperparameter | GLUE-small | GLUE-big | SQuAD | CNN/DM | Alpaca |
|---------------|-----------|---------|-------|--------|--------|
| Learning rate | 2e-4 | 2e-4 | 2e-4 | 1e-4 | 1e-4 |
| Batch size | 32 | 32 | 32 | 16 | Not specified in paper |
| Epochs (total) | 40 | 40 | 40 | 16 | 15 (after pre-tuning pruning) |
| Distill epochs | 20 | 20 | 20 | 6 | — (no distillation for LLaMA) |
| Fine-tune recovery epochs | 20 | 20 | 20 | 10 | — |
| Finetune baseline epochs | 10 | 10 | 10 | 10 | Not specified in paper |
| Initial adapter rank | 8 | 8 | 8 | 8 | 8 |
| LoRA scaling factor (s) | 2 | 2 | 2 | 2 | 2 |

*Note: GLUE-small tasks: MRPC, CoLA, RTE, STS-B. GLUE-big tasks: MNLI, SST2, QNLI, QQP.*
*Note: For Alpaca, 15 epochs refers to the post-pruning fine-tuning; the pre-tuning pruning duration is not specified in terms of epoch count in the main text.*
