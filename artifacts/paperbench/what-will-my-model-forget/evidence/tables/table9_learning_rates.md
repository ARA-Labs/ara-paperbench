---
# Table 9: Edit Success Rate and EM Drop Under Different Learning Rates

**Source**: Table 9, Appendix D.1  
**Claims**: —  
**Description**: Edit success rate (%) and EM Drop Ratio (%) under different learning rates for continual model refinement over multiple examples with Full FT on FLAN-T5Large. Default learning rate is 1e-5.

| Learning Rate | Edit Succ. (%) | EM Drop (%) |
|---------------|----------------|-------------|
| 1e-4 | 50.7 | 24.897 |
| 1e-5 (default) | 82.6 | 3.302 |
| 2e-6 | 81.1 | 1.820 |

**Notes**:
- Higher LR (1e-4): much worse edit success (50.7%) and extremely high forgetting (24.897%)
- Default LR (1e-5): balanced plasticity and stability
- Lower LR (2e-6): slightly better forgetting (1.820%) but 1.5pp lower edit success
- Precision of forecasting stable across learning rates; recall varies (Figure 4 in paper)
