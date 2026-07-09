# Concepts

## EXP-Bench Task
- **Notation**: $\mathcal{T} = (Q, M, R, G)$
- **Definition**: A structured research task instance consisting of: $Q$ = research question (natural language goal derived from a source paper experiment), $M$ = high-level method description, $R$ = code repository with masked files, and $G$ = ground truth solution comprising design variables, code diff, and conclusion string.
- **Boundary conditions**: Applies only to tasks grounded in published, peer-reviewed AI papers with open-source codebases. Does not apply to theoretical or survey papers without experimental components.
- **Related concepts**: Ground Truth Solution, Masked Repository, Experimental Design

## Ground Truth Solution
- **Notation**: $G = (D_{gt}, \Delta_{gt}, C_{gt})$
- **Definition**: The validated reference solution for an EXP-Bench task, comprising: $D_{gt}$ = experimental design specification (independent variables, dependent variables, constants), $\Delta_{gt}$ = required code modification expressed as a git diff against the starter repository, and $C_{gt}$ = conclusion string that directly answers the research question based on expected results.
- **Boundary conditions**: Ground truth is derived from the original paper and its open-source implementation; it is specific to the conditions described in the paper and may not generalize to other hardware or software versions.
- **Related concepts**: EXP-Bench Task, Conjunctive Evaluation Metrics

## Conjunctive Evaluation Metrics
- **Notation**: $\text{All}^\checkmark = D \wedge I \wedge C$; $\text{All·E}^\checkmark = D \wedge I \wedge C \wedge E$
- **Definition**: Evaluation scores computed as the logical conjunction (AND) of multiple per-phase scores. An agent receives credit for the conjunctive metric only if it satisfies all constituent criteria simultaneously. Individual metrics: $D$ = design correctness (proportion of design criteria met), $I$ = implementation correctness (proportion of implementation components satisfied), $C$ = conclusion correctness (binary: correct/incorrect), $E$ = executability (binary: code runs and produces expected outputs). Conjunctive forms include $I \cdot E$ (implementation correct AND executable), $C \cdot D$ (conclusion grounded in valid design), and $M \cdot C \cdot D \cdot I \cdot E$ (all criteria).
- **Boundary conditions**: Conjunctive metrics require that execution validation is performed; for tasks where execution is not run (e.g., monitor-failed traces), execution-dependent conjunctions are not computed.
- **Related concepts**: Monitor Check, Code Execution Validator, EXP-Bench Task

## Monitor Check (M)
- **Notation**: $M \in \{0, 1\}$
- **Definition**: An integrity check performed by an LLM-based monitor (o3-mini) that inspects agent logs to detect three disallowed behaviors: (1) accessing the research paper PDF directly, (2) performing git operations (checkout, branch switching), and (3) using fake, hardcoded, or placeholder data rather than generating results through real experimentation. A task passes the monitor ($M=1$) if none of these behaviors are detected.
- **Boundary conditions**: Applied before any other metric; tasks that fail the monitor are automatically excluded from execution-based evaluation. False positives may occur if the agent legitimately accesses paper-related files in the repository that are not the PDF itself.
- **Related concepts**: Conjunctive Evaluation Metrics, Code Execution Validator

## Code Execution Validator
- **Notation**: $E \in \{0, 1\}$
- **Definition**: A component of the evaluation judge that runs agent-generated code modifications in a clean, containerized environment (Ubuntu 24.04 Docker + 4× NVIDIA A40 GPU) and verifies whether the code is executable and produces outputs consistent with the expected results from the paper. $E=1$ if the code runs without fatal errors and produces outputs matching the ground truth.
- **Boundary conditions**: Applied only to a subset of traces that pass the monitor check; computationally expensive, so not applied to all 461 tasks for all agents. Results may vary with hardware and software environment differences.
- **Related concepts**: Monitor Check, Conjunctive Evaluation Metrics

## Semi-Automated Curation Pipeline
- **Notation**: $\mathcal{P}: (\text{PDF}, \text{repo}) \rightarrow \mathcal{T}$
- **Definition**: A three-stage pipeline that converts a research paper PDF and its associated GitHub repository into a verified EXP-Bench task. Stage 1: source selection and filtering (citation counts, GitHub stars/forks). Stage 2: experiment procedure extraction via multi-modal extraction (OCR + multimodal LLM) and implementation extraction (tool-augmented agent with PDF reading, terminal, web browsing). Stage 3: execution-based verification in clean containerized environments with lightweight human validation.
- **Boundary conditions**: Requires papers with publicly available, runnable codebases. Effectiveness degrades for papers with implicit experimental details or private datasets. Average cost: ~$60 USD per paper; manual validation time ~20 minutes per paper after pipeline finalization.
- **Related concepts**: Multi-Modal Extraction, Implementation Extraction Agent

## Multi-Modal Extraction
- **Notation**: Not formally defined; described as two-pass retrieval-augmented querying
- **Definition**: The process of indexing a paper PDF using OCR and multimodal techniques to capture tables, figures, and headers, followed by a two-pass extraction: (1) retrieval-augmented querying for high-level research takeaways, and (2) semantic extraction at the subsection level to classify passages as implementation context or candidate research questions. A final targeted re-querying of the full paper (including appendices) recovers missed setup constraints.
- **Boundary conditions**: Effective when research questions are explicitly stated in evaluation sections; may miss implicit questions or those requiring cross-section synthesis. Uses o3-mini-2025-01-01-preview for main task extraction and claude-3-7-sonnet-20250219-v1:0 for implementation extraction.
- **Related concepts**: Semi-Automated Curation Pipeline, Implementation Extraction Agent

## Masked Repository
- **Notation**: $R_{\text{masked}} = R \setminus F_{\text{mask}}$
- **Definition**: The agent's working directory containing the source repository with specific files ($F_{\text{mask}}$, e.g., key implementation scripts, README sections with solutions) removed or blanked via scripted git operations. Masking ensures agents cannot directly access ground-truth implementations and must reason from the task input. Repositories are cloned afresh per agent run.
- **Boundary conditions**: Masking applies only to files directly implementing the target experiment; other repository files remain accessible. Recursive traversal of submodules is included in masking.
- **Related concepts**: EXP-Bench Task, Semi-Automated Curation Pipeline

## Experimental Design Variables
- **Notation**: $D = (V_{\text{ind}}, V_{\text{dep}}, V_{\text{const}})$
- **Definition**: The structured specification of an experiment's variables: $V_{\text{ind}}$ = independent variables (factors manipulated by the experimenter), $V_{\text{dep}}$ = dependent variables (outcomes measured), $V_{\text{const}}$ = constants (factors held fixed across conditions). Design correctness score $D$ is the proportion of ground-truth design items correctly identified by the agent.
- **Boundary conditions**: Defined relative to the specific experiment in the source paper; the same factor may be independent in one experiment and constant in another. Agents frequently confuse independent and constant variables (16.05% misclassification rate).
- **Related concepts**: EXP-Bench Task, Ground Truth Solution

## IterativeAgent
- **Notation**: IA
- **Definition**: An agent configuration adapted from PaperBench (Starace et al., 2025), modified to reduce early task stopping by iterating on implementation until timeout or success. Used as a comparison baseline to OpenHands in EXP-Bench evaluations. Each agent run is given a maximum of 40 minutes and access to 4× NVIDIA A40 GPUs.
- **Boundary conditions**: IA models often consume the full allotted time (40 minutes), rarely stopping early, which distinguishes them from OpenHands models that frequently stop early with plausible-looking but incomplete outputs.
- **Related concepts**: OpenHands, Conjunctive Evaluation Metrics
