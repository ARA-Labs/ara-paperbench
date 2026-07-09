# Experiments

## E01: Gaussian Targets with Increasing Dimensions
- **Verifies**: C01, C02, C03, C04, C05, C06
- **Setup**:
  - Model: Full-covariance Gaussian variational approximation N(μ, Σ)
  - Hardware: CPU/GPU via JAX (exact hardware not specified; wallclock shown in Fig E.1)
  - Dataset: Synthetically generated Gaussian targets of dimension D ∈ {4, 16, 64, 256}; covariance Σ* = AA^T for random D×D matrix A
  - System: BaM (batch sizes B=2 and B=D-tuned: 5/15/40/150 for D=4/16/64/256), ADVI (B=2, ADAM), GSM (B=2), ADVI-Score (B=2), ADVI-Fisher (B=2)
- **Procedure**:
  1. Generate random Gaussian target N(μ*, Σ*) where Σ* = AA^T for random A
  2. Initialize all methods with μ_0 ~ Uniform[0, 0.1] and Σ_0 = I
  3. For BaM: set λ_t = BD (constant); for ADVI/Score/Fisher: grid-search learning rate
  4. Run each method for at least 10^4 iterations
  5. At each iteration, compute forward KL divergence KL(p; q_t) and reverse KL divergence KL(q_t; p) empirically
  6. Repeat for 10 random seeds
  7. Plot mean (and individual) KL curves vs number of gradient evaluations
- **Metrics**: Forward KL divergence KL(p; q_t) and reverse KL divergence KL(q_t; p) as functions of gradient evaluations (= B × iterations)
- **Expected outcome**:
  - BaM with large batch size converges orders of magnitude faster (in gradient evaluations) than ADVI
  - BaM with B=2 and GSM perform similarly; BaM at larger batch sizes outperforms GSM
  - ADVI, Score-ADVI, and Fisher-ADVI have similar convergence to each other
  - BaM convergence improves with increasing batch size; GSM does not benefit from B>2
- **Baselines**: ADVI (ELBO, ADAM), ADVI-Score (score-based divergence, ADAM), ADVI-Fisher (Fisher divergence, ADAM), GSM
- **Dependencies**: none

## E02: Non-Gaussian Targets (Sinh-Arcsinh Distribution)
- **Verifies**: C01, C05, C06
- **Setup**:
  - Model: Full-covariance Gaussian variational approximation
  - Hardware: CPU/GPU via JAX
  - Dataset: D=10 sinh-arcsinh normal distributions; varying skew s ∈ {0.2, 1.0, 1.8} with τ=1; varying tails τ ∈ {0.1, 0.9, 1.7} with s=0
  - System: BaM (B=5 and B=10), ADVI (B=5), GSM (B=5), ADVI-Score (B=5), ADVI-Fisher (B=5)
- **Procedure**:
  1. Construct sinh-arcsinh target distributions with specified (s, τ) parameters
  2. Initialize all methods with random μ_0 and Σ_0 = I
  3. For BaM: use decaying learning rate λ_t = BD/(t+1); for ADVI/Score/Fisher: grid-search learning rate
  4. Run each method for at least 10^4 iterations; 10 seeds
  5. Compute forward and reverse KL divergence at each iteration
  6. Report mean ± standard error curves
- **Metrics**: Forward KL KL(p; q_t) and reverse KL KL(q_t; p) vs gradient evaluations
- **Expected outcome**:
  - BaM converges faster than ADVI for all skew/tail configurations
  - For large skew (s=1.0, 1.8): BaM reaches higher forward KL but similar reverse KL vs ADVI
  - GSM reverse KL diverges for highly skewed targets (s=1.8); Score variant also diverges for high skew
  - For varying tails: all methods converge to similar reverse KL; BaM typically converges in fewer iterations than ADVI
  - Decaying learning rate λ_t = BD/(t+1) outperforms constant schedule for non-Gaussian targets
- **Baselines**: ADVI, ADVI-Score, ADVI-Fisher, GSM
- **Dependencies**: none

## E03: Posterior Inference in Hierarchical Bayesian Models (PosteriorDB)
- **Verifies**: C05, C06
- **Setup**:
  - Model: Full-covariance Gaussian VI on 3 Stan/PosteriorDB models
  - Hardware: CPU/GPU via JAX
  - Dataset: (1) arK (autoregressive model, D=7, nearly Gaussian); (2) gp-pois-regr (Gaussian process Poisson regression, D=13, non-Gaussian); (3) eight-schools-centered (8-schools hierarchical, D=10, non-Gaussian). Reference samples from HMC provided by PosteriorDB.
  - System: BaM (B=8 and B=32), ADVI (B=8 and B=32), GSM (B=8 and B=32). Score function computed via BridgeStan.
- **Procedure**:
  1. Load Stan model and reference HMC samples from PosteriorDB
  2. Initialize all methods with μ_0 ~ Uniform[0, 0.1] and Σ_0 = I
  3. For BaM: use decaying learning rate λ_t = BD/(t+1)
  4. For ADVI: grid-search over learning rates
  5. Run each method for at least 10^4 iterations; 5 seeds
  6. At each iteration, compute relative mean error = ||μ_VI - μ_HMC|| / ||μ_HMC|| and relative SD error = ||σ_VI - σ_HMC|| / ||σ_HMC||
  7. Report mean ± standard error over seeds
- **Metrics**: Relative posterior mean error and relative posterior SD error vs gradient evaluations (Equation 242)
- **Expected outcome**:
  - BaM outperforms ADVI (lower mean error, faster convergence)
  - GSM can converge faster than BaM at small batch sizes but oscillates around the solution
  - BaM benefits from larger batch sizes (B=32 > B=8); ADVI and GSM do not benefit from larger batches
  - For hierarchical model: BaM converges to larger relative SD error than GSM (exception to trend)
- **Baselines**: ADVI, GSM
- **Dependencies**: none

## E04: Deep Generative Model — CIFAR-10 Image Reconstruction
- **Verifies**: C05, C06
- **Setup**:
  - Model: VAE decoder network Ω(z, θ̂): R^256 → R^3072; 5-layer convolutional encoder and decoder; Gaussian likelihood x_n|z_n ~ N(Ω(z_n, θ̂), 0.1·I); latent z ∈ R^256; observation x ∈ R^3072
  - Hardware: GPU (JAX with JIT compilation)
  - Dataset: CIFAR-10 (60,000 images, 32×32×3 = 3072 pixels); training split for VAE pre-training; test split for VI evaluation
  - System: BaM (B=10, 100, 300), ADVI (B=10, 100, 300), GSM, Amortized VI (factorized Gaussian encoder)
- **Procedure**:
  1. Pre-train VAE on CIFAR-10 training split for 100 epochs using standard VAE training (ELBO, ADAM, factorized Gaussian encoder)
  2. Sample test image x' from CIFAR-10 test set
  3. For BaM and ADVI: run 100-iteration pilot with candidate learning rates {λ} to select best λ per batch size
  4. Initialize all VI methods at N(0, I)
  5. Run BaM for T=1000 iterations; run ADVI for T=1000 iterations; run GSM for T=1000 iterations
  6. At each iteration, evaluate E[z'|x'] and compute reconstructed image Ω(E[z'|x'], θ̂)
  7. Compute MSE between reconstructed and original image at each iteration
  8. Compare 3000-gradient-evaluation budget: ADVI (B=10, T=300) vs BaM (B=300, T=10)
- **Metrics**: Mean Squared Error (MSE) between reconstructed and test image, vs. iteration count and wallclock time
- **Expected outcome**:
  - BaM with B=10 (small relative to D=256) performs poorly (high MSE)
  - BaM with B=300 (comparable to D) converges an order of magnitude (or more) faster than ADVI and GSM
  - Under 3000-gradient-evaluation budget: BaM B=300, T=10 achieves comparable MSE to ADVI B=10, T=300
  - BaM B=300 is faster in wallclock time (more parallelizable) than ADVI
  - Both BaM and ADVI (full covariance) eventually achieve lower MSE than Amortized VI (factorized Gaussian)
- **Baselines**: ADVI (various batch sizes), GSM, Amortized VI (trained VAE encoder)
- **Dependencies**: none
