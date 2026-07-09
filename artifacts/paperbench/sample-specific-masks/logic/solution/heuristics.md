# Heuristics

## H01: Initialize δ (shared pattern) to zero matrix
- **Rationale**: Starting δ from zeros prevents the noise pattern from disrupting the pre-trained model's predictions at the beginning of training, allowing the label mapping (ILM) to first stabilize before noise is introduced. This avoids initialization bias that could destabilize early training.
- **Sensitivity**: high
- **Bounds**: δ must be initialized to exactly {0}^dP; non-zero initialization degrades early training stability
- **Code ref**: [src/execution/smm.py]
- **Source**: Section 3.4, Algorithm 1 line 3

## H02: Use patch size 8 (l=3 Max-Pool layers) as default
- **Rationale**: Empirical ablation over patch sizes {1, 2, 4, 8, 16} (i.e., l ∈ {0, 1, 2, 3, 4}) shows that accuracy increases from l=0 to l=3, then plateaus or decreases at l=4. Small patches (l=0,1) cause overfitting due to too much spatial freedom; large patches (l≥4) lose spatial detail. l=3 (patch=8) balances these effects.
- **Sensitivity**: medium
- **Bounds**: l ∈ {0, 1, 2, 3} for ResNet (5-layer CNN has at most 4 MaxPool layers, but l=4 is not recommended); l=3 is optimal across tested datasets
- **Code ref**: [src/execution/smm.py]
- **Source**: Section 5 "Impact of Patch Size", Figure 4

## H03: Use a unified learning rate schedule across all datasets for fair comparison
- **Rationale**: For ResNet models: initial LR=0.01, decay=0.1 at epochs 100 and 145, 200 total epochs. For ViT: LR=0.001, decay=1 (no decay). While dataset-specific tuning can improve individual results (e.g., ViT/UCF101 benefits from LR=0.01), unified parameters ensure fair comparison across methods and reflect practical deployment scenarios.
- **Sensitivity**: medium
- **Bounds**: ResNet: LR ∈ [0.001, 0.1]; ViT: LR ∈ [0.0001, 0.01] based on Table 7 search; milestones at epochs [100, 145] for ResNet
- **Code ref**: [src/configs/training.md]
- **Source**: Section 5, Appendix C, Tables 7-9

## H04: Use batch size 64 for small datasets (DTD, OxfordPets), 256 for others
- **Rationale**: DTD has only 2820 training samples and OxfordPets only 2944; using batch=256 would mean very few iterations per epoch and noisy gradient estimates. Batch=64 provides more stable gradients for these smaller datasets.
- **Sensitivity**: low
- **Bounds**: batch=64 for datasets with <5000 training samples; batch=256 for datasets with ≥5000 training samples
- **Code ref**: [src/configs/training.md]
- **Source**: Appendix C, Table 9

## H05: Apply patch-wise interpolation (not bilinear/bicubic) for mask upscaling
- **Rationale**: Patch-wise interpolation performs only copy operations with no floating-point arithmetic, requiring 0.151×10^6 pixel accesses vs 0.602×10^6 (bilinear) and 2.408×10^6 (bicubic) for ResNet-18/50. It also avoids gradient computation through the upsampling step, simplifying backpropagation. This is especially important since upsampling is applied at every forward pass for every training sample.
- **Sensitivity**: low
- **Bounds**: Acceptable whenever l > 0; provides ~4× speedup over bilinear and ~8× over bicubic per batch
- **Code ref**: [src/execution/smm.py]
- **Source**: Section 3.3, Appendix A.3, Table 5
