# Figure 5.3: PosteriorDB — Relative Mean Error vs. Gradient Evaluations

**Source**: Figure 5.3 (§5.2), Figure E.6 (Appendix E.5)  
**Claims**: C05  
**Description**: Relative mean error (eq. 242) vs. number of gradient evaluations for BaM, ADVI, and GSM on three PosteriorDB models. Curves = mean over 5 runs with std error shading. Solid = B=32; dashed = B=8.

## Relative Mean Error Metric

$$\text{relative mean error} = \left\|\frac{\mu - \hat{\mu}}{\sigma}\right\|_2$$

where $\hat{\mu}$ is from variational posterior, and $\mu$, $\sigma$ are computed from HMC reference samples.

## PosteriorDB Models Tested

| Model | Dimension | Type |
|-------|-----------|------|
| arK | D=7 | Nearly Gaussian (autoregressive K) |
| gp-pois-regr | D=13 | Non-Gaussian (GP Poisson regression) |
| eight-schools-centered | D=10 | Hierarchical Bayesian (highly non-Gaussian) |

## Key Observations from Paper (§5.2)

- **BaM vs ADVI**: BaM outperforms ADVI, converging earlier to lower relative mean error.
- **GSM at small B**: GSM can converge faster than BaM for smaller batch sizes (B=8) but oscillates around the solution.
- **Batch size scaling**:
  - BaM benefits from larger batch size (B=32 converges faster and more stably than B=8).
  - ADVI and GSM do *not* benefit from increasing batch size.
- **Relative SD error**: Similar trends as mean error (Figure E.6), *except* for eight-schools-centered where BaM converges to a larger relative SD error (but GSM's low error suggests better BaM LR tuning might help).

## Initialization
- All algorithms: μ₀ ~ uniform[0, 0.1], Σ₀ = I
- BaM: λ_t = BD/(t+1)
- ADVI: learning rate selected by grid search per problem

## Relative SD Error Results (Figure E.6, Appendix E.5)

$$\text{relative SD error} = \left\|\frac{\sigma - \hat{\sigma}}{\sigma}\right\|_2$$

- Generally same trends as relative mean error.
- Exception: eight-schools-centered (hierarchical) — BaM learns mean quickly but converges to larger SD error.
- GSM shows lower SD error in hierarchical model, suggesting BaM may benefit from more careful LR tuning.
