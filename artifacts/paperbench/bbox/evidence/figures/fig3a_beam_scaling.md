# Figure 3(a): Accuracy vs. Number of Beams on StrategyQA
- **Source**: Figure 3(a), Section 4.6
- **Caption**: "Scale analysis on StrategyQA with (a) different beam sizes. Both experiments are conducted with two-shot prompting."
- **Axis labels**: X-axis: # Beam (k); Y-axis: Accuracy (%)
- **Conditions**: gpt-3.5-turbo generator; StrategyQA; two-shot prompting; Ground-Truth setting; 3 lines: Base+Adapter(0.1B), Base+Adapter(0.3B), Base Model (gpt-3.5-turbo without adapter)

**Note**: Exact per-beam data points are not tabulated in the paper text; values below are extracted from visual reading of Figure 3(a). Marked ≈ for estimated values.

| Beam Size (k) | Base Model Acc. (%) | Adapter 0.1B Acc. (%) | Adapter 0.3B Acc. (%) |
|---------------|--------------------|-----------------------|-----------------------|
| 1 | 66.59 | ≈68.0 | ≈68.5 |
| 3 | 66.59 | 71.62 | 71.18 |
| 5 | 66.59 | ≈70.5 | ≈71.5 |

**Key finding**: "increasing the number of beams contributes to an average performance enhancement of 2.41% across different adapter sizes (0.1B and 0.3B)" — Section 4.6.
