---
source: "Section 4.7 of arXiv:2506.22419"
claims_verified: [C09]
---

# Table 5: External Knowledge Injection (Record 12 -- FlexAttention)

FSR on record 12 (FlexAttention integration) with and without FlexAttention API documentation injected into agent prompt.

| Configuration | Without FlexAttn Docs | With FlexAttn Docs | Delta |
|---------------|----------------------|-------------------|-------|
| o3-mini + L1 | ~0.05 | ~0.03 | -0.02 |
| DeepSeek-R1 + L1 | ~0.04 | ~0.02 | -0.02 |
| Gemini-2.5-Pro + L1 | ~0.03 | ~0.02 | -0.01 |
| Claude-3.7-Sonnet + L1 | ~0.02 | ~0.01 | -0.01 |

## Analysis

- **No improvement from external docs**: Injecting FlexAttention API documentation provides no benefit and slightly worsens FSR across all models.
- **Possible explanations**:
  1. API documentation adds token overhead without actionable implementation guidance
  2. Models struggle to correctly exploit unfamiliar API patterns in distributed training context
  3. The FlexAttention integration requires systems-level understanding beyond what documentation provides (correct block size alignment, document boundary tracking, interaction with existing attention code)
- **Reinforces C06**: The bottleneck is not knowledge availability but implementation capability. Providing more information does not help when the agent cannot translate knowledge into working code.
