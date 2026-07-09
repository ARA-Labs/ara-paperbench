# Experiments

## E01: Demonstration of Shared Mask Failure on Individual Samples
- **Verifies**: C01
- **Setup**:
  - Model: ResNet (ImageNet-1K pre-trained), fixed
  - Hardware: Single A100 GPU
  - Dataset: OxfordPets (training and test sets)
  - System: Watermarking VR with three mask configurations (Full, Medium, Narrow)
- **Procedure**:
  1. Train watermarking VR with three separate shared mask configurations: Full (all-ones 224×224), Medium (width=56 border mask), Narrow (width=28 border mask)
  2. For each trained model, record classification confidence scores for a diverse set of test images
  3. Identify the mask configuration that maximizes classification confidence for each individual image
  4. Record the distribution of [final loss – initial loss] per training sample for the Full watermarking configuration
  5. Compare this distribution against finetuning-all-parameters (which should show only negative values)
- **Metrics**: Per-sample classification confidence (%), distribution of [final loss – initial loss] per sample, fraction of samples with positive loss change
- **Expected outcome**:
  - Different images should prefer different mask configurations (the optimal mask varies across individual images)
  - The distribution of [final loss – initial loss] under shared-mask VR should contain a substantial positive tail (some samples' loss increases)
  - Finetuning should show no positive loss changes
- **Baselines**: Standard finetuning of all model parameters (no shared-mask constraint)
- **Dependencies**: none

## E02: Theoretical Verification of Approximation Error Ordering
- **Verifies**: C02
- **Setup**:
  - Model: Fixed f'P = fout ∘ fP for any architecture
  - Hardware: N/A (theoretical/analytical)
  - Dataset: Any target domain distribution DT
  - System: PAC learning framework
- **Procedure**:
  1. Define Fshr(f'P) = {f | f(x) = f'P(r(x) + M ⊙ δ)} with constant M ∈ {0,1}^dP
  2. Define Fsmm(f'P) = {f | f(x) = f'P(r(x) + fmask(r(x)) ⊙ δ)} with CNN fmask
  3. Verify Fshr ⊆ Fsmm: show any constant mask M can be recovered by a CNN with zero last-layer weights (output = bias which spans R^dP, and {0,1}^dP ⊆ R^dP)
  4. Apply Theorem 4.2 (if F1 ⊆ F2 then Errapx(F1) ≥ Errapx(F2))
  5. Also verify Fsp ⊆ Fsmm (sample-specific without δ is also a subset, via J_dP ∈ Δ argument)
  6. Measure empirical estimation error by comparing train-test accuracy gaps for SMM vs shared-mask VR across datasets
- **Metrics**: Logical inclusion proof (Fshr ⊆ Fsmm), training accuracy vs test accuracy gap per method
- **Expected outcome**:
  - Logical proof should hold: Fshr strictly contained in Fsmm
  - SMM's train-test accuracy gap should not be larger than shared-mask methods (negligible estimation error increase)
  - Enlarging fmask beyond the default size should show diminishing returns and eventual overfitting (Table 11)
- **Baselines**: Shared-mask VR (Full watermarking as representative Fshr)
- **Dependencies**: none

## E03: SMM vs Baselines on ResNet-18 and ResNet-50 (Main Results)
- **Verifies**: C01, C03
- **Setup**:
  - Model: ResNet-18 (ImageNet-1K), ResNet-50 (ImageNet-1K) — both fixed
  - Hardware: Single A100 GPU
  - Dataset: 11 datasets — CIFAR10, CIFAR100, SVHN, GTSRB, Flowers102, DTD, UCF101, Food101, SUN397, EuroSAT, OxfordPets
  - System: ILM output mapping; batch=256 for most datasets, batch=64 for DTD/OxfordPets; 200 epochs; initial LR=0.01; decay=0.1 at epochs 100 and 145; 3 random seeds each
- **Procedure**:
  1. For each dataset, resize images to 224×224 using bilinear interpolation
  2. Initialize δ = zeros, ϕ randomly
  3. Train Pad, Narrow, Medium, Full, and SMM (Ours) methods under identical hyperparameters
  4. For SMM: generate per-sample masks via 5-layer CNN fmask, apply patch-wise interpolation (l=3, patch size=8), compute fin(xi) = r(xi) + δ ⊙ fmask(r(xi)|ϕ)
  5. Update δ and ϕ via SGD with the ILM-mapped cross-entropy loss
  6. Record test accuracy at end of 200 epochs for 3 seeds; report mean ± std
- **Metrics**: Classification accuracy (%) on test set, mean ± standard deviation across 3 seeds, average across 11 datasets
- **Expected outcome**:
  - SMM should outperform all baselines on the majority of datasets for both ResNet-18 and ResNet-50
  - Improvement should be most pronounced on datasets with domain gap (SVHN, Flowers102, EuroSAT)
  - DTD may be an exception for ResNet-18 due to texture interference from watermark noise
  - SMM average accuracy should be highest among all methods for both models
- **Baselines**: Pad (Chen et al. 2023), Narrow/Medium/Full watermarking (Bahng et al. 2022)
- **Dependencies**: none

## E04: SMM vs Baselines on ViT-B32 (Main Results)
- **Verifies**: C01, C04
- **Setup**:
  - Model: ViT-B32 (ImageNet-1K) — fixed
  - Hardware: Single A100 GPU
  - Dataset: Same 11 datasets; images resized to 384×384
  - System: ILM output mapping; batch=256 for most datasets, batch=64 for DTD/OxfordPets; 200 epochs; initial LR=0.001; decay=1 (no decay); 3 random seeds; SMM uses 6-layer CNN mask generator with patch size=8
- **Procedure**:
  1. Resize images to 384×384 using bilinear interpolation
  2. Apply same training procedure as E03 but with ViT-specific hyperparameters
  3. For UCF101, additionally test with LR=0.01 and decay=0.1 (reported separately)
  4. Report mean test accuracy at end of training
- **Metrics**: Classification accuracy (%) on test set, mean across 3 seeds, average across 11 datasets
- **Expected outcome**:
  - SMM should achieve the highest average accuracy across all methods
  - Large improvements expected on Flowers102, Food101, and SUN397 compared to best baseline
  - EuroSAT exception: padding-based method may perform better due to simple dataset + ViT overfitting
  - UCF101: with default parameters SMM may lag, but with tuned LR=0.01 it achieves leading accuracy
- **Baselines**: Same as E03
- **Dependencies**: none

## E05: Ablation Study — Impact of Masking Components
- **Verifies**: C05
- **Setup**:
  - Model: ResNet-18 (ImageNet-1K) — fixed
  - Hardware: Single A100 GPU
  - Dataset: Same 11 datasets
  - System: ILM output mapping; same hyperparameters as E03; 3 random seeds
- **Procedure**:
  1. Train 4 variants: (i) Only δ: fin(xi) = r(xi) + δ (Full watermark = all-one M, no fmask), (ii) Only fmask: fin(xi) = r(xi) + fmask(r(xi)) (no shared δ), (iii) Single-channel SMM: fin(xi) = r(xi) + δ ⊙ f^s_mask(r(xi)) (average penultimate-layer output), (iv) Full SMM (Ours): fin(xi) = r(xi) + δ ⊙ fmask(r(xi)|ϕ) (3-channel)
  2. Record test accuracy for all 11 datasets under each variant
  3. Compare average performance across all datasets
- **Metrics**: Classification accuracy (%) per dataset, mean ± std across 3 seeds, average across 11 datasets
- **Expected outcome**:
  - Full SMM should achieve highest average accuracy
  - Only δ (no fmask) should degrade performance on feature-rich datasets (CIFAR10, Flowers102, UCF101)
  - Only fmask (no δ) should degrade on large-data datasets (CIFAR10, SVHN, GTSRB, SUN397)
  - Single-channel should underperform three-channel, especially on GTSRB and Flowers102
  - Ablating any component degrades average performance
- **Baselines**: The three ablated variants (Only δ, Only fmask, Single-channel)
- **Dependencies**: E03

## E06: Efficiency Comparison — Patch-wise vs Bilinear vs Bicubic Interpolation
- **Verifies**: C06
- **Setup**:
  - Model: ResNet-18/50 and ViT-B32
  - Hardware: Single A100 GPU
  - Dataset: Batch of 256 images
  - System: Three upsampling methods applied to CNN mask outputs
- **Procedure**:
  1. For a batch of 256 images, apply each interpolation method to upsample CNN-generated masks from H/2^l × W/2^l to H × W
  2. Measure number of pixel accesses per image during interpolation
  3. Measure wall-clock time per batch (mean ± std) for bilinear, bicubic, and patch-wise methods
  4. Verify that patch-wise interpolation does not require backpropagation gradients through the upsampling step
- **Metrics**: Number of pixel accesses (×10^6), time per batch (seconds ± std), backpropagation requirement (yes/no)
- **Expected outcome**:
  - Patch-wise interpolation should require substantially fewer pixel accesses than bilinear (which requires 4 neighbors per pixel) and bicubic (which requires 16 neighbors)
  - Patch-wise interpolation should be fastest in wall-clock time
  - Patch-wise interpolation should not require backpropagation through the upsampling step (simplifying gradient computation)
- **Baselines**: Bilinear interpolation (standard), bicubic interpolation (standard)
- **Dependencies**: none
