# Figure 2a: General Benchmarks — ARC-c, ARC-e, BoolQ, HellaSwag
- **Source**: Figure 2a, Section 3.1
- **Caption**: "Results of general natural language benchmarks. In each cell, the first value is the result for γ=1 (baseline) and the second value is the result for γ=1.5 (ours)."
- **Condition**: Zero-shot evaluation using EleutherAI LM Evaluation Harness; format is "γ=1 / γ=1.5"

| Model | ARC-c | ARC-e | BoolQ | HellaSwag |
|-------|-------|-------|-------|-----------|
| GPT2-small | 22.7 / 23.0 | 39.5 / 42.1 | 48.7 / 57.0 | 31.1 / 31.9 |
| GPT2-medium | 25.0 / 23.9 | 43.6 / 47.6 | 58.6 / 60.1 | 39.4 / 40.9 |
| GPT2-large | 25.1 / 24.7 | 46.6 / 51.0 | 60.5 / 62.1 | 45.3 / 47.1 |
| GPT2-xl | 28.5 / 30.0 | 51.1 / 56.5 | 61.8 / 62.6 | 50.9 / 52.4 |
| Pythia-160M | 23.5 / 23.0 | 39.5 / 42.2 | 55.0 / 58.3 | 30.1 / 31.2 |
| Pythia-410M | 24.1 / 23.8 | 45.7 / 50.3 | 60.6 / 61.2 | 40.6 / 41.6 |
| Pythia-1B | 27.0 / 28.0 | 49.0 / 54.9 | 60.7 / 61.8 | 47.1 / 48.9 |
| Pythia-1.4B | 28.6 / 29.6 | 53.8 / 59.6 | 63.0 / 63.8 | 52.1 / 54.3 |
| Pythia-2.8B | 33.1 / 34.5 | 58.8 / 65.4 | 64.7 / 64.7 | 59.3 / 61.9 |
| Pythia-6.9B | 35.2 / 36.1 | 61.3 / 67.4 | 63.7 / 64.6 | 64.0 / 66.5 |
| Pythia-12B | 36.9 / 38.7 | 64.1 / 72.6 | 67.6 / 67.8 | 67.3 / 69.6 |
| LLaMA-7B | 41.5 / 43.9 | 52.5 / 58.9 | 73.1 / 71.8 | 73.0 / 76.9 |
| LLaMA-13B | 47.8 / 54.2 | 74.8 / 79.1 | 78.0 / 75.8 | 79.1 / 82.1 |
| LLaMA-30B | 52.9 / 57.4 | 78.9 / 83.2 | 82.7 / 80.0 | 82.6 / 85.3 |
| LLaMA-65B | 55.6 / 59.0 | 79.7 / 84.2 | 84.8 / 83.0 | 84.1 / 86.3 |

**Notes:**
- BoolQ shows CFG degradation for LLaMA-7B (73.1 → 71.8), LLaMA-13B (78.0 → 75.8), LLaMA-30B (82.7 → 80.0), LLaMA-65B (84.8 → 83.0)
- ARC-c shows inconsistent improvement (paper notes reasons unknown)
- LLaMA models generally show strong improvement on ARC-c and ARC-e
