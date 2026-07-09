# Experiments

## E01: LVLM Robustness Evaluation (Clean + Adversarial)
- **Verifies**: C01, C07
- **Setup**:
  - Model: OpenFlamingo 9B (MPT-7B backbone) and LLaVA-1.5 7B (Vicuna-7B backbone)
  - Hardware: Not specified in paper (GPU cluster assumed; single-precision and half-precision attacks require significant memory)
  - Dataset: COCO (Lin et al., 2014), Flickr30k (Plummer et al., 2015), VQAv2 (Goyal et al., 2017), TextVQA (Singh et al., 2019)
  - System: Five vision encoders evaluated: CLIP (original), TeCoA2, FARE2, TeCoA4, FARE4 (all ViT-L/14)
- **Procedure**:
  1. Load OpenFlamingo 9B and LLaVA-1.5 7B with each of the five vision encoders substituted in.
  2. Evaluate clean performance on all available images per dataset; report CIDEr for COCO/Flickr30k, VQA accuracy for VQAv2/TextVQA.
  3. For adversarial evaluation, sample 500 images per dataset.
  4. Run APGD attack pipeline (Appendix B.6): first run 100-iteration APGD at half precision for each of 5 ground-truth captions (captioning) or 5 most-frequent ground-truths (VQA); compute metrics after each attack; skip samples that already score below threshold (CIDEr < 10 for COCO, < 2 for Flickr30k; VQA score = 0).
  5. Run final single-precision APGD using the best perturbation found and ground-truth giving lowest score.
  6. For VQA: additionally run targeted attacks with strings "Maybe" and "Word" (not "Word" for TextVQA).
  7. Report clean, ε=2/255, and ε=4/255 performance for each (VLM, encoder) pair, plus average across datasets.
  8. For transfer attacks: use adversarial COCO images generated against OF-CLIP and LLaVA-CLIP, evaluate on all five encoders for both OF and LLaVA; report CIDEr.
- **Metrics**: CIDEr score (Vedantam et al., 2015) for captioning; VQA accuracy (Antol et al., 2015) for QA tasks. Average over datasets.
- **Expected outcome**:
  - FARE models should outperform TeCoA models in average clean and robust performance for LLaVA
  - Original CLIP should achieve best clean but near-zero robust performance
  - Transfer attacks should transfer between OF-CLIP and LLaVA-CLIP, but fail against robust encoders
  - FARE2 should provide higher clean performance than FARE4 at some robustness cost
- **Baselines**: CLIP (original), TeCoA2, TeCoA4
- **Dependencies**: none

## E02: Stealthy Targeted Attack Evaluation
- **Verifies**: C03
- **Setup**:
  - Model: LLaVA-1.5 7B with five vision encoders (CLIP, TeCoA2, FARE2, TeCoA4, FARE4)
  - Hardware: Not specified in paper
  - Dataset: COCO (captions 1–5: 25 randomly sampled images each); stock photos (caption 6: 25 hand-selected images showing patients/syringes)
  - System: APGD with 10,000 iterations; ℓ∞ with ε ∈ {2/255, 4/255}
- **Procedure**:
  1. Define 6 target captions (see Appendix B.8): EmailAPI injection, vaccine misinformation, insult, stock fraud, phishing URL, vaccination side effects.
  2. For captions 1–5: randomly sample 25 images from COCO per caption. For caption 6: use 25 hand-selected medical images.
  3. For each (target caption, image, vision encoder, ε) combination, run APGD for 10,000 iterations minimizing autoregressive cross-entropy with respect to the target string.
  4. Attack succeeds if the target string is exactly contained in the model output.
  5. Report success counts (out of 25) per (target, ε, encoder) and mean success rate per (ε, encoder).
- **Metrics**: Attack success rate (count / 25 per target; mean % across targets)
- **Expected outcome**:
  - Original CLIP should be susceptible to all attacks at both ε values
  - Robust encoders (FARE4, TeCoA4) should achieve near-zero success rate at both ε values
  - FARE4 and TeCoA4 should be completely robust at both radii
  - FARE2 and TeCoA2 should break in only a small fraction of cases at ε = 4/255
  - FARE should produce higher-quality outputs than TeCoA on clean (non-attacked) images
- **Baselines**: CLIP (original), TeCoA2, TeCoA4
- **Dependencies**: none

## E03: Zero-Shot Classification Evaluation
- **Verifies**: C04
- **Setup**:
  - Model: CLIP ViT-L/14 with five vision encoders (CLIP, TeCoA2, FARE2, TeCoA4, FARE4)
  - Hardware: Not specified in paper
  - Dataset: ImageNet (Deng et al., 2009) + 13 zero-shot datasets: CalTech101, StanfordCars, CIFAR10, CIFAR100, DTD, EuroSAT, FGVC Aircrafts, Flowers102, ImageNet-R, ImageNet-Sketch, PCAM, OxfordPets, STL-10
  - System: AutoAttack (first two attacks: APGD-CE + APGD-DLR targeted, 100 iterations each); evaluation on 1000 samples each for robustness; all samples for clean
- **Procedure**:
  1. For each dataset, construct text embeddings by encoding class name prompt templates with CLIP text encoder and averaging across templates per class.
  2. Classify images by nearest-neighbor cosine similarity to class text embeddings.
  3. Evaluate clean accuracy on all samples of each dataset.
  4. For robustness, sample 1000 images per dataset; run APGD-CE and APGD-DLR (targeted) attacks, 100 iterations each, at ε ∈ {2/255, 4/255}.
  5. Evaluate at original resolution for CIFAR10/CIFAR100/STL-10; at 224×224 for all others.
  6. For PCAM (binary), use only APGD-CE.
  7. Report per-dataset and average clean/robust accuracy (average excludes ImageNet).
- **Metrics**: Top-1 accuracy (%)
- **Expected outcome**:
  - TeCoA should perform best on ImageNet clean and robust (supervised on ImageNet)
  - On other datasets: CLIP should have best clean, TeCoA should drop significantly, FARE should maintain close to CLIP clean performance
  - FARE4 should outperform TeCoA models on adversarial accuracy across non-ImageNet datasets
  - CLIP should achieve near-zero robustness at both radii on all datasets
- **Baselines**: CLIP (original), TeCoA2, TeCoA4
- **Dependencies**: none

## E04: Hallucination and Chain-of-Thought Evaluation
- **Verifies**: C05, C06
- **Setup**:
  - Model: LLaVA-1.5 7B with five vision encoders
  - Hardware: Not specified in paper
  - Dataset: POPE benchmark (Li et al., 2023b) — COCO validation set, three splits: random, popular, adversarial; SQA-I — 10k image/question pairs from Science QA (Lu et al., 2022)
  - System: Clean evaluation only (no adversarial perturbations)
- **Procedure**:
  1. POPE: For each split (random, popular, adversarial), query LLaVA with binary "Is there a [object] in the image?" questions; record Yes/No predictions; compute F1-score vs ground truth.
  2. SQA-I: Provide explanation + question + image to LLaVA; record predicted answer; compute accuracy vs ground truth.
  3. Report per-split POPE F1 and mean F1; report SQA-I accuracy for each encoder.
- **Metrics**: POPE: F1-score per split + mean; SQA-I: accuracy (%)
- **Expected outcome**:
  - Original CLIP should achieve highest POPE F1 and SQA-I accuracy
  - FARE should be closest to CLIP among robust encoders
  - TeCoA should show the largest degradation in hallucination and reasoning
  - FARE models should outperform TeCoA counterparts by a clear margin
- **Baselines**: CLIP (original), TeCoA2, TeCoA4
- **Dependencies**: none

## E05: Jailbreaking Attack Evaluation
- **Verifies**: C01 (extended to jailbreak domain)
- **Setup**:
  - Model: LLaVA-1.5 7B with CLIP, TeCoA4, FARE4 vision encoders
  - Hardware: Not specified in paper
  - Dataset: Single image per attack; 40 harmful prompts from Qi et al. (2023) across categories: identity, disinfo, crime, x-risk
  - System: Attack from Qi et al. (2023): 5,000 iterations, α = 1/255; ε ∈ {0, 16/255, 32/255, 64/255}
- **Procedure**:
  1. Craft adversarial image using Qi et al. (2023) attack against LLaVA with each encoder at ε ∈ {16/255, 32/255, 64/255}.
  2. Query each attacked model with 40 harmful prompts from 4 categories.
  3. Record number of successful harmful outputs per category.
  4. Report per-category and total success counts in format matching Table 7.
- **Metrics**: Count of successful jailbreaks per category (identity 11 prompts, disinfo 13, crime 13, x-risk 3; total 40)
- **Expected outcome**:
  - Both FARE4 and TeCoA4 should significantly reduce jailbreaking success compared to CLIP
  - FARE4 and TeCoA4 should perform comparably across all epsilon values
  - Robust encoders should remain effective even at radii much larger than training epsilon
- **Baselines**: CLIP (original), TeCoA4
- **Dependencies**: none

## E06: Embedding Loss Analysis
- **Verifies**: C02
- **Setup**:
  - Model: All five CLIP vision encoders (ViT-L/14): CLIP, TeCoA2, FARE2, TeCoA4, FARE4
  - Hardware: Not specified in paper
  - Dataset: 500 images from ImageNet validation set
  - System: 100-step APGD at ε = 4/255 for adversarial embedding loss
- **Procedure**:
  1. For each fine-tuned encoder φ_FT, compute clean embedding loss: L_clean(x) = ||φ_FT(x) - φ_Org(x)||²₂ on 500 ImageNet validation images.
  2. Compute adversarial embedding loss: L_adv(x) = max_{||z-x||∞ ≤ 4/255} ||φ_FT(z) - φ_Org(x)||²₂ using 100-step APGD on the same 500 images.
  3. Report mean L_clean and mean L_adv for each encoder.
- **Metrics**: Mean clean embedding loss E[L_clean(x)]; Mean adversarial embedding loss E[L_adv(x)]
- **Expected outcome**:
  - FARE models should have dramatically lower L_clean than TeCoA models
  - FARE models should have lower L_adv than TeCoA models
  - Original CLIP should have near-zero L_clean but very high L_adv
  - FARE4 should have higher L_clean than FARE2 but lower L_adv
- **Baselines**: CLIP (original, L_clean = 0 by definition)
- **Dependencies**: none
