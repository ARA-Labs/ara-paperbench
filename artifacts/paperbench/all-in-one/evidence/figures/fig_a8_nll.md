---
# Figure A8: Average Negative Log-Likelihood

- **Source**: Figure A8, Appendix A3.1
- **Caption**: "Average negative loglikelihood of the true parameter for NPE, NLE, and all Simformer variants. Evaluating both the likelihood (top row) and posterior (bottom row)."
- **Axis labels**: X-axis = Number of simulations (log scale); Y-axis = NLL (likelihood, top) and NLL (posterior, bottom)
- **Series**: Simformer, Simformer (undirected graph), Simformer (directed graph), NLE (top row), NPE (bottom row)
- **Conditions**: VESDE; 4 benchmark tasks; 5000 samples from joint distribution; log-probability via probability flow ODE

## Approximate NLL values by task (extracted from Figure A8)

### NLL (likelihood) — top row
| Task | Method | 1k | 10k | 100k |
|------|--------|----|-----|------|
| Linear Gaussian | Simformer | ≈3.5 | ≈3.2 | ≈3.0 |
| Linear Gaussian | NLE | ≈3.2 | ≈3.0 | ≈3.0 |
| Mixture Gaussian | Simformer | ≈1.6 | ≈1.45 | ≈1.4 |
| Mixture Gaussian | NLE | ≈1.5 | ≈1.4 | ≈1.4 |
| Two Moons | Simformer | ≈-3.8 | ≈-4.0 | ≈-4.1 |
| Two Moons | NLE | ≈-3.9 | ≈-4.1 | ≈-4.1 |
| SLCP | Simformer | ≈15 | ≈12 | ≈10.5 |
| SLCP | NLE | ≈12 | ≈10.5 | ≈10.2 |

### NLL (posterior) — bottom row
| Task | Method | 1k | 10k | 100k |
|------|--------|----|-----|------|
| Linear Gaussian | Simformer | ≈0.3 | ≈-0.1 | ≈-0.3 |
| Linear Gaussian | NPE | ≈0.2 | ≈-0.1 | ≈-0.3 |
| Mixture Gaussian | Simformer | ≈1.3 | ≈1.2 | ≈1.15 |
| Mixture Gaussian | NPE | ≈1.25 | ≈1.15 | ≈1.12 |
| Two Moons | Simformer | ≈-3.1 | ≈-3.3 | ≈-3.4 |
| Two Moons | NPE | ≈-3.2 | ≈-3.35 | ≈-3.45 |
| SLCP | Simformer | ≈-3.0 | ≈-3.2 | ≈-3.4 |
| SLCP | NPE | ≈-3.1 | ≈-3.3 | ≈-3.5 |

**Note**: All values marked ≈ are approximate. NLL is evaluated via probability flow ODE for Simformer (not SDE), introducing a systematic discrepancy vs. SDE sampling quality. NPE/NLE are directly trained to minimize NLL, giving them a natural advantage on this metric.

## Key Findings

- Simformer NLL is competitive with NPE/NLE on most tasks despite not directly minimizing NLL
- NLL discrepancy between SDE sampling quality (C2ST) and ODE log-probability: "the difference is due to the discrepancy between SDE sampling and ODE log probability evaluation and the fact that Simformer is not trained to minimize loglikelihood"
- In some cases NLE or NPE outperform Simformer on NLL metric, while Simformer may still win on C2ST
- "In most cases, the results agree with the C2ST evaluation"
