# Evidence Index

## Tables
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_resnet_main_results.md](tables/table1_resnet_main_results.md) | Table 1, §5 | C01, C03 | Main accuracy results (mean%±std%) for ResNet-18 and ResNet-50 on 11 datasets across Pad, Narrow, Medium, Full, and SMM (Ours) methods with ILM output mapping. |
| [tables/table2_vit_main_results.md](tables/table2_vit_main_results.md) | Table 2, §5 | C01, C04 | Main accuracy results (mean%) for ViT-B32 on 11 datasets across all 5 VR methods; shows SMM achieves highest average (72.4%) with large gains on Flowers102, Food101, SUN397. |
| [tables/table3_ablation_masking.md](tables/table3_ablation_masking.md) | Table 3, §5 | C05 | Ablation study comparing four SMM variants (Only δ, Only fmask, Single-Channel, Full SMM) on 11 datasets with ResNet-18, demonstrating necessity of all components. |
| [tables/table4_parameter_statistics.md](tables/table4_parameter_statistics.md) | Table 4, Appendix A.2 | C02 | Parameter count statistics for the SMM mask generator fmask across ResNet-18/50 and ViT-B32, showing <0.23% overhead relative to pre-trained model parameters. |
| [tables/table5_interpolation_comparison.md](tables/table5_interpolation_comparison.md) | Table 5, Appendix A.3 | C06 | Efficiency comparison of patch-wise interpolation vs bilinear and bicubic methods: pixel accesses and wall-clock time per batch for ResNet and ViT configurations. |
| [tables/table6_dataset_info.md](tables/table6_dataset_info.md) | Table 6, Appendix C | C03, C04 | Detailed dataset information including original image size, training set size, test set size, and number of classes for all 11 target datasets. |
| [tables/table10_label_mapping_comparison.md](tables/table10_label_mapping_comparison.md) | Table 10, Appendix D.1 | C03 | SMM performance improvement over baselines across all three label mapping methods (ILM, FLM, RLM), showing consistent gains especially for worse-performing output mappers. |
| [tables/table_stanfordcars.md](tables/table_stanfordcars.md) | Table 12, Appendix D.4 | C03 | StanfordCars results showing all VR methods fail (<10% accuracy) on this fine-grained recognition task, confirming VR's fundamental limitation on subtle appearance tasks. |

## Figures
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure4_patch_size_ablation.md](figures/figure4_patch_size_ablation.md) | Figure 4, §5 | C05 | Accuracy vs patch size (2^l for l∈{0,1,2,3,4}) on EuroSAT, Flowers102, CIFAR100, and SVHN using ResNet-18, showing that patch size 8 (l=3) is optimal with accuracy increasing then plateauing/declining. |
