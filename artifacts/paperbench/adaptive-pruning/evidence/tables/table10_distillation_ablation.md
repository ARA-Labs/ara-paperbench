# Table 10: Ablation Study of Distillation Strategies on RoBERTa SST2
- **Source**: Table 10, Appendix G
- **Caption**: "Ablation study of distillation strategies and comparison to non-efficient distillation techniques. The training speed and memory are relative metrics compared to fine-tuning the dense model."

| Method | SST2 | Train Speed(⇑) | Train Mem(⇓) |
|--------|------|----------------|-------------|
| APT (full, with self-distillation) | 94.5 | 16.9% | 70.1% |
| w/o L_layer (no layer distillation) | 93.7 | 17.4% | 69.8% |
| w/o self-distillation (no distillation) | 92.9 | 20.7% | 69.2% |
| FT teacher (separate fully FT teacher model) | 94.3 | 7.9% | 111.8% |
| LoRA teacher (separate LoRA-tuned teacher) | 93.7 | 1.7% | 96.1% |

*Note: Training speed reported as relative speed (higher = faster); training memory is relative to FT dense model (lower = better).*
*Note: FT teacher cost includes both teacher model training time and student training time.*
*Note: LoRA teacher cost includes both LoRA fine-tuning time and student training time.*
*Note: Training speed for APT is 16.9% meaning APT is roughly 5.9× slower than dense FT but substantially faster than FT teacher (7.9% speed = ~12.7× slower than FT) or LoRA teacher (1.7% speed = ~59× slower than FT).*
