# Experiment Plans

## E01: Main comparison — LBCS vs. 7 baselines on F-MNIST, SVHN, CIFAR-10
- **Verifies**: C01, C02
- **Setup**:
  - Model (proxy/inner): LeNet for F-MNIST; CNN (inner-loop architecture, Table 5 left) for SVHN; CNN (inner-loop architecture, Table 5 right) for CIFAR-10
  - Model (post-selection evaluation): LeNet for F-MNIST; CNN (Table 5 center) for SVHN; ResNet-18 for CIFAR-10
  - Hardware: NVIDIA GTX3090 GPUs
  - Dataset: Fashion-MNIST, SVHN, CIFAR-10
  - System: Predefined coreset sizes k ∈ {1000, 2000, 3000, 4000}; ε=0.2; T=500
- **Procedure**:
  1. Load and preprocess the dataset (normalize, standard splits).
  2. For LBCS: initialize mask randomly with ‖m‖₀ = k.
  3. Run Algorithm 1 (LBCS): for each outer iteration t=1..T, (a) train inner loop to convergence using Adam (lr=0.001) on the coreset, (b) run LexiFlow mask update using lexicographic comparison of f1(m) and f2(m).
  4. Record the final mask's coreset size (f2) and train the evaluation network from scratch on the selected coreset.
  5. Evaluate the evaluation network on the test set; record mean±std over 10 repetitions.
  6. Repeat steps 2-5 for each baseline (Uniform, EL2N, GraNd, Influential, Moderate, CCS, Probabilistic) using their published implementations.
  7. For Table 3: apply the LBCS-determined coreset size as the fixed k for all baselines and re-run each baseline at that size.
- **Metrics**: Test accuracy (%), mean and standard deviation over 10 runs; final coreset size (mean ± std)
- **Expected outcome**:
  - LBCS achieves final coreset size strictly less than predefined k across all datasets and k values
  - LBCS test accuracy is at least as high as the best competing baseline on most dataset/k combinations
  - When evaluated at LBCS-determined coreset sizes (Table 3), LBCS consistently outperforms all baselines
- **Baselines**: Uniform sampling, EL2N (Paul et al. 2021), GraNd (Paul et al. 2021), Influential (Yang et al. 2023), Moderate (Xia et al. 2023), CCS (Zheng et al. 2023), Probabilistic (Zhou et al. 2022)
- **Dependencies**: none

## E02: Per-data-point accuracy analysis (Figure 3)
- **Verifies**: C01, C02
- **Setup**:
  - Same as E01 (F-MNIST, SVHN, CIFAR-10; k ∈ {1000, 2000, 3000, 4000})
  - Computed from E01 results
- **Procedure**:
  1. Use results from E01.
  2. For each method and each k configuration, compute average accuracy per data point = test_accuracy / final_coreset_size.
  3. Report as a bar chart / table.
- **Metrics**: Average test accuracy per coreset data point (test accuracy / coreset size)
- **Expected outcome**:
  - LBCS achieves the highest average accuracy per data point across all dataset and k configurations
- **Baselines**: Same as E01
- **Dependencies**: E01

## E03: Ablation on search time T (Table 7 in appendix)
- **Verifies**: C03
- **Setup**:
  - Model: LeNet as proxy and evaluation on F-MNIST
  - Hardware: NVIDIA GTX3090
  - Dataset: F-MNIST; k ∈ {1000, 2000}; ε=0.2
  - T ∈ {100, 200, 300, 500, 800, 1500, 2000}
- **Procedure**:
  1. Run LBCS with each T value for k=1000 and k=2000 on F-MNIST.
  2. After each run, record the final test accuracy and coreset size.
  3. Repeat and average results across repetitions.
- **Metrics**: Test accuracy (%), final coreset size; both as a function of T
- **Expected outcome**:
  - At low T, test accuracy increases and coreset size decreases as T increases
  - Beyond a certain T, test accuracy plateaus (empirical convergence)
  - Coreset size continues to decrease after accuracy plateaus, then also plateaus at larger T
- **Baselines**: none (ablation of LBCS)
- **Dependencies**: E01

## E04: Robustness under imperfect supervision (Figures 2a, 2b, Figure 4, Table 6 appendix)
- **Verifies**: C04
- **Setup**:
  - Model: LeNet proxy + LeNet evaluation on F-MNIST
  - Hardware: NVIDIA GTX3090
  - Dataset: F-MNIST with (a) 30% symmetric label noise, (b) 50% symmetric label noise, (c) exponential class imbalance (imbalance ratio 0.01)
  - k ∈ {1000, 2000, 3000, 4000}; ε=0.2; T=500
- **Procedure**:
  1. Construct the noisy/imbalanced F-MNIST training split: (a) randomly flip labels for 30% of training samples, (b) same at 50%, (c) apply exponential class imbalance with ratio 0.01 as in Xu et al. (2021).
  2. Run LBCS and all 7 baselines on each corrupted dataset at each k.
  3. Train evaluation LeNet on the selected coreset; evaluate on the clean vanilla F-MNIST test set.
  4. Record test accuracy and final coreset size.
- **Metrics**: Test accuracy (%) on clean test set; final coreset size
- **Expected outcome**:
  - LBCS achieves higher test accuracy than all baselines across all k and noise levels
  - LBCS coreset sizes are smaller than k (size reduction observed even under noise)
  - The advantage of LBCS over baselines grows with the severity of noise/imbalance
- **Baselines**: Same 7 baselines as E01
- **Dependencies**: none

## E05: ImageNet-1k evaluation (Table 4)
- **Verifies**: C05
- **Setup**:
  - Model: ResNet-50 for both proxy (inner loop) and post-selection training
  - Hardware: NVIDIA GTX3090 (or equivalent)
  - Dataset: ImageNet-1k; predefined selection ratios k/n ∈ {70%, 80%}
  - System: Groups of 100 examples share the same mask (acceleration trick); VISSL library; Adam inner loop; SGD post-selection (lr=0.01, batch=256, momentum=0.9, weight_decay=0.001, 100 epochs)
- **Procedure**:
  1. Partition ImageNet-1k training data into groups of 100 examples; each group shares one binary mask variable.
  2. Run LBCS at predefined ratio 70% and 80%; apply same grouping trick to Probabilistic baseline.
  3. Train ResNet-50 from scratch on the selected coreset using specified SGD settings.
  4. Evaluate Top-5 accuracy on ImageNet-1k validation set.
  5. Report the optimized selection ratio (final coreset size / n).
- **Metrics**: Top-5 test accuracy (%); optimized selection ratio (%)
- **Expected outcome**:
  - LBCS achieves the highest Top-5 accuracy at both predefined ratios
  - The optimized ratio is strictly less than the predefined ratio (size reduction demonstrated at scale)
- **Baselines**: Uniform, EL2N, GraNd, Moderate, CCS, Probabilistic (Influential not reported for ImageNet)
- **Dependencies**: none

## E06: Preliminary optimization demonstration on MNIST-S (Table 1, Section 5.1)
- **Verifies**: C01, C03
- **Setup**:
  - Model: CNN with two blocks (Conv→Dropout→MaxPool→ReLU), same as Zhou et al. (2022) baseline
  - Hardware: NVIDIA GTX3090
  - Dataset: MNIST-S = 1000 random samples from MNIST; k ∈ {200, 400}; ε ∈ {0.2, 0.3, 0.4}
  - Repetitions: 20
- **Procedure**:
  1. Construct MNIST-S by randomly sampling 1000 examples from the original MNIST dataset.
  2. Initialize mask randomly with ‖m‖₀ = k (k=200 or k=400).
  3. Record initial f1(m) (full-data loss) and f2(m) (coreset size = k) before optimization.
  4. Run LBCS for T iterations.
  5. Record final f1(m) and f2(m).
  6. Repeat 20 times; report mean ± std.
- **Metrics**: f1(m) (cross-entropy on full data, mean ± std), f2(m) (coreset size, mean ± std)
- **Expected outcome**:
  - After LBCS, both f1(m) and f2(m) are lower than their initial values
  - Larger ε leads to smaller f2(m) on average across runs
  - Larger ε leads to larger f1(m) on average (but not necessarily in individual runs, only in expectation)
- **Baselines**: none (demonstrates LBCS in isolation)
- **Dependencies**: none
