# Training Configuration

## BaM Learning Rate (Gaussian Targets)

### λ_t (Gaussian Targets, Constant Schedule)
- **Value**: λ_t = B × D (constant for all t)
- **Rationale**: For Gaussian targets, Theorem 3.1 guarantees convergence for any fixed λ > 0. Larger λ allows faster convergence when ||ε_0|| is small; BD scaling accounts for both dimension and batch size.
- **Search range**: Also tested: BD/√(t+1), BD/(t+1). Constant performs best for Gaussian.
- **Sensitivity**: low
- **Source**: Section 5.1, Appendix E.3

### λ_t (Non-Gaussian Targets and PosteriorDB, Decaying Schedule)
- **Value**: λ_t = B × D / (t + 1)
- **Rationale**: Constant λ does not converge for non-Gaussian targets; decay allows stabilization. BD/(t+1) preferred over BD/√(t+1) per Appendix E.4.
- **Search range**: BD, BD/√(t+1), BD/(t+1)
- **Sensitivity**: medium
- **Source**: Sections 5.1, 5.2

## Batch Sizes

### BaM Batch Size (Gaussian, Fig 5.1)
- **Value**: D=4 → B ∈ {2, 5}; D=16 → B ∈ {2, 15}; D=64 → B ∈ {2, 40}; D=256 → B ∈ {2, 150}
- **Rationale**: B=2 is baseline (same as GSM/ADVI). Larger B (roughly B ≈ D/10 to D/4) shows benefit of BaM's batch structure.
- **Sensitivity**: high for BaM (C06)
- **Source**: Figure 5.1 legend

### BaM Batch Size (Non-Gaussian, Fig 5.2)
- **Value**: B ∈ {5, 10}; ADVI/GSM/Score/Fisher: B=5
- **Rationale**: Non-Gaussian experiments use D=10; B=5 or B=10 tested.
- **Sensitivity**: medium
- **Source**: Figure 5.2 legend, Section 5.1

### Batch Sizes (PosteriorDB, Fig 5.3)
- **Value**: B ∈ {8, 32}; all methods use same batch sizes
- **Rationale**: Solid lines: B=32; dashed lines: B=8.
- **Sensitivity**: medium (BaM benefits; ADVI/GSM do not)
- **Source**: Section 5.2, Figure 5.3

### Batch Sizes (Deep Generative, D=256)
- **Value**: B ∈ {10, 100, 300}
- **Rationale**: B must be comparable to D=256. B=10 too small (fails). B=300 ≈ D succeeds.
- **Sensitivity**: high
- **Source**: Section 5.3, Figure 5.4

## ADVI Learning Rates

### ADVI Adam Learning Rate (Gaussian Targets)
- **Value**: 0.01 (for ADVI-ELBO and ADVI-Fisher); per dimension for ADVI-Score: [0.01, 0.005, 0.001, 0.001] for D=4, 16, 64, 256
- **Rationale**: Grid search over learning rates; best value selected per experiment
- **Search range**: Grid search (unspecified grid; selected from typical ADAM range)
- **Sensitivity**: high (Score variant especially sensitive)
- **Source**: Appendix E.3

### ADVI Adam Learning Rate (Non-Gaussian Targets)
- **Value**: ADVI-ELBO: 0.02; ADVI-Fisher: 0.05; ADVI-Score: s=[0.2,1.0,1.8]/τ=1 → [0.01, 0.001, 0.001]; s=0/τ=[0.1,0.9,1.7] → [0.001, 0.01, 0.01]
- **Rationale**: Grid search; Score method is more sensitive to learning rate and more likely to diverge for highly skewed targets
- **Sensitivity**: high
- **Source**: Appendix E.4

### ADVI Adam Learning Rate (Deep Generative)
- **Value**: ℓ = 0.02 (consistently best from grid {0.001, 0.01, 0.02, 0.05})
- **Rationale**: Pilot run of 100 iterations with grid search; B=10, T=300 under 3000 gradient budget
- **Sensitivity**: medium
- **Source**: Appendix E.6

## BaM Learning Rates (Deep Generative, Pilot-Tuned)
- **Value**: B=10 → λ=0.1; B=100 → λ=50; B=300 → λ=7500
- **Rationale**: Pilot run of 100 iterations with candidate λ values per batch size; selected based on lowest MSE at end of pilot. At B=300, all candidates achieve minimal MSE (BaM converges in <100 iters); λ=7500 picked for fastest convergence.
- **Search range**: B=10: {0.01, 0.1, 0.2, 10}; B=100: {2, 20, 50, 100, 200}; B=300: {1000, 5000, 7500, 10000}
- **Sensitivity**: high (varies significantly with B)
- **Source**: Appendix E.6

### ADVI Adam Learning Rate (Deep Generative, Pilot-Tuned)
- **Value**: ℓ = 0.02 (consistently best across all batch sizes)
- **Rationale**: Pilot run of 100 iterations with grid search
- **Search range**: {0.001, 0.01, 0.02, 0.05}
- **Sensitivity**: medium
- **Source**: Appendix E.6

### Gradient Budget Comparison (Deep Generative)
- ADVI (best): B=10, T=300 → 3000 gradient evaluations
- BaM (comparable): B=300, T=10 → 3000 gradient evaluations
- Note: BaM with B=300, T=10 achieves comparable MSE to ADVI with B=10, T=300. BaM gradients are more parallelizable (larger batch per step).

## Complete Hyperparameter Summary Table

All numerical hyperparameter values as reported in the paper, organized by experiment:

### Experiment 1: Gaussian Targets (Section 5.1, Figure 5.1)

| Method | D | Batch Size B | Learning Rate / λ_t | Iterations | Seeds |
|--------|---|-------------|---------------------|------------|-------|
| BaM | 4 | 2 | λ_t = BD = 8 (constant) | ≥10^4 | 10 |
| BaM | 4 | 5 | λ_t = BD = 20 (constant) | ≥10^4 | 10 |
| BaM | 16 | 2 | λ_t = BD = 32 (constant) | ≥10^4 | 10 |
| BaM | 16 | 15 | λ_t = BD = 240 (constant) | ≥10^4 | 10 |
| BaM | 64 | 2 | λ_t = BD = 128 (constant) | ≥10^4 | 10 |
| BaM | 64 | 40 | λ_t = BD = 2560 (constant) | ≥10^4 | 10 |
| BaM | 256 | 2 | λ_t = BD = 512 (constant) | ≥10^4 | 10 |
| BaM | 256 | 150 | λ_t = BD = 38400 (constant) | ≥10^4 | 10 |
| ADVI (ELBO) | 4,16,64,256 | 2 | Adam lr = 0.01 | ≥10^4 | 10 |
| ADVI (Fisher) | 4,16,64,256 | 2 | Adam lr = 0.01 | ≥10^4 | 10 |
| ADVI (Score) | 4 | 2 | Adam lr = 0.01 | ≥10^4 | 10 |
| ADVI (Score) | 16 | 2 | Adam lr = 0.005 | ≥10^4 | 10 |
| ADVI (Score) | 64 | 2 | Adam lr = 0.001 | ≥10^4 | 10 |
| ADVI (Score) | 256 | 2 | Adam lr = 0.001 | ≥10^4 | 10 |
| GSM | 4,16,64,256 | 2 | N/A (no learning rate) | ≥10^4 | 10 |

### Experiment 2: Non-Gaussian Targets (Section 5.1, Figure 5.2)

| Method | D | Batch Size B | Learning Rate / λ_t | Iterations | Seeds |
|--------|---|-------------|---------------------|------------|-------|
| BaM | 10 | 5 | λ_t = BD/(t+1) = 50/(t+1) | ≥10^4 | 10 |
| BaM | 10 | 10 | λ_t = BD/(t+1) = 100/(t+1) | ≥10^4 | 10 |
| ADVI (ELBO) | 10 | 5 | Adam lr = 0.02 | ≥10^4 | 10 |
| ADVI (Fisher) | 10 | 5 | Adam lr = 0.05 | ≥10^4 | 10 |
| ADVI (Score) | 10 | 5 | Adam lr = 0.01 (s=0.2), 0.001 (s=1.0), 0.001 (s=1.8) | ≥10^4 | 10 |
| GSM | 10 | 5 | N/A | ≥10^4 | 10 |

### Experiment 3: PosteriorDB (Section 5.2, Figure 5.3)

| Method | Model | D | Batch Size B | Learning Rate / λ_t | Seeds |
|--------|-------|---|-------------|---------------------|-------|
| BaM | arK | 7 | 8 | λ_t = 56/(t+1) | 5 |
| BaM | arK | 7 | 32 | λ_t = 224/(t+1) | 5 |
| BaM | gp-pois-regr | 13 | 8 | λ_t = 104/(t+1) | 5 |
| BaM | gp-pois-regr | 13 | 32 | λ_t = 416/(t+1) | 5 |
| BaM | eight-schools | 10 | 8 | λ_t = 80/(t+1) | 5 |
| BaM | eight-schools | 10 | 32 | λ_t = 320/(t+1) | 5 |
| ADVI | all models | varies | 8, 32 | Adam lr = grid searched | 5 |
| GSM | all models | varies | 8, 32 | N/A | 5 |

### Experiment 4: Deep Generative (Section 5.3, Figure 5.4)

| Method | D | Batch Size B | Learning Rate / λ | Pilot Iters | Main Iters |
|--------|---|-------------|-------------------|-------------|------------|
| BaM | 256 | 10 | λ = 0.1 | 100 | 1000 |
| BaM | 256 | 100 | λ = 50 | 100 | 1000 |
| BaM | 256 | 300 | λ = 7500 | 100 | 1000 |
| ADVI | 256 | 10 | Adam lr = 0.02 | 100 | 1000 |
| ADVI | 256 | 100 | Adam lr = 0.02 | 100 | 1000 |
| ADVI | 256 | 300 | Adam lr = 0.02 | 100 | 1000 |
| GSM | 256 | 10, 100, 300 | N/A | 0 | 1000 |
| Amortized VI | 256 | N/A | N/A (encoder) | 0 | N/A |

## Iteration Counts

### Number of Iterations
- **Value**: Gaussian targets: ≥ 10^4 iterations; Non-Gaussian: ≥ 10^4 iterations; PosteriorDB: ≥ 10^4 iterations; Deep generative: pilot T=100, main T=1000
- **Rationale**: Enough iterations to observe convergence behavior and plateaus
- **Sensitivity**: low
- **Source**: Sections 5.1, 5.2, 5.3

### Number of Seeds
- **Value**: Gaussian targets: 10 seeds; Non-Gaussian: 10 seeds; PosteriorDB: 5 seeds; Deep generative: 1 seed (single test image)
- **Rationale**: Sufficient for mean/std estimates
- **Sensitivity**: low
- **Source**: Sections 5.1, 5.2, 5.3

## Initialization

### Variational Mean Initialization
- **Value**: μ_0 ~ Uniform[0, 0.1] for synthetic experiments; μ_0 = 0 (standard Gaussian N(0,I)) for deep generative
- **Rationale**: Small random initialization; standard Gaussian for deep generative
- **Sensitivity**: low (Theorem 3.1 holds for any finite initialization)
- **Source**: Appendix E.3, E.5, E.6

### Variational Covariance Initialization
- **Value**: Σ_0 = I (identity matrix)
- **Rationale**: Ensures Σ_0 ≻ 0; neutral starting point
- **Sensitivity**: low
- **Source**: Appendix E.3, E.5, E.6
