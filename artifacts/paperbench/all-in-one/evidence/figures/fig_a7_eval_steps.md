---
# Figure A7: C2ST vs Number of Evaluation Steps

- **Source**: Figure A7, Appendix A3.1
- **Caption**: "For all tasks as well as the VPSDE and VESDE, we show how the performance as measured in C2ST increases as we increase the evaluation steps to solve the reverse SDE."
- **Axis labels**: X-axis = Evaluation steps (100, 250, 500, 750, 1000); Y-axis = C2ST (0.5 to 1.0)
- **Series**: Simformer (single line per task)
- **Conditions**: Both VESDE and VPSDE, 4 benchmark tasks (Linear Gaussian, Mixture Gaussian, Two Moons, SLCP)

## Key Findings

| Finding | Value |
|---------|-------|
| Sharp transition threshold | ≈50 evaluation steps |
| Minimum steps for near-best performance (VESDE) | 50 steps (all tasks) |
| Exception | Two Moons on VPSDE requires more steps |
| Default steps used in all experiments | 500 |
| Approximate sampling time at 50 steps (10k samples) | A few seconds |

## Paper-stated quantitative findings

- "There is a sharp transition from suboptimal to near-perfect performance when the number of evaluations exceeds 50."
- "For all tasks, except Two Moons on the VPSDE, 50 evaluations are sufficient to reach best performance."
- "Accurate inference is achievable with as few as 50 evaluation steps, leading to sampling times of a few seconds for 10k samples."
- This demonstrates efficiency advantage: MCMC-based methods (NLE, NRE) "typically require significantly more than 50 evaluations" for the subsequent MCMC run.
