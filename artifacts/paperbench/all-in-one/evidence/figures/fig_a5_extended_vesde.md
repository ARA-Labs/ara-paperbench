---
# Figure A5: Extended VESDE Benchmark Results

- **Source**: Figure A5, Appendix A3.1
- **Caption**: "Extended benchmark results for the VESDE. In addition to NPE, we also run NRE, NLE, and NSPE. (a) Shows performance in terms of C2ST for SBIBM tasks. (b) Shows performance in terms of C2ST for all conditional distributions."
- **Axis labels**: X-axis = Number of simulations (log scale); Y-axis = C2ST (0.6 to 1.0)
- **Series**: Simformer, Simformer (posterior only), Simformer (directed graph), Simformer (undirected graph), NPE, NSPE, NLE, NRE

## Key Findings from Extended Benchmark

| Method Pair | Finding |
|-------------|---------|
| Simformer vs Simformer (posterior only) | Similar performance; posterior-only ≈ NPSE architecture ablation |
| Simformer (posterior only) vs NPSE | Similar (differ only in architecture: transformer vs MLP) |
| Simformer (dense) vs NPE | Simformer outperforms on most tasks/budgets |
| SLCP: NLE vs NPE | NLE outperforms NPE (simple likelihood helps); Simformer benefits from joint estimation |
| VESDE vs VPSDE (see Fig A6) | VESDE better on Two Moons; VPSDE slightly better on SLCP |

## Approximate C2ST values at 100k simulations

### Posterior C2ST (Section a)
| Task | Simformer | Simformer (post. only) | Simformer (directed) | Simformer (undirected) | NPE | NSPE | NLE | NRE |
|------|-----------|----------------------|---------------------|----------------------|-----|------|-----|-----|
| Linear Gaussian | ≈0.52 | ≈0.52 | ≈0.50 | ≈0.50 | ≈0.52 | ≈0.52 | ≈0.50 | ≈0.60 |
| Mixture Gaussian | ≈0.55 | ≈0.55 | ≈0.55 | ≈0.55 | ≈0.60 | ≈0.58 | ≈0.55 | ≈0.65 |
| Two Moons | ≈0.55 | ≈0.55 | ≈0.55 | ≈0.55 | ≈0.62 | ≈0.57 | ≈0.58 | ≈0.65 |
| SLCP | ≈0.65 | ≈0.65 | ≈0.52 | ≈0.55 | ≈0.75 | ≈0.68 | ≈0.58 | ≈0.80 |

### All-Conditionals C2ST (Section b)
| Task | Simformer | Simformer (post. only) | Simformer (directed) | Simformer (undirected) | NSPE |
|------|-----------|----------------------|---------------------|----------------------|------|
| Tree | ≈0.62 | ≈0.63 | ≈0.55 | ≈0.58 | ≈0.72 |
| HMM | ≈0.65 | ≈0.66 | ≈0.60 | ≈0.62 | ≈0.75 |
| Two Moons | ≈0.57 | ≈0.58 | ≈0.55 | ≈0.57 | ≈0.68 |
| SLCP | ≈0.60 | ≈0.61 | ≈0.52 | ≈0.55 | ≈0.72 |

**Note**: All values marked ≈ are approximate readings from Figure A5.

## Paper-stated qualitative findings

- "These two approaches [Simformer (posterior only) and NPSE] do perform similarly."
- "Training solely on the posterior mask does not enhance performance relative to learning all conditional distributions."
- "In cases like the SLCP, where the likelihood is relatively simple, there appears to be an added advantage in learning both the posterior and the likelihood distributions."
- "The Simformer approach estimates both quantities jointly, it may benefit from this additional information."
