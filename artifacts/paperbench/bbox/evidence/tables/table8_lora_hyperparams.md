# Table 8: SFT-LoRA Hyperparameter Settings
- **Source**: Table 8, Appendix F.2
- **Caption**: "Hyperparameter settings of SFT-LoRA (Hu et al., 2021)."
- **Conditions**: Applied to Mixtral-8×7B fine-tuning on StrategyQA; run on 4× NVIDIA A100-SXM4-80GB GPUs; using HuggingFace peft and transformers

| Hyperparameter | Value |
|----------------|-------|
| LoRA Dropout | 0.1 |
| # Epochs | 3 |
| Learning Rate | 2e-4 |
| Weight Decay | 0.001 |
| Batch Size / GPU | 8 |
| Max Gradient Norm | 0.3 |
| Optimizer | Paged AdamW 32bit |
| LR Scheduler | Cosine |

**Note**: LoRA rank r=128 for 0.1B adapter comparison, r=384 for 0.3B; alpha=2r in both cases (per Hu et al., 2021 recommendation).
