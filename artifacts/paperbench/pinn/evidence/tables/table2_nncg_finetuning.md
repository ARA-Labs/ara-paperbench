# Table 2: Loss and L2RE After Fine-tuning by NNCG and GD

**Source**: Table 2, Section 7.3
**Caption**: Loss and L2RE after fine-tuning by NNCG and GD. NNCG outperforms both GD and the original Adam+L-BFGS results.

## Raw Data

| Optimizer | Convection Loss | Convection L2RE | Reaction Loss | Reaction L2RE | Wave Loss | Wave L2RE |
|-----------|----------------|-----------------|---------------|----------------|-----------|-----------|
| Adam+L-BFGS | 5.95e-6 | 4.19e-3 | 5.26e-6 | 1.92e-2 | 1.12e-3 | 5.52e-2 |
| Adam+L-BFGS+NNCG | 3.63e-7 | 1.94e-3 | 2.89e-7 | 9.92e-3 | 6.13e-5 | 1.27e-2 |
| Adam+L-BFGS+GD | 5.95e-6 | 4.19e-3 | 5.26e-6 | 1.92e-2 | 1.12e-3 | 5.52e-2 |

## Key Derived Statistics
- NNCG loss improvement over Adam+L-BFGS:
  - Convection: 5.95e-6 / 3.63e-7 ≈ **16.4×** reduction
  - Reaction: 5.26e-6 / 2.89e-7 ≈ **18.2×** reduction
  - Wave: 1.12e-3 / 6.13e-5 ≈ **18.3×** reduction (all > 10× as claimed)
- GD makes **zero improvement** from the Adam+L-BFGS starting point

## Notes
- Note: Adam+L-BFGS reaction loss in Table 2 (5.26e-6) differs slightly from Table 1 (3.26e-6); Table 2 uses a specific run (not best across all widths)
- NNCG hyperparameters: rank=60, update_freq=20, cg_tol=1e-16, cg_max_iters=1000; µ tuned from {1e-5,...,1e-1}
