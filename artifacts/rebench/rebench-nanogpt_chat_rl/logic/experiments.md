# Experiments

## E01: Train mode end-to-end on 2 × H100
- **Verifies**: C01, C05
- **Status**: completed
- **Source**: official-solution
- **Setup**:
  - Hardware: 2 × H100 (`manifest.yaml:13-17`).
  - Input: `gpt2-xl` (loaded via `GPT.from_pretrained`), Alpaca prompts at
    `/home/agent/prompts.jsonl`.
  - System: PyTorch 2.4.1, transformers 4.44.2, tiktoken 0.7.0, replicate 0.32.1.
- **Procedure**:
  1. Load `gpt2-xl` via `GPT.from_pretrained` (`model.py:249-329`).
  2. Run `rl_finetune_best_of_n.py` in `mode="train"`: 4 steps, each step samples
     2048 prompts, generates 8 candidates per prompt, runs pairwise tournament
     selection via `evaluate_n`, fine-tunes on the winners with
     `train_only_response=True`.
  3. Save final model to `/home/agent/finetuned_model` (`model.py:444-445` save format).
  4. Score via `score.py` (held-out Alpaca prompts vs `gpt2-xl` and `gpt2-alpaca`).
- **Metrics**: `mean(win_vs_gpt2-xl, win_vs_gpt2-alpaca)`.
- **Expected/actual outcome**: Final score reaches the official reference; no
  exact numbers in this file (see evidence).
- **Baselines**: starting score (untrained gpt2-xl on the same scorer);
  `gpt2-alpaca` as one of the two references.
- **Evidence output**: `evidence/tables/reference_scores.md`.
- **Dependencies**: none.

## E02: Best-of-2 vs best-of-8 ablation (implied delta in notes.md)
- **Verifies**: C02
- **Status**: explored-not-shipped
- **Source**: official-solution (inferred from `notes.md:2` "previously selected
  only among 2"; the prior best-of-2 configuration is documented as the base
  solution, not as a re-run by the official solution author).
- **Setup**: Same as E01 but with `best_of=2` instead of `best_of=8` and a single
  pairwise judge call per prompt instead of a tournament.
- **Procedure**: Set `best_of=2` in `rl_finetune_best_of_n.py:35`, leave other
  hyperparameters at their `train` mode values, run end-to-end and score.
- **Metrics**: same as E01.
- **Expected/actual outcome**: Final win-rate below the best-of-8 result; the
  base-solution recipe corresponds to this configuration. Not run by the
  official solution author as a standalone ablation, so no quantitative
  comparison is recorded.
- **Baselines**: best-of-8 (E01).
- **Evidence output**: pending.
- **Dependencies**: E01.

## E03: Distribution-alignment verification
- **Verifies**: C03
- **Status**: completed (implicitly, by code-path inspection)
- **Source**: official-solution
- **Setup**: Single end-to-end run; no parameter sweep.
- **Procedure**:
  1. Inspect `model.GPT.generate_strings_autobatch` (`model.py:369-402`):
     `temperature`, `top_k`, `max_new_tokens` are unconditionally overridden
     inside the method body to `0.7, 8, 20` respectively.
  2. Confirm `rl_finetune_best_of_n.py:91-99` calls
     `model.generate_strings_autobatch(... temperature=0.7, top_k=10, ...)`
     but the in-method override clamps `top_k` to `8` regardless.
  3. Score via the standard `score.py` entry which goes through the same model
     class — same overrides apply.
- **Metrics**: code-path equality; no numeric metric.
- **Expected/actual outcome**: Trainer and scorer share identical generation
  parameters; verified.
- **Baselines**: none.
- **Evidence output**: not-applicable (code-path observation).
- **Dependencies**: none.

## E04: Final scoring of the official solution
- **Verifies**: C01, C05
- **Status**: completed
- **Source**: official-solution (README-recorded; no `score.log` shipped with the
  official_solution directory)
- **Setup**: 2 × H100, `gpt2-xl` initialised from HuggingFace, Replicate API for
  Llama-3-8b judge calls.
- **Procedure**: After E01 completes, the held-out Alpaca prompt set is fed to
  the final model; `mean(win_vs_gpt2-xl, win_vs_gpt2-alpaca)` is recorded.
- **Metrics**: mean win-rate.
- **Expected/actual outcome**: matches `0.85` per README:23.
- **Baselines**: starting score `0.54` (README:22); best human `0.97` (README:45).
- **Evidence output**: `evidence/tables/reference_scores.md`,
  `evidence/tables/human_baselines.md`.
- **Dependencies**: E01.
