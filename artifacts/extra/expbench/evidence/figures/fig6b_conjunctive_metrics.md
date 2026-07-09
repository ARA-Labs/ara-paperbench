# Figure 6b: Conjunctive Metrics — Progressive Score Collapse
- **Source**: Figure 6b, Section 4.2 (main paper); Figure 14, Appendix I.1 (extended with all agents)
- **Caption**: "Stricter metrics reveal lower true correctness."
- **Conditions**: Execution-verified subset of tasks only (tasks that passed monitor check and had execution run); average score (%) vs. judge metric conjunction level

## Data Points — Average Score at Each Conjunction Level

*From Figure 6b (main paper, 4 OH configurations) and Figure 14 (all 7 configurations):*

| Judge Metric Level | Approximate Average Score (%) | Notes |
|-------------------|-------------------------------|-------|
| M (monitor only) | 20.6 | Stated explicitly in §4.2 |
| M·C·D | 3.7 | Stated explicitly in §4.2 |
| M·C·D·I | 0.4 | Stated explicitly in §4.2 |
| M·C·D·I·E | 0.2 | Stated explicitly in §4.2 |

**Per-agent values at M·C·D·I·E** (from Figure 14, approximate visual readings):

| Agent | Model | M·C·D·I·E Score (%) |
|-------|-------|---------------------|
| OpenHands | o3-mini | ≈0.5 (matches All·E✓ from Table 1) |
| OpenHands | Claude-3.7 Sonnet | ≈0.4 (matches All·E✓ from Table 1) |
| OpenHands | Amazon Nova Pro | 0.0 (matches Table 1) |
| OpenHands | Claude-3.5 Haiku | 0.0 (matches Table 1) |
| OpenHands | DeepSeek R1 | 0.0 (matches Table 1) |
| IterativeAgent | Claude-3.5 Haiku | 0.0 (matches Table 1) |
| IterativeAgent | Amazon Nova Pro | 0.0 (matches Table 1) |

**Key finding**: Monotone score decrease at every conjunction step; 100× collapse from M-only (20.6%) to M·C·D·I·E (0.2%); demonstrates that partial metrics substantially overestimate true end-to-end agent capability.
