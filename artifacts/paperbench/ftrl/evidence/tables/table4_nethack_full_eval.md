---
# Table 4: NetHack Full Evaluation Results

**Source**: Table 4, Appendix D
**Caption**: NetHack full evaluation results on last checkpoint of each run for 1000 episodes.

| method | score | turns | steps | dlvl | xplvl | eating | gold | scout | sokoban | staircase |
|--------|-------|-------|-------|------|-------|--------|------|-------|---------|-----------|
| From scratch | 776 | 6696 | 13539 | 1.06 | 4.07 | 5862.56 | 5.34 | 370.62 | 0.00 | 25.17 |
| Fine-tuning | 647 | 7756 | 13352 | 1.02 | 2.73 | 7161.20 | 9.26 | 149.70 | 0.00 | 19.94 |
| Fine-tuning + EWC | 3976 | 16725 | 35018 | 1.41 | 6.29 | 15896.45 | 217.12 | 719.70 | 0.00 | 81.74 |
| Fine-tuning + BC | 7610 | 22895 | 34560 | 1.70 | 7.30 | 21995.63 | 582.33 | 959.34 | 0.00 | 69.89 |
| Fine-tuning + KS | 10588 | 24436 | 38635 | 2.66 | 7.73 | 23705.56 | 857.20 | 1551.18 | 0.04 | 90.10 |

## Notes
- All metrics are mean values over 1000 episodes from the last checkpoint
- **score**: In-game NetHack score (primary metric)
- **turns**: Number of in-game turns
- **steps**: Number of environment steps
- **dlvl**: Maximum dungeon level reached
- **xplvl**: Experience level
- **eating/gold/scout/sokoban/staircase**: Sub-task scores (NLE defined tasks; Küttler et al., 2020)
- Fine-tuning + KS achieves the highest score (10588) and outperforms all other methods on all metrics
- Vanilla fine-tuning (647) performs below training from scratch (776) — confirming catastrophic FPC
- The pre-trained baseline (Tuyls et al., 2023) achieves ~5218 (not shown here; see Table 5)
