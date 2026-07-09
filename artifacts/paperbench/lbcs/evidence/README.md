# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_mnist_s_objectives.md](tables/table1_mnist_s_objectives.md) | Table 1, §5.1 | C01, C03 | LBCS on MNIST-S (k=200,400; ε=0.2,0.3,0.4; 20 reps): initial and final f1/f2 values showing both objectives decrease after LBCS. |
| [tables/table2_main_results.md](tables/table2_main_results.md) | Table 2, §5.2 | C01 | Main comparison: test accuracy (%) and LBCS coreset sizes on F-MNIST/SVHN/CIFAR-10 for all 8 methods at k∈{1000,2000,3000,4000}. |
| [tables/table3_lbcs_sizes.md](tables/table3_lbcs_sizes.md) | Table 3, §5.2 | C02 | All 8 methods evaluated at LBCS-determined coreset sizes on F-MNIST/SVHN/CIFAR-10, showing LBCS consistently outperforms. |
| [tables/table4_imagenet.md](tables/table4_imagenet.md) | Table 4, §5.4 | C05 | ImageNet-1k Top-5 test accuracy (%) at predefined ratios 70% and 80%; LBCS optimized ratios reported. |
| [tables/table5_ablation_search_times.md](tables/table5_ablation_search_times.md) | Table 7 (Appendix E.4), §6 | C03 | Ablation on search time T for F-MNIST at k=1000 and k=2000: test accuracy and coreset size vs. T. |
| [tables/table6_cross_architecture.md](tables/table6_cross_architecture.md) | Table 8 (Appendix E.5), §6 | C01 | Cross-architecture evaluation on SVHN: ViT-small and WideResNet (W-NET) trained on coresets selected by all 8 methods. |
| [tables/table7_imperfect_supervision.md](tables/table7_imperfect_supervision.md) | Table 6 (Appendix E.3), §5.3 | C04 | Optimized coreset sizes (mean±std) by LBCS under 30%/50% label noise and class imbalance at k∈{1000,2000,3000,4000}. |
| [tables/table8_continual_streaming.md](tables/table8_continual_streaming.md) | Tables 9–10 (Appendix E.6–E.7), §6 | C01 | Continual learning (PermMNIST) and streaming task accuracy for all methods. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/fig1_trivial_solutions.md](figures/fig1_trivial_solutions.md) | Figure 1, §2.1 | C01, C03 | f1(m) and f2(m) vs. outer loop iterations for Eq. (3) and Eq. (4) at k∈{100,150,200,250} on MNIST-S, showing failure modes of trivial solutions. |
| [figures/fig2_imperfect_supervision.md](figures/fig2_imperfect_supervision.md) | Figure 2, §5.3 | C04 | Test accuracy of all 8 methods on F-MNIST with 30% corrupted labels (2a) and class-imbalanced data (2b) at k∈{1000,2000,3000,4000}. |
| [figures/fig3_per_point_accuracy.md](figures/fig3_per_point_accuracy.md) | Figure 3 (Appendix E.1), §5.2 | C01, C02 | Average test accuracy per coreset data point for all 8 methods across F-MNIST/SVHN/CIFAR-10 at k∈{1000,2000,3000,4000}. |
