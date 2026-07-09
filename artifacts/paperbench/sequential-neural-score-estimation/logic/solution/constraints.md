# Constraints and Limitations

## Boundary Conditions

### BC1: Truncation correctness requires support containment
The TSNPSE correctness guarantee (Proposition 3.1) holds only if the true posterior support Θ_obs is contained within HPR_ε(p^s_ψ(θ|x_obs)) for all rounds s ≥ 1. If the truncation region excludes posterior mass, the score network will learn a biased score function. In practice, this is mitigated by using a generous ε = 5×10⁻⁴.

### BC2: Computational cost of density evaluation
TSNPSE requires evaluating the posterior log-density via the instantaneous change-of-variables formula, which involves solving an augmented ODE (the trace of the Jacobian). This is significantly more expensive than a single forward pass of a normalising flow:
- TSNPE (normalising flow): single backward pass for density evaluation
- TSNPSE (CNF): multiple forward passes + gradient computation per density evaluation
This cost is mitigated by: (a) the initial hypercube pre-rejection step in sampling, (b) the energy-based parameterisation alternative (Appendix G), (c) faster ODE solvers (DPM-Solver, exponential integrators).

### BC3: Amortisation scope
NPSE (non-sequential) can in principle generate samples for any observation x, but performance degrades when x_obs is far from regions well-covered by the training data. TSNPSE is not amortised — a separate model must be trained per observation x_obs.

### BC4: Applicable SDE types
The paper demonstrates NPSE/TSNPSE with VE SDE and VP SDE. The framework is general and supports any SDE for which the transition density p_{t|0}(θ_t|θ_0) and its score are available in closed form.

### BC5: Sinusoidal embedding time range
The sinusoidal embedding formula in Eq. (138) is designed for t ∈ (0, 1]. Both VE and VP SDEs use this time interval in the paper's implementation.

### BC6: Pyloric simulator — invalid outputs
Over 99% of prior samples input to the Pyloric simulator result in ill-defined (NaN) summary statistics. Invalid statistics are replaced by values 2 standard deviations below the prior predictive of each statistic, following Deistler et al. (2022a).

## Known Limitations

### L1: Sequential overhead vs. TSNPE
TSNPSE is more computationally expensive than TSNPE per round because likelihood evaluation requires ODE solving. For simulators with fast evaluation, this overhead is significant; for expensive simulators, it is negligible.

### L2: Fixed hyperparameters across tasks
The same network architecture and hyperparameters are used across all experiments without task-specific tuning. Performance may be improved with per-task hyperparameter search (unlike FMPE, which tunes per task).

### L3: SNPSE-C requires additional approximations
SNPSE-C requires estimating the proposal prior score ∇_θ log ˜p^r_t(θ_t), which introduces additional approximation errors and computational cost. Empirically, SNPSE-C fails to produce meaningful results (C2ST ≈ 1).

### L4: Multiple observations require different approach
NPSE as described handles single observations x_obs. Multi-observation inference p(θ|x¹_obs,...,xⁿ_obs) requires the compositional score approach of Geffner et al. (2023) or the alternative in Appendix D; naive concatenation is sample-inefficient.

### L5: Architecture is relatively simple
The paper uses a relatively simple MLP-based architecture. More specialised architectures (e.g., attention, U-Net) used in other diffusion model applications may further improve performance.
