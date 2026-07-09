# Evidence Index

## Tables
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_models_hardware.md](tables/table1_models_hardware.md) | Table 1, §6.1 | C02, C03, C04, C08 | Four model configurations (Phi-3 3.8B to Llama 3.1 70B) and their A100 GPU allocations used across all experiments. |
| [tables/table2_dataset_statistics.md](tables/table2_dataset_statistics.md) | Table 2, §6.1 | C02, C03, C08 | Request length statistics for BurstGPT, ShareGPT, and LMSYS-Chat-1M datasets used to construct workloads. |

## Figures
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure2_user_consumption_speeds.md](figures/figure2_user_consumption_speeds.md) | Figure 2, §2.1 | C01 | Reading speed (4.8 tok/s) and listening speed (3.3 tok/s) across demographic groups, motivating user-centric scheduling. |
| [figures/figure4_vllm_ttft_tds_vs_burst_duration.md](figures/figure4_vllm_ttft_tds_vs_burst_duration.md) | Figure 4, §2.2 | C01, C04 | vLLM's TTFT inflates to 10.4s under burst while TDS stays well above consumption speed, revealing the scheduling gap. |
| [figures/figure11_burstgpt_cdf_qoe_ttft_tds.md](figures/figure11_burstgpt_cdf_qoe_ttft_tds.md) | Figure 11, §6.2 | C04, C07 | CDF comparison showing Andes achieves 97% of requests at QoE ≥ 0.95 vs 75% for vLLM on BurstGPT traces. |
| [figures/figure15_avg_qoe_vs_burst_intensity.md](figures/figure15_avg_qoe_vs_burst_intensity.md) | Figure 15, §6.3 | C02, C03, C08 | Andes maintains high QoE across increasing burst intensity while baselines degrade, demonstrating robustness. |
| [figures/figure16_avg_qoe_vs_burst_duration.md](figures/figure16_avg_qoe_vs_burst_duration.md) | Figure 16, §6.3 | C08 | QoE under varying burst durations shows Andes sustains performance where FCFS and LQSF collapse. |
| [figures/figure17_overhead_refiner_ablation.md](figures/figure17_overhead_refiner_ablation.md) | Figure 17, §6.4 | C05 | Ablation confirming the overhead-aware refiner prevents QoE degradation from excessive preemptions under long bursts. |
| [figures/figure18_knapsack_solver_comparison.md](figures/figure18_knapsack_solver_comparison.md) | Figure 18, §6.4 | C06 | Greedy solver is ~20× faster than exact 3D DP with slightly better QoE due to lower per-quantum scheduling latency. |
| [figures/figure19_delta_t_sensitivity.md](figures/figure19_delta_t_sensitivity.md) | Figure 19, §6.4 | C08 | Sensitivity analysis showing Andes is robust to scheduling quantum Δt across a range of values. |
| [figures/figure20_poisson_arrival.md](figures/figure20_poisson_arrival.md) | Figure 20, §6.4 | C08 | Andes outperforms baselines under Poisson arrival patterns, validating generalization beyond bursty workloads. |
| [figures/figure21_context_length_vs_batch_size.md](figures/figure21_context_length_vs_batch_size.md) | Figure 21, Appendix B | C02 | Token latency increases with both context length and batch size, justifying the knapsack formulation's weight function. |
