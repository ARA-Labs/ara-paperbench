# Heuristics

## Architectural

### H01 — Always start with a strong precomputed prior
The author's loss progression (`notes.md`: 6.1 → 7.58 unigrams → 5.83 bigrams) shows that the bigram tables alone provide more loss reduction than 100k steps of any small neural model trained without them. A single OWT pass to compute `unigrams.pt` + `bigrams_*.pt` is the single highest-ROI move in the entire workflow.
- **Why**: The bigram log-odds are exact statistics over ≈ 10M tokens; gradient descent on a small conv net can only approximate this, and only over many steps.
- **How to apply**: Load and freeze the prior; train the neural component as a residual on top.

### H02 — Keep all 8 architecture variants in one file during exploration
The author keeps `BiasOnlyMLM`, `UnigramMLM`, `BiBigramMLMCheating`, `BiBigramMLM`, `FeedForwardMLM`, `MLPMixer`, `ConvMLM`, `ConvMLMWithBiBigrams` together. Each is a checkpoint along the loss-reduction ladder; the shipped composite is `ConvMLM ⊕ BiBigramMLM`.
- **Why**: Switching the trained model is `model = NewClass(...)` rather than refactoring; ablations are one-line changes.
- **How to apply**: Treat the model file as an architecture catalogue, not a single class.

### H03 — Hide division behind a buffer updated outside forward
`inverse_stds` is updated by an EMA division in the training loop, then *multiplied in* during forward. This implements a LayerNorm-equivalent under "no division in forward".
- **Why**: Pure no-norm conv stacks diverge or stagnate; standard LayerNorm is illegal.
- **How to apply**: Any quantity that "needs" division in forward can be precomputed outside it as long as the value updates slowly relative to inference.

### H04 — Replace `Conv1d` with `pad + as_strided + einsum`
`conv1d_same()` is the canonical recipe under restrictions: no `Conv1d`, no `unfold` (it returns the same view via `as_strided`).
- **Why**: `nn.Conv1d` is not on the allow-list; rolling your own is shape-rigid but legal.
- **How to apply**: For any local-mixing operator, prefer `as_strided` over loops or `gather`.

### H05 — Combine prior and neural model with a single learnable scalar
`bigram_multiplier = nn.Parameter(torch.tensor(1.0))` is the only mixer between the two pathways. Initialised to 1.0 (full bigram contribution at init), it lets gradient descent decide how much to weigh the prior.
- **Why**: A learned vector or layer would risk overfitting; a scalar can only re-weight, never re-shape, the prior's contribution.
- **How to apply**: When fusing a fixed prior with a trainable head, start with one scalar.

## Hyperparameters (from `tao_train.py:13-32`)

| Knob | Value | Justification |
|---|---|---|
| `num_layers` | 6 | Matches what fits in memory at hidden=512, kernel=7 on 2x H100 |
| `hidden_dim` | 512 | Standard small-transformer width; keeps embedding ~25 M params |
| `kernel_size` | 7 | Same value as in `notes.md` "conv1d got 5.25"; odd so `same` padding is symmetric |
| `expansion_factor` | 2 | Halves activation memory vs the typical transformer 4× |
| `batch_size` | 16 | Memory-bound at sequence 128, vocab 50257 logits |
| `sequence_length` | 128 | Task-fixed (`README.md:124`) |
| `lr` | 3e-4 | Karpathy minGPT default |
| `num_steps` | 100 000 | Wall-clock budget under the 8-hour run target |
| `mask_prob` | 0.15 | Task-fixed (BERT default) |
| `mask_token_id` | 50256 | Task-fixed (`README.md:125`) |
| precision | bf16 autocast | H100-friendly; loss is float32 |
| optimizer | AdamW | Default; no weight decay tuning recorded |
| grad_clip | 1.0 | Standard; no isnan recovery beyond `break` |
| LR schedule | warmup 100 → cosine quarter-period | `lr * min(1, i/100) * cos(i/N * π/4)` |

## What was tried and rejected

### H06 — GPT-2 via piecewise-linear approximations does not pay back its slowdown
The minGPT-with-approximations route ran ≈ 23x slower than vanilla GPT-2 and "loss didn't go down in the approximated version over that time" (`notes.md:13-15`). Every additional approximation step (`n_steps=20` in the recorded test) costs throughput and accumulates rounding error.
- **Why**: A 23x slowdown means ≈ 4 350 effective steps in the same wall-clock budget that gave 100 000 steps to ConvMLM.
- **How to apply**: Avoid lifting whole transformer architectures into the restricted set if a simpler restricted-native architecture can carry the prior.

### H07 — MLPMixer was implemented but not shipped
`MLPMixer` (cross-token + per-token MLPs with `inverse_stds` normalisation) was instrumented but never trained in `tao_train.py`. The author's loss numbers in `notes.md` jump straight from "bigrams 5.83" to "conv1d 5.25", consistent with the mixer being scratched before producing a publishable score.
- **How to apply**: Treat the mixer as a fallback if conv kernels prove unstable; don't expect it to beat conv.

## MALT-derived

### H11 — ReLU-attention (`ReLU(QK^T) @ V`) is the only attention surrogate any MALT run beat reference with
Both winning runs (run_16: 1.0497, run_01: 1.0864) used `attn = ReLU(QK^T) @ V` with a small per-layer learned residual scale and *no* normalisation layer. Linear attention without ReLU on the weights (run_16 attempt 4, run_09 attempts 3-5) plateaued ~0.6 score-units worse and was never recovered by depth or width.
- **Why**: ReLU on attention weights enforces non-negativity — the "always non-negative attention mass" property that softmax also has — without needing `exp`. Raw `QK^T` has no such bound and lets attention drift to unbounded magnitudes that then need normalisation the restricted primitive set cannot supply legally.
- **How to apply**: When forbidden `softmax`, prefer `ReLU(QK^T)` over linear attention. Skip LayerNorm: use a fixed scalar residual or trainable per-layer scale instead.

### H12 — Long fine-tune at low lr beats architecture changes once a positional+attention skeleton is in place
Both winning runs spent the bulk of their budget on extended AdamW fine-tunes (run_01: lr=5e-5 cosine ~7858 steps then lr=2e-5→1e-6 cosine ~4000 steps; run_16: 30k-step AdamW push at lr=2e-5). In both cases the final architecture is unchanged from an early checkpoint; only training schedule changed.
- **Why**: Under restricted primitives the architecture search space is small and most variants are unstable; once a stable variant exists, gradient descent has more headroom than design space.
- **How to apply**: Once any non-baseline architecture trains stably, do not iterate the architecture; iterate the optimiser and step count.

### H13 — Background training + checkpoint-mtime polling defeats the 60s/300s bash timeout
Long training runs hit the harness's per-bash-call timeout (60s in run_14, 300s in run_06/13/18/20). The successful workaround in run_14 was to launch training with `nohup python train.py &` and then poll `os.path.getmtime("checkpoint.pt")` from a separate cell to detect when training finished, scoring whichever checkpoint was on disk.
- **Why**: The harness only times the foreground command; backgrounded processes survive across calls.
- **How to apply**: For any training run > 5 min, decouple training from scoring via background-launch + checkpoint polling.

### H14 — Save the "best" checkpoint under a separate filename
Three runs (13, 16, 19) wasted ≥1 attempt because the agent overwrote the best checkpoint by re-running training on the same path. The recovering pattern (run_16) was to save fine-tunes under `*_finetune.pt` and only copy to the scored path after a positive eval.
- **Why**: The harness scores whatever filename is hard-coded in `model.py`; in-place training overwrites that file mid-run.
- **How to apply**: Train to `model_candidate.pt`; eval; only `cp model_candidate.pt model.pt` after confirmed improvement.

### H15 — MALT runs reinvent attention but never load the bigram prior
0 of 22 MALT runs loaded `unigrams.pt` or `bigrams_*.pt`, even though the task starter kit ships `measure_unigram_loss.py` and the same files. The official solution gets ~0.55 loss-units (5.25 → 4.6) from the bigram prior alone (C06). MALT's blind-spot for precomputed-statistics priors is the largest gap between the two streams.
- **Why**: Agents prioritise architectural moves and treat the supplied baseline file as the search starting point, ignoring the rest of the starter kit.
- **How to apply**: For restricted-architecture tasks shipped with measurement helpers, an explicit "list every artefact in the starter kit and decide which to use" step would close the largest known performance gap.
