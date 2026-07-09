# Figure E.6: PosteriorDB — Relative SD Error vs. Gradient Evaluations

**Source**: Figure E.6, Appendix E.5  
**Claims**: C05  
**Description**: Relative standard deviation error (eq. 242) vs. gradient evaluations for BaM, ADVI, and GSM on three PosteriorDB models. Same setup as Figure 5.3 but measuring SD error instead of mean error.

## Relative SD Error Metric

$$\text{relative SD error} = \left\|\frac{\sigma - \hat{\sigma}}{\sigma}\right\|_2$$

where $\hat{\sigma}$ is the variational standard deviation (diagonal of sqrt(Σ)), and $\sigma$ is from HMC reference.

## PosteriorDB Models

| Model | Dimension | General SD Error Trend |
|-------|-----------|------------------------|
| arK | D=7 | BaM outperforms ADVI; GSM oscillates (same as mean error) |
| gp-pois-regr | D=13 | BaM outperforms ADVI; GSM oscillates (same as mean error) |
| eight-schools-centered | D=10 | BaM converges to larger SD error than GSM; exception to general trend |

## Key Observations from Paper (Appendix E.5)

- **General trend**: Same trends as relative mean error for arK and gp-pois-regr models — BaM outperforms ADVI; GSM oscillates.
- **Exception — eight-schools-centered (hierarchical model)**:
  - BaM converges quickly to a low mean error but *converges to a larger relative SD error* than GSM.
  - Suggests BaM approximates the posterior mean well but underestimates posterior variance in the hierarchical model.
  - Paper note: "the low error of GSM suggests that more robust tuning of the learning rate may lead to better performance with BaM."
- **Batch size effect**: Same as mean error — BaM benefits from B=32 vs B=8; ADVI/GSM do not.
