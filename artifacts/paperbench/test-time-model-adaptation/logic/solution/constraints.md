---
# Constraints and Limitations

## Boundary Conditions (Where FOA Works)

### BC1: Transformer-based architectures
- FOA's prompt mechanism (concatenation to patch embeddings) naturally integrates with Vision Transformers (ViT, VisionMamba) because global attention allows prompt tokens to influence all patch representations.
- The system relies on a CLS token at the final layer for activation shifting.

### BC2: Batch size ≥ 2 for stable statistics
- Computing batch statistics μ_i(X_t) and σ_i(X_t) for the fitness function requires at least a few samples.
- For BS=1, the FOA-I interval update strategy buffers I samples before running CMA optimization.
- FOA-I V1 stores CLS token features; FOA-I V2 stores original images.

### BC3: Source statistics availability
- Requires Q ≥ 32 unlabeled source in-distribution samples (no labels needed).
- These can be obtained via OOD detection or directly from training samples.
- Source statistics are precomputed once and stored, not updated during TTA.

### BC4: Low-dimensional optimization target
- CMA-ES is effective up to ~2,304 dimensions (Np=3, d=768 for ViT-Base).
- Full model parameter optimization with CMA-ES is intractable (O(86M) parameters for ViT-Base).

### BC5: Online unsupervised test data
- Works with one-pass online test data stream, no data storage or multi-epoch replay.
- Adapts per mini-batch; no dependency on labels.

## Known Limitations

### L1: Suboptimal on CNN architectures
- On ResNet-50, FOA achieves only 22.6% accuracy (Gaussian noise, level 5), compared to TENT (29.4%) and SAR (30.7%).
- Convolutions are local operations; location-invariant input prompts cannot effectively influence global representations in CNNs as they can in transformers.
- FOA† (replacing CMA with SGD, optimizing norm layers) achieves 33.6% on ResNet-50, suggesting the prompt mechanism itself is the bottleneck for CNNs.

### L2: Requires K forward passes per batch
- K=28 (default) requires 28 forward passes for each test batch, increasing wall-clock time proportionally to K.
- However, these forward passes are memory-efficient (no gradients) and can be parallelized.
- At K=2, FOA is already competitive with TENT while being faster.

### L3: Activation shifting ECE not as good as full FOA
- Activation shifting alone (59.1% accuracy, 12.7% ECE) provides lower ECE benefit than the combined FOA (3.2% ECE).
- The entropy term in the fitness function is crucial for low ECE.

### L4: CMA convergence speed
- CMA requires sufficient iterations (batches) to converge; at the very beginning of adaptation (< 200 test samples), performance may be temporarily below MEMO.
- The activation shifting component helps bridge this early-adaptation gap.

### L5: Source statistics must be computed without prompts
- The source statistics {μ^S_i, σ^S_i} must be computed from the model without prompt insertion to maintain consistency with the non-prompted source distribution.

### L6: Population size trades off efficiency and accuracy
- Larger K improves accuracy but increases computation: K=28 gives 66.3% accuracy; K=2 gives 59.6%.
- K must be chosen based on available compute budget.

## Assumptions

- A1: Model quantization memory scales as 0.25× for 8-bit vs. 32-bit (per Liu et al., 2021b).
- A2: The CLS token at the final layer is the primary representation for classification and distribution characterization.
- A3: Test data distribution is continuously shifting (online setting); no access to future batches.
- A4: The shifting direction from OOD to source domain is approximately captured by center-to-center direction (mean-based shifting).
