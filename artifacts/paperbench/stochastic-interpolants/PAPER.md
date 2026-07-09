---
title: "Stochastic Interpolants with Data-Dependent Couplings"
authors:
  - "Michael S. Albergo"
  - "Mark Goldstein"
  - "Nicholas M. Boffi"
  - "Rajesh Ranganath"
  - "Eric Vanden-Eijnden"
year: 2024
venue: "Proceedings of the 41st International Conference on Machine Learning (ICML 2024)"
doi: "arXiv:2310.03725"
ara_version: "1.0"
domain: "Generative models, dynamical transport, flow matching"
keywords:
  - stochastic interpolants
  - data-dependent couplings
  - flow matching
  - conditional generation
  - image inpainting
  - super-resolution
  - probability flow ODE
  - velocity field regression
  - optimal transport
  - ImageNet
claims_summary:
  - "Data-dependent couplings ρ(x0,x1)=ρ1(x1)ρ0(x0|x1) can be incorporated into stochastic interpolants without changing the quadratic regression training objective"
  - "Dependent couplings reduce transport cost upper bound compared to independent couplings, enabling simpler probability flow trajectories"
  - "Dependent-coupling stochastic interpolants outperform baselines on ImageNet inpainting (FID 1.13 vs 1.35) and set new SOTA on super-resolution (FID 2.05 valid)"
abstract: "Generative models inspired by dynamical transport of measure — such as flows and diffusions — construct a continuous-time map between two probability densities. Conventionally, one of these is the target density, only accessible through samples, while the other is taken as a simple base density that is data-agnostic. In this work, using the framework of stochastic interpolants, we formalize how to couple the base and the target densities, whereby samples from the base are computed conditionally given samples from the target in a way that is different from (but does not preclude) incorporating information about class labels or continuous embeddings. This enables us to construct dynamical transport maps that serve as conditional generative models. We show that these transport maps can be learned by solving a simple square loss regression problem analogous to the standard independent setting. We demonstrate the usefulness of constructing dependent couplings in practice through experiments in super-resolution and in-painting."
---

# Stochastic Interpolants with Data-Dependent Couplings

## Overview

This paper extends the stochastic interpolant framework (Albergo & Vanden-Eijnden, 2022; Albergo et al., 2023) to support **data-dependent couplings** between a base density ρ₀ and a target density ρ₁. Rather than drawing the base sample x₀ independently from a Gaussian, the paper formalizes the construction ρ(x₀,x₁) = ρ₁(x₁)ρ₀(x₀|x₁), where the base sample is computed as a (possibly noisy) function of the target sample. The core theoretical result shows that the velocity field governing transport under such couplings remains the unique minimizer of the same simple quadratic loss used in the standard independent setting. This enables simulation-free training via SGD.

The key practical insight is that designing x₀ = m(x₁) + σζ (a corrupted/degraded version of x₁) directly encodes the structure of inverse problems into the generative model, reducing transport costs and enabling specialized architectures. The authors demonstrate this on ImageNet inpainting (FID 1.13 vs 1.35 baseline) and super-resolution 64×64→256×256 (FID 2.05 validation, surpassing I²SB's 2.70).

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight |
| [claims.md](logic/claims.md) | 5 falsifiable claims (C01–C05) |
| [concepts.md](logic/concepts.md) | 10 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 4 verification plans (E01–E04) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: interpolant + velocity U-Net + ODE solver |
| [solution/algorithm.md](logic/solution/algorithm.md) | Training & sampling algorithms, loss formulation, complexity |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and known limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | 6 convergence and design tricks |
| [related_work.md](logic/related_work.md) | 12 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/stochastic_interpolant.py](src/execution/stochastic_interpolant.py) | Core interpolant construction and velocity loss | C01, C02 |
| [execution/inpainting.py](src/execution/inpainting.py) | Inpainting coupling: mask generation, x0 construction, forward Euler sampling | C03 |
| [execution/superresolution.py](src/execution/superresolution.py) | Super-resolution coupling: downsample/upsample, noise, ODE sampling | C04, C05 |
| [configs/training.md](src/configs/training.md) | Optimizer, LR scheduler, gradient clipping, batch size | — |
| [configs/model.md](src/configs/model.md) | U-Net architecture configurations | — |
| [environment.md](src/environment.md) | Hardware, deps, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 3 tables + 2 figures |
| [tables/table1_couplings.md](evidence/tables/table1_couplings.md) | Taxonomy of coupling strategies |
| [tables/table2_inpainting_fid.md](evidence/tables/table2_inpainting_fid.md) | FID-50k inpainting results |
| [tables/table3_superresolution_fid.md](evidence/tables/table3_superresolution_fid.md) | FID-50k super-resolution comparison |
| [figures/figure2_transport_comparison.md](evidence/figures/figure2_transport_comparison.md) | Qualitative transport comparison: GMM coupling vs conditioning vs independent |
| [figures/figure3_inpainting_samples.md](evidence/figures/figure3_inpainting_samples.md) | Qualitative inpainting samples on ImageNet-256/512 |
