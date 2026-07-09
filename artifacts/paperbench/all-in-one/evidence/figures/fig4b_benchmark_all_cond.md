---
# Figure 4b: All-Conditionals C2ST vs Simulation Budget

- **Source**: Figure 4, bottom panel (4b), Section 4.1
- **Caption**: "C2ST between arbitrary Simformer-conditional distributions and their ground truth."
- **Axis labels**: X-axis = Number of simulations (10³, 10⁴, 10⁵, log scale); Y-axis = C2ST (all cond.) (0.5 to 1.0)
- **Series**: Simformer (dense), Simformer (undirected graph), Simformer (directed graph)
- **Tasks**: Tree, HMM, Two Moons, SLCP (4 subplots)

## Data Description

Ground truth from MCMC on 100 randomly sampled conditional distributions per task:
- Tree: 5000 HMC steps
- HMM: 5000 HMC steps
- Two Moons: 1000 slice + 3000 MHMCMC (step=0.01)
- SLCP: 600 slice + 2000 MHMCMC (step=0.1)

## Approximate data points (extracted from figure)

### Tree
| Method | 1k | 10k | 100k |
|--------|-----|------|------|
| Simformer | ≈0.90 | ≈0.78 | ≈0.62 |
| Simformer (undirected) | ≈0.85 | ≈0.72 | ≈0.58 |
| Simformer (directed) | ≈0.80 | ≈0.67 | ≈0.55 |

### HMM
| Method | 1k | 10k | 100k |
|--------|-----|------|------|
| Simformer | ≈0.90 | ≈0.82 | ≈0.65 |
| Simformer (undirected) | ≈0.85 | ≈0.78 | ≈0.62 |
| Simformer (directed) | ≈0.82 | ≈0.72 | ≈0.60 |

### Two Moons
| Method | 1k | 10k | 100k |
|--------|-----|------|------|
| Simformer | ≈0.85 | ≈0.72 | ≈0.57 |
| Simformer (undirected) | ≈0.85 | ≈0.70 | ≈0.57 |
| Simformer (directed) | ≈0.83 | ≈0.70 | ≈0.55 |

### SLCP
| Method | 1k | 10k | 100k |
|--------|-----|------|------|
| Simformer | ≈0.90 | ≈0.78 | ≈0.60 |
| Simformer (undirected) | ≈0.85 | ≈0.70 | ≈0.55 |
| Simformer (directed) | ≈0.80 | ≈0.65 | ≈0.52 |

**Note**: All values marked ≈ are approximate readings from Figure 4b.

## Paper-stated quantitative findings

- At 10⁵ simulations, all Simformer models on all tasks achieve C2ST (all cond.) below 0.7
- "Despite the complexity of these tasks, Simformer was able to accurately model all conditionals across all tasks"
- "Training solely on the posterior mask does not enhance performance relative to learning all conditional distributions" (confirmed by Appendix A3)
- Simformer is "well calibrated" (Appendix Fig. A9–A12) and "in most cases, also superior with respect to the loglikelihood" (Appendix Fig. A8)
