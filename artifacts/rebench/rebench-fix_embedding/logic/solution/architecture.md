# Architecture

Source: `official_solutions/ai_rd_fix_embedding/official_solution/model_adapted.py`

## Component Graph (Stages 1–2: adapter present)

```
token ids (int64[B, T])
        |
        v
[wte]  (nn.Embedding, V × d_small)     ← frozen copy of small model's embedding in Stage 1
        |   (output shape: [B, T, d_small])
        v
[adapter]  (nn.Linear, d_small × d_large, bias=False)   ← only trainable module in Stage 1
        |   (output shape: [B, T, d_large])
        v
[wpe]  (nn.Embedding, block_size × d_large) +
        |
        v
[drop] → [h.0 ... h.N-1]  (12 transformer blocks, d_large-wide)
        |
        v
[ln_f] → [lm_head]  (weight-tied to wte: weight ∈ R^{V × d_small})
        |
        v
logits (float[B, T, V]) via  (lm_head.weight · adapterᵀ · hidden)
```

Because `wte.weight` and `lm_head.weight` are the same tensor (tied embeddings), the
adapter participates in the output path symmetrically: `logits_j = (E_small A)[j, :] · h`
rather than `E_large[j, :] · h`.

## Component Graph (Stage 3: baked, adapter absorbed)

```
token ids → [wte]  (nn.Embedding, V × d_large)   ← wte_baked = E_small · A
                |
                v
            [wpe] → [drop] → [h.0 ... h.N-1] → [ln_f] → [lm_head]   (vanilla GPT)
                                                            ↑
                                                        tied to wte (d_large)
```

Architecture is now identical to the original uncorrupted GPT — no adapter, no
`d_small` bottleneck, but with the adapter's learned alignment folded into the
embedding matrix.

## Class Surface

```
model_adapted.GPTConfig(dataclass)
  - block_size, vocab_size, n_layer, n_head, n_embd, dropout, bias
  - embedding_size            ← NEW field (d_small); absent in model_vanilla.GPTConfig
  - init_from_two: bool       ← triggers init_from_small_and_big path
  - only_train: str | None    ← param-name filter for configure_optimizers

model_adapted.GPT(nn.Module)
  - transformer: nn.ModuleDict
      - wte: nn.Embedding(V, d_small)
      - wpe: nn.Embedding(block_size, d_large)
      - drop, h (list of Block), ln_f
  - adapter: nn.Linear(d_small, d_large, bias=False)
  - lm_head: tied to transformer.wte (model_adapted.py:161-163)

  Key methods:
  - init_from_small_and_big(small_path, large_path)   (model_adapted.py:178-192)
      loads small model wte into transformer.wte, large model blocks into h,
      initializes adapter with default PyTorch Linear init.
  - save_with_baked_adapter(path)                     (model_adapted.py:194-204)
      computes wte_baked = einsum("vs,bs->vb", wte.weight, adapter.weight),
      saves a model_vanilla.GPT checkpoint.
  - configure_optimizers(..., only_train=...)         (model_adapted.py:226-256)
      if only_train is set, excludes all params whose name does not start with that string.
  - forward(idx, targets=None)
      wte(idx) → adapter(...) → + wpe(pos) → blocks → ln_f → lm_head (via tied wte+adapter).
```

## Checkpoint Contents

| Checkpoint | Architecture | Key Tensors |
|------------|--------------|-------------|
| `large_model.pth` (given) | vanilla GPT | permuted `wte.weight` ∈ R^{V × d_large} |
| `small_correct_model.pth` (given) | vanilla GPT (small) | clean `wte.weight` ∈ R^{V × d_small} |
| `adapter_only.pth` | adapted GPT | small `wte` (frozen), random-init-trained `adapter`, frozen large blocks |
| `adapter_all.pth` | adapted GPT | small `wte`, trained `adapter`, fine-tuned large blocks |
| `baked.pth` | vanilla GPT | `wte_baked` = E_small · A (no adapter stored) |
| `fixed_model.pth` (output) | vanilla GPT | fine-tuned `wte_baked` + fine-tuned blocks |

## Call Paths

```
train_adapted.py main
  ├─ read config
  ├─ if init_from_two:
  │     model = model_adapted.GPT.init_from_small_and_big(small_path, large_path)
  ├─ elif bake:
  │     prev = load(adapter_all.pth)  # model_adapted.GPT
  │     prev.save_with_baked_adapter("baked.pth")
  │     model = model_vanilla.GPT.from_pretrained("baked.pth")
  └─ else:
        model = model_adapted.GPT.from_pretrained(init_from)  # adapter_only.pth → adapter_all
  ├─ model.configure_optimizers(weight_decay, lr, betas, only_train=cfg.only_train)
  └─ standard nanoGPT training loop  (AdamW, cosine schedule, bfloat16 autocast)
```

## Why `wte` Is the Small Embedding (not the Large Permuted One)

The corrupted large embedding is not a usable content source: its rows are shuffled, so
no matter what adapter you apply on top, row `v` of the effective embedding would still
be the permuted row for some other token. The small model's embedding *is* usable
content, so it becomes the content source; the adapter then projects it to the large
model's hidden dimension. The large permuted embedding is discarded at Stage-1 init
(`model_adapted.py:178-192`) and only reenters the training data as the `wte_baked`
matrix after bake, at which point it has been fully replaced by `E_small · A`.
