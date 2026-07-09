# Figure 5: Main Performance Curves — All Methods vs. All Tasks
- **Source**: Figure 5, Section 6
- **Caption**: "Performance curves of SAPG with respect to PPO, PBT and PQL baselines. On AllegroKuka tasks, PPO and PQL barely make progress and SAPG beats PBT. On Shadow Hand and Allegro Kuka Reorientation and Two Arms Reorientation, SAPG performs best with an entropy coefficient of 0.005 while the coefficient is 0 for other environments. On ShadowHand and AllegroHand, while PQL is initially more sample efficient, SAPG is more performant in the longer run. AllegroKuka environments use successes as a performance metric while AllegroHand and ShadowHand use episode rewards."
- **Axes**: x-axis = Number of env steps (0 to 2e10); y-axis = Episode successes or episode rewards (task-dependent)
- **Methods shown**: SAPG (Ours), PPO, PBT, PQL

## Final Performance at 2e10 Steps (from Table 1, confirmed by Figure 5 endpoints)

| Task | PPO | PBT | PQL | SAPG (λENT=0) | SAPG (λENT=0.005) |
|------|-----|-----|-----|---------------|-------------------|
| Allegro Kuka Regrasping (successes) | 1.25 ± 1.15 | 31.9 ± 2.26 | 2.73 ± 0.02 | 35.7 ± 1.46 | 33.4 ± 2.25 |
| Allegro Kuka Throw (successes) | 16.8 ± 0.48 | 19.2 ± 1.07 | 2.62 ± 0.08 | 23.7 ± 0.74 | 18.7 ± 0.43 |
| Allegro Kuka Reorientation (successes) | 2.85 ± 0.05 | 23.2 ± 4.86 | 1.66 ± 0.11 | 33.2 ± 4.20 | 38.6 ± 0.63 |
| Two Arms Reorientation (successes) | 1.73 ± 0.51 | 14.46 ± 2.91 | — | — | 28.58 ± 1.55 |
| Allegro Hand (reward) | 1.01e4 ± 6.31e2 | 7.28e3 ± 1.24e3 | 1.01e4 ± 5.28e2 | 1.23e4 ± 3.29e2 | 9.14e3 ± 8.38e2 |
| Shadow Hand (reward) | 1.07e4 ± 4.90e2 | 1.01e4 ± 1.80e2 | 1.28e4 ± 1.25e2 | 1.17e4 ± 2.64e2 | 1.28e4 ± 2.80e2 |

## Qualitative Summary of Curves (from Figure 5)

### Allegro Kuka Regrasping
- **PPO**: Briefly reaches ~10 successes early in training, then drops to near 0. Worst performing method.
- **PQL**: Reaches a few successes, consistently near 0. Marginally better than PPO after initial training.
- **PBT**: Rapidly increases; achieves ~30+ successes. Significantly outperforms PPO and PQL.
- **SAPG**: Rapidly increases; reaches highest final performance (~35.7 successes). Best method.

### Allegro Kuka Throw
- **PPO**: Rapid initial increase, drops toward end of training; achieves ~16.8 successes at 2e10.
- **PQL**: Consistently slightly above 0; worst performing method (~2.62 successes at 2e10).
- **PBT**: Steady increase; achieves ~19.2 successes. Outperforms PPO.
- **SAPG**: Rapid steady increase; highest final performance (~23.7 successes). Best method.

### Allegro Kuka Reorientation
- **PPO**: Consistently approximately 0 throughout training (~2.85 at 2e10).
- **PQL**: Consistently approximately 0 (~1.66 at 2e10).
- **PBT**: Steadily increases; achieves ~23.2 successes. Outperforms PPO and PQL.
- **SAPG (entropy=0.005)**: Steadily increases; highest final performance (~38.6 successes). Best method.

### Allegro Kuka Two Arms Reorientation
- **PPO**: Near 0 (~1.73 at 2e10).
- **PBT**: Steady increase; ~14.46 at 2e10.
- **SAPG (entropy=0.005)**: Steady increase; ~28.58 at 2e10. More than twice PBT. Best method.

### Allegro Hand
- **PPO**: Steady increase; competitive performance (~1.01e4 at 2e10).
- **PBT**: Steady but slowest increase; worst performing (~7.28e3 at 2e10).
- **PQL**: Rapid initial increase then plateau; similar to PPO long-term (~1.01e4 at 2e10). Most sample-efficient initially.
- **SAPG (entropy=0)**: Steady continuous increase; highest final performance (~1.23e4 at 2e10). Best method.

### Shadow Hand
- **PPO**: Steady increase; ~1.07e4 at 2e10.
- **PBT**: Steady but slightly below PPO; ~1.01e4 at 2e10.
- **PQL**: Sharp initial increase then plateau; highest or tied-highest performance (~1.28e4 at 2e10). Most sample-efficient.
- **SAPG (entropy=0.005)**: Steady increase; ~1.28e4 at 2e10. Tied with PQL for best performance.

**Note**: All quantitative final values match Table 1 exactly. Curve shapes described above are qualitative readings from Figure 5.
