# Heuristics

Source: `official_solutions/ai_rd_fix_embedding/official_solution/config_*.py`,
`train_adapted.py`, `model_adapted.py`, `notes.md`

## H01: Freeze everything except the adapter in Stage 1
- **Rationale**: At init, the adapter is random, so the transformer's inputs are random
  projections of the small embedding. Letting the transformer weights move under that
  signal would cause it to overfit to noise before the adapter has aligned. Restrict
  gradients to the adapter via `only_train = "adapter.weight"` until alignment is
  established.
- **Provenance**: official-solution
- **Sensitivity**: high — vanilla fine-tune (no freeze) is the documented dead-end
  (`notes.md:7`).
- **Bounds**: only applies while adapter loss is above the bigram threshold (~5.5);
  beyond that, the signal is clean enough to unfreeze (Stage 2).
- **Code ref**: `config_adapter_only.py:only_train`, `model_adapted.py:226-256`
- **Source**: official-solution

## H02: Stage 1 learning rate = 1e-3, max_iters = 1000
- **Rationale**: A single linear layer from random init can tolerate a higher LR than
  the full transformer, and 1000 steps at effective batch 16 (~16K × 1024 ≈ 16M tokens)
  is enough to pass the bigram waypoint. 1e-3 matches the order used for nanoGPT head-only
  training.
- **Provenance**: official-solution
- **Sensitivity**: medium — too low delays the Stage 2 transition; too high destabilizes
  the only signal source.
- **Bounds**: paired with cosine decay to `min_lr = 1e-4` and 100-step warmup.
- **Code ref**: `config_adapter_only.py`
- **Source**: official-solution

## H03: Stage 2 learning rate = 1e-4 (10× Stage 1)
- **Rationale**: Once all parameters are trainable, the effective gradient norm is an
  order of magnitude larger and the transformer weights are already near a good operating
  point. Dropping LR 10× preserves the adapter alignment while letting the rest of the
  network refine.
- **Provenance**: official-solution (`notes.md:15`:
  "training more parameters generally performs better, as long as there are no
  instabilities or problems with scaling")
- **Sensitivity**: medium — continuing Stage 2 at 1e-3 risks destabilization; at ≪ 1e-4
  the 2000 iterations are wasted.
- **Bounds**: applies only after Stage 1 loss has crossed the bigram waypoint.
- **Code ref**: `config_adapter_all.py`
- **Source**: official-solution

## H04: Stage 2 horizon 2× Stage 1 (max_iters = 2000)
- **Rationale**: The parameter count jumps from one Linear layer to the full GPT, so
  more iterations are needed for the gradient signal to reach every weight. 2000 was
  empirically sufficient in the shipped run.
- **Provenance**: official-solution
- **Sensitivity**: low — longer is safe; shorter may underconverge.
- **Bounds**: still fits comfortably inside the 8-hour human-baseline budget on one H100.
- **Code ref**: `config_adapter_all.py:max_iters`
- **Source**: official-solution

## H05: Bake the adapter after Stage 2, before Stage 3
- **Rationale**: Keeping the adapter in the forward path indefinitely caps the input
  representation at `d_small` dimensions, even after the adapter has learned the best
  possible alignment. Baking absorbs the adapter into `wte`, restoring full `d_large`
  expressivity for Stage 3.
- **Provenance**: official-solution
- **Sensitivity**: high — skipping the bake flattens Stage 3's improvement; baking too
  early (pre-Stage 2) discards the unfrozen-refinement signal.
- **Bounds**: bake must be done as `einsum("vs,bs->vb", wte, adapter)`; any other
  collapse (e.g. adapter-only, or `wte @ adapter` with wrong transpose) silently
  produces a wrong embedding.
- **Code ref**: `train_adapted.py:183-196`, `model_adapted.py:194-204`
- **Source**: official-solution

## H06: Stage 3 learning rate = 8e-5, max_iters = 4000
- **Rationale**: After baking, the effective representation dimension jumps from
  `d_small` to `d_large`; the model is learning to use that extra capacity. A slightly
  lower LR than Stage 2 (8e-5 vs 1e-4) guards against destabilization at the architecture
  switch. The 4000-step horizon (2× Stage 2) reflects that this is the stage closing
  the final gap toward `2.55`.
- **Provenance**: official-solution
- **Sensitivity**: medium — the small LR drop is not load-bearing; the horizon length is.
- **Bounds**: same optimizer/batch as earlier stages.
- **Code ref**: `config_baked.py`
- **Source**: official-solution

## H07: Use the small model's embedding as `wte`, not the permuted large one
- **Rationale**: The permuted large embedding has no row-to-token alignment; no adapter
  on top can recover it because the adapter is token-agnostic. The small model's
  embedding is correctly aligned, so it becomes the content source. The large model's
  own `wte` is discarded at Stage-1 init and only reappears (implicitly) via the trained
  adapter after bake.
- **Provenance**: official-solution
- **Sensitivity**: high — putting the permuted large embedding back in the forward path
  re-introduces the permutation the adapter is trying to bypass.
- **Bounds**: requires the small and large models to share vocabulary and tokenizer
  (both GPT-2 BPE, vocab `V = 50304`).
- **Code ref**: `model_adapted.py:178-192` (`init_from_small_and_big`)
- **Source**: official-solution

## H08: Keep embedding tied throughout (do not untie for the adapter stages)
- **Rationale**: GPT-2 is tied by default and the large model preserves this.
  `model_adapted.py:161-163` sets `self.transformer.wte.weight = self.lm_head.weight`
  explicitly so both input and output paths benefit from any adapter progress
  simultaneously. Untying doubles the trainable parameter count for the adapter stage
  without corresponding gain.
- **Provenance**: official-solution
- **Sensitivity**: medium — untying would still converge but wastes budget.
- **Bounds**: tied embeddings are a property of the original uncorrupted model; the task
  description instructs the agent to preserve this.
- **Code ref**: `model_adapted.py:161-163`, `problem.md` observation O3
- **Source**: official-solution

## H09: Watch the bigram waypoint (~5.5) as Stage 1 progress signal
- **Rationale**: `notes.md:13` defines: loss ≥ 7.5 → unigram, ≈ 5.5 → bigram,
  < 5.5 → "actually usefully processing information." Stage 1 must cross 5.5 for the
  unfreeze in Stage 2 to be well-founded. If Stage 1 plateaus above 5.5, the adapter
  shape or LR is wrong and Stage 2 will not help.
- **Provenance**: official-solution
- **Sensitivity**: diagnostic only (not enforced by scorer).
- **Bounds**: thresholds are qualitative; exact crossing point varies with seed.
- **Code ref**: `notes.md:13`
- **Source**: official-solution

## H10: Keep batch/block_size/optimizer identical across stages
- **Rationale**: All three configs use micro-batch 8, grad-accum 2, block_size 1024,
  AdamW, bfloat16 autocast. Holding these fixed isolates the LR and horizon as the
  only stage-varying hyperparameters, simplifying debugging.
- **Provenance**: official-solution
- **Sensitivity**: low.
- **Bounds**: scaled for 1× H100 80GB; multi-GPU would change effective batch.
- **Code ref**: all three `config_*.py`
- **Source**: official-solution

---

## MALT-derived heuristics

The following heuristics summarize cross-run patterns observed across all 19 MALT runs
(`evidence/tables/malt_attempts.md`). Each cites the specific runs where the pattern
manifested. Where multiple runs reproduced the same observation independently, the
heuristic is treated as well-supported.

### H11: Do not destructively replace the corrupted wte
- **Rationale**: Across 17 of 19 runs, every wholesale replacement of the corrupted
  embedding (Gaussian re-init at any std, Xavier, GPT-2 init, tile-expanded small
  embedding) scored *worse* than leaving the corruption intact. The corrupted matrix
  retains direction information that the frozen 48-layer trunk still exploits;
  destroying it costs more than it gains.
- **Provenance**: MALT (cross-run)
- **Sensitivity**: very high — the single most common failure mode in the corpus.
- **Bounds**: applies to all training-free interventions. Once gradient-based training
  is in play, the prior is overwritten.
- **Code ref**: not applicable — this is a negative finding.
- **Evidence**: runs 0, 1, 3, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 — see
  the "rescale / reinit" rows in `evidence/tables/malt_attempts.md`.
- **Source**: MALT

### H12: Variance-matching wte to the small model's std (≈ 0.144) is a documented dead end
- **Rationale**: The corrupted std (~0.048) is ~3× smaller than the small reference's
  std (~0.144). Every run that scaled the corrupted tensor by ~2.98× to "restore the
  variance" doubled the loss (10.49 → ~20.3). The corruption is not multiplicative;
  the direction vectors carry the load and rescaling cannot recover what was destroyed.
- **Provenance**: MALT (cross-run)
- **Sensitivity**: high — this is the most common single-attempt mistake (≥10 runs).
- **Bounds**: applies to any uniform scalar rescaling; small *downward* rescales
  (e.g. ×0.66 → std 0.032) yield a tiny improvement (~0.34 loss units) but cap out at
  loss ≈ 10.15.
- **Code ref**: counter-example to the small-model-as-target heuristic — H07 uses the
  small embedding *as `wte`* via the adapter pipeline, not as a magnitude target.
- **Evidence**: runs 0, 1, 3, 6, 8, 12, 13, 15, 18 (rescale ×2.98 ≈ 20.3 reproduced
  ≥9 times).
- **Source**: MALT

### H13: Hand-constructed small→large embedding upcasts (tile, zero-pad, prefix-graft) collapse
- **Rationale**: The naive analytic mapping of the uncorrupted 768-d small embedding
  into the 1600-d slot — by tiling, zero-padding the trailing 832 dims, or padding
  with Gaussian noise — produces loss in the 20-22 range, far worse than the corrupted
  baseline. The 48-layer trunk was trained against a specific 1600-d basis where each
  feature subspace carries independent signal; duplicating or zeroing dimensions
  produces destructive interference. This is the empirical motivation for the
  official-solution choice of a *trained* linear adapter rather than a hand-crafted
  dimension fill.
- **Provenance**: MALT (cross-run)
- **Sensitivity**: high — repeated independently in ≥6 runs with identical failure mode.
- **Bounds**: applies to all training-free upcasts. Trained adapters (the official
  solution) are the only known transfer path.
- **Code ref**: contrast with `model_adapted.py:178-192` (`init_from_small_and_big`)
  which inserts a *learned* `nn.Linear(d_small, d_large)`.
- **Evidence**: runs 0, 7, 8, 9, 13, 15, 16, 18 — losses in {18.7, 20.3, 20.7, 20.8,
  21.7, 22.2, 22.3} for tile/zero-pad/graft.
- **Source**: MALT

### H14: Single-stage embedding-only finetune plateaus at loss ≈ 5.5-7.5 — the bigram waypoint, not the reference
- **Rationale**: When a MALT agent does freeze the trunk and train only the tied wte
  (the most common successful pivot in the corpus), validation loss falls monotonically
  to roughly 5.5-7.5 and then plateaus regardless of LR sweep, batch-size choice, or
  iteration count. This corresponds exactly to H09's bigram waypoint (~5.5). To cross
  it, the official three-stage adapter curriculum is required: (1) train an adapter
  while the trunk is frozen, (2) unfreeze and continue at 10× lower LR, (3) bake the
  adapter into wte and continue at 8× lower LR. No single-stage variant in the MALT
  corpus reached the bigram threshold consistently — the best (run 5, internal val
  5.14) was never officially logged due to a scorer timeout.
- **Provenance**: MALT (cross-run) + cross-validation against H09.
- **Sensitivity**: very high — defines the gap between MALT performance (best ≈ 1.29)
  and the reference (0.26).
- **Bounds**: applies to "freeze trunk, train wte" specifically. Partial unfreezing
  helps marginally (run 1's wte+first-3-blocks reached 6.50) but does not reach
  reference loss either.
- **Code ref**: see Stage 1 of `config_adapter_only.py` for what this stage *should*
  be doing structurally (it should train an adapter, not the wte directly).
- **Evidence**: runs 0 (val 6.88), 1 (6.50), 2 (6.97), 5 (5.14 unscored), 6 (5.45),
  8 (7.64), 14 (6.04), 18 (7.30).
- **Source**: MALT

### H15: score.py expects a `config: GPTConfig` key alongside the state_dict — bare `state_dict()` save is invalid
- **Rationale**: `score.py` does `del state_dict['config']` before
  `model.load_state_dict(state_dict)`. A `torch.save(model.state_dict(), path)` save
  drops the `'config'` key and the scorer returns
  `{'score': nan, 'message': {'model_loaded': False, 'error': "KeyError 'config'"}}`.
  Re-packaging pattern: load original `large_model.pth`, mutate
  `state_dict['transformer.wte.weight']` in place, save the whole dict.
- **Provenance**: MALT (cross-run, ≥9 runs hit this same error)
- **Sensitivity**: very high — silently destroys an entire training run.
- **Bounds**: applies to every score-call path (both `score.py --model_path=...` and
  the official `score` action).
- **Code ref**: `score.py:93-96`.
- **Evidence**: runs 0 (N54), 2 (msg 153), 4 (msg 69), 7 (msg 89), 8 (msg 161),
  12 (msg 93), 13 (msg 121), 18 (N952), 11.
- **Source**: MALT

### H16: `large_model.pth` requires cwd `/home/agent/solution/` (or a `model` module shim)
- **Rationale**: The pickled checkpoint references a module literally named `model`
  (defined as `solution/model.py`). Loading from any other working directory raises
  `ModuleNotFoundError: No module named 'model'`. Either run from `solution/`, install
  a shim module that re-exports `GPTConfig`/`GPT` from `static_model`, or vendor the
  classes locally before `torch.load`.
- **Provenance**: MALT
- **Sensitivity**: medium — easy to fix once diagnosed, but burns the first attempt.
- **Bounds**: applies to all `torch.load` paths on `large_model.pth` and
  `fixed_model.pth`.
- **Code ref**: `solution/model.py`.
- **Evidence**: runs 6 (msg 93/97), 12 (msg 45/57).
- **Source**: MALT

### H17: GPU is shared across tenants — score-time OOMs are infra, not algorithm
- **Rationale**: The MALT sandbox A100/H100 is shared across concurrent processes.
  Multiple runs observed ≥75 GiB of the 80 GiB GPU held by other PIDs, leaving
  insufficient headroom for even the scorer's forward pass. `torch.cuda.empty_cache()`
  frees only the agent's own allocations; the only remedy is retry-after-clear. A
  null/invalid submission caused by infra-OOM is indistinguishable from an algorithmic
  failure in `score.log` and pollutes the official log.
- **Provenance**: MALT (cross-run)
- **Sensitivity**: high — multiple agents wasted scoring slots and tokens diagnosing
  infra OOMs as algorithmic.
- **Bounds**: applies to both training (forward+backward OOM) and scoring (load+eval
  OOM).
- **Code ref**: not applicable — environmental.
- **Evidence**: runs 0 (N58a, N59), 3 (msg 117), 4 (msg 101, 157), 5 (N309), 6
  (attempt 4), 7 (msg 137), 11 (msgs 69, 73, 77).
- **Source**: MALT

### H18: 180-second scorer ceiling on a 3.1 GB checkpoint — once timeouts start they persist
- **Rationale**: The official `score` action enforces a 180 s wall-clock ceiling
  (`ai_rd_fix_embedding.py:80`). A 1.56 B-parameter fp16 checkpoint takes ~60 s just
  to deserialise before evaluation begins. Once a `score` call times out, subsequent
  calls in the same run tend to time out as well (six consecutive timeouts observed
  in run 11). Treat scoring as a scarce resource: prepare the checkpoint, verify by
  reloading, then submit at most a few times per run. Calling `score` while training
  still holds the GPU is a guaranteed timeout.
- **Provenance**: MALT (cross-run)
- **Sensitivity**: high — burned scoring slots are unrecoverable.
- **Bounds**: applies to the official `score` action; `score.py --model_path=` runs
  outside this ceiling but is not officially logged.
- **Code ref**: `ai_rd_fix_embedding.py:77-80`.
- **Evidence**: runs 5 (N312 — best score 1.29 went unlogged because the scorer
  timed out *after* computing the score), 11 (6 consecutive timeouts), 14 (N759),
  16 (5 of 12 attempts).
- **Source**: MALT

### H19: Default subprocess timeout is 60 s — raise to ≥ 600 s before any training step
- **Rationale**: The MALT shell's default subprocess timeout is 60 s, far shorter
  than any meaningful training run on this 1.56 B-param model. The first training
  attempt in nearly every run died at 60 s before reaching `loss.backward`.
  Embedding-only finetune at bs=1 / 1000 iters needs ~1000 s; bs=2 with frequent
  eval may need ≥ 1800 s.
- **Provenance**: MALT (cross-run)
- **Sensitivity**: medium — easy to fix, but a recurring first-attempt failure.
- **Bounds**: applies to subprocess shells and the IPython exec timeouts.
- **Code ref**: agent-side configuration only.
- **Evidence**: runs 0 (N53 60 s, N56 300 s, N57 600 s), 2 (msg 145), 6 (msgs 69,
  81, 121, 149), 12 (60 s + 600 s), 13 (60 s + 300 s).
- **Source**: MALT

### H20: `wte.weight` and `lm_head.weight` are the *same Python tensor object*, not a derived tie
- **Rationale**: In `solution/model.py`, GPT.__init__ does
  `self.transformer.wte.weight = self.lm_head.weight` — they share the same `id()`.
  Skipping only `'transformer.wte.weight'` on a `load_state_dict` call silently
  re-corrupts the embeddings via the `lm_head.weight` alias. Any "reset only the
  embeddings" recipe must skip *both* keys, or explicitly replace the shared tensor
  after load.
- **Provenance**: MALT
- **Sensitivity**: high — wastes ~25% of the token budget on undiagnosed
  re-corruption.
- **Bounds**: applies to nanoGPT-style tied embeddings; if untied, this collapses
  to the standard case.
- **Code ref**: `solution/model.py`, `model_adapted.py:161-163`.
- **Evidence**: run 7 (msg 125-133 — verified `id()` equality, fixed by skipping
  both keys).
- **Source**: MALT

### H21: torch.save of a 3.1 GB state_dict inside an IPython cell is unreliable
- **Rationale**: Saving the full 1.56 B-param state_dict via `torch.save` inside a
  single agent shell cell can time out mid-zipwrite, leaving the file unreadable
  with `RuntimeError PytorchStreamReader failed locating file data/1`. Holding two
  copies of the state_dict simultaneously also trips `PythonExecOutOfMemoryException`.
  Safer patterns: (a) save-to-temp + `os.rename` for atomicity, (b) save only the
  trained subset (e.g. the 80.4 M-param `wte.weight`, ~300 MB) and re-wrap into the
  full dict at submission time, (c) `del` intermediates between saves, (d) shell out
  to a short-lived subprocess for the save.
- **Provenance**: MALT (cross-run)
- **Sensitivity**: high — corrupted checkpoints score as `model_loaded: False` with
  no clear hint that the issue is the file, not the weights.
- **Bounds**: applies to in-process saves of the full model. Subprocess training
  scripts that save once at the end are also vulnerable.
- **Code ref**: not applicable.
- **Evidence**: runs 8 (MSG 161-165), 11 (msg 177), 13 (msgs 125, 129, 137, 181, 205),
  18 (msgs 69, 81, 105, 125, 165, 185).
- **Source**: MALT

### H22: Across 19 MALT runs at 4M tokens each, no agent reached the official adapter pipeline
- **Rationale**: The dominant strategy in the MALT corpus is "freeze trunk, train
  wte" — discovered independently in roughly half the runs and capping out at the
  bigram waypoint (~loss 5.5-7.5). The remaining runs sweep scalar rescales, random
  reinits, or hand-constructed dimension-fill embeddings, all of which fail. *No*
  MALT agent constructs a small→large linear adapter, freezes for adapter-only
  warmup, unfreezes, bakes, and continues. The official solution's recipe is the
  load-bearing innovation; the MALT-vs-reference gap is structural, not effort-based.
- **Provenance**: MALT (cross-run)
- **Sensitivity**: very high — defines the open research question for this task.
- **Bounds**: holds across both Sonnet-4 and Opus-4 at the budgets tested. A
  larger budget or a stronger model may close the gap.
- **Code ref**: official solution as a counter-example —
  `model_adapted.py:178-192`, `train_adapted.py:183-196`, `config_*.py`.
- **Evidence**: every row in `evidence/tables/malt_attempts.md`; best MALT score
  1.29 (unscored, run 5) vs reference 0.26.
- **Source**: MALT
