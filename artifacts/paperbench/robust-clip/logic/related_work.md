# Related Work

## RW01: Mao et al., 2023 (TeCoA)
- **DOI**: ICLR 2023 (Understanding zero-shot adversarial robustness for large-scale models)
- **Type**: baseline
- **Delta**:
  - What changed: FARE replaces supervised cross-entropy loss on ImageNet classes with unsupervised squared ℓ₂ embedding preservation loss
  - Why: Supervised loss distorts unnormalized embeddings and does not generalize to non-ImageNet classes; FARE avoids both issues
- **Claims affected**: C01, C02, C03, C04
- **Adopted elements**: Adversarial training framework, PGD inner maximization, training on ImageNet, ViT-L/14 architecture, training hyperparameter search procedure

## RW02: Radford et al., 2021 (CLIP)
- **DOI**: ICML 2021 (Learning transferable visual models from natural language supervision)
- **Type**: imports
- **Delta**:
  - What changed: FARE fine-tunes CLIP's vision encoder φ to be adversarially robust
  - Why: CLIP's original training on 400M image-text pairs produces excellent zero-shot features but provides no adversarial robustness
- **Claims affected**: C01, C02, C03, C04
- **Adopted elements**: ViT-L/14 architecture, joint embedding space, zero-shot classification protocol, prompt engineering, WIT pretraining

## RW03: Croce & Hein, 2020 (AutoAttack / APGD)
- **DOI**: ICML 2020 (Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks)
- **Type**: imports
- **Delta**:
  - What changed: APGD used as evaluation attack; initial step size set to ε; targeted DLR loss used (stronger than untargeted in Mao et al.)
  - Why: Provides reliable, parameter-free adversarial evaluation
- **Claims affected**: C03, C04
- **Adopted elements**: APGD-CE and APGD-DLR attacks; 100-iteration evaluation protocol

## RW04: Madry et al., 2018 (PGD Adversarial Training)
- **DOI**: ICLR 2018 (Towards deep learning models resistant to adversarial attacks)
- **Type**: imports
- **Delta**:
  - What changed: PGD applied to embedding preservation loss rather than classification loss; unsupervised setting
  - Why: PGD is the standard inner maximization solver for adversarial training
- **Claims affected**: C01, C02
- **Adopted elements**: Min-max adversarial training formulation; PGD inner maximization

## RW05: Schlarmann & Hein, 2023
- **DOI**: ICCV Workshop on Adversarial Robustness In the Real World, 2023
- **Type**: bounds
- **Delta**:
  - What changed: FARE provides a defense against the attacks demonstrated in this work; new ensemble attack pipeline is stronger and 7.7× faster than original
  - Why: Establishes that imperceptible attacks on LVLMs are practical threats
- **Claims affected**: C03
- **Adopted elements**: Attack pipeline design for LVLM evaluation; targeted attack success criterion

## RW06: Liu et al., 2023a / 2023b (LLaVA / LLaVA-1.5)
- **DOI**: NeurIPS 2023 / arXiv:2310.03744
- **Type**: imports
- **Delta**:
  - What changed: FARE-CLIP substituted as vision encoder; no modification to LLM or projection layers
  - Why: LLaVA-1.5 7B is a primary evaluation target LVLM
- **Claims affected**: C01, C03, C05, C06
- **Adopted elements**: LVLM architecture, evaluation prompts, VQA/captioning benchmarks

## RW07: Awadalla et al., 2023 (OpenFlamingo)
- **DOI**: arXiv:2308.01390
- **Type**: imports
- **Delta**:
  - What changed: FARE-CLIP substituted as vision encoder; no modification to MPT-7B or cross-attention
  - Why: OpenFlamingo 9B is the second primary evaluation target LVLM
- **Claims affected**: C01, C07
- **Adopted elements**: LVLM architecture, zero-shot evaluation setup, COCO/Flickr evaluation

## RW08: Kim et al., 2020; Jiang et al., 2020; Fan et al., 2021 (Unsupervised Adversarial SSL)
- **DOI**: NeurIPS 2020 (multiple)
- **Type**: refutes
- **Delta**:
  - What changed: FARE uses embedding preservation loss rather than contrastive loss; targets CLIP's downstream zero-shot tasks
  - Why: Prior unsupervised adversarial SSL methods (SimCLR-based) do not preserve the original embedding needed for zero-shot transfer without label-based linear heads
- **Claims affected**: C02
- **Adopted elements**: Unsupervised adversarial fine-tuning concept

## RW09: Gowal et al., 2020 (Self-Supervised Adversarial Training / BYOL)
- **DOI**: ICLR 2020
- **Type**: refutes
- **Delta**:
  - What changed: FARE targets zero-shot tasks and requires no linear head; embedding preservation replaces BYOL-style self-supervised loss
  - Why: Gowal et al. requires adding linear heads for downstream classification; cannot be used zero-shot
- **Claims affected**: C02, C04
- **Adopted elements**: Self-supervised adversarial training concept

## RW10: Qi et al., 2023 (Visual Adversarial Jailbreaking)
- **DOI**: arXiv:2306.13213
- **Type**: bounds
- **Delta**:
  - What changed: FARE reduces jailbreaking attack success rates; evaluation uses Qi et al. attack with 5000 iterations, α=1/255
  - Why: Establishes visual jailbreaking of LVLMs as a practical threat
- **Claims affected**: C01 (extended to jailbreak domain)
- **Adopted elements**: Jailbreak attack methodology, 40 harmful prompts, category taxonomy (identity/disinfo/crime/x-risk)

## RW11: Li et al., 2023b (POPE Benchmark)
- **DOI**: arXiv:2305.10355
- **Type**: imports
- **Delta**:
  - What changed: POPE used to measure hallucination rates of LVLMs with different vision encoders
  - Why: Standard benchmark for object hallucination in LVLMs
- **Claims affected**: C05
- **Adopted elements**: POPE evaluation protocol, random/popular/adversarial splits, F1-score metric

## RW12: Loshchilov & Hutter, 2018 (AdamW)
- **DOI**: ICLR 2018 (Decoupled weight decay regularization)
- **Type**: imports
- **Delta**:
  - What changed: AdamW used as outer optimizer in FARE fine-tuning with β1=0.9, β2=0.95, WD=1e-4
  - Why: Standard optimizer for transformer fine-tuning
- **Claims affected**: none (implementation detail)
- **Adopted elements**: AdamW optimizer with decoupled weight decay
