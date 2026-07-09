---
# Evidence Index

## Tables
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/benchmark_c2st_posterior.md](tables/benchmark_c2st_posterior.md) | Figure 4a, §4.1 | C01, C02 | C2ST posterior accuracy (lower=better) for Simformer variants and NPE across 4 benchmark tasks at simulation budgets 10³, 10⁴, 10⁵; shows Simformer outperforms NPE and structured masks improve efficiency. |
| [tables/benchmark_c2st_all_cond.md](tables/benchmark_c2st_all_cond.md) | Figure 4b, §4.1 | C03, C06 | C2ST all-conditional accuracy for Simformer variants across Tree, HMM, Two Moons, SLCP tasks at simulation budgets 10³, 10⁴, 10⁵; verifies all-conditionals estimation capability. |

## Figures
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/fig4a_benchmark_posterior.md](figures/fig4a_benchmark_posterior.md) | Figure 4a, §4.1 | C01, C02 | C2ST posterior accuracy curves vs simulation budget for Simformer (dense, undirected, directed) and NPE on Linear Gaussian, Mixture Gaussian, Two Moons, SLCP; shows ~10x simulation efficiency gain and structured mask improvements. |
| [figures/fig4b_benchmark_all_cond.md](figures/fig4b_benchmark_all_cond.md) | Figure 4b, §4.1 | C03, C06 | C2ST all-conditional accuracy curves vs simulation budget for Simformer variants on Tree, HMM, Two Moons, SLCP; verifies accurate modeling of arbitrary conditionals at 10⁵ sims. |
| [figures/fig5c_lotka_volterra.md](figures/fig5c_lotka_volterra.md) | Figure 5c, §4.2 | C04 | C2ST curves for Lotka-Volterra posterior and arbitrary conditionals vs simulation budget; shows Simformer achieves good calibration with unstructured data at 10⁵ simulations. |
| [figures/fig_a5_extended_vesde.md](figures/fig_a5_extended_vesde.md) | Figure A5, Appendix A3.1 | C01, C03, C06 | Extended VESDE benchmark including NRE, NLE, NPSE, Simformer (posterior only) in addition to NPE; confirms Simformer advantages and validates all-conditionals training objective. |
| [figures/fig_a7_eval_steps.md](figures/fig_a7_eval_steps.md) | Figure A7, Appendix A3.1 | C01 | C2ST vs number of reverse SDE evaluation steps (50–1000) for VESDE and VPSDE across 4 benchmark tasks; demonstrates sharp performance transition at ~50 steps. |
| [figures/fig_a8_nll.md](figures/fig_a8_nll.md) | Figure A8, Appendix A3.1 | C01, C03 | Average negative log-likelihood for likelihood and posterior across 4 benchmark tasks, comparing Simformer variants with NLE and NPE; shows Simformer is competitive despite not directly minimizing NLL. |
| [figures/figA15_guidance_bm.md](figures/figA15_guidance_bm.md) | Figure A15, Appendix A3.3 | C05 | Guidance benchmark: Simformer trained for joint-only estimation uses diffusion guidance (Repaint and General Guidance) for conditioning; self-recurrence r=5 closes gap with model-based conditioning at 5× compute cost. |
