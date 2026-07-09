# Figure 3: Task Performance vs. Inference Efficiency Pareto Curves
- **Source**: Figure 3, Section 5.5
- **Caption**: "Task performance v.s. relative inference efficiency on RoBERTa, T5, and LLaMA-2 7B models with APT and baselines."
- **X-axis (left plots)**: Relative inference speedup (throughput ratio vs. dense LoRA baseline)
- **Y-axis (left plots)**: Relative task accuracy (fraction of full fine-tuning accuracy)
- **X-axis (right note)**: Inference memory reduction (fraction of dense model memory)
- **Methods shown**: APT, LoRA+Prune, Prune+Distill (RoBERTa only), LoRA+Prune+Distill (RoBERTa only), LLMPruner (LLaMA only)

## Quantitative Observations from Section 5.5

### RoBERTa-base (multiple sparsity levels: 40%, 50%, 60%, 70%, 80%, 90%, 95%)
| Observation | Value |
|-------------|-------|
| APT inference speedup advantage vs. LoRA+Prune at iso-accuracy | ≈ 21.8% more |
| APT memory efficiency advantage vs. LoRA+Prune at iso-accuracy | ≈ 7% more |

### T5-base (multiple sparsity levels: 40%, 50%, 60%, 70%, 80%, 90%)
| Observation | Value |
|-------------|-------|
| APT inference speedup advantage vs. LoRA+Prune at 97% accuracy | ≈ 62.7% more |
| APT memory reduction advantage vs. LoRA+Prune at 97% accuracy | ≈ 24.8% more |

### LLaMA-2 7B (multiple sparsity levels)
| Observation | Value |
|-------------|-------|
| APT inference speedup advantage vs. LoRA+Prune at >85% accuracy | ≈ 6.7% more |
| APT memory reduction advantage vs. LoRA+Prune at >85% accuracy | ≈ 9.2% more |
| APT task performance at >85% of dense model performance | Maintained |

## Specific Data Points at 60% Sparsity (from Table 2/3)

### RoBERTa-base
| Method | Inf Speedup (vs FT) | Inf Mem (vs FT) | Relative Accuracy |
|--------|---------------------|-----------------|-------------------|
| LoRA+Prune | 1/0.38 ≈ 2.63× | 75.1% | ≈ 92.3% |
| Prune+Distill | 1/0.386 ≈ 2.59× | 79.2% | ≈ 97.8% |
| APT | 1/0.413 ≈ 2.42× | 78.1% | ≈ 97.8% |

### T5-base
| Method | Inf Speedup (vs FT) | Inf Mem (vs FT) | Relative Accuracy (SST2+MNLI avg) |
|--------|---------------------|-----------------|-----------------------------------|
| LoRA+Prune | 1/0.471 ≈ 2.12× | 73.4% | ≈ 91.9% |
| APT | 1/0.746 ≈ 1.34× | 81.5% | ≈ 97.0% |
