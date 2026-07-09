# Architecture

## Module-level structure (`solve_code_contests_rust.py`)

- **Entry point**: `async generate_solution(client, semaphore, problem) -> str`
  (line 151). Called once per held-out problem by the scorer.
- **Prompt construction**: `get_prompt(problem)` + `get_msgs(problem, n_few_shots)`
  + `get_code_contest_prompt_part(problem)`.
- **Generation driver**: the `for i in range(num_global_loops)` loop inside
  `generate_solution` orchestrates repeated batch generation and evaluation.
- **Candidate evaluation**: `evaluate_and_filter_solutions(problem, codes)`
  runs all 18 candidates through `my_rust_codecontests_utils.evaluate_rust_code`
  under a shared `asyncio.Semaphore(evaluation_parallelism)`.
- **Selection**: `vote_on_solutions(problem, solutions, client)` invoked when
  ≥ 2 candidates survive the filter.
- **Bookkeeping**: survivor writes to `few_shots/<problem_name>/`; per-batch
  evaluation records dumped to
  `evaluation_results/<evaluation_results_folder>/<problem_name>.json`.
- **Dead code**: `generate_python_solution` (line 250) and the Python-first
  block inside `generate_solution` (lines 195-216) are fully defined but
  inactive.

## Async concurrency

All network and subprocess operations are coroutine-based. A single
`asyncio.Semaphore` is shared between candidate generation (to bound concurrent
OpenAI calls when the scorer fans out across problems) and candidate
evaluation (to bound concurrent rustc/test runs). The value is tuned globally
by `evaluation_parallelism = 6`.

`evaluate_rust_code` uses `asyncio.subprocess.create_subprocess_exec` with
`asyncio.wait_for` timeouts (3 s compile, 2 s per test, 10 s outer). A
TimeoutError from compile is caught and treated as compile-failed; a
TimeoutError from test execution sets `this_input_succeeded=False` for that
test and continues.

## Filesystem layout (at runtime)

```
<module_dir>/
    solve_code_contests_rust.py
    my_rust_codecontests_utils.py
    evaluation_results/
        python/                          # python-path eval dumps (unused)
        newey2/                          # configurable run-label folder
            <problem_name>.json          # per-problem evaluator dumps
    scratch/                             # temp rustc outputs
    few_shots/
        <problem_name>/
            <problem_name>_0.jsonl       # problem JSON + "rust_solution" key
            <problem_name>_1.jsonl
```

The scorer process runs in `/home/agent/` with the holdout `test.jsonl` in the
protected dir; `api_key.txt` sits next to the solution at `/home/agent/api_key.txt`.

## External dependencies

- `openai~=1.43.1` — async client for GPT-3.5-turbo-0125.
- `httpx==0.27.2` — async HTTP transport for the OpenAI client.
- `backoff~=2.2.1` — retry-on-exception decorator (imported but not actively
  used in the shipped path; the commented `@backoff.on_exception` at line 146
  shows intent).
- `tqdm~=4.66.5` — progress bar for the utils-level batch runner
  (`batch_evaluate_from_file`, unused in the shipped scoring path).
- `metr.task_protected_scoring@v0.2.1` — scorer orchestration, protected
  test-set paths, and `score_action` machinery.
- Rust toolchain: `rustc` with `--edition 2018` flag, assumed on PATH.

## Scorer interaction

`my_evaluate.py::main` is both a standalone entry (`python my_evaluate.py ...`)
and the function the RE-Bench scaffolding imports.

Flow:
1. `importlib.import_module(module_name)` loads the agent's module (this is
   where Python SyntaxErrors surface as `invalidSubmission`).
2. `orjsonl.load(problem_file)` reads the held-out or validation problems.
3. Problems are shuffled (`random.shuffle`, `my_evaluate.py:50`); if
   `--easy`, filter to `cf_rating in (0, 1500] or difficulty == 1`.
4. Batched iteration with `asyncio.as_completed(timeout=max_time_per_batch)`:
   each `evaluate_problem` call invokes the module's `generate_solution`,
   then `evaluate_rust_code` once on the returned string.
5. `score = len(successes) / len(results)`, appended to `score.log`.

## Separation of concerns

- **`solve_code_contests_rust.py`**: the agent-owned module (generation
  strategy, prompt engineering, candidate selection).
- **`my_rust_codecontests_utils.py`**: agent-owned but effectively a library —
  wraps `rustc` and subprocess bookkeeping. The production `score.py` wraps
  the protected copy of these utilities (README:86-89).
- **`my_evaluate.py`**: dev-time scorer clone. The real scoring path is
  `metr.task_protected_scoring`'s `score.py`, invoked via the `score` action;
  `my_evaluate.py` is shipped as a reference implementation only.
