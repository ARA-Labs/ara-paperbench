---
# Figure 5c: Lotka-Volterra C2ST Performance

- **Source**: Figure 5c, Section 4.2
- **Caption**: "C2ST-performance in estimating arbitrary conditionals (right) or the posterior distribution (left) using the C2ST metric."
- **Axis labels**: X-axis = Number of simulations (10³, 10⁴, 10⁵, log scale); Y-axis = C2ST (0.5 to 1.0)
- **Series**: Simformer (dense), Simformer (undirected graph), Simformer (directed graph)
- **Conditions**: Lotka-Volterra ODE simulator; 8-layer Simformer; Gaussian observation noise σ=0.1; full time-series (no summary statistics); prior: sigmoid-transformed Normal ∈ [1,3]

## Paper-stated quantitative thresholds (from rubric and paper text)

| Metric | Threshold | Finding |
|--------|-----------|---------|
| C2ST (posterior) at 10⁵ sims | < 0.65 | "Simformer posterior closely matched the ground truth posterior generated with MCMC" |
| C2ST (arbitrary conditionals) at 10⁵ sims | < 0.75 | Good calibration across arbitrary conditionals |

## Experimental scenarios

| Scenario | Observations | Description |
|----------|-------------|-------------|
| A | 4 prey measurements at irregular times | Posterior predictive captures data and uncertainty; true params in high-probability region |
| B | 4 prey + 9 predator measurements (all irregular) | Including predator measurements reduces uncertainty in both posterior and posterior predictive |

## Paper-stated findings

- "The ground truth parameter set was indeed within regions of high posterior probability"
- "The Simformer posterior closely matched the ground truth posterior generated with MCMC"
- "Including these measurements reduces the uncertainty in both the posterior and posterior predictive distributions"
- Trained on 10⁵ Lotka-Volterra simulations
