# Table 11: Raw Efficiency Metrics for RoBERTa-base and T5-base
- **Source**: Table 11, Appendix I
- **Caption**: "Raw efficiency metrics, including time to accuracy, training peak memory, inference time and memory footprints, when using different methods to fine-tune RoBERTabase and T5base models on SST2."
- **Conditions**: SST2 task; single A100 GPU; training time = 97% TTA in seconds; training memory in MB; inference time in milliseconds (batch size 128); inference memory in MB

| Model | Method | Sparsity | 97% TTA (s) | Train Mem. (MB) | Inf. Time (ms) | Inf Mem (MB) |
|-------|--------|----------|-------------|-----------------|----------------|--------------|
| RoBERTa-base | FT | - | 2,696 | 2,696 | 220.8 | 1,157 |
| RoBERTa-base | LoRA | - | 2,714 | 1,630 | 181.8 | 1,157 |
| RoBERTa-base | LoRA+Prune | 60% | 6,513 | 1,630 | 84.0 | (not reported) |
| RoBERTa-base | Prune+Distill | 60% | 1,899 | 4,544 | 85.2 | (not reported) |
| RoBERTa-base | LoRA+Prune+Distill | 60% | 8,299 | 3,813 | 87.0 | (not reported) |
| RoBERTa-base | APT | 60% | 752 | (not reported) | 91.3 | (not reported) |
| T5-base | FT | - | 7,217 | (not reported) | 248.1 | 2,347 |
| T5-base | LoRA | - | 4,476 | (not reported) | 254.2 | 2,347 |
| T5-base | LoRA+Prune | 60% | 14,417 | 4,476 | 116.8 | 1,724 |
| T5-base | APT | 60% | 1,774 | 5,332 | 185.0 | 1,913 |

**Note**: Some cells are not reported in the published table (paper Table 11 has partial data). The exact values reported in the paper are transcribed above.
