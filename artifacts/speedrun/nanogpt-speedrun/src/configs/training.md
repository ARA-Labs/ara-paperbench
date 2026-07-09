---
type: training_config
paper: nanogpt-speedrun
---

# Training Configuration

## Model Architecture (Final Record 21)

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| n_layers | 7 (was 12 in baseline) | Reduced after U-Net skip connections compensate |
| n_heads | 6 | 128-dim heads for GPU efficiency |
| n_kv_heads | 3 | GQA (2:1 ratio) from Record 15 |
| d_model | 768 | Standard GPT-2 124M width |
| d_ff | 3072 | 4× expansion |
| vocab_size | 50304 | Padded from 50257 for 64-alignment |
| activation | ReLU² | Faster than GELU, torch.compile friendly |
| position_encoding | RoPE (half-truncated) | From Record 2, truncated in Record 17 |
| normalization | RMSNorm | After embeddings and per-layer |

## Optimizer Configuration (Final)

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| optimizer | Muon (2D) + AdamW (1D, head) | H01: orthogonalize only matrices |
| lr_muon | 0.6 | Doubled in Record 10 |
| lr_adam_head | 0.008 | Separate group for LM head |
| lr_adam_1d | 0.04 | Biases, norms, embeddings |
| momentum | 0.85→0.95 (warmup) | H09: stability with skip connections |
| weight_decay | 0.0 (Muon), 0.01 (AdamW) | |
| grad_clip | 1.0 | Gradient norm scaling |
| newton_schulz_steps | 5 | Convergence vs. compute tradeoff |

## Training Recipe (Final)

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| batch_size | 64 (micro) × 8 (GPUs) | 512 effective |
| seq_length_train | 48K | Reduced from 64K in Record 20 (H10) |
| seq_length_val | 256K | Longer for stable loss estimation |
| total_steps | ~1,400 | Down from 24,576 in baseline |
| lr_schedule | Trapezoidal | From Record 2 |
| precision | bfloat16 (CastedLinear) + FP8 (head) | H05, H08 |
| logit_softcap | 15 (tanh) | Reduced from 30 in Record 17 |

## Agent Benchmark Configuration

| Parameter | Value |
|-----------|-------|
| iterations | 20 |
| branch_factor | 1 (AIDE), 3 (Tree/Forest/Multi-AIDE), 20 (Flat) |
| initial_branches | 1 (Tree), 3 (Forest/AIDE/Multi-AIDE), 20 (Flat) |
| debug_prob | 0.0 (BoN), 0.5 (AIDE/Multi-AIDE) |
| max_bug_depth | 3 |
| slurm_timeout | 2× target train_time |
