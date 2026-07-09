# Concepts

## Score Function
- **Notation**: `∇_θ log p(θ)` or `s(θ)`
- **Definition**: The gradient of the log-density of a probability distribution with respect to the variable of interest. For a posterior, this is `∇_θ log p(θ|x)`.
- **Boundary conditions**: Requires the log-density to be differentiable. Does not require the normalising constant of p(θ|x) to be tractable.
- **Related concepts**: Denoising Score Matching, Forward SDE, Conditional Score Network

## Conditional Score Network
- **Notation**: `s_ψ(θ_t, x, t) ≈ ∇_θ log p_t(θ_t|x)`
- **Definition**: A neural network parameterised by ψ that approximates the score of the time-marginal posterior density `p_t(θ_t|x)` at noise level t, conditioned on observation x. Architecture: independent MLP embeddings for θ_t, x, and t (sinusoidal), concatenated and passed through a final MLP. Output dimension equals dim(θ).
- **Boundary conditions**: Approximation error decreases with training data size and network capacity. At t=0, approximates the posterior score; at t=T, approximates the reference distribution score.
- **Related concepts**: Score Function, Denoising Score Matching, Forward SDE

## Forward SDE (Noising Process)
- **Notation**: `dθ_t = f(θ_t, t)dt + g(t)dw_t`, with `θ_0 ~ p(·|x)`
- **Definition**: A stochastic differential equation that gradually adds noise to samples from the posterior distribution, transforming them into samples from a tractable reference distribution π (e.g., standard Gaussian). The paper considers VE SDE and VP SDE variants.
- **Boundary conditions**: Coefficients f and g must be chosen so the process admits a unique stationary distribution π. Time horizon T must be large enough that p_T ≈ π.
- **Related concepts**: VE SDE, VP SDE, Reverse SDE, Conditional Score Network

## VE SDE (Variance-Exploding SDE)
- **Notation**: `dθ_t = σ_min (σ_max/σ_min)^t √(2 log(σ_max/σ_min)) dw_t`, `t ∈ (0,1]`
- **Definition**: A forward SDE with zero drift and a time-varying diffusion coefficient such that the variance grows without bound. Transition density: `p_{t|0}(θ_t|θ_0) = N(θ_0, σ²_min (σ_max/σ_min)^{2t} I)`. Parameters: σ_min ∈ {0.01, 0.05}, σ_max = maximum pairwise Euclidean distance in training data.
- **Boundary conditions**: σ_min = 0.01 for 2D experiments (SIR, Two Moons); σ_min = 0.05 for all others. Recommended for low-dimensional problems.
- **Related concepts**: Forward SDE, VP SDE, Denoising Score Matching

## VP SDE (Variance-Preserving SDE)
- **Notation**: `dθ_t = -½β_t θ_t dt + √β_t dw_t`, where `β_t = β_min + t(β_max - β_min)`, `t ∈ (0,1]`
- **Definition**: A forward SDE with linear drift and time-varying diffusion coefficient such that the variance remains bounded. Transition density: `p_{t|0}(θ_t|θ_0) = N(θ_0 exp(-∫β_s ds/2), I - I exp(-∫β_s ds))`. Parameters: β_min = 0.1, β_max = 11.0.
- **Boundary conditions**: Recommended for high-dimensional problems. Used for the Pyloric neuroscience experiment.
- **Related concepts**: Forward SDE, VE SDE, Denoising Score Matching

## Denoising Score Matching (DSM) Objective
- **Notation**: `J^{DSM}_{post}(ψ) = ∫₀ᵀ λ_t E_{p_{t|0}(θ_t|θ_0) p(x|θ_0) p(θ_0)} [||s_ψ(θ_t,x,t) - ∇_{θ_t} log p_{t|0}(θ_t|θ_0)||²] dt`
- **Definition**: A tractable surrogate for the weighted Fisher divergence between the score network and the true posterior score. Minimised when `s_ψ(θ_t,x,t) = ∇_θ log p_t(θ_t|x)` almost everywhere. The transition score `∇_{θ_t} log p_{t|0}(θ_t|θ_0)` is available in closed form for VE/VP SDEs.
- **Boundary conditions**: Requires i.i.d. samples (θ_0, x) from the joint p(θ)p(x|θ) (or a proposal). Approximated via Monte Carlo in practice.
- **Related concepts**: Score Function, Conditional Score Network, NPSE, TSNPSE

## Probability Flow ODE
- **Notation**: `dθ_t/dt = f(θ_t,t) - ½g²(t)∇_θ log p_t(θ_t|x)`
- **Definition**: A deterministic ODE with the same marginal distributions as the forward SDE. Its time-reversal can be used to generate posterior samples deterministically (via numerical ODE solvers, e.g., RK45) and to evaluate densities via the instantaneous change-of-variables formula. This ODE is an instance of a continuous normalising flow (CNF).
- **Boundary conditions**: Density evaluation requires solving an augmented ODE (trace computation), which is computationally expensive. Density evaluation is needed for TSNPSE's HPR computation.
- **Related concepts**: Forward SDE, Reverse SDE, HPR Estimation, CNF

## NPSE (Neural Posterior Score Estimation)
- **Notation**: Non-sequential (amortised) variant; trains `s_ψ(θ_t, x, t)` on samples from p(θ)p(x|θ).
- **Definition**: Algorithm that (i) simulates (θ_0, x, θ_t) triples, (ii) trains the score network via the DSM objective, (iii) generates posterior samples by simulating the time-reversal of the probability flow ODE initialised at π with x = x_obs.
- **Boundary conditions**: Amortised — same trained network can be queried for any x. Requires a large simulation budget to cover the prior predictive. Equivalent to FMPE when using the deterministic ODE.
- **Related concepts**: TSNPSE, Denoising Score Matching Objective, Probability Flow ODE

## TSNPSE (Truncated Sequential NPSE)
- **Notation**: Algorithm 1 in the paper.
- **Definition**: Sequential variant of NPSE using truncated prior proposals. In round r, the proposal is `˜p^r(θ) ∝ p(θ) · I{θ ∈ HPR_ε(p^{r-1}_ψ(θ|x_obs))}`, averaged over previous rounds. No importance weight correction is needed because the proposal is proportional to the prior within the posterior support (Proposition 3.1). Uses R=10 rounds by default with equal simulation budget M=N/R per round.
- **Boundary conditions**: Requires that the true posterior support is contained within HPR_ε at each round (Assumption A3). Computationally more expensive than TSNPE because likelihood evaluation requires solving the ODE.
- **Related concepts**: NPSE, HPR Estimation, Probability Flow ODE, DSM Objective

## HPR (Highest Probability Region)
- **Notation**: `HPR_ε(p(·|x_obs))` — the smallest region containing mass 1-ε of the posterior.
- **Definition**: Used in TSNPSE to define the truncated proposal. Estimated by: (1) drawing 20000 samples from the approximate posterior via the ODE, (2) computing their log-density via the instantaneous change-of-variables formula, (3) setting the truncation boundary κ as the ε=5×10⁻⁴ quantile.
- **Boundary conditions**: Requires density evaluation via the probability flow ODE — computationally expensive. An energy-based parameterisation of the score network (Appendix G) can reduce this cost to a single forward pass.
- **Related concepts**: TSNPSE, Probability Flow ODE, Rejection Sampling

## C2ST (Classification-Based Two-Sample Test)
- **Notation**: C2ST score ∈ [0.5, 1.0]; lower is better; 0.5 = perfect posterior approximation.
- **Definition**: A metric for comparing two distributions by training a binary classifier to distinguish samples from the approximate posterior `q_ψ(·|x_obs)` and the true posterior `p(·|x_obs)`. A score of 0.5 indicates the classifier cannot distinguish the two (perfect approximation). 10000 samples from each distribution are used for evaluation.
- **Boundary conditions**: Only applicable when samples from the true posterior are available (as in sbibm). Implemented via the sbibm library (Lopez-Paz & Oquad, 2017).
- **Related concepts**: NPSE, TSNPSE, SBI benchmarks

## Simulation-Based Inference (SBI)
- **Notation**: Also called likelihood-free inference (LFI).
- **Definition**: The problem of Bayesian inference `p(θ|x_obs) ∝ p(θ)p(x_obs|θ)` when the likelihood `p(x|θ)` is intractable but the simulator can generate samples `(θ, x) ~ p(θ)p(x|θ)`.
- **Boundary conditions**: Applies when the likelihood has no closed form but the simulator is available. Traditional ABC methods are sample-inefficient; neural SBI methods (SNPE, SNLE, SNRE, NPSE) are more efficient but require training.
- **Related concepts**: NPSE, TSNPSE, Score Function, Denoising Score Matching Objective
