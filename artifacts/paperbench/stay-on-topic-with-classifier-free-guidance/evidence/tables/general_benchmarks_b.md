# Figure 2b: General Benchmarks — PIQA, SciQ, TriviaQA, WinoGrande, Lambada
- **Source**: Figure 2b, Section 3.1
- **Caption**: "Results of general natural language benchmarks. In each cell, the first value is the result for γ=1 (baseline) and the second value is the result for γ=1.5 (ours). LLaMA 7B with CFG on Lambada zero-shot already outperforms vanilla PaLM 540B, Chinchilla 70B, and GPT-3 175B, tops the SOTA leaderboard for Lambada zero-shot as of June 26th, 2023"
- **Condition**: Zero-shot evaluation using EleutherAI LM Evaluation Harness; format is "γ=1 / γ=1.5"

| Model | PIQA | SciQ | TriviaQA | WinoGrande | Lambada |
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

**Notes:**
- WinoGrande shows consistent degradation with CFG across all models (exception to general trend)
- TriviaQA shows degradation for larger LLaMA models (56.0→52.7 for 7B; 62.4→59.8 for 13B; etc.) — evaluated with substring match per LLaMA methodology
- Lambada shows the most dramatic improvements: GPT2-small 32.6→44.6, LLaMA-7B 73.6→81.3
- LLaMA-7B Lambada 81.3% is SOTA as of June 26, 2023, surpassing PaLM-540B (77.9%), Chinchilla-70B, and GPT-3-175B
