---
title: "RE-Bench: Rust CodeContests Inference — GPT-3.5-turbo Scaffolding for Competitive Programming in Rust"
task: "ai_rd_rust_codecontests_inference"
venue: "RE-Bench (METR)"
domain: "LLM Inference Scaffolding / Code Generation"
ara_version: "2.0"
keywords:
  - GPT-3.5-turbo
  - competitive programming
  - Rust
  - inference scaffolding
  - self-consistency
  - filter-then-vote
  - chain of thought
sources:
  official_solution: "/n/netscratch/sompolinsky_lab/Everyone/zechenzhang/ara-project/official_solutions/ai_rd_rust_codecontests_inference/official_solution/"
  task_readme: "/n/netscratch/sompolinsky_lab/Everyone/zechenzhang/ara-project/metr-re-bench/ai_rd_rust_codecontests_inference/README.md"
  malt_transcripts_primary: "/n/netscratch/sompolinsky_lab/Everyone/zechenzhang/ara-project/malt_analysis/rust_codecontests_new_models.jsonl"
  malt_transcripts_supplement: "/n/netscratch/sompolinsky_lab/Everyone/zechenzhang/ara-project/malt_analysis/rust_codecontests_claude37_supplement.jsonl"
  malt_runs_primary: 12
  malt_runs_supplement: 10
  malt_models:
    - "claude-opus-4-20250514"
    - "claude-sonnet-4-20250514"
    - "claude-3-7-sonnet-20250219"
scores:
  starting: 0.00
  reference: 0.13
  best_human: 0.13
  score_formula: "n_successes / n_problems"
  held_out_problem_count: 165
  best_malt_observed_primary: 0.0545
  best_malt_observed_supplement: 0.0970
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
| [problem.md](logic/problem.md) | Task definition, scoring formula, held-out problem count, hardware/API budget |
| [claims.md](logic/claims.md) | Falsifiable claims about the scaffold and its properties |
| [concepts.md](logic/concepts.md) | Key terms: filter-then-vote, chain-of-thought, few-shot memory bank |
| [experiments.md](logic/experiments.md) | Documented experiments from official dev history and MALT runs |
| [solution/algorithm.md](logic/solution/algorithm.md) | The generate→filter→vote→retry-on-timeout pipeline |
| [solution/architecture.md](logic/solution/architecture.md) | Module boundaries and async concurrency structure |
| [solution/heuristics.md](logic/solution/heuristics.md) | Tuning decisions (N=18, parallelism=6, global_loops=3, 80s cutoff) |
| [solution/constraints.md](logic/solution/constraints.md) | API budget, Rust toolchain, interface contract |

## Source (`src/`)
| File | Description | Source |
|------|-------------|--------|
| [kernel/solve_code_contests_rust.py](src/kernel/solve_code_contests_rust.py) | Main solution: generate/filter/vote loop | official-solution |
| [kernel/my_evaluate.py](src/kernel/my_evaluate.py) | Off-scorer batch evaluator (formula at line 88) | official-solution |
| [kernel/my_rust_codecontests_utils.py](src/kernel/my_rust_codecontests_utils.py) | Rust/Python compile-and-run utilities | official-solution |
| [configs/hyperparameters.md](src/configs/hyperparameters.md) | Exact hyperparameter values from `solve_code_contests_rust.py:25-31` |
| [environment.md](src/environment.md) | Rust toolchain, OpenAI API, dependency versions |

## Trace (`trace/`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG: official dev stages + MALT agent attempts |

## Evidence (`evidence/`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of all evidence tables |
| [tables/reference_scores.md](evidence/tables/reference_scores.md) | Starting score, reference score, score.log reading |
| [tables/human_baselines.md](evidence/tables/human_baselines.md) | 14 human attempt scores (from README) |
| [tables/malt_attempts.md](evidence/tables/malt_attempts.md) | MALT agent attempts: 22 sub-runs, 2,508 raw scoring events, 0/22 beat reference |

# MALT Findings

22 MALT sub-runs were processed (12 primary using Claude-Opus-4 / Claude-Sonnet-4, 10 supplement using
Claude-3.7-Sonnet) yielding 2,508 raw scoring events. The supplement stream was added because the primary
stream's Opus-4/Sonnet-4 runs cluster heavily near the 0.03 ceiling and the larger event volume of the
slower-but-cheaper Sonnet-3.7 runs is needed to characterise the low-end behaviour space.

## Headline result
**0 of 22** sub-runs beat the 0.13 reference. The maximum observed test-set score was **0.0970** (16/165),
achieved by `supplement_run_5` via a hand-coded Rust solution library, ≈ 75% of reference. The median
best-per-run was **0.0364** (6/165), ≈ 28% of reference.

## Cross-stream aggregates

| stream | n_runs | total_events | invalid | max_best | median_best |
|---|---|---|---|---|---|
| primary (Opus-4 / Sonnet-4) | 12 | 339 | 11 | 0.0545 | 0.0303 |
| supplement (Sonnet-3.7) | 10 | 2,169 | 202 | 0.0970 | 0.0455 |

Frontier-coding-agent rebuilds approached but did not match the reference. Notably the Sonnet-3.7
supplement stream produced *higher* maxima than the Opus-4 / Sonnet-4 primary stream — the gap is
explained not by base-model capability but by Sonnet-3.7's tendency to spend more events on low-cost
exploration loops, which occasionally surface high-variance wins.

## Pattern aggregates (from per-run `insights.yaml`)

| pattern | runs | description |
|---|---|---|
| simple_beats_complex | 14/22 | Minimal scaffold (single template, low temperature) outperforms multi-strategy hybrids |
| context_trim_replay | 12/22 | MALT context truncation triggers deterministic re-derivation of earlier ladder, inflating event counts 3-7× without exploration |
| generator_ceiling | 11/22 | GPT-3.5-turbo Rust ceiling lies in 0.05–0.10 band regardless of scaffolding effort |
| scaffold_syntaxerror | 10/22 | Repeating Python `SyntaxError` cluster (f-string brace escaping, unescaped backslashes in Rust template literals) |
| no_filter_then_vote | 22/22 | **No** sub-run rediscovered the official compile-and-public-tests filter + JSON-mode vote pipeline |
| hand_coded_library | 2/22 | Highest-scoring approach (`supplement_run_5`, `primary_run_7`): bypass generator, hand-write Rust solutions for known templates |

## Key takeaways

1. **Filter-then-vote is structurally non-obvious.** Across 2,508 events spanning two model families, no
   agent rediscovered the official pipeline's compile-and-test filter on N=18 candidates with JSON-mode
   vote selection. Agents converge on prompt engineering instead of inference-time search.
2. **Hand-coded Rust libraries are the only MALT pathway approaching reference.** `supplement_run_5`
   achieved 0.0970 by abandoning generation and hand-writing Rust for recognised problem templates. This
   exposes a brittleness in the official benchmark: it rewards memorised solutions when the agent
   correctly recognises the public test set's distribution.
3. **Validation-test conflation hazard.** `primary_run_3` (Sonnet-4) reported 0.10 on a local 10-problem
   subset but scored 0/165 on all three official test-set submissions — a textbook small-sample noise
   trap that the official solution avoids by always scoring against the full held-out set.
4. **Context-truncation replay loops dominate event counts.** The MALT harness's truncation behaviour
   (every 80–150 messages) causes 12 of 18 long-running runs to re-derive their earlier scaffold ladder
   3-7 times, masking apparent "exploration" with structurally redundant events.

See `evidence/tables/malt_attempts.md` for the per-run table, `trace/exploration_tree.yaml::malt_stream`
(M01–M10) for the cross-run trace nodes, and `logic/solution/heuristics.md` (H11–H15) and
`logic/claims.md` (C11–C14) for the MALT-derived heuristics and claims.
