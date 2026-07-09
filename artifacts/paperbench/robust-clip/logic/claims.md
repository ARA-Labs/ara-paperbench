# Claims

## C01: FARE outperforms TeCoA in clean and robust LVLM performance
- **Statement**: FARE2 and FARE4 vision encoders yield higher clean and robust (ℓ∞) performance than TeCoA2 and TeCoA4 respectively on average across COCO, Flickr30k, TextVQA, and VQAv2 tasks for both OpenFlamingo 9B and LLaVA-1.5 7B.
- **Status**: supported
- **Falsification criteria**: If TeCoA achieves equal or higher average performance than FARE (at matching training ε) on the LVLM task suite, the claim is refuted.
- **Proof**: [E01]
- **Dependencies**: C02
- **Tags**: FARE, TeCoA, LVLM, robustness, clean performance, CIDEr, VQA

## C02: FARE-CLIP preserves the original CLIP embedding structure better than TeCoA
- **Statement**: FARE fine-tuning results in significantly lower clean embedding distortion (||φ_FT(x) - φ_Org(x)||²₂) and lower adversarial embedding distortion compared to TeCoA at matching training radius, enabling drop-in replacement in LVLMs without retraining.
- **Status**: supported
- **Falsification criteria**: If TeCoA's clean or adversarial embedding loss is equal to or lower than FARE's, the claim is refuted.
- **Proof**: [E06]
- **Dependencies**: none
- **Tags**: embedding preservation, FARE, TeCoA, embedding loss, drop-in replacement

## C03: FARE makes LVLMs fully robust against stealthy targeted ℓ∞ attacks
- **Statement**: LLaVA-1.5 7B equipped with FARE4-CLIP achieves 0% targeted attack success rate for ε = 2/255 and ε = 4/255 across all 6 target captions (150 trials total). FARE2 achieves 0% at ε = 2/255 and 2.0% mean success rate at ε = 4/255.
- **Status**: supported
- **Falsification criteria**: If any targeted attack with ε ≤ 4/255 succeeds against FARE4-LLaVA, the claim is refuted.
- **Proof**: [E02]
- **Dependencies**: C01
- **Tags**: targeted attacks, FARE4, robustness, LLaVA, stealthy attacks, imperceptible perturbations

## C04: FARE maintains better zero-shot classification performance than TeCoA on non-ImageNet datasets
- **Statement**: FARE2-CLIP achieves 7.0% higher average clean zero-shot accuracy (67.0% vs 60.0%) and comparable adversarial accuracy (43.1% at ε=2/255 vs TeCoA2's 43.6%) than TeCoA2 on 13 non-ImageNet zero-shot datasets. FARE4 achieves 6.9% higher clean accuracy than TeCoA4 (61.1% vs 54.2%).
- **Status**: supported
- **Falsification criteria**: If TeCoA achieves equal or higher average clean accuracy than FARE on non-ImageNet datasets, the claim is refuted.
- **Proof**: [E03]
- **Dependencies**: C02
- **Tags**: zero-shot classification, FARE, TeCoA, generalization, clean accuracy, robustness

## C05: FARE reduces LLaVA hallucination rate compared to TeCoA
- **Statement**: LLaVA-1.5 7B with FARE2-CLIP achieves a mean POPE F1-score of 80.8 vs TeCoA2's 75.9. FARE4 achieves 76.3 vs TeCoA4's 72.2. FARE models are closer to the original CLIP (84.5).
- **Status**: supported
- **Falsification criteria**: If TeCoA achieves equal or higher mean POPE F1-score than FARE at matching training radius, the claim is refuted.
- **Proof**: [E04]
- **Dependencies**: C02
- **Tags**: hallucination, POPE, FARE, TeCoA, LLaVA, embedding preservation

## C06: FARE preserves LLaVA's chain-of-thought reasoning ability better than TeCoA
- **Statement**: LLaVA-1.5 7B with FARE2 achieves 63.4% SQA-I accuracy (2.3% above TeCoA2's 61.1%) and FARE4 achieves 62.3% (2.4% above TeCoA4's 59.9%). FARE2 is only 1.1% below the original CLIP (64.5%).
- **Status**: supported
- **Falsification criteria**: If TeCoA achieves equal or higher SQA-I accuracy than FARE at matching training radius, the claim is refuted.
- **Proof**: [E04]
- **Dependencies**: C02
- **Tags**: SQA-I, chain-of-thought, reasoning, FARE, TeCoA, LLaVA

## C07: Transfer attacks between LVLMs sharing non-robust CLIP are effective, but fail with robust encoders
- **Statement**: Adversarial COCO images (ε=4/255) generated against OF-CLIP transfer to LLaVA-CLIP with CIDEr score 25.5 (vs clean 115.5), and vice versa (LLaVA-CLIP adversarial transferred to OF: CIDEr 8.3 vs clean 79.7). With robust encoders (FARE2/FARE4), transfer attacks achieve near-clean performance.
- **Status**: supported
- **Falsification criteria**: If transfer attacks fail against the non-robust CLIP LVLMs, or if they succeed against FARE-equipped LVLMs, the claim is refuted.
- **Proof**: [E01]
- **Dependencies**: C01
- **Tags**: transfer attacks, CLIP, FARE, OpenFlamingo, LLaVA, cross-model transfer
