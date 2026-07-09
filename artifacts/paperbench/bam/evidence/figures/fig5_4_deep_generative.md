# Figure 5.4: Deep Generative Model — Image Reconstruction MSE
- **Source**: Figure 5.4, Section 5.3
- **Caption**: "(a) Image reconstruction across iterations with batch size, B = 300. (b) Reconstruction error for varying batch sizes."

## Experimental Conditions
- Model: VAE on CIFAR-10; Gaussian likelihood with σ²=0.1; z∈R^256; x∈R^3072
- Architecture: 5-layer convolutional encoder/decoder
- Evaluation: MSE between reconstructed image Ω(E[z'|x'], θ̂) and test image x'
- Initialization: N(0, I) for all VI methods
- Pilot: 100 iterations for learning rate selection; Main: 1000 iterations

## Panel (b): Reconstruction Error vs. Iterations

### Batch Size B=10
| Method | Notes |
|--------|-------|
| BaM | Performs poorly (MSE > 0.2); batch too small relative to D=256 |
| ADVI | Converges to reasonable MSE |
| GSM | Baseline performance |
| Amortized VI | Fixed baseline (encoder network) |

### Batch Size B=100
| Method | Notes |
|--------|-------|
| BaM | Becoming competitive |
| ADVI | Similar or slower than B=10 (no batch size benefit) |
| GSM | Similar |

### Batch Size B=300
| Method | Notes |
|--------|-------|
| BaM | Converges order of magnitude (or more) faster than ADVI and GSM in iterations |
| ADVI | Converges, but requires many more iterations |
| GSM | Similar to ADVI |

## Key Quantitative Comparisons (from paper text)
| Comparison | Detail |
|------------|--------|
| 3000 gradient budget (ADVI) | B=10, T=300 → achieves lowest ADVI MSE |
| 3000 gradient budget (BaM) | B=300, T=10 → achieves comparable MSE to ADVI |
| Wallclock advantage of BaM | BaM B=300 converges faster in wallclock time (more parallelizable) |
| BaM vs Amortized VI | Both BaM and ADVI eventually achieve lower MSE than AVI (full vs. factorized covariance) |

## Selected BaM Learning Rates
| B | λ (selected) | Search grid |
|---|-------------|-------------|
| 10 | 0.1 | {0.01, 0.1, 0.2, 10} |
| 100 | 50 | {2, 20, 50, 100, 200} |
| 300 | 7500 | {1000, 5000, 7500, 10000} |

ADVI learning rate: ℓ=0.02 consistently best from {0.001, 0.01, 0.02, 0.05}.
