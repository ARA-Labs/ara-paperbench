# Evidence Index

## Tables
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_main_results.md](tables/table1_main_results.md) | Table 1, §4.2 | C01 | Main CIL comparison of 8 methods on 6 dataset configurations with ViT-B/16-IN1K, reporting AN and Ā; SEMA achieves highest or competitive AN across all settings. |
| [tables/table2_ablation_composing.md](tables/table2_ablation_composing.md) | Table 2, §4.3 | C03 | Ablation of expansion strategy and adapter composing on ImageNet-A and VTAB; shows learned soft router with expansion outperforms all variants including no-expansion and hard selection. |
| [tables/table3_adapter_variants.md](tables/table3_adapter_variants.md) | Table 3, §4.3 | C04 | Performance of SEMA with three functional adapter types (Adapter, LoRA, Convpass) on ImageNet-A and VTAB; results are within ~1% confirming adapter-agnosticism. |
| [tables/table4_in21k.md](tables/table4_in21k.md) | Table 4, Appendix C.1 | C01 | Main CIL comparison using ViT-B/16-IN21K weights; SEMA consistently outperforms baselines confirming robustness to pre-training dataset choice. |
| [tables/table5_param_efficiency.md](tables/table5_param_efficiency.md) | Table 5, Appendix C.2 | C02, C03 | Comparison of "Expansion by Task" vs SEMA on parameters (M) and accuracy; SEMA uses fewer params with better accuracy demonstrating the value of on-demand expansion. |
| [tables/table6_added_params.md](tables/table6_added_params.md) | Table 6, Appendix C.2 | C02 | Number of added parameters (Millions) for L2P, DualPrompt, CODA-P, and SEMA on all datasets; SEMA has the fewest added parameters among expandable methods. |
| [tables/table7_rd_routing.md](tables/table7_rd_routing.md) | Table 7, Appendix C.3 | C03 | Learned router vs RD-based hard routing across all dataset configurations; learned router outperforms RD-based routing by ~2% AN on average. |
| [tables/table8_train_time.md](tables/table8_train_time.md) | Table 8, Appendix C.4 | C01 | Per-batch training time (seconds) for each method; SEMA is faster than or comparable to baselines, especially on datasets where few expansions occur. |
| [tables/table9_inference_time.md](tables/table9_inference_time.md) | Table 9, Appendix C.4 | C01 | Per-image inference time (ms) for each method; SEMA has the lowest or comparable inference latency because it does not require frozen model queries for prompt retrieval. |
| [tables/table10_50task.md](tables/table10_50task.md) | Table 10, Appendix C.5 | C01 | Evaluation on 50-task sequences (4 classes per task) on ImageNet-R and ImageNet-A; SEMA outperforms all baselines in long task sequences. |
| [tables/table11_limited_data_vtab.md](tables/table11_limited_data_vtab.md) | Table 11, Appendix C.7 | C01, C03 | SEMA vs EASE on VTAB with 90% data removed from 1 or 2 tasks; SEMA matches or exceeds EASE despite the latter using a stronger classification head. |
| [tables/table12_limited_data_ina.md](tables/table12_limited_data_ina.md) | Table 12, Appendix C.7 | C01, C02 | SEMA vs EASE on ImageNet-A with 10% and 20% data; comparable performance with sub-linear parameter growth advantage for SEMA. |
| [tables/table13_multiple_seeds.md](tables/table13_multiple_seeds.md) | Table 13, Appendix C.8 | C01 | SEMA mean ± std accuracy over 5 runs with different seeds on all datasets; demonstrates robustness to class order and initialization. |
| [tables/table14_ranpac.md](tables/table14_ranpac.md) | Table 14, Appendix C.10 | C01 | RanPAC vs SEMA+RanPAC combination; SEMA's representations improve RanPAC classification, showing the methods are orthogonal and complementary. |
| [tables/table15_clip.md](tables/table15_clip.md) | Table 15, Appendix C.11 | C01, C04 | SEMA with CLIP ViT-B/16 backbone vs zero-shot CLIP and ADAM; SEMA improves over both on CIFAR-100 and 10-Task ImageNet-R. |

## Figures
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/fig4_reconstruction_error.md](figures/fig4_reconstruction_error.md) | Figure 4, §4.3 | C03 | Reconstruction error of 3 AE-based RDs across 5 VTAB tasks; shows that RDs converge during training and signal expansion for Tasks 1-3 but not Tasks 4-5 (reuse). |
| [figures/fig5_adapter_usage.md](figures/fig5_adapter_usage.md) | Figure 5, §4.3 | C03 | Normalized adapter usage (router weights) per task on VTAB; Tasks 4 and 5 primarily reuse Adapters 1 and 3 respectively, demonstrating effective knowledge transfer. |
| [figures/fig6_threshold.md](figures/fig6_threshold.md) | Figure 6, §4.3 | C03 | Accuracy and adapter count vs expansion threshold τ for ImageNet-A (τ=1.0-2.0) and VTAB (τ=1.0-8.0); shows z-score robustness and expected accuracy-efficiency trade-off. |
| [figures/fig7_multilayer.md](figures/fig7_multilayer.md) | Figure 7, §4.3 | C03 | Accuracy and adapter count vs number of eligible expansion layers (11-12, 10-12, 9-12) on ImageNet-A and VTAB; more layers improve accuracy at the cost of more adapters. |
| [figures/fig8_param_growth.md](figures/fig8_param_growth.md) | Figure 8, §4.3 | C02 | Total added parameters (M) over 20 tasks on ImageNet-A for L2P, DualPrompt, CODA-P, SEMA, and Expansion-by-Task; visually demonstrates SEMA's sub-linear growth rate. |
