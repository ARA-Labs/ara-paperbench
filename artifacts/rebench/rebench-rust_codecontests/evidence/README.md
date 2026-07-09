# Evidence Index

| File | Description | Key refs |
|------|-------------|---------|
| [tables/reference_scores.md](tables/reference_scores.md) | Starting / reference / best-human / best-MALT, with score.log cross-check and the README 165-vs-175 note | C01, C05, C12 |
| [tables/human_baselines.md](tables/human_baselines.md) | 14 human baseline runs from README:38-51 | C01 |
| [tables/malt_attempts.md](tables/malt_attempts.md) | MALT attempts across 22 runs (12 Claude-4 primary + 10 Claude-3.7-Sonnet supplement) — populated in Phase 3 | C11, C12 |

## Notes

- `reference_scores.md` records both the README reference (`0.13`, rounded) and
  the score.log value (`0.12727272727272726 = 21/165`).
- `malt_attempts.md` uses the **degenerate-metric header form** per PIPELINE.md §4:
  a single `score` column plus a prose `n_successes / n_problems` auxiliary.
- All MALT rows carry `source: MALT run_id={id} model={model}` provenance with
  `stream: primary` or `stream: supplement` in the trace YAML.
