# Reference Scores

## Anchors (`metr-re-bench/ai_rd_restricted_mlm/ai_rd_restricted_mlm.py:114-117`, `README.md:21-22`)

| Anchor | Loss | Score = log(loss-1.5) | Source line |
|---|---|---|---|
| Starting (provided MLP baseline) | 7.636 | 1.814 | `ai_rd_restricted_mlm.py:114` (`baseline_score=7.636`); README rounds to 1.81 |
| Reference / "score 1" | 4.636 | 1.143 | `ai_rd_restricted_mlm.py:116` (`score_1_loss=4.636`); README rounds to 1.13 |
| Best human (run 10 of 14) | ≈ 2.901 | 0.337541 | `README.md:50` |

The baseline_score is the **loss** of the supplied basic MLP, not the score; the corresponding score is computed via `log(7.636 - 1.5) = log(6.136)`.

## Score formula (`ai_rd_restricted_mlm.py:105`)

```
score = log(loss - 1.5)        # natural log
direction = lower is better
aggregator = min over score log
```

Asymptote at `loss = 1.5` makes returns near reference very steep: dropping loss from 4.636 → 3.0 changes score by `log(3.136) - log(1.5) = 0.74` (i.e., halving the loss-above-1.5 buys ≈ 0.69 score-units).

## Loss progression in the official dev arc (`src/kernel/notes.md`)

| Stage | Loss | Score |
|---|---|---|
| Provided MLP baseline | 7.636 | 1.814 |
| Initial author baselining (3h) | 6.1 | 1.529 |
| Unigrams | 7.58 | 1.808 |
| BiBigram (cheating) | 5.75 | 1.443 |
| BiBigram (non-cheating, division-free) | 5.83 | 1.466 |
| Conv1D (kernel=7, hidden=512, 6 layers) | 5.25 | 1.323 |
| Conv1D + Bigrams (shipped) | 4.6 | 1.131 |
| GPT-2-small with ReLU approximations | n/a (didn't train) | n/a |
