# Related Work

## RW01: Wang et al., 2022 — L2P (Learning to Prompt)
- **DOI**: CVPR 2022 proceedings
- **Type**: baseline
- **Delta**:
  - What changed: L2P uses a fixed-size prompt pool (0.123M params) optimized via cosine similarity queries; SEMA uses on-demand adapter expansion with z-score detection.
  - Why: L2P's fixed pool limits adaptation to long or diverse task sequences.
- **Claims affected**: C01, C02
- **Adopted elements**: Evaluation benchmark protocol (same ViT-B/16-IN1K backbone, class splits, data shuffling)

## RW02: Wang et al., 2022 — DualPrompt
- **DOI**: ECCV 2022 proceedings
- **Type**: baseline
- **Delta**:
  - What changed: DualPrompt uses G-Prompt (general) + E-Prompt (expert, task-specific), expanding linearly by task. SEMA uses on-demand expansion, growing sub-linearly.
  - Why: DualPrompt's linear growth (1.022M params for CIFAR-100 10-task) impairs efficiency.
- **Claims affected**: C01, C02
- **Adopted elements**: CIL evaluation protocol

## RW03: Smith et al., 2023 — CODA-P
- **DOI**: CVPR 2023 proceedings
- **Type**: baseline
- **Delta**:
  - What changed: CODA-P expands attention-conditioned prompt pools per task (3.917M params for CIFAR-100); SEMA expands adapters on demand (0.645M).
  - Why: CODA-P's attention-weighted prompt selection is expensive and linearly scaling.
- **Claims affected**: C01, C02
- **Adopted elements**: CIL benchmark comparison

## RW04: Zhou et al., 2023 — SimpleCIL and ADAM
- **DOI**: arXiv:2303.10049 / RevisitingCIL
- **Type**: baseline
- **Delta**:
  - What changed: ADAM adds a single adapter in the first session and freezes it; SEMA continuously expands adapters on demand across all sessions.
  - Why: First-session-only adaptation limits plasticity for later tasks.
- **Claims affected**: C01, C03
- **Adopted elements**: AdaptFormer-style functional adapter architecture; ViT-B/16 backbone; class splitting protocol

## RW05: Liang and Li, 2024 — InfLoRA
- **DOI**: CVPR 2024 proceedings
- **Type**: baseline
- **Delta**:
  - What changed: InfLoRA uses LoRA with gradient projection to prevent interference; SEMA uses modular adapters with on-demand expansion and mixture routing.
  - Why: InfLoRA's post-training gradient projection adds computational overhead (two full data passes per task).
- **Claims affected**: C01
- **Adopted elements**: LoRA as an alternative functional adapter type (Table 3)

## RW06: Chen et al., 2022 — AdaptFormer
- **DOI**: NeurIPS 2022; arXiv:2205.13535
- **Type**: imports
- **Delta**:
  - What changed: AdaptFormer uses a single adapter for all tasks in a standard fine-tuning setting; SEMA uses AdaptFormer's adapter architecture as its functional adapter but adds RDs, routers, and on-demand expansion for CL.
  - Why: Direct fine-tuning causes forgetting; CL requires the expansion + freezing mechanism.
- **Claims affected**: C04
- **Adopted elements**: Down-projection + ReLU + up-projection architecture (Eq. 1); side-branch insertion after MLP LayerNorm

## RW07: Hu et al., 2021 — LoRA
- **DOI**: arXiv:2106.09685
- **Type**: imports
- **Delta**:
  - What changed: LoRA is used as an alternative functional adapter inside SEMA's modular framework.
  - Why: To demonstrate adapter-agnosticism of SEMA framework.
- **Claims affected**: C04
- **Adopted elements**: Low-rank matrix parameterisation of weight updates

## RW08: Jie and Deng, 2022 — Convpass
- **DOI**: arXiv:2207.07039
- **Type**: imports
- **Delta**:
  - What changed: Convpass adapter used as third functional adapter variant in SEMA.
  - Why: Broadens demonstration of SEMA's adapter-agnosticism.
- **Claims affected**: C04
- **Adopted elements**: Convolutional bypass adapter architecture

## RW09: Hinton and Salakhutdinov, 2006 — Autoencoder
- **DOI**: Science 313(5786):504–507
- **Type**: imports
- **Delta**:
  - What changed: AE used as the representation descriptor for distribution shift detection.
  - Why: Simple reconstruction objective provides a natural novelty score without requiring class labels.
- **Claims affected**: C03
- **Adopted elements**: Encoder-decoder architecture; reconstruction loss $\|x - g(x)\|_2^2$

## RW10: Zhou et al., 2024 — EASE (Expandable Subspace Ensemble)
- **DOI**: CVPR 2024
- **Type**: extends
- **Delta**:
  - What changed: EASE expands task-specific adapters at all layers per task (linear growth); SEMA expands on demand (sub-linear). SEMA outperforms EASE on limited-data settings (Tables 11, 12) with fewer parameters.
  - Why: Linear expansion impairs knowledge reuse; SEMA's selective expansion is more efficient.
- **Claims affected**: C02, C03
- **Adopted elements**: Concept of architecture-based expansion for PTM-based CL

## RW11: McDonnell et al., 2023 — RanPAC
- **DOI**: NeurIPS 2023
- **Type**: extends
- **Delta**:
  - What changed: RanPAC uses random projection + prototype classifiers on frozen PTM features; SEMA+RanPAC combines SEMA's adaptive representations with RanPAC's statistical alignment, outperforming both individually (Table 14).
  - Why: The two approaches are orthogonal (representation adaptation vs. classifier alignment).
- **Claims affected**: C01
- **Adopted elements**: Random projection classification head technique

## RW12: Gong et al., 2019 — Memory-Augmented AE for Anomaly Detection
- **DOI**: ICCV 2019 proceedings
- **Type**: imports
- **Delta**:
  - What changed: The z-score based reconstruction error novelty detection is inspired by AE-based anomaly detection using reconstruction error as a novelty proxy.
  - Why: Reliable out-of-distribution detection without requiring OOD labels.
- **Claims affected**: C03
- **Adopted elements**: Reconstruction error as distribution shift indicator; z-score normalization for robustness
