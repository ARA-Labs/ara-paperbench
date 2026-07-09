# Heuristics

## H01: σ_max set to maximum pairwise Euclidean distance in training data
- **Rationale**: For the VE SDE, σ_max determines the noise level at t=1. Setting it to the maximum pairwise Euclidean distance in the training data (Technique 1 in Song & Ermon, 2020) ensures the forward process sufficiently noises the data so p_T ≈ N(0, σ²_max I) is a reasonable approximation to the reference distribution.
- **Sensitivity**: high — if σ_max is too small, the reference distribution is not well-approximated; if too large, training is inefficient.
- **Bounds**: σ_max > diameter of the training data in parameter space. For sequential methods, use first-round training data to set σ_max.
- **Code ref**: [src/execution/sde.py]
- **Source**: Appendix E.3.1

## H02: σ_min = 0.01 for 2D experiments; σ_min = 0.05 for higher-dimensional
- **Rationale**: The minimum noise level σ_min controls the resolution of the diffusion path. Lower-dimensional problems have tighter posterior distributions that require smaller minimum noise to avoid over-smoothing. Higher-dimensional problems are more tolerant of larger σ_min.
- **Sensitivity**: medium
- **Bounds**: σ_min ∈ {0.01, 0.05}; 2D tasks (SIR, Two Moons) use 0.01; all others use 0.05.
- **Code ref**: [src/execution/sde.py]
- **Source**: Appendix E.3.1

## H03: VP SDE parameters β_min=0.1, β_max=11.0
- **Rationale**: These values follow Song & Ermon (2020) and ensure the VP SDE noises the data to near-Gaussian in [0,1]. The linear schedule β_t = β_min + t(β_max - β_min) provides a smooth transition.
- **Sensitivity**: medium — affects variance schedule and training dynamics.
- **Bounds**: β_min = 0.1, β_max = 11.0 (fixed).
- **Code ref**: [src/execution/sde.py]
- **Source**: Appendix E.3.1

## H04: Early stopping with patience=1000 steps on 15% validation split
- **Rationale**: Prevents overfitting with limited simulation budgets. Validation loss on held-out data provides a reliable stopping criterion. 15% is a standard fraction that balances training data size and validation reliability.
- **Sensitivity**: medium — too short patience leads to underfitting; too long wastes compute.
- **Bounds**: patience = 1000 steps; validation split = 15%; maximum 3000 iterations.
- **Code ref**: [src/execution/npse.py]
- **Source**: Appendix E.3.2

## H05: Batch size 50 (non-seq, N≤10k), 200 (seq, N≤10k), 500 (N=100k)
- **Rationale**: Larger simulation budgets allow larger batches, improving gradient estimates. Sequential experiments have larger accumulated datasets, justifying larger batch sizes. Non-sequential with small budgets requires small batches to see the whole dataset during training.
- **Sensitivity**: medium
- **Bounds**: batch_size ∈ {50, 200, 500} depending on method and budget.
- **Code ref**: [src/execution/npse.py]
- **Source**: Appendix E.3.2

## H06: Truncation threshold ε = 5×10⁻⁴ for HPR estimation
- **Rationale**: Small ε ensures the truncated region contains almost all posterior mass (1 - 5×10⁻⁴ = 99.95%), making Proposition 3.1 approximately valid. Larger ε would be more aggressive but risks truncating posterior mass.
- **Sensitivity**: medium — too large ε truncates posterior mass and introduces bias; too small ε reduces simulation efficiency.
- **Bounds**: ε = 5×10⁻⁴ (fixed across all experiments).
- **Code ref**: [src/execution/tsnpse.py]
- **Source**: Appendix E.3.3

## H07: Pre-rejection hypercube step before expensive likelihood evaluation
- **Rationale**: Computing log-density via the probability flow ODE is expensive (multiple forward passes + trace). A cheap preliminary rejection step (checking if θ is within the bounding box of the posterior samples) filters most prior samples quickly before the expensive step.
- **Sensitivity**: low — hypercube is a necessary but not sufficient condition; false positives are handled by the likelihood threshold.
- **Bounds**: Bounding box = [min, max] of posterior samples in each dimension.
- **Code ref**: [src/execution/tsnpse.py]
- **Source**: Appendix E.3.3

## H08: 20000 samples for HPR estimation per round
- **Rationale**: A sufficiently large number of samples is needed for an accurate empirical estimate of the posterior's HPR. 20000 provides a reliable sample from the approximate posterior for computing the log-density quantile κ.
- **Sensitivity**: medium — too few samples give noisy HPR estimates; too many are computationally expensive.
- **Bounds**: 20000 samples (fixed across all TSNPSE experiments).
- **Code ref**: [src/execution/tsnpse.py]
- **Source**: Appendix E.3.3
