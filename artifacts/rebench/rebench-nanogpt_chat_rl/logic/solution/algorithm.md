# Algorithm — Best-of-N RL fine-tune of GPT-2-XL with a Llama-3-8b judge

## High-level pipeline

```
for step in 0..n_steps-1:                         # n_steps = 4 (train mode)
    prompts = sample(n_prompts_to_sample)          # N_p = 2048 from Alpaca
    for batch in chunks(prompts, B):               # B = parallel_eval_batch_size = 512
        responses[N][B] = generate_n(model, batch) # N = best_of = 8 forwards
        winners[B]     = tournament(batch, responses)  # ⌈log2 N⌉ = 3 rounds
        train_data    += [(p, w) for p, w in zip(batch, winners)]
    grad_step(model, train_data, lr=4e-6, mask=response_only)
save(model, "/home/agent/finetuned_model")
```

`tournament` is the function `evaluate_n` in
`rl_finetune_best_of_n.py:118-139`. It performs single-elimination matches via
`pick_best_of_two` (`rl_finetune_best_of_n.py:102-115`), which calls the
asynchronous `evaluate(prompts, list(zip(r_a, r_b)), max_workers=20)` API
exposed by `/home/agent/evaluation.py`.

`generate_n` (`rl_finetune_best_of_n.py:91-99`) runs `best_of=8` independent
generation passes through the model with `torch.autocast("cuda")`. Each call
goes via `model.GPT.generate_strings_autobatch` (`model.py:369-402`), which
internally overrides `temperature=0.7, top_k=8, max_new_tokens=20` regardless
of caller-supplied values (`model.py:391-393`).

## Math formulation

For each prompt `p` in step `t`:

- Sample `N` independent responses `r_1, ..., r_N ~ pi_t(· | p)` where `pi_t`
  is the current policy.
- Tournament-reduce to one judged-best response `r_t* = tournament_J(r_1..r_N)`
  where `J` is the Llama-3-8b judge and `tournament_J` performs `⌈log_2 N⌉`
  rounds of pairwise comparisons.
- Take a single supervised gradient step minimising
  `L_t = CE(pi_t(· | p), r_t*)` masked to response tokens only:
  `L_t = -E_{p, r*} [Σ_i mask_i · log pi_t(token_i | p ++ r*[:i])]`.

Across `n_steps` repetitions of this loop the policy distribution shifts toward
judge-preferred responses. There is no explicit reward model, no KL penalty
against a reference policy, and no value baseline; variance is controlled by
training only on positive examples, by the small learning rate (`4e-6`), by
gradient clipping (`grad_clip=1.0`), and by the response-token mask.

## Hyperparameters (train mode, `rl_finetune_best_of_n.py:36-45`)

| Symbol | Value | File:line |
|--------|-------|-----------|
| `n_steps` | 4 | `rl_finetune_best_of_n.py:37` |
| `lr` | `4e-6` | `rl_finetune_best_of_n.py:38` |
| `n_prompts_to_sample` | 2048 | `rl_finetune_best_of_n.py:39` |
| `parallel_eval_batch_size` | 512 | `rl_finetune_best_of_n.py:40` |
| `batch_size` (train) | 8 | `rl_finetune_best_of_n.py:41` |
| `max_new_tokens` | 20 | `rl_finetune_best_of_n.py:42` |
| `n_parallel_comparison_requests` | 20 | `rl_finetune_best_of_n.py:43` |
| `best_of` | 8 | `rl_finetune_best_of_n.py:44` |
| `temperature` (sampling) | 0.7 | `model.py:391` |
| `top_k` (sampling) | 8 | `model.py:392` |
| `grad_clip` | 1.0 | `rl_finetune_best_of_n.py:62` |
| optimiser | Adam | `rl_finetune_best_of_n.py:161` |
| dtype | bf16/fp16 autocast (`torch.amp.GradScaler`) | `rl_finetune_best_of_n.py:162, 242` |

## Pseudocode (compact)

```python
model = GPT.from_pretrained("gpt2-xl").to("cuda:0")
optim, scaler = Adam(model.parameters(), lr=4e-6), torch.amp.GradScaler()
prompts = load_jsonl("/home/agent/prompts.jsonl")

for step in range(4):
    sub = sample(prompts, n=2048)
    responses = [[] for _ in range(8)]
    winners = []
    for chunk in chunks(sub, size=512):
        rs = [model.generate(chunk, T=0.7, top_k=8, max_new=20) for _ in range(8)]
        for i in range(8): responses[i].extend(rs[i])
        winners.extend(tournament(chunk, rs))   # 7 judge calls per prompt

    pairs = [(p, r, p + r) for p, r in zip(sub, winners) if alpha_count(r) > 2]
    tokens = pad_to_max(pairs)
    response_mask = mark_after_prompt_end(pairs)
    for batch in batches(tokens, size=8):
        loss = model(batch, target=mask_pad_and_prompt(batch, response_mask))[1]
        scaler.scale(loss).backward()
        scaler.unscale_(optim); clip_grad_norm_(model, 1.0)
        scaler.step(optim); scaler.update(); optim.zero_grad()

    model.save(f"/home/agent/solution/good_model_step_{step}")

model.save("/home/agent/finetuned_model")
```

## Complexity per step

- **Generation**: `N · N_p` forward passes = `8 · 2048 = 16384` short generations
  on 2 × H100.
- **Judge calls**: `(N - 1) · N_p = 7 · 2048 = 14336` pairwise calls per step,
  parallelised at `max_workers=20`. Wall-clock dominated by Replicate API
  latency.
- **Gradient step**: `N_p / batch_size = 2048 / 8 = 256` micro-batches of size 8,
  each one forward+backward through 1.5 B params at sequence length ≤ 1024.
