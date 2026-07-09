# Figure 2: Performance under Imperfect Supervision
- **Source**: Figure 2, Section 5.3
- **Caption**: "Illustrations of coreset selection under imperfect supervision. (a) Test accuracy (%) in coreset selection with 30% corrupted labels; (b) Test accuracy (%) in coreset selection with class-imbalanced data. The optimized coreset sizes by LBCS in these cases are provided in Appendix E.3."
- **Experimental conditions**: F-MNIST dataset. LeNet for both coreset selection and final training. LBCS with ε=0.2, T=500. 10 repetitions. 30% symmetric label noise (subfigure a); exponential class imbalance ratio 0.01 (subfigure b).
- **Axis labels**: x-axis: Predefined coreset size k ∈ {1000, 2000, 3000, 4000}; y-axis: Test accuracy (%)

## Subfigure (a): 30% Corrupted Labels — approximate values read from bar chart

| Method | k=1000 | k=2000 | k=3000 | k=4000 |
|--------|--------|--------|--------|--------|
| Uniform | ≈62 | ≈65 | ≈67 | ≈69 |
| EL2N | ≈55 | ≈58 | ≈61 | ≈63 |
| GraNd | ≈58 | ≈61 | ≈63 | ≈65 |
| Influential | ≈63 | ≈66 | ≈68 | ≈70 |
| Moderate | ≈62 | ≈66 | ≈68 | ≈70 |
| CCS | ≈63 | ≈67 | ≈69 | ≈71 |
| Probabilistic | ≈64 | ≈67 | ≈70 | ≈72 |
| LBCS | ≈66 | ≈70 | ≈72 | ≈74 |

## Subfigure (b): Class-Imbalanced Data — approximate values read from bar chart

| Method | k=1000 | k=2000 | k=3000 | k=4000 |
|--------|--------|--------|--------|--------|
| Uniform | ≈60 | ≈64 | ≈68 | ≈71 |
| EL2N | ≈53 | ≈58 | ≈62 | ≈64 |
| GraNd | ≈55 | ≈59 | ≈63 | ≈66 |
| Influential | ≈61 | ≈65 | ≈68 | ≈71 |
| Moderate | ≈62 | ≈66 | ≈69 | ≈72 |
| CCS | ≈63 | ≈67 | ≈70 | ≈73 |
| Probabilistic | ≈63 | ≈67 | ≈70 | ≈73 |
| LBCS | ≈65 | ≈70 | ≈73 | ≈75 |

**Note**: Values marked ≈ are approximate readings from bar charts in the figure. Exact values are not tabulated in the paper for Figure 2; Table 6 provides the exact optimized coreset sizes. See also Figure 4 (Appendix E.2) for 50% noise results.
