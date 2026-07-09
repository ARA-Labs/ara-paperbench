# Table 12: Raw Efficiency Metrics for LLaMA-2 7B
- **Source**: Table 12, Appendix I
- **Caption**: "Raw efficiency metrics, including time to accuracy, training peak memory, inference time, and memory footprints, when using different methods to fine-tune LLaMA2 7B models on Alpaca."
- **Conditions**: LLaMA-2 7B; GPT-4 Alpaca dataset; single A100 GPU; training time in seconds per epoch; training memory in MB; inference time in milliseconds (batch size 32); inference memory in MB

| Method | Train Time (s/epoch) | Train Mem. (MB) | Inf. Time (ms) | Inf Mem (MB) |
|--------|---------------------|-----------------|----------------|--------------|
| LoRA | 32,185 | 2457.5 | (not reported) | 45,311 |
| LoRA+MT (LoRA+Prune, no retrain) | 32,185 | 2127.5 | (not reported) | 31,207 |
| LoRA+MT+retrain | 1,773 | 32,185 | 2127.5 | 31,207 |
| LLMPruner | 23,425 | (not reported) | 2140.6 | 33,625 |
| APT | 1,039 | 24,408 | 2099.7 | 30,469 |

**Note**: The LoRA+MT+retrain row appears to have a data formatting anomaly in the paper (1,773 may be epochs to accuracy rather than time/epoch for the retrain phase). All values transcribed exactly as published.
