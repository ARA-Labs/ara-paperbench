# Environment

- **Python**: Not specified in paper
- **Framework**: PyTorch (version not specified in paper); Hugging Face Transformers (version not specified)
- **Hardware**: Single NVIDIA A100 GPU (80GB)
- **Key dependencies**:
  - PyTorch (version not specified in paper)
  - Hugging Face Transformers (version not specified)
  - lm-eval-harness (Gao et al., 2023) for LLaMA evaluation on Open LLM Leaderboard tasks
  - CoFi codebase (https://github.com/princeton-nlp/CoFiPruning) for Prune+Distill baseline
  - Mask Tuning codebase (https://github.com/WoosukKwon/retraining-free-pruning) for LoRA+Prune baseline
  - LLMPruner codebase (https://github.com/horseee/LLM-Pruner) for LLMPruner baseline
- **Random seeds**: Not specified in paper
- **Code repository**: https://github.com/ROIM1998/APT
- **Memory notes**:
  - APT for LLaMA2-7B pruning: <24 GB (fits on consumer-level GPU)
  - LLMPruner for LLaMA2-7B pruning: ~80 GB
  - Prune+Distill (CoFi) for RoBERTa: 4,544 MB (168.5% of FT = 2,696 MB)
  - APT for RoBERTa at 60% sparsity: training memory = 70.1% of FT (absolute: not directly stated for APT row, but FT = 2,696 MB so APT ≈ 1,890 MB; see Table 11 for raw values — some cells not filled in paper)
