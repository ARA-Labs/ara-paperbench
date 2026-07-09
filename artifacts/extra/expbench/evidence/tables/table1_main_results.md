# Table 1: Average Benchmark Scores — All Agents on EXP-Bench
- **Source**: Table 1, Section 4.1
- **Caption**: "Average benchmark scores for various models when tested against various evaluation metrics. Popular Agents and LLMs perform poorly on EXP-Bench, showcasing its difficulty."
- **Conditions**: 461 research tasks from 51 papers (NeurIPS 2024 + ICLR 2024); Ubuntu 24.04 Docker; 4× NVIDIA A40; 40-minute timeout per task; LLM judge: o3-mini-2025-01-01-preview

| Agent | Model | D | I | E | C | I·E | All✓ | All·E✓ |
|-------|-------|---|---|---|---|-----|-------|---------|
| OpenHands | o3-mini | 18.4 | 20.3 | 15.0 | 2.9 | 21.0 | 1.4 | 0.5 |
| OpenHands | Claude-3.7 Sonnet | 16.0 | 35.0 | 33.2 | 14.9 | 13.4 | 0.7 | 0.4 |
| OpenHands | Amazon Nova Pro | 18.2 | 19.5 | 26.8 | 0.0 | 15.7 | 0.0 | 0.0 |
| OpenHands | Claude-3.5 Haiku | 20.6 | 26.2 | 9.3 | 1.3 | 13.8 | 0.0 | 0.0 |
| OpenHands | DeepSeek R1 | 6.8 | 10.0 | 0.7 | 0.0 | 2.4 | 0.0 | 0.0 |
| IterativeAgent | Claude-3.5 Haiku | 6.4 | 20.6 | 25.2 | 5.4 | 2.2 | 0.0 | 0.0 |
| IterativeAgent | Amazon Nova Pro | 0.1 | 10.0 | 18.1 | 0.0 | 0.3 | 0.0 | 0.0 |

**Notes**:
- D = design correctness (proportion of design criteria met, %)
- I = implementation correctness (proportion of implementation components satisfied, %)
- E = executability (% of tasks where code executes and produces expected outputs)
- C = conclusion correctness (% of tasks with correct conclusion)
- I·E = implementation correct AND executable
- All✓ = D > 0 AND I > 0 AND C correct (no execution requirement)
- All·E✓ = D > 0 AND I > 0 AND C correct AND executable
- Ranking: OH+o3-mini (1st), OH+3.7 Sonnet (2nd), OH+Nova Pro (3rd) via All·E✓ with C as tiebreaker
- #E (tasks execution-checked) not listed in main table; only subset of monitor-passing traces executed
