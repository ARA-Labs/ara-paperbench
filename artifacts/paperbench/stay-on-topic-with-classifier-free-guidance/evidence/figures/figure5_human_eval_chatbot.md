# Human Preference Study: CFG for Chatbot System-Prompt Following
- **Source**: Figure 5, Section 3.4
- **Caption**: "Evaluators (611 votes, 71 unique voters) significantly preferred the system-prompt with CFG (max at γ=3). The user-prompt relevance, not subject to CFG, did not degrade until γ≥4, showing a clear win without tradeoff at γ=3."
- **Axis labels**: x-axis: CFG guidance strength γ; y-axis: % preference for CFG over baseline
- **Model**: GPT4All-J v1.3-jazzy
- **Setup**: nc=25 system prompts, np=46 user prompts, 1,740 combinations; γ randomly chosen ∈ {1,2,3,4,5,6}

## Key Data Points (extracted from figure description)

| γ | System-Prompt Preference (% for CFG) | User-Prompt Relevance (% for CFG) |
|---|--------------------------------------|-----------------------------------|
| 1 | ~50% (baseline) | ~50% (baseline) |
| 2 | Increasing | ~52% |
| 3 | **75%** (peak) | **52%** (undegraded) |
| 4 | Still high | Begins degrading |
| 5 | ≈ decreasing | Degraded |
| 6 | ≈ decreasing | Degraded |

**Key findings**:
- Peak system-prompt following preference: **75% at γ=3**
- User-prompt relevance at γ=3: **52%** (not significantly different from 50% baseline)
- User-prompt relevance begins degrading at **γ ≥ 4**
- Total votes: **611** from **71 unique voters**
- Clear win-without-tradeoff region: γ=3

**Note**: Exact values for each γ are read from the bar/line chart in the paper; values marked approximately where paper text specifies exactly (γ=3: 75% system-prompt, 52% user-prompt are stated explicitly).
