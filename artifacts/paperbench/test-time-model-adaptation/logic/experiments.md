---
# Experiments

## E01: Main comparison — full-precision ViT-Base on ImageNet-C
- **Verifies**: C01, C05
- **Setup**:
  - Model: ViT-Base (32-bit full precision), pretrained on ImageNet-1K via timm repository
  - Hardware: GPU (RTX 3090 or equivalent)
  - Dataset: ImageNet-C, severity level 5, all 15 corruption types (50,000 images per corruption type)
  - System: Batch size 64; source ID statistics from ImageNet-1K validation set (Q=full validation set); Np=3 prompts; K=28; λ=0.4×BS/64; γ=1.0; α=0.1
- **Procedure**:
  1. Load pretrained ViT-Base weights from timm
  2. Pre-compute source statistics {μ^S_i, σ^S_i}_{i=0}^N over ImageNet-1K validation set without prompts
  3. For each of the 15 corruption types, run online TTA over the 50,000 test images in mini-batches of 64
  4. For each batch: sample K=28 prompt candidates via CMA-ES; compute fitness (Eq. 5) for each; update CMA distribution; apply activation shifting (Eq. 7); predict with best-fitness prompt
  5. Compare against NoAdapt, LAME, T3A (gradient-free), TENT, CoTTA, SAR (gradient-based)
  6. Report per-corruption accuracy and average accuracy + average ECE across all 15 corruptions
- **Metrics**: Classification accuracy (%, ↑) and ECE (%, ↓) per corruption type and average
- **Expected outcome**:
  - FOA achieves higher average accuracy than all baselines including gradient-based TENT and SAR
  - FOA achieves lower average ECE than all baselines
  - Gradient-based methods (TENT, CoTTA, SAR) outperform gradient-free baselines (LAME, T3A) in accuracy
  - LAME performs worse than or similar to NoAdapt
- **Baselines**: NoAdapt (no adaptation), LAME, T3A (gradient-free), TENT, CoTTA, SAR (gradient-based)
- **Dependencies**: none

## E02: Extended benchmarks — ImageNet-R, ImageNet-V2, ImageNet-Sketch
- **Verifies**: C01
- **Setup**:
  - Model: ViT-Base (32-bit full precision), same pretrained weights as E01
  - Hardware: GPU
  - Dataset: ImageNet-R (30,000 images, 200 classes), ImageNet-V2 Matched Frequency (10,000 images, 1000 classes), ImageNet-Sketch (50,899 images, 1000 classes)
  - System: Same hyperparameters as E01; λ=0.2×BS/64 for ImageNet-R; λ=0.4×BS/64 for ImageNet-V2/Sketch
- **Procedure**:
  1. Use same pretrained model and source statistics as E01
  2. Run FOA and all baselines on each benchmark independently
  3. Report accuracy and ECE per benchmark
- **Metrics**: Classification accuracy (%, ↑) and ECE (%, ↓) per benchmark
- **Expected outcome**:
  - FOA achieves best or comparable accuracy and ECE across all three benchmarks
  - FOA shows lower ECE than gradient-based methods due to activation discrepancy regularization
- **Baselines**: NoAdapt, LAME, T3A, TENT, CoTTA, SAR
- **Dependencies**: E01

## E03: Quantized model evaluation on ImageNet-C
- **Verifies**: C02
- **Setup**:
  - Model: ViT-Base quantized to 8-bit and 6-bit using PTQ4ViT with 32 randomly selected ImageNet-1K training samples
  - Hardware: GPU
  - Dataset: ImageNet-C, severity level 5, all 15 corruption types
  - System: Same FOA hyperparameters as E01; T3A as the only applicable gradient-free baseline
- **Procedure**:
  1. Quantize ViT-Base to 8-bit and 6-bit using PTQ4ViT
  2. Pre-compute source statistics on quantized model using ImageNet-1K validation set
  3. Run FOA on each quantized model across all 15 ImageNet-C corruption types
  4. Run T3A and NoAdapt as baselines
  5. Compare FOA (8-bit) accuracy to TENT (32-bit) accuracy from E01
  6. Report per-corruption accuracy and average accuracy + ECE
- **Metrics**: Classification accuracy (%, ↑) and ECE (%, ↓) per corruption type and average
- **Expected outcome**:
  - FOA with 8-bit quantized ViT surpasses TENT with full-precision 32-bit ViT in average accuracy
  - FOA significantly outperforms T3A in both accuracy and ECE on both 8-bit and 6-bit models
  - 6-bit model shows lower baseline accuracy but FOA still substantially improves over NoAdapt and T3A
- **Baselines**: NoAdapt (quantized), T3A (quantized); TENT (32-bit, from E01 for cross-precision comparison)
- **Dependencies**: E01

## E04: Run-time memory usage analysis
- **Verifies**: C03
- **Setup**:
  - Model: ViT-Base (32-bit and 8-bit)
  - Hardware: Single RTX 3090 GPU
  - Dataset: ImageNet-C Gaussian noise, severity level 5 (50,000 images)
  - System: Various batch sizes (BS=1, 4, 8, 16, 32, 64)
- **Procedure**:
  1. Measure peak GPU memory usage for each method at each batch size
  2. For 8-bit models, estimate memory as 0.25× of 32-bit model measurements (per Liu et al., 2021b)
  3. Measure FOA-I V1 (stores CLS features) and FOA-I V2 (stores images) at BS=1 with intervals I={1,4,8,16,32,64}
  4. Compare FOA against NoAdapt, TENT, CoTTA
- **Metrics**: Run-time memory usage in MB
- **Expected outcome**:
  - FOA memory is marginally higher than NoAdapt (by a few MB for feature statistics storage)
  - FOA uses significantly less memory than TENT and CoTTA at all batch sizes
  - FOA (8-bit) achieves substantial additional memory savings over FOA (32-bit)
  - FOA-I V1/V2 reduce memory further vs. standard FOA
- **Baselines**: NoAdapt, TENT, CoTTA
- **Dependencies**: none

## E05: Ablation of FOA components (entropy, activation discrepancy, activation shifting)
- **Verifies**: C04, C05
- **Setup**:
  - Model: ViT-Base (32-bit full precision)
  - Hardware: GPU
  - Dataset: ImageNet-C, severity level 5, all 15 corruption types
  - System: Default FOA hyperparameters; ablate three components independently and in combination
- **Procedure**:
  1. Run NoAdapt (baseline)
  2. Run CMA + entropy fitness only (no activation discrepancy, no activation shifting)
  3. Run CMA + activation discrepancy fitness only (no entropy term, no activation shifting)
  4. Run activation shifting only (no CMA prompt adaptation)
  5. Run CMA + entropy + activation discrepancy fitness (no activation shifting)
  6. Run activation shifting + CMA + activation discrepancy fitness
  7. Run full FOA (entropy + activation discrepancy + activation shifting)
  8. Report average accuracy and ECE over all 15 corruptions for each configuration
- **Metrics**: Average classification accuracy (%, ↑) and average ECE (%, ↓) over 15 corruption types
- **Expected outcome**:
  - CMA with entropy-only fitness performs worse than NoAdapt
  - Activation discrepancy fitness alone substantially improves accuracy over NoAdapt (>5% gain)
  - Activation shifting alone improves accuracy over NoAdapt (>2% gain)
  - Full FOA combination achieves highest accuracy and lowest ECE among all variants
- **Baselines**: NoAdapt
- **Dependencies**: none

## E06: Design choice ablation — learnable params × optimizer × loss function
- **Verifies**: C04, C05
- **Setup**:
  - Model: ViT-Base (32-bit full precision)
  - Hardware: GPU
  - Dataset: ImageNet-C, severity level 5, all 15 corruption types
  - System: All combinations of {norm layers, prompts} × {SGD, CMA} × {entropy, Eq. 5 fitness}
- **Procedure**:
  1. Run TENT (norm layers + SGD + entropy) as reference
  2. exp1: prompts + SGD + entropy
  3. exp2: norm layers + SGD + Eq. 5 fitness
  4. exp3: prompts + SGD + Eq. 5 fitness
  5. exp4: norm layers + CMA + Eq. 5 fitness
  6. exp5: norm layers + CMA + entropy
  7. exp6: prompts + CMA + entropy
  8. FOA (ours): prompts + CMA + Eq. 5 fitness
  9. Report average accuracy and ECE for each
- **Metrics**: Average classification accuracy (%, ↑) and average ECE (%, ↓) over 15 corruption types
- **Expected outcome**:
  - CMA with norm layers (exp4, exp5) collapses to near-zero accuracy (~0.1%)
  - CMA with prompts + entropy (exp6) underperforms NoAdapt
  - Eq. 5 fitness with SGD on norm layers (exp2) substantially outperforms TENT
  - FOA (prompts + CMA + Eq. 5) achieves good performance, validating all three design choices
- **Baselines**: NoAdapt, TENT
- **Dependencies**: E05

## E07: In-distribution performance on clean ImageNet validation set
- **Verifies**: C06
- **Setup**:
  - Model: ViT-Base (32-bit full precision)
  - Hardware: GPU
  - Dataset: ImageNet-1K validation set (clean, no corruption)
  - System: Batch size 64; all methods use same hyperparameters as in main experiments
- **Procedure**:
  1. Run each method (NoAdapt, TENT, CoTTA, SAR, FOA) on the clean ImageNet validation set
  2. Report accuracy and ECE
  3. Compute relative accuracy decline from NoAdapt baseline
- **Metrics**: Classification accuracy (%, ↑) and ECE (%, ↓)
- **Expected outcome**:
  - FOA maintains accuracy within ~0.1% of NoAdapt (minimal catastrophic forgetting)
  - FOA's accuracy drop is substantially smaller than TENT, CoTTA, and SAR
  - FOA achieves lower ECE than NoAdapt due to activation discrepancy regularization
- **Baselines**: NoAdapt, TENT, CoTTA, SAR
- **Dependencies**: E01

## E08: Non-i.i.d. scenarios (online label shift and mixed domain shift)
- **Verifies**: C07
- **Setup**:
  - Model: ViT-Base (32-bit full precision)
  - Hardware: GPU
  - Dataset: ImageNet-C, severity level 5
  - System: Two non-i.i.d. scenarios — (1) online imbalanced label distribution shift: test data in class order; (2) mixed domain shift: single stream of 15 mixed corruptions randomly interleaved
- **Procedure**:
  1. Scenario 1 (online label shift): Arrange ImageNet-C test samples by class order; run TENT, SAR, FOA; report average accuracy and ECE over 15 corruptions
  2. Scenario 2 (mixed domain shift): Randomly interleave samples from all 15 corruption types into one stream; run TENT, SAR, FOA; report accuracy and ECE on the mixed stream
  3. Compare performance to i.i.d. baseline from E01
- **Metrics**: Classification accuracy (%, ↑) and ECE (%, ↓) per scenario
- **Expected outcome**:
  - All methods show some degradation under non-i.i.d. vs. i.i.d. conditions
  - FOA maintains best accuracy and lowest ECE among TENT, SAR, FOA in both non-i.i.d. settings
  - FOA's ECE remains substantially lower than TENT in non-i.i.d. settings
- **Baselines**: TENT, SAR
- **Dependencies**: E01
