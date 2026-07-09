---
# Figure 5: Main Comparison Learning Curves
- **Source**: Figure 5, §6
- **Caption**: "Performance curves of SAPG with respect to PPO, PBT and PQL baselines. On AllegroKuka tasks, PPO and PQL barely make progress and SAPG beats PBT. On Shadow Hand and Allegro Kuka Reorientation and Two Arms Reorientation, SAPG performs best with an entropy coefficient of 0.005 while the coefficient is 0 for other environments. On ShadowHand and AllegroHand, while PQL is initially more sample efficient, SAPG is more performant in the longer run."

## Axis Information
- **X-axis**: Number of environment steps (0 to 2×10^10 for most tasks)
- **Y-axis**: Episode successes (AllegroKuka tasks) or Episode rewards (AllegroHand, ShadowHand)
- **Methods**: SAPG (Ours), PPO, PBT, PQL

## Final Performance at 2×10^10 Steps (exact values from Table 1)

| Task | Metric | PPO | PBT | PQL | SAPG (λ=0) | SAPG (λ=0.005) |
|------|--------|-----|-----|-----|------------|----------------|
| Allegro Kuka Regrasping | Successes | 1.25 ± 1.15 | 31.9 ± 2.26 | 2.73 ± 0.02 | 35.7 ± 1.46 | 33.4 ± 2.25 |
| Allegro Kuka Throw | Successes | 16.8 ± 0.48 | 19.2 ± 1.07 | 2.62 ± 0.08 | 23.7 ± 0.74 | 18.7 ± 0.43 |
| Allegro Kuka Reorientation | Successes | 2.85 ± 0.05 | 23.2 ± 4.86 | 1.66 ± 0.11 | 33.2 ± 4.20 | 38.6 ± 0.63 |
| Two Arms Reorientation | Successes | 1.73 ± 0.51 | 14.46 ± 2.91 | — | — | 28.58 ± 1.55 |
| Allegro Hand | Episode Reward | 1.01e4 ± 6.31e2 | 7.28e3 ± 1.24e3 | 1.01e4 ± 5.28e2 | 1.23e4 ± 3.29e2 | 9.14e3 ± 8.38e2 |
| Shadow Hand | Episode Reward | 1.07e4 ± 4.90e2 | 1.01e4 ± 1.80e2 | 1.28e4 ± 1.25e2 | 1.17e4 ± 2.64e2 | 1.28e4 ± 2.80e2 |

## Qualitative Description of Curves (extracted from paper text and figure caption)

### Allegro Kuka Regrasping
- PPO: Starts ~10 successes, quickly drops to ~0; worst performing method
- PQL: Few successes at start, consistently slightly above PPO; performs better than PPO except at start
- PBT: Rapidly increases successes; significantly outperforms PPO and PQL
- SAPG: Rapidly increases successes; outperforms PBT; best performing method

### Allegro Kuka Throw
- PPO: Rapid increase then drops toward end; significantly outperforms PQL
- PQL: Slightly above 0 throughout; worst performing method
- PBT: Rapid increase; outperforms PPO
- SAPG: Rapid increase; best performing method

### Allegro Kuka Reorientation
- PPO: Approximately 0 throughout
- PQL: Approximately 0 throughout
- PBT: Increases steadily; better than PPO and PQL
- SAPG: Increases steadily; best performing method

### Allegro Kuka Two Arms Reorientation
- PPO: Near zero throughout
- PBT: Increases slowly; outperforms PPO
- SAPG: Increases; best performing method; >2× PBT

### Allegro Hand (Episode Rewards, range 2500–12500)
- PPO: Increases steadily
- PBT: Increases steadily; worst performing method
- PQL: Increases quickly then plateaus; similar performance to PPO
- SAPG: Increases steadily; best asymptotic performance

### Shadow Hand (Episode Rewards, range 2500–12500)
- PPO: Increases steadily; similar performance to PBT
- PBT: Increases steadily; similar performance to PPO
- PQL: Increases sharply then plateaus; outperforms PPO and PBT; achieves similar to SAPG
- SAPG: Increases steadily; outperforms PPO and PBT; comparable to PQL
