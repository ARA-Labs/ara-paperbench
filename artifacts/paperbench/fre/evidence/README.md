# Evidence Index

## Tables
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_main_results.md](tables/table1_main_results.md) | Table 1, §5.2 | C01, C02, C03 | Main zero-shot offline RL comparison across AntMaze, ExORL (walker/cheetah), and Kitchen domains for FRE, GC-IQL, GC-BC, OPAL, FB, and SF — every cell value (mean ± std over 5 seeds, 20 episodes each, normalized 0–100). |
| [tables/table4_reward_subset_ablation.md](tables/table4_reward_subset_ablation.md) | Table 4, Appendix D | C04 | Full AntMaze ablation comparing FRE agents trained on all 7 subsets of the three random reward families (goal, linear, MLP), showing that FRE-all achieves the highest total score. |

## Figures
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure5_reward_diversity_scaling.md](figures/figure5_reward_diversity_scaling.md) | Figure 5, §5.3 | C04 | Bar chart comparing 7 FRE reward-family-subset variants across 4 AntMaze task categories, showing FRE-all (trained on all three families) achieves the largest total and competitive per-task scores. |
| [figures/figure6_domain_knowledge.md](figures/figure6_domain_knowledge.md) | Figure 6, §5.4 | C05 | Bar chart showing FRE-hint (domain-knowledge-augmented prior) vs. FRE-all on ant-directional, exorl-cheetah-velocity, and exorl-walker-velocity tasks, demonstrating improvement from incorporating domain-specific reward distributions. |
