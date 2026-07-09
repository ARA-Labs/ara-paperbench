---
# Problem Specification

## Observations

### O1: Gradient-based TTA requires backpropagation per test sample
- **Statement**: State-of-the-art TTA methods (TENT, SAR, CoTTA, MEMO) perform one or more backward passes per test sample, consuming up to 16,836 MB of GPU memory at batch size 64.
- **Evidence**: Table 1 (TENT: 5,165 MB; CoTTA: 16,836 MB at BS=64); Table 8 (#BP ≥ 1 per sample for all gradient-based methods)
- **Implication**: Gradient-based TTA is incompatible with memory-limited edge devices and quantized models.

### O2: Quantized models cannot propagate gradients
- **Statement**: Quantization (e.g., 32-bit → 8-bit or 6-bit) introduces discrete quantizers that are non-differentiable, causing vanishing gradients when backpropagated through multiple layers.
- **Evidence**: Paper §1 (citing Louizos et al., 2019); Table 4 shows only T3A and FOA can be applied to 8-bit/6-bit ViT.
- **Implication**: Any TTA method requiring backpropagation cannot be applied to quantized models deployed in practice.

### O3: Hard-coded hardware accelerators have non-modifiable model parameters
- **Statement**: Specialized computational chips (FPGAs, custom ASICs) often hard-code model parameters, making parameter updates physically impossible.
- **Evidence**: Paper §1 (citing Dass et al., 2023; You et al., 2023)
- **Implication**: Weight-modifying TTA methods are structurally inapplicable on these platforms.

### O4: Existing gradient-free TTA has limited learning capacity
- **Statement**: Prior gradient-free methods (LAME: 54.1%, T3A: 56.9%) underperform gradient-based methods (SAR: 62.7%) on ImageNet-C (severity 5) because they do not exploit model feedback for optimization.
- **Evidence**: Table 2; LAME performs worse than NoAdapt (55.5%) on average accuracy.
- **Implication**: Simply avoiding backpropagation at the cost of performance is not an acceptable solution.

### O5: CMA-ES cannot directly optimize high-dimensional deep model parameters
- **Statement**: Directly applying CMA-ES to optimize normalization layer parameters (ultra-high-dimensional) causes catastrophic failure (0.1% accuracy), as shown in Table 9 (exp4, exp5).
- **Evidence**: Table 9 (norm layers + CMA + Eqn.5 → 0.1%; norm layers + CMA + entropy → 0.1%)
- **Implication**: CMA-ES requires a low-dimensional optimization target to be tractable for TTA.

## Gaps

### G1: No TTA method works on quantized or hard-coded edge models
- **Statement**: All prior high-performing TTA methods require gradient computation and weight modification, making them fundamentally inapplicable to quantized models and hardware-locked deployments.
- **Caused by**: O2, O3
- **Existing attempts**: BN adaptation (Schneider et al., 2020), T3A (Iwasawa & Matsuo, 2021), LAME (Boudiaf et al., 2022)
- **Why they fail**: BN adaptation only works on architectures with batch normalization (not ViT); T3A and LAME have limited learning capacity (G2) without model feedback.

### G2: Gradient-free TTA lacks explicit model feedback for optimization
- **Statement**: Prior gradient-free methods do not update learnable parameters using the model's response to test inputs, capping their OOD generalization performance.
- **Caused by**: O4
- **Existing attempts**: T3A adjusts class prototypes; LAME corrects output logits; BN adaptation updates batch normalization statistics.
- **Why they fail**: None of these explicitly optimize learnable parameters in response to per-batch model predictions.

### G3: No suitable unsupervised fitness function exists for CMA in online TTA
- **Statement**: Standard fitness signals for CMA (supervised labels) are unavailable in TTA, and entropy alone leads to degenerate solutions (Table 9, exp6: 44.9% accuracy).
- **Caused by**: O5
- **Existing attempts**: Prediction entropy minimization (Wang et al., 2021)
- **Why they fail**: Entropy is noisy under severe distribution shift; optimizing entropy alone collapses CMA to trivial solutions.

## Key Insight

- **Insight**: Inserting a small low-dimensional input prompt (Np=3 embeddings) reduces the CMA optimization dimension to tractable levels, while a fitness function combining prediction entropy with CLS activation distribution discrepancy provides stable, reliable learning signals without labels.
- **Derived from**: O1, O2, O4, O5
- **Enables**: A fully forward-only, weight-frozen TTA method that (a) works on any model including quantized/hard-coded models, (b) achieves better accuracy than gradient-based TENT, and (c) uses ~6× less memory than TENT.

## Assumptions

- A1: A small set of unlabeled source in-distribution samples (≥32 for ImageNet) is available for computing source statistics {μ^S_i, σ^S_i}.
- A2: Test data arrives in mini-batches (batch size ≥ 1; for single-sample, the FOA-I interval strategy is used).
- A3: The source model architecture supports input prompt concatenation (naturally satisfied for transformer-based models; requires adaptation for CNNs).
- A4: The CLS token activations at the final layer are representative of the overall distribution shift.
- A5: 8-bit quantized models consume 0.25× the memory of 32-bit models (following Liu et al., 2021b).
