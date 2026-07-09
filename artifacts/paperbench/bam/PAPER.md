---
title: "Batch and Match: Black-Box Variational Inference with a Score-Based Divergence"
authors: ["Diana Cai", "Chirag Modi", "Loucas Pillaud-Vivien", "Charles C. Margossian", "Robert M. Gower", "David M. Blei", "Lawrence K. Saul"]
year: 2024
venue: "arXiv (stat.ML)"
doi: "arXiv:2402.14758v2"
ara_version: "1.0"
domain: "Variational Inference / Bayesian Computation"
keywords: ["black-box variational inference", "score matching", "score-based divergence", "proximal point algorithm", "Gaussian variational family", "quadratic matrix equation", "affine invariance", "BBVI", "approximate inference", "stochastic optimization"]
claims_summary:
  - "The score-based divergence is non-negative, affine invariant, and computable for unnormalized target densities"
  - "BaM's closed-form proximal updates converge exponentially quickly to Gaussian targets in the infinite-batch limit"
  - "BaM converges faster (fewer gradient evaluations) than ADVI on Gaussian, non-Gaussian, hierarchical, and deep generative targets"
abstract: "Most leading implementations of black-box variational inference (BBVI) are based on optimizing a stochastic evidence lower bound (ELBO). But such approaches to BBVI often converge slowly due to the high variance of their gradient estimates and their sensitivity to hyperparameters. In this work, we propose batch and match (BaM), an alternative approach to BBVI based on a score-based divergence. Notably, this score-based divergence can be optimized by a closed-form proximal update for Gaussian variational families with full covariance matrices. We analyze the convergence of BaM when the target distribution is Gaussian, and we prove that in the limit of infinite batch size the variational parameter updates converge exponentially quickly to the target mean and covariance. We also evaluate the performance of BaM on Gaussian and non-Gaussian target distributions that arise from posterior inference in hierarchical and deep generative models. In these experiments, we find that BaM typically converges in fewer (and sometimes significantly fewer) gradient evaluations than leading implementations of BBVI based on ELBO maximization."
---

# Batch and Match: Black-Box Variational Inference with a Score-Based Divergence

## Overview

BaM introduces a novel score-based divergence D(q;p) = E_q[||∇log(q/p)||²_{Cov(q)}] for black-box variational inference with Gaussian families. Unlike ELBO-based methods that require stochastic gradient descent, BaM alternates between a **batch step** (sampling from the current approximation and computing target scores) and a **match step** (analytically solving a regularized optimization via a quadratic matrix equation). The covariance update Σ_{t+1}UΣ_{t+1} + Σ_{t+1} = V has a symmetric positive-definite closed-form solution, avoiding all gradient-based optimization. For Gaussian targets in the infinite-batch limit, updates converge exponentially quickly for any regularization λ>0, a stability property characteristic of proximal algorithms. Empirically, BaM outperforms ADVI and GSM across Gaussian, non-Gaussian, hierarchical Bayesian, and deep generative model benchmarks, typically requiring significantly fewer gradient evaluations.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight: slow BBVI → score divergence |
| [claims.md](logic/claims.md) | 6 falsifiable claims (C01–C06) |
| [concepts.md](logic/concepts.md) | 10 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 4 verification plans (E01–E04) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: batch step + match step + quadratic solver |
| [solution/algorithm.md](logic/solution/algorithm.md) | BaM algorithm, quadratic matrix equation, complexity O(D³) |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions: Gaussian family, differentiable log-target |
| [solution/heuristics.md](logic/solution/heuristics.md) | 5 convergence tricks (learning rate schedule, batch size selection) |
| [related_work.md](logic/related_work.md) | 12 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/bam.py](src/execution/bam.py) | BaM batch+match algorithm core implementation | C01–C06 |
| [execution/gsm.py](src/execution/gsm.py) | Gaussian score matching baseline (Algorithm 3) | C03 |
| [execution/advi.py](src/execution/advi.py) | ADVI baseline with ADAM optimizer (Algorithm 2) | C03, C05 |
| [execution/score_divergence.py](src/execution/score_divergence.py) | Score-based and Fisher divergence estimators | C01, C02 |
| [configs/training.md](src/configs/training.md) | Learning rate schedules, batch sizes, iteration counts | — |
| [configs/model.md](src/configs/model.md) | Variational family, VAE architecture for deep generative model | — |
| [environment.md](src/environment.md) | JAX, hardware, dependencies, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 8 result figures (measured outcomes only) |
| [figures/fig5_1_gaussian_targets.md](evidence/figures/fig5_1_gaussian_targets.md) | Fig 5.1: forward KL vs gradient evaluations for Gaussian targets (D=4,16,64,256) |
| [figures/fig5_2_nongaussian_targets.md](evidence/figures/fig5_2_nongaussian_targets.md) | Fig 5.2: forward KL vs gradient evaluations for sinh-arcsinh non-Gaussian targets |
| [figures/fig5_3_posteriordb.md](evidence/figures/fig5_3_posteriordb.md) | Fig 5.3: relative mean error for posteriordb Bayesian models |
| [figures/fig5_4_deep_generative.md](evidence/figures/fig5_4_deep_generative.md) | Fig 5.4: image reconstruction MSE vs iterations for deep generative model |
| [figures/figE1_wallclock.md](evidence/figures/figE1_wallclock.md) | Fig E.1: wallclock timings for Gaussian targets |
| [figures/figE3_gaussian_reverse_kl.md](evidence/figures/figE3_gaussian_reverse_kl.md) | Fig E.3: reverse KL for Gaussian targets |
| [figures/figE4_nongaussian_reverse_kl.md](evidence/figures/figE4_nongaussian_reverse_kl.md) | Fig E.4: reverse KL for non-Gaussian targets |
| [figures/figE6_posteriordb_sd_error.md](evidence/figures/figE6_posteriordb_sd_error.md) | Fig E.6: relative SD error for posteriordb models |
