---
# Claims

## C01: Simformer outperforms NPE on benchmark posterior approximation tasks
- **Statement**: The Simformer with a dense attention mask achieves lower C2ST error (closer to 0.5) than NPE on three out of four SBIBM benchmark tasks (Gaussian Mixture, Two Moons, SLCP) across all simulation budgets tested (10³, 10⁴, 10⁵). It achieves similar performance on Gaussian Linear except at 10k simulations.
- **Status**: supported
- **Falsification criteria**: If NPE achieves equal or lower C2ST error than the dense Simformer on a majority of benchmark tasks at the same simulation budget.
- **Proof**: [E01]
- **Dependencies**: none
- **Tags**: benchmark, C2ST, NPE, posterior, simulation-efficiency

## C02: Structured attention masks improve simulation efficiency up to 10×
- **Statement**: Equipping Simformer with an attention mask matching the simulator's dependency structure (undirected or directed graph) reduces the simulation budget needed to reach a given C2ST level by approximately an order of magnitude on average across tasks with notable independence structure (Linear Gaussian, SLCP).
- **Status**: supported
- **Falsification criteria**: If structured-mask Simformer variants require comparable or more simulations than the dense Simformer to achieve similar C2ST performance.
- **Proof**: [E01]
- **Dependencies**: C01
- **Tags**: attention mask, simulation efficiency, dependency structure, graphical model

## C03: Simformer accurately estimates all arbitrary conditionals of the joint distribution
- **Statement**: A single trained Simformer network can produce well-calibrated samples from any conditional of p(θ, x), including posteriors, likelihoods, and arbitrary parameter/data conditionals, as verified by C2ST against MCMC ground truth on 100 randomly sampled conditionals across Tree, HMM, Two Moons, and SLCP tasks.
- **Status**: supported
- **Falsification criteria**: If C2ST for arbitrary conditionals exceeds 0.7 for all Simformer variants on any task at 10⁵ simulations; or if training only on the posterior mask substantially improves performance.
- **Proof**: [E02]
- **Dependencies**: C01
- **Tags**: arbitrary conditionals, joint distribution, all-in-one, C2ST, MCMC

## C04: Simformer handles unstructured/missing data and function-valued parameters
- **Statement**: The Simformer can perform inference for Lotka-Volterra with irregularly placed observations of varying numbers across species (unstructured data) and for SIRD with an infinite-dimensional time-varying contact rate parameter, producing well-calibrated posteriors and posterior predictives in both cases.
- **Status**: supported
- **Falsification criteria**: If posterior predictives fail to capture the observed data within 99% quantiles, or if the ground truth parameter lies outside high-probability posterior regions.
- **Proof**: [E03, E04]
- **Dependencies**: C03
- **Tags**: unstructured data, missing data, function-valued parameters, Lotka-Volterra, SIRD

## C05: Guided diffusion enables conditioning on intervals without retraining
- **Statement**: The Simformer can condition on observation intervals (e.g., energy below the lowest 10% quantile) using a general guidance formulation with constraint function c(x̂) = x̂ − u and scaling s(t) = 1/σ(t)², producing samples that satisfy the constraint while remaining consistent with the data likelihood.
- **Status**: supported
- **Falsification criteria**: If samples from guided diffusion violate the specified energy constraint at test time, or if the posterior predictive voltage trace diverges from observations.
- **Proof**: [E05]
- **Dependencies**: C03
- **Tags**: guided diffusion, interval conditioning, Hodgkin-Huxley, energy constraint, Algorithm 1

## C06: The 'all-in-one' training objective does not hurt posterior-only performance
- **Statement**: Training the Simformer on all conditional distributions (joint, posterior, likelihood, random masks) achieves similar or better C2ST for the posterior compared to training exclusively on the posterior mask (Simformer posterior-only ≈ NPSE baseline).
- **Status**: supported
- **Falsification criteria**: If the posterior-only Simformer variant significantly outperforms the all-conditionals Simformer in C2ST on any benchmark task.
- **Proof**: [E01, E02]
- **Dependencies**: C01, C03
- **Tags**: training objective, posterior-only, all-conditionals, free lunch
