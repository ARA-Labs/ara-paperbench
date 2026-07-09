# Figure 3: Task Performance vs Relative Inference Efficiency
- **Source**: Figure 3, Section 5.5
- **Caption**: "Task performance v.s. relative inference efficiency on RoBERTa, T5, and LLaMA-2 7B models with APT and baselines."
- **Axis labels**:
  - X-axis (left panels): Inf. Speedup (relative to FT or LoRA)
  - X-axis (right panels): Inf. Mem. Red. (relative memory reduction, lower = more efficient)
  - Y-axis: Relative Accuracy (fraction of dense FT model performance) or task score
- **Note**: Figure 3 contains curves showing multiple sparsity settings for APT and single points for baselines. Exact data points are not fully readable from the figure text; quantitative summary extracted from Section 5.5 text below.

## Quantitative Data Points (extracted from Section 5.5 narrative)

### RoBERTa — APT vs LoRA+Prune at Same Target Task Performance
| Comparison | APT Advantage |
|-----------|--------------|
| Inference speedup vs LoRA+Prune (same accuracy) | APT is 21.8% faster |
| Inference memory vs LoRA+Prune (same accuracy) | APT is 7% more memory-efficient |

### T5 — APT vs LoRA+Prune at 97% Dense Model Performance
| Comparison | APT Advantage |
|-----------|--------------|
| Inference speedup vs LoRA+Prune (97% accuracy) | APT has 62.7% more inference speedup |
| Inference memory vs LoRA+Prune (97% accuracy) | APT has 24.8% more inference memory reduction |

### LLaMA2-7B — APT vs LoRA+Prune (>85% task performance)
| Comparison | APT Advantage |
|-----------|--------------|
| Inference speedup vs LoRA+Prune (>85% accuracy) | APT is 6.7% more speedup |
| Inference memory vs LoRA+Prune (>85% accuracy) | APT reduces 9.2% more inference memory |

## Approximate Sparsity Range for APT Curves (from §5.5 and Appendix F)
| Model | Sparsity Range Analyzed |
|-------|------------------------|
| RoBERTa | 40%, 50%, 60%, 70%, 80%, 90%, 95% |
| T5 | 40%, 50%, 60%, 70%, 80%, 90% |
| LLaMA2-7B | 30%, 50% (from Table 5) |

## Baseline Points (from Table 2/3 at 60% / 30% sparsity)
| Model | Method | Inf. Speedup (vs FT) | Task Accuracy (relative) |
|-------|--------|---------------------|------------------------|
| RoBERTa | LoRA+Prune | 1/0.38 ≈ 2.63× | (84.0+93.0)/(87.6+94.8) ≈ 97.3% |
| RoBERTa | Prune+Distill | 1/0.386 ≈ 2.59× | (87.3+94.5)/(87.6+94.8) ≈ 99.8% |
| RoBERTa | APT | 1/0.413 ≈ 2.42× | (86.4+94.5)/(87.6+94.8) ≈ 98.8% |
| T5 | LoRA+Prune | 1/0.471 ≈ 2.12× | (80.9+92.3)/(87.1+95.2) ≈ 94.8% |
| T5 | APT | 1/0.746 ≈ 1.34× | (87.0+95.0)/(87.1+95.2) ≈ 99.8% |
