---
# Figure 5: Performance Curves — SAPG vs. PPO, PBT, PQL (All 6 Tasks)

- **Source**: Figure 5, Section 6
- **Caption**: "Performance curves of SAPG with respect to PPO, PBT and PQL baselines. On AllegroKuka tasks, PPO and PQL barely make progress and SAPG beats PBT. On Shadow Hand and Allegro Kuka Reorientation and Two Arms Reorientation, SAPG performs best with an entropy coefficient of 0.005 while the coefficient is 0 for other environments. On ShadowHand and AllegroHand, while PQL is initially more sample efficient, SAPG is more performant in the longer run. AllegroKuka environments use successes as a performance metric while AllegroHand and ShadowHand use episode rewards."
- **X-axis**: Number of environment steps (0 to 2×10¹⁰)
- **Y-axis**: Episode successes (AllegroKuka tasks) or episode rewards (AllegroHand, ShadowHand)
- **Curves**: SAPG (Ours), PPO, PBT, PQL; shaded regions = ±1 standard error; solid line = mean over 5 seeds

## Qualitative Curve Descriptions (exact numeric traces not available from paper)

### Allegro Kuka Regrasping
| Method | Qualitative behavior | Final value (from Table 1) |
|--------|---------------------|--------------------------|
| SAPG (λ=0) | Rapidly increases; best performer | 35.7 ± 1.46 |
| PBT | Rapidly increases; second best | 31.9 ± 2.26 |
| PQL | Near zero throughout | 2.73 ± 0.02 |
| PPO | Near zero; initial ~10 successes then drops | 1.25 ± 1.15 |

### Allegro Kuka Throw
| Method | Qualitative behavior | Final value (from Table 1) |
|--------|---------------------|--------------------------|
| SAPG (λ=0) | Rapidly increases; best performer | 23.7 ± 0.74 |
| PBT | Increases; second best | 19.2 ± 1.07 |
| PPO | Increases then drops at end of training | 16.8 ± 0.48 |
| PQL | Near zero throughout | 2.62 ± 0.08 |

### Allegro Kuka Reorientation
| Method | Qualitative behavior | Final value (from Table 1) |
|--------|---------------------|--------------------------|
| SAPG (λ=0.005) | Steady increase; best performer | 38.6 ± 0.63 |
| SAPG (λ=0) | Steady increase; second best | 33.2 ± 4.20 |
| PBT | Steady increase | 23.2 ± 4.86 |
| PPO | Consistently ~0 | 2.85 ± 0.05 |
| PQL | Consistently ~0 | 1.66 ± 0.11 |

### Allegro Kuka Two Arms Reorientation
| Method | Qualitative behavior | Final value (from Table 1) |
|--------|---------------------|--------------------------|
| SAPG (λ=0.005) | Steady increase; best performer | 28.58 ± 1.55 |
| PBT | Moderate increase | 14.46 ± 2.91 |
| PPO | Near zero | 1.73 ± 0.51 |
| PQL | Not reported ("-") | - |

### Allegro Hand (Easy Task)
| Method | Qualitative behavior | Final value (from Table 1) |
|--------|---------------------|--------------------------|
| SAPG (λ=0) | Steady increase throughout; best performer | 1.23e4 ± 3.29e2 |
| PQL | Rapid early increase, then plateau ~similar to PPO | 1.01e4 ± 5.28e2 |
| PPO | Steady increase | 1.01e4 ± 6.31e2 |
| PBT | Steady increase; worst performer | 7.28e3 ± 1.24e3 |

### Shadow Hand (Easy Task)
| Method | Qualitative behavior | Final value (from Table 1) |
|--------|---------------------|--------------------------|
| SAPG (λ=0.005) | Steady increase; best performer (tied PQL) | 1.28e4 ± 2.80e2 |
| PQL | Sharp early increase, plateaus; similar to SAPG | 1.28e4 ± 1.25e2 |
| PPO | Steady increase; similar to PBT | 1.07e4 ± 4.90e2 |
| PBT | Steady increase; similar to PPO | 1.01e4 ± 1.80e2 |
