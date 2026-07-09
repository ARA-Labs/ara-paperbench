---
# Constraints and Limitations

## Boundary Conditions

### BC1: Sequence length scalability
- **Condition**: Transformer attention scales as O(d²) in number of tokens d. For simulators with high-dimensional observations (e.g., x ∈ ℝ^8192 gravitational waves), full tokenization is computationally prohibitive.
- **Mitigation**: Use an embedding network to compress high-dimensional observations into a single token, but this sacrifices individual condition-state control per data element.
- **Threshold**: Practically tested up to ~20 tokens for benchmark tasks; Lotka-Volterra and SIRD use variable-length sequences up to ~50 tokens.

### BC2: Sampling speed
- **Condition**: Generating samples requires solving the reverse SDE with 500 Euler-Maruyama steps. This is slower than normalizing flows (single forward pass) but faster than MCMC.
- **Measured**: "Accurate inference is achievable with as few as 50 evaluation steps, leading to sampling times of a few seconds for 10k samples."
- **Mitigation**: Distillation (Song et al., 2021a), alternative SDE solvers (Gonzalez et al., 2023), or adapted SDEs (Albergo et al., 2023) may improve speed.

### BC3: Log-probability evaluation
- **Condition**: Unlike normalizing flows, the Simformer does not provide cheap log-probability evaluation; computing log p(x) requires solving the probability flow ODE, which is computationally expensive.
- **Impact**: Cannot easily integrate into MCMC frameworks that require frequent likelihood evaluations. MAP computation and Langevin-MCMC (using the score directly) are viable alternatives.

### BC4: Directed graph mask validity at t > 0
- **Condition**: Directed graphical model structure is only faithfully enforced at t=0. At t>0, the marginal pt(x̂_t) does not generally respect the original DAG structure (directed models not closed under marginalization).
- **Implication**: Conditional independence guarantees weaken during the diffusion process; the model may attend to variables it should be independent of at intermediate noise levels.
- **Mitigation**: Dynamic mask updates using Webb et al. (2018) algorithm handle conditioning-induced dependencies at t=0.

### BC5: Post-hoc prior/likelihood modification accuracy
- **Condition**: Affine modifications to the score (tempering or shifting prior/likelihood) are only exact for Gaussian families. For non-Gaussian distributions, the approximation may fail when modifications diverge significantly from the training distribution.
- **Measured**: Increasing prior variance works less well than decreasing it (Figure A3, toy example).

### BC6: Guided diffusion accuracy without self-recurrence
- **Condition**: General guidance without self-recurrence (r=0) is approximate and may produce slightly noisy or inaccurate samples for complex constraints.
- **Mitigation**: Using self-recurrence (r>0) markedly improves accuracy but requires r× more computational resources.

### BC7: Simulation budget requirements
- **Condition**: Simformer requires sufficient simulations for convergence. At very low budgets (10³), performance degrades, though it still outperforms NPE on most tasks.
- **Minimum effective budget**: ~10³ simulations for simple tasks; ~10⁵ for complex tasks (Lotka-Volterra, SIRD, Hodgkin-Huxley).

## Assumptions

- **A1**: The simulator is a black box providing (θ, x) pairs; no likelihood evaluations needed.
- **A2**: The VESDE/VPSDE does not introduce additional cross-variable correlations (valid for these SDE families).
- **A3**: The graphical model assumed by M_E correctly reflects the simulator's conditional independence structure (wrong M_E may hurt performance on tasks with incorrect structural assumptions).
- **A4**: For function-valued parameters, the Kolmogorov Extension Theorem applies: finite-dimensional marginals at random subsampled time points characterize the full infinite-dimensional distribution.
- **A5**: For joint distribution estimation, the score decomposes additively across i.i.d. observations: s(θ,x₁,...,xₙ) = Σᵢ s(θ,xᵢ).

## Known Failure Modes

- **High-dimensional data with complex posteriors**: Estimating the full joint may be harder than just the posterior when x is high-dimensional (e.g., images, long time series). In such cases, restrict M_C to only sample posterior and missing-data masks.
- **Very long token sequences**: Memory scales quadratically; sparse attention masks reduce this but require knowledge of the dependency structure.
- **Large prior/likelihood modifications post-hoc**: Affine score transformations have limited range of validity.
