# Figure 5: Human Evaluation — GPT4All System-Prompt Faithfulness
- **Source**: Figure 5, Section 3.4
- **Caption**: "Evaluators (611 votes, 71 unique voters) significantly preferred the system-prompt with CFG (max at γ=3). The user-prompt relevance, not subject to CFG, did not degrade until γ≥4, showing a clear win without tradeoff at γ=3."
- **Model**: GPT4All-J v1.3-jazzy; 1,740 sampled prompt combinations (25 system × 46 user prompts)
- **Axis labels**: X = guidance strength γ (1–6); Y = preference % for CFG over baseline

## System-Prompt Following Preference (A: which output better follows system-prompt c)

| γ | System-Prompt Following Preference (%) |
|---|----------------------------------------|
| 1 | ≈ 50% (baseline — equal) |
| 2 | > 50% (above baseline) |
| 3 | ≈ 75% (peak preference for CFG) |
| 4 | still high but beginning to decline |
| 5 | declining |
| 6 | declining further |

## User-Prompt Relevance (B: which output better follows user-prompt p)

| γ | User-Prompt Relevance (%) |
|---|--------------------------|
| 1 | ≈ 50% (baseline — equal) |
| 2 | ≈ 50% (no degradation) |
| 3 | ≈ 52% (no significant degradation — reported as 52%) |
| 4 | begins to degrade below 50% |
| 5 | degraded |
| 6 | further degraded |

**Key findings**:
- Clear peak for system-prompt following preference at γ=3 (75%)
- User-prompt relevance undegraded at γ=3 (52%), degradation begins at γ≥4
- γ=3 is the "sweet spot" with no tradeoff between system-prompt and user-prompt adherence
- Evaluated with 611 total votes from 71 unique voters
- Negative prompting setup: c̄ = default GPT4All system-prompt; c = customized system-prompt
