---
# Experiment Plans

## E01: Main Quantitative Comparison — Intra-LPIPS and FID on 10-shot Adaptation Tasks
- **Verifies**: C01, C02
- **Setup**:
  - Model: DDPM-TAN (DDPM backbone with adaptor, c=4, d=8, 1.3% params) and LDM-TAN (LDM backbone, c=2, d=8, 1.6% params)
  - Hardware: 8× NVIDIA A100 GPUs
  - Dataset: Source — FFHQ (faces) and LSUN Church. Target — 10-shot subsets of: Babies, Sunglasses, Raphael's paintings, Amedeo Modigliani's paintings, Sketches (from FFHQ); Haunted Houses, Landscape drawings (from LSUN Church). For FID: Sunglasses 2,500 images, Babies 2,700 images reference sets.
  - System: DDPM pre-trained similar to DDPM-PA [34]; LDM pre-trained from [23]. All baselines from StyleGAN2 [12] codebase.
- **Procedure**:
  1. Pre-train binary classifier pϕ: fine-tune an ImageNet pre-trained model with binary head on 10 target-domain images to distinguish source vs. target.
  2. Initialize adaptor layers ψl with all parameters = 0 (so initial output matches frozen pre-trained model).
  3. For each of 300 iterations: sample x0 from 10-shot target dataset, sample t uniformly from {1,...,T}, compute adversarial noise ε* via J=10 PGD steps with ω=0.02 (Eq. 8), compute similarity-guided loss L(ψ) with γ=5 (Eq. 9), update only adaptor parameters ψ via gradient descent with lr=5×10^-5 (DDPM) or lr=1×10^-5 (LDM), batch size 40.
  4. At evaluation: generate 1,000 images per method; compute Intra-LPIPS (assign each image to nearest training sample by LPIPS, average pairwise LPIPS within clusters, average across clusters). For FID: generate 10,000 images, compare against full reference dataset.
  5. Compare DDPM-TAN and LDM-TAN against baselines: TGAN (100% params), TGAN+ADA (100%), EWC (100%), CDC (100%), DCL (100%), DDPM-PA (100%).
- **Metrics**: Intra-LPIPS (↑, higher = more diverse); FID (↓, lower = better quality)
- **Expected outcome**:
  - DDPM-TAN and LDM-TAN achieve higher Intra-LPIPS than all baselines on most adaptation tasks
  - LDM-TAN achieves highest Intra-LPIPS on LSUN Church → Landscape drawings among all methods
  - TAN achieves substantially lower FID than all baselines on FFHQ→Sunglasses
  - TAN shows improvement over DDPM-PA on FID for both Babies and Sunglasses tasks
- **Baselines**: TGAN, TGAN+ADA, EWC, CDC, DCL, DDPM-PA (all implemented on StyleGAN2 codebase)
- **Dependencies**: none

## E02: Additional Adaptation Tasks — Sketches and Amedeo's Paintings (Appendix)
- **Verifies**: C01
- **Setup**:
  - Model: DDPM-TAN with same configuration as E01
  - Hardware: 8× NVIDIA A100 GPUs
  - Dataset: Source — FFHQ. Target — 10-shot Sketches and 10-shot Amedeo Modigliani's paintings
  - System: Same as E01
- **Procedure**:
  1. Follow same training procedure as E01 for the two additional target domains.
  2. Evaluate Intra-LPIPS following the same 1,000-image generation and cluster-assignment procedure.
  3. Compare against TGAN, TGAN+ADA, EWC, CDC, DCL, DDPM-PA baselines.
- **Metrics**: Intra-LPIPS (↑)
- **Expected outcome**:
  - DDPM-TAN surpasses all baselines on FFHQ→Sketches by a significant margin
  - DDPM-TAN is competitive or better than baselines on FFHQ→Amedeo's paintings
- **Baselines**: TGAN, TGAN+ADA, EWC, CDC, DCL, DDPM-PA
- **Dependencies**: none

## E03: Efficiency Comparison — Iterations, GPU Hours, and Memory
- **Verifies**: C03
- **Setup**:
  - Model: DDPM-TAN vs. direct DDPM fine-tuning baseline
  - Hardware: Single GPU for baseline comparison; ×8 NVIDIA A100 for TAN
  - Dataset: FFHQ → 10-shot Sunglasses
  - System: Baseline uses batch size 5 on one GPU, 5,000 iterations (same as DDPM-PA). TAN uses 300 iterations, batch size 40, ×8 A100.
- **Procedure**:
  1. Train direct DDPM fine-tuning (100% parameters, batch size 5, 1 GPU) for 5,000 iterations; record wall-clock time and peak GPU memory.
  2. Train DDPM-TAN (adaptor only, batch size 40, ×8 A100) for 300 iterations; record wall-clock time and peak GPU memory.
  3. Record parameter rate (trainable params / total params) for each method.
  4. Compare quality (FID) at convergence for each method.
- **Metrics**: Wall-clock time (GPU hours), peak GPU memory (GB), parameter rate (%), iterations to convergence
- **Expected outcome**:
  - DDPM-TAN requires substantially fewer GPU hours than direct fine-tuning at 5,000 iterations
  - DDPM-TAN uses substantially less GPU memory than direct fine-tuning
  - DDPM-TAN achieves better image quality (lower FID) with fewer iterations
- **Baselines**: Direct DDPM fine-tuning (100% parameters)
- **Dependencies**: none

## E04: Toy 2D Experiment — Gradient Direction Correction and Distribution Coverage
- **Verifies**: C04
- **Setup**:
  - Model: Simple neural network DDPM trained on 2D Gaussian data
  - Hardware: Not specified
  - Dataset: Source — 2D Gaussian N([1,1], I); Target — 2D Gaussian N([-1,-1], I); 10-shot target samples (repeated 1,000× for batch comparison)
  - System: Four settings compared — (a) DDPM baseline with 10,000 source samples, (b) DDPM baseline with 10-shot target samples, (c) DDPM + similarity-guided training only, (d) DDPM-TAN (similarity + adversarial noise)
- **Procedure**:
  1. Train DDPM on source distribution N([1,1], I).
  2. Compute gradient of output layer at first iteration for all four settings with same noise and timestep t.
  3. Use 10,000 samples as reference gradient direction (reliable reference, close to 45° southwest).
  4. Visualize adversarial noise distribution (red points) to show shift from circular to elliptical along gradient principal axis.
  5. Generate 20,000 samples from baseline DDPM and DDPM-TAN after transfer; visualize as heatmaps.
  6. Plot sampling process trajectory (cyan = DDPM, gold = DDPM-TAN) against sample distribution heatmap.
- **Metrics**: Angular deviation of gradient direction from reference; concentration of samples near target mean [-1,-1] in heatmap
- **Expected outcome**:
  - DDPM gradient (10-shot, no adaptation) has largest angular deviation from reference direction
  - Similarity-guided only reduces deviation compared to vanilla DDPM
  - DDPM-TAN has smallest angular deviation from reference, closest to reliable gradient
  - Adversarial noise distribution shifts from circle (normal Gaussian) to ellipse aligned with gradient
  - DDPM-TAN heatmap shows brighter concentration near target mode [-1,-1] vs. baseline
  - Sampling trajectories of DDPM and DDPM-TAN are approximately parallel in heatmap visualization
- **Baselines**: DDPM (10,000 samples reference), DDPM (10-shot), DDPM + similarity only
- **Dependencies**: none

## E05: Ablation Study — Component Contribution (Figure 4)
- **Verifies**: C05
- **Setup**:
  - Model: Four variants: (1) Baseline (direct fine-tuning, all parameters), (2) Adaptor only (no similarity, no adversarial noise), (3) DPMs-TAN w/o adversarial noise (adaptor + similarity-guided only), (4) DPMs-TAN full (adaptor + similarity + adversarial noise)
  - Hardware: 8× NVIDIA A100 GPUs
  - Dataset: FFHQ → 10-shot Sunglasses
  - System: All models trained for 300 iterations; same fixed noise inputs used to generate comparison images
- **Procedure**:
  1. Train variant (1): direct fine-tuning of full DDPM model on 10-shot Sunglasses for 300 iterations.
  2. Train variant (2): freeze pre-trained DDPM, train only adaptor layer (initialized to 0) using standard DDPM loss, 300 iterations.
  3. Train variant (3): freeze pre-trained DDPM, train adaptor with similarity-guided loss only (no adversarial noise), γ=5, 300 iterations.
  4. Train variant (4): full DDPM-TAN with adaptor + similarity-guided + adversarial noise (J=10, ω=0.02), 300 iterations.
  5. Generate images from same fixed noise inputs; compute FID for each variant.
  6. Visually inspect whether sunglasses are successfully applied to all generated faces.
- **Metrics**: FID (↓), qualitative visual inspection of sunglasses transfer completeness
- **Expected outcome**:
  - Adaptor-only achieves slightly worse FID than direct fine-tuning baseline at 300 iterations
  - Adding similarity-guided training (variant 3) substantially improves FID over adaptor-only
  - Full DDPM-TAN (variant 4) achieves best FID, improving further over variant 3
  - Variants 3 and 4 successfully transfer sunglasses to all generated faces; variants 1 and 2 fail on some images
  - FID decreases monotonically from variant 1 → 4 (with adaptor being the exception)
- **Baselines**: Direct fine-tuning (variant 1)
- **Dependencies**: E01
