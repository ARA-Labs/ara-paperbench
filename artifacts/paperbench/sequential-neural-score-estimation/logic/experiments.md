# Experiments

## E01: Non-sequential benchmark — NPSE-VE/VP vs NPE
- **Verifies**: C01, C05
- **Setup**:
  - Model: Score network (3-layer MLP, 256 hidden units per layer, SiLU), θ/x/t embeddings as described in Appendix E.3.2
  - Hardware: Not specified in paper
  - Dataset: 8 sbibm benchmark tasks (Gaussian Linear, Gaussian Mixture, Two Moons, Gaussian Linear Uniform, Bernoulli GLM, SLCP, SIR, Lotka Volterra); simulation budgets 1000, 10000, 100000
  - System: NPSE-VE and NPSE-VP trained independently; NPE results from sbibm toolkit
- **Procedure**:
  1. For each task and each simulation budget N ∈ {1000, 10000, 100000}, sample N pairs (θ_i, x_i) ~ p(θ)p(x|θ).
  2. Train score network s_ψ by minimising Monte Carlo estimate of DSM objective (Eq. 7) using Adam (lr=1e-4), batch size 50 (budget 1k/10k) or 500 (budget 100k), max 3000 iterations, early stopping patience 1000 steps, 15% validation split.
  3. For NPSE-VE: use VE SDE with σ_min=0.01 (SIR/Two Moons) or σ_min=0.05 (others), σ_max = max pairwise Euclidean distance.
  4. For NPSE-VP: use VP SDE with β_min=0.1, β_max=11.0.
  5. Generate 10000 posterior samples via time-reversal of probability flow ODE (RK45 solver) at x=x_obs.
  6. Compute C2ST score using sbibm default implementation with 10000 true posterior samples.
  7. Compare C2ST scores of NPSE-VE, NPSE-VP, and NPE across all tasks and budgets.
- **Metrics**: C2ST score (range [0.5, 1.0], lower is better), reported per task per budget.
- **Expected outcome**:
  - NPSE-VE and NPSE-VP achieve C2ST comparable to NPE on most tasks.
  - NPSE variants outperform NPE on the most challenging tasks (SLCP, Lotka Volterra) at larger budgets.
  - VE SDE tends to outperform VP SDE on low-dimensional tasks (SIR dim=2, Two Moons dim=2, Gaussian Mixture dim=2).
  - VP SDE tends to outperform or match VE SDE on high-dimensional tasks (Lotka Volterra dim=4+20, SLCP dim=5+8, Bernoulli GLM dim=10).
  - Performance differences between methods increase with task difficulty.
- **Baselines**: NPE (Papamakarios & Murray, 2016) via sbibm toolkit.
- **Dependencies**: none

## E02: Sequential benchmark — TSNPSE-VE/VP vs SNPE-C and TSNPE
- **Verifies**: C02, C05
- **Setup**:
  - Model: Same score network architecture as E01.
  - Hardware: Not specified in paper.
  - Dataset: Same 8 sbibm benchmark tasks; simulation budgets 10000 and 100000. (1000 budget also tested; results reported.)
  - System: R=10 rounds; M = N/R simulations per round; SNPE-C and TSNPE results from sbibm toolkit.
- **Procedure**:
  1. For each task and each simulation budget N ∈ {1000, 10000, 100000} and R=10 rounds (M=N/R per round):
  2. Round 1: sample M pairs (θ_i, x_i) ~ p(θ)p(x|θ); train score network as in E01.
  3. Subsequent rounds r=2,...,R: estimate HPR_ε with ε=5×10⁻⁴ using 20000 posterior samples from ODE; compute truncation boundary κ; define truncated proposal via rejection sampling (initial cheap hypercube rejection, then likelihood threshold).
  4. Sample M pairs (θ_i, x_i) with θ_i ~ ˜p^r(θ); add to accumulated dataset D; retrain score network on D with batch size 200 (budget 1k/10k) or 500 (budget 100k).
  5. After R rounds, generate 10000 posterior samples and compute C2ST.
  6. Compare TSNPSE-VE, TSNPSE-VP, SNPE-C, and TSNPE.
- **Metrics**: C2ST score per task per budget.
- **Expected outcome**:
  - TSNPSE outperforms or matches SNPE-C and TSNPE on SLCP and Lotka Volterra (the hardest tasks).
  - Results are mixed on simpler tasks; no single method dominates all tasks.
  - Sequential methods achieve lower C2ST than their non-sequential counterparts at the same total budget.
  - VP SDE is preferred for high-dimensional tasks (Lotka Volterra, Bernoulli GLM); VE SDE for low-dimensional tasks.
- **Baselines**: SNPE-C (Greenberg et al., 2019) and TSNPE (Deistler et al., 2022a) via sbibm toolkit.
- **Dependencies**: E01

## E03: Ablation — TSNPSE vs SNPSE-A/B/C sequential variants
- **Verifies**: C03
- **Setup**:
  - Model: Same score network as E01/E02.
  - Hardware: Not specified in paper.
  - Dataset: SLCP and Gaussian Linear Uniform (GLU) benchmark tasks.
  - System: R rounds sequential; same budget allocations.
- **Procedure**:
  1. Implement SNPSE-A (post-hoc SIR correction), SNPSE-B (importance-weighted DSM loss), SNPSE-C (score-space correction with proposal prior score estimation).
  2. Run each algorithm on SLCP and GLU with the same total simulation budget and R rounds.
  3. Compute C2ST for each method at each round.
  4. Compare TSNPSE, SNPSE-A, SNPSE-B, and SNPSE-C.
- **Metrics**: C2ST score per method per task.
- **Expected outcome**:
  - TSNPSE achieves lower C2ST than SNPSE-A and SNPSE-B on both tasks.
  - SNPSE-C fails to produce meaningful results (C2ST approximately at ceiling ≈ 1.0) due to approximation errors in the proposal prior score estimation.
  - SNPSE-B shows unstable training due to high-variance importance weights.
- **Baselines**: SNPSE-A, SNPSE-B, SNPSE-C (paper's own alternative sequential methods).
- **Dependencies**: E01, E02

## E04: Real-world Pyloric neuroscience problem
- **Verifies**: C04
- **Setup**:
  - Model: Same score network architecture (VP SDE) as used in benchmarks; same hyperparameters for robustness demonstration.
  - Hardware: Not specified in paper.
  - Dataset: Pyloric network simulator (Prinz et al., 2003; 2004); 31 parameters (conductances/synapses of 3 neurons: AB, LP, PY), 18 summary statistics; prior = uniform over known parameter ranges; observed data from Haddad & Marder (2021) at Zenodo.
  - System: 9 rounds; 30000 initial simulations + 20000 per subsequent round.
- **Procedure**:
  1. Initialise with 30000 simulations from prior.
  2. Replace invalid summary statistics (NaN outputs) with values 2 standard deviations below prior predictive of each statistic.
  3. Train score network (VP SDE, same architecture as benchmarks).
  4. For rounds 2–9: apply truncated proposal procedure (HPR_ε, ε=5×10⁻⁴), add 20000 new simulations per round.
  5. Track % valid summary statistics from the simulator at each round.
  6. After final round, compute posterior mean and generate a posterior mean-predictive sample.
  7. Compare % valid statistics vs simulation budget against TSNPE and SNVI.
- **Metrics**: Percentage of valid (non-NaN) summary statistics from the simulator per round, posterior mean-predictive trace vs observed data.
- **Expected outcome**:
  - TSNPSE achieves approximately 81% valid summary statistics in the final round.
  - TSNPSE exceeds the percentage of valid summary statistics of both TSNPE and SNVI for all simulation budgets below 200k.
  - Posterior mean-predictive closely matches the observed neural voltage traces.
  - Posterior marginals are visually consistent with previously reported results (Deistler et al., 2022a; Glöckler et al., 2022).
- **Baselines**: TSNPE (Deistler et al., 2022a), SNVI (Glöckler et al., 2022).
- **Dependencies**: E01, E02

## E05: Comparison of NPSE vs NLSE (alternative score decomposition)
- **Verifies**: C01
- **Setup**:
  - Model: NPSE (VE and VP SDE) vs NLSE (VE SDE only, requires computable perturbed prior).
  - Hardware: Not specified in paper.
  - Dataset: 4 benchmark tasks from sbibm.
  - System: Amortised (non-sequential).
- **Procedure**:
  1. Train NLSE: decompose posterior score as likelihood score + prior score (Eq. 54-55). Minimise denoising likelihood score matching objective (Eq. 57). Compute perturbed prior score analytically (for VE SDE with uniform/Gaussian prior).
  2. Train NPSE-VE and NPSE-VP as in E01.
  3. Generate 10000 posterior samples and compute C2ST on the 4 tasks.
  4. Compare NPSE-VE, NPSE-VP, and NLSE-VE.
- **Metrics**: C2ST score per task.
- **Expected outcome**:
  - When the perturbed prior can be computed analytically, NPSE and NLSE achieve roughly equivalent C2ST.
  - When the perturbed prior requires a second score network, NPSE significantly outperforms NLSE.
- **Baselines**: NLSE-VE (Neural Likelihood Score Estimation with VE SDE).
- **Dependencies**: E01
