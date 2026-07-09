# Experiments

## E01: LCA-on-the-Line Correlation Study
- **Verifies**: C01
- **Setup**:
  - Model: 75 pretrained models (36 VMs: AlexNet, ConvNeXt, DenseNet variants, EfficientNet, GoogLeNet, InceptionV3, MnasNet variants, MobileNetV3, RegNet, WideResNet, ResNet variants, ShuffleNet, SqueezeNet, Swin-B, VGG variants, ViT-B/L; 39 VLMs: ALBEF, BLIP, CLIP variants (RN50/101/50x4/ViT-B-32/B-16/L-14/L-14-336px), OpenCLIP variants (31 models))
  - Hardware: Standard GPU inference (no specific hardware requirement for evaluation)
  - Dataset: ImageNet (ID), ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, ObjectNet (OOD)
  - System: WordNet hierarchy for LCA computation; information content scoring
- **Procedure**:
  1. Load all 75 pretrained models (VMs from torchvision, VLMs from CLIP/OpenCLIP repositories)
  2. For each model, run inference on ImageNet test set; collect per-sample (prediction, ground truth) pairs
  3. Compute ID Top-1 accuracy for each model
  4. Compute ID average LCA distance (information content) for each model using WordNet hierarchy, averaging only over misclassified samples
  5. For each of the 5 OOD datasets, run inference on each model; compute OOD Top-1 and Top-5 accuracy
  6. Compute R² and PEA between: (a) ID Top-1 vs OOD Top-1/Top-5, and (b) ID LCA vs OOD Top-1/Top-5, for each OOD dataset
  7. Apply min-max scaling to LCA values before fitting linear regressions (LCA not in [0,1])
  8. Report absolute values of correlations
- **Metrics**: R² (coefficient of determination), PEA (Pearson correlation coefficient), across all 75 models combined, VMs only, and VLMs only
- **Expected outcome**:
  - ID LCA distance should show substantially higher R² and PEA than ID Top-1 accuracy for severely shifted OOD datasets (ImageNet-S/R/A/ObjectNet) when considering all 75 models together
  - ID Top-1 should remain superior predictor for ImageNet-v2 (mild shift)
  - For VMs-only or VLMs-only subsets, both LCA and Top-1 should show high correlation
  - The combined-modality analysis should show two divergent linear trends for Top-1 but one unified trend for LCA
- **Baselines**: ID Top-1 accuracy (Miller et al., 2021 Accuracy-on-the-Line)
- **Dependencies**: none

## E02: OOD Error Prediction via ID LCA (MAE Comparison)
- **Verifies**: C01
- **Setup**:
  - Model: Same 75 models as E01
  - Hardware: Standard GPU
  - Dataset: Same as E01
  - System: Linear regression fitted to ID metric → OOD Top-1; min-max scaling for LCA
- **Procedure**:
  1. Compute ID metrics for all 75 models: Top-1, Average Confidence (AC), Aline-D, Aline-S, ID LCA distance
  2. For Average Confidence: AC = (1/N) * sum(max_j P(y_j|x_i)) with temperature scaling
  3. For each of 5 OOD datasets, fit a linear regression from each ID metric to OOD Top-1 accuracy
  4. Use leave-one-out or held-out validation to compute MAE (Mean Absolute Error) between predicted and actual OOD Top-1 accuracy for each model
  5. Report MAE for each method × OOD dataset combination
- **Metrics**: MAE (Mean Absolute Error) between predicted OOD Top-1 and actual OOD Top-1, lower is better
- **Expected outcome**:
  - ID LCA should achieve lower MAE than all baselines on the majority of OOD datasets (especially ImageNet-S/A/ObjectNet)
  - ID Top-1 (Miller et al.) should maintain lowest MAE on ImageNet-v2
  - ID LCA should be especially superior on ImageNet-A (adversarial) where Top-1-based methods degrade severely
- **Baselines**: ID Top-1 (Miller et al., 2021), Average Confidence (AC, Hendrycks & Gimpel, 2017), Aline-D (Baek et al., 2022), Aline-S (Baek et al., 2022)
- **Dependencies**: E01

## E03: K-means Latent Hierarchy Robustness
- **Verifies**: C02
- **Setup**:
  - Model: All 75 pretrained models as source models for hierarchy construction; all 75 as evaluation models
  - Hardware: Standard GPU for feature extraction
  - Dataset: ImageNet test set for feature extraction; all 5 OOD datasets for evaluation
  - System: 9-layer K-means hierarchical clustering on per-class average features
- **Procedure**:
  1. For each of 75 source models: extract per-sample features, group by class label, compute per-class average features (1000 feature vectors for ImageNet)
  2. Apply K-means clustering hierarchically: for i=1,2,...,9, cluster into 2^i centers, resulting in 9 cluster assignments per class
  3. For each class pair, find the lowest level at which they share a cluster (this is their LCA height). All pairs share level 10 by default.
  4. This yields 75 latent hierarchy distance matrices (n×n for n=1000 classes)
  5. For each of 75 evaluation models and each of 75 source hierarchies, compute LCA distance using depth-based scoring
  6. Compute PEA between (LCA distance under each source hierarchy) and (OOD Top-1) across 75 evaluation models
  7. Aggregate PEA statistics (mean, min, max, std) across 75 source hierarchies for each OOD dataset
  8. Compare to WordNet-based PEA and Top-1-based PEA baselines
- **Metrics**: PEA statistics (mean, min, max, std) over 75 source hierarchies; comparison to WordNet PEA
- **Expected outcome**:
  - Mean PEA across 75 latent hierarchies should exceed that of Top-1 accuracy baseline on all severely shifted OOD datasets
  - PEA values should be somewhat lower than WordNet-based LCA but still substantially positive (>0.5)
  - Low standard deviation across 75 hierarchies demonstrates robustness to source model choice
  - VLM-sourced hierarchies should produce higher-quality (higher PEA) soft labels than VM-sourced hierarchies
- **Baselines**: WordNet-based LCA (upper bound), Top-1 accuracy (lower bound baseline)
- **Dependencies**: E01

## E04: LCA Soft Labels for Linear Probing
- **Verifies**: C03
- **Setup**:
  - Model: 6 backbone models (ResNet-18, ResNet-50, ViT-B, ViT-L, ConvNext-Tiny, Swin-B)
  - Hardware: Single NVIDIA GeForce GTX 1080 Ti GPU
  - Dataset: ImageNet (train/val/test), ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, ObjectNet
  - System: Linear probe on frozen backbone features; WordNet LCA soft labels or K-means latent hierarchy soft labels
- **Procedure**:
  1. Extract features from frozen backbone models for all ImageNet train/val/test samples
  2. Compute n×n LCA distance matrix using tree depth (DP_LCA) and WordNet hierarchy
  3. Apply temperature scaling (T=25) and min-max normalization: M_LCA = MinMax(M^T)
  4. Train linear probe (CE-only baseline) using standard cross-entropy loss
  5. Train linear probe with LCA alignment loss (Algorithm 1): lambda=0.03, temperature=25, CE mode
  6. Find optimal interpolation weight alpha ∈ {0.0, 0.1, ..., 1.0} that maximizes ID val Top-1: W_interp = alpha*W_CE + (1-alpha)*W_{CE+soft}
  7. Evaluate all probes (CE-only, CE+soft, interpolated) on all 6 datasets
  8. Repeat using K-means latent hierarchies (Table 6 extension)
  - Optimizer: AdamW, lr=0.001, batch_size=1024, weight decay enabled, cosine LR scheduler, linear warm-up (1e-5), 50 epochs
- **Metrics**: Top-1 accuracy on all 6 datasets (ImageNet, ImageNet-v2, ImageNet-S/R/A, ObjectNet)
- **Expected outcome**:
  - Interpolated probe (CE + LCA soft loss) should outperform CE-only baseline on OOD datasets without significantly reducing ID accuracy
  - VLM-sourced latent hierarchies should produce better soft labels than VM-sourced ones
  - WordNet soft labels should produce larger OOD improvements than latent hierarchy soft labels
  - OOD improvements should be visible across all backbone architectures
- **Baselines**: CE-only linear probe, CE + interpolation (weight interpolation without soft labels)
- **Dependencies**: E01, E03

## E05: Taxonomy-Aligned Prompt Engineering for VLMs
- **Verifies**: C05
- **Setup**:
  - Model: CLIP-ViT32 (Radford et al., 2021)
  - Hardware: Standard GPU
  - Dataset: ImageNet, ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, ObjectNet
  - System: Zero-shot evaluation with 4 prompt variants
- **Procedure**:
  1. Implement 4 prompt templates:
     - Baseline: "<class_name>"
     - Stack Parent: "<class_name>, <parent>, <grandparent>" (correct hierarchy but no relational info)
     - Taxonomy Parent: "<class_name>, which is a type of <parent>, which is a type of <grandparent>"
     - Shuffle Parent: "<class_name>, which is a type of <random_node1>, which is a type of <random_node2>"
  2. For each prompt template, run zero-shot inference on all 6 datasets
  3. Report Top-1 accuracy and test-time cross-entropy for each prompt × dataset combination
- **Metrics**: Top-1 accuracy, test-time Cross-Entropy (CE) on all 6 datasets
- **Expected outcome**:
  - Taxonomy Parent prompt should achieve highest Top-1 accuracy on OOD datasets among all 4 variants
  - Taxonomy Parent should have lowest test-time CE across datasets
  - Shuffle Parent should perform worse than Taxonomy Parent but possibly better than Stack Parent (has hierarchical language even if wrong)
  - Stack Parent should perform worst (correct labels but no relational structure communicated)
- **Baselines**: Baseline prompt (class name only)
- **Dependencies**: C01

## E06: Simulation Validation of LCA as Feature Quality Indicator
- **Verifies**: C04
- **Setup**:
  - Model: Two logistic regression models (model f on causal feature x1+noise x3; model g on confounding feature x2+noise x3)
  - Hardware: CPU (logistic regression)
  - Dataset: Synthetic 4-class Gaussian mixture dataset (n=10,000 samples, 100 independent trials)
  - System: Controlled data generation with known causal and confounding features
- **Procedure**:
  1. Generate 4-class dataset: x1 ∈ {1,3,15,17} (hierarchy-aligned), x2 ∈ {1,17,7,21} (non-hierarchy), x3=0 (noise). Each class follows N(mu_c, I).
  2. Design hierarchy: root→{class1,class2}, root→{class3,class4} (x1 supports this, x2 does not)
  3. Train model f on (x1, x3) features; train model g on (x2, x3) features
  4. For OOD: only x1 and x3 are observed (x2 is absent)
  5. Compute ID Top-1 error, ID LCA distance (depth-based), OOD Top-1 error for both models
  6. Average results across 100 independent trials
- **Metrics**: ID Top-1 error (↓), ID LCA distance (↓), OOD Top-1 error (↓) for models f and g
- **Expected outcome**:
  - Model g (confounding features) should achieve lower ID Top-1 error than model f (causal features)
  - Model f (causal features) should achieve lower ID LCA distance than model g
  - Model f should achieve better (lower) OOD Top-1 error than model g
  - This demonstrates LCA distance predicts OOD better than Top-1 accuracy even in controlled settings
- **Baselines**: Model g (confounding-feature model) serves as baseline
- **Dependencies**: none
