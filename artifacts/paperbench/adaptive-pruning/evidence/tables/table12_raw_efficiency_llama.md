# Table 12: Raw Efficiency Metrics — LLaMA2-7B on Alpaca
- **Source**: Table 12, Appendix I
- **Caption**: "Raw efficiency metrics, including time to accuracy, training peak memory, inference time, and memory footprints, when using different methods to fine-tune LLaMA2 7B models on Alpaca."

| Method | Train Time (s) | Train Mem. (MB) | Inf. Time (ms) | Inf. Mem (MB) |
|--------|---------------|----------------|---------------|--------------|
| LoRA | Not specified in paper | 32,185 | 2457.5 | 45,311 |
| LoRA+MT (Mask Tuning, no retrain) | Not specified in paper | 32,185 | 2127.5 | 31,207 |
| LoRA+MT+retrain | 1,773 | 32,185 | 2127.5 | 31,207 |
| LLMPruner | Not specified in paper | 23,425 | 2140.6 | 33,625 |
| APT | 1,039 | 24,408 | 2099.7 | 30,469 |

*Note: Training times in seconds; inference times in milliseconds; memory in MB.*
*Note: APT training memory (24,408 MB ≈ 23.8 GB) vs LoRA (32,185 MB ≈ 31.4 GB) confirms <24GB claim.*
*Note: LLMPruner training memory (23,425 MB) — this is what is listed in the table but the paper text states LLMPruner costs ~80GB; the table may reflect different measurement conditions or the pruning-phase memory. The paper footnote cites GitHub issue #4 for the 80GB figure.*
*Note: LoRA column for train time not specified in paper (LoRA+MT+retrain and APT training times given as per-step values × epochs; absolute numbers shown here are for the retraining/APT phase only).*
