# Table 8: UCF101 Results with Different ViT Training Parameters
- **Source**: Table 8, Appendix C
- **Caption**: "Results on UCF101 with Different Training Parameters (using ViT-B32)"
- **Experimental conditions**: ViT-B32 pretrained on ImageNet-1K; UCF101 dataset; ILM output mapping; 200 epochs; SMM (Ours) method; comparing unified vs. specific learning parameters

| LEARNING PARAMETER TYPE | INITIAL LR (α) | LR DECAY (γ) | SMM ACCURACY (%) |
|-------------------------|----------------|--------------|-----------------|
| UNIFIED LEARNING PARAMETERS | 0.001 | 1 | 42.6 |
| SPECIFIC LEARNING PARAMETERS | 0.01 | 0.1 | 49.9 |

**Note**: The main Table 2 reports 42.6% (unified parameters) for UCF101. With dataset-specific LR=0.01 and γ=0.1, SMM achieves 49.9% which exceeds all baselines (Narrow: 44.5%, Medium: 44.8%, Full: 40.9%, Pad: 33.6%).
