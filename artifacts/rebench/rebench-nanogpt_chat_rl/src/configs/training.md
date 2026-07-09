# Training Configuration (train mode)

All values verbatim from `src/kernel/rl_finetune_best_of_n.py:36-45` and
`src/kernel/model.py:391-393` — the official solution's `mode = "train"` path.

## RL outer loop

| Parameter | Value | File:line | Source |
|-----------|-------|-----------|--------|
| `n_steps` | 4 | `rl_finetune_best_of_n.py:37` | official-solution |
| `lr` | `4e-6` | `rl_finetune_best_of_n.py:38` | official-solution (`notes.md` line 1) |
| `n_prompts_to_sample` | 2048 | `rl_finetune_best_of_n.py:39` | official-solution (`notes.md` line 1) |
| `parallel_eval_batch_size` | 512 | `rl_finetune_best_of_n.py:40` | official-solution |
| `batch_size` (train micro-batch) | 8 | `rl_finetune_best_of_n.py:41` | official-solution |
| `best_of` | 8 | `rl_finetune_best_of_n.py:44` | official-solution (`notes.md` line 2) |
| `n_parallel_comparison_requests` | 20 | `rl_finetune_best_of_n.py:43` | official-solution |
| `train_only_response` | True | `rl_finetune_best_of_n.py:53` | official-solution |
| `grad_clip` | 1.0 | `rl_finetune_best_of_n.py:62` | official-solution |
| `optimiser` | `torch.optim.Adam` | `rl_finetune_best_of_n.py:161` | official-solution |
| `scaler` | `torch.amp.GradScaler` | `rl_finetune_best_of_n.py:162` | official-solution |
| `device` | `cuda:0` | `rl_finetune_best_of_n.py:21` | official-solution |
| `dtype` | autocast (`torch.autocast(device_type="cuda")`) | `rl_finetune_best_of_n.py:93, 242` | official-solution |
| `model_save_path` | `/home/agent/solution/good_model` | `rl_finetune_best_of_n.py:45` | official-solution |
| `prompts_path` | `/home/agent/prompts.jsonl` | `rl_finetune_best_of_n.py:54` | official-solution |
| `pad_token` | 50255 | `rl_finetune_best_of_n.py:67` | official-solution |
| `eot_token` | `enc.eot_token` (50256) | `rl_finetune_best_of_n.py:66, 75` | official-solution |
| `max_length` (per batch) | `min(1024, max(len(p) for p in texts))` | `rl_finetune_best_of_n.py:229` | official-solution |
| Response filter | `sum(c.isalpha()) > 2` | `rl_finetune_best_of_n.py:222` | official-solution |

## Sampling parameters (in-method overrides)

`GPT.generate_strings_autobatch` overrides any caller-supplied sampling args.

| Parameter | Value | File:line |
|-----------|-------|-----------|
| `temperature` | 0.7 | `model.py:391` |
| `top_k` | 8 | `model.py:392` |
| `max_new_tokens` | 20 | `model.py:393` |
| `min_length` | 3 | `model.py:332, 355-356` (default in `generate`) |

## Generation-side hyperparameters in `rl_finetune_best_of_n.generate_n`

These are passed at the call site but the in-method overrides above clamp
`top_k` to 8 regardless of the value sent here (the trainer happens to send
`top_k=10`, which is a no-op).

| Parameter | Value passed | File:line |
|-----------|-------------|-----------|
| `max_new_tokens` | 20 | `rl_finetune_best_of_n.py:96` |
| `batch_size` | 32 | `rl_finetune_best_of_n.py:96` |
| `temperature` | 0.7 | `rl_finetune_best_of_n.py:96` |
| `top_k` | 10 | `rl_finetune_best_of_n.py:96` (overridden to 8 by `model.py:392`) |

## Smoke-test mode (`small_run`)

`mode = "small_run"` (default in the shipped file, `rl_finetune_best_of_n.py:24`)
runs a 1-step smoke test with `n_prompts_to_sample=8`, `best_of=2`,
`parallel_eval_batch_size=8`. The agent must change `mode = "train"` to run the
real training pipeline.
