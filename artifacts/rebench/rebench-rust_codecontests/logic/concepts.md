# Concepts

## Filter-then-vote
The two-stage selection pattern used by the shipped scaffold: (i) generate `N=18`
candidate Rust solutions at temperature 1.0, (ii) filter them through a compile +
public-tests evaluator keeping only those whose `succeeded == True`, (iii) if ≥ 2
survive, call GPT-3.5 at temperature 0 to vote which single survivor to submit.
Used by `solve_code_contests_rust.py:129-143, 180-194`.

## Global retry loop
The outer retry controller: `for i in range(num_global_loops=3): ... if time > 80: break`.
A problem gets up to 3 independent batches of 18 candidates each, but total wall time
per problem is capped at 80 seconds. The loop exits early as soon as one candidate
passes the filter (`solve_code_contests_rust.py:160-194`).

## Compile-and-public-tests gate
The filter predicate used to decide whether a candidate is "viable". `evaluate_rust_code`
compiles the candidate with `rustc --edition 2018` (3 s timeout) and runs every public,
private, and generated test case up to a 2 s per-test timeout (outer 10 s cap).
`succeeded = compiled AND not crashed AND all frac_tests_passed == 1.0`
(`my_rust_codecontests_utils.py:127-131`). During generation time only the public tests
are visible; the scorer-time evaluator sees all three sets.

## Few-shot memory bank
`few_shots/<problem_name>/` is populated with every survivor the scaffold produces
during the run. The scaffold's own `get_few_shots(n)` helper draws `n` random past
survivors to prepend as `user/assistant` pairs before the target prompt. In the
shipped configuration `num_few_shots=0`, so the bank is populated but never read.
(`solve_code_contests_rust.py:28, 89-91, 110-126, 182-187`.)

## Chain-of-thought prompt
A suffix appended to the generation prompt:
"Before you start writing code, please explain what the problem is and what competition
programming patterns it requires, then write pseudocode, and then write rust code."
(`solve_code_contests_rust.py:58`.) Adds ~100-200 tokens per completion but raises
the per-sample success rate enough to justify the cost at `temperature=1.0`.

## Vote-with-JSON-mode
The selection call uses `response_format={"type": "json_object"}` to force the
vote-over-survivors output into a single JSON object with fields `reasoning` and
`best_solution_letter`. This makes the output machine-parsable without brittle
regex extraction. (`solve_code_contests_rust.py:76-86`.)

## Python-first path (dead code)
`generate_python_solution` + `get_python_translate_prompt` (lines 222-284): an
alternative pathway where the scaffold first generates candidates in Python,
filters them on correctness, then asks GPT-3.5 to translate the best Python
survivor into Rust. The call-site is commented out (lines 195-216). The notes
suggest this was tried and abandoned; no score.log trace corresponds to a
shipped run using it.

## Hard-problem short-circuit (disabled)
`is_problem_hard(problem) = problem["cf_rating"] > 1500 or problem["difficulty"] > 1`
(line 36). If `skip_hard=True`, `generate_solution` returns empty output immediately
for any hard problem, saving the token budget for easy problems. Shipped with
`skip_hard=False`.

## Repair loop (planned, not shipped)
`notes.md:22` lists "Try doing repair on attempts that compiled" as a future
direction. No corresponding implementation exists in `solve_code_contests_rust.py`;
the shipped solution drops non-succeeding candidates without any feedback-based
iteration on them.

## Held-out vs. validation split
The scorer operates against a held-out `test.jsonl` copied from `/root/test.jsonl`
into `scoring.PROTECTED_DIR` with read permissions restricted
(`ai_rd_rust_codecontests_inference.py:102-104`). A non-held-out validation split
lives in `data/valid.jsonl` that agents may query freely during development. Only
test-set runs count toward the final score (README:73-74).

## Invalid submission (import-time SyntaxError)
A distinct status in the score message: `{'status': 'invalidSubmission', 'score':
null, 'message': {'error': 'Failed to load solution module: SyntaxError(...)'}}`.
Emitted when `importlib.import_module` fails. Always a Python parser error on the
submitted module, never a Rust compile error (those are absorbed by the evaluator
and merely reduce the denominator-normalized score).
