---
type: task_config
paper: nanogpt-speedrun
---

# Task Configuration & Scoring

## NanoGPT Speedrun Scoring

| Property | Value | Notes |
|----------|-------|-------|
| Target model | GPT-2 124M parameters | Standard architecture as baseline |
| Dataset | FineWeb-Edu 10B tokens | Pre-tokenized with GPT-2 tokenizer |
| Val loss threshold | <= 3.28 | Cross-entropy on held-out validation split |
| Hardware | 8x H100 80GB SXM5 + NVLink | Fixed, single-node |
| Metric | Wall-clock training time (ms) | End-to-end including data loading, compilation, checkpointing |
| Timing | Single run, no ensembling | One execution per record submission |
| Code constraint | Single `train_gpt2.py` file | All logic in one script |

## Fraction of Speedup Recovered (FSR)

The primary agent evaluation metric. For record transition i -> i+1:

```
FSR_i = (t_i - t'_{i+1}) / (t_i - t_{i+1})
```

Where:
- `t_i` = human record i training time (starting point)
- `t_{i+1}` = human record i+1 training time (target)
- `t'_{i+1}` = agent's best achieved training time

| FSR Value | Interpretation |
|-----------|---------------|
| 1.0 | Agent fully reproduces the human record |
| 0.0 | Agent makes no improvement over baseline |
| < 0.0 | Agent's code is slower than the baseline (capped to 0 in reporting) |
| > 1.0 | Agent discovers a faster solution than the human record |

Aggregated across records using Interquartile Mean (IQM) for robustness to outliers.

## Record Transition Tasks

19 valid transitions (Record 16->17 excluded as it was a PyTorch version upgrade only):

| Transition | Start Time (ms) | Target Time (ms) | Speedup Gap (ms) | Innovation Category |
|-----------|-----------------|-------------------|-------------------|---------------------|
| R1->R2 | 2,968,348 | 2,209,926 | 758,422 | Optimizer (RoPE, LR schedule) |
| R2->R3 | 2,209,926 | 1,386,147 | 823,779 | Optimizer (Muon) |
| R3->R4 | 1,386,147 | 1,301,740 | 84,407 | Optimizer (Muon tuning) |
| R4->R5 | 1,301,740 | 949,528 | 352,212 | Architecture (ReLU², vocab, heads) |
| R5->R6 | 949,528 | 766,259 | 183,269 | Architecture (distributed Muon) |
| R6->R7 | 766,259 | 773,072 | -6,813 | Architecture (untied embed) |
| R7->R8 | 773,072 | 662,205 | 110,867 | Architecture (U-Net skip) |
| R8->R9 | 662,205 | 505,531 | 156,674 | Precision (bfloat16) |
| R9->R10 | 505,531 | 477,150 | 28,381 | Precision (refined U-Net, LR) |
| R10->R11 | 477,150 | 442,985 | 34,165 | Attention (FlexAttention) |
| R11->R12 | 442,985 | 317,839 | 125,146 | Attention (block mask opt) |
| R12->R13 | 317,839 | 289,805 | 28,034 | Advanced (VTE, seq parallel) |
| R13->R14 | 289,805 | 273,107 | 16,698 | Advanced (Muon restructure) |
| R14->R15 | 273,107 | 241,463 | 31,644 | Advanced (GQA, sliding window) |
| R15->R17 | 241,463 | 220,374 | 21,089 | Advanced (softcap, microbatch) |
| R17->R18 | 220,374 | 211,840 | 8,534 | Hardware (FP8 head) |
| R18->R19 | 211,840 | 199,442 | 12,398 | Hardware (merged QKV) |
| R19->R20 | 199,442 | 188,680 | 10,762 | Hardware (seq len tuning) |
| R20->R21 | 188,680 | 184,262 | 4,418 | Hardware (final tuning) |

## Agent Benchmark Rules

1. **Single-file constraint**: Agent may only modify `train_gpt2.py` (the single training script)
2. **No internet access**: Agent cannot fetch external resources beyond provided hints
3. **Fixed compute budget**: Maximum 20 search nodes (M=20) per run
4. **SLURM timeout**: 2x the target record's training time per training execution
5. **Validation protocol**: Success requires val_loss <= 3.28 AND train_time < starting record
6. **Seeds**: 3 seeds per configuration for statistical robustness
7. **Total evaluation budget**: 6,840 agent runs totaling ~55,000 H100-hours
8. **Agent run timeout**: 20 hours total per complete search

## Hint Levels

| Level | Name | Content | Token Count (approx.) |
|-------|------|---------|----------------------|
| z | Zero-knowledge | No hints; agent must identify optimization independently | 0 |
| 3 | Paper | Mini-paper describing the technique with motivation and context | ~2,000 |
| 2 | Description | Natural-language explanation with rationale | ~500 |
| 1 | Pseudocode | Algorithmic pseudocode of the changes | ~300 |
| 0 | Diff | Raw git diff between records (not used in evaluation as it trivializes the task) | varies |
| 9 | External | API documentation (e.g., FlexAttention docs); only available for select records | varies |

Combinations tested: z, L1, L2, L3, L1+L2, L1+L2+L3, L1+L9 (for FlexAttention record).

## In-Bounds vs Out-of-Bounds Optimizations

### In-Bounds
- Algorithmic changes to training loop (optimizers, schedules, loss functions)
- Architecture modifications (layer types, attention patterns, skip connections)
- Precision engineering (mixed precision, FP8, custom dtype management)
- Systems-level optimizations (async communication, memory pinning, kernel fusion)
- Custom CUDA kernels (for operations on fixed H100 hardware)
- Training recipe tuning (batch size, sequence length, steps)

### Out-of-Bounds
- Hardware changes (different GPU count, different GPU type)
- Dataset changes (different tokenization, different data source)
- Evaluation changes (different val_loss threshold, different validation set)
- Multi-run selection (must be a single training run)
- Pre-trained weight initialization (must train from scratch)
