---
# Table 8: Computational Complexity Comparison
- **Source**: Table 8, Section 4.4
- **Caption**: "Comparisons w.r.t. computation complexity. FP/BP is short forward/backward propagation. #FP and #BP are numbers counted for processing a single sample. Accuracy (%) and ECE (%) are average results on ImageNet-C (level 5) with ViT-Base. The Wall-Clock Time (seconds) and Memory Usage (MB) are measured for processing 50,000 images of ImageNet-C on a single RTX 3090 GPU. K is the population size in CMA and it works well with all K ∈ [2, 28] and K ∈ N+, as shown in Figure 2(a)."
- **Conditions**: ViT-Base (full precision, 32-bit); 50,000 images of ImageNet-C, level 5; single RTX 3090 GPU

| Method | #FP | #BP | Avg Acc. (%) | Avg ECE (%) | Wall-Clock Time (s) | Memory (MB) |
|--------|-----|-----|-------------|------------|---------------------|-------------|
| NoAdapt | 1 | 0 | 55.5 | 10.5 | — | — |
| T3A | 1 | 0 | 56.9 | 26.8 | — | — |
| MEMO | 64 | 64 | 57.2 | 9.9 | 40,428 | 11,058 |
| TENT | 1 | 1 | 59.6 | 18.5 | — | 5,165 |
| SAR | [1,2] | [0,2] | 62.7 | 7.0 | — | 5,166 |
| CoTTA | 3 or 35 | ≥1 | 61.7 | 6.5 | — | 16,836 |
| Act. Shifting | 1 | 0 | 59.1 | 12.7 | — | — |
| FOA (K=2) | 2 | 0 | 59.6 | 9.7 | — | — |
| FOA (K=4) | 4 | 0 | 60.9 | 5.8 | — | — |
| FOA (K=6) | 6 | 0 | 62.7 | 4.6 | — | — |
| FOA (K=28) | 28 | 0 | 66.3 | 3.2 | — | 3,386 |

**Notes**:
- Wall-clock time and memory are measured on 50,000 ImageNet-C images on RTX 3090
- MEMO: 40,428 seconds for 50,000 images; 11,058 MB memory
- FOA (K=28): 3,386 MB memory (vs 16,836 MB for CoTTA — significantly lower)
- FOA (K=2) matches TENT accuracy (59.6%) with 0 backward passes and lower memory
- FOA (K=6) matches SAR accuracy (62.7%) with 0 backward passes
- Wall-clock time for TENT, SAR, CoTTA, NoAdapt, T3A not individually specified in paper
- Act. Shifting uses same FP count as NoAdapt but achieves 59.1% accuracy
