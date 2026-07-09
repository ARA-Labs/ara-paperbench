# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_main_results.md](tables/table1_main_results.md) | Table 1, §4.3 | C01, C02, C03 | Final reward (mean ± std) for all 8 environments × 4 refining methods × 3 explanation methods, showing RICE/Ours achieves highest reward in all environments. |
| [tables/table3_hyperparameters.md](tables/table3_hyperparameters.md) | Table 3, Appendix C.3 | C04, C05 | Per-environment values of hyperparameters p, λ, and α for all 8 benchmark environments. |
| [tables/table4_efficiency.md](tables/table4_efficiency.md) | Table 4, Appendix C.3 | C03 | Training time (seconds) for StateMask vs optimized StateMask (Ours) at fixed sample budgets across all 8 environments, demonstrating 16.8% average speedup. |
| [tables/table5_sil_comparison.md](tables/table5_sil_comparison.md) | Table 5, Appendix C.3 | C02 | Performance comparison between Self-Imitation Learning (SIL) and RICE on four MuJoCo tasks, showing RICE consistently outperforms SIL. |
| [tables/table6_explanation_methods.md](tables/table6_explanation_methods.md) | Table 6, Appendix C.3 | C01, C03 | Final reward comparison when using different explanation methods (Random, Integrated Gradients, AIRS, Ours) with fixed RICE refining on MuJoCo, confirming Ours achieves best refining. |
| [tables/table7_malware_casestudy.md](tables/table7_malware_casestudy.md) | Table 7, Appendix D | C04, C05 | Malware mutation ablation case study showing contribution of each RICE component (explanation, mixed distribution, exploration) to evasion probability. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure2_sparse_mujoco.md](figures/figure2_sparse_mujoco.md) | Figure 2, §4.3 | C02 | Refining curves (reward vs. training steps) for SparseHopper and SparseHalfCheetah, showing RICE achieves highest final reward (~900) fastest compared to baselines. |
| [figures/figure3_sac_hopper.md](figures/figure3_sac_hopper.md) | Figure 3, §4.3 | C06 | SAC pre-training curve (1M steps) and refining curves for all methods on Hopper, demonstrating RICE generalizes to non-PPO pretrained agents. |
| [figures/figure7_p_sensitivity.md](figures/figure7_p_sensitivity.md) | Figure 7, Appendix C.3 | C04 | Final reward vs. p ∈ {0, 0.25, 0.5, 0.75, 1.0} for all 8 environments under different λ values, confirming p=0.25 or p=0.5 is optimal. |
| [figures/figure8_lambda_sensitivity.md](figures/figure8_lambda_sensitivity.md) | Figure 8, Appendix C.3 | C05 | Final reward vs. λ ∈ {0.1, 0.01, 0.001} for all 8 environments, confirming any λ > 0 improves performance and λ=0.01 is generally best. |
| [figures/figure9_alpha_sensitivity.md](figures/figure9_alpha_sensitivity.md) | Figure 9, Appendix C.3 | C03 | Fidelity scores vs. α ∈ {0.01, 0.001, 0.0001} for all 8 environments at K=10%,20%,30%,40%, confirming low sensitivity of explanation quality to α. |
