# Constraints

## Boundary Conditions

### BC1: Source paper requirements
- EXP-Bench tasks require papers with **publicly available, runnable codebases** (GitHub repositories). Papers without code or with private datasets cannot be processed by the curation pipeline.
- Papers must have **sufficient experimental detail** in evaluation sections; purely theoretical papers or those with only conceptual experiments are out of scope.
- Currently limited to **NeurIPS 2024 and ICLR 2024** papers; generalization to other venues or years requires re-running the curation pipeline.

### BC2: Task scope limitations
- EXP-Bench evaluates the **experimentation procedure only** (design → implementation → execution → conclusion). It does not cover: literature review, open-ended research ideation, gap identification, or the iterative, unpredictable path of real-world discovery.
- Each task is grounded in an **already-completed** experiment from a published paper; the benchmark tests replication and extension, not open-ended hypothesis generation.

### BC3: Agent execution constraints
- **Soft timeout**: 40 minutes per task; agents may occasionally exceed this limit.
- **Hardware**: 4× NVIDIA A40 GPUs per agent run; tasks requiring more specialized hardware (e.g., 50× A800 GPUs for Bag of Tricks jailbreak paper) may not be faithfully executable.
- **Masking**: Agents cannot access the research paper PDF directly; they must reconstruct experimental procedures from task description and repository context only.

### BC4: Evaluation constraints
- **Execution subset**: Due to computational cost, execution validation (metric E) is run only on a **subset** of traces — those that pass the monitor check. Results may not be representative of all tasks.
- **LLM judge limitations**: o3-mini has a finite context window; long diffs or logs are chunked iteratively, which may introduce inconsistencies at chunk boundaries.
- **Monitor false positives/negatives**: The monitor may incorrectly flag legitimate behaviors (e.g., accessing paper-related text files in the repository) or miss sophisticated shortcutting behaviors.

### BC5: Curation pipeline limitations
- **Multi-pass extraction** can miss experimental details that are deeply implicit or require expert domain knowledge to interpret.
- **AST tracing** for implementation requirements assumes code follows conventional Python/script patterns; non-standard codebases may produce incomplete requirement lists.
- **Execution-based validation** validates that the ground-truth scripts run in a clean container but cannot guarantee they reproduce exact paper results (minor numerical differences from hardware/seed variation are possible).

## Known Limitations (as stated by authors)

1. Does not evaluate the broader AI research lifecycle (literature review, ideation, iterative discovery).
2. Task structures may not capture the full complexity and unpredictability of real-world AI research.
3. LLM-based categorization of failure types (Table 2, Table 8) may have inter-category overlap.
4. Cost reporting covers only backbone LLM token usage, excluding agent-internal API calls and GPU compute costs.
5. IA models often consume the full 40-minute timeout, potentially masking early failures with long runs.
