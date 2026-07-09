# Table 7: ViT LR and Decay Hyperparameter Tuning
- **Source**: Table 7, Appendix C
- **Caption**: "Tuning Initial Learning Rate and Learning Rate Decay Using CIFAR10 and ViT-B32 (Accuracy %)"
- **Axis labels**: Rows: γ (learning rate decay); Columns: α (initial learning rate)
- **Experimental conditions**: ViT-B32 pretrained on ImageNet-1K; CIFAR10 dataset; grid search over initial LR × decay factor combinations; ILM output mapping; 200 epochs

| γ \ α | 0.1 | 0.01 | 0.001 | 0.0001 |
|-------|-----|------|-------|--------|
| **1** | 0.9542 | 0.9577 | **0.9745** | 0.9734 |
| **0.1** | 0.9516 | 0.9572 | 0.9738 | 0.9727 |

**Note**: Best configuration is α=0.001, γ=1 (no decay) achieving 97.45% on CIFAR10. This configuration is adopted as the default for all ViT experiments except UCF101.
