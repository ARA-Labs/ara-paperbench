# Algorithm

Source: `official_solutions/ai_rd_fix_embedding/official_solution/{official_solution.sh,
train_adapted.py, model_adapted.py, config_adapter_only.py, config_adapter_all.py,
config_baked.py, notes.md}`

## Overview

The official solution is a three-stage curriculum that progressively removes constraints
while growing the trainable parameter set. Each stage uses the previous stage's checkpoint
as initialization, lowers the learning rate, and trains for a longer horizon.

```
Stage 1: adapter-only           →  adapter_only.pth
Stage 2: adapter + all unfrozen →  adapter_all.pth
Stage 3: baked (no adapter)     →  /home/agent/fixed_model.pth   (official output)
```

The unifying idea is that the small uncorrupted model's embedding `E_small` contains
usable content for every token; a linear adapter `A: R^{d_small} → R^{d_large}` aligns
`E_small · A` to the large transformer's input space. Once alignment is good enough for
gradient signal to stop being noise (loss < 5.5), the network can be unfrozen; once it
has fully adapted, `A` can be absorbed into the embedding matrix and the original
architecture restored.

## Stage 1: Adapter-Only (`config_adapter_only.py`)

**Purpose**: Initialize the alignment from random adapter weights without disturbing the
rest of the large model. The adapter is the only trainable parameter.

**Model construction** (`model_adapted.py:178-192`,
`GPT.init_from_small_and_big(small_correct_model.pth, large_model.pth)`):
- Load small uncorrupted model; copy its `wte` (and hence `lm_head` via weight tying)
  into the large model.
- Load corrupted large model; keep its transformer blocks and final `lm_head`, but
  overwrite `wte` with the small model's embedding.
- Insert a fresh `adapter = nn.Linear(embedding_size, n_embd, bias=False)` between the
  embedding output and the transformer input (and equivalently on the output path via
  tied weights).

**Training** (`train_adapted.py`, `config_adapter_only.py`):
- `only_train = "adapter.weight"` → `configure_optimizers` includes only the adapter
  parameters; all other weights are frozen by excluding them from the AdamW parameter list.
- `learning_rate = 1e-3`, `max_iters = 1000`, `warmup_iters = 100`, cosine decay to
  `min_lr = 1e-4`.
- Micro-batch 8, grad-accum 2 → effective batch 16; `block_size = 1024`; bfloat16 autocast.

**Output**: `adapter_only.pth` — checkpoint with trained adapter and original frozen
weights.

## Stage 2: Unfreeze All (`config_adapter_all.py`)

**Purpose**: With alignment already established, let every weight move a little to close
the remaining gap. Learning rate drops 10× to control instability (`notes.md:15`:
"training more parameters generally performs better, as long as there are no instabilities
or problems with scaling").

**Model construction**:
- Load `adapter_only.pth` via the standard `train_adapted.py` resume path
  (`init_from_two = False`, `bake = False`).
- No `only_train` setting → all parameters are trainable.

**Training**:
- `learning_rate = 1e-4`, `max_iters = 2000`; same warmup shape, optimizer, batch, dtype.

**Output**: `adapter_all.pth` — fully fine-tuned adapter + corrupted-turned-corrected
transformer.

## Stage 3: Bake + Continue (`config_baked.py`)

**Purpose**: Remove the `d_small`-dimensional bottleneck by absorbing the adapter into
the embedding matrix, then continue training in the original architecture.

**Pre-step** (`train_adapted.py:183-196`,
`model_adapted.save_with_baked_adapter("baked.pth")`):
1. Load the Stage 2 model.
2. Compute `wte_baked = torch.einsum("vs,bs->vb", model.wte.weight, model.adapter.weight)`
   — this gives a `[V, n_embd]` tensor equivalent to applying the adapter to every row
   of `wte` at once.
3. Construct a fresh `model_vanilla.GPTConfig` (no `embedding_size` field) and a vanilla
   `model_vanilla.GPT`; copy all transformer weights over; set `wte.weight = wte_baked`;
   discard the adapter module.
4. Save to `baked.pth`.

**Training**:
- Load `baked.pth` with `bake = True` (tells `train_adapted.py` to use
  `model_vanilla.GPT` instead of `model_adapted.GPT`).
- `learning_rate = 8e-5`, `max_iters = 4000`.
- All parameters trainable, same optimizer/batch/dtype as Stage 2.

**Output**: `/home/agent/fixed_model.pth` — the final submission. Final logged loss
`2.8917` per `score.log`; score `≈ 0.328`.

## Orchestration (`official_solution.sh`)

Three sequential calls to the same training entry point with different configs:

```bash
python train_adapted.py config_adapter_only.py
python train_adapted.py config_adapter_all.py
python train_adapted.py config_baked.py
```

No data parallel / DDP: the task environment provides a single H100 (`manifest.yaml:13-19`).

## Why Three Stages (not one)

Collapsing to a single end-to-end unfrozen run with random adapter init fails by the same
mechanism that vanilla fine-tuning fails: the transformer would be receiving permuted /
random-adapter-projected inputs and would train its weights to fit noise before the
adapter stabilizes. Stage 1 buys a clean alignment signal before any non-adapter weight
is perturbed; Stage 2 refines under that signal; Stage 3 removes the structural
bottleneck only after the network has committed to using the recovered embedding.
