---
title: "Robust CLIP: Unsupervised Adversarial Fine-Tuning of Vision Embeddings for Robust Large Vision-Language Models"
authors: ["Christian Schlarmann", "Naman Deep Singh", "Francesco Croce", "Matthias Hein"]
year: 2024
venue: "ICML 2024 (Proceedings of the 41st International Conference on Machine Learning)"
doi: "arXiv:2402.12336v2"
ara_version: "1.0"
domain: "Adversarial Robustness, Vision-Language Models, CLIP"
keywords:
  - adversarial robustness
  - CLIP
  - vision-language models
  - adversarial fine-tuning
  - unsupervised training
  - FARE
  - LLaVA
  - OpenFlamingo
  - zero-shot classification
  - PGD
claims_summary:
  - "FARE (unsupervised adversarial fine-tuning) outperforms TeCoA (supervised) in both clean and robust performance across LVLM tasks"
  - "FARE-CLIP preserves original CLIP embeddings better than TeCoA, enabling drop-in replacement without LVLM retraining"
  - "FARE makes LVLMs robust against stealthy targeted ℓ∞ attacks while TeCoA introduces output quality degradation"
  - "FARE maintains superior zero-shot classification performance over TeCoA on non-ImageNet datasets"
  - "FARE reduces LLaVA hallucination rates and preserves chain-of-thought reasoning better than TeCoA"
abstract: "Multi-modal foundation models like OpenFlamingo, LLaVA, and GPT-4 are increasingly used for various real-world tasks. Prior work has shown that these models are highly vulnerable to adversarial attacks on the vision modality. These attacks can be leveraged to spread fake information or defraud users, and thus pose a significant risk, which makes the robustness of large multi-modal foundation models a pressing problem. The CLIP model, or one of its variants, is used as a frozen vision encoder in many large vision-language models (LVLMs), e.g. LLaVA and OpenFlamingo. We propose an unsupervised adversarial fine-tuning scheme to obtain a robust CLIP vision encoder, which yields robustness on all vision down-stream tasks (LVLMs, zero-shot classification) that rely on CLIP. In particular, we show that stealth-attacks on users of LVLMs by a malicious third party providing manipulated images are no longer possible once one replaces the original CLIP model with our robust one. No retraining or fine-tuning of the down-stream LVLMs is required. The code and robust models are available on GitHub."
---

# Robust CLIP: Unsupervised Adversarial Fine-Tuning of Vision Embeddings for Robust Large Vision-Language Models

## Overview

This paper introduces **FARE** (Fine-tuning for Adversarially Robust Embeddings), an unsupervised adversarial fine-tuning method for the CLIP vision encoder that achieves robustness across all downstream tasks relying on CLIP (zero-shot classification, LVLMs) without requiring labels or retraining of downstream models. The key insight is to minimize the ℓ₂ distance between adversarially-perturbed embeddings and the original clean embeddings, which simultaneously enforces adversarial robustness and preserves clean performance.

FARE is compared against TeCoA (the only prior robust CLIP method, which uses supervised adversarial fine-tuning on ImageNet). FARE consistently outperforms TeCoA on clean and robust performance for LVLMs (OpenFlamingo 9B, LLaVA-1.5 7B) across captioning and VQA tasks, while TeCoA suffers significant clean performance degradation outside ImageNet. Only 2 epochs of fine-tuning are required — about 0.2% of the original CLIP training cost.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight motivating FARE |
| [claims.md](logic/claims.md) | 7 falsifiable claims (C01–C07) |
| [concepts.md](logic/concepts.md) | 9 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 6 verification plans (E01–E06) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: FARE fine-tuning pipeline and downstream integration |
| [solution/algorithm.md](logic/solution/algorithm.md) | FARE loss, PGD inner maximization, TeCoA comparison, complexity |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and known limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | 6 convergence tricks and design choices |
| [related_work.md](logic/related_work.md) | 12 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/fare_training.py](src/execution/fare_training.py) | FARE fine-tuning loop with PGD inner maximization | C01, C02 |
| [execution/pgd_attack.py](src/execution/pgd_attack.py) | PGD/APGD attack implementation for ℓ∞ threat model | C03, C04 |
| [execution/tecoa_training.py](src/execution/tecoa_training.py) | TeCoA supervised adversarial fine-tuning baseline | C01 |
| [execution/zero_shot_eval.py](src/execution/zero_shot_eval.py) | Zero-shot classification evaluation with CLIP | C04 |
| [configs/training.md](src/configs/training.md) | AdamW, LR schedule, batch size, PGD steps, epochs |  — |
| [configs/model.md](src/configs/model.md) | ViT-L/14 CLIP encoder configuration | — |
| [environment.md](src/environment.md) | Hardware, dependencies, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 14-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 14 tables + quantitative figures |
| [tables/table1_lvlm_robustness.md](evidence/tables/table1_lvlm_robustness.md) | Clean/robust performance of OF-9B and LLaVA-1.5-7B across encoders |
| [tables/table2_transfer_attacks.md](evidence/tables/table2_transfer_attacks.md) | Transfer attack CIDEr scores across OF and LLaVA |
| [tables/table3_targeted_attacks.md](evidence/tables/table3_targeted_attacks.md) | Targeted attack success rates (out of 25) for all encoders |
| [tables/table4_zeroshot_classification.md](evidence/tables/table4_zeroshot_classification.md) | Zero-shot clean and adversarial accuracy on 14 datasets |
| [tables/table5_pope_hallucination.md](evidence/tables/table5_pope_hallucination.md) | POPE F1-score hallucination benchmark |
| [tables/table6_sqai.md](evidence/tables/table6_sqai.md) | SQA-I chain-of-thought reasoning accuracy |
| [tables/table7_jailbreak.md](evidence/tables/table7_jailbreak.md) | Jailbreaking attack success rates across categories and ε |
| [tables/table8_hparam_ablation.md](evidence/tables/table8_hparam_ablation.md) | LR/WD hyperparameter ablation for ViT-B/32 FARE |
| [tables/table9_loss_ablation.md](evidence/tables/table9_loss_ablation.md) | ℓ₁ vs ℓ₂ loss function ablation |
| [tables/table10_vitb_comparison.md](evidence/tables/table10_vitb_comparison.md) | ViT-B/32 comparison including Mao et al. TeCoA checkpoint |
| [tables/table11_attack_comparison.md](evidence/tables/table11_attack_comparison.md) | Ensemble attack vs. Schlarmann & Hein (2023) attack comparison |
| [tables/table12_targeted_500iter.md](evidence/tables/table12_targeted_500iter.md) | Targeted attacks with only 500 iterations |
| [tables/table13_llava13b.md](evidence/tables/table13_llava13b.md) | Clean LLaVA-13B evaluations |
| [tables/table14_embedding_loss.md](evidence/tables/table14_embedding_loss.md) | Clean and adversarial embedding loss evaluation |
