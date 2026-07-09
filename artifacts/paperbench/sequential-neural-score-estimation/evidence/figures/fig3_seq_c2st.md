# Figure 3: Sequential Benchmark Results (C2ST)

- **Source**: Figure 3, Section 5.2
- **Caption**: "Results on eight benchmark tasks (sequential methods)."
- **Experimental conditions**:
  - Methods: TSNPSE-VE, TSNPSE-VP, SNPE (= SNPE-C), TSNPE
  - Simulation budgets: 10k and 100k (x-axis)
  - Metric: C2ST score (y-axis, range [0.5, 1.0], lower is better)
  - R = 10 rounds; M = N/R simulations per round
  - SNPE-C and TSNPE results from sbibm toolkit

## Qualitative Data Points (Read from Plot)

All values are approximate (≈) as the paper presents visual plots without exact numbers.

### Lotka Volterra (dim θ = 4, dim x = 20)
| Budget | TSNPSE-VE | TSNPSE-VP | SNPE | TSNPE |
|--------|-----------|-----------|------|-------|
| 10k | ≈0.65 | ≈0.65 | ≈0.75 | ≈0.72 |
| 100k | ≈0.57 | ≈0.57 | ≈0.70 | ≈0.68 |

**Finding**: TSNPSE variants outperform SNPE and TSNPE on this challenging task.

### SLCP (dim θ = 5, dim x = 8)
| Budget | TSNPSE-VE | TSNPSE-VP | SNPE | TSNPE |
|--------|-----------|-----------|------|-------|
| 10k | ≈0.68 | ≈0.68 | ≈0.78 | ≈0.75 |
| 100k | ≈0.55 | ≈0.55 | ≈0.72 | ≈0.68 |

**Finding**: TSNPSE variants substantially outperform SNPE and TSNPE on SLCP.

### Gaussian Linear Uniform (dim θ = 10, dim x = 10)
| Budget | TSNPSE-VE | TSNPSE-VP | SNPE | TSNPE |
|--------|-----------|-----------|------|-------|
| 10k | ≈0.72 | ≈0.65 | ≈0.63 | ≈0.62 |
| 100k | ≈0.62 | ≈0.58 | ≈0.56 | ≈0.55 |

**Finding**: TSNPSE-VP competitive with SNPE and TSNPE; TSNPSE-VE slightly worse.

### Bernoulli GLM (dim θ = 10, dim x = 10)
| Budget | TSNPSE-VE | TSNPSE-VP | SNPE | TSNPE |
|--------|-----------|-----------|------|-------|
| 10k | ≈0.62 | ≈0.60 | ≈0.64 | ≈0.62 |
| 100k | ≈0.55 | ≈0.53 | ≈0.58 | ≈0.55 |

**Finding**: TSNPSE achieves lower or equivalent C2ST vs. SNPE and TSNPE.

### SIR (dim θ = 2, dim x = 10)
| Budget | TSNPSE-VE | TSNPSE-VP | SNPE | TSNPE |
|--------|-----------|-----------|------|-------|
| 10k | ≈0.60 | ≈0.72 | ≈0.58 | ≈0.60 |
| 100k | ≈0.53 | ≈0.65 | ≈0.52 | ≈0.53 |

**Finding**: TSNPSE-VE competitive with SNPE and TSNPE; TSNPSE-VP worse (VP not suitable for 2D).

### Two Moons (dim θ = 2, dim x = 2)
| Budget | TSNPSE-VE | TSNPSE-VP | SNPE | TSNPE |
|--------|-----------|-----------|------|-------|
| 10k | ≈0.63 | ≈0.78 | ≈0.58 | ≈0.62 |
| 100k | ≈0.55 | ≈0.72 | ≈0.52 | ≈0.55 |

**Finding**: TSNPSE-VE competitive with TSNPE; TSNPSE-VP significantly worse.

### Gaussian Mixture (dim θ = 2, dim x = 2)
| Budget | TSNPSE-VE | TSNPSE-VP | SNPE | TSNPE |
|--------|-----------|-----------|------|-------|
| 10k | ≈0.60 | ≈0.78 | ≈0.60 | ≈0.62 |
| 100k | ≈0.53 | ≈0.70 | ≈0.53 | ≈0.55 |

**Finding**: TSNPSE-VE matches SNPE; TSNPSE-VP worse due to high-dim VP preference.

### Gaussian Linear (dim θ = 10, dim x = 10)
| Budget | TSNPSE-VE | TSNPSE-VP | SNPE | TSNPE |
|--------|-----------|-----------|------|-------|
| 10k | ≈0.60 | ≈0.60 | ≈0.58 | ≈0.60 |
| 100k | ≈0.53 | ≈0.53 | ≈0.52 | ≈0.53 |

**Finding**: All methods roughly equivalent on this simple task; TSNPSE competitive.

## Key Takeaways
- TSNPSE outperforms SNPE and TSNPE on the two hardest tasks (SLCP, Lotka Volterra).
- Results mixed on simpler/lower-dimensional tasks.
- VP SDE preferred for high-dimensional tasks; VE SDE for low-dimensional.
- TSNPSE achieves meaningful improvement over non-sequential NPSE on hard tasks.
