---
# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_optimizer_comparison.md](tables/table1_optimizer_comparison.md) | Table 1, §6.1 | C05 | Best loss and L2RE for Adam, L-BFGS, and Adam+L-BFGS across all widths after hyperparameter tuning on all three PDEs — shows Adam+L-BFGS consistently achieves lowest values. |
| [tables/table2_nncg_results.md](tables/table2_nncg_results.md) | Table 2, §7.3 | C06 | Loss and L2RE comparison after NNCG and GD fine-tuning vs. baseline Adam+L-BFGS — shows NNCG substantially reduces both metrics while GD produces no improvement. |
| [tables/table3_timing.md](tables/table3_timing.md) | Table 3, Appendix E.3 | C06 | Per-iteration wall-clock times (seconds) for L-BFGS and NNCG on each PDE, showing NNCG is 5–322× slower due to Hessian-vector products. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/fig2_loss_vs_l2re.md](figures/fig2_loss_vs_l2re.md) | Figure 2, §4 | C01 | Scatter plot of final loss vs. final L2RE for all optimizer/width/seed combinations across three PDEs, showing monotone correlation (lower loss → lower L2RE) and presence of trivial solutions. |
| [figures/fig3_hessian_spectral.md](figures/fig3_hessian_spectral.md) | Figure 3 + Figure 7, §5 | C02, C03, C04 | Spectral density plots of the Hessian (solid) and L-BFGS preconditioned Hessian (dashed) for the total PINN loss and individual components across all three PDEs, demonstrating ill-conditioning and 1000× improvement from preconditioning. |
