# Problem Specification

## Observations

### O1: CLIP is the frozen vision encoder of most major LVLMs
- **Statement**: OpenFlamingo (9B) and LLaVA-1.5 (7B, 13B) both use the frozen ViT-L/14 CLIP model as their vision encoder. The vision encoder is frozen during LVLM training, and only interaction layers (projection, cross-attention) are learned.
- **Evidence**: Section 2 (Multi-modal models), experimental setup §4
- **Implication**: A single robust CLIP vision encoder can make all downstream LVLMs robust simultaneously without requiring LVLM retraining.

### O2: CLIP (and LVLMs built on it) is completely non-robust to adversarial attacks
- **Statement**: Under ℓ∞ perturbations of ε = 2/255, the original CLIP achieves 0% robust accuracy across all zero-shot classification datasets. Under targeted attacks on LLaVA with ε = 2/255 and ε = 4/255, the original CLIP-based LLaVA is susceptible in 100% of cases (25/25 for all 6 target captions at both radii).
- **Evidence**: Table 4 (ℓ∞=2/255 row for CLIP: all 0.0%), Table 3 (CLIP column), §4.1
- **Implication**: LVLMs can be weaponized by malicious third parties to spread misinformation or defraud users via imperceptible image manipulations.

### O3: TeCoA (supervised adversarial fine-tuning) degrades clean performance significantly
- **Statement**: TeCoA2-CLIP drops average zero-shot clean accuracy from 73.1% to 60.0% on non-ImageNet datasets (a 13.1% drop). TeCoA4-CLIP drops to 54.2%. For LLaVA captioning (COCO CIDEr), TeCoA2 drops from 115.5 to 98.4 and TeCoA4 drops to 88.3.
- **Evidence**: Table 4 (clean row), Table 1 (LLaVA-1.5 clean column)
- **Implication**: Supervised fine-tuning on ImageNet class labels introduces distortions that hurt generalization to unseen classes and unnormalized embeddings used by LVLMs.

### O4: TeCoA's supervised loss does not preserve the original CLIP embedding structure
- **Statement**: TeCoA2-CLIP has a mean clean embedding loss (||φ_FT(x) - φ_Org(x)||²₂) of 236.9 and TeCoA4 of 292.7, compared to FARE2's 32.7 and FARE4's 47.6.
- **Evidence**: Table 14, Appendix C.4
- **Implication**: Because TeCoA's cross-entropy loss uses cosine similarity (ignoring radial direction), the unnormalized embeddings used by LVLMs are heavily distorted.

## Gaps

### G1: No label-free robust CLIP encoder exists
- **Statement**: The only prior method for robust CLIP (TeCoA, Mao et al. 2023) requires ImageNet labels during fine-tuning, binding it to ImageNet's class structure.
- **Caused by**: O1, O2, O3
- **Existing attempts**: TeCoA performs supervised adversarial training using ImageNet cross-entropy loss on CLIP's zero-shot classifier.
- **Why they fail**: The cosine-similarity-based loss is invariant to radial rescaling of embeddings; fine-tuning can freely distort the unnormalized embedding in the radial direction, breaking LVLM downstream tasks that use unnormalized embeddings (O3, O4).

### G2: Replacing CLIP in LVLMs requires LVLM retraining with prior methods
- **Statement**: Because TeCoA changes the embedding distribution significantly, plugging TeCoA-CLIP into LLaVA/OpenFlamingo degrades clean performance substantially (Table 1), suggesting the connection layers would need retraining.
- **Caused by**: O3, O4
- **Existing attempts**: None — Mao et al. (2023) did not demonstrate successful LVLM integration without retraining.
- **Why they fail**: Embedding distortion from supervised fine-tuning makes the fine-tuned encoder incompatible with frozen LVLM connection layers.

## Key Insight

- **Insight**: Adversarial robustness can be achieved by minimizing the ℓ₂ distance between the perturbed embedding φ(z) and the original clean embedding φ_Org(x). This simultaneously (a) forces robustness by constraining how much adversarial perturbations can move the embedding, and (b) preserves clean performance by driving φ(x) → φ_Org(x) as the loss approaches zero. No labels are needed.
- **Derived from**: O1, O2, O3, O4
- **Enables**: A single unsupervised fine-tuning objective (FARE loss, Eq. 3) that yields a drop-in robust replacement for CLIP's vision encoder in any downstream task.

## Assumptions

- A1: The CLIP vision encoder is frozen in downstream LVLMs (true for OpenFlamingo and LLaVA-1.5).
- A2: Adversarial robustness in the ℓ∞ threat model is the primary threat model of concern.
- A3: ImageNet is used as the fine-tuning dataset for comparability with TeCoA, but the method requires no labels.
- A4: The class token of ViT-L/14 is sufficient to represent the CLIP visual embedding for FARE loss computation (using all tokens does not improve results; Appendix B.1).
- A5: Two epochs of fine-tuning on ImageNet (≈0.2% of original CLIP training cost) is sufficient for non-trivial robustness.
