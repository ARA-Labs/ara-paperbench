---
source: "NanoGPT Speedrun leaderboard + workspace_templates/nanogpt_speedrun/"
claims_verified: [C01, C03, C05, C10]
---

# Table 1: NanoGPT Speedrun Progression (21 Records)

| Record | Time (ms) | Time (min) | Steps | Val Loss | Key Optimization | Phase |
|--------|-----------|------------|-------|----------|-----------------|-------|
| 1 | 2,968,348 | 49.47 | 24,576 | 3.2766 | Baseline: standard GPT-2 124M, AdamW, learned PE | — |
| 2 | 2,209,926 | 36.83 | 9,536 | 3.2603 | RoPE, trapezoidal LR, grad norm scaling, BS 32→64 | Optimizer |
| 3 | 1,386,147 | 23.10 | 7,000 | 3.2813 | **Muon optimizer** (OrthogonalNesterov + AdamW hybrid) | Optimizer |
| 4 | 1,301,740 | 21.70 | 6,200 | 3.2772 | Muon refinements: QKV split, unit variance, no warmup | Optimizer |
| 5 | 949,528 | 15.83 | 5,100 | 3.2751 | ReLU², padded vocab, zero-init, QK norm, 6 heads | Architecture |
| 6 | 766,259 | 12.77 | 5,100 | 3.2750 | Distributed Muon, CUDA 12.5 upgrade | Architecture |
| 7 | 773,072 | 12.88 | 5,100 | 3.2760 | Untied embed/head, RMSNorm, 3 optim groups, cuDNN attn | Architecture |
| 8 | 662,205 | 11.04 | 4,578 | 3.2789 | U-Net skip connections, momentum warmup, logit softcap | Architecture |
| 9 | 505,531 | 8.43 | 3,200 | 3.2785 | bfloat16 via CastedLinear, remove autocast | Precision |
| 10 | 477,150 | 7.95 | 3,200 | 3.2782 | Refined U-Net, doubled LRs, optimized Newton-Schulz | Precision |
| 11 | 442,985 | 7.38 | 3,242 | 3.2742 | **FlexAttention**: 64K context, doc-aware masking, SW 1024 | Attention |
| 12 | 317,839 | 5.30 | 1,875 | 3.2739 | Block mask opt, async all_gather, pinned memory DL | Attention |
| 13 | 289,805 | 4.83 | 1,750 | 3.2739 | Value token embeddings, sequence parallelism | Advanced |
| 14 | 273,107 | 4.55 | 1,530 | 3.2739 | Muon restructuring, size-based param groups | Advanced |
| 15 | 241,463 | 4.02 | 1,480 | 3.2771 | GQA, gradient_as_bucket_view, block SW 128 | Advanced |
| 16 | 232,971 | 3.88 | 1,480 | 3.2773 | Sparse value embeddings, removed layer 8, RoPE truncation | Advanced |
| 17 | 220,374 | 3.67 | 1,490 | 3.2739 | Logit softcap 30→15, microbatching, dynamic SW | Advanced |
| 18 | 211,840 | 3.53 | 1,390 | 3.2770 | **FP8 linear head**, sigmoid logit offset, LR floor | Hardware |
| 19 | 199,442 | 3.32 | 1,395 | 3.2770 | Merged QKV, long-short SW, attention scale, batched Muon | Hardware |
| 20 | 188,680 | 3.14 | 1,393 | 3.2739 | Train 48K/val 256K, FP8 scale tuning | Hardware |
| 21 | 184,262 | 3.07 | 1,770 | 3.2739 | Final record | Hardware |

## Phase Summary

| Phase | Records | Start (min) | End (min) | Reduction | Cumulative Speedup |
|-------|---------|-------------|-----------|-----------|-------------------|
| Optimizer | 2-4 | 49.47 | 21.70 | 56.2% | 2.3× |
| Architecture | 5-8 | 21.70 | 11.04 | 49.1% | 4.5× |
| Precision | 9-10 | 11.04 | 7.95 | 28.0% | 6.2× |
| Attention | 11-12 | 7.95 | 5.30 | 33.3% | 9.3× |
| Advanced | 13-17 | 5.30 | 3.67 | 30.8% | 13.5× |
| Hardware | 18-21 | 3.67 | 3.07 | 16.3% | 16.1× |
