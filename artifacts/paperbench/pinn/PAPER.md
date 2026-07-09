---
title: "Challenges in Training PINNs: A Loss Landscape Perspective"
authors: ["Pratik Rathore", "Weimu Lei", "Zachary Frangella", "Lu Lu", "Madeleine Udell"]
year: 2024
venue: "Proceedings of the 41st International Conference on Machine Learning (ICML)"
doi: "arXiv:2402.01868v2"
ara_version: "1.0"
domain: "Scientific Machine Learning / PDE Solvers"
keywords: ["physics-informed neural networks", "PINN", "loss landscape", "ill-conditioning", "optimization", "L-BFGS", "Adam", "NysNewton-CG", "Hessian", "partial differential equations"]
claims_summary:
  - "PINN loss must be minimized to near-zero to obtain accurate PDE solutions (L2RE correlates strongly with training loss)"
  - "PINN loss landscape is ill-conditioned (condition numbers >10^4) primarily due to differential operators in the residual term, with L-BFGS reducing conditioning by ≥1000×"
  - "Adam+L-BFGS combined optimizer consistently outperforms either alone; NNCG further improves solutions where L-BFGS terminates early"
abstract: "This paper explores challenges in training Physics-Informed Neural Networks (PINNs), emphasizing the role of the loss landscape in the training process. We examine difficulties in minimizing the PINN loss function, particularly due to ill-conditioning caused by differential operators in the residual term. We compare gradient-based optimizers Adam, L-BFGS, and their combination Adam+L-BFGS, showing the superiority of Adam+L-BFGS, and introduce a novel second-order optimizer, NysNewton-CG (NNCG), which significantly improves PINN performance. Theoretically, our work elucidates the connection between ill-conditioned differential operators and ill-conditioning in the PINN loss and shows the benefits of combining first- and second-order optimization methods. Our work presents valuable insights and more powerful optimization strategies for training PINNs, which could improve the utility of PINNs for solving difficult partial differential equations."
---

# Challenges in Training PINNs: A Loss Landscape Perspective

## Overview

This paper investigates why training Physics-Informed Neural Networks (PINNs) is difficult, and proposes practical and theoretical solutions. The central insight is that the PINN loss is inherently ill-conditioned because differential operators in the residual term induce large Hessian eigenvalue spreads (condition numbers >10^4), causing first-order methods like Adam to converge slowly.

The paper empirically demonstrates that: (1) near-zero training loss is required for accurate PDE solutions; (2) the ill-conditioning is worst in the residual loss component; (3) L-BFGS preconditioning reduces the condition number by ≥1000×; and (4) the combined optimizer Adam+L-BFGS dominates pure Adam or pure L-BFGS. A novel second-order optimizer NysNewton-CG (NNCG) is introduced that exploits the fast spectral decay of the Hessian to further reduce the loss and L2RE after Adam+L-BFGS stalls. Theoretically, they prove (Theorem 8.4) that ill-conditioned differential operators lead to condition numbers Ω(n_res^α), and (Theorem 8.5) that the hybrid GDND algorithm achieves fast convergence independent of the condition number.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight |
| [claims.md](logic/claims.md) | 7 falsifiable claims (C01–C07) |
| [concepts.md](logic/concepts.md) | 10 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 6 verification plans (E01–E06) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: MLP + PINN loss + optimizer pipeline |
| [solution/algorithm.md](logic/solution/algorithm.md) | NNCG (NysNewton-CG) + GDND, complexity analysis |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | 6 convergence tricks and tuning heuristics |
| [related_work.md](logic/related_work.md) | 12 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/pinn_model.py](src/execution/pinn_model.py) | MLP model, PINN loss, L2RE metric | C01, C02 |
| [execution/nncg.py](src/execution/nncg.py) | NNCG optimizer (RandomizedNystrom, NystromPCG, Armijo) | C06 |
| [execution/preconditioned_hessian.py](src/execution/preconditioned_hessian.py) | L-BFGS preconditioned Hessian spectral density | C03, C04 |
| [configs/training.md](src/configs/training.md) | Optimizer hyperparameters, iteration counts, seeds | — |
| [configs/model.md](src/configs/model.md) | MLP architecture, initialization, activation | — |
| [environment.md](src/environment.md) | Hardware, PyTorch version, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 2 tables + 5 figures |
| [tables/table1_optimizer_comparison.md](evidence/tables/table1_optimizer_comparison.md) | Best loss and L2RE across all widths (Table 1) |
| [tables/table2_nncg_results.md](evidence/tables/table2_nncg_results.md) | NNCG vs GD fine-tuning results (Table 2) |
| [tables/table3_timing.md](evidence/tables/table3_timing.md) | Per-iteration wall-clock times L-BFGS vs NNCG (Table 3) |
| [figures/fig2_loss_vs_l2re.md](evidence/figures/fig2_loss_vs_l2re.md) | Final loss vs L2RE scatter across all runs (Figure 2) |
| [figures/fig3_hessian_spectral.md](evidence/figures/fig3_hessian_spectral.md) | Hessian spectral density before/after L-BFGS preconditioning (Figure 3) |
