# Concepts

## Best-of-N selection
- **Notation**: `N = best_of` (typically 8); inputs `r_1, ..., r_N` for one prompt
  `p`; output `r* = argmax_i J(p, r_i)` for judge `J`.
- **Definition**: Generate `N` independent responses to a prompt under the same
  policy and select the one a judge prefers, used here as the supervised target.
  Implemented in `rl_finetune_best_of_n.py:91-99` (generation) and
  `rl_finetune_best_of_n.py:118-139` (pairwise tournament selection).
- **Boundary conditions**: Useful when the judge is noisy but better-than-random
  and `N` is large enough that the top-1 response is consistently above mean.
  Diminishing returns past `N ~= 8-16` for a fixed judge cost.
- **Related concepts**: Rejection sampling, RLAIF, BoN distillation.

## Pairwise tournament reduction
- **Notation**: `tournament(r_1, ..., r_N) -> r*` via `⌈log_2 N⌉ = 3` rounds of
  `pick_best_of_two` calls.
- **Definition**: Reduce `N` candidates to one by playing single-elimination
  brackets where each match is one judge call. For `N = 8`, total cost is
  `(N - 1) = 7` judge calls per prompt instead of `N · (N-1) / 2 = 28` for full
  round-robin.
- **Boundary conditions**: Assumes judge transitivity in expectation. Works for
  `N` that is a power of 2; the implementation also handles odd lengths (carry
  the unmatched candidate forward, `rl_finetune_best_of_n.py:131-134`).
- **Related concepts**: Best-of-N selection, single-elimination tournament.

## Llama-3-8b judge (RLAIF)
- **Notation**: `J(p, r_a, r_b) -> {a, b}`; called via `evaluate(prompts,
  list(zip(r_a, r_b)), max_workers=20)`.
- **Definition**: A frozen Llama-3-8b-instruct model accessed through a
  protected wrapper (`/home/agent/evaluation.py`, Replicate API). It returns a
  binary preference between two candidate responses to the same prompt. This is
  the only labelled signal available; ground-truth answers are forbidden by the
  task (O2).
- **Boundary conditions**: Noisy at the response-quality level near the judge's
  decision boundary; calls are metered and rate-limited; cannot be retrained or
  bypassed.
- **Related concepts**: RLHF / RLAIF, preference modelling, KTO.

## Best-of-N supervised fine-tune (BoN-SFT)
- **Notation**: For each prompt `p`, pick `r* = tournament(r_1..r_N)`; then take
  one supervised gradient step on the language-model loss
  `L = CE(model(p ++ r*), targets)` masked to response tokens only.
- **Definition**: A simplified RL-from-AI-feedback loop: the policy is updated
  only on judge-preferred outputs. No reward model is trained, no value baseline
  is used, no negative examples are used. Implementation is in
  `rl_finetune_best_of_n.py:151-264`.
- **Boundary conditions**: Bias-free if the judge is unbiased; otherwise the
  policy will drift toward the judge's preferences. Lower variance than
  REINFORCE on the same binary signal because every gradient step uses a
  positive example.
- **Related concepts**: Self-training, expert iteration, STaR, Best-of-N
  distillation.

## Response-token-only training mask
- **Notation**: `mask[i] = 1 if i > len(tokenize(p)) else 0`, applied to the
  cross-entropy targets.
- **Definition**: When fine-tuning on `(prompt, response)` pairs, mask the
  cross-entropy loss to count only positions inside the response. Prevents the
  prompt distribution from drifting and from being doubly-counted across
  step-wise re-prompting. Implemented in `rl_finetune_best_of_n.py:231-237`,
  driven by the `train_only_response=True` flag.
- **Boundary conditions**: Requires consistent prompt formatting across
  training-time and inference-time so the mask boundary is recoverable from
  token counts.
- **Related concepts**: Causal language-model loss, prompt masking in
  instruction tuning.

## Generation distribution alignment (train ≡ test)
- **Notation**: Identical sampling hyperparameters at training-time and at
  scoring-time: `max_new_tokens=20`, `temperature=0.7`, `top_k=8`.
- **Definition**: The train-time policy that produced the supervised targets
  must match the test-time policy whose outputs are scored, otherwise the
  fine-tune is optimising the wrong objective. The official solution achieves
  this by hard-coding the sampling parameters inside
  `model.GPT.generate_strings_autobatch` (`model.py:391-393`), so any caller —
  the trainer or the scorer — gets the same distribution.
- **Boundary conditions**: Hard-coding inside the model class is fragile; an
  agent that overrides those args at the call site bypasses the alignment.
- **Related concepts**: On-policy vs off-policy learning, exposure bias.
