# Figure 3(b): Accuracy vs. Number of Online Adaptation Iterations on StrategyQA
- **Source**: Figure 3(b), Section 4.6
- **Caption**: "Scale analysis on StrategyQA with (b) different iterations of online adaptation. Both experiments are conducted with two-shot prompting."
- **Axis labels**: X-axis: # Iteration (T); Y-axis: Accuracy (%)
- **Conditions**: gpt-3.5-turbo generator; StrategyQA; two-shot prompting; Ground-Truth setting; 3 lines: Base+Adapter(0.1B), Base+Adapter(0.3B), Base Model (constant)

**Note**: Exact per-iteration values not tabulated in paper; values below are extracted from visual reading of Figure 3(b). Marked ≈ for estimated values.

| Iteration (T) | Base Model Acc. (%) | Adapter 0.1B Acc. (%) | Adapter 0.3B Acc. (%) |
|---------------|--------------------|-----------------------|-----------------------|
| 0 | 66.59 | ≈62.0 | ≈63.0 |
| 1 | 66.59 | ≈68.5 | ≈69.0 |
| 2 | 66.59 | ≈70.5 | ≈70.5 |
| 3 | 66.59 | 71.62 | 71.18 |
| 4 | 66.59 | ≈71.5 | ≈71.3 |

**Key findings** (from Section 4.6):
- T=0 (un-finetuned adapter): performs BELOW base model (random scores misguide beam search)
- T=1: surpasses base model performance
- T=3–4: convergence / plateau
