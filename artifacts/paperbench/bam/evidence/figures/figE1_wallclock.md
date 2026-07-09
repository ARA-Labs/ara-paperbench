# Figure E.1: Wallclock Timings for Gaussian Targets
- **Source**: Figure E.1, Appendix E.2
- **Caption**: "Wallclock timings for the Gaussian targets example."

## Experimental Conditions
- Dimensions: D = 4, 16, 64, 128, 256
- Methods: BaM (full-rank and low-rank), ADVI, GSM, Score, Fisher

## Key Observations (from paper text)
| D Range | Observation |
|---------|-------------|
| D ≤ 64 | All methods (BaM, ADVI, GSM, Score, Fisher) have similar wallclock timing |
| D = 128, 256 | Low-rank BaM solver has similar timing to other methods |

## Implications
- Gradient evaluations are a good proxy for computational cost in the lower-dimensional regime
- BaM's O(D³) covariance update is not prohibitive because models with full covariance already assume O(D²) parameters
- Low-rank solver (Lemma B.3): O(D²B + B³) costs applicable when B << D
- All paper experiments fit the lower-dimensional or low-rank regime, except deep generative model which additionally reports wallclock in Fig E.7

Note: Exact timing values (in seconds) not reported numerically in paper; figure shows qualitative timing curves.
