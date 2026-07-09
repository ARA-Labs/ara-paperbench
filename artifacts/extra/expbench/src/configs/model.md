# Model Configuration

## Evaluated Agent: OpenHands (OH)
- **Value**: OpenHands framework (Wang et al., 2024, arXiv:2407.16741) with interchangeable LLM backbone
- **Rationale**: Top-performing code generation agent; generalizes across diverse software tasks; used as primary evaluation subject
- **Search range**: Not varied (framework is fixed; backbone LLM is varied)
- **Sensitivity**: high
- **Source**: §4.1

## Evaluated Agent: IterativeAgent (IA)
- **Value**: IterativeAgent as configured in PaperBench (Starace et al., 2025, arXiv:2504.01848), modified to reduce likelihood of early task stopping
- **Rationale**: Provides comparison to an agent that persists through the full timeout rather than stopping early with plausible output
- **Search range**: Not varied
- **Sensitivity**: medium
- **Source**: §4.1

## Backbone LLM: OpenAI o3-mini
- **Value**: o3-mini (exact version at evaluation time not specified in paper)
- **Rationale**: Top-ranked model in overall performance (rank 1 via All·E✓); achieves best cost-performance tradeoff
- **Search range**: Not varied
- **Sensitivity**: high
- **Source**: §4.1, Table 1

## Backbone LLM: Claude-3.7 Sonnet
- **Value**: claude-3-7-sonnet (Anthropic)
- **Rationale**: Rank 2 overall; highest implementation score (I=35.0) and highest conclusion score (C=14.9); most expensive and slowest
- **Search range**: Not varied
- **Sensitivity**: high
- **Source**: §4.1, Table 1, Table 9

## Backbone LLM: Amazon Nova Pro
- **Value**: Amazon Nova Pro (Amazon Bedrock)
- **Rationale**: Rank 3 overall; moderate cost, fastest OH configuration (Avg T=17.82 min)
- **Search range**: Not varied
- **Sensitivity**: medium
- **Source**: §4.1, Table 1

## Backbone LLM: Claude-3.5 Haiku
- **Value**: claude-3-5-haiku (Anthropic)
- **Rationale**: Included as lower-tier Anthropic model comparison; highest design score among OH models (D=20.6)
- **Search range**: Not varied
- **Sensitivity**: medium
- **Source**: §4.1, Table 1

## Backbone LLM: DeepSeek R1
- **Value**: DeepSeek R1 (DeepSeek)
- **Rationale**: Included as open-source reasoning model baseline; lowest overall performance among OH configurations
- **Search range**: Not varied
- **Sensitivity**: medium
- **Source**: §4.1, Table 1

## Dataset Scale
- **Value**: 461 research tasks, 12,737 individually gradable subtasks, 51 papers
- **Rationale**: Derived from NeurIPS 2024 (53%) and ICLR 2024 (47%) papers; spans 17 AI subfields
- **Search range**: Not applicable (fixed benchmark)
- **Sensitivity**: low
- **Source**: §3.1

## Task Venue Split
- **Value**: NeurIPS 2024: 53%, ICLR 2024: 47% of tasks
- **Rationale**: Covers two premier AI venues to maximize diversity of experimental paradigms
- **Search range**: Not applicable
- **Sensitivity**: low
- **Source**: §3.1
