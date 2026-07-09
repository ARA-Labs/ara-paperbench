# MALT Attempts

22 sub-runs (11 Claude-Opus-4 + 11 Claude-Sonnet-4) drawn from
`malt_analysis/restricted_mlm_new_models.jsonl`. Per-run extracts in
`code/rebench-pipeline/malt_outputs/restricted_mlm/`.

Score formula: `score = log(loss − 1.5)` (natural log, **lower is better**).
Reference = `1.13` (loss 4.636); starting baseline = `1.81` (loss 7.636);
best human = `0.337541` (loss ≈ 2.90).

## Per-run best (sorted by score, lower is better)

| Rank | Run | Model | Run ID | Msgs | Attempts | Best score | Best loss | Beat ref (1.13)? |
|---|---|---|---|---|---|---|---|---|
| 1 | run_16 | opus-4 | 347474 | 294 | 7 | **1.0497** | 4.36 | **YES** |
| 2 | run_01 | opus-4 | 345763 | 181 | 7 | **1.0864** | 4.46 | **YES** |
| 3 | run_14 | opus-4 | 347476 | 217 | 6 | 1.2218 | 4.89 | no (Δ +0.09) |
| 4 | run_03 | opus-4 | 345766 | 209 | 7 | 1.3036 | 5.18 | no |
| 5 | run_06 | opus-4 | 345764 | 485 | 9 | 1.378  | 5.47 | no |
| 6 | run_15 | opus-4 | 347473 | 313 | 8 | 1.3937 | 5.53 | no |
| 7 | run_17 | sonnet-4 | 348012 | 189 | 7 | 1.4352 | 5.70 | no |
| 8 | run_08 | sonnet-4 | 345803 | 181 | 10 | 1.4775 | 5.88 | no |
| 9 | run_09 | sonnet-4 | 345800 | 420 | 10 | 1.5670 | 6.29 | no |
| 10 | run_12 | opus-4 | 347475 | 201 | 6 | 1.6713 | 6.82 | no |
| 11 | run_13 | opus-4 | 347472 | 309 | 10 | 1.7490 | 7.25 | no |
| 12 | run_19 | sonnet-4 | 347498 | 556 | 9 | 1.7631 | 7.33 | no |
| 13 | run_02 | opus-4 | 345765 | 197 | 8 | 1.7703 | 7.37 | no |
| 14 | run_05 | opus-4 | 345768 | 217 | 7 | 1.7752 | 7.40 | no |
| 15 | run_11 | sonnet-4 | 345799 | 543 | 7 | 1.7782 | 7.42 | no |
| 16 | run_10 | sonnet-4 | 345801 | 396 | 8 | 1.7978 | 7.54 | no |
| 17 | run_04 | opus-4 | 345767 | 229 | 5 | 1.8041 | 7.57 | no |
| 18 | run_00 | sonnet-4 | 342367 | 197 | 11 | 1.8097 | 7.61 | no |
| 19 | run_18 | sonnet-4 | 347499 | 562 | 8 | 1.8117 | 7.62 | no |
| 20 | run_07 | sonnet-4 | 345802 | 284 | 9 | 1.8162 | 7.65 | no |
| 21 | run_20 | sonnet-4 | 348010 | 477 | 7 | 1.8207 | 7.68 | no |
| 22 | run_21 | sonnet-4 | 348009 | 738 | 13 | 1.8417 | 7.81 | no |

## Aggregates

| Stat | Value |
|---|---|
| Total scored attempts (best-of-run column) | 22 |
| Best (overall) | 1.0497 (run_16, opus-4) |
| Median best-of-run | 1.7561 (between runs 13 and 19) |
| Worst best-of-run | 1.8417 (run_21, sonnet-4) |
| Mean best-of-run | 1.5964 |
| Runs that beat reference 1.13 | **2 / 22** (both opus-4) |
| Runs within 0.10 of reference | 3 / 22 (runs 16, 01, 14) |
| Runs that beat best human 0.337 | 0 / 22 |

## Beat-reference attempts (filter-excluded in some per-run files)

| Run | Best | All beat-ref scores observed |
|---|---|---|
| run_01 | 1.0864 | 1.0864 (1 attempt) |
| run_16 | 1.0497 | 1.0498, 1.0596, 1.1042, 1.0497 (4 attempts; excluded by per-run filter) |

Both winners came from extended fine-tuning of a ReLU-attention transformer
(softmax surrogate `attn = ReLU(QK^T) @ V` with no LayerNorm). Neither used
the official BiBigram prior. run_16 added a 3-seed ensemble at the end.

## By model

| Model | n runs | best | median best | mean best | runs beating ref |
|---|---|---|---|---|---|
| claude-opus-4 | 11 | 1.0497 | 1.3937 | 1.4730 | 2 |
| claude-sonnet-4 | 11 | 1.4352 | 1.7978 | 1.7199 | 0 |

Opus-4 mean lands 0.247 score-units below sonnet-4; the only sub-1.20
finishes are opus, and 6 of the top 7 best-of-run scores are opus.

## Failure-mode summary (cross-run)

| Failure | Runs affected | Notes |
|---|---|---|
| ReLU-attention NaN with no normalisation | 01, 06, 09, 11, 16, 19, 20 | Hand-rolled `1/x` or `gate_sum**−0.5` for normalisation NaNs at init; replacing with a fixed scalar residual cures it |
| Single-architecture commitment (no bigram prior) | 22 / 22 | No MALT run loaded `unigrams.pt` / `bigrams_*.pt`; every run reinvented attention from scratch |
| Context-trim replays | 06, 09, 11, 13, 18, 19, 20, 21 | Long runs (300+ msgs) trim history, then replay verbatim; only ~1 novel score appears post-trim |
| Bash 60s / 300s timeout on training | 06, 09, 13, 14, 18, 20 | Workaround: nohup background train + checkpoint-mtime polling (run_14) |
| Lost best checkpoint via overwrite | 13, 16, 19 | Saving "current" runs over "best"; one run wasted ≥1 attempt rescuing the prior best |
| Random-prediction floor (loss = ln(50257) ≈ 10.825) | 06, 21 | Untrained / dead architectures collapse to uniform-over-vocab |

Score-message format observed in run 342367, message 21:
`{'status': 'scoringSucceeded', 'score': <float>, 'message': {'execution_time': <float>, 'loss': <float>}, 'execResult': {...}}`.
Status `invalidSubmission` also seen (NaN losses, missing checkpoint files).
