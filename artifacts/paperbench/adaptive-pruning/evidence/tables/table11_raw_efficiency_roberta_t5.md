# Table 11: Raw Efficiency Metrics — RoBERTa-base and T5-base on SST2
- **Source**: Table 11, Appendix I
- **Caption**: "Raw efficiency metrics, including time to accuracy, training peak memory, inference time and memory footprints, when using different methods to fine-tune RoBERTabase and T5base models on SST2."

| Model | Method | Sparsity | 97% TTA (s) | Train Mem. (MB) | Inf. Time (ms) | Inf. Mem (MB) |
|-------|--------|---------|------------|----------------|---------------|--------------|
| RoBERTabase | FT | 0% | 2,696 | Not specified in paper | 220.8 | 1,157 |
| RoBERTabase | LoRA | 0% | Not specified in paper | 1,630 | 181.8 | 1,157 |
| RoBERTabase | LoRA+Prune | 60% | 6,513 | 1,630 | 84.0 | Not specified in paper |
| RoBERTabase | Prune+Distill | 60% | 1,899 | 4,544 | 85.2 | Not specified in paper |
| RoBERTabase | LoRA+Prune+Distill | 60% | 8,299 | 3,813 | 87.0 | Not specified in paper |
| RoBERTabase | APT | 60% | 752 | Not specified in paper | 91.3 | Not specified in paper |
| T5base | FT | 0% | 7,217 | Not specified in paper | 248.1 | 2,347 |
| T5base | LoRA | 0% | 4,476 | Not specified in paper | 254.2 | 2,347 |
| T5base | LoRA+Prune | 60% | 14,417 | 4,476 | 116.8 | 1,724 |
| T5base | APT | 60% | 1,774 | 5,332 | 185.0 | 1,913 |

*Note: Some cells in the original Table 11 are not filled in the paper (indicated as "Not specified in paper" above).*
*Note: Training times are in seconds; inference times are in milliseconds; memory in MB.*
*Note: APT RoBERTa TTA (752s) vs LoRA+Prune TTA (6,513s) gives speedup ratio of approximately 8.7×. APT T5 TTA (1,774s) vs LoRA+Prune T5 TTA (14,417s) gives 8.13× speedup.*
*Note: Relative metrics in Table 2 are computed from these raw values normalized to FT baseline TTA.*
