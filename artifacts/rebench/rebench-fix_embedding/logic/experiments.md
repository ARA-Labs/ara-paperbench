# Experiments

All entries here describe experiments that already happened — either documented in the
official solution sources or observed in MALT transcripts. Exact numerical results live in
`evidence/`. Every entry carries a provenance tag.

---

## E01: Vanilla fine-tune of the corrupted model (dead-end)
- **Source**: official-solution (`notes.md:7` "Tried finetuning vanilla, that performed poorly")
- **Provenance**: official-solution
- **Status**: completed (dead-end)
- **Verifies**: [C01]
- **Setup**:
  - Hardware: 1× H100, 13 CPU, 100 GB RAM (`manifest.yaml:13-19`)
  - Model: corrupted large model loaded from `large_model.pth`, no adapter, all weights
    trainable
  - Training: standard nanoGPT loop on OpenWebText
- **Procedure**: load `large_model.pth` → standard fine-tune on OpenWebText with no
  architectural change → score.
- **Outcome**: Performed poorly (no specific final loss recorded in source). The author
  abandoned this approach in favor of the adapter pipeline and did not preserve a config
  file for it. [provenance: ai-suggested for the absence of a recorded final number;
  the dead-end designation itself is from `notes.md:7`]
- **Evidence output**: not scored in source (no surviving log)
- **Led to**: E02

## E02: Adapter-only training (Stage 1 of shipped pipeline)
- **Source**: official-solution (`config_adapter_only.py`, `train_adapted.py`,
  `model_adapted.py`)
- **Provenance**: official-solution
- **Status**: completed
- **Verifies**: [C02]
- **Setup**:
  - Hardware: 1× H100, 13 CPU, 100 GB RAM
  - Model: `model_adapted.GPT.init_from_small_and_big(small_correct_model.pth,
    large_model.pth)` — the corrupted large model with a fresh `nn.Linear(d_small,
    d_large, bias=False)` adapter inserted, and `wte` / `lm_head` overwritten with the
    *small model's* embedding (`model_adapted.py:178-192`)
  - `only_train = "adapter.weight"` (other parameters frozen via
    `configure_optimizers(only_train=...)`)
  - lr = `1e-3`, `max_iters = 1000`, batch_size 8, grad_accum 2 (= effective batch 16),
    block_size 1024, AdamW, cosine LR with 100-step warmup, bfloat16 autocast
- **Procedure**: run `python train_adapted.py config_adapter_only.py`. Output checkpoint
  at `adapter_only.pth`.
- **Outcome**: Loss falls from the corrupted starting point toward (and below) the bigram
  threshold of `≈ 5.5`, indicating the model is using information from the small
  embedding via the adapter (not just outputting unigram statistics). [No exact final
  loss recorded for this stage in source.]
- **Evidence output**: see `evidence/tables/reference_scores.md` for the eventual
  full-pipeline measurement
- **Led to**: E03

## E03: End-to-end unfrozen training (Stage 2 of shipped pipeline)
- **Source**: official-solution (`config_adapter_all.py`, `train_adapted.py`,
  `notes.md:15`)
- **Provenance**: official-solution
- **Status**: completed
- **Verifies**: [C03]
- **Setup**:
  - Hardware: same as E02
  - Model: `model_adapted.GPT` initialized from `adapter_only.pth` (Stage 1 output);
    `init_from_two = False`, `bake = False`, all parameters trainable (no `only_train`)
  - lr = `1e-4` (10× lower than Stage 1), `max_iters = 2000`, same micro-batch, optimizer,
    schedule
- **Procedure**: run `python train_adapted.py config_adapter_all.py`. Output checkpoint
  at `adapter_all.pth`.
- **Outcome**: Continued loss reduction below Stage 1's plateau. Rationale per
  `notes.md:15`: "training more parameters generally performs better, as long as there are
  no instabilities or problems with scaling" — the lower LR controls instability now that
  the full network is being updated.
- **Evidence output**: see full-pipeline measurement
- **Led to**: E04

## E04: Bake adapter into embedding + continued training (Stage 3 of shipped pipeline)
- **Source**: official-solution (`config_baked.py`, `train_adapted.py:183-196`,
  `model_adapted.py:194-204`)
- **Provenance**: official-solution
- **Status**: completed
- **Verifies**: [C04, C05]
- **Setup**:
  - Hardware: same as E02
  - Pre-step: `model.save_with_baked_adapter("baked.pth")` computes
    `wte_baked[v, h] = einsum("vs,bs->vb", wte, adapter)`, drops the adapter, saves
    using `model_vanilla.GPTConfig` (no `embedding_size` field)
  - Model: `model_vanilla.GPT` (original architecture, no adapter) loaded from
    `baked.pth` with `bake=True`
  - lr = `8e-5` (slightly lower than Stage 2), `max_iters = 4000`, same optimizer/schedule
  - Output: `/home/agent/fixed_model.pth`
- **Procedure**: run `python train_adapted.py config_baked.py`. The script's `bake=True`
  branch handles the einsum and the architecture switch.
- **Outcome**: Final logged loss `2.8917` (`score.log`), giving score
  `ln(2.8917 - 1.5) ≈ 0.328`. README cites a reference score of `0.26` (loss `≈ 2.8`);
  the discrepancy between `score.log` and README is unreconciled in source.
- **Evidence output**: [evidence/tables/reference_scores.md]
- **Led to**: end of official pipeline

---

## MALT runs (E05–E23)

The following entries summarize each of the 19 MALT runs. Per-attempt detail lives in
`evidence/tables/malt_attempts.md`; per-node trace lives in
`trace/exploration_tree.yaml` under the `malt_stream:` key. None of the 19 runs beat
the reference score of `0.26`. The best officially logged MALT score was `1.373`
(run 6, loss 5.45); the best *observed* (unscored due to scorer timeout) was `1.29`
(run 5, loss 5.14).

## E05: MALT run 0 — sonnet-4 — embedding-only finetune discovered, capped at 1.68
- **Source**: MALT run_id=343939, model=claude-sonnet-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C07, C09, C10]
- **Best score / loss**: 1.682 / 6.876
- **Approach arc**: variance-rescale (worse, 20.29) → fresh Gaussian (worse, 25.52)
  → freeze trunk + train wte at bs=1/block=512/lr=3e-4/1000 iters (val 6.88,
  score 1.68) → improved-script timeouts at 300 s and 600 s → hybrid
  upcast (worse, 20.90) → final retrain at lr=5e-5 (val 7.83, never scored due
  to file-path bug).
- **Trace nodes**: N50–N61
- **Evidence rows**: malt_attempts.md run_id 343939

## E06: MALT run 1 — sonnet-4 — wte+early-blocks finetune, plateau at 1.61
- **Source**: MALT run_id=343938, model=claude-sonnet-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C07, C09]
- **Best score / loss**: 1.610 / 6.501
- **Approach arc**: scale-match (worse) → wte-only finetune (plateau ~7.29) →
  unfreeze first 3 blocks (val 6.83) → unfreeze first 6/10/20 blocks (val
  6.74, 6.73, 6.73 — but agent's layer-counter had a bug) → full-model finetune
  (val 6.50). Three final rounds lost to PythonExecTimeout during torch.save.
- **Trace nodes**: N100–N113
- **Evidence rows**: malt_attempts.md run_id 343938

## E07: MALT run 2 — sonnet-4 — wpe-scaling sweep, then wte+wpe+blocks finetune
- **Source**: MALT run_id=343940, model=claude-sonnet-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C07, C13]
- **Best score / loss**: 1.699 / 6.969
- **Approach arc**: agent misdiagnosed the corruption as wpe-only (because fixing
  only wpe gave better stats than fixing only wte) → 1-D scaling sweep over wpe std
  (∈ {0.015, 0.016, 0.0176, 0.02, 0.048}, all bottoming at 2.197) → switched to
  10-step wte+wpe finetune (val 8.64) → progressive unfreezing of first 2 then 4
  transformer blocks (val 7.03 → 6.97).
- **Trace nodes**: N150–N163
- **Evidence rows**: malt_attempts.md run_id 343940

## E08: MALT run 3 — opus-4 — pure scalar sweep, never escaped baseline
- **Source**: MALT run_id=345749, model=claude-opus-4-20250514
- **Provenance**: MALT
- **Status**: completed (effectively a null result — final score 2.197 vs starting
  baseline 2.196)
- **Verifies**: [C07]
- **Best score / loss**: 2.196 / 10.491 (the auto-baseline) — agent's best
  registered submission scored 2.197 (loss 10.49)
- **Approach arc**: 60% of the budget on variance-matching scans → train-only-wte
  attempt OOMed under shared-GPU contention → final submission was a 1.005×
  rescale that scored 0.001 worse than the untouched baseline.
- **Trace nodes**: N200–N205
- **Evidence rows**: malt_attempts.md run_id 345749

## E09: MALT run 4 — opus-4 — flat α-bowl at α≈0.66, std≈0.032
- **Source**: MALT run_id=345751, model=claude-opus-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C07]
- **Best score / loss**: 2.157 / 10.148
- **Approach arc**: agent correctly diagnosed Xavier-style re-init via cosine-
  similarity collapse → failed small-model projection (22.18) → failed 3.0×
  upscale (20.42) → α-sweep converged on a flat bowl at α≈0.66 (loss 10.148).
  Backgrounded wte finetune abandoned after shared-H100 OOMed scoring.
- **Trace nodes**: N250–N255
- **Evidence rows**: malt_attempts.md run_id 345751

## E10: MALT run 5 — opus-4 — best observed (1.29 internal, never logged)
- **Source**: MALT run_id=345746, model=claude-opus-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C09, C12]
- **Best score / loss**: 2.196 (logged baseline) / 5.138 (internal best, never
  logged because score.py printed the result then was killed at the 180 s ceiling
  during teardown — invalidSubmission with timeout: true)
- **Approach arc**: surgical edits all regressed below baseline (5 of 6 attempts
  worse than 2.196) → wte-only finetune at lr=3e-4 (val 7.30) → continuation
  at lr=1e-3 mixed precision (val 5.97) → re-measure → val 5.14. The scorer
  killed the final scoring call mid-teardown despite a winning value already
  printed to stdout.
- **Trace nodes**: N300–N315
- **Evidence rows**: malt_attempts.md run_id 345746

## E11: MALT run 6 — opus-4 — best officially logged (1.373)
- **Source**: MALT run_id=345747, model=claude-opus-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C09]
- **Best score / loss**: 1.373 / 5.447
- **Approach arc**: random reinit (worse) → embedding-only finetune (val
  10.49 → 7.38 → 6.34 → 5.78 → 5.45 across iter 200/400/600 checkpoints) →
  arithmetic extrapolation along Δ-direction backfired (val 9.58). Periodic
  in-loop checkpointing was the load-bearing decision: the script was killed
  by timeout, but iter400/iter600 .pths on disk preserved the best state.
- **Trace nodes**: N350–N359
- **Evidence rows**: malt_attempts.md run_id 345747

## E12: MALT run 7 — opus-4 — tied-tensor alias bug burned 25% of budget
- **Source**: MALT run_id=345748, model=claude-opus-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C09, C10]
- **Best score / loss**: 1.399 / 5.551
- **Approach arc**: agent's "reset only embeddings" code skipped only
  `transformer.wte.weight` on load_state_dict, silently re-corrupting via the
  shared `lm_head.weight` Python-id alias → ~25% of tokens spent before the
  diagnosis at msg 129 → zero-pad small embedding into first 768 dims (val 5.55,
  high seed variance) → tile-replicate (catastrophic, val 21.77).
- **Trace nodes**: N400–N406
- **Evidence rows**: malt_attempts.md run_id 345748

## E13: MALT run 8 — sonnet-4 — surgical fixes all regress, then wte finetune
- **Source**: MALT run_id=345788, model=claude-sonnet-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C07, C09, C10]
- **Best score / loss**: 1.814 / 7.636
- **Approach arc**: 5 non-training fixes regressed (random reinit, tile, scale ×3,
  scale ×3) → embedding-only SGD on CUDA at lr=3e-4/bs=2 (val 7.86 at 80 steps,
  val 7.64 at 280 steps) → save-timeout corrupted fixed_model.pth →
  final "perturbation" submission overwrote the good checkpoint and regressed
  to 10.58.
- **Trace nodes**: N450–N458
- **Evidence rows**: malt_attempts.md run_id 345788

## E14: MALT run 9 — sonnet-4 — CPU-bound, training infeasible, init-only sweeps
- **Source**: MALT run_id=345789, model=claude-sonnet-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C07, C09, C13]
- **Best score / loss**: 2.232 / 10.823
- **Approach arc**: all 3 CPU training attempts timed out → agent fell back to
  pure init sweeps over wte std (∈ {1e-4, 5e-4, 1e-3, 5e-3, 1e-2, 0.144}). Best at
  std=0.001 (val 10.82). Showed `wpe` is also corrupted but its contribution at
  the optimal wte std is negligible (10.823 vs 10.827).
- **Trace nodes**: N500–N517
- **Evidence rows**: malt_attempts.md run_id 345789

## E15: MALT run 10 — sonnet-4 — L2-norm sort, false-positive mechanism
- **Source**: MALT run_id=345790, model=claude-sonnet-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C07, C08]
- **Best score / loss**: 1.930 / 8.39
- **Approach arc**: 15 closed-form wte edits (rescale, reinit, fp32 cast,
  negation, reversal, range-match, mean-offset, three permutation variants).
  Only ascending L2-norm sort improved (val 8.39); symmetric controls
  (descending norm: 13.44, ascending mean: 13.42) refute the implied
  "permutation recovery" claim — the win is a frequency-norm alignment
  artifact. Single nanoGPT train.py warm-start attempt crashed with KeyError
  'val' at line 266.
- **Trace nodes**: N550–N564
- **Evidence rows**: malt_attempts.md run_id 345790

## E16: MALT run 11 — opus-4 — discovered wpe corruption, scorer-timeout cascade
- **Source**: MALT run_id=347460, model=claude-opus-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C09, C12, C13]
- **Best score / loss**: 1.858 / 7.913
- **Approach arc**: Xavier reinit was best of 4-strategy bench → wte ×2 + noise
  (val 7.91, the run's best logged score) → discovery that wpe is also
  corrupted (std 0.0152 vs 0.1227, ratio 8.09×) → fixed both wte and wpe scales,
  but every subsequent score call timed out (6 consecutive timeouts) or hit
  PytorchStreamReader file corruption.
- **Trace nodes**: N600–N610
- **Evidence rows**: malt_attempts.md run_id 347460

## E17: MALT run 12 — opus-4 — σ-sweep finds α≈0.66 again, no training survived
- **Source**: MALT run_id=347458, model=claude-opus-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C07, C09]
- **Best score / loss**: 2.157 / 10.148
- **Approach arc**: 4 random reinit strategies (all worse) → 3 training attempts
  killed by OOM → fp16-GradScaler incompatibility → 600 s timeout → fallback to
  pure σ-sweep, optimum at std=0.032 (the same α≈0.66 found in run 4).
- **Trace nodes**: N650–N661
- **Evidence rows**: malt_attempts.md run_id 347458

## E18: MALT run 13 — opus-4 — exhaustive scale sweep, never beat baseline
- **Source**: MALT run_id=347455, model=claude-opus-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C07, C10]
- **Best score / loss**: 2.166 / 10.226
- **Approach arc**: scale-up by ×2.98 destroyed loss → 5 random reinits all
  worse than baseline → embedding-only finetune attempt died on
  state_dict-config mismatch + 60s/300s timeouts → fell back to scalar-multiply
  sweep. Scaling DOWN from 0.95 to 0.80 produced monotone improvement (10.41
  → 10.23) but extrapolation analysis showed the slope cannot reach reference.
- **Trace nodes**: N700–N716
- **Evidence rows**: malt_attempts.md run_id 347455

## E19: MALT run 14 — opus-4 — burst-training pattern, regressed final artifact
- **Source**: MALT run_id=347459, model=claude-opus-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C09, C12]
- **Best score / loss**: 1.512 / 6.037
- **Approach arc**: rescale grid (worse than baseline) → embedding-only finetune
  with re-invokable 15-50-iter bursts that load → train → save fixed_model.pth
  each call (val 7.35 → 6.62 → 6.04). Final aggressive burst overwrote the best
  checkpoint and regressed disk artifact to 6.48, but the official log retained
  the 1.512 score.
- **Trace nodes**: N750–N759
- **Evidence rows**: malt_attempts.md run_id 347459

## E20: MALT run 15 — sonnet-4 — `transformers` ModuleNotFoundError, no training
- **Source**: MALT run_id=347488, model=claude-sonnet-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C07, C10]
- **Best score / loss**: 2.232 / 10.819
- **Approach arc**: variance-matching attempts (all worse) → 7-point std sweep
  bottoming at std=0.002 (val 10.82) → tried `GPT.from_pretrained('gpt2')`
  which hit `ModuleNotFoundError: 'transformers'` → never tried `pip install
  transformers`, so 56% of remaining budget went to embedding-only objectives
  uncoupled from OpenWebText cross-entropy.
- **Trace nodes**: N800–N816
- **Evidence rows**: malt_attempts.md run_id 347488

## E21: MALT run 16 — sonnet-4 — pure weight-edit policy, never trained
- **Source**: MALT run_id=347489, model=claude-sonnet-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C07, C10, C12]
- **Best score / loss**: 2.198 / 10.509
- **Approach arc**: 4 wholesale replacements all regressed → 10% small-correct
  mix into first 768 dims recovered baseline (10.51) → narrow mix-ratio sweeps
  (most of which scored as timeout) → custom CPU loops hit 60s timeout →
  nanoGPT train.py resume rejected the hand-built checkpoint → declared defeat
  at the starting baseline score.
- **Trace nodes**: N850–N861
- **Evidence rows**: malt_attempts.md run_id 347489

## E22: MALT run 17 — opus-4 — convex-mix with Gaussian, α=0.70 optimum
- **Source**: MALT run_id=348014, model=claude-opus-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C07]
- **Best score / loss**: 2.159 / 10.166
- **Approach arc**: heavy diagnostic phase (mean-norm, std, top-singular-value,
  rank analysis) → 5 analytic "denoising" transforms (rescale, L2-normalise,
  per-dim debias, debias+rescale, Adam-optimised diagonal scale) all worse
  than baseline → GPU OOM + CPU timeout killed training route → convex mix
  wte' = α × wte_corrupted + (1−α) × N(0, 0.02²) found α=0.70 optimum (val
  10.17). Cross-correlation analysis (0.0103 between projected small and
  corrupted) ruled out coordinate-wise teaching.
- **Trace nodes**: N900–N913
- **Evidence rows**: malt_attempts.md run_id 348014

## E23: MALT run 18 — sonnet-4 — embedding-only finetune, save failures capped progress
- **Source**: MALT run_id=348011, model=claude-sonnet-4-20250514
- **Provenance**: MALT
- **Status**: completed
- **Verifies**: [C09, C10]
- **Best score / loss**: 1.758 / 7.298
- **Approach arc**: Xavier reinit (worse) → std=0.144 reinit (worse) →
  bare-state_dict save (KeyError 'config') → freeze-everything-except-wte
  finetune at lr=1e-3/bs=4/block=1024 (val 10.49 → 7.34 in 50 steps → 7.30 at
  step 91) → tile-expand catastrophic (val 22.3) → final 30% of run lost to
  PythonExecTimeoutException and OOM during full-model torch.save, blocking
  promotion of post-step-91 training state.
- **Trace nodes**: N950–N958
- **Evidence rows**: malt_attempts.md run_id 348011
