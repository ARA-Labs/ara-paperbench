# Figure 6a: Cost–Time Trade-offs Across Agents
- **Source**: Figure 6a, Section 4.2
- **Caption**: "Cost–time trade-offs across agents."
- **Conditions**: Average cost (USD, backbone LLM token usage only) vs. average time (minutes) per task; number in parentheses next to each legend entry indicates performance rank; 40-minute soft timeout
- **Axis labels**: X-axis: Average Time (minutes); Y-axis: Average Cost ($)

## Data Points (from Table 9, supplementing figure)

| Agent | Model | Performance Rank | Avg Time (min) | Avg Cost ($) |
|-------|-------|-----------------|---------------|-------------|
| OpenHands | o3-mini | 1 | 24.89 | 0.55 |
| OpenHands | Claude-3.7 Sonnet | 2 | 33.53 | 10.15 |
| OpenHands | Amazon Nova Pro | 3 | 17.82 | 1.09 |
| OpenHands | Claude-3.5 Haiku | 4 | 25.17 | 0.68 |
| OpenHands | DeepSeek R1 | 5 | 32.24 | 1.55 |
| IterativeAgent | Claude-3.5 Haiku | 6 | 30.24 | 2.82 |
| IterativeAgent | Amazon Nova Pro | 7 | 30.09 | 3.93 |

**Key findings**:
- OH+o3-mini (rank 1): best cost-performance tradeoff — low cost ($0.55 avg) and moderate time (24.89 min avg)
- OH+3.7 Sonnet (rank 2): slowest (33.53 min) and most expensive ($10.15); good performance but poor efficiency
- IA models (ranks 6, 7): often consumed full allotted time, rarely stopping early; higher cost than comparable OH models for lower performance
- OH+Nova Pro (rank 3): fastest OH model (17.82 min avg), moderate cost ($1.09)
- Little correlation found between runtime/cost and overall performance across configurations
