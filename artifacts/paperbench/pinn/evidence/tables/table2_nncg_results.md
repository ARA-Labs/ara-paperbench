---
# Table 2: Loss and L2RE After NNCG and GD Fine-Tuning

- **Source**: Table 2, Section 7.3
- **Caption**: "Loss and L2RE after fine-tuning by NNCG and GD. NNCG outperforms both GD and the original Adam+L-BFGS results."
- **Experimental conditions**: Starting from best Adam+L-BFGS run (lowest L2RE per PDE), then 2000 additional steps with NNCG (μ tuned) or GD. NNCG parameters: η=1, K=2000, s=60, F=20, μ∈{1e-2,1e-1} best.

| Optimizer | Convection Loss | Convection L2RE | Reaction Loss | Reaction L2RE | Wave Loss | Wave L2RE |
|-----------|----------------|-----------------|---------------|---------------|-----------|-----------|
| Adam+L-BFGS | 5.95e-6 | 4.19e-3 | 5.26e-6 | 1.92e-2 | 1.12e-3 | 5.52e-2 |
| Adam+L-BFGS+NNCG | 3.63e-7 | 1.94e-3 | 2.89e-7 | 9.92e-3 | 6.13e-5 | 1.27e-2 |
| Adam+L-BFGS+GD | 5.95e-6 | 4.19e-3 | 5.26e-6 | 1.92e-2 | 1.12e-3 | 5.52e-2 |

**Notes**:
- NNCG reduces loss by: 16.4× (convection), 18.2× (reaction), 18.3× (wave)
- NNCG reduces L2RE by: 2.16× (convection), 1.94× (reaction), 4.35× (wave)
- GD produces zero improvement (exactly same values as Adam+L-BFGS baseline)
- Reaction Adam+L-BFGS loss in this table (5.26e-6) differs slightly from Table 1 (3.26e-6) because Table 2 uses the run with lowest L2RE, not lowest loss
