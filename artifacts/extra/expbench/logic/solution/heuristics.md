# Heuristics

## H01: Two-pass RAG for scattered experimental details
- **Rationale**: Academic papers present research findings non-linearly; key experimental details (e.g., dataset splits, hyperparameters, evaluation conditions) are scattered across body, appendix, and supplementary materials. A single-pass extraction misses cross-section dependencies.
- **Sensitivity**: high
- **Bounds**: First pass: retrieval over full paper for high-level takeaways. Second pass: subsection-level prompting conditioned on accumulated context and extracted tables/figures. Third pass: full-paper re-query targeting appendices for missed setup details.
- **Code ref**: [src/execution/curation_pipeline.py]
- **Source**: §3.2, Stage 2.1

## H02: Iterative implementation refinement with execution feedback
- **Rationale**: The implementation extraction agent cannot know a priori if its candidate script chain is correct. Execution-based validation in a containerized environment provides ground truth feedback; failed executions trigger agent refinement iterations.
- **Sensitivity**: high
- **Bounds**: Agent iterates until a working solution is found or a fixed iteration limit is reached; final validated script chain is then parsed via AST.
- **Code ref**: [src/execution/curation_pipeline.py]
- **Source**: §3.2, Stage 2.2

## H03: Chunked LLM judge processing for long diffs/logs
- **Rationale**: Agent-generated git diffs and execution logs can exceed o3-mini's context window. Segmenting inputs into chunks and carrying over evaluation results and context between chunks prevents information loss.
- **Sensitivity**: medium
- **Bounds**: Chunk size determined by model's maximum context length. Evaluation results from chunk $k$ are passed as context to chunk $k+1$; this introduces sequential dependence and potential inconsistency at boundaries.
- **Code ref**: [src/execution/evaluation_judge.py]
- **Source**: §4.1, Evaluation Judge Implementation Details

## H04: Conjunctive scoring to reduce metric instability
- **Rationale**: Individual metrics C (conclusion) and E (execution) exhibit high variance — agents can produce plausible-sounding conclusions without valid experiments (inflating C), or incorrect mock implementations may still execute (inflating E). Conjunctive forms C·D and I·E mitigate these failure modes.
- **Sensitivity**: medium
- **Bounds**: C·D requires both conclusion correctness AND valid design (filters unfounded conclusions); I·E requires both implementation correctness AND executability (filters mock executions). These conjunctions reduce over-crediting and annotation leniency sensitivity.
- **Code ref**: [src/execution/evaluation_judge.py]
- **Source**: §4.2, Metric Stability Analysis; Figure 5

## H05: Source filtering via citation count + GitHub repository activity
- **Rationale**: High citation count and GitHub stars/forks serve as proxies for paper quality, reproducibility, and community adoption. Filtering on both signals reduces the probability of including papers with unreliable or unmaintainable codebases.
- **Sensitivity**: low
- **Bounds**: Exact thresholds not specified in paper; applied as initial filter to generate candidate set before more expensive extraction steps. The 51 selected papers span citation ranges from ~1287 (Causal-learn) to several thousand.
- **Code ref**: [src/execution/curation_pipeline.py]
- **Source**: §3.2, Stage 1
