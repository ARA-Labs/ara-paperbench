# Figure 2: Imperfect Supervision Results (§5.3)
- **Source**: Figure 2, Section 5.3
- **Caption**: "Illustrations of coreset selection under imperfect supervision. (a) Test accuracy (%) in coreset selection with 30% corrupted labels; (b) Test accuracy (%) in coreset selection with class-imbalanced data. The optimized coreset sizes by LBCS in these cases are provided in Appendix E.3."
- **Conditions**: F-MNIST; LeNet proxy + LeNet evaluation; Adam lr=0.001; 100 epochs; ε=0.2; T=500; k∈{1000,2000,3000,4000}. (a) 30% symmetric label noise; (b) exponential class imbalance ratio=0.01.

## Panel (a): 30% Corrupted Labels
**Axis labels**: x = Predefined coreset size k ∈ {1000, 2000, 3000, 4000}; y = Test accuracy (%)

Data extracted from figure (approximate values, visual reading):

| k | Uniform | EL2N | GraNd | Influential | Moderate | CCS | Probabilistic | LBCS |
|---|---------|------|-------|-------------|----------|-----|---------------|------|
| 1000 | ≈62 | ≈54 | ≈58 | ≈64 | ≈63 | ≈61 | ≈64 | ≈68 |
| 2000 | ≈70 | ≈62 | ≈65 | ≈70 | ≈71 | ≈70 | ≈72 | ≈74 |
| 3000 | ≈73 | ≈67 | ≈70 | ≈74 | ≈74 | ≈74 | ≈75 | ≈77 |
| 4000 | ≈75 | ≈70 | ≈72 | ≈76 | ≈76 | ≈76 | ≈76 | ≈79 |

**Key observation**: LBCS consistently achieves the highest test accuracy across all k values under 30% label noise.

## Panel (b): Class-Imbalanced Data (imbalance ratio=0.01)
**Axis labels**: x = Predefined coreset size k ∈ {1000, 2000, 3000, 4000}; y = Test accuracy (%)

Data extracted from figure (approximate values, visual reading):

| k | Uniform | EL2N | GraNd | Influential | Moderate | CCS | Probabilistic | LBCS |
|---|---------|------|-------|-------------|----------|-----|---------------|------|
| 1000 | ≈56 | ≈48 | ≈52 | ≈59 | ≈58 | ≈57 | ≈59 | ≈63 |
| 2000 | ≈65 | ≈57 | ≈61 | ≈66 | ≈66 | ≈65 | ≈67 | ≈70 |
| 3000 | ≈70 | ≈63 | ≈67 | ≈72 | ≈72 | ≈71 | ≈72 | ≈75 |
| 4000 | ≈74 | ≈68 | ≈71 | ≈75 | ≈75 | ≈75 | ≈75 | ≈78 |

**Note**: Values marked ≈ are best-effort readings from the figure. Exact numerical values are not provided in the paper for these figures; only the ranking and relative comparison are presented.
