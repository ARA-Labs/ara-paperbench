# Figure A15: Guidance Benchmark Comparison
- **Source**: Figure A15, Appendix A3.3
- **Caption**: "The Simformer exclusively trained for joint distribution estimation (i.e., MC is always zero and thereby disables model-based conditioning). As model-based conditioning is not feasible, conditioning is implemented through diffusion guidance. This figure demonstrates the application of varying levels of self-recurrence, denoted as r, to enforce different conditions."
- **Axis labels**: X-axis: Number of simulations (log scale); Y-axis: C2ST [0.5, 1.0]; lower is better
- **Methods**: Repaint (r=0), Repaint (r=5), General Guidance (r=0), General Guidance (r=5)
- **Tasks**: Tree (all cond.), HMM (all cond.), Two Moons (all cond.), SLCP (all cond.)
- **SDEs**: VESDE (top row), VPSDE (bottom row)

## Key Observations
- **Without self-recurrence (r=0)**: Both Repaint and General Guidance fall short of model-based conditioning within the same computational budget
- **With self-recurrence (r=5)**: Results align closely with model-based conditioning (approximately matching performance of Simformer with model-based M_C); 5× increase in computational demand
- **General Guidance vs. Repaint**: General Guidance is more flexible (extends to non-normal constraints); Repaint only handles normal conditioning

## Approximate C2ST values at 100k simulations

| Task | Method (r=0) | C2ST (r=0) | Method (r=5) | C2ST (r=5) | Model-based (approx.) |
|------|-------------|------------|-------------|------------|----------------------|
| Tree (all cond.) | Gen. Guidance | ≈0.80 | Gen. Guidance | ≈0.62 | ≈0.62 |
| HMM (all cond.) | Gen. Guidance | ≈0.85 | Gen. Guidance | ≈0.68 | ≈0.65 |
| Two Moons (all cond.) | Gen. Guidance | ≈0.75 | Gen. Guidance | ≈0.60 | ≈0.57 |
| SLCP (all cond.) | Gen. Guidance | ≈0.80 | Gen. Guidance | ≈0.62 | ≈0.60 |

**Note**: Values marked ≈ are approximate. Key finding: guidance without self-recurrence underperforms model-based conditioning; self-recurrence (r=5) closes most of the gap at 5× cost.
