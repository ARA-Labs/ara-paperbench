# Figure 2: Non-Sequential Benchmark Results (C2ST)

- **Source**: Figure 2, Section 5.2
- **Caption**: "Results on eight benchmark tasks (non-sequential methods)."
- **Experimental conditions**:
  - Methods: NPSE-VE, NPSE-VP, NPE
  - Simulation budgets: 10k and 100k (x-axis)
  - Metric: C2ST score (y-axis, range [0.5, 1.0], lower is better; 0.5 = perfect)
  - 8 benchmark tasks from sbibm (Lueckmann et al., 2021)
  - NPE results obtained from sbibm toolkit

## Qualitative Data Points (Read from Plot)

All values are approximate (≈) as the paper presents visual plots without exact numbers.

### Lotka Volterra (dim θ = 4, dim x = 20)
| Budget | NPSE-VE | NPSE-VP | NPE |
|--------|---------|---------|-----|
| 10k | ≈0.75 | ≈0.75 | ≈0.75 |
| 100k | ≈0.65 | ≈0.65 | ≈0.70 |

**Finding**: All methods achieve similar results; NPSE variants slightly outperform NPE at 100k.

### SLCP (dim θ = 5, dim x = 8)
| Budget | NPSE-VE | NPSE-VP | NPE |
|--------|---------|---------|-----|
| 10k | ≈0.72 | ≈0.72 | ≈0.78 |
| 100k | ≈0.58 | ≈0.58 | ≈0.70 |

**Finding**: NPSE-VE and NPSE-VP achieve lower (better) C2ST than NPE; VE ≈ VP.

### Gaussian Linear Uniform (dim θ = 10, dim x = 10)
| Budget | NPSE-VE | NPSE-VP | NPE |
|--------|---------|---------|-----|
| 10k | ≈0.70 | ≈0.70 | ≈0.62 |
| 100k | ≈0.62 | ≈0.62 | ≈0.55 |

**Finding**: NPE achieves lower C2ST than NPSE variants on this task; NPSE-VE ≈ NPSE-VP.

### Bernoulli GLM (dim θ = 10, dim x = 10)
| Budget | NPSE-VE | NPSE-VP | NPE |
|--------|---------|---------|-----|
| 10k | ≈0.65 | ≈0.65 | ≈0.65 |
| 100k | ≈0.58 | ≈0.58 | ≈0.58 |

**Finding**: All methods achieve roughly equivalent C2ST.

### SIR (dim θ = 2, dim x = 10)
| Budget | NPSE-VE | NPSE-VP | NPE |
|--------|---------|---------|-----|
| 10k | ≈0.62 | ≈0.73 | ≈0.60 |
| 100k | ≈0.55 | ≈0.68 | ≈0.52 |

**Finding**: NPE and NPSE-VE outperform NPSE-VP; VE recommended for low-dim (dim θ = 2).

### Two Moons (dim θ = 2, dim x = 2)
| Budget | NPSE-VE | NPSE-VP | NPE |
|--------|---------|---------|-----|
| 10k | ≈0.65 | ≈0.78 | ≈0.58 |
| 100k | ≈0.55 | ≈0.72 | ≈0.52 |

**Finding**: NPE and NPSE-VE substantially outperform NPSE-VP on this 2D task; VE preferred.

### Gaussian Mixture (dim θ = 2, dim x = 2)
| Budget | NPSE-VE | NPSE-VP | NPE |
|--------|---------|---------|-----|
| 10k | ≈0.62 | ≈0.78 | ≈0.62 |
| 100k | ≈0.53 | ≈0.70 | ≈0.53 |

**Finding**: NPE and NPSE-VE achieve equivalent C2ST; NPSE-VP is worse (VP not suitable for low-dim).

### Gaussian Linear (dim θ = 10, dim x = 10)
| Budget | NPSE-VE | NPSE-VP | NPE |
|--------|---------|---------|-----|
| 10k | ≈0.60 | ≈0.60 | ≈0.60 |
| 100k | ≈0.53 | ≈0.53 | ≈0.53 |

**Finding**: All methods achieve roughly equivalent C2ST on this simple task.

## Key Takeaways
- NPSE-VE and NPSE-VP are broadly competitive with NPE.
- NPSE outperforms NPE on hardest tasks (SLCP, Lotka Volterra).
- VE SDE outperforms VP SDE on low-dimensional tasks (SIR, Two Moons, Gaussian Mixture).
- VP SDE matches or beats VE SDE on high-dimensional tasks.
