# Experiment Plans

## E01: Main Agent Evaluation on All 461 EXP-Bench Tasks
- **Verifies**: C01, C02
- **Setup**:
  - Model: 7 configurations — (OpenHands × {o3-mini, Claude-3.7 Sonnet, Amazon Nova Pro, Claude-3.5 Haiku, DeepSeek R1}) + (IterativeAgent × {Claude-3.5 Haiku, Amazon Nova Pro})
  - Hardware: 4× NVIDIA A40 GPU per agent run; Ubuntu 24.04 Docker container
  - Dataset: EXP-Bench, 461 tasks from 51 papers (NeurIPS 2024 + ICLR 2024)
  - System: Fresh repository clone per agent; masked files applied via scripted git operations; 40-minute soft timeout per task
- **Procedure**:
  1. For each agent configuration, clone the task repository into a fresh Docker container with 4× A40 GPUs and task-specific credentials.
  2. Apply file masking using scripted git operations (recursive submodule traversal).
  3. Provide the agent with: research question, high-level method description, masked repository, and relevant API credentials.
  4. Allow agent to run for up to 40 minutes; record all agent logs and generated artifacts.
  5. Run the monitor check (o3-mini) to detect paper access, git operations, or faked data; discard failed traces.
  6. Evaluate design (D): compare agent-specified design variables against ground truth $D_{gt}$ using LLM judge (o3-mini); compute percentage of correct items.
  7. Evaluate implementation (I): compare agent git diff against $\Delta_{gt}$ and reference scripts using LLM judge; compute percentage of fulfilled requirements.
  8. Evaluate conclusion (C): compare agent conclusion text against $C_{gt}$ for semantic match (correct/incorrect).
  9. Run code execution validator: apply agent diff to clean repository and execute; record success/failure (E).
  10. Compute conjunctive metrics: I·E, All✓ (D∧I∧C), All·E✓ (D∧I∧C∧E).
  11. Aggregate results across all 461 tasks per agent configuration.
- **Metrics**: D (%), I (%), E (%), C (correct/incorrect), I·E (%), All✓ (%), All·E✓ (%)
- **Expected outcome**:
  - OpenHands + o3-mini and OpenHands + Claude-3.7 Sonnet are the top-performing configurations overall
  - All agents score low on the strictest conjunctive metric (All·E✓); no agent achieves strong end-to-end performance
  - OpenHands-based configurations generally outperform IterativeAgent-based ones
  - DeepSeek R1 and IterativeAgent + Amazon Nova Pro are the weakest configurations across most metrics
- **Baselines**: Human expert (implicit via paper ground truth); PaperBench agents; RE-Bench agents
- **Dependencies**: none

## E02: Conjunctive Metric Strictness Analysis
- **Verifies**: C03
- **Setup**:
  - Model: OpenHands × {o3-mini, Claude-3.7 Sonnet, Amazon Nova Pro, Claude-3.5 Haiku} + IterativeAgent × {Claude-3.5 Haiku, Amazon Nova Pro} + OpenHands × {DeepSeek R1}
  - Hardware: Same as E01
  - Dataset: Execution-verified subset of EXP-Bench tasks (tasks that passed monitor check and had execution run)
  - System: Same containerized environment as E01
- **Procedure**:
  1. Filter the full evaluation results from E01 to include only tasks where execution was run (i.e., passed monitor check and code execution validator was invoked).
  2. Compute average score at each conjunction level: (a) M only, (b) M·C·D, (c) M·C·D·I, (d) M·C·D·I·E.
  3. For each level, record the average across all agent configurations on the execution-verified subset.
  4. Plot average score (%) vs. judge metric conjunction level for each agent.
  5. Verify monotone decrease across all agents and measure the magnitude of score collapse.
- **Metrics**: Average score (%) at M, M·C·D, M·C·D·I, M·C·D·I·E levels
- **Expected outcome**:
  - Scores decrease monotonically at each conjunction level across all agent configurations
  - The steepest drop occurs when adding execution verification
  - The most stringent conjunction level collapses scores to near zero for all agents
- **Baselines**: none (within-benchmark comparison)
- **Dependencies**: E01

## E03: Failure Pattern Analysis Across All Phases
- **Verifies**: C04, C05
- **Setup**:
  - Model: All 7 agent configurations from E01
  - Hardware: Analysis performed post-hoc on stored evaluation logs
  - Dataset: All 461 EXP-Bench task evaluation traces including error logs (stderr, judge outputs, implementation diffs)
  - System: Two-pass open-ended LLM-assisted categorization process
- **Procedure**:
  1. For each evaluated agent-task pair, collect metric score and accompanying error analysis derived from implementation logs and ground truth comparisons.
  2. First pass: extract high-level, domain-specific failure insights from error analyses across all phases (implementation, execution, design, conclusion).
  3. Second pass: iteratively group insights into distinct failure types — assign each insight to an existing category or create a new one.
  4. Compute prevalence (%) of each failure type within its phase.
  5. Distill raw insights (3,238 total) into unique failure types (361 total); report a simplified subset in Table 2.
  6. Compute prevalence of the dominant failure type per phase.
- **Metrics**: Prevalence (%) of each failure type within phase; total raw insights count; total unique failure types
- **Expected outcome**:
  - Missing essential implementation components is the dominant failure type in the implementation phase
  - Environment/dependency configuration errors dominate execution failures, followed closely by execution script and file errors
  - In the design phase, incomplete or misclassified design variables are the most prevalent failure type
  - Missing conclusion content is the most common conclusion failure, followed by incorrect conclusion interpretation
  - Raw insights distill into a much smaller set of unique failure types, indicating strong clustering of failure modes
- **Baselines**: none
- **Dependencies**: E01

## E04: Metric Stability Analysis (Individual vs. Conjunctive)
- **Verifies**: C06
- **Setup**:
  - Model: All 7 agent configurations from E01
  - Hardware: Post-hoc analysis on E01 results
  - Dataset: All evaluated EXP-Bench tasks with per-task scores for C, E, C·D, I·E
  - System: Statistical analysis of score distributions
- **Procedure**:
  1. For each agent configuration, collect per-task scores for individual metrics C and E, and conjunctive metrics C·D and I·E.
  2. Compute variance (or standard deviation) of each metric across all tasks, per agent.
  3. Compare variance of C vs. C·D and variance of E vs. I·E to verify conjunctive forms reduce variance.
  4. Identify sources of high variance in C (plausible but unfounded conclusions without valid experiments) and E (incorrect implementations that still execute).
  5. Verify that C·D filters conclusions not grounded in valid design, and I·E discounts executions that do not fulfill setup requirements.
- **Metrics**: Per-metric score variance across tasks; qualitative identification of variance sources
- **Expected outcome**:
  - Individual metrics (C, E) exhibit higher variance than their conjunctive forms (C·D, I·E)
  - High variance in C stems from plausible but unfounded conclusions without valid experiments
  - High variance in E stems from incorrect implementations that still execute
  - Conjunctive forms reduce variance by filtering out these spurious successes
- **Baselines**: none
- **Dependencies**: E01

## E05: Cost–Time Analysis Across Agent Configurations
- **Verifies**: C01 (indirectly — shows best agent achieves good cost-performance tradeoff)
- **Setup**:
  - Model: All 7 agent configurations from E01
  - Hardware: Same as E01; 40-minute soft timeout
  - Dataset: All 461 EXP-Bench tasks
  - System: Token usage logging for cost; wall-clock time logging for duration
- **Procedure**:
  1. For each agent run, record wall-clock time from task start to termination (minutes) and token usage for the backbone LLM (input + output tokens only; exclude agent-internal LLM API calls and compute consumption).
  2. Convert token usage to USD cost using provider pricing at evaluation time.
  3. Compute summary statistics per agent: average, median, Q1, Q3, std, min, max for both time and cost.
  4. Plot average cost vs. average time per agent configuration with performance rank annotations.
  5. Compute correlation between (average time, average cost) and overall performance (average correctness across metrics).
- **Metrics**: Average/median/Q1/Q3/std/min/max time (minutes) and cost (USD) per agent
- **Expected outcome**:
  - Higher cost and runtime do not reliably predict better performance; there is little correlation between resource consumption and task success
  - The top-ranked agent is among the cheapest and fastest, while the most expensive agent is not the best performer
  - IterativeAgent configurations tend to be more expensive per task than comparably-performing OpenHands configurations
- **Baselines**: none
- **Dependencies**: E01
