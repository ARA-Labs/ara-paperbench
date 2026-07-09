# Figure 8: Sensitivity of Hyperparameter λ Across All Applications
- **Source**: Figure 8, Appendix C.3
- **Caption**: "Sensitivity results of hyper-parameter λ. We vary the hyper-parameter λ from {0.1, 0.01, 0.001} and record the performance of the agent after refining. A smaller choice of λ means a smaller reward bonus for exploration."
- **Axes**: X = p value ∈ {0, 0.25, 0.5, 0.75, 1.0}; Y = Performance; separate curves for p ∈ {0, 0.25, 0.5, 0.75, 1.0}
- **Note**: The figure shows performance as a function of p for each value of λ. Key observation: any λ > 0 provides improvement; λ=0.01 generally best (except Selfish Mining).

## Hopper (Y-axis range ≈ 3650–3665)
| λ | p=0 | p=0.25 | p=0.5 | p=0.75 | p=1.0 |
|---|-----|--------|-------|--------|-------|
| 0.1 | ≈3645 | ≈3661 | ≈3658 | ≈3650 | ≈3647 |
| 0.01 | ≈3648 | ≈3663 | ≈3660 | ≈3655 | ≈3652 |
| 0.001 | ≈3646 | ≈3660 | ≈3659 | ≈3653 | ≈3650 |

## Walker2d (Y-axis range ≈ 3965–3980)
| λ | p=0.25 (best) |
|---|---------------|
| 0.1 | ≈3979 |
| 0.01 | ≈3980 |
| 0.001 | ≈3978 |

## Reacher (Y-axis range ≈ -4.0 to -2.5)
| λ | p=0.5 (best) |
|---|--------------|
| 0.1 | ≈-2.8 |
| 0.01 | ≈-2.7 |
| 0.001 | ≈-2.8 |

## HalfCheetah (Y-axis range ≈ 2110–2140)
| λ | p=0.5 (best) |
|---|--------------|
| 0.1 | ≈2135 |
| 0.01 | ≈2138 |
| 0.001 | ≈2134 |

## Selfish Mining (Y-axis range ≈ 15.0–16.5)
| λ | p=0.25 (best) |
|---|---------------|
| 0.1 | ≈16.1 |
| 0.01 | ≈16.4 |
| 0.001 | ≈16.5 |

## Cage Challenge 2 (less negative = better)
| λ | p=0.5 (best) |
|---|--------------|
| 0.1 | ≈-21.0 |
| 0.01 | ≈-20.2 |
| 0.001 | ≈-20.5 |

## Safe Driving (Autonomous Driving)
| λ | p=0.25 (best) |
|---|---------------|
| 0.1 | ≈16.5 |
| 0.01 | ≈17.0 |
| 0.001 | ≈16.8 |

## Malware Mutation (Y-axis range ≈ 47.5–57.5)
| λ | p=0.5 (best) |
|---|--------------|
| 0.1 | ≈56.0 |
| 0.01 | ≈57.5 |
| 0.001 | ≈57.0 |
