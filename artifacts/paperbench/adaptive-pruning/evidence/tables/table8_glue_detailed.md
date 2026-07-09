# Table 8: Detailed Results of RoBERTa Pruning vs LoRA+Distill Baseline (40% Sparsity)
- **Source**: Table 8, Appendix D.2
- **Caption**: "Detailed results of RoBERTa pruning with APT compared to the LoRA+Distill baseline. We ignore the evaluation results of the STS-B task since it cannot be successfully reproduced with CoFi (the distillation backbone)."

| Sparsity | Method | MNLI | QQP | QNLI | SST2 | CoLA | MRPC | RTE | GLUE Avg. |
|---------|--------|------|-----|------|------|------|------|-----|-----------|
| 0% | FT | 87.6 | 91.9 | 92.8 | 95.2 | 91.2 | 90.2 | 78.7 | 89.7 |
| 0% | LoRA | 87.5 | 90.8 | 93.3 | 95.0 | 63.4 | 89.7 | 72.1 | 84.5 |
| 40% | LoRA+Distill | 84.2 | 88.3 | 90.1 | 91.9 | 49.9 | 86.8 | 68.6 | 80.0 |
| 40% | APT | 86.4 | 90.9 | 92.3 | 94.5 | 56.5 | 92.3 | 74.4 | 83.9 |

*Note: STS-B excluded because CoFi distillation cannot be successfully reproduced with LoRA-only tunable parameters.*
*Note: GLUE Avg. for FT and LoRA is computed over 7 tasks (excluding STS-B); for consistency.*
*Note: APT reaches 93.5% of FT performance on average (83.9/89.7 = 93.5%).*
