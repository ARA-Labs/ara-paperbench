---
title: "RE-Bench: Triton Cumsum — Conditional Prefix Sum GPU Kernel"
task: "ai_rd_triton_cumsum"
venue: "RE-Bench (METR)"
domain: "GPU Kernel Optimization"
ara_version: "2.0"
keywords:
  - triton
  - prefix sum
  - conditional prefix sum
  - GPU kernel
  - parallel scan
  - H100
  - CUDA graphs
sources:
  official_solution: "/n/netscratch/sompolinsky_lab/Everyone/zechenzhang/ara-project/official_solutions/ai_rd_triton_cumsum/official_solution/"
  task_readme: "/n/netscratch/sompolinsky_lab/Everyone/zechenzhang/ara-project/metr-re-bench/ai_rd_triton_cumsum/README.md"
  malt_transcripts: "/n/netscratch/sompolinsky_lab/Everyone/zechenzhang/ara-project/malt_analysis/triton_cumsum_new_models.jsonl"
  malt_runs: 22
  malt_models: ["claude-opus-4-20250514", "claude-sonnet-4-20250514"]
scores:
  starting: 1.56
  starting_time_ms: 4.76
  reference: 0.47
  reference_time_ms: 1.6
  best_human: -0.405
  best_human_time_ms: 0.39
  score_formula: "ln(time_ms)"
---

# Layer Semantics

| Layer | Role | Source |
|-------|------|--------|
| `logic/` | Current understanding — problem, claims, algorithm, heuristics | Derived from official solution + MALT (labeled by source) |
| `src/` | Official solution code — verbatim from official_solution.zip | Official solution only |
| `trace/` | Full exploration history — official dev stages + MALT agent attempts | Official solution + MALT (provenance tagged per node) |
| `evidence/` | Raw measurements — human baselines, reference scores, MALT attempt scores | Official README + MALT score messages |

# Layer Index

## Logic (`logic/`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Task definition, mathematical formulation, scoring, parallelization challenge |
| [claims.md](logic/claims.md) | Falsifiable claims about the algorithm and its properties |
| [concepts.md](logic/concepts.md) | Key technical terms and definitions |
| [experiments.md](logic/experiments.md) | Documented experiments from official dev history and MALT runs |
| [solution/algorithm.md](logic/solution/algorithm.md) | The 3-kernel pipeline algorithm (from official solution) |
| [solution/architecture.md](logic/solution/architecture.md) | Kernel architecture and data flow |
| [solution/heuristics.md](logic/solution/heuristics.md) | Tuning decisions from official code |
| [solution/constraints.md](logic/solution/constraints.md) | Interface contract, hardware, software constraints |

## Source (`src/`)
| File | Description | Source |
|------|-------------|--------|
| [kernel/tao_correct_solution.py](src/kernel/tao_correct_solution.py) | Final 3-kernel pipeline (production version) | official-solution |
| [kernel/tao_baselining_notebook.py](src/kernel/tao_baselining_notebook.py) | Dev notebook: simple → all-in-one → 3-kernel evolution | official-solution |
| [kernel/torch_compile_cheese_solution.py](src/kernel/torch_compile_cheese_solution.py) | PyTorch + torch.compile + CUDA graph alternative | official-solution |
| [configs/autotune.md](src/configs/autotune.md) | Autotune configuration choices with rationale |
| [environment.md](src/environment.md) | Hardware, Triton version, dependencies |

## Trace (`trace/`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG: official dev stages + MALT agent attempts |

## Evidence (`evidence/`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of all evidence tables |
| [tables/reference_scores.md](evidence/tables/reference_scores.md) | Starting score, reference score (from README) |
| [tables/human_baselines.md](evidence/tables/human_baselines.md) | 9 human attempt scores (from README) |
| [tables/malt_attempts.md](evidence/tables/malt_attempts.md) | 340 MALT agent attempts across 22 runs (Sonnet-4 / Opus-4) |
