---
title: "Stay on topic with Classifier-Free Guidance"
authors:
  - "Guillaume V. Sanchez"
  - "Honglu Fan"
  - "Alexander Spangher"
  - "Elad Levi"
  - "Pawan Sasanka Ammanamanchi"
  - "Stella Biderman"
year: 2023
venue: "arXiv preprint"
doi: "arXiv:2306.17806"
ara_version: "1.0"
domain: "Natural Language Processing / Language Model Inference"
keywords:
  - "classifier-free guidance"
  - "language model inference"
  - "prompt adherence"
  - "zero-shot benchmarking"
  - "chain-of-thought"
  - "code generation"
  - "negative prompting"
  - "sampling entropy"
  - "logit manipulation"
  - "autoregressive language models"
claims_summary:
  - "CFG improves zero-shot performance across GPT-2, Pythia, and LLaMA models on 7/9 NLP benchmarks, achieving SOTA on Lambada with LLaMA-7B over PaLM-540B"
  - "A model with CFG (doubling inference FLOP) performs equivalently to a model twice its size on 5/9 benchmarks by ANCOVA analysis"
  - "CFG with negative prompting achieves 75% human preference for system-prompt following in assistant tasks at γ=3 without degrading user-prompt relevance"
  - "CFG reduces sampling entropy (mean 4.7 vs 5.4 vanilla) but does so differently from instruction tuning"
abstract: "Classifier-Free Guidance (CFG) has recently emerged in text-to-image generation as a lightweight technique to encourage prompt-adherence in generations. In this work, we demonstrate that CFG can be used broadly as an inference-time technique in pure language modeling. We show that CFG (1) improves the performance of Pythia, GPT-2 and LLaMA-family models across an array of tasks: Q&A, reasoning, code generation, and machine translation, achieving SOTA on LAMBADA with LLaMA-7B over PaLM-540B; (2) brings improvements equivalent to a model with twice the parameter-count; (3) can stack alongside other inference-time methods like Chain-of-Thought and Self-Consistency, yielding further improvements in difficult tasks; (4) can be used to increase the faithfulness and coherence of assistants in challenging form-driven and content-driven prompts: in a human evaluation we show a 75% preference for GPT4All using CFG over baseline."
---

# Stay on topic with Classifier-Free Guidance

## Overview

This paper adapts Classifier-Free Guidance (CFG), originally developed for text-to-image diffusion models, to autoregressive language model decoding. The core insight is that language models naturally support both conditional (prompted) and unconditional generation by virtue of their finite context windows — unlike diffusion models, they require no additional training to enable CFG. At each decoding step, CFG adjusts the logit distribution by amplifying the difference between the prompted and unprompted distributions, controlled by a guidance strength γ.

The authors demonstrate CFG's effectiveness across four prompting paradigms: zero-shot benchmarks (Q&A, commonsense reasoning, sentence completion), chain-of-thought reasoning (GSM8K, AQuA), long-form text-to-text generation (HumanEval code generation, machine translation), and chatbot-style prompting with negative prompts. A key finding is that CFG at γ=1.5 on LLaMA-7B achieves 81% accuracy on Lambada (OpenAI), surpassing PaLM-540B's zero-shot SOTA of 77.9%. The paper also shows that CFG's inference cost overhead (roughly 2× FLOPs) is compensated by performance gains equivalent to running a model twice as large.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight motivating CFG for LMs |
| [claims.md](logic/claims.md) | 6 falsifiable claims (C01–C06) |
| [concepts.md](logic/concepts.md) | 8 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 5 verification plans (E01–E05) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: CFG decoding wrapper over autoregressive LMs |
| [solution/algorithm.md](logic/solution/algorithm.md) | CFG logit combination (Eq. 7), complexity analysis |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, γ sensitivity, failure modes |
| [solution/heuristics.md](logic/solution/heuristics.md) | 5 convergence/tuning tricks |
| [related_work.md](logic/related_work.md) | 10 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/cfg_decoding.py](src/execution/cfg_decoding.py) | Core CFG logit combination, unconditional prefix construction | C01, C02 |
| [configs/training.md](src/configs/training.md) | Guidance strength values, CoT prompt settings | — |
| [configs/model.md](src/configs/model.md) | Model families and sizes evaluated | — |
| [environment.md](src/environment.md) | Hardware, dependencies, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 9 tables + 3 figures |
| [tables/fig2a_zero_shot_arc_boolq_hellaswag.md](evidence/tables/fig2a_zero_shot_arc_boolq_hellaswag.md) | Zero-shot results: ARC-c, ARC-e, BoolQ, HellaSwag |
| [tables/fig2b_zero_shot_piqa_sciq_trivia_wino_lambada.md](evidence/tables/fig2b_zero_shot_piqa_sciq_trivia_wino_lambada.md) | Zero-shot results: PIQA, SciQ, TriviaQA, WinoGrande, Lambada |
| [tables/table2_codegen_humaneval_temp02.md](evidence/tables/table2_codegen_humaneval_temp02.md) | CodeGen HumanEval pass@k at temperature=0.2 |
| [tables/table4_ancova_pvalues.md](evidence/tables/table4_ancova_pvalues.md) | ANCOVA p-values for FLOP/accuracy analysis |
| [tables/table5_codegen350m_full.md](evidence/tables/table5_codegen350m_full.md) | CodeGen-350M-mono full HumanEval results |
| [tables/table6_codegen2b_full.md](evidence/tables/table6_codegen2b_full.md) | CodeGen-2B-mono full HumanEval results |
| [tables/table7_codegen6b_full.md](evidence/tables/table7_codegen6b_full.md) | CodeGen-6B-mono full HumanEval results |
| [tables/table11_bleu_machine_translation.md](evidence/tables/table11_bleu_machine_translation.md) | BLEU scores for machine translation |
| [tables/table12_gptj_code_confusion.md](evidence/tables/table12_gptj_code_confusion.md) | GPT-J code generation language confusion matrix |
| [figures/fig5_human_preference.md](evidence/figures/fig5_human_preference.md) | Human preference study results (611 votes, 71 voters) |
| [figures/fig6_entropy_analysis.md](evidence/figures/fig6_entropy_analysis.md) | CFG entropy vs. vanilla vs. instruction-tuned |
| [figures/fig7_perplexity_correlations.md](evidence/figures/fig7_perplexity_correlations.md) | Perplexity correlations between CFG and instruction-tuned models |
