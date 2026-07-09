---
# Figure 3: Forecasting Performance Over Continual Refinement Stream

**Source**: Figure 3, §5.1  
**Claims**: C07  
**Description**: F1, Precision, and Recall of representation-based (Rep), threshold-based (Thres), and trainable logit-based (Logit) forecasting models averaged up to a given time step during continual refinement of FLAN-T5Large with Full FT.

## Key Trends (Qualitative — exact plot values not digitized)

### (a) F1 — FLAN-T5Large Full FT
| Time Step | Rep (approx.) | Thres (approx.) | Logit (approx.) |
|-----------|---------------|-----------------|-----------------|
| Early | ~0.55 | ~0.48 | ~0.45 |
| Middle | ~0.47 | ~0.40 | ~0.38 |
| End | ~0.40 | ~0.35 | ~0.35 |

**Trend**: Representation-based achieves best F1 throughout; all methods decline over time.

### (b) Precision — FLAN-T5Large Full FT
| Time Step | Rep (approx.) | Thres (approx.) | Logit (approx.) |
|-----------|---------------|-----------------|-----------------|
| Early | ~0.55 | ~0.45 | ~0.45 |
| Middle | ~0.55 | ~0.45 | ~0.43 |
| End | ~0.55 | ~0.44 | ~0.42 |

**Trend**: Precision remains mostly STABLE across all time steps for all methods (key finding). Rep achieves highest stable precision.

### (c) Recall — FLAN-T5Large Full FT
| Time Step | Rep (approx.) | Thres (approx.) | Logit (approx.) |
|-----------|---------------|-----------------|-----------------|
| Early | ~1.00 | ~0.75 | ~0.50 |
| Middle | ~0.55 | ~0.40 | ~0.35 |
| End | ~0.25 | ~0.28 | ~0.28 |

**Trend**: Recall DROPS over time for all methods as more examples become forgotten (positive class grows).

## Key Observations (from paper §5.1):
- Precision is mostly stable throughout the stream → forecasting models remain effective in sequential updates
- Recall drops over time → future work should focus on improving recall in continual settings
- Representation-based achieves highest F1 and precision at end of stream
- Relative ordering matches single-error results from Table 1
