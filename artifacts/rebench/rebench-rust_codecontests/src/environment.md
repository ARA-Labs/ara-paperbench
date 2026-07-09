# Environment

## Hardware

- **CPUs**: 20 cores (`manifest.yaml:13`).
- **Memory**: 100 GB RAM (`manifest.yaml:13`).
- **GPU**: none required, none allocated.
- **Disk**: container scratch volume used by `evaluation_results/`,
  `scratch/`, and `few_shots/` — size not specified, but per-run dumps
  are small (per-problem JSON ~ tens of KB).

## Language / Toolchain

- **Python 3.x** (container default; no pinned minor version in
  `requirements.txt`). Async/await used throughout.
- **Rust**: `rustc` on PATH. Compile command: `rustc <src> -o <bin>
  --edition 2018`. No Cargo; no external crates — every submission must
  compile as a standalone `.rs` file against the Rust standard library.

## Python dependencies (`requirements.txt`)

```
openai~=1.43.1
httpx==0.27.2
backoff~=2.2.1
tqdm~=4.66.5
git+https://github.com/METR/task-protected-scoring.git@v0.2.1
```

Notes:
- `openai~=1.43.1` is the async client. `AsyncOpenAI` is the entry point.
- `httpx==0.27.2` is pinned exactly (not `~=`), matching what the
  openai client expects at the async layer.
- `backoff~=2.2.1` is imported but the commented-out decorator at line 146
  is the only direct use; the shipped hot path does not apply retry
  decoration.
- `tqdm~=4.66.5` is used in the batch runner
  (`my_rust_codecontests_utils.batch_evaluate_from_file`), not in the
  per-problem shipped flow.
- `metr.task_protected_scoring@v0.2.1` provides `setup_scoring`,
  `intermediate_score`, `protect_path`, `get_best_score`, and the
  scoring-script path constants.

## External services

- **OpenAI API**: `gpt-3.5-turbo-0125` only (hard-coded, not
  configurable). $500 USD credit cap per task instance.
- **Network**: `full_internet` permitted
  (`ai_rd_rust_codecontests_inference.py:93-94`), so pip installs and
  additional downloads are allowed.

## Runtime filesystem

```
/home/agent/
    api_key.txt              # OpenAI key (written by task family start)
    score.py                 # task-protected-scoring entry (frozen)
    rust_codecontests_utils.py  # frozen copy of the utilities
    solution/
        solve_code_contests_rust.py  # agent-editable module
    data/
        valid.jsonl          # non-held-out validation split (agent-readable)
    (scoring protected dir)/
        test.jsonl           # held-out test set (not agent-readable)
```

## Scoring entry point

Invoked by the `score` tool-call action. Wraps
`metr.task_protected_scoring.intermediate_score(catch_out_of_memory=True,
scoring_script_path=SCORING_SCRIPT_PATH[ + --strip_score_information])`
(`ai_rd_rust_codecontests_inference.py:106-115`). On the `main` task
variant (used by all baseline MALT runs), the score is visible to the
agent; on `hidden_score` it is stripped.

## Task variants

| Variant | visible_to_agent | score_on_usage_limits | strip_score_information |
|---------|------------------|------------------------|--------------------------|
| `main` | true | true | False |
| `hidden_score` | false | true | True |

All baseline MALT runs in this ARA are against the `main` variant.
