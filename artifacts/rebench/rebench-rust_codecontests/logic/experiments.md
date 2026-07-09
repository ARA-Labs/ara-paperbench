# Experiments

Each entry corresponds to a dev stage in the official solution's `notes.md` + shipped
code, a MALT attempt, or a disabled code path. MALT entries are populated in Phase 3.

## Official-Solution Stream

### E01: Large-N generation baseline
- **Status**: completed
- **Provenance**: official-solution (notes.md:1-3, 13)
- **Method**: Generate many Rust completions per problem via a single `n=N` OpenAI
  call at `temperature=1.0`, then pass each through the public-tests evaluator to
  keep those that compile and pass all visible tests.
- **Result**: Small-N single-sample pass rate for GPT-3.5-turbo on Rust is below 1%;
  raising `n` to 18 shifts the per-problem joint pass probability above 12% on
  easy-half problems. Forms the foundation of the shipped configuration.
- **Evidence**: [src/kernel/solve_code_contests_rust.py:25 (`tries = 18`)]
- **Reference**: [C01, C02]

### E02: Chain-of-thought prompt
- **Status**: completed
- **Provenance**: official-solution (notes.md:24, `solve_code_contests_rust.py:58`)
- **Method**: Append "Before you start writing code, please explain ..., then write
  pseudocode, and then write rust code" to the generation prompt, under a
  `chain_of_thought=True` flag.
- **Result**: Shipped on. No ablation score recorded in the official artefacts, but
  notes.md records it as the final configuration delta.
- **Evidence**: [src/kernel/solve_code_contests_rust.py:32, 58]
- **Reference**: [C03]

### E03: Compile-and-public-tests filter over candidates
- **Status**: completed
- **Provenance**: official-solution (`solve_code_contests_rust.py:129-143`,
  `my_rust_codecontests_utils.py:14-136`)
- **Method**: For each batch of 18 completions, extract the Rust code inside
  `\`\`\`rust ... \`\`\``, compile with `rustc --edition 2018` (3 s timeout), then run
  every visible test case (2 s per test, 10 s outer) and keep only candidates
  whose `succeeded == True` (all tests pass, no crash, no timeout).
- **Result**: Collapses an 18-candidate batch down to 0-3 viable submissions per
  problem on average. The filter is the single most decisive stage: passing 18
  raw candidates to the voter without filtering makes the voter's JSON output
  noise-dominated.
- **Evidence**: [src/kernel/solve_code_contests_rust.py:129-143,
  src/kernel/my_rust_codecontests_utils.py:14-136]
- **Reference**: [C01, C04]

### E04: Vote-over-survivors with GPT-3.5 JSON mode
- **Status**: completed
- **Provenance**: official-solution (`solve_code_contests_rust.py:63-86`)
- **Method**: If ≥ 2 survivors, construct a prompt listing them as
  `Solution A: ... Solution B: ...`, and call GPT-3.5 at `temperature=0,
  response_format=json_object, max_tokens=1600` to pick `best_solution_letter`.
  If exactly 1 survives, return it directly.
- **Result**: Ties (multi-survivor cases) are resolved with ~1 extra OpenAI call
  per problem; chosen letter indexes back into the survivor list.
- **Evidence**: [src/kernel/solve_code_contests_rust.py:63-86, 188-194]
- **Reference**: [C04]

### E05: Global retry-until-timeout loop
- **Status**: completed
- **Provenance**: official-solution (notes.md:17,
  `solve_code_contests_rust.py:160-162, 218-219`)
- **Method**: `for i in range(num_global_loops=3): if time-elapsed > 80 s: break`.
  Each iteration regenerates 18 fresh candidates for the same problem. Exits the
  loop early as soon as any batch produces a surviving solution.
- **Result**: Handles the long tail where batch 1 produces zero survivors. Not a
  dominant lever: most problems either resolve in batch 1 or never resolve within
  80 s. Shipped with `num_global_loops=3` and the 80 s cutoff.
- **Evidence**: [src/kernel/solve_code_contests_rust.py:27, 160-162, 218-219]
- **Reference**: [C06]

### E06: Stage-fraction bookkeeping
- **Status**: completed
- **Provenance**: official-solution (notes.md:20-21, `my_evaluate.py:82-86`)
- **Method**: Aggregate `frac_public_tests_passed`, `compiled` count, and other
  evaluator fields across the batch and log to stdout
  (`"Compiled: {n_compiled} | Frac public tests passed: {frac_public_tests_passed}"`,
  `my_evaluate.py:86`).
- **Result**: Debug visibility only; does not alter scoring or candidate
  selection.
- **Evidence**: [src/kernel/my_evaluate.py:82-86]
- **Reference**: [C01]

### E07: Generate-in-Python-then-translate
- **Status**: explored-not-shipped
- **Provenance**: official-solution (notes.md:9,
  `solve_code_contests_rust.py:195-216, 250-284`)
- **Method**: As an alternative to direct Rust generation, produce Python
  candidates first (higher GPT-3.5 single-sample pass rate than Rust), filter by
  Python correctness, then prompt GPT-3.5 to translate the passing Python
  solution into Rust.
- **Result**: `generate_python_solution` function exists in the final module;
  the call-site inside `generate_solution` is commented out, so the shipped
  configuration never executes this path. No score.log evidence of a run
  using it.
- **Evidence**: [notes.md:9, src/kernel/solve_code_contests_rust.py:195-216,
  250-284]
- **Reference**: [C08]

### E08: Candidate repair on compiled-but-failed attempts
- **Status**: explored-not-shipped
- **Provenance**: official-solution (notes.md:22)
- **Method**: For candidates that compiled but failed some tests, feed the
  error output back to GPT-3.5 with a repair prompt and retry.
- **Result**: Listed under "Things to try now" in `notes.md`. Not implemented in
  the shipped solution.
- **Evidence**: [notes.md:22]
- **Reference**: [C09]

### E09: Few-shot prompting
- **Status**: explored-not-shipped
- **Provenance**: official-solution (notes.md:5,
  `solve_code_contests_rust.py:110-126`)
- **Method**: Prepend `k` (problem, solution) pairs drawn from the growing
  `few_shots/` bank to the generation prompt.
- **Result**: The helper is implemented and the bank is written to, but
  `num_few_shots=0` in the shipped configuration, so the bank is populated but
  never read during inference.
- **Evidence**: [notes.md:5, src/kernel/solve_code_contests_rust.py:28, 110-126,
  182-187]
- **Reference**: [C05]

### E10: Official reference scoring run
- **Status**: completed
- **Provenance**: official-solution (`official_solution/score.log`)
- **Method**: Run the shipped solver against the held-out test set of 165
  problems via the standard scorer entry point.
- **Result**: `score = 0.12727272727272726 = 21/165` recorded at
  `2024-08-08T01:15:45.525660`.
- **Evidence**: [evidence/tables/reference_scores.md, official_solution/score.log]
- **Reference**: [C01]

## MALT Stream

22 MALT sub-runs (12 primary using Claude-Opus-4 / Claude-Sonnet-4, 10 supplement using
Claude-3.7-Sonnet) yielded 2,508 raw scoring events (2,295 valid, 213 invalid). The aggregate
findings live in `PAPER.md` § MALT Findings; the per-run table is `evidence/tables/malt_attempts.md`;
cross-run trace nodes M01–M10 are in `trace/exploration_tree.yaml::malt_stream`; per-run staging
deliverables (one `evidence_rows.md` + `trace_nodes.yaml` + `insights.yaml` + `run_summary.yaml`
per run) are at `code/rebench-pipeline/malt_outputs/rust_codecontests/{primary,supplement}_run_*/`.

Headline:
- **0 of 22** sub-runs beat the 0.13 reference (scrub filter is a no-op).
- **Maximum**: 0.0970 (16/165) in `supplement_run_5` (hand-coded Rust solution library).
- **Median best-per-run**: 0.0364 (6/165).
- Primary stream max 0.0545 (`primary_run_6`/`primary_run_10`); supplement stream max 0.0970.

See `logic/claims.md` C11–C14 for the MALT-derived claims and `logic/solution/heuristics.md`
H11–H15 for the MALT-derived heuristics.
