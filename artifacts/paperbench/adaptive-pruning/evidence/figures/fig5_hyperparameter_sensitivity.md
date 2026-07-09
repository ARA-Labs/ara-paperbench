# Figure 5: Hyperparameter Sensitivity Analysis
- **Source**: Figure 5, Appendix H
- **Caption**: "(a) Comparison of different initial ranks of LoRA layers pruning with APT on RoBERTa with SST2 task accuracy, relative training peak memory and speed to 97% fine-tuning accuracy to the fine-tuning model. (b) Training initial sparsity trade-off with 30% target sparsity model's relative performances to the LoRA-tuned LLaMA2-7B and 13B models."

## Figure 5a: Initial LoRA Rank Sensitivity (RoBERTa SST2, 60% sparsity)

| Initial LoRA Rank | SST2 Accuracy | Relative Train Peak Memory | Relative 97% TTA Speed |
|-------------------|---------------|---------------------------|------------------------|
| 8 (default) | ≈ 94.5 | ≈ 0.70 | ≈ 0.17 |
| 16 | ≈ 94.5 | ≈ 0.75 | ≈ 0.15 |
| 32 | ≈ 94.4 | ≈ 0.85 | ≈ 0.13 |
| 64 | ≈ 94.3 | ≈ 0.95 | ≈ 0.12 |
| 128 | ≈ 94.2 | ≈ 1.05 | ≈ 0.11 |
| 256 | ≈ 93.9 | ≈ 1.25 | ≈ 0.10 |

**Key finding**: Increasing initial rank beyond 8 does not improve accuracy, while memory grows super-linearly. Rank 8 is Pareto-optimal.

## Figure 5b: Initial Density Sensitivity for LLaMA Pruning (30% target sparsity)

### LLaMA-2 7B
| Init Density | ARC | HellaSwag | MMLU | TruthfulQA | Avg. |
|--------------|-----|-----------|------|------------|------|
| 0.7 (prune to target directly) | ≈ 45.4 | ≈ 71.1 | ≈ 36.9 | ≈ 46.6 | ≈ 50.0 |
| 0.85 | ≈ 44.5 | ≈ 70.2 | ≈ 37.5 | ≈ 47.0 | ≈ 49.8 |
| 1.0 (no pre-pruning) | ≈ 43.5 | ≈ 70.0 | ≈ 37.0 | ≈ 48.6 | ≈ 49.8 |

### LLaMA-2 13B
| Init Density | ARC | HellaSwag | MMLU | TruthfulQA | Avg. |
|--------------|-----|-----------|------|------------|------|
| 0.7 | ≈ 49.5 | ≈ 75.8 | ≈ 52.5 | ≈ 44.7 | ≈ 55.6 |
| 0.85 | ≈ 50.0 | ≈ 75.5 | ≈ 52.0 | ≈ 45.5 | ≈ 55.7 |
| 1.0 (no pre-pruning) | ≈ 49.8 | ≈ 75.3 | ≈ 52.0 | ≈ 47.4 | ≈ 56.1 |

**Key finding**: Dense pre-pruning training (init density=1.0) only helps TruthfulQA; harms ARC and HellaSwag (catastrophic forgetting). Default pre-pruning to target density is optimal for most tasks.

**Note**: Figure 5 values are read from plots; marked as ≈ approximate where exact values are not labeled in the figure.
