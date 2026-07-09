---
type: experiments
paper: nanogpt-speedrun
---

# Experiments

## E01 — Per-Record Agent Reproduction
- **Tests**: C02, C06, C08, C09
- **Setup**: For each record N ∈ {1..20}, agent starts from record N's `train_gpt2.py` and attempts to reproduce record N+1's speedup.
- **Variables**: Model (4 frontier LLMs) × hint_level (0,1,2,3,z) × search_strategy (Flat, Tree, Forest, AIDE, Multi-AIDE)
- **Procedure**: Agent runs BoNScienceRunner with budget of 20 iterations. Success = achieves target train_time with val_loss ≤ 3.28.
- **Metrics**: Gap recovered (primary), success rate (binary), number of iterations to best result, bug rate.
- **Expected**: No model achieves full success on any record with level ≥ 1 hints. Directional: gap_recovered decreases with record number.
- **Hardware**: 8×H100 80GB per trial, SLURM cluster.

## E02 — Search Strategy Comparison
- **Tests**: C07
- **Setup**: Fix model and hint level; compare 5 search strategies on same records.
- **Procedure**: Run all strategies with identical compute budget (20 iterations × branch_factor). Compare gap_recovered distributions.
- **Metrics**: IQM of gap_recovered, per-record rankings.
- **Expected**: BoN tree/forest strategies achieve higher IQM than linear AIDE.
- **Dependencies**: [E01]

## E03 — Hint Level Ablation
- **Tests**: C09
- **Setup**: Fix model and search strategy; vary hint level from z (no hints) through 3,2,1.
- **Procedure**: Compare agent performance across hint levels on same records.
- **Metrics**: Gap_recovered difference between hint levels.
- **Expected**: Marginal improvement from more detailed hints, especially for implementation-heavy records.
- **Dependencies**: [E01]

## E04 — Bug Analysis
- **Tests**: C06
- **Setup**: Classify all agent failures from E01 into error categories.
- **Procedure**: Parse agent workspace logs. Categorize bugs: distributed training errors, CUDA/compile errors, numerical precision, wrong optimization direction, timeout.
- **Metrics**: Proportion of each error category.
- **Expected**: >70% of failures are implementation bugs, <20% are wrong direction.
- **Dependencies**: [E01]

## E05 — Model Comparison
- **Tests**: C02
- **Setup**: Fix search strategy and hint level; compare 4 frontier models.
- **Procedure**: Aggregate gap_recovered across records per model.
- **Metrics**: IQM of gap_recovered per model, pairwise rankings.
- **Expected**: No model achieves consistent success. Relative ranking may vary by record category (optimizer vs. architecture vs. systems).
- **Dependencies**: [E01]

## E06 — Cumulative Optimization
- **Tests**: C01, C05
- **Setup**: Agent starts from Record 1 and attempts multiple sequential optimizations.
- **Procedure**: After each successful (or best-effort) optimization, agent continues from its best version to attempt the next record.
- **Metrics**: Total wall-clock reduction achieved, number of records where meaningful progress is made.
- **Expected**: Compounding errors prevent progress beyond first few records.
- **Dependencies**: [E01]

## E07 — Additional Knowledge Impact
- **Tests**: C09
- **Setup**: Supplement standard hints with external documentation (flex_attn.md, muon.md).
- **Procedure**: Compare agent performance with and without additional knowledge documents.
- **Metrics**: Gap_recovered difference.
- **Expected**: External docs help on records requiring unfamiliar APIs (FlexAttention, Muon) but not on general systems engineering.
- **Dependencies**: [E01, E03]
