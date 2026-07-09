---
# Training Configuration

## Optimizer
- **Value**: Adam
- **Rationale**: Standard optimizer for deep learning; used consistently across all methods (Simformer, NPE, NLE, NRE).
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Appendix A2.1

## Batch Size
- **Value**: 1000
- **Rationale**: Consistent with baseline methods; large batch improves gradient estimates for score-matching.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: Appendix A2.1

## Early Stopping
- **Value**: Enabled, based on validation loss
- **Rationale**: Prevents overfitting; determines when to stop training without a fixed number of epochs.
- **Search range**: Not specified (patience not explicitly given)
- **Sensitivity**: medium
- **Source**: Appendix A2.1

## Simulation Budgets (Benchmark)
- **Value**: 10³, 10⁴, 10⁵ simulations (separate training runs)
- **Rationale**: Tests simulation efficiency across orders of magnitude.
- **Search range**: [10³, 10⁵]
- **Sensitivity**: high
- **Source**: Section 4.1, Figure 4

## Simulation Budget (Lotka-Volterra, SIRD, Hodgkin-Huxley)
- **Value**: 10⁵ simulations
- **Rationale**: Complex physical simulators require more training data.
- **Search range**: 10³–10⁵ (also tested at 10³, 10⁴ for LV)
- **Sensitivity**: high
- **Source**: Section 4.2, 4.3, 4.4

## Condition Mask Sampling Distribution
- **Value**: At each training batch, uniformly select one of 5 mask types:
  1. Joint: $M_C = [0,...,0]$
  2. Posterior: data variables = 1, parameter variables = 0
  3. Likelihood: data variables = 0, parameter variables = 1
  4. Random Bernoulli with p=0.3 (independently per element)
  5. Random Bernoulli with p=0.7 (independently per element)
- **Rationale**: Found to work slightly better than purely random sampling; ensures coverage of all practically useful conditionals.
- **Search range**: Bernoulli probabilities {0.3, 0.7} chosen empirically
- **Sensitivity**: medium
- **Source**: Appendix A2.1

## VESDE Parameters (Primary SDE)
- **σ_max**: 15
- **σ_min**: 0.0001
- **Time interval**: [1e-5, 1.0]
- **Drift**: $f_\text{VESDE}(x, t) = 0$
- **Diffusion**: $g_\text{VESDE}(t) = \sigma_{\min} \cdot \left(\frac{\sigma_{\max}}{\sigma_{\min}}\right)^t \cdot \sqrt{2\log\frac{\sigma_{\max}}{\sigma_{\min}}}$
- **Perturbation kernel**: $p_t(x_t|x_0) = \mathcal{N}(x_t; x_0, \sigma_{\min}^2(\sigma_{\max}/\sigma_{\min})^{2t} \cdot I)$
- **Rationale**: Standard VESDE parameterization; σ_max=15 ensures sufficient noise to destroy data structure at t=1.
- **Sensitivity**: medium (σ_max critical; σ_min low-sensitivity)
- **Source**: Appendix A2.1, Equations 4 and 5

## VPSDE Parameters (Alternative SDE, Appendix only)
- **β_min**: 0.01
- **β_max**: 10
- **Time interval**: [1e-5, 1.0]
- **Drift**: $f_\text{VPSDE}(x, t) = -0.5 \cdot (\beta_{\min} + t \cdot (\beta_{\max} - \beta_{\min})) \cdot x$
- **Diffusion**: $g_\text{VPSDE}(t) = \sqrt{\beta_{\min} + t \cdot (\beta_{\max} - \beta_{\min})}$
- **Rationale**: Alternative noise schedule; comparable performance to VESDE with slight differences per task.
- **Sensitivity**: medium
- **Source**: Appendix A2.1, Equations 4 and 5

## Reverse SDE Discretization Steps
- **Value**: 500 steps (default)
- **Rationale**: Sharp performance transition at ~50 steps; 500 provides comfortable margin. Euler-Maruyama discretization.
- **Search range**: 50–1000 (see Figure A7)
- **Sensitivity**: low (above 50), high (below 50)
- **Source**: Appendix A2.1, Figure A7

## NPE/NLE/NRE Baseline Training
- **Library**: sbi (Tejero-Cantero et al., 2020)
- **Network**: Neural spline flow for NPE and NLE (more expressive than default); default for NRE
- **Optimizer**: Adam
- **Batch size**: 1000
- **Stopping**: Early stopping on validation loss
- **Source**: Appendix A2.1
