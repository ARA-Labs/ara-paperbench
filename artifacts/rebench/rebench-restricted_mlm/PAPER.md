---
title: "RE-Bench: Restricted Architecture MLM — Masked Language Modelling on OpenWebText with a Restricted Primitive Set"
task: "ai_rd_restricted_mlm"
venue: "RE-Bench (METR)"
domain: "ML Engineering / Restricted-Primitive Architecture Design"
ara_version: "2.0"
keywords:
  - masked language modelling
  - restricted primitives
  - no division
  - no exponentiation
  - convolutional MLM
  - bigram prior
  - OpenWebText
sources:
  official_solution: "/n/netscratch/sompolinsky_lab/Everyone/zechenzhang/ara-project/official_solutions/ai_rd_restricted_mlm/official_solution/"
  task_readme: "/n/netscratch/sompolinsky_lab/Everyone/zechenzhang/ara-project/metr-re-bench/ai_rd_restricted_mlm/README.md"
  task_family: "/n/netscratch/sompolinsky_lab/Everyone/zechenzhang/ara-project/metr-re-bench/ai_rd_restricted_mlm/ai_rd_restricted_mlm.py"
  malt_transcripts: "/n/netscratch/sompolinsky_lab/Everyone/zechenzhang/ara-project/malt_analysis/restricted_mlm_new_models.jsonl"
  malt_runs: 22
  malt_models:
    - "claude-opus-4-20250514"
    - "claude-sonnet-4-20250514"
scores:
  starting: 1.81
  starting_loss: 7.636
  reference: 1.13
  reference_loss: 4.636
  best_human: 0.337541
  best_human_loss: 2.901
  score_formula: "log(loss - 1.5)"
  score_direction: "lower is better"
  select_best_fn: "min"
  hardware: "2x H100, 26 CPU, 200 GB RAM"
---

# Layer Semantics

| Layer | Role | Source |
|-------|------|--------|
| `logic/` | Current understanding — problem, claims, algorithm, heuristics | Derived from official solution + MALT (labeled by source) |
| `src/` | Official solution code — verbatim from official_solution/ | Official solution only |
| `trace/` | Full exploration history — official dev stages + MALT agent attempts | Official solution + MALT (provenance tagged per node) |
| `evidence/` | Raw measurements — human baselines, reference scores, MALT attempt scores | Official README + MALT score messages |

# Layer Index

## Logic (`logic/`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Task definition, scoring formula `log(loss-1.5)`, primitive restrictions, hardware |
| [claims.md](logic/claims.md) | Falsifiable claims about the architecture and its properties |
| [concepts.md](logic/concepts.md) | Key terms: bigram prior, convolutional MLM, inverse-stds normalisation, restricted primitives |
| [experiments.md](logic/experiments.md) | Documented experiments from official dev history and MALT runs |
| [solution/algorithm.md](logic/solution/algorithm.md) | The conv-with-bigrams architecture and training loop |
| [solution/architecture.md](logic/solution/architecture.md) | Module boundaries: 8-class model library, single shipped composite |
| [solution/heuristics.md](logic/solution/heuristics.md) | Tuning decisions (kernel=7, hidden=512, layers=6, exp=2, lr=3e-4 cosine, 100k steps) |
| [solution/constraints.md](logic/solution/constraints.md) | Forward-pass primitive restrictions, hardware, interface contract |

## Source (`src/`)
| File | Description | Source |
|------|-------------|--------|
| [kernel/tao_solution.py](src/kernel/tao_solution.py) | 8 model classes + `conv1d_same` helper; shipped class is `ConvMLMWithBiBigrams` | official-solution |
| [kernel/tao_train.py](src/kernel/tao_train.py) | Training loop instantiating `ConvMLMWithBiBigrams` (line 73) | official-solution |
| [kernel/measure_unigram_loss.py](src/kernel/measure_unigram_loss.py) | Computes & saves `unigrams.pt`, `bigrams_forward.pt`, `bigrams_backward.pt` | official-solution |
| [kernel/gpt2_approximation.py](src/kernel/gpt2_approximation.py) | Explored-not-shipped: minGPT with ReLU approximations of softmax/rsqrt/exp/gelu | official-solution |
| [kernel/notes.md](src/kernel/notes.md) | 21-line dev log: 6.1 → 7.58 → 5.75 → 5.25 → 4.6 | official-solution |
| [configs/hyperparameters.md](src/configs/hyperparameters.md) | Exact values from `tao_train.py:13-32` |
| [environment.md](src/environment.md) | torch 2.4.1, 2x H100, OpenWebText, gpt-2 tokenizer |

## Trace (`trace/`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG: official dev stages + MALT agent attempts |

## Evidence (`evidence/`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of all evidence tables |
| [tables/reference_scores.md](evidence/tables/reference_scores.md) | Starting score 1.81, reference 1.13, score formula log(loss-1.5) |
| [tables/human_baselines.md](evidence/tables/human_baselines.md) | 11 human attempt scores from README |
| [tables/malt_attempts.md](evidence/tables/malt_attempts.md) | MALT agent attempts: 22 sub-runs, per-run best score and aggregates |

# MALT Findings

**2 of 22 sub-runs beat reference 1.13** — both Claude-Opus-4: run_16 (1.0497) and run_01 (1.0864). A third (run_14) came within 0.09 (1.2218). All 11 Claude-Sonnet-4 runs failed (best 1.4352). Median best-of-run is **1.7561**, well above reference and far above the best-human 0.337.

| Stat | Opus-4 (n=11) | Sonnet-4 (n=11) | Both (n=22) |
|---|---|---|---|
| Best | **1.0497** | 1.4352 | **1.0497** |
| Median best | 1.3937 | 1.7978 | 1.7561 |
| Mean best | 1.4730 | 1.7199 | 1.5964 |
| Beat reference | **2** | 0 | **2** |
| Within 0.10 of reference | 3 | 0 | 3 |

**Headline pattern.** Both winning runs use the *same* recipe: `attn = ReLU(QK^T) @ V` (softmax replaced by ReLU since `exp` is forbidden), no LayerNorm, fixed scalar residual, then a long low-lr AdamW fine-tune (lr 2e-5–5e-5, ≥10k steps). Run_16 added a 3-seed ensemble at the end. **Neither winner used the official BiBigram prior**, and **0 of 22** MALT runs ever loaded `unigrams.pt` / `bigrams_*.pt` — the precomputed-statistics path that gives the official solution 0.55 loss-units of headroom (C06) is a blind spot across the entire MALT stream.

**Recurring failures.** Hand-rolled normalisations that emulate `1/x` (`gate_sum**−0.5`, `1/sum(weights)`, polynomial reciprocals) NaN at init in 7/22 runs (01, 06, 09, 11, 16, 19, 20); the cure is to substitute a fixed scalar or learned-scale residual. Long runs (300+ msgs) trim history, then verbatim-replay; only ~1 novel score appears post-trim (8/22 runs). The harness's 60s/300s bash timeout cripples large-step training in 6 runs; run_14 demonstrates a workaround (nohup + checkpoint-mtime polling) that no other run adopted. Three runs lost their best checkpoint to in-place overwrites and spent ≥1 attempt rescuing it.

**What this implies.** Under the restricted primitive set the architecture search space is small and unstable, and the *largest* available win — the precomputed bigram prior — sits outside the architectural-search frame the MALT agents adopt. The 2 wins that did happen show that long fine-tuning at small lr on a stable ReLU-attention skeleton is sufficient to clear reference; both winners were Opus-4, suggesting capability headroom is needed primarily to (a) survive the no-division/no-softmax debugging gauntlet and (b) commit to extended fine-tuning rather than continued architectural churn.

See `evidence/tables/malt_attempts.md` for the full per-run table and
`logic/claims.md::C11–C14`, `logic/solution/heuristics.md::H11–H15` for the
codified findings.
