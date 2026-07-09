# Figure 2(b): Effects of Number of Prompt Embeddings Np
- **Source**: Figure 2(b), Section 4.3
- **Caption**: "Parameter sensitivity analyses of our FOA. Experiments are conducted on ImageNet-C (Gaussian Noise, level 5) with ViT-Base. (b) Effects of #Prompts."
- **Dataset**: ImageNet-C Gaussian Noise, severity level 5
- **Model**: ViT-Base, full precision 32-bit, batch size 64
- **Axes**: X-axis: Number of Prompt Embeddings Np (1–10); Y-axis left: Accuracy (%); Y-axis right: ECE (%)
- **Note**: Exact per-point values not reported numerically in paper; approximate readings from figure

| Np | FOA Acc. (%) | NoAdapt Acc. (%) | FOA ECE (%) | NoAdapt ECE (%) |
|----|-------------|-----------------|-------------|-----------------|
| 1 | ≈60.0 | 56.8 | ≈3.5 | 7.5 |
| 2 | ≈60.8 | 56.8 | ≈3.0 | 7.5 |
| 3 | ≈61.5 | 56.8 | ≈2.5 | 7.5 |
| 4 | ≈61.0 | 56.8 | ≈3.0 | 7.5 |
| 5 | ≈62.0 | 56.8 | ≈2.5 | 7.5 |
| 6 | ≈61.5 | 56.8 | ≈2.5 | 7.5 |
| 7 | ≈62.0 | 56.8 | ≈2.5 | 7.5 |
| 8 | ≈61.0 | 56.8 | ≈3.0 | 7.5 |
| 9 | ≈61.0 | 56.8 | ≈3.0 | 7.5 |
| 10 | ≈60.5 | 56.8 | ≈3.5 | 7.5 |

Notes:
- All values are approximate (≈) from figure; exact values not reported in text
- Paper states: "only minor variations across different Np"; Np=5/7 marginally better
- Default Np=3 used for all main experiments
