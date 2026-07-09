# Table 3: LLaMA-2 7B 30% Sparsity Pruning Results
- **Source**: Table 3, Section 5.4
- **Caption**: "LLaMA 2 7B 30% sparsity pruning results with GPT4-generated Alpaca dataset, evaluated on the Open LLM leaderboard few-shot tasks. Training speed is measured via training time per step. We do not compare to distillation baselines because the training cost of distillation is too large, and we also compare APT to LLMPruner since it is dedicated to large LM pruning. All efficiency metrics are normalized to LoRA. ⇓ denotes smaller is better. The best-pruned results are bold. Raw efficiency results are reported in Table 12."
- **Conditions**: 30% target sparsity (70% parameters remaining); GPT-4 Alpaca dataset; 25-shot ARC, 10-shot HellaSwag, 5-shot MMLU, 0-shot TruthfulQA; single A100 GPU; inference batch size 32; all efficiency metrics normalized to LoRA (LoRA = 100%)

| Method | ARC | HellaSwag | MMLU | TruthfulQA | Avg. | Train Time(↓) | Train Mem(↓) | Inf Time(↓) | Inf Mem(↓) |
|--------|-----|-----------|------|------------|------|---------------|--------------|-------------|------------|
| LLaMA 2 7B (base) | 53.1 | 77.7 | 43.8 | 39.0 | 53.4 | - | - | - | - |
| LoRA | 55.6 | 79.3 | 46.9 | 49.9 | 57.9 | 100.0% | 100.0% | 100.0% | 100.0% |
| LoRA+Prune | 46.8 | 65.2 | 23.9 | 46.2 | 45.5 | 180.9% | 100.0% | 115.5% | 68.9% |
| LLMPruner | 39.2 | 67.0 | 24.9 | 40.6 | 42.9 | 86.9% | 253.6% | 114.8% | 74.2% |
| APT | 45.4 | 71.1 | 36.9 | 46.6 | 50.0 | 106.0% | 75.8% | 117.0% | 67.2% |
