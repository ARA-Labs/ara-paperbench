---
# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_main_results.md](tables/table1_main_results.md) | Table 1, §6 | C02, C03, C06 | Final performance (mean ± SE) after 2×10¹⁰ environment steps for all methods (PPO, PBT, PQL, SAPG λ=0, SAPG λ=0.005) across all 6 tasks; demonstrates SAPG superiority on hard tasks. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/fig2_ppo_batch_saturation.md](figures/fig2_ppo_batch_saturation.md) | Figure 2, §3 | C01 | PPO asymptotic performance vs. batch size for Shadow Hand and Allegro Kuka Throw, showing saturation plateau beyond ~25k environments with SAPG reference line above. |
| [figures/fig5_performance_curves.md](figures/fig5_performance_curves.md) | Figure 5, §6 | C02 | Learning curves (performance vs. number of env steps up to 2×10¹⁰) for SAPG, PPO, PBT, PQL across all 6 manipulation tasks. |
| [figures/fig6_ablation_curves.md](figures/fig6_ablation_curves.md) | Figure 6, §6.3 | C03, C05, C06 | Ablation learning curves comparing SAPG variants (symmetric, no off-policy, high off-policy ratio, entropy coefficients 0/0.003/0.005) across 5 tasks. |
| [figures/fig7_fig8_diversity_metrics.md](evidence/figures/fig7_fig8_diversity_metrics.md) | Figures 7–8, §6.4 | C04 | State diversity metrics: PCA reconstruction error vs. number of components (Fig 7) and MLP reconstruction error vs. hidden layer size (Fig 8) for SAPG, PPO, and random policy across 3 tasks. |
