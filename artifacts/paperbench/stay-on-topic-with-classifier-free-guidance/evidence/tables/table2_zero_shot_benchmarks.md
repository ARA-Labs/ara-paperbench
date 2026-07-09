# Zero-Shot Benchmark Results: GPT-2, Pythia, and LLaMA Families
- **Source**: Figure 2 (Tables 2a and 2b), Section 3.1
- **Caption**: "Results of general natural language benchmarks. In each cell, the first value is the result for γ=1 (baseline) and the second value is the result for γ=1.5 (ours). LLaMA 7B with CFG on Lambada zero-shot already outperforms vanilla PaLM 540B, Chinchilla 70B, and GPT-3 175B, tops the SOTA leaderboard for Lambada zero-shot as of June 26th, 2023"
- **Conditions**: Zero-shot, evaluated using EleutherAI Language Model Evaluation Harness; format: baseline (γ=1) / CFG (γ=1.5)

## Table 2a: ARC-c, ARC-e, BoolQ, HellaSwag

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

## Table 2b: PIQA, SCIQ, TriviaQA, WinoGrande, Lambada

| Model | PIQA | SCIQ | TriviaQA | WinoGrande | Lambada |
|-------|------|------|----------|------------|---------|
| GPT2-small | 62.5 / 63.8 | 64.4 / 70.8 | 5.5 / 6.5 | 51.6 / 50.5 | 32.6 / 44.6 |
| GPT2-medium | 66.4 / 66.9 | 67.2 / 76.7 | 8.3 / 9.3 | 53.1 / 52.1 | 43.0 / 55.8 |
| GPT2-large | 69.2 / 70.2 | 69.4 / 78.8 | 11.1 / 12.0 | 55.4 / 54.4 | 47.7 / 60.5 |
| GPT2-xl | 70.5 / 71.3 | 76.1 / 82.4 | 14.7 / 15.2 | 58.3 / 55.6 | 51.2 / 62.5 |
| Pythia-160M | 61.4 / 62.1 | 67.0 / 75.4 | 4.1 / 5.3 | 52.3 / 51.1 | 32.8 / 47.4 |
| Pythia-410M | 67.1 / 67.8 | 72.1 / 79.0 | 7.9 / 9.1 | 52.9 / 50.7 | 51.3 / 64.0 |
| Pythia-1B | 69.2 / 70.5 | 76.0 / 82.9 | 12.3 / 12.3 | 53.9 / 51.5 | 56.2 / 69.0 |
| Pythia-1.4B | 71.1 / 72.5 | 79.4 / 85.1 | 15.9 / 15.9 | 57.4 / 56.0 | 61.6 / 72.7 |
| Pythia-2.8B | 73.6 / 75.8 | 83.3 / 88.2 | 22.1 / 20.9 | 60.1 / 57.9 | 64.6 / 76.5 |
| Pythia-6.9B | 76.3 / 77.4 | 84.3 / 89.7 | 28.2 / 27.2 | 61.1 / 60.3 | 67.1 / 78.8 |
| Pythia-12B | 77.0 / 78.4 | 87.7 / 91.9 | 33.4 / 32.1 | 65.0 / 63.4 | 70.4 / 80.6 |
| LLaMA-7B | 77.4 / 79.8 | 66.3 / 75.4 | 56.0 / 52.7 | 67.1 / 65.5 | 73.6 / 81.3 |
| LLaMA-13B | 80.1 / 80.9 | 91.1 / 95.1 | 62.4 / 59.8 | 72.8 / 71.5 | 76.2 / 82.2 |
| LLaMA-30B | 82.3 / 82.3 | 94.3 / 96.4 | 69.7 / 67.9 | 75.8 / 74.1 | 77.5 / 83.9 |
| LLaMA-65B | 82.3 / 82.6 | 95.1 / 96.6 | 73.3 / 71.8 | 77.4 / 76.1 | 79.1 / 84.0 |

**Note**: LLaMA-7B with CFG (γ=1.5) achieves **81.3%** on Lambada, surpassing PaLM-540B zero-shot (77.9%).
