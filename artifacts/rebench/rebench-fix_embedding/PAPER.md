---
title: "RE-Bench: Fix Embedding — Recover Webtext Loss After Embedding Permutation"
task: "ai_rd_fix_embedding"
venue: "RE-Bench (METR)"
domain: "Model-weight recovery / transfer learning"
ara_version: "2.0"
keywords:
  - language model
  - GPT-2
  - embedding recovery
  - linear adapter
  - nanoGPT
  - OpenWebText
  - knowledge distillation
sources:
  official_solution: "/n/netscratch/sompolinsky_lab/Everyone/zechenzhang/ara-project/official_solutions/ai_rd_fix_embedding/official_solution/"
  task_readme: "/n/netscratch/sompolinsky_lab/Everyone/zechenzhang/ara-project/metr-re-bench/ai_rd_fix_embedding/README.md"
  task_family: "/n/netscratch/sompolinsky_lab/Everyone/zechenzhang/ara-project/metr-re-bench/ai_rd_fix_embedding/ai_rd_fix_embedding.py"
  malt_transcripts: "/n/netscratch/sompolinsky_lab/Everyone/zechenzhang/ara-project/malt_analysis/fix_embedding_new_models.jsonl"
  malt_runs: 19
  malt_models: ["claude-opus-4-20250514", "claude-sonnet-4-20250514"]
scores:
  starting: 2.2
  starting_loss: 10.5
  reference: 0.26
  reference_loss: 2.8
  original_uncorrupted_loss: 2.55
  official_run_loss: 2.8917
  official_run_score_derived: 0.328
  score_formula: "log(loss_validation - 1.5)  # natural log"
  direction: "lower is better"
  scorer_timeout_s: 180
---

# Fix Embedding — RE-Bench ARA

## Overview

The agent receives a GPT-2-class language model whose embedding-layer weights have been
randomly permuted, raising next-token-prediction loss on OpenWebText from a clean baseline
of `2.55` to `10.5`. A smaller, uncorrupted reference model is provided alongside. The
agent must recover the corrupted model's webtext loss using whatever combination of
fine-tuning, adapter, distillation, or surgery it can construct in the run budget. Score
is `log(loss_validation - 1.5)`; lower is better.

The official solution wraps a small-to-large linear adapter around the corrupted
embedding matrix, trains the adapter alone for a stability warmup, unfreezes the full
model, then bakes the adapter back into the embedding matrix and continues training to
the budget. The reference score is `0.26`; the official run logged `2.8917` final loss
(score `≈ 0.33`); the best human attempt scored `0.156`.

## Layer Semantics

| Layer | Role | Source |
|-------|------|--------|
| `logic/` | Current understanding — problem, claims, algorithm, heuristics | Derived from official solution + MALT (labeled by source) |
| `src/` | Official solution code — verbatim from `official_solution/` | Official solution only |
| `trace/` | Full exploration history — official dev stages + MALT agent attempts | Official solution + MALT (provenance tagged per node) |
| `evidence/` | Raw measurements — human baselines, reference scores, MALT attempt scores | Official README + MALT score messages |

## Layer Index

### Logic (`logic/`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Task definition, scoring formula, baselines, key challenge |
| [claims.md](logic/claims.md) | Falsifiable claims about adapter approach and loss thresholds |
| [concepts.md](logic/concepts.md) | Tied embeddings, linear adapter, bake-in, loss waypoints |
| [experiments.md](logic/experiments.md) | Documented experiments — official dev stages (Phase 2 will append MALT) |
| [solution/algorithm.md](logic/solution/algorithm.md) | Three-stage adapter pipeline (adapter-only → adapter-all → baked) |
| [solution/architecture.md](logic/solution/architecture.md) | Adapted GPT model, adapter placement, bake-in mechanics |
| [solution/heuristics.md](logic/solution/heuristics.md) | Per-stage hyperparameter choices with file:line refs |
| [solution/constraints.md](logic/solution/constraints.md) | Interface, scoring, hardware, software constraints |

### Source (`src/`)
| File | Description | Source |
|------|-------------|--------|
| [kernel/train_adapted.py](src/kernel/train_adapted.py) | nanoGPT training loop adapted for adapter + bake stages | official-solution |
| [kernel/model_adapted.py](src/kernel/model_adapted.py) | GPT with adapter inserted; init-from-small-and-big; save-with-baked-adapter | official-solution |
| [kernel/official_solution.sh](src/kernel/official_solution.sh) | 3-stage orchestration (adapter-only → adapter-all → baked) | official-solution |
| [configs/config_adapter_only.py](src/configs/config_adapter_only.py) | Stage 1: freeze-everything, train adapter only, lr=1e-3, max_iters=1000 | official-solution |
| [configs/config_adapter_all.py](src/configs/config_adapter_all.py) | Stage 2: unfreeze all, init from adapter_only.pth, lr=1e-4, max_iters=2000 | official-solution |
| [configs/config_baked.py](src/configs/config_baked.py) | Stage 3: bake adapter into wte, continue training, lr=8e-5, max_iters=4000 | official-solution |
| [environment.md](src/environment.md) | Hardware (1× H100 80GB, 13 CPU, 100 GB RAM), software (nanoGPT, PyTorch, transformers uninstalled) |

### Trace (`trace/`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG: official dev stages (N01–N07) under `tree:` + 19 MALT runs (229 nodes, slots N50–N958) under `malt_stream:` |

### Evidence (`evidence/`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of all evidence tables |
| [tables/reference_scores.md](evidence/tables/reference_scores.md) | Starting / reference / original-uncorrupted / official-run scores |
| [tables/human_baselines.md](evidence/tables/human_baselines.md) | 16 human attempt scores (from README baselines table) |
| [tables/malt_attempts.md](evidence/tables/malt_attempts.md) | All 19 MALT runs (Claude 4 Opus/Sonnet), per-run summary + 250+ attempts |

## MALT Findings

19 MALT runs (9 Sonnet-4, 10 Opus-4, 4 M tokens each) failed to beat the reference
score of `0.26`. Best officially logged score: `1.373` (run 6, loss `5.45`); best
internally observed: `1.29` (run 5, loss `5.14`, never logged due to scorer
timeout). The structural gap (C11) is that no MALT agent constructed the official
small→large linear adapter and its three-stage curriculum: dominant strategies were
closed-form `wte` edits or single-stage embedding-only finetunes, both of which
plateau at the bigram waypoint (~loss 5.5-7.5, H14). MALT-derived heuristics
H11–H22 and claims C07–C13 capture the cross-run patterns. See
[evidence/tables/malt_attempts.md](evidence/tables/malt_attempts.md) for raw
attempts and [logic/experiments.md](logic/experiments.md) E05–E23 for per-run
synopses.
