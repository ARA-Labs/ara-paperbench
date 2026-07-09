"""
EXP-Bench Semi-Automated Dataset Curation Pipeline.

Implements the three-stage pipeline that converts research papers and their
associated codebases into verified EXP-Bench benchmark tasks.

Novel contributions:
  - Multi-pass RAG extraction for scattered experimental details
  - Execution-based validation with iterative refinement
  - AST tracing for step-by-step implementation requirement extraction
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ResearchTask:
    """Structured representation of an EXP-Bench task."""
    research_question: str          # Q: specific goal from source paper
    high_level_method: str          # M: description of experimental approach
    design_ground_truth: dict       # D_gt: {independent, dependent, constants}
    conclusion_ground_truth: str    # C_gt: expected conclusion text
    implementation_requirements: list[str]  # Δ_gt: step-by-step NL requirements
    masked_files: list[str]         # F_mask: files removed from agent repo
    source_paper: str               # citation / paper title
    source_section: str             # paper section origin
    additional_context: dict = field(default_factory=dict)  # hyperparams, etc.


@dataclass
class CandidateImplementation:
    """Output of the implementation extraction agent."""
    script_list: list[str]          # ordered list of scripts to run
    usage_instructions: str         # high-level instructions (natural language)
    is_executable: bool = False     # set after container validation


def stage1_filter_paper(
    paper_metadata: dict,
    citation_threshold: int,
    stars_threshold: int,
) -> bool:
    """
    Stage 1: Filter papers by citation count and repository activity.

    Args:
        paper_metadata: dict with keys 'citations', 'github_stars', 'github_forks',
                        'venue' (e.g., 'NeurIPS2024'), 'has_open_source_code' (bool)
        citation_threshold: minimum citation count for inclusion
        stars_threshold: minimum GitHub stars for inclusion

    Returns:
        True if paper passes all filters, False otherwise
    """
    if not paper_metadata.get("has_open_source_code", False):
        return False
    if paper_metadata.get("citations", 0) < citation_threshold:
        return False
    if paper_metadata.get("github_stars", 0) < stars_threshold:
        return False
    if paper_metadata.get("venue") not in {"NeurIPS2024", "ICLR2024"}:
        return False
    return True


def stage2_1_extract_research_tasks(
    paper_pdf_path: str,
    llm_client,
    model: str = "o3-mini-2025-01-01-preview",
) -> list[dict]:
    """
    Stage 2.1: Multi-modal extraction of research tasks from paper PDF.

    Uses a three-pass approach:
      Pass 1: RAG querying for high-level research takeaways
      Pass 2: Subsection-level semantic classification and task extraction
      Pass 3: Full-paper re-querying to recover missed setup details

    Args:
        paper_pdf_path: path to the research paper PDF
        llm_client: initialized LLM API client (e.g., OpenAI)
        model: LLM model name for extraction

    Returns:
        List of raw task dicts with keys:
          'question', 'method', 'design_gt', 'conclusion_gt', 'context'
    """
    # Step 1: Index PDF (OCR + multimodal extraction of tables/figures/headers)
    indexed_pdf = _index_pdf_multimodal(paper_pdf_path)

    # Step 2, Pass 1: High-level RAG for research takeaways
    takeaways = _rag_query_high_level(indexed_pdf, llm_client, model)

    # Step 3, Pass 2: Subsection-level semantic extraction
    raw_tasks = []
    context_store = {}
    evaluation_sections = _get_evaluation_sections(indexed_pdf)

    for section in evaluation_sections:
        section_label = _classify_section(
            section, llm_client, model,
            classes=["implementation_context", "research_question"]
        )
        if section_label == "implementation_context":
            context_store.update(_extract_context(section))
        else:
            task = _extract_task_from_section(
                section,
                context=context_store,
                tables=indexed_pdf["tables"],
                figures=indexed_pdf["figures"],
                llm_client=llm_client,
                model=model,
            )
            if task:
                raw_tasks.append(task)

    # Step 4, Pass 3: Full-paper re-querying for missed details
    refined_tasks = []
    for task in raw_tasks:
        refined = _refine_task_full_paper(
            task, indexed_pdf, llm_client, model
        )
        refined_tasks.append(refined)

    return refined_tasks


def stage2_2_extract_implementation(
    task: dict,
    repo_path: str,
    llm_client,
    model: str = "claude-3-7-sonnet-20250219-v1:0",
    max_iterations: int = 5,
) -> CandidateImplementation:
    """
    Stage 2.2: Tool-augmented agent searches codebase for task implementation.

    The agent has access to: PDF reader, terminal (for codebase exploration),
    and web browser. It performs goal-conditioned search over the repository.
    Failed executions trigger iterative refinement.

    Args:
        task: raw task dict from stage2_1 (contains Q, M, C_gt)
        repo_path: local path to cloned repository
        llm_client: initialized LLM API client
        model: extraction model (claude-3-7-sonnet recommended for code understanding)
        max_iterations: maximum refinement attempts

    Returns:
        CandidateImplementation with validated scripts and AST-traced requirements
    """
    # Initialize tool-augmented agent
    agent = _init_tool_augmented_agent(
        tools=["pdf_reader", "terminal", "web_browser"],
        llm_client=llm_client,
        model=model,
    )

    candidate = None
    for iteration in range(max_iterations):
        # Agent explores repository to find implementation
        candidate = agent.search_codebase(
            repo_path=repo_path,
            goal={
                "question": task["question"],
                "method": task["method"],
                "expected_outcome": task["conclusion_gt"],
            },
        )

        # Execution-based validation in containerized environment
        is_executable = _execute_in_container(
            script_list=candidate.script_list,
            repo_path=repo_path,
        )

        if is_executable:
            candidate.is_executable = True
            break
        else:
            # Agent refines based on execution feedback
            agent.refine(candidate, feedback=_get_execution_error())

    if not (candidate and candidate.is_executable):
        raise RuntimeError(f"Failed to find executable implementation after {max_iterations} iterations")

    # AST tracing to extract step-by-step NL requirements
    implementation_requirements = _ast_trace_to_requirements(
        script_list=candidate.script_list,
        repo_path=repo_path,
    )
    candidate.implementation_requirements = implementation_requirements

    # Extract additional context (hyperparams from configs, README)
    additional_context = _extract_additional_context(repo_path)
    candidate.additional_context = additional_context

    return candidate


def stage3_verify_and_finalize(
    task: dict,
    candidate: CandidateImplementation,
    repo_path: str,
    expected_output_from_paper: Optional[str] = None,
) -> Optional[ResearchTask]:
    """
    Stage 3: Verify task execution and apply masking for dataset inclusion.

    Args:
        task: raw task dict from stage2_1
        candidate: validated implementation from stage2_2
        repo_path: local path to repository
        expected_output_from_paper: expected output string for comparison (optional)

    Returns:
        Finalized ResearchTask ready for dataset inclusion, or None if validation fails
    """
    # Execute in clean containerized environment
    execution_result = _execute_in_container(
        script_list=candidate.script_list,
        repo_path=repo_path,
        clean=True,
    )

    if not execution_result["success"]:
        return None  # Task returned to stage 2 for refinement

    # Optional: compare against expected outputs from paper
    if expected_output_from_paper:
        if not _outputs_match(execution_result["output"], expected_output_from_paper):
            return None

    # Apply file masking via scripted git operations
    masked_files = _apply_masking(repo_path, candidate.script_list)

    # Create finalized task
    finalized_task = ResearchTask(
        research_question=task["question"],
        high_level_method=task["method"],
        design_ground_truth=task["design_gt"],
        conclusion_ground_truth=task["conclusion_gt"],
        implementation_requirements=candidate.implementation_requirements,
        masked_files=masked_files,
        source_paper=task.get("source_paper", ""),
        source_section=task.get("source_section", ""),
        additional_context=candidate.additional_context,
    )

    return finalized_task


# ─────────────────────────────────────────────────────────────────────────────
# Private helper stubs (not implemented; signatures document interfaces)
# ─────────────────────────────────────────────────────────────────────────────

def _index_pdf_multimodal(pdf_path: str) -> dict:
    """OCR + multimodal extraction → {text, tables, figures, headers}."""
    raise NotImplementedError

def _rag_query_high_level(indexed_pdf: dict, llm_client, model: str) -> list[str]:
    """RAG query for high-level research takeaways across full paper."""
    raise NotImplementedError

def _get_evaluation_sections(indexed_pdf: dict) -> list[dict]:
    """Extract and return list of evaluation/experiment sections."""
    raise NotImplementedError

def _classify_section(section: dict, llm_client, model: str, classes: list[str]) -> str:
    """LLM classification of section type."""
    raise NotImplementedError

def _extract_context(section: dict) -> dict:
    """Extract implementation context key-value pairs from a section."""
    raise NotImplementedError

def _extract_task_from_section(section: dict, context: dict, tables, figures, llm_client, model: str) -> Optional[dict]:
    """Extract structured task from evaluation section conditioned on accumulated context."""
    raise NotImplementedError

def _refine_task_full_paper(task: dict, indexed_pdf: dict, llm_client, model: str) -> dict:
    """Full-paper re-querying to recover missed setup details from appendices."""
    raise NotImplementedError

def _init_tool_augmented_agent(tools: list[str], llm_client, model: str):
    """Initialize an agent with specified tool access."""
    raise NotImplementedError

def _execute_in_container(script_list: list[str], repo_path: str, clean: bool = False) -> dict:
    """Execute script chain in Docker container; return {'success': bool, 'output': str}."""
    raise NotImplementedError

def _get_execution_error() -> str:
    """Retrieve error output from the most recent container execution."""
    raise NotImplementedError

def _ast_trace_to_requirements(script_list: list[str], repo_path: str) -> list[str]:
    """Parse scripts via AST to extract step-by-step implementation requirements in NL."""
    raise NotImplementedError

def _extract_additional_context(repo_path: str) -> dict:
    """Extract hyperparameters and context from config files and README."""
    raise NotImplementedError

def _apply_masking(repo_path: str, scripts_to_mask: list[str]) -> list[str]:
    """Apply file masking via scripted git operations; return list of masked file paths."""
    raise NotImplementedError

def _outputs_match(actual: str, expected: str) -> bool:
    """Compare actual execution output against expected output from paper."""
    raise NotImplementedError
