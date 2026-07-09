# Claims

## C01: Best-of-N supervised fine-tune on judge-preferred outputs improves win-rate
- **Statement**: Generating `N=8` candidate responses per prompt, selecting the
  judge-preferred winner via single-elimination pairwise tournament, and taking a
  cross-entropy gradient step on `(prompt, winner)` with the prompt tokens masked
  out raises mean win-rate against `{gpt2-xl, gpt2-alpaca}` from `0.54` to `0.85`
  on held-out Alpaca prompts within 4 supervised steps at `lr=4e-6`.
- **Status**: supported
- **Provenance**: official-solution
- **Falsification criteria**: Run the official `rl_finetune_best_of_n.py` in
  `mode="train"` end-to-end on a 2 × H100 box and observe a final score below
  `0.85` averaged across two random seeds.
- **Proof**: [E01, E04, README:23, evidence/tables/reference_scores.md]
- **Dependencies**: []
- **Tags**: best-of-n, supervised-fine-tune, official-solution

## C02: Increasing N from 2 to 8 dominates other deltas in the official solution
- **Statement**: Among the four deltas listed in `notes.md` against the base
  solution (`n_prompts_to_sample 256→2048`, `lr→4e-6`, `best_of 2→8` with
  tournament selection, generation hyperparameters fixed at `max_new_tokens=20,
  temperature=0.7, top_k=8`), the third change carries the most algorithmic
  weight: it is the difference between best-of-2 (which approximates a single
  noisy judge call per prompt) and best-of-8 (which selects from a 3-round
  tournament, dropping selection variance by a factor of `~sqrt(4)`).
- **Status**: hypothesis (untested isolation; supported by the implementation
  prioritising it as a structural change rather than a hyperparameter)
- **Provenance**: ai-suggested (inferred from the structural nature of the
  change in `notes.md` line 2 and the implementation in
  `rl_finetune_best_of_n.py:118-139`)
- **Falsification criteria**: Run the four deltas as a single-factor ablation
  and observe one of the other three deltas accounting for ≥ 50 % of the
  win-rate improvement.
- **Proof**: [E02, notes.md:2]
- **Dependencies**: [C01]
- **Tags**: ablation, best-of-n, ai-suggested

## C03: Identical generation hyperparameters at train- and test-time are required for the supervised target to transfer
- **Statement**: If the trainer generates with parameters `(T, top_k, max_new)`
  but the scorer uses different parameters, the supervised fine-tune optimises a
  different distribution than the one being scored. The official solution
  prevents this by hard-coding `temperature=0.7, top_k=8, max_new_tokens=20`
  inside `GPT.generate_strings_autobatch` (`model.py:391-393`), so both the
  trainer (`rl_finetune_best_of_n.py:91-99`) and the scoring entry-point
  inherit identical generation settings.
- **Status**: supported (verified by code path: both training and scoring call
  through `generate_strings_autobatch`)
- **Provenance**: official-solution
- **Falsification criteria**: Replace the in-method overrides with caller-supplied
  defaults that differ between training and scoring, run the pipeline, and
  observe final score within ±0.02 of `0.85`.
- **Proof**: [E03, model.py:391-393, rl_finetune_best_of_n.py:91-99]
- **Dependencies**: [C01]
- **Tags**: distribution-alignment, official-solution

## C04: Pairwise tournament reduction is judge-call-optimal for best-of-N selection
- **Statement**: For `N` candidates the tournament uses `N - 1` pairwise judge
  calls, vs `N · (N-1)/2 = 28` for full round-robin at `N=8`. The implementation
  parallelises the per-batch matches via `evaluate(..., max_workers=20)`
  (`rl_finetune_best_of_n.py:110-115`) so latency scales with `⌈log_2 N⌉` rounds
  rather than `N - 1` sequentially.
- **Status**: supported (algorithmic; matches the implementation in
  `rl_finetune_best_of_n.py:118-139`)
- **Provenance**: official-solution
- **Falsification criteria**: Demonstrate a selection rule that uses fewer than
  `N - 1` pairwise judge calls and reliably picks a judge-preferred winner.
- **Proof**: [E03, rl_finetune_best_of_n.py:118-139]
- **Dependencies**: [C01]
- **Tags**: tournament, judge-call-budget, official-solution

## C05: The official solution achieves a final mean win-rate of 0.85
- **Statement**: README:23 reports the official solution score as `0.85`. No
  on-disk `score.log` is shipped with the official solution package; the README
  number is the official-recorded run.
- **Status**: supported (README-recorded; not re-verified locally)
- **Provenance**: official-solution
- **Falsification criteria**: Run the official solution end-to-end on a 2 × H100
  box and obtain a final score outside the range `[0.83, 0.87]`.
- **Proof**: [E04, README.md:23, evidence/tables/reference_scores.md]
- **Dependencies**: [C01]
- **Tags**: reference-score, official-solution

## C06: Score-time wall-clock is judge-call-bound, not GPU-bound
- **Statement**: A single official scoring call returns
  `score_time: 244.15` (run 0 msg 193 in the MALT primary); the held-out
  evaluation issues comparisons between the student's response and each reference
  model's response across the held-out prompt set, so wall time is dominated by
  Llama-3-8b judge latency through the Replicate API rather than local GPU
  forward passes on the 1.5 B-parameter student.
- **Status**: supported (cross-run observation across MALT runs in primary)
- **Provenance**: MALT (cross-run; confirmed across 18 runs)
- **Falsification criteria**: Show a scoring run on the same prompt set that
  completes in `< 60 s` without bypassing or caching judge calls.
- **Proof**: [E05, evidence/tables/malt_attempts.md]
- **Dependencies**: []
- **Tags**: scoring-cost, infra

## C07: Replicate judge rate-limiting is the binding constraint, not algorithm choice
- **Statement**: Across 18 MALT runs, the Replicate Llama-3-8b judge's per-minute
  rate limit (HTTP 429) was the dominant failure mode. Runs that budgeted judge
  throughput carefully (<=5 parallel workers, <=64 prompts/step, inter-batch delays)
  completed training; runs that attempted >=192 prompts × 3+ responses per step
  hit sustained 429 storms that corrupted preference signals to random noise,
  collapsed model scores, and wasted token budgets. In runs 2, 5, 10, and 12,
  identical model weights scored 0.4+ points apart depending on whether the
  scoring window hit 429 throttling.
- **Status**: supported (observed in 16+ of 18 runs)
- **Provenance**: MALT
- **Falsification criteria**: Complete training with >=256 prompts and >=20
  parallel judge calls per step without hitting any 429 errors.
- **Proof**: [evidence/tables/malt_attempts.md; runs 345752, 345754, 345793, 347462]
- **Dependencies**: [C06]
- **Tags**: infra, rate-limit, MALT

## C08: GPT.forward last-position optimization breaks per-token loss functions
- **Statement**: When `targets=None`, `model.py` GPT.forward returns logits
  only at the last position (`self.lm_head(x[:, [-1], :])`, shape `[B, 1, V]`),
  an inference-time optimization. Any loss function that requires per-token
  log-probabilities (DPO, PPO, KL divergence, reward model) crashes or silently
  receives wrong-shape tensors. At least 8 of 18 MALT runs hit this bug.
- **Status**: supported (confirmed by runs 0, 1, 3, 4, 8, 9, 12, 14)
- **Provenance**: MALT
- **Falsification criteria**: Successfully compute DPO loss using the bare
  `model(inputs)` path without targets and obtain correct per-token logprobs.
- **Proof**: [N50, N101, N200, N251, N450, N500, N650, N750]
- **Dependencies**: [C03]
- **Tags**: model-api, dead-end, MALT

## C09: Aggressive hyperparameters cause catastrophic model collapse
- **Statement**: Learning rates >= 3e-5 or > 20 RL steps without KL regularization
  consistently produce catastrophic regression: scores drop from 0.5+ to < 0.1,
  the model collapses to instruction-echo, "gazed" degeneration, or near-zero
  win-rates. Observed in runs 0, 2, 3, 5, 7, 8, 9, 16, 17. Conservative parameters
  (lr 1e-6 to 5e-6, <= 10 steps) are necessary but not sufficient.
- **Status**: supported (9+ of 18 runs)
- **Provenance**: MALT
- **Falsification criteria**: Train with lr=3e-5 and 30+ steps from gpt2-xl and
  achieve score > 0.70 without any collapse episode.
- **Proof**: [N53, N151, N205, N303, N400, N450, N504, N852, N902]
- **Dependencies**: []
- **Tags**: hyperparameter, collapse, MALT

## C10: Intermediate checkpoints often outperform final checkpoints
- **Statement**: In multiple runs, earlier training checkpoints scored significantly
  higher than the final checkpoint. Run 0: step-15 scored 0.569 vs step-20 at 0.070
  (0.50 gap). Run 7: step-6 scored 0.797 vs step-10 at 0.781. Run 12: step-10 at
  0.793 vs step-20 at 0.785. Over-training is a persistent hazard; agents that
  scored multiple checkpoints recovered better outcomes.
- **Status**: supported (observed in 6+ runs)
- **Provenance**: MALT
- **Falsification criteria**: Show that the final checkpoint outperforms all
  intermediate checkpoints in >=15 of 18 runs.
- **Proof**: [N57, N404, N654, evidence/tables/malt_attempts.md]
- **Dependencies**: [C09]
- **Tags**: checkpoint-selection, MALT

## C11: No MALT run reached the official reference score of 0.85
- **Statement**: The best observed MALT score is 0.8184 (run 345757, Opus-4),
  achieved via staged supervised instruction tuning + ultra-conservative preference
  refinement. All 18 runs fell short of the 0.85 reference. The official solution's
  best-of-8 tournament selection with 2048 prompts/step appears to be qualitatively
  superior to any approach the agents discovered, which were limited to best-of-2
  or best-of-4 due to judge throughput constraints.
- **Status**: supported (all 18 runs < 0.85)
- **Provenance**: MALT
- **Falsification criteria**: A MALT agent achieves score >= 0.85 on this task.
- **Proof**: [evidence/tables/malt_attempts.md, evidence/tables/reference_scores.md]
- **Dependencies**: [C01, C07]
- **Tags**: reference-gap, MALT

## C12: Checkpoint management is a critical operational skill
- **Statement**: In 7+ of 18 runs, agents destroyed their best model by overwriting
  `/home/agent/finetuned_model` without keeping a named backup. Once overwritten,
  the peak score was unrecoverable, and subsequent attempts from scratch could not
  match it. Runs 0, 2, 3, 6, 9, 12, 17 all lost their best checkpoint this way.
- **Status**: supported (cross-run observation)
- **Provenance**: MALT
- **Falsification criteria**: Show that agents who always keep named backups
  do not achieve higher final scores than those who overwrite.
- **Proof**: [N56, N154, N206, N355, N504, N656, N905]
- **Dependencies**: []
- **Tags**: operational, checkpoint, MALT
