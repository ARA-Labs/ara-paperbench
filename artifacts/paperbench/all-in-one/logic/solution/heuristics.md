---
# Heuristics

## H01: Random condition mask sampling from 5 distributions
- **Rationale**: Training on a mix of condition masks (joint, posterior, likelihood, Bernoulli p=0.3, Bernoulli p=0.7) ensures the model learns all conditional distributions while still emphasizing the most practically useful ones (posterior and likelihood). Found to work "slightly better than just random sampling."
- **Sensitivity**: medium
- **Bounds**: At each training batch, uniformly select one of: (a) joint mask (all zeros), (b) posterior mask (data=1, params=0), (c) likelihood mask (data=0, params=1), (d) Bernoulli(p=0.3) mask, (e) Bernoulli(p=0.7) mask.
- **Code ref**: [src/execution/simformer.py]
- **Source**: Appendix A2.1

## H02: 500 Euler-Maruyama steps for reverse SDE
- **Rationale**: Performance shows a sharp transition at ~50 steps; using 500 steps provides a comfortable safety margin. Accuracy for different budgets analyzed in Figure A7.
- **Sensitivity**: low (above 50 steps)
- **Bounds**: Minimum effective threshold ≈50 steps; default=500 steps; more steps improve ODE log-probability accuracy but not sample quality significantly.
- **Code ref**: [src/execution/simformer.py]
- **Source**: Appendix A2.1, Figure A7

## H03: Token dimension = 50 with attention size = 10 and widening factor = 3
- **Rationale**: This compact architecture balances expressiveness with computational cost for the sequence lengths encountered in SBI tasks. Token dimension 50, 4 heads, attention size 10, feed-forward hidden dimension 150 (=50×3).
- **Sensitivity**: medium
- **Bounds**: Increased to 8 layers for more complex tasks (Lotka-Volterra, SIRD, Hodgkin-Huxley); 6 layers sufficient for benchmark tasks.
- **Code ref**: [src/execution/simformer.py, src/configs/model.md]
- **Source**: Appendix A2.1

## H04: Diffusion time embedding via 128-dim random Gaussian Fourier features
- **Rationale**: Random Fourier features provide a fixed, expressive encoding of the continuous diffusion time t without requiring learnable positional embeddings. Added as a linear projection to each feed-forward block output.
- **Sensitivity**: low
- **Bounds**: 128 dimensions; also used for metadata embeddings (index set for function-valued parameters).
- **Code ref**: [src/execution/simformer.py]
- **Source**: Appendix A2.1; Section 3.1

## H05: Subsampling for function-valued parameters
- **Rationale**: For infinite-dimensional parameters (e.g., time-varying contact rate β(t)), training on randomly subsampled time points τ₁,...,τₙ exploits the Kolmogorov Extension Theorem to learn all finite-dimensional marginals. Also reduces sequence length during training.
- **Sensitivity**: medium
- **Bounds**: Applied in Lotka-Volterra and SIRD experiments. Attention mask may need modification when nodes are dropped (reconnect variables that were connected through dropped nodes).
- **Code ref**: [src/execution/simformer.py]
- **Source**: Appendix A1.2

## H06: Scaling function s(t) = 1/σ(t)² for guided diffusion
- **Rationale**: The scaling function inversely proportional to the SDE variance ensures the constraint guidance is appropriately calibrated across noise levels. Too-large scaling at high noise levels would overwhelm the diffusion score; too-small at low noise levels would fail to enforce the constraint.
- **Sensitivity**: high
- **Bounds**: s(t) = 1/σ(t)² for VESDE (σ(t)² = σ_min² · (σ_max/σ_min)^{2t}); must be adapted to the specific SDE used.
- **Code ref**: [src/execution/guided_diffusion.py]
- **Source**: Appendix A3.3

## H07: Self-recurrence (r steps) for guided diffusion accuracy
- **Rationale**: Without self-recurrence, guided diffusion approximation is less accurate (visible as excessive noise in two-moon results, Figure A16a). Self-recurrence with r=5 markedly improves results by applying a predictor-corrector correction at each step.
- **Sensitivity**: high
- **Bounds**: r=0 (fast, approximate); r=5 (5× computational cost, much more accurate). Set r=5 for energy constraint experiments in Section 4.4. Implementation: after each reverse step, re-noise future point (forward SDE step) and re-run (r times).
- **Code ref**: [src/execution/guided_diffusion.py]
- **Source**: Appendix A3.3, Algorithm 1, Figure A15, Figure A16
