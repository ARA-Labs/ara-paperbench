# Problem Specification

## Observations

### O1: Sample-specific mask preferences exist
- **Statement**: For the same VR method (watermarking on OxfordPets via ImageNet ResNet), different images achieve their highest classification confidence under different mask types. Specifically, a Sphynx image reaches peak confidence with medium watermarking (67.3%), Abyssinian with full watermarking (77.1%), and Bengal with narrow watermarking (70.4%).
- **Evidence**: Figure 1 in the paper; qualitative demonstration with three cat images across three mask configurations.
- **Implication**: No single shared mask is simultaneously optimal for all samples; the ideal mask location is image-dependent.

### O2: Shared masks cause positive loss changes for some training samples
- **Statement**: When training VR with a shared all-one matrix mask (full watermarking) on OxfordPets/ImageNet, the distribution of [final loss – initial loss] contains a substantial positive portion (red in Figure 2), meaning some samples' training loss actually increases after optimization. In contrast, finetuning all parameters results in loss decreases for all samples.
- **Evidence**: Figure 2 in the paper; distribution plot of per-sample loss change after training.
- **Implication**: Shared masks constrain the hypothesis space so severely that the global optimum for the shared δ necessarily worsens individual sample losses.

### O3: SMM adds negligible parameters relative to pre-trained model
- **Statement**: The mask generator fmask adds only 26,499 parameters for ResNet-18/50 (0.23% and 0.10% of model parameters respectively) and 102,339 parameters for ViT-B32 (0.12% of model parameters). These constitute only 17.60% (ResNet) and 23.13% (ViT) of the reprogramming pattern size.
- **Evidence**: Table 4 in the paper.
- **Implication**: SMM's additional estimation error is negligible relative to the reduction in approximation error.

### O4: VR fails on fine-grained recognition tasks
- **Statement**: On StanfordCars (196 classes), all input VR methods achieve below 10% accuracy, far below random chance for subtle appearance differentiation.
- **Evidence**: Table 12 in the paper.
- **Implication**: SMM cannot rescue VR when the fundamental task structure is incompatible with input-space perturbations.

## Gaps

### G1: Lack of sample-level adaptation in existing VR methods
- **Statement**: All prior VR methods (Elsayed et al. 2018; Tsai et al. 2020; Bahng et al. 2022; Chen et al. 2023) use a single pre-defined binary mask M ∈ {0,1}^dP shared across all training and test samples.
- **Caused by**: O1, O2
- **Existing attempts**: Padding-based VR (varies mask shape globally), watermarking (varies mask coverage area globally), AutoVP (scalable padding), but all maintain a globally shared mask.
- **Why they fail**: The hypothesis space Fshr(f'P) = {f | f(x) = f'P(r(x) + M ⊙ δ), ∀x ∈ X} is strictly smaller than what is theoretically achievable, causing higher approximation error (Theorem 4.2 + Proposition 4.3).

### G2: Binary masks miss multi-channel image structure
- **Statement**: Existing binary masks treat the three color channels identically, even though different datasets have different channel-priority structure (e.g., SVHN has rich color structure, grayscale-dominated datasets do not).
- **Caused by**: O1
- **Existing attempts**: No prior VR work produces per-channel masks.
- **Why they fail**: A single-channel mask forces the same noise amplitude modulation across R, G, B channels, preventing channel-specific emphasis.

## Key Insight
- **Insight**: The hypothesis space of sample-specific masks with a shared pattern (Fsmm) strictly contains the hypothesis space of shared-mask VR (Fshr) because any constant mask M can be recovered by a CNN with zero weights in the last layer (the bias blast spans all {0,1}^(H*W*C) values). Therefore Errapx(Fshr) ≥ Errapx(Fsmm) by Theorem 4.2.
- **Derived from**: O1, O2; and the PAC learning framework.
- **Enables**: Replacing the fixed binary mask with a lightweight CNN fmask: R^dP → R^dP that produces a distinct three-channel continuous mask per image, while retaining a shared δ to capture dataset-level statistics.

## Assumptions
- A1: The pre-trained model fP is fixed (frozen) during VR training; only fin parameters (δ and ϕ) are updated.
- A2: The target label space is no larger than the source label space: |YT| ≤ |YP|.
- A3: The input domain gap between source and target is bridgeable through input-space perturbations (VR fails on fine-grained tasks like StanfordCars where this gap is too structured).
- A4: The estimation error added by fmask's lightweight CNN does not offset the approximation error reduction (supported by <0.23% parameter overhead and empirical overfitting analysis in Appendix D.3).
