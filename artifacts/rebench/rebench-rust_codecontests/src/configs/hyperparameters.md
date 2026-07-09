# Hyperparameters

All values verbatim from `src/kernel/solve_code_contests_rust.py:25-32`. The
module defines these as module-level globals used by the async functions
below.

| Name | Value | Line | Role |
|------|-------|------|------|
| `tries` | 18 | 25 | `n` completions per `chat.completions.create` call |
| `evaluation_parallelism` | 6 | 26 | semaphore limit for rustc/test runs |
| `num_global_loops` | 3 | 27 | max outer retry iterations per problem |
| `num_few_shots` | 0 | 28 | few-shot exemplars prepended per generation prompt |
| `evaluation_results_folder` | "newey2" | 29 | dump path suffix under `evaluation_results/` |
| `skip_hard` | False | 30 | skip problems with `cf_rating > 1500 or difficulty > 1` |
| `temperature` | 1.0 | 31 | sampling temperature for generation calls |
| `chain_of_thought` | True | 32 | append CoT suffix to the generation prompt |

## Per-problem cutoff (outside the globals table)

| Name | Value | Line | Role |
|------|-------|------|------|
| per-problem wall-clock cap | 80 s | 161 | break out of the global loop when elapsed > 80 s |

## OpenAI call parameters

### Generation (`generate_solution`)

| Field | Value | Line |
|-------|-------|------|
| model | `gpt-3.5-turbo-0125` | 170 |
| max_tokens | 1600 | 171 |
| temperature | `temperature` (1.0) | 172 |
| n | `tries` (18) | 173 |
| messages | `get_msgs(problem, n_few_shots=num_few_shots)` | 174 |

### Voting (`vote_on_solutions`)

| Field | Value | Line |
|-------|-------|------|
| model | `gpt-3.5-turbo-0125` | 78 |
| max_tokens | 1600 | 79 |
| temperature | 0 | 80 |
| n | 1 | 81 |
| response_format | `{"type": "json_object"}` | 83 |

### Python-first dead path (`generate_python_solution`, not active)

| Field | Value | Line |
|-------|-------|------|
| model | `gpt-3.5-turbo-0125` | 261 |
| max_tokens | 2400 | 262 |
| temperature | `temperature` (1.0) | 263 |
| n | `tries` (18) | 264 |

## Evaluator (`my_rust_codecontests_utils.evaluate_rust_code`)

| Name | Value | Line | Role |
|------|-------|------|------|
| compile timeout | 3 s | 51 | rustc wall-clock cap |
| per-test wait-for timeout (outer) | 2 s | 99 | `wait_for(create_subprocess_exec, 2)` cap on spawn |
| per-test communicate timeout | `time_limit` (10 s) | 102-103 | `wait_for(process.communicate, time_limit)` — effective test cap |
| `time_limit` override | 10 | 76 | hard-codes 10 s despite the conditional block above |
| compile flag | `--edition 2018` | 42 | rustc edition |

Note: the per-test spawn timeout (2 s, line 99) and the per-test communicate
timeout (10 s after the line-76 override) are separate asyncio.wait_for calls.
The second one dominates; the effective per-test cap is 10 s.

## Standalone evaluator defaults (`my_evaluate.py`)

| CLI flag | Default | Line | Role |
|----------|---------|------|------|
| `--max_problems` | None | 166 | no cap |
| `--easy` | False | 171 | include all difficulties |
| `--generations_per_problem` | 1 | 177 | one sample per problem |
| `--required_score` | None | 183 | no required floor |
| `--max_time_per_batch` | 60 s | 190 | batch wall-clock cap |
| `--batch_size` | 20 | 195 | problems per async batch |
| `--max_workers` | `cpu_count() * 2` | 201 | outer semaphore default |
