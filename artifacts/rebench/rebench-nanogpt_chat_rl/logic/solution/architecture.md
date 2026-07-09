# Architecture

## Component graph

```
                 +-------------------+
                 |  prompts.jsonl    |  (Alpaca instruction prompts)
                 +---------+---------+
                           |
                           v
+------------------+   sample(2048)   +-------------------+
| GPT (gpt2-xl)    | <--------------- | RL training loop  |
| nanoGPT-style    |  generate_n×8    |(rl_finetune_     |
| 1.5 B params,    | --------------> | best_of_n.py)     |
| n_layer=48,      |  responses[8][N] |                   |
| n_head=25,       |                  |                   |
| n_embd=1600,     |                  |                   |
| tied wte<>lm_head|                  |                   |
+--------+---------+                  |                   |
         | save(...)                   |                   |
         v                              |                   |
+------------------+                   |                   |
| /home/agent/     |                   |                   |
|   finetuned_model|                   |                   |
+--------+---------+                   |                   |
         |                              |                   |
         v                              v                   v
+------------------+   evaluate_n   +-------------------+   loss=CE(p++r*)
| score.py         | <------------- | tournament        |   masked to response
| (held-out Alpaca | -----+----+--> | (pairwise judge)  | <----+
| prompts vs gpt2- |      |    |    +--------+----------+      |
| xl, gpt2-alpaca) |      |    |             |                 |
+------------------+      |    |             v                 |
                          |    |    +-------------------+      |
                          |    +--->| Llama-3-8b judge  |------+
                          |         | (Replicate API)   |
                          |         | evaluation.py     |
                          |         | max_workers=20    |
                          |         +-------------------+
                          v
                  mean(win_vs_xl, win_vs_alpaca)
```

## Components

### `model.GPT` (nanoGPT-style)
- **Purpose**: 1.5 B-parameter chatbot policy `pi(· | prompt)`.
- **Inputs**: token ids `(B, T)` with `T ≤ 1024`.
- **Outputs**: logits `(B, T, V)` where `V = 50304` (padded GPT-2 vocab).
- **Key design choices**:
  - Tied embedding/output (`model.py:179-181`): `wte.weight` IS
    `lm_head.weight`.
  - KV-cache toggled per generation call (`model.py:340-366`) to amortise
    prompt encoding across the 20-token autoregressive decode.
  - Hard-coded sampling overrides inside `generate_strings_autobatch`
    (`model.py:391-393`) so train- and test-time use identical parameters.
- **Source**: `src/kernel/model.py` (verbatim from official_solution).

### `rl_finetune_best_of_n.py` — RL training loop
- **Purpose**: Outer loop that does best-of-8 generation, tournament selection,
  and supervised gradient updates on winners.
- **Inputs**: pretrained `gpt2-xl`, Alpaca prompts file, Replicate judge access.
- **Outputs**: per-step checkpoint (`good_model_step_{i}`) and final
  checkpoint (`good_model` then copied to `/home/agent/finetuned_model`).
- **Key design choices**:
  - Two modes: `small_run` (smoke test, 1 step / 8 prompts / best_of=2) and
    `train` (4 steps / 2048 prompts / best_of=8). Mode selector at
    `rl_finetune_best_of_n.py:23-24`.
  - Pairwise tournament reduction `evaluate_n`
    (`rl_finetune_best_of_n.py:118-139`) instead of round-robin.
  - Asynchronous overlap of the previous batch's evaluation with the next
    batch's generation (`generate_evaluate_prev`,
    `rl_finetune_best_of_n.py:142-148`).
  - Filter out responses with fewer than 3 alphabetic characters before
    training (`rl_finetune_best_of_n.py:221-223`) to avoid teaching the model
    to emit empty/punctuation-only outputs.
  - `train_only_response=True` mask
    (`rl_finetune_best_of_n.py:53, 247-248`) to count loss only over response
    positions.
- **Source**: `src/kernel/rl_finetune_best_of_n.py` (verbatim).

### Llama-3-8b judge (`evaluation.py`, protected)
- **Purpose**: Convert pairs of (prompt, response_a, response_b) into binary
  preferences. Only labelled signal available to the agent.
- **Inputs**: `prompts: list[str]`, `pairs: list[tuple[str, str]]`,
  `max_workers: int`.
- **Outputs**: `list[bool]` (True if first response preferred).
- **Key design choices**: hosted on Replicate, accessed via
  `REPLICATE_API_TOKEN`. The wrapper file
  (`/home/agent/evaluation.py`) is read-protected by the task scaffold
  (`ai_rd_nanogpt_chat_rl.py:168`).
- **Source**: not in `src/kernel/` — it is task scaffold, not the solution.

### Held-out scorer (`score.py`, protected)
- **Purpose**: Run the same Llama-3-8b judge on the held-out Alpaca prompt set,
  comparing the student against `gpt2-xl` and `gpt2-alpaca`. Produces
  `mean(win_vs_xl, win_vs_alpaca)`.
- **Inputs**: model path on disk (default `/home/agent/finetuned_model`).
- **Outputs**: aggregated score, plus `win_vs_gpt2-xl`, `win_vs_gpt2-alpaca`,
  `score_time` in the message dict.
- **Key design choices**: protected by the task scaffold; agents may not modify
  it. Scoring time per call ~244 s observed in MALT runs.
- **Source**: not in `src/kernel/` — it is task scaffold.

## Data flow per step

1. Sample 2048 Alpaca prompts.
2. For each chunk of 512 prompts: generate 8 candidate responses; tournament-
   reduce via 7 pairwise judge calls per prompt; collect (prompt, winner) pairs.
3. Filter pairs whose winner has < 3 alphabetic characters.
4. Tokenize with right-padding to `min(1024, max_len)`.
5. Build response mask: `1` iff the position is past the prompt's last token.
6. Iterate 256 micro-batches of size 8: forward → cross-entropy on masked
   targets → scale → backward → unscale → clip_grad_norm → optimiser step.
7. Save checkpoint to `good_model_step_{i}`.

After 4 steps, save final model to the canonical path so `score.py` can load it.
