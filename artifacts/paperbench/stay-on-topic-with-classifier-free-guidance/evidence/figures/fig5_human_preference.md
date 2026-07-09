---
# Figure 5: Human Preference Study Results (GPT4All with CFG)
- **Source**: Figure 5, Section 3.4
- **Caption**: "Evaluators (611 votes, 71 unique voters) significantly preferred the system-prompt with CFG (max at γ=3). The user-prompt relevance, not subject to CFG, did not degrade until γ≥4, showing a clear win without tradeoff at γ=3."
- **Model**: GPT4All-J v1.3-jazzy
- **Setup**: 25 system prompts × 46 user prompts = 1,740 combinations; negative prompt = default system prompt; guidance strength randomly chosen from {1, 2, 3, 4, 5, 6}
- **Axes**: x-axis = guidance strength γ; y-axis = % preference for CFG over vanilla

**Data points (read from figure description):**

| γ | System-Prompt Following Preference (%) | User-Prompt Relevance Preference (%) |
|---|----------------------------------------|--------------------------------------|
| 1 | ≈50% (baseline / random) | ≈50% |
| 2 | > 50% (increasing) | ≈50% |
| 3 | 75% (peak) | 52% (undegraded) |
| 4 | < 75% (declining) | ≈50% (beginning to degrade) |
| 5 | decreasing | < 50% (degraded) |
| 6 | decreasing | < 50% (degraded) |

**Key findings**:
- Peak system-prompt preference: **75%** at γ=3
- User-prompt relevance at γ=3: **52%** (approximately random — not degraded)
- User-prompt relevance degrades significantly at γ≥4
- Total votes: **611** from **71** unique voters
- Conclusion: Clear win at γ=3 with no tradeoff between system-prompt adherence and user-prompt relevance

**Note**: Exact per-γ vote counts not provided in the paper; values above are extracted from the figure description and text. ≈ marks approximate readings.
