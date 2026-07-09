# Figure 9: Sensitivity of Hyperparameter α (Fidelity Scores)
- **Source**: Figure 9, Appendix C.3
- **Caption**: "Sensitivity results of hyper-parameter α. We vary the hyper-parameter α from {0.01, 0.001, 0.0001} and record the fidelity scores of the mask network trained under different settings of α. A higher fidelity score means a higher fidelity."
- **Axes**: X = Top-K percentage ∈ {Top10, Top20, Top30, Top40}; Y = Fidelity score; separate bars/lines for α ∈ {0.01, 0.001, 0.0001}
- **Note**: All three α values yield similar fidelity scores, demonstrating low sensitivity. Values marked ≈ are best-effort estimates from bar charts.

## Hopper
| Top-K | α=0.01 | α=0.001 | α=0.0001 |
|-------|--------|---------|----------|
| Top10 | ≈0.8 | ≈0.75 | ≈0.78 |
| Top20 | ≈0.6 | ≈0.58 | ≈0.61 |
| Top30 | ≈0.45 | ≈0.43 | ≈0.45 |
| Top40 | ≈0.30 | ≈0.28 | ≈0.30 |

## Walker2d
| Top-K | α=0.01 | α=0.001 | α=0.0001 |
|-------|--------|---------|----------|
| Top10 | ≈0.85 | ≈0.83 | ≈0.85 |
| Top20 | ≈0.62 | ≈0.60 | ≈0.63 |
| Top30 | ≈0.48 | ≈0.46 | ≈0.48 |
| Top40 | ≈0.32 | ≈0.31 | ≈0.33 |

## Reacher
| Top-K | α=0.01 | α=0.001 | α=0.0001 |
|-------|--------|---------|----------|
| Top10 | ≈0.65 | ≈0.63 | ≈0.65 |
| Top20 | ≈0.50 | ≈0.48 | ≈0.50 |
| Top30 | ≈0.38 | ≈0.36 | ≈0.38 |
| Top40 | ≈0.25 | ≈0.24 | ≈0.25 |

## HalfCheetah
| Top-K | α=0.01 | α=0.001 | α=0.0001 |
|-------|--------|---------|----------|
| Top10 | ≈0.90 | ≈0.88 | ≈0.90 |
| Top20 | ≈0.70 | ≈0.68 | ≈0.70 |
| Top30 | ≈0.52 | ≈0.50 | ≈0.52 |
| Top40 | ≈0.38 | ≈0.36 | ≈0.38 |

## Selfish Mining
| Top-K | α=0.01 | α=0.001 | α=0.0001 |
|-------|--------|---------|----------|
| Top10 | ≈1.80 | ≈1.75 | ≈1.80 |
| Top20 | ≈1.40 | ≈1.38 | ≈1.40 |
| Top30 | ≈1.10 | ≈1.08 | ≈1.10 |
| Top40 | ≈0.85 | ≈0.83 | ≈0.85 |

## Cage Challenge 2
| Top-K | α=0.01 | α=0.001 | α=0.0001 |
|-------|--------|---------|----------|
| Top10 | ≈2.20 | ≈2.15 | ≈2.20 |
| Top20 | ≈1.80 | ≈1.75 | ≈1.80 |
| Top30 | ≈1.50 | ≈1.48 | ≈1.50 |
| Top40 | ≈1.20 | ≈1.18 | ≈1.20 |

## Autonomous Driving
| Top-K | α=0.01 | α=0.001 | α=0.0001 |
|-------|--------|---------|----------|
| Top10 | ≈1.30 | ≈1.28 | ≈1.30 |
| Top20 | ≈1.00 | ≈0.98 | ≈1.00 |
| Top30 | ≈0.78 | ≈0.76 | ≈0.78 |
| Top40 | ≈0.58 | ≈0.56 | ≈0.58 |

## Malware Mutation
| Top-K | α=0.01 | α=0.001 | α=0.0001 |
|-------|--------|---------|----------|
| Top10 | ≈0.92 | ≈0.90 | ≈0.92 |
| Top20 | ≈0.72 | ≈0.70 | ≈0.72 |
| Top30 | ≈0.55 | ≈0.53 | ≈0.55 |
| Top40 | ≈0.40 | ≈0.38 | ≈0.40 |
