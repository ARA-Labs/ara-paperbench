---
# Experiments

## E01: Benchmark posterior approximation — Simformer vs NPE
- **Verifies**: C01, C02, C06
- **Setup**:
  - Model: Simformer (6 layers, token dim 50, 4 heads, attention size 10, hidden dim 150) and NPE (neural spline flow, sbi library defaults)
  - Hardware: Not specified in paper (JAX backend)
  - Dataset: Four SBIBM benchmark tasks — Gaussian Linear (θ,x ∈ ℝ¹⁰), Gaussian Mixture (θ,x ∈ ℝ²), Two Moons (θ,x ∈ ℝ²), SLCP (θ ∈ ℝ⁵, x ∈ ℝ⁸)
  - System: Simformer variants: dense attention, undirected graph, directed graph; baselines: NPE, NLE, NRE, NPSE (Appendix A3)
- **Procedure**:
  1. Generate 10³, 10⁴, and 10⁵ simulation pairs (θ, x) from each benchmark simulator.
  2. Train four models for each simulation budget: (a) NPE with neural spline flow, (b) Simformer with dense mask, (c) Simformer with undirected graph mask, (d) Simformer with directed graph mask. Use batch size 1000, Adam optimizer, early stopping on validation loss.
  3. For each trained model and each of 10 ground-truth reference observations, generate N posterior samples (N = number of reference samples) using 500-step Euler-Maruyama reverse SDE.
  4. Compute C2ST accuracy between model-generated and ground-truth MCMC posterior samples using 5-fold cross-validation with a random forest classifier (100 trees).
  5. Plot C2ST vs number of simulations for each model/task combination.
- **Metrics**: C2ST accuracy (closer to 0.5 = better); reported per task per simulation budget per model.
- **Expected outcome**:
  - Simformer (all variants) should outperform NPE on most benchmark tasks, particularly at lower simulation budgets
  - Structured attention mask variants (undirected, directed) should outperform dense Simformer on tasks with sparser dependency structures (Linear Gaussian, SLCP)
  - Average simulation budget needed for Simformer to match NPE's best performance should be approximately 10× lower
  - Training on all conditionals (dense Simformer) should not meaningfully hurt posterior-only C2ST compared to Simformer (posterior only)
- **Baselines**: NPE, NLE, NRE, NPSE (Simons et al., 2023; Geffner et al., 2023)
- **Dependencies**: none

## E02: Arbitrary conditional estimation — Tree, HMM, Two Moons, SLCP
- **Verifies**: C03, C06
- **Setup**:
  - Model: Simformer (6 layers, dense/undirected/directed attention variants)
  - Hardware: Not specified in paper
  - Dataset: Tree task (θ ∈ ℝ³, x ∈ ℝ⁴, nonlinear tree), HMM task (θ ∈ ℝ¹⁰, x ∈ ℝ¹⁰, Markovian), Two Moons, SLCP
  - System: MCMC reference: HMC (5000 steps) for Tree/HMM; slice sampling (1000 steps) + MHMCMC (3000 steps, step size 0.01) for Two Moons; slice sampling (600 steps) + MHMCMC (2000 steps, step size 0.1) for SLCP
- **Procedure**:
  1. Generate 10³, 10⁴, 10⁵ simulations from each task simulator.
  2. Train Simformer variants (dense, undirected graph, directed graph) on each budget.
  3. For each task, randomly sample 100 conditional distributions (arbitrary subsets of variables observed/unobserved).
  4. Generate MCMC reference samples for each of the 100 conditionals using task-specific samplers.
  5. Generate Simformer samples for each conditional using 500-step reverse SDE.
  6. Compute C2ST between Simformer and MCMC samples for each conditional; average across 100 conditionals.
  7. Plot average C2ST vs number of simulations.
- **Metrics**: C2ST accuracy for arbitrary conditionals (averaged over 100 randomly sampled conditionals); expected coverage (calibration).
- **Expected outcome**:
  - Simformer should accurately model arbitrary conditionals (C2ST near 0.5) when trained on 10⁵ simulations across all four tasks
  - All Simformer models on all tasks should achieve C2ST below 0.7 when trained on 10⁵ simulations
  - Performance should improve monotonically with simulation budget
  - Training solely on the posterior mask should not substantially improve arbitrary conditional performance
- **Baselines**: MCMC ground truth; no competing method targets arbitrary conditionals
- **Dependencies**: E01

## E03: Lotka-Volterra — unstructured/missing data inference
- **Verifies**: C04
- **Setup**:
  - Model: Simformer (8 layers, dense/undirected/directed attention variants)
  - Hardware: Not specified in paper
  - Dataset: Lotka-Volterra ODE simulator; prior: sigmoid-transformed Normal, parameters α, β, γ, δ ∈ [1,3]; Gaussian observation noise σ=0.1; full time-series (no summary statistics)
  - System: MCMC reference for posterior; 10³, 10⁴, 10⁵ simulation budgets
- **Procedure**:
  1. Train Simformer on 10⁵ Lotka-Volterra simulations (full time series, no summary statistics).
  2. Generate scenario A: four prey observations at irregular time points.
  3. Condition Simformer on the four prey observations; sample posterior over parameters and posterior predictive for full predator+prey time series at uniform grid t ∈ [0, 15].
  4. Generate scenario B: add nine additional predator observations at irregular times.
  5. Condition Simformer on all 13 observations; sample posterior and posterior predictive.
  6. Generate MCMC reference posterior for both scenarios.
  7. Compute C2ST for posterior and for arbitrary conditionals at 10³, 10⁴, 10⁵ simulation budgets.
  8. Check that ground truth parameters lie within high-probability regions of the Simformer posterior.
- **Metrics**: C2ST (posterior), C2ST (arbitrary conditionals); visual inspection of posterior predictive coverage.
- **Expected outcome**:
  - Ground truth parameters should be within high-probability posterior regions for scenario A
  - Adding nine predator observations (scenario B) should reduce posterior uncertainty compared to scenario A
  - Simformer trained on 10⁵ simulations should achieve C2ST (posterior) below 0.65 and C2ST (arbitrary conditionals) below 0.75
  - Posterior predictives should capture data and uncertainty in a realistic manner
- **Baselines**: MCMC ground truth
- **Dependencies**: none

## E04: SIRD model — inference with infinite-dimensional parameters
- **Verifies**: C04
- **Setup**:
  - Model: Simformer (8 layers, dense attention mask)
  - Hardware: Not specified in paper
  - Dataset: SIRD simulator; γ, δ ∼ Unif(0, 0.5); β(t) from Gaussian process with RBF kernel k(t₁,t₂)=2.5²exp(−‖t₁−t₂‖²/(2·7²)), passed through sigmoid; log-normal observation noise σ=0.05
  - System: Two scenarios: (A) 5 observations of I/R/D at irregular times; (B) 4 measurements of contact rate β(t) + 1 measurement of I
- **Procedure**:
  1. Train Simformer on SIRD simulations.
  2. Scenario A: Generate 5 synthetic observations from infected, recovered, deceased at random times. Apply Simformer to estimate posterior over γ, δ, β(t) and generate posterior predictives for I, R, D on a regular time grid 0–40.
  3. Scenario B: Generate 4 synthetic contact rate measurements and 1 infected observation. Apply Simformer to estimate parameter-conditioned posterior.
  4. Evaluate expected coverage (calibration) on 20 random time points for each time-dependent variable.
- **Metrics**: Visual posterior alignment with ground truth; expected coverage; qualitative posterior predictive accuracy.
- **Expected outcome**:
  - Simformer should recover a realistic time-varying contact rate β(t) with increasing uncertainty near zero-infection regions (around timestamp 25)
  - Death and recovery rate posteriors should be realistic and cover the true parameters within 99% quantiles
  - Parameter-conditioned posterior should align closely with contact rate measurements (scenario B)
  - Expected coverage analysis should verify calibration
- **Baselines**: MCMC reference (for coverage analysis)
- **Dependencies**: none

## E05: Hodgkin-Huxley — interval conditioning via guided diffusion
- **Verifies**: C05
- **Setup**:
  - Model: Simformer (8 layers, dense attention mask)
  - Hardware: Not specified in paper
  - Dataset: Hodgkin-Huxley simulator (7 parameters); V₀=−65.0mV; simulation duration 200ms; input current 4mA during [50ms,150ms]; summary statistics from Gonçalves et al. (2020) + metabolic energy (sodium charge, converted to µJ/s)
  - System: Guided diffusion with self-recurrence for interval constraint; 10⁵ simulations
- **Procedure**:
  1. Train Simformer on HH simulations with summary statistics including energy.
  2. Phase 1: Infer posterior given only voltage summary statistics (no energy constraint). Sample posterior predictive energy distribution.
  3. Phase 2: Define observation interval = lowest 10% quantile of posterior predictive energy. Apply Simformer with guided diffusion (Algorithm 1) to infer energy-constrained posterior given voltage + energy constraint.
  4. Generate posterior predictive samples from both posteriors (via Simformer and via running the simulator).
  5. Verify that energy-constrained samples satisfy the energy threshold.
  6. Verify that constrained voltage posterior predictives remain consistent with observations.
- **Metrics**: Visual comparison of posterior marginals; posterior predictive energy distributions vs threshold; coverage of voltage traces.
- **Expected outcome**:
  - Unconstrained posterior should show wide marginals for gNa, gK and narrow marginals for Cm, gL (consistent with Gonçalves et al., 2020)
  - Simformer posterior predictive energy should closely match posterior predictive from running the simulator
  - Energy-constrained posterior should be significantly more constrained, particularly for maximal sodium and potassium conductances
  - Energy of constrained posterior predictives should lie below the 10% quantile threshold
  - Constrained voltage traces should remain consistent with observed voltage summary statistics
- **Baselines**: Unconstrained Simformer; posterior predictive from running simulator
- **Dependencies**: E03

## E06: Evaluation steps ablation — reverse SDE efficiency
- **Verifies**: C01
- **Setup**:
  - Model: Simformer (6 layers, dense attention)
  - Hardware: Not specified in paper
  - Dataset: Four benchmark tasks (Gaussian Linear, Gaussian Mixture, Two Moons, SLCP); both VESDE and VPSDE
  - System: Euler-Maruyama discretization with varying number of steps
- **Procedure**:
  1. Train Simformer on each benchmark task.
  2. At inference time, solve the reverse SDE using Euler-Maruyama with N steps, for N ∈ {50, 100, 250, 500, 750, 1000}.
  3. Compute C2ST vs N for each task and SDE variant.
- **Metrics**: C2ST accuracy as a function of number of evaluation steps.
- **Expected outcome**:
  - Performance improvement with increasing steps should be non-gradual, showing a sharp transition
  - For all tasks (except Two Moons on VPSDE), 50 evaluation steps should be sufficient to reach near-best performance
  - This demonstrates efficiency advantage over MCMC-based methods (which typically need far more than 50 evaluations)
- **Baselines**: NLE (requiring MCMC), NRE (requiring MCMC)
- **Dependencies**: E01
