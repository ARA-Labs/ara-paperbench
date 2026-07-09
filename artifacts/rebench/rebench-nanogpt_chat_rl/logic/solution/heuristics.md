# Heuristics

## H01: Use best-of-8 with pairwise tournament selection
- **Rationale**: Best-of-8 selects from a 3-round single-elimination bracket, so
  the surviving response is in expectation well above the median; combined with
  a noisy judge, this gives a low-variance positive signal for supervised
  fine-tuning. The base solution used `best_of=2` (single judge call); the
  official delta is `best_of=8` per `notes.md` line 2.
- **Sensitivity**: high — this is the most structural change vs the base
  solution.
- **Bounds**: Useful range `4 ≤ N ≤ 16`. Each extra `N` adds one extra
  generation pass per prompt and `(N-1)` extra judge calls per prompt; past
  `N ~ 16` the judge-call budget dominates without commensurate quality gain.
- **Code ref**: `src/kernel/rl_finetune_best_of_n.py:44, 91-99, 118-139`.
- **Source**: official-solution (`notes.md` line 2).

## H02: Tournament selection beats round-robin and re-judging
- **Rationale**: For `N=8`, single-elimination uses `N-1 = 7` pairwise judge
  calls per prompt vs `N(N-1)/2 = 28` for full round-robin. With 2048 prompts
  per step the savings are `~43k` judge calls per step. The implementation
  parallelises matches within a round at `max_workers=20`, so wall time scales
  with `⌈log_2 N⌉ = 3` rounds, not `N - 1`.
- **Sensitivity**: high for judge-call budget; medium for wall time.
- **Bounds**: Assumes judge transitivity in expectation; mild violations
  average out over 2048 prompts. The implementation also supports odd-length
  brackets by carrying the unmatched candidate (`rl_finetune_best_of_n.py:131-134`).
- **Code ref**: `src/kernel/rl_finetune_best_of_n.py:118-139`.
- **Source**: official-solution.

## H03: Train at lr=4e-6 (10× smaller than typical SFT)
- **Rationale**: The student is initialised from a pretrained 1.5 B model, the
  supervised target is self-generated noisy text, and only 4 steps are taken
  in `train` mode. A small learning rate prevents catastrophic drift while
  still allowing the policy to specialise toward judge-preferred outputs.
  `notes.md` line 1 records this as a downward delta from the base solution's
  default LR.
- **Sensitivity**: high — too high causes the model to collapse to short or
  malformed outputs; too low yields no measurable improvement in 4 steps.
- **Bounds**: `1e-6 — 1e-5` plausible range; `4e-6` is the chosen point.
- **Code ref**: `src/kernel/rl_finetune_best_of_n.py:38`.
- **Source**: official-solution (`notes.md` line 1).

## H04: Sample 2048 prompts per step
- **Rationale**: With `best_of=8` and tournament selection, each prompt yields
  one judge-preferred training pair. 2048 prompts × 4 steps = 8192 unique
  supervised training pairs over the run, giving 256 micro-batches of size 8 per
  step. Larger samples improve gradient quality but inflate judge-call budget;
  this is the chosen point per `notes.md` line 1.
- **Sensitivity**: medium.
- **Bounds**: Must be divisible by `parallel_eval_batch_size=512`
  (`rl_finetune_best_of_n.py:49-52`).
- **Code ref**: `src/kernel/rl_finetune_best_of_n.py:39`.
- **Source**: official-solution (`notes.md` line 1).

## H05: Hard-code generation hyperparameters inside the model class
- **Rationale**: The scorer (`score.py`) and the trainer both go through
  `GPT.generate_strings_autobatch`. Hard-coding `temperature=0.7`, `top_k=8`,
  `max_new_tokens=20` inside the method body
  (`model.py:391-393`) ensures train- and test-time distributions are identical
  even if a caller passes different defaults (the trainer in fact passes
  `top_k=10` at the call site, which is overridden to `8` by the method body).
  This is the structural mechanism that realises `notes.md` line 4.
- **Sensitivity**: high — distribution mismatch between train and test would
  invalidate the entire supervised target.
- **Bounds**: applies as long as both code paths route through this method.
- **Code ref**: `src/kernel/model.py:391-393`,
  `src/kernel/rl_finetune_best_of_n.py:91-99`.
- **Source**: official-solution (`notes.md` line 4 + the implementation
  realising it).

## H06: Cap response length at 20 tokens
- **Rationale**: Short responses (a) reduce per-step generation latency, (b)
  reduce judge-call latency (Llama processes shorter sequences faster), (c)
  match the typical Alpaca answer length, and (d) give the judge a tighter
  decision surface (it is easier to rank short answers reliably than long ones).
- **Sensitivity**: high — increasing past 50-100 tokens disproportionately
  inflates wall time without improving win-rate, since the held-out scorer
  applies the same cap.
- **Bounds**: `10 — 30` plausible; chosen value 20.
- **Code ref**: `src/kernel/rl_finetune_best_of_n.py:42`,
  `src/kernel/model.py:393`.
- **Source**: official-solution (`notes.md` line 4).

## H07: Train only on response tokens, not prompt tokens
- **Rationale**: With `train_only_response=True` the cross-entropy loss is
  masked to positions strictly past the prompt's last token
  (`rl_finetune_best_of_n.py:231-237`). Prevents the prompt distribution
  from drifting and avoids a doubly-counted prompt loss when the same prompt
  appears across steps.
- **Sensitivity**: medium.
- **Bounds**: requires consistent prompt formatting so the mask boundary is
  recoverable from token counts.
- **Code ref**: `src/kernel/rl_finetune_best_of_n.py:53, 247-248`.
- **Source**: official-solution.

## H08: Filter out winners with fewer than 3 alphabetic characters before training
- **Rationale**: Empty or punctuation-only "winners" (which the noisy judge
  occasionally selects) would teach the model to emit degenerate outputs.
  Filter pre-batch via `sum(c.isalpha() for c in r) > 2`
  (`rl_finetune_best_of_n.py:221-223`).
- **Sensitivity**: medium — a few percent of winners are filtered per step;
  removing the filter risks mode collapse to short outputs after a few steps.
- **Bounds**: threshold `> 2` is the chosen value; `> 0` is too weak,
  `> 10` discards too many valid short answers.
- **Code ref**: `src/kernel/rl_finetune_best_of_n.py:221-223`.
- **Source**: official-solution.

## H09: Overlap evaluation of the previous batch with generation of the next
- **Rationale**: Judge calls have ~250 ms latency per pairwise call; generation
  of 8 × 512 short responses is GPU-bound. The official solution
  (`generate_evaluate_prev`, `rl_finetune_best_of_n.py:142-148`) runs the
  previous batch's tournament reduction concurrently with the next batch's
  generation so neither resource sits idle.
- **Sensitivity**: medium — saves ~30 % wall-clock per step in practice.
- **Bounds**: only applies when `parallel_eval_batch_size < n_prompts_to_sample`
  so there is more than one batch.
- **Code ref**: `src/kernel/rl_finetune_best_of_n.py:142-148, 192-200`.
- **Source**: official-solution.

## H10: Use Adam + GradScaler with grad_clip=1.0
- **Rationale**: Adam handles the loose statistics of short, noisy supervised
  targets better than SGD; `torch.amp.GradScaler` enables fp16/bf16 autocast
  without underflow; `clip_grad_norm_(model.parameters(), 1.0)` limits the
  damage of any one outlier batch on a 1.5 B model that started from a strong
  prior.
- **Sensitivity**: medium — clipping at `> 5` allows occasional spikes,
  `< 0.5` over-attenuates valid updates.
- **Bounds**: `0.5 — 5.0` plausible; chosen value 1.0.
- **Code ref**: `src/kernel/rl_finetune_best_of_n.py:62, 161-162, 253-260`.
- **Source**: official-solution.

---

# MALT-Sourced Heuristics

## H11: Budget judge throughput before scaling prompts per step
- **Rationale**: The Replicate Llama-3-8b judge enforces a per-minute rate limit.
  Steps with >= 192 prompts × 3 responses (~576 pairwise comparisons) or >= 20
  parallel workers consistently triggered sustained 429 storms. Successful runs
  used <= 64 prompts/step, 2 responses, <= 5 parallel workers, plus inter-batch
  delays of 20-30 s.
- **Evidence**: Runs 0 (N50, N53), 2 (N151), 5 (N302), 10 (N552), 13 (N701).
- **Source**: MALT (cross-run).

## H12: Pass targets to GPT.forward for full-sequence logits
- **Rationale**: The model.py GPT.forward short-circuits to last-position-only
  logits when `targets=None` (inference optimization). Any training loop that
  needs per-token logprobs must either pass dummy targets or edit the forward
  path. 8+ MALT runs wasted significant token budget rediscovering this.
- **Evidence**: Runs 0 (N50), 1 (N101), 3 (N200), 4 (N251), 9 (N500).
- **Source**: MALT (cross-run).

## H13: Keep named backups of scored checkpoints
- **Rationale**: `/home/agent/finetuned_model` is a shared mutable path; both
  the trainer and scorer write to it. Overwriting without a named copy of
  a good checkpoint is an irreversible loss: 7+ runs destroyed their peak
  this way (e.g. run 0: 0.44 -> 0.07 after overwrite).
- **Evidence**: Runs 0 (N56), 2 (N154), 3 (N206), 6 (N353), 9 (N504), 12 (N656), 17 (N905).
- **Source**: MALT (cross-run).

## H14: Score multiple intermediate checkpoints, not just the final one
- **Rationale**: Fine-tuning loss is not monotonically correlated with
  win-rate; earlier checkpoints frequently score better. In run 0,
  step-15 scored 0.569 vs step-20 at 0.070. Saving checkpoints every
  5 steps and scoring the best is a low-cost hedge.
- **Evidence**: Runs 0 (N57), 7 (N404), 11 (N603), 12 (N653/N654), 17 (N903).
- **Source**: MALT (cross-run).

## H15: Use lr <= 5e-6 for preference RL on gpt2-xl
- **Rationale**: lr >= 1e-5 works for short supervised phases (< 10 steps)
  but causes collapse in RL loops where preference noise compounds across
  steps. The official solution uses 4e-6. MALT runs that used 5e-6 or lower
  avoided catastrophic regression; those at 3e-5 collapsed within 1-2 steps.
- **Evidence**: Runs 3 (N202, 0.766 at cosine ~5e-6), 7 (N401, 0.798 at 5e-6),
  vs runs 7 (N400, collapse at 3e-5), 8 (N452, collapse at 3e-5).
- **Source**: MALT (cross-run).

## H16: Kill GPU processes before scoring
- **Rationale**: The scorer loads gpt2-xl weights (~6 GB) in its own process
  but shares the GPU. Zombie Python processes from interactive testing or
  killed trainers hold tens of GiB, causing the scorer to OOM. Before
  calling `score`, explicitly kill all other Python processes on GPU.
- **Evidence**: Runs 0 (N58), 3 (N204, N208), 10 (N553), 14 (N753).
- **Source**: MALT (cross-run).

## H17: model.py generate_strings_autobatch does not support top_p
- **Rationale**: The function signature is `(self, prompts, max_new_tokens,
  temperature=1.0, top_k=None, batch_size=128, use_old=False)`. Passing
  `top_p` raises TypeError. Diversity must be controlled via temperature
  and top_k only.
- **Evidence**: Runs 0 (N52), 1 (N101), 12 (N652).
- **Source**: MALT (cross-run).

## H18: Staged training (SFT then RL) outperforms RL-only on gpt2-xl
- **Rationale**: Base gpt2-xl has no instruction-following ability. Applying
  preference RL directly yields little gain because the model cannot even
  generate coherent responses to compare. A supervised warm-up phase (on
  manual examples or judge-preferred outputs) gives the RL loop a
  meaningful starting distribution. Runs 4 (N253, +0.525 in one attempt
  via 20 SFT + 50 RL), 6 (N357, 0.816 via SFT + refinement), and 16
  (N856, 0.807 via iterative SFT) all used this pattern.
- **Evidence**: Runs 4 (N253), 6 (N356-N358), 16 (N853-N856).
- **Source**: MALT (cross-run).
