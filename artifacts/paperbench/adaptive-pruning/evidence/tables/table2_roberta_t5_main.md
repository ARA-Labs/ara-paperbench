# Table 2: RoBERTa and T5 Pruning with APT at 60% Sparsity
- **Source**: Table 2, Section 5.4
- **Caption**: "RoBERTa and T5 pruning with APT compared to baselines under 60% sparsity. We measure the training and inference efficiency with LMs pruned on the SST2 task. Training speed is measured via 97% accuracy TTA. All efficiency metrics are normalized to FT. ⇓ denotes smaller is better. The best-pruned results are bold."

| Model | Method | MNLI | SST2 | SQuAD v2 | CNN/DM | Train Time(⇓) | Train Mem(⇓) | Inf Time(⇓) | Inf Mem(⇓) |
|-------|--------|------|------|----------|--------|--------------|-------------|------------|----------|
| RoBERTabase | FT | 87.6 | 94.8 | 82.9 | — | 100.0% | 100.0% | 100.0% | 100.0% |
| RoBERTabase | LoRA | 87.5 | 95.1 | 83.0 | — | 2137.0% | 60.5% | 100.0% | 100.0% |
| RoBERTabase | LoRA+Prune | 84.0 | 93.0 | 79.2 | — | 5128.3% | 60.5% | 38.0% | 75.1% |
| RoBERTabase | Prune+Distill | 87.3 | 94.5 | — | — | 1495.3% | 168.5% | 38.6% | 79.2% |
| RoBERTabase | LoRA+Prune+Distill | 84.2 | 91.9 | — | — | 6534.6% | 141.4% | 39.4% | 82.3% |
| RoBERTabase | APT | 86.4 | 94.5 | 81.8 | — | 592.1% | 70.1% | 41.3% | 78.1% |
| T5base | FT | 87.1 | 95.2 | — | 42.1/20.3/39.4 | 100.0% | 100.0% | 100.0% | 100.0% |
| T5base | LoRA | 87.0 | 95.0 | — | 38.7/17.2/36.0 | 255.5% | 62.0% | 100.0% | 100.0% |
| T5base | LoRA+Prune | 80.9 | 92.3 | — | 36.7/15.7/33.9 | 4523.5% | 62.0% | 47.1% | 73.4% |
| T5base | APT | 87.0 | 95.0 | — | 38.6/17.0/35.8 | 484.7% | 73.9% | 74.6% | 81.5% |

*Note: CNN/DM scores are ROUGE-1/ROUGE-2/ROUGE-L. SQuAD v2 score is F1. MNLI and SST2 scores are accuracy.*
*Note: LoRA for RoBERTa Train Time of 2137.0% reflects longer convergence (Ding et al., 2023).*
