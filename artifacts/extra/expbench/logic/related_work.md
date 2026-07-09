# Related Work

## RW01: OpenHands (Wang et al., 2024)
- **DOI**: arXiv:2407.16741
- **Type**: baseline
- **Delta**:
  - What changed: EXP-Bench uses OpenHands as a primary evaluation agent rather than a code generation tool; tests it on research experimentation tasks rather than software engineering tasks
  - Why: OpenHands is a top-performing code generation agent; provides a strong baseline for assessing AI research automation capability
- **Claims affected**: C01, C02
- **Adopted elements**: Agent framework and execution environment; Docker containerization approach

## RW02: PaperBench / IterativeAgent (Starace et al., 2025)
- **DOI**: arXiv:2504.01848
- **Type**: baseline, extends
- **Delta**:
  - What changed: EXP-Bench uses IterativeAgent configuration from PaperBench but applies it to tasks requiring implementation generation, not just script execution. EXP-Bench also requires conjunctive evaluation vs. PaperBench's focus on script running and documented analysis
  - Why: PaperBench represents the closest prior work on paper-grounded agent evaluation; IterativeAgent reduces early stopping to test sustained task engagement
- **Claims affected**: C01, C02, C03
- **Adopted elements**: IterativeAgent configuration; LLM-as-a-judge evaluation pattern

## RW03: RE-Bench (Wijk et al., 2024)
- **DOI**: arXiv (RE-Bench)
- **Type**: baseline
- **Delta**:
  - What changed: EXP-Bench scales from 7 hand-curated tasks to 461 semi-automatically curated tasks; adds execution validation and multi-phase conjunctive scoring
  - Why: RE-Bench's hand-curation approach cannot scale; its 7 tasks provide insufficient statistical coverage of AI research diversity
- **Claims affected**: C01, C02
- **Adopted elements**: Human-vs-agent comparison framing; research task grounding concept

## RW04: MLE-Bench (Chan et al., 2024)
- **DOI**: arXiv:2410.07095
- **Type**: baseline
- **Delta**:
  - What changed: EXP-Bench targets open AI research experiments from academic papers rather than Kaggle-style ML competitions; requires full experimental workflow rather than constrained hyperparameter tuning
  - Why: Kaggle tasks have simplified evaluation metrics and constrained environments that do not reflect real research complexity
- **Claims affected**: C01
- **Adopted elements**: Code execution validation concept; containerized evaluation environment

## RW05: ScienceAgentBench (Chen et al., 2024)
- **DOI**: arXiv:2410.05080
- **Type**: baseline
- **Delta**:
  - What changed: EXP-Bench requires end-to-end experimentation including execution, not just data analysis or hypothesis testing; tasks are grounded in peer-reviewed AI papers, not data science scenarios
  - Why: Data-driven scientific discovery benchmarks isolate analysis from the broader experimental context
- **Claims affected**: C01
- **Adopted elements**: Scientific coding evaluation framework concept

## RW06: BLADE (Gu et al., 2024)
- **DOI**: arXiv:2408.09667
- **Type**: baseline
- **Delta**:
  - What changed: EXP-Bench requires implementation generation and execution, not primarily post-hoc data analysis; covers diverse AI subfields rather than data science
  - Why: BLADE primarily assesses data-driven science without requiring agents to generate and run new experiments
- **Claims affected**: C01
- **Adopted elements**: Benchmarking framework for data analysis tasks

## RW07: BoxingGym (Gandhi et al., 2025)
- **DOI**: arXiv (BoxingGym)
- **Type**: baseline
- **Delta**:
  - What changed: EXP-Bench uses real, peer-reviewed papers with actual code rather than simulated theory formation environments
  - Why: Simulated environments do not capture the complexity of real AI research codebases and experimental workflows
- **Claims affected**: C01
- **Adopted elements**: Concept of benchmarking automated experimental design

## RW08: Curie (Kon et al., 2025)
- **DOI**: arXiv (Curie)
- **Type**: extends
- **Delta**:
  - What changed: EXP-Bench provides the benchmark dataset and evaluation framework for Curie; scales evaluation to 461 tasks with semi-automated curation
  - Why: Curie compares agents against humans on research tasks but at limited scale with simplified metrics; EXP-Bench provides the large-scale, multi-phase evaluation infrastructure
- **Claims affected**: C01, C02, C03
- **Adopted elements**: Research task formulation; agent-based experimentation concept

## RW09: AAAR-1.0 (Lou et al., 2024)
- **DOI**: arXiv (AAAR)
- **Type**: baseline
- **Delta**:
  - What changed: EXP-Bench requires actual experiment execution, not reasoning over static artifacts; tasks are grounded in executable codebases
  - Why: Static artifact reasoning does not evaluate an agent's ability to run and validate experiments
- **Claims affected**: C01
- **Adopted elements**: Paper-grounded research assessment concept

## RW10: ML-Gym (Nathani et al., 2025)
- **DOI**: arXiv (ML-Gym)
- **Type**: baseline
- **Delta**:
  - What changed: EXP-Bench uses real peer-reviewed papers as task sources and applies conjunctive multi-phase evaluation; ML-Gym uses simplified evaluation metrics
  - Why: Simplified metrics do not capture end-to-end experiment correctness
- **Claims affected**: C01, C03
- **Adopted elements**: ML research agent evaluation framing

## RW11: Scicode (Tian et al., 2024)
- **DOI**: arXiv (Scicode)
- **Type**: baseline
- **Delta**:
  - What changed: EXP-Bench targets AI research experiments with full execution pipelines, not code snippet generation for natural science tasks
  - Why: Code snippet generation is a sub-task of experimentation; EXP-Bench requires complete runnable experiment chains
- **Claims affected**: C01, C04
- **Adopted elements**: Research coding benchmark design

## RW12: The AI Scientist (Lu et al., 2024)
- **DOI**: arXiv:2408.06292
- **Type**: baseline
- **Delta**:
  - What changed: EXP-Bench provides structured, verifiable evaluation with ground truth from real papers; The AI Scientist has limited automated evaluation and focuses on commonsense domains
  - Why: Without verifiable ground truth tied to published results, automated evaluation of research quality is unreliable
- **Claims affected**: C01, C02
- **Adopted elements**: Multi-agent research automation concept; end-to-end research lifecycle framing
