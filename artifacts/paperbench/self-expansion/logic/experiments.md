# Experiment Plans

## E01: Main CIL Comparison on CIFAR-100, ImageNet-R, ImageNet-A, VTAB
- **Verifies**: C01
- **Setup**:
  - Model: ViT-B/16 pre-trained on ImageNet-1K (frozen backbone)
  - Hardware: Single NVIDIA GeForce RTX 3090 GPU
  - Dataset: CIFAR-100 (100 classes, 10-class tasks); ImageNet-R (200 classes, 5/10/20-task splits); ImageNet-A (200 classes, 10-class tasks); VTAB (50 classes, 5 domains × 10 classes, domain order: resisc45 classes 10-19, dtd 20-29, pets 30-39, eurosat 40-49, flowers 50-59)
  - System: Class-incremental learning, no memory rehearsal
- **Procedure**:
  1. Load ViT-B/16-IN1K weights; freeze all ViT parameters.
  2. For each dataset, construct the class-incremental task sequence with 10 classes per task (for CIFAR-100, ImageNet-A, VTAB) or per the specified split for ImageNet-R.
  3. Use the same class order (data shuffling) as Zhou et al. [90] for all methods.
  4. Train SEMA: for each task, scan last 3 transformer layers (10, 11, 12) for expansion signals (z-score threshold=1.2 for ImageNet-A); if triggered, add and train adapter + RD + expanded router (5 epochs for adapters, 20 epochs for RDs); optimizer: SGD, adapter LR=0.005, RD LR=0.01, cosine annealing, batch size=32.
  5. Train all baselines (FT Adapter, L2P, DualPrompt, CODA-P, SimpleCIL, ADAM, InfLoRA) using their official/specified implementations with hyperparameters from original papers.
  6. After training on each task $t$, evaluate on test sets of all tasks seen so far; record $A_{i,N}$ for all $i \leq t$.
  7. Compute $A_N = \frac{1}{N}\sum_{i=1}^N A_{i,N}$ (average accuracy) and $\bar{A} = \frac{1}{N}\sum_{t=1}^N A_t$ (average incremental accuracy).
- **Metrics**: Average accuracy $A_N$ (%), average incremental accuracy $\bar{A}$ (%), both on test splits.
- **Expected outcome**:
  - SEMA should outperform or match all baselines on $A_N$ across most datasets and task splits.
  - SEMA should show greater improvement on challenging datasets (ImageNet-A) with more distribution shift compared to simpler benchmarks (CIFAR-100).
  - The incremental accuracy curve should show consistently superior performance of SEMA throughout training, not just at the end.
- **Baselines**: FT Adapter, L2P, DualPrompt, CODA-P, SimpleCIL, ADAM with Adapter, InfLoRA
- **Dependencies**: none

## E02: Sub-Linear Parameter Growth Analysis
- **Verifies**: C02
- **Setup**:
  - Model: ViT-B/16-IN1K (frozen backbone + SEMA adapters)
  - Hardware: Single NVIDIA GeForce RTX 3090 GPU
  - Dataset: ImageNet-A (20-task split, 10 classes per task)
  - System: Class-incremental, no rehearsal
- **Procedure**:
  1. Train SEMA, L2P, DualPrompt, CODA-P on ImageNet-A (20 tasks) using the same experimental setup as E01.
  2. Also train the "Expansion by Task" variant of SEMA, which adds one set of adapters at all eligible expansion layers for every new task (no z-score gating).
  3. After each task $t$, record the total number of added parameters (in millions) for each method.
  4. For SEMA, count only functional adapters (not RDs, which are training-time only).
  5. Plot/tabulate added parameters vs. number of tasks completed.
  6. Also compare SEMA vs "Expansion by Task" on accuracy and final parameter count across CIFAR-100, ImageNet-R, ImageNet-A, VTAB (Table 5).
- **Metrics**: Total added parameters (Millions) at each task step; final accuracy $A_N$.
- **Expected outcome**:
  - SEMA parameter count should follow a sub-linear curve (concave, growing slower as tasks increase).
  - DualPrompt and CODA-P should show linear parameter growth.
  - L2P should remain constant (fixed pool size).
  - "Expansion by Task" should outperform SEMA in parameter count but underperform in accuracy, showing SEMA's efficiency.
- **Baselines**: L2P, DualPrompt, CODA-P, Expansion-by-Task variant
- **Dependencies**: E01

## E03: Ablation on Expansion and Adapter Composing Strategies
- **Verifies**: C03
- **Setup**:
  - Model: ViT-B/16-IN1K (frozen) + SEMA
  - Hardware: Single NVIDIA GeForce RTX 3090 GPU
  - Dataset: ImageNet-A (10-class tasks) and VTAB (5 tasks, 10 classes each)
  - System: Class-incremental, no rehearsal
- **Procedure**:
  1. Train SEMA (full method) on ImageNet-A and VTAB.
  2. Train the following ablation variants with same hyperparameters:
     - **No Exp.**: Remove self-expansion entirely; use one adapter per layer from Task 1 only (frozen after Task 1, reused for all subsequent tasks). Router trained only on Task 1.
     - **Avg. W.**: Self-expansion enabled but router replaced with uniform averaging (equal weights for all adapters).
     - **Rand. W.**: Self-expansion enabled but router replaced with random weights resampled per batch.
     - **Top-1 Sel.**: Self-expansion enabled; during both training and inference, only the adapter with the highest router weight is used (hard selection).
     - **Rand. Sel.**: Self-expansion enabled; during both training and inference, one adapter is selected uniformly at random per sample.
     - **Top-1 Sel. Inf.**: Standard SEMA training with learned soft router; during inference only, select the top-1 adapter by router weight.
  3. Evaluate each variant with $A_N$ and $\bar{A}$ on both datasets.
- **Metrics**: Average accuracy $A_N$ (%), average incremental accuracy $\bar{A}$ (%) on ImageNet-A and VTAB test splits.
- **Expected outcome**:
  - Full SEMA (soft learned router + expansion) should achieve highest $A_N$ on both datasets.
  - No Exp. should degrade significantly relative to SEMA, demonstrating value of expansion.
  - Avg. W. and Rand. W. should underperform SEMA's learned router.
  - Hard selection variants (Top-1 Sel., Rand. Sel.) should underperform soft mixture.
  - Top-1 Sel. Inf. (trained with soft mixture, hard inference) should be between full SEMA and Top-1 Sel.
- **Baselines**: No Exp., Avg. W., Rand. W., Top-1 Sel., Rand. Sel., Top-1 Sel. Inf.
- **Dependencies**: none

## E04: Ablation on Functional Adapter Type Variants
- **Verifies**: C04
- **Setup**:
  - Model: ViT-B/16-IN1K (frozen) + SEMA framework
  - Hardware: Single NVIDIA GeForce RTX 3090 GPU
  - Dataset: ImageNet-A and VTAB
  - System: Class-incremental, no rehearsal
- **Procedure**:
  1. Train three SEMA variants on ImageNet-A and VTAB, each using a different functional adapter type:
     - **Adapter** [9]: default (down-projection + ReLU + up-projection), side branch of MLP
     - **LoRA** [30]: low-rank matrix injection (same SEMA expansion and routing framework)
     - **Convpass** [34]: convolutional bypass adapter
  2. All other hyperparameters and SEMA components (RD, router, expansion strategy) remain identical.
  3. Evaluate $A_N$ and $\bar{A}$ on both datasets for each variant.
- **Metrics**: Average accuracy $A_N$ (%), average incremental accuracy $\bar{A}$ (%).
- **Expected outcome**:
  - All three adapter variants should achieve comparable performance (within ~2% $A_N$) on both datasets.
  - The default Adapter should perform best or be competitive on both datasets.
  - Results should confirm that SEMA's expansion and routing framework provides benefit regardless of the underlying adapter type.
- **Baselines**: none (all SEMA variants)
- **Dependencies**: E01

## E05: Analysis of Expansion Threshold Sensitivity
- **Verifies**: C03
- **Setup**:
  - Model: ViT-B/16-IN1K (frozen) + SEMA
  - Hardware: Single NVIDIA GeForce RTX 3090 GPU
  - Dataset: ImageNet-A (thresholds 1.0–2.0 in steps of 0.1) and VTAB (thresholds 1.0–8.0 in steps of 1.0)
  - System: Class-incremental, no rehearsal
- **Procedure**:
  1. For ImageNet-A: train 11 SEMA models with thresholds τ ∈ {1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0}.
  2. For VTAB: train 8 SEMA models with thresholds τ ∈ {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0}.
  3. For each model: record final $A_N$ and number of adapters added at each of the last 3 transformer layers (layers 10, 11, 12).
  4. Also analyse the dynamic expansion process on VTAB (first 5 tasks), restricting expansion to the last layer only: visualise RD reconstruction errors during training and detection phases.
- **Metrics**: $A_N$ (%), adapter count per layer (integer) for each threshold value.
- **Expected outcome**:
  - On ImageNet-A: accuracy should remain roughly stable across thresholds 1.0–2.0 (low sensitivity to τ).
  - On VTAB: accuracy should be higher at lower thresholds (more expansion) and degrade at very high thresholds (insufficient adaptation).
  - Number of adapters should monotonically decrease as threshold increases.
  - The expansion process analysis should show RDs triggering expansion for Tasks 1–3 on VTAB and reusing adapters for Tasks 4–5.
- **Baselines**: none
- **Dependencies**: E01

## E06: Multi-Layer Expansion Range Analysis
- **Verifies**: C03
- **Setup**:
  - Model: ViT-B/16-IN1K (frozen) + SEMA
  - Hardware: Single NVIDIA GeForce RTX 3090 GPU
  - Dataset: ImageNet-A and VTAB
  - System: Class-incremental, no rehearsal
- **Procedure**:
  1. Train three SEMA variants on each dataset with different layer ranges eligible for expansion:
     - **Layers 11-12**: last 2 transformer layers only
     - **Layers 10-12**: last 3 layers (default)
     - **Layers 9-12**: last 4 layers
  2. Record $A_N$, $\bar{A}$, total adapters added, and adapters in the last layer specifically.
- **Metrics**: $A_N$ (%), $\bar{A}$ (%), total adapter count (integer), last-layer adapter count (integer).
- **Expected outcome**:
  - More expansion layers should yield higher accuracy on both datasets (at least for layers 9-12 vs. 11-12).
  - Expanding into earlier layers (9) should add more total adapters without proportional accuracy improvement.
  - The last layer should receive the most adapters across all configurations.
- **Baselines**: none
- **Dependencies**: E01
