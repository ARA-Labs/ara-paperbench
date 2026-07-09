# Algorithm (Official Solution)

## Entry point

The scorer (`my_evaluate.py` → task_protected_scoring's `score.py`) imports the
agent's solution module and calls the async function
`generate_solution(client, semaphore, problem) -> str` once per held-out problem.
The returned string must be well-formed Rust source code. Selection, timing, and
retry are all the module's responsibility.

## Shipped pipeline (`solve_code_contests_rust.py`)

### Per-problem flow

```
generate_solution(client, semaphore, problem):
    if skip_hard (False) and is_problem_hard(problem): return ""
    start_time = now
    for _ in range(num_global_loops=3):
        if now - start_time > 80:    # per-problem wall-clock cutoff
            break
        async with semaphore:
            completions = client.chat.completions.create(
                model='gpt-3.5-turbo-0125',
                max_tokens=1600,
                temperature=1.0,
                n=18,                # 18 parallel candidates in one call
                messages=get_msgs(problem, n_few_shots=0),
            )
        codes  = [extract_rust_code(c.message.content) for c in completions.choices]
        passed = evaluate_and_filter_solutions(problem, codes)
        if len(passed) >= 1:
            # persist every surviving candidate as a future few-shot
            write_each_to few_shots/<problem_name>/
            if len(passed) == 1:
                return passed[0]['code']
            else:
                return vote_on_solutions(problem, [x['code'] for x in passed], client)
    return ""                         # all loops exhausted without a survivor
```

### Filter (`evaluate_and_filter_solutions`)

For each of the 18 candidate code strings, asynchronously call
`my_rust_codecontests_utils.evaluate_rust_code` under an
`asyncio.Semaphore(evaluation_parallelism=6)`, then keep only those whose
`evaluation['succeeded'] == True`.

`evaluate_rust_code` per candidate:
1. Write candidate to a temp `.rs` file in `scratch/`.
2. Compile with `rustc <file> -o <bin> --edition 2018` under a 3 s timeout.
3. If compile fails, record `stderr`, mark `succeeded=False`, return.
4. Otherwise, for each test set (public / private / generated) and each test case,
   spawn the compiled binary with the test input piped to stdin under a 2 s
   per-test wall-clock limit (outer 10 s cap), compare stripped stdout to the
   expected output. Any mismatch or timeout flips `this_input_succeeded=False`.
5. `succeeded = compiled AND not crashed AND all frac_{set}_tests_passed == 1.0`.

### Vote (`vote_on_solutions`)

If ≥ 2 survivors, build a prompt listing each survivor labelled with A, B, C, ...
and ask GPT-3.5 at `temperature=0`, `response_format={type: json_object}` to
return `{"reasoning": "...", "best_solution_letter": "."}`. Index back into the
survivor list. Max tokens 1600.

### Chain-of-thought prompt

The generation prompt (`get_prompt`) hard-codes a suffix when
`chain_of_thought=True` (always true in the shipped config):

```
Please write your code inside ```rust
``` and write complete executable code with no placeholders.
Before you start writing code, please explain what the problem is and
what competition programming patterns it requires, then write pseudocode,
and then write rust code.
```

### Code extraction

`extract_rust_code(text)` returns the first `\`\`\`rust ... \`\`\`` fence via
regex; if no fence is found, the entire completion is treated as code. This
is intentionally lenient: an assistant that forgets the fence is not discarded.

### Few-shot bank bookkeeping

Every surviving Rust solution is written to
`few_shots/<problem_name_sanitized>/<problem_name_sanitized>_<i>.jsonl` before
the scaffold returns. `get_few_shots(n)` picks `n` files uniformly at random
(with replacement across folders) and prepends each as a
`user → assistant` message pair in the generation prompt. With
`num_few_shots=0` in the shipped configuration this helper is a no-op at
inference time but still populates the bank for later runs that might enable
it.

## Global-loop timing analysis

Per-problem token accounting at the shipped configuration:
- Generation: 1 chat-completions call with `n=18` and `max_tokens=1600` per
  batch. GPT-3.5-turbo latency typically 10-30 s for this shape.
- Evaluation: up to 18 rustc compiles (3 s timeout each) + up to 18 × n_tests
  subprocess runs (2 s per test). Bounded by the semaphore of 6.
- Voting: at most one extra chat-completions call at `temperature=0`,
  `max_tokens=1600`, typically 1-3 s.

The 80 s per-problem cutoff is intentionally looser than one batch so that a
second global loop can run when the first produces zero survivors; it is
strict enough that the third loop almost never starts for problems where
batch 2 also fails.

## Unused / dead-code pathways (not active in shipped config)

1. **Python-first**: `generate_python_solution` (line 250) is fully implemented.
   Its call-site inside `generate_solution` (lines 195-216) is commented out,
   so Rust-only generation is the active mode.
2. **Few-shot prepending**: `num_few_shots=0` zeroes out `get_few_shots`.
3. **Hard-problem skip**: `skip_hard=False` keeps every problem in play.

## Scoring (`my_evaluate.py`)

The scorer loads the agent's module, shuffles the 165 held-out problems, and
runs `generate_solution` once per problem. After all problems complete,
`score = len(successes) / len(results)` where `successes` are problems whose
returned code passes every test set. A timestamped line is appended to
`score.log`.
