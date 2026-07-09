---
# Table 10: EM Drop Ratio for Different Numbers of Replayed Batches

**Source**: Table 10, Appendix D.2  
**Claims**: C04  
**Description**: EM Drop Ratio (%) when replaying random examples while fixing (1) single errors or (2) continually fixing multiple errors. Replay batches counted over the full error-fixing process (30 steps total). Default = 3 mini-batches.

| # Replayed Batches | Single Errors EM Drop (%) | Multiple Errors EM Drop (%) |
|--------------------|--------------------------|------------------------------|
| 0 (Vanilla) | 0.068 | 1.129 |
| 1 | 0.064 | 0.089 |
| 3 (default) | 0.122 | 0.038 |
| 6 | 0.138 | -0.141 |

**Notes**:
- For single errors: more replay INCREASES forgetting (overfitting to replay examples)
- For multiple errors: more replay DECREASES forgetting (more coverage of at-risk examples)
- This is consistent with Buzzega et al. (2020b) and Jin et al. (2022)
- Default (3 mini-batches) of forecasted examples ≈ 6-15 mini-batches of random examples (Table 3 comparison)
- Negative EM Drop = slight improvement on upstream data
