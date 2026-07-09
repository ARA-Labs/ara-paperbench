# Related Work

## RW01: Elsayed et al., 2018 (Adversarial Reprogramming)
- **DOI**: ICLR 2018
- **Type**: imports
- **Delta**:
  - What changed: Original adversarial reprogramming; SMM replaces fixed binary mask M with sample-specific CNN-generated continuous masks
  - Why: Fixed mask prevents sample-level adaptation and causes suboptimal approximation error
- **Claims affected**: C01, C02
- **Adopted elements**: The core VR paradigm of adding learnable pattern to input without modifying model; binary mask concept as the baseline Fshr

## RW02: Bahng et al., 2022 (Watermarking VR)
- **DOI**: arXiv:2203.17274
- **Type**: baseline
- **Delta**:
  - What changed: Full/Medium/Narrow watermarking uses shared all-ones or partial binary masks; SMM generates per-sample three-channel continuous masks
  - Why: Different images prefer different mask types (Figure 1); shared mask increases approximation error
- **Claims affected**: C01, C03, C04
- **Adopted elements**: Resizing-based input transformation r(xi) (bilinear upsampling); concept of mask coverage area (Full=all-ones baseline in SMM); δ shared across all images

## RW03: Chen et al., 2023 (ILM / Understanding Visual Prompting)
- **DOI**: CVPR 2023
- **Type**: imports
- **Delta**:
  - What changed: Proposed ILM label mapping; SMM builds on ILM and adopts the same experimental protocol (datasets, splits, hyperparameters)
  - Why: ILM is the strongest output mapping baseline; used as fout in main SMM experiments
- **Claims affected**: C03, C04
- **Adopted elements**: ILM algorithm (Algorithm 4), dataset splits, training hyperparameters for ResNet, padding-based VR method (Pad baseline)

## RW04: Tsai et al., 2020 (Reprogramming Black-Box Models)
- **DOI**: ICML 2020
- **Type**: baseline
- **Delta**:
  - What changed: Frequency-based label mapping (FLM) for padding-based VR; SMM uses ILM for main results, FLM as secondary comparison
  - Why: FLM is a simpler fixed mapping; SMM outperforms on all mapping strategies
- **Claims affected**: C03
- **Adopted elements**: Padding-based VR structure; FLM as secondary evaluation method

## RW05: Tsao et al., 2024 (AutoVP)
- **DOI**: ICLR 2024
- **Type**: extends
- **Delta**:
  - What changed: AutoVP automates the selection of padding/scaling for VR; SMM instead generates dynamic sample-specific masks
  - Why: Automation of shared masks still doesn't address the fundamental sample-level adaptation gap
- **Claims affected**: C01
- **Adopted elements**: Motivation for scalable VR approaches

## RW06: He et al., 2016 (ResNet)
- **DOI**: CVPR 2016
- **Type**: imports
- **Delta**:
  - What changed: SMM uses ResNet-18 and ResNet-50 as frozen pre-trained classifiers; CNN architecture design for fmask was inspired by ResNet's localized visual perception
  - Why: CNNs efficiently capture local visual patterns with fewer parameters than MLPs or ViTs
- **Claims affected**: C03
- **Adopted elements**: ResNet architecture as pre-trained backbone; rationale for using CNN (not MLP) as mask generator

## RW07: Dosovitskiy et al., 2020 (ViT)
- **DOI**: arXiv:2010.11929
- **Type**: imports
- **Delta**:
  - What changed: SMM applies to ViT-B32 with a 6-layer CNN mask generator adapted for 384×384 input; standard ViT prompting methods add tokens before/within encoder layers
  - Why: SMM is model-agnostic (applies to both CNN and transformer architectures)
- **Claims affected**: C04
- **Adopted elements**: ViT-B32 as pre-trained backbone for evaluation

## RW08: Jia et al., 2022 (Visual Prompt Tuning)
- **DOI**: ECCV 2022
- **Type**: bounds
- **Delta**:
  - What changed: VPT adds prompt tokens alongside image embeddings; SMM modifies the raw pixel input before the model. SMM is model-agnostic while VPT is ViT-specific
  - Why: SMM's input-space approach avoids architecture-specific modifications
- **Claims affected**: C04
- **Adopted elements**: Motivation for parameter-efficient prompting methods

## RW09: Kearns & Vazirani, 1994 (PAC Learning)
- **DOI**: MIT Press, 1994
- **Type**: imports
- **Delta**:
  - What changed: SMM uses PAC learning framework to formally define approximation error and prove Proposition 4.3
  - Why: Provides theoretical grounding for the claim that larger hypothesis spaces yield lower approximation error
- **Claims affected**: C02
- **Adopted elements**: Approximation error definition (Definition 4.1), Theorem 4.2 proof structure

## RW10: Hu et al., 2021 (LoRA)
- **DOI**: ICLR 2022
- **Type**: bounds
- **Delta**:
  - What changed: LoRA injects low-rank adapters into model layers; SMM modifies the input space. Comparison (Table 13) shows SMM outperforms LoRA on low-resolution target tasks (CIFAR10/100, SVHN, GTSRB) while being comparable on 128×128 tasks
  - Why: VR handles domain shift in input resolution better than LoRA because it operates in the input space
- **Claims affected**: C03, C04
- **Adopted elements**: Comparison baseline; motivation for VR as an orthogonal approach to finetuning

## RW11: Wang et al., 2022 (Watermarking for OOD Detection)
- **DOI**: NeurIPS 2022
- **Type**: baseline
- **Delta**:
  - What changed: Used watermarking for out-of-distribution detection; SMM improves on this by making masks sample-specific for better classification accuracy
  - Why: Watermarking is the representative resizing-based VR method used as the "Full" baseline
- **Claims affected**: C01, C03
- **Adopted elements**: Full watermarking as the primary resizing-based baseline

## RW12: Van der Maaten & Hinton, 2008 (t-SNE)
- **DOI**: Journal of Machine Learning Research, 2008
- **Type**: imports
- **Delta**:
  - What changed: Used t-SNE to visualize feature space quality for SMM vs baselines; not a baseline method itself
  - Why: Qualitative validation that SMM improves class separation in the feature space
- **Claims affected**: C03
- **Adopted elements**: t-SNE visualization methodology for feature space analysis (Figure 6)
