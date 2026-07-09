---
# Figure 4a: Benchmark Posterior C2ST vs Simulation Budget

- **Source**: Figure 4, top panel (4a), Section 4.1
- **Caption**: "Simformer performance on benchmark tasks. (a) Classifier Two-Sample Test (C2ST) accuracy between Simformer- and ground-truth posteriors."
- **Axis labels**: X-axis = Number of simulations (10³, 10⁴, 10⁵, log scale); Y-axis = C2ST posterior (0.5 to 1.0)
- **Series**: NPE (solid), Simformer (dense, solid), Simformer (undirected graph, dashed), Simformer (directed graph, dotted)

## Qualitative Data (extracted from figure — exact values not tabulated in paper)

| Task | Key qualitative finding |
|------|------------------------|
| Linear Gaussian | Simformer undirected + directed reach near-0.5 at 10³ sims; NPE matches at 10⁴; Dense Simformer underperforms at low sims due to no structure exploitation |
| Mixture Gaussian | Simformer (all variants) outperform NPE across all budgets; dense Simformer ~0.5 at 10⁵ |
| Two Moons | Simformer (all variants) substantially outperform NPE; NPE still ~0.55 at 10⁵ while Simformer ~0.51 |
| SLCP | Largest gap: Simformer undirected/directed reach ~0.5 at 10⁴; NPE needs ~10⁵ for similar performance |

## Approximate data points (extracted from figure)

### Linear Gaussian
| Method | 1k | 10k | 100k |
|--------|-----|------|------|
| NPE | ≈0.75 | ≈0.55 | ≈0.52 |
| Simformer | ≈0.80 | ≈0.60 | ≈0.52 |
| Simformer (undirected) | ≈0.60 | ≈0.52 | ≈0.50 |
| Simformer (directed) | ≈0.52 | ≈0.50 | ≈0.50 |

### Mixture Gaussian
| Method | 1k | 10k | 100k |
|--------|-----|------|------|
| NPE | ≈0.82 | ≈0.70 | ≈0.60 |
| Simformer | ≈0.75 | ≈0.60 | ≈0.55 |
| Simformer (undirected) | ≈0.73 | ≈0.60 | ≈0.55 |
| Simformer (directed) | ≈0.73 | ≈0.60 | ≈0.55 |

### Two Moons
| Method | 1k | 10k | 100k |
|--------|-----|------|------|
| NPE | ≈0.90 | ≈0.75 | ≈0.60 |
| Simformer | ≈0.80 | ≈0.62 | ≈0.55 |
| Simformer (undirected) | ≈0.80 | ≈0.62 | ≈0.55 |
| Simformer (directed) | ≈0.80 | ≈0.62 | ≈0.55 |

### SLCP
| Method | 1k | 10k | 100k |
|--------|-----|------|------|
| NPE | ≈1.00 | ≈0.90 | ≈0.75 |
| Simformer | ≈0.95 | ≈0.80 | ≈0.65 |
| Simformer (undirected) | ≈0.88 | ≈0.68 | ≈0.55 |
| Simformer (directed) | ≈0.83 | ≈0.62 | ≈0.52 |

**Note**: All values marked ≈ are approximate readings from Figure 4a.

## Paper-stated quantitative findings

- "Averaged across all benchmark tasks and observations, the Simformer required about 10 times fewer simulations than NPE"
- "The only exception was the Gaussian linear task with 10k simulations" (where NPE was slightly better than dense Simformer)
- "Incorporating domain knowledge into the attention mask of the transformer led to further improvements in the accuracy of the Simformer, particularly in tasks with sparser dependency structures, such as the Linear Gaussian (fully factorized) and SLCP (4 i.i.d. observations)"
- C2ST metric: 0.5 = perfect alignment, 1.0 = completely distinguishable
