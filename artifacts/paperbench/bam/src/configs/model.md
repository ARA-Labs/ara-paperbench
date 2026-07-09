# Model Configuration

## Variational Family

### Gaussian Variational Family
- **Value**: Q = {N(μ, Σ) : μ ∈ R^D, Σ ∈ S^D_{++}}; full (non-factorized) covariance
- **Rationale**: Full covariance captures correlations between latent variables; required for BaM closed-form updates
- **Source**: Section 2.2

### Variational Parameters
- **Value**: μ ∈ R^D (mean vector), Σ ∈ R^{D×D} (full covariance matrix, D(D+1)/2 free parameters)
- **Rationale**: Full parameterization provides richer approximation than mean-field (factorized) family
- **Source**: Section 2

## Synthetic Gaussian Targets

### Covariance Construction
- **Value**: Σ* = AA^T where A ∈ R^{D×D} is random; dimensions D ∈ {4, 16, 64, 256}
- **Rationale**: Random covariance to test robustness of VI algorithms
- **Source**: Appendix E.3

## Non-Gaussian Targets (Sinh-Arcsinh)

### Distribution
- **Value**: z = sinh(τ^{-1}(sinh^{-1}(y) + s)) where y ~ N(μ, Σ), D=10
- **Parameters tested**:
  - Fixed τ=1 (normal tails), varying s ∈ {0.2, 1.0, 1.8}
  - Fixed s=0 (no skew), varying τ ∈ {0.1, 0.9, 1.7}
- **Gaussian recovered at**: s=0, τ=1
- **Source**: Section 5.1

## PosteriorDB Models

### arK (Nearly Gaussian)
- **Value**: D=7; Stan model from PosteriorDB (Magnusson et al., 2022)
- **Source**: Section 5.2

### GP Poisson Regression
- **Value**: D=13 (gp-pois-regr); Stan model from PosteriorDB; non-Gaussian
- **Source**: Section 5.2

### Eight-Schools Hierarchical (Centered)
- **Value**: D=10 (eight-schools-centered); Stan model from PosteriorDB; non-Gaussian
- **Source**: Section 5.2

## Deep Generative Model (VAE)

### Prior
- **Value**: z_n ~ N(0, I), z_n ∈ R^256
- **Source**: Section 5.3, Eq. (28)

### Likelihood Model
- **Value**: x_n | z_n ~ N(Ω(z_n, θ̂), σ²I), x_n ∈ R^{3072}; σ² = 0.1
- **Rationale**: Gaussian likelihood with fixed variance; images treated as continuous
- **Source**: Section 5.3, Eq. (29)

### Neural Network Architecture
- **Value**: Decoder Ω(z, θ̂): R^256 → R^{3072}; 5-layer convolutional network; same architecture for encoder q(z|x)
- **Dataset**: CIFAR-10 (Krizhevsky, 2009); 32×32×3 = 3072 pixels; continuous-valued images
- **Training**: 100 epochs, standard VAE ELBO, factorized Gaussian encoder; ELBO converges by epoch 100 (Figure E.8)
- **Source**: Section 5.3, Appendix E.6

### Latent Dimension
- **Value**: z_n ∈ R^256 (D=256 for VI posterior inference)
- **Rationale**: Low-dimensional representation of 3072-dimensional image; D much smaller than x dimension
- **Source**: Section 5.3

### Posterior Inference Task
- **Value**: Given new test image x', approximate posterior p(z'|x') using BaM/ADVI/GSM with full-covariance Gaussian
- **Evaluation**: Reconstruction MSE = ||x' - Ω(E[z'|x'], θ̂)||²
- **Source**: Section 5.3

## ADVI Optimizer

### Adam Hyperparameters
- **Value**: Adam optimizer; learning rate specified per experiment (see training.md); default Adam betas not explicitly specified
- **Source**: Algorithm 2, Appendix E.1
