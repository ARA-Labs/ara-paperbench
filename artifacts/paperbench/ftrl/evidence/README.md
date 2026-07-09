# Evidence Index

This directory contains **experiment results only** (scores, metrics, performance curves).
Hyperparameters and configuration details live in `src/configs/` (`training.md` and `model.md`).

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table4_nethack_full_eval.md](tables/table4_nethack_full_eval.md) | Table 4, §D (Appendix) | C01, C03, C04 | Full evaluation metrics (1000 episodes, last checkpoint) for all NetHack methods, including score, turns, dungeon level, XP, eating, gold, scout, sokoban, staircase. |
| [tables/table5_nethack_sota_comparison.md](tables/table5_nethack_sota_comparison.md) | Table 5, §D (Appendix) | C04 | Comparison of our best method (Fine-tuning + KS = 10588 ± 672) against all prior offline and offline+online NetHack baselines, establishing new neural SOTA. |
| [tables/table6_forward_transfer.md](tables/table6_forward_transfer.md) | Table 6, §F (Appendix) | C02, C04 | Forward transfer metric on pre-trained tasks (push-wall, peg-unplug-side) for fine-tuning, EWC, and BC as the number of prefix tasks increases from 1 to 4. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/fig3_main_performance.md](figures/fig3_main_performance.md) | Figure 3, §4 | C01, C03, C04 | Main performance comparison across all three domains. |
| [figures/nethack_performance.md](figures/nethack_performance.md) | Figure 3a, §4 | C01, C03, C04 | NetHack average return over training steps for all methods; shows KS and BC surpassing pre-trained SOTA while vanilla FT collapses. |
| [figures/montezuma_performance.md](figures/montezuma_performance.md) | Figure 3b, §4 | C01, C02, C04 | Montezuma's Revenge average return over ~5e7 training steps; BC achieves highest return (~6000), EWC converges faster but saturates lower. |
| [figures/robotic_performance.md](figures/robotic_performance.md) | Figure 3c, §4 | C01, C02, C04 | RoboticSequence overall success rate; BC ~80%, EM close second, EWC above vanilla FT, vanilla FT ≈ from scratch. |
| [figures/fig5_nethack_level_analysis.md](figures/fig5_nethack_level_analysis.md) | Figure 5, §5 | C03, C04, C05 | Per-level evaluation in NetHack: average return from Level 4 and Sokoban level throughout training. |
| [figures/nethack_level4_sokoban.md](figures/nethack_level4_sokoban.md) | Figure 5, §5 | C03, C04, C05 | Per-level evaluation in NetHack: average return from Level 4 (top) and Sokoban level (bottom) throughout training, showing KS advantage on Level 4 but BC advantage on Sokoban. |
| [figures/fig6_montezuma_room7.md](figures/fig6_montezuma_room7.md) | Figure 6, §5 | C02, C04, C06 | Room 7 success rate in Montezuma's Revenge throughout fine-tuning. |
| [figures/montezuma_room7.md](figures/montezuma_room7.md) | Figure 6, §5 | C02, C04, C06 | Room 7 success rate in Montezuma's Revenge throughout fine-tuning; vanilla FT drops sharply at ~20M steps while BC/EWC remain stable at ~75%. |
| [figures/fig7_robotic_per_stage.md](figures/fig7_robotic_per_stage.md) | Figure 7, §5 | C02, C04, C06 | Per-stage success rates for RoboticSequence throughout training. |
| [figures/robotic_stage_success.md](figures/robotic_stage_success.md) | Figure 7, §5 | C02, C04, C06 | Per-stage success rates for RoboticSequence throughout training; shows catastrophic forgetting of peg-unplug-side and push-wall under vanilla FT and recovery behavior for BC/EM/EWC. |
| [figures/fig8_pushwall_loglikelihood.md](figures/fig8_pushwall_loglikelihood.md) | Figure 8, §5 | C02, C04 | Push-wall log-likelihood analysis. |
| [figures/fig15_nethack_return_distribution.md](figures/fig15_nethack_return_distribution.md) | Figure 15, Appendix | C03, C04 | NetHack return distribution analysis. |
| [figures/fig_appleretrieval.md](figures/fig_appleretrieval.md) | Appendix | — | Apple retrieval task figure. |
