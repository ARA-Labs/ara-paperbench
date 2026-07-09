---
title: "Sequential Neural Score Estimation: Likelihood-Free Inference with Conditional Score Based Diffusion Models"
authors: ["Louis Sharrock", "Jack Simons", "Song Liu", "Mark Beaumont"]
year: 2024
venue: "Proceedings of the 41st International Conference on Machine Learning (ICML 2024)"
doi: "arXiv:2210.04872v3"
ara_version: "1.0"
domain: "Simulation-Based Inference / Bayesian Computation"
keywords: ["likelihood-free inference", "simulation-based inference", "diffusion models", "score matching", "posterior estimation", "sequential inference", "normalising flows", "denoising score matching", "stochastic differential equations", "approximate Bayesian computation"]
claims_summary:
  - "NPSE (score-based diffusion) achieves comparable or superior C2ST vs NPE on 8 SBI benchmarks across simulation budgets"
  - "TSNPSE outperforms SNPE-C and TSNPE on the two hardest benchmarks (SLCP, Lotka Volterra), demonstrating better scaling"
  - "TSNPSE's truncated-proposal sequential strategy dominates all alternative corrections (SNPSE-A/B/C)"
  - "TSNPSE achieves 81% valid summary statistics on the Pyloric neuroscience problem, superior to TSNPE and SNVI at matched budgets"
  - "The VP SDE is preferable for high-dimensional tasks; VE SDE for low-dimensional tasks"
abstract: "We introduce Sequential Neural Posterior Score Estimation (SNPSE), a score-based method for Bayesian inference in simulator-based models. Our method, inspired by the remarkable success of score-based methods in generative modelling, leverages conditional score-based diffusion models to generate samples from the posterior distribution of interest. The model is trained using an objective function which directly estimates the score of the posterior. We embed the model into a sequential training procedure, which guides simulations using the current approximation of the posterior at the observation of interest, thereby reducing the simulation cost. We also introduce several alternative sequential approaches, and discuss their relative merits. We then validate our method, as well as its amortised, non-sequential, variant on several numerical examples, demonstrating comparable or superior performance to existing state-of-the-art methods such as Sequential Neural Posterior Estimation (SNPE)."
---

# Sequential Neural Score Estimation

## Overview

This paper introduces **Neural Posterior Score Estimation (NPSE)** and its sequential variant **TSNPSE** for likelihood-free (simulation-based) Bayesian inference. Given a simulator that generates synthetic data `x` from parameters `θ` under an intractable likelihood `p(x|θ)`, the goal is to sample from the posterior `p(θ|x_obs)`. NPSE trains a conditional score network `s_ψ(θ_t, x, t) ≈ ∇_θ log p_t(θ_t|x)` using a denoising score matching objective derived from a forward diffusion SDE; samples are then drawn by simulating the reverse-time process. TSNPSE embeds NPSE in a sequential loop that concentrates simulations near `x_obs` via truncated proposals, achieving simulation efficiency without requiring importance weight corrections.

The paper benchmarks NPSE and TSNPSE against NPE, SNPE-C, and TSNPE on 8 standard SBI tasks plus a real-world 31-parameter neuroscience (Pyloric) problem, demonstrating comparable or superior performance, and superior performance on challenging high-dimensional tasks.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight: intractable likelihoods motivate score-based SBI |
| [claims.md](logic/claims.md) | 5 falsifiable claims (C01–C05) about NPSE/TSNPSE performance |
| [concepts.md](logic/concepts.md) | 12 key terms: score function, SDE, DSM objective, CNF, HPR, C2ST, etc. |
| [experiments.md](logic/experiments.md) | 5 verification plans (E01–E05) covering benchmarks and Pyloric |
| [solution/architecture.md](logic/solution/architecture.md) | System design: embedding networks + score network + SDE sampler |
| [solution/algorithm.md](logic/solution/algorithm.md) | DSM objective, VE/VP SDE specs, TSNPSE algorithm, complexity |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions: truncation assumption, CNF cost, high-dim limits |
| [solution/heuristics.md](logic/solution/heuristics.md) | 8 convergence/design tricks with rationale |
| [related_work.md](logic/related_work.md) | 14 typed dependencies (SNPE, SNLE, SNRE, diffusion models, flow matching) |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/score_network.py](src/execution/score_network.py) | Score network with θ/x/t embeddings, sinusoidal t embedding | C01, C02 |
| [execution/sde.py](src/execution/sde.py) | VE-SDE and VP-SDE: drift, diffusion, transition log-density | C01–C05 |
| [execution/npse.py](src/execution/npse.py) | NPSE training loop (DSM loss) and ODE-based posterior sampling | C01, C02 |
| [execution/tsnpse.py](src/execution/tsnpse.py) | TSNPSE sequential loop: truncated proposal, HPR estimation, rejection sampling | C02–C05 |
| [configs/training.md](src/configs/training.md) | Optimizer, lr, batch sizes, early stopping, validation split, max iterations |  — |
| [configs/model.md](src/configs/model.md) | Network widths, embedding dims, SDE hyperparameters | — |
| [environment.md](src/environment.md) | Python, PyTorch, sbibm, hardware, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG: question → experiments → dead-ends → TSNPSE decision |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 4 figures (Figures 2, 3, 4c, 5) |
| [figures/fig2_nonseq_c2st.md](evidence/figures/fig2_nonseq_c2st.md) | Figure 2: C2ST for NPSE-VE/VP vs NPE on 8 benchmarks |
| [figures/fig3_seq_c2st.md](evidence/figures/fig3_seq_c2st.md) | Figure 3: C2ST for TSNPSE-VE/VP vs SNPE/TSNPE on 8 benchmarks |
| [figures/fig4c_pyloric_valid.md](evidence/figures/fig4c_pyloric_valid.md) | Figure 4c: % valid summary statistics vs simulation budget (Pyloric) |
| [figures/fig5_npse_vs_nlse.md](evidence/figures/fig5_npse_vs_nlse.md) | Figure 5: NPSE vs NLSE comparison on 4 benchmark tasks |
| [figures/fig6_seq_comparison.md](evidence/figures/fig6_seq_comparison.md) | Figure 6: TSNPSE vs SNPSE-A/B on SLCP and GLU |
| [figures/fig9_npse_vs_fmpe.md](evidence/figures/fig9_npse_vs_fmpe.md) | Figure 9: NPSE vs FMPE on 8 benchmark tasks |
