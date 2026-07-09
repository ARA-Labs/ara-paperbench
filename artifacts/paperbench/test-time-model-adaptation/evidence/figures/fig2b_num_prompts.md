---
# Figure 2(b): Effects of Number of Prompt Embeddings Np
- **Source**: Figure 2(b), Section 4.3
- **Caption**: "Effects of #Prompts — Parameter sensitivity analyses of our FOA. Experiments are conducted on ImageNet-C (Gaussian Noise, level 5) with ViT-Base."
- **Conditions**: ViT-Base (full precision, 32-bit); ImageNet-C, Gaussian noise, severity level 5; batch size 64; K=28
- **Axes**: X-axis: Number of prompt embeddings Np ∈ {1, 2, ..., 10}; Y-axis (left): Accuracy (%); Y-axis (right): ECE (%)
- **Series**: Acc FOA (ours), Acc NoAdapt, ECE FOA (ours), ECE NoAdapt

## Key Data Points (Extracted from Figure 2b)

| Np | FOA Acc. (%) | NoAdapt Acc. (%) | FOA ECE (%) | NoAdapt ECE (%) |
|----|-------------|-----------------|-------------|-----------------|
| 1 | ≈61.0 | ≈56.8 | ≈3.5 | ≈7.5 |
| 2 | ≈61.2 | ≈56.8 | ≈3.2 | ≈7.5 |
| 3 | ≈61.5 | ≈56.8 | ≈2.5 | ≈7.5 |
| 4 | ≈61.2 | ≈56.8 | ≈2.8 | ≈7.5 |
| 5 | ≈61.8 | ≈56.8 | ≈2.6 | ≈7.5 |
| 6 | ≈61.5 | ≈56.8 | ≈2.7 | ≈7.5 |
| 7 | ≈61.8 | ≈56.8 | ≈2.5 | ≈7.5 |
| 8 | ≈61.3 | ≈56.8 | ≈2.9 | ≈7.5 |
| 9 | ≈61.2 | ≈56.8 | ≈3.0 | ≈7.5 |
| 10 | ≈61.0 | ≈56.8 | ≈3.2 | ≈7.5 |

**Key findings (from paper text)**:
- Performance shows "only minor variations across different Np" — low sensitivity
- Np=5 or Np=7 results in marginally better performance
- Default Np=3 used for all main experiments (not carefully tuned)
- All values are approximate (≈) — read from a line plot
