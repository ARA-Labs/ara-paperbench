# Architecture

## Module map

| File | Lines | Role |
|---|---|---|
| `tao_train.py` | 1–129 | Training loop. Imports model classes, constructs `ConvMLMWithBiBigrams`, trains 100k steps, logs to wandb |
| `tao_solution.py` | 1–367 | All 8 model classes + `conv1d_same` helper |
| `measure_unigram_loss.py` | 1–99 | Computes & saves `unigrams.pt`, `bigrams_forward.pt`, `bigrams_backward.pt` over 50257*200 OWT train tokens |
| `gpt2_approximation.py` | 1–469 | Explored-not-shipped: minGPT with piecewise-linear ReLU approximations of softmax/rsqrt/exp/gelu |
| `notes.md` | 1–21 | Author dev log: loss progression 6.1 → 7.58 → 5.75 → 5.25 → 4.6 |

## Class library (`tao_solution.py`)

The author kept all 8 attempted architectures in a single file. Only the last is wired into training.

| Class | Lines | Trainable params | Inherits prior | Role |
|---|---|---|---|---|
| `BiasOnlyMLM` | 6–16 | `(V,)` bias | — | Sanity floor; output independent of input |
| `UnigramMLM` | 19–30 | `(V,)` log-odds | unigrams.pt | Loaded prior, learnable |
| `BiBigramMLMCheating` | 33–46 | bigram tables | bigrams + unigrams | Averages **probabilities** then takes log-odds (uses division → cheating wrt restrictions) |
| `BiBigramMLM` | 49–69 | None (registered as buffers) | bigrams + unigrams | Averages **log-odds** (division-free in forward) |
| `FeedForwardMLM` | 80–119 | dense layers | — | Sequence flattened to `S*hidden_expansion`, dense MLP, project back |
| `MLPMixer` | 122–203 | cross-token + per-token | inverse_stds | Cross-token MLP + per-token MLP (explored-not-shipped) |
| `ConvMLM` | 239–297 | conv up/down | inverse_stds | Residual 1D conv stack; basis of shipped model |
| `ConvMLMWithBiBigrams` | 300–367 | conv up/down + scalar | bigrams + inverse_stds | **Shipped**: `ConvMLM` + frozen `BiBigramMLM` combined by learned scalar |

## Helper: `conv1d_same` (lines 206–236)

Shape-preserving 1D convolution implemented without `torch.nn.Conv1d`:
- `pad = (kernel_size - 1) // 2`
- `padded = F.pad(input, (pad, pad))` (constant pad, no numerical computation)
- `strided = padded.as_strided(size=(B, in_C, L, k), stride=(s0, s1, s2, 1))` — sliding window view
- `output = einsum("bilk,oik->bol", strided, weight)`

## Buffer: `inverse_stds`

Stored as `register_buffer("inverse_stds", torch.ones(num_layers))`. Used by `ConvMLM`, `ConvMLMWithBiBigrams`, and `MLPMixer`. Updated by `update_inverse_stds()` (lines 199–203, 293–297, 363–367), which is called from the training loop and may use division. The forward pass only **multiplies** by entries of this buffer.

## Concurrency / parallelism

Single-process, single-GPU training (`device = "cuda:6"` hard-coded). bf16 mixed precision via `torch.amp.autocast`. Score evaluation runs the model on a held-out OWT validation slice via the framework's score script.

## Why the file layout matters

Keeping `BiasOnlyMLM`, `UnigramMLM`, `BiBigramMLM*`, `FeedForwardMLM`, `MLPMixer`, `ConvMLM`, and `ConvMLMWithBiBigrams` in one file makes the **dev arc legible**: each architecture is a strict superset (in capability terms) of the one before, and the shipped composite is `ConvMLM ⊕ BiBigramMLM` — both visibly present in the same module. A MALT agent without this file structure has to rediscover the entire ladder.
