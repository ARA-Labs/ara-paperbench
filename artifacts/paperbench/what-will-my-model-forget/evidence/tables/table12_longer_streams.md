---
# Table 12: F1 Scores in Longer Continual Refinement Streams on FLAN-T5Large

**Source**: Table 12, Appendix E  
**Claims**: C07  
**Description**: F1 scores at 5 time-step checkpoints while continually updating FLAN-T5Large on longer error streams. "+Accumulate" variants carry forward predicted examples from past steps.

| Method | t=1 | t=2 | t=3 | t=4 | t=5 |
|--------|-----|-----|-----|-----|-----|
| Threshold | 42.4 | 23.7 | 16.1 | 15.1 | 11.4 |
| Representation | 40.0 | 26.1 | 23.2 | 22.4 | 12.4 |
| Representation + Accumulate | **49.3** | **39.6** | **33.7** | **31.7** | **23.4** |
| Logit | 31.8 | 30.6 | 26.1 | 21.5 | 15.2 |
| Logit + Accumulate | 34.0 | 39.6 | 35.9 | 27.3 | 21.7 |

**Notes**:
- F1 decreases over time for all methods as more examples become forgotten (recall drops)
- Accumulating predicted examples from past steps significantly improves F1 for both methods
- Representation + Accumulate achieves highest F1 at all time steps
- Threshold F1 also drops steeply as it cannot adapt to new forgetting patterns
