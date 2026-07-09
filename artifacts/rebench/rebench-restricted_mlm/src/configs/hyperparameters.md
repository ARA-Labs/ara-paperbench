# Hyperparameters (verbatim from `tao_train.py:13-32`)

| Name | Value | Line |
|---|---|---|
| `device` | `"cuda:6"` | 13 |
| `batch_size` | `16` | 15 |
| `sequence_length` | `128` | 16 |
| `vocab_size` | `50257` | 17 |
| `num_steps` | `100_000` | 19 |
| `lr` | `3e-4` | 20 |
| `mask_prob` | `0.15` | 21 |
| `mask_token_id` | `50256` | 22 |
| `num_layers` | `6` | 24 |
| `hidden_dim` | `512` | 25 |
| `hidden_expansion` | `32` | 26 (only used by `FeedForwardMLM`, not the shipped model) |
| `expansion_factor` | `2` | 27 |
| `kernel_size` | `7` | 30 |
| `save` | `False` | 28 |
| `save_file_name` | `"model.pt"` | 33 |
| `run_name` | `"convbigramslearnedmul2"` | 35 |
| precision | `bfloat16 autocast` | 84 |
| optimizer | `torch.optim.AdamW` | 78 |
| grad clip | `1.0` | 119 |
| LR schedule | `lr * min(1, i/100) * cos(i/N * π/4)` | 125-127 |
| logger | `wandb` (project `restricted_mlm`) | 38-42 |

## Model instantiation (line 73)

```python
model = ConvMLMWithBiBigrams(
    vocab_size=50257,
    kernel_size=7,
    hidden_dim=512,
    num_layers=6,
    expansion_factor=2,
    mask_token=50256,
)
```

## Notes
- `hidden_expansion=32` is dead code in the shipped configuration; it is only consumed by `FeedForwardMLM`.
- `save=False` means the trained `model.pt` is **not** persisted by the training script. The shipped flow re-trains end-to-end during scoring.
- The cosine schedule uses a quarter-period (`π/4`), so the LR at step 100 000 is `3e-4 * cos(π/4) ≈ 2.12e-4`, not zero.
- `wandb` is configured but `WANDB_SILENT=true`, so no console output during runs.
