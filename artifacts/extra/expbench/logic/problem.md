# Problem Specification

## Observations

### O1: AI agents achieve only 0.5% complete end-to-end experiment success
- **Statement**: On 461 EXP-Bench tasks, the best-performing agent (OpenHands + o3-mini) achieves only 0.5% on All·E✓ (fully correct experiments including executability), despite reaching 20.3% on implementation correctness alone.
- **Evidence**: Table 1, §4.1
- **Implication**: Partial success on individual phases does not compound to end-to-end success; small per-phase failure rates multiply to near-zero overall.

### O2: Individual phase scores reach 20–35%, masking underlying brittleness
- **Statement**: Design (D) scores range from 6.4–20.6%, implementation (I) from 10.0–35.0%, and conclusion (C) from 0.0–14.9% across 7 evaluated agent configurations. These scores appear moderate in isolation.
- **Evidence**: Table 1, §4.1
- **Implication**: Evaluating agents on any single phase of experimentation severely overestimates their true capability.

### O3: Conjunctive metrics collapse scores from 20.6% to 0.2%
- **Statement**: Applying evaluation criteria progressively — Monitor (M) → Design (D) → Conclusion (C) → Implementation (I) → Execution (E) — reduces the average score from 20.6% (M only) to 3.7% (M·C·D) to 0.4% (M·C·D·I) to 0.2% (M·C·D·I·E).
- **Evidence**: Figure 6b, §4.2
- **Implication**: Each phase filters out a substantial fraction of agents, confirming that failure compounds across phases.

### O4: Missing implementation components is the dominant failure mode
- **Statement**: 39.71% of implementation failures are attributed to missing essential implementation components (e.g., missing retrieval strategies, regularization techniques, data preprocessing steps).
- **Evidence**: Table 2, §4.3
- **Implication**: Agents generate plausible but structurally incomplete implementations; they understand the high-level method but omit critical details.

### O5: Execution failures are driven by environment misconfiguration (29.38%) and script errors (23.84%)
- **Statement**: Among execution phase failures, 29.38% are environment or dependency configuration errors and 23.84% are script-level errors such as missing checkpoints or unrecognized model names.
- **Evidence**: Table 2, §4.3
- **Implication**: Even when implementation intent is correct, failures in environment reproducibility prevent successful execution.

### O6: Existing benchmarks do not evaluate end-to-end AI experimentation at scale
- **Statement**: Prior benchmarks either target sub-components (MLE-Bench: Kaggle tasks; RE-Bench: 7 hand-curated tasks; PaperBench: documented script execution), evaluate static artifacts (AAAR, Lab-Bench), or omit actual execution (ScienceAgentBench, BLADE).
- **Evidence**: §2 (Related Work), §3 introduction
- **Implication**: No existing benchmark captures the full experimentation pipeline — hypothesis → design → implementation → execution → conclusion — at scale, with verifiable ground truth.

## Gaps

### G1: No benchmark evaluates complete AI research experimentation end-to-end
- **Statement**: No prior work evaluates agents on the full cycle of research experimentation (design, implementation, execution, and conclusion derivation) using real, peer-reviewed AI papers as ground truth.
- **Caused by**: O6
- **Existing attempts**: MLE-Bench, RE-Bench, PaperBench, ScienceAgentBench
- **Why they fail**: Either scope is too narrow (single phase), scale is too small (7 tasks), or evaluation relies on pre-written scripts rather than requiring agents to generate implementations.

### G2: Partial-phase evaluation metrics overestimate agent capability
- **Statement**: Evaluating agents on design, implementation, or conclusion separately inflates apparent performance and fails to surface end-to-end brittleness.
- **Caused by**: O1, O2, O3
- **Existing attempts**: Individual metric scoring in MLE-Bench, DSBench, ML-Agent-Bench
- **Why they fail**: They credit partial solutions at individual stages without requiring all phases to succeed jointly.

### G3: High-fidelity AI research task curation is not scalable manually
- **Statement**: Academic papers present polished narratives with fragmented experimental details; manual extraction of complete, structured tasks with verified implementations is labor-intensive.
- **Caused by**: Nature of academic writing; details scattered across paper body, appendix, supplementary, and codebases
- **Existing attempts**: RE-Bench (7 hand-curated tasks), Curie
- **Why they fail**: Manual curation cannot scale to hundreds of tasks without unsustainable human effort.

## Key Insight

- **Insight**: By coupling multi-modal extraction from papers with execution-based validation against existing open-source codebases, it is possible to semi-automatically construct large-scale, high-fidelity research task benchmarks — and conjunctive evaluation metrics across phases are necessary to accurately measure end-to-end agent capability.
- **Derived from**: O1, O2, O3, O6
- **Enables**: A scalable pipeline (EXP-Bench) that produces 461 verified tasks from 51 papers, and a multi-phase conjunctive evaluation framework that exposes true agent performance gaps.

## Assumptions

- A1: Peer-reviewed, open-source AI papers (NeurIPS, ICLR) with high citation counts and GitHub stars represent authentic, reproducible research experiments.
- A2: An agent that correctly solves all four phases (design, implementation, execution, conclusion) for a task is a meaningful proxy for autonomous AI research capability.
- A3: LLM-as-a-judge (using o3-mini) provides sufficiently reliable evaluation for design, implementation, and conclusion correctness to serve as ground truth comparison.
- A4: Masking specific source files prevents agents from shortcutting to ground-truth solutions without solving the research task.
