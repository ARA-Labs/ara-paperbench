# Human Preference Study: CFG vs Vanilla for Chatbot System-Prompt Adherence

- **Source**: Figure 5, Section 3.4
- **Caption**: "Evaluators (611 votes, 71 unique voters) significantly preferred the system-prompt with CFG (max at γ=3). The user-prompt relevance, not subject to CFG, did not degrade until γ≥4, showing a clear win without tradeoff at γ=3."
- **Conditions**: GPT4All-J v1.3-jazzy; 25 system prompts, 46 user prompts, 1740 sampled combinations; guidance strength γ randomly drawn from {1, 2, 3, 4, 5, 6}; blind pairwise human evaluation; 611 total votes; 71 unique voters

## System-Prompt Adherence Preference (% preferring CFG)

| γ | % Prefer CFG (System Prompt) | Notes |
|---|------------------------------|-------|
| 1 | ~50% | Baseline (random chance) |
| 2 | >50% | Improvement over baseline |
| 3 | 75% | Peak preference — clear win |
| 4 | ~65% (estimated) | Still above 50% |
| 5 | ~55% (estimated) | Declining |
| 6 | ~50% (estimated) | Near baseline |

Note: Exact values for γ≠3 are approximate readings from Figure 5. Only γ=3 (75%) is stated explicitly in text.

## User-Prompt Relevance Preference (% preferring CFG)

| γ | % Prefer CFG (User Prompt) | Notes |
|---|---------------------------|-------|
| 1 | ~50% | Baseline |
| 2 | ~52% | Not statistically different from chance |
| 3 | 52% | "undegraded user-prompt relevance" — stated explicitly |
| 4 | ~50% | Beginning of degradation |
| 5 | <50% | Below chance; CFG hurts user-prompt relevance |
| 6 | <50% | Significant degradation |

## Key Finding
CFG at γ=3 achieves 75% preference for system-prompt adherence with no meaningful tradeoff in user-prompt relevance (52%, statistically indistinguishable from 50%). This represents the "sweet spot" for chatbot applications.
