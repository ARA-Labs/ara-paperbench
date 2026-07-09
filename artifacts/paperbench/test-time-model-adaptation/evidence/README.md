---
# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table2_imagenetc_accuracy.md](tables/table2_imagenetc_accuracy.md) | Table 2, §4.1 | C01, C05 | Accuracy (%) for all methods on ImageNet-C (severity 5), 15 corruption types plus average and ECE; FOA achieves 66.3% average accuracy and 3.2% ECE, best overall. |
| [tables/table3_imagenet_rvs_accuracy.md](tables/table3_imagenet_rvs_accuracy.md) | Table 3, §4.1 | C01 | Accuracy (%) and ECE (%) for all methods on ImageNet-R, ImageNet-V2, and ImageNet-Sketch; FOA achieves best or comparable results across all three benchmarks. |
| [tables/table4_quantized_accuracy.md](tables/table4_quantized_accuracy.md) | Table 4, §4.2 | C02, C03 | Accuracy (%) and ECE (%) for 8-bit and 6-bit quantized ViT-Base on ImageNet-C; FOA (8-bit) achieves 63.5% accuracy, surpassing TENT (32-bit, 59.6%). |
| [tables/table5_ablation_components.md](tables/table5_ablation_components.md) | Table 5, §4.3 | C04, C05 | Component ablation for FOA showing contribution of entropy, activation discrepancy, and activation shifting; entropy-only CMA fails (44.9%), discrepancy fitness alone gives 63.4%. |
| [tables/table6_foai_intervals.md](tables/table6_foai_intervals.md) | Table 6, §4.4 | C01 | Accuracy and ECE for FOA-I (interval update strategy) with different intervals I={4,8,16,32,64}; FOA-I with I=4 outperforms TENT (BS=64). |
| [tables/table7_memory_usage.md](tables/table7_memory_usage.md) | Table 7, §4.4 | C03 | Run-time memory usage (MB) for different methods and batch sizes; FOA uses 832 MB vs. TENT 5,165 MB and CoTTA 16,836 MB at BS=64. |
| [tables/table8_computation.md](tables/table8_computation.md) | Table 8, §4.4 | C01, C03 | Computational complexity: number of forward/backward passes, wall-clock time, and memory; FOA (K=28) uses 3,386 MB vs. TENT 5,165 MB and CoTTA 16,836 MB. |
| [tables/table9_design_choices.md](tables/table9_design_choices.md) | Table 9, §4.4 | C04, C05 | Design choice study comparing learnable parameters × optimizer × loss function; CMA on norm layers collapses to 0.1%, CMA on prompts with entropy gives 44.9%, FOA combination gives 65.4%. |
| [tables/table10_resnet_mamba.md](tables/table10_resnet_mamba.md) | Table 10, §4.4 | C01 | FOA results on ResNet-50 and VisionMamba; FOA is competitive on VisionMamba but lags behind TENT on ResNet-50 due to CNN locality limitation. |
| [tables/table11_noniid.md](tables/table11_noniid.md) | Table 11, §4.4 | C07 | Performance under non-i.i.d. scenarios (online label shift and mixed domain shift); FOA maintains best accuracy and lowest ECE among TENT, SAR, FOA. |
| [tables/table12_indistribution.md](tables/table12_indistribution.md) | Table 12, §4.4 | C06 | In-distribution accuracy and ECE on clean ImageNet validation set; FOA achieves 85.11% (−0.06% from NoAdapt), best among all TTA methods. |
| [tables/table13_lambda_sensitivity.md](tables/table13_lambda_sensitivity.md) | Table 13, Appendix C | C05 | Sensitivity of FOA to trade-off parameter λ ∈ [0.1, 1.0] on ImageNet-C (Gaussian, level 5); accuracy varies only slightly (61.1%–61.8%) showing low sensitivity. |
| [tables/table16_ece_fullprecision.md](tables/table16_ece_fullprecision.md) | Table 16, Appendix D | C01 | Detailed ECE (%) for all methods on ImageNet-C (severity 5) for all 15 corruption types; FOA achieves 3.2% average ECE vs. TENT 18.5% and SAR 7.0%. |
| [tables/table17_ece_quantized.md](tables/table17_ece_quantized.md) | Table 17, Appendix D | C02 | Detailed ECE (%) for 8-bit and 6-bit quantized ViT on ImageNet-C; FOA (8-bit) achieves 3.8% ECE vs. T3A 25.9%. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/fig2a_population_size.md](figures/fig2a_population_size.md) | Figure 2(a), §4.3 | C01, C03 | Accuracy and ECE of FOA vs. population size K ∈ {2,...,28} on ImageNet-C (Gaussian, level 5); performance converges at K>15; K=2 already beats NoAdapt and T3A. |
| [figures/fig2b_num_prompts.md](figures/fig2b_num_prompts.md) | Figure 2(b), §4.3 | C05 | Accuracy and ECE of FOA vs. number of prompt embeddings Np ∈ {1,...,10}; shows low sensitivity across all values with marginal optimum at Np=5 or 7. |
| [figures/fig2c_num_id_samples.md](figures/fig2c_num_id_samples.md) | Figure 2(c), §4.3 | C05 | Accuracy and ECE of FOA vs. number of source ID samples Q ∈ {16,32,...,1600}; stable performance for Q≥32, demonstrating minimal source data requirement. |
