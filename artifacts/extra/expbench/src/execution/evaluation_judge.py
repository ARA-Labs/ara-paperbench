"""
EXP-Bench Multi-Metric Evaluation Judge.

Implements the four-component evaluation framework:
  1. Monitor: integrity check for disallowed behaviors
  2. Design/Conclusion Judge: LLM-based scoring of D and C metrics
  3. Implementation Judge: LLM-based scoring of I metric via git diff comparison
  4. Code Execution Validator: binary executability check (E metric)

Novel contribution: conjunctive scoring (I·E, C·D, All✓, All·E✓) that
substantially reduces metric variance and reveals true end-to-end capability.
"""

from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class MonitorResult:
    paper_access: bool
    git_operations: bool
    faked_or_nonexperimental_data: bool
    reason: str

    @property
    def passed(self) -> bool:
        return not (self.paper_access or self.git_operations or self.faked_or_nonexperimental_data)


@dataclass
class DesignConclusionResult:
    design_score: int               # 0–100 (proportion of design criteria met)
    design_explanation: str
    design_error_analysis: str
    conclusion_score: Literal["correct", "incorrect"]
    conclusion_explanation: str
    conclusion_error_analysis: str


@dataclass
class ImplementationResult:
    setup_score: int                # 0–100 (proportion of requirements satisfied)
    setup_explanation: str
    setup_error_analysis: str


@dataclass
class EvalResult:
    """Complete evaluation result for a single task-agent pair."""
    task_id: str
    monitor: MonitorResult
    design: Optional[DesignConclusionResult]    # None if monitor failed
    implementation: Optional[ImplementationResult]  # None if monitor failed
    executability: Optional[bool]               # None if not executed

    @property
    def D(self) -> float:
        """Design correctness score (0–100)."""
        return self.design.design_score if self.design else 0.0

    @property
    def I(self) -> float:
        """Implementation correctness score (0–100)."""
        return self.implementation.setup_score if self.implementation else 0.0

    @property
    def C(self) -> bool:
        """Conclusion correctness (True/False)."""
        return self.design.conclusion_score == "correct" if self.design else False

    @property
    def E(self) -> bool:
        """Executability (True/False)."""
        return bool(self.executability)

    # ─── Conjunctive Metrics ────────────────────────────────────────────────

    @property
    def IE(self) -> bool:
        """I·E: implementation correct AND executable."""
        return self.I > 0 and self.E

    @property
    def all_correct(self) -> bool:
        """All✓: D > 0 AND I > 0 AND C."""
        return self.D > 0 and self.I > 0 and self.C

    @property
    def all_correct_executable(self) -> bool:
        """All·E✓: D > 0 AND I > 0 AND C AND E."""
        return self.D > 0 and self.I > 0 and self.C and self.E

    @property
    def CD(self) -> bool:
        """C·D: conclusion correct AND design score > 0."""
        return self.C and self.D > 0


def run_monitor(
    agent_logs: str,
    llm_client,
    model: str = "o3-mini-2025-01-01-preview",
    max_chunk_tokens: int = 100_000,
) -> MonitorResult:
    """
    Integrity check: detect disallowed behaviors in agent logs.

    Checks for:
      (1) Direct access to the research paper PDF
      (2) Git operations (checkout, branch switching, history access)
      (3) Faked, hardcoded, or mock data used as experimental results

    Args:
        agent_logs: full agent execution log (may be long; chunked internally)
        llm_client: initialized LLM API client
        model: judge model name
        max_chunk_tokens: maximum tokens per LLM call

    Returns:
        MonitorResult with boolean flags and comprehensive reason string
    """
    chunks = _chunk_text(agent_logs, max_chunk_tokens)
    accumulated_result = MonitorResult(
        paper_access=False,
        git_operations=False,
        faked_or_nonexperimental_data=False,
        reason="",
    )

    for i, chunk in enumerate(chunks):
        prompt = _build_monitor_prompt(chunk, prior_context=accumulated_result.reason)
        response = llm_client.complete(model=model, prompt=prompt)
        chunk_result = _parse_monitor_response(response)
        accumulated_result = _merge_monitor_results(accumulated_result, chunk_result)

    return accumulated_result


def evaluate_design_and_conclusion(
    design_output: str,
    conclusion_output: str,
    design_ground_truth: dict,
    conclusion_ground_truth: str,
    llm_client,
    model: str = "o3-mini-2025-01-01-preview",
) -> DesignConclusionResult:
    """
    Score design correctness (D) and conclusion correctness (C).

    Design evaluation: count proportion of ground-truth design items
    (independent variables, dependent variables, constants) correctly
    identified in agent output.

    Conclusion evaluation: semantic match between agent conclusion and
    ground-truth conclusion (binary: correct/incorrect).

    Args:
        design_output: agent's experimental design specification (free text)
        conclusion_output: agent's conclusion text
        design_ground_truth: dict with keys 'independent', 'dependent', 'constants'
        conclusion_ground_truth: expected conclusion string from paper
        llm_client: initialized LLM API client
        model: judge model name

    Returns:
        DesignConclusionResult with scores and error analyses
    """
    prompt = _build_design_conclusion_prompt(
        design_output=design_output,
        conclusion_output=conclusion_output,
        design_gt=design_ground_truth,
        conclusion_gt=conclusion_ground_truth,
    )
    response = llm_client.complete(model=model, prompt=prompt)
    return _parse_design_conclusion_response(response)


def evaluate_implementation(
    setup_output_diff: str,
    setup_ground_truth: list[str],
    setup_ground_truth_scripts: dict[str, str],
    llm_client,
    model: str = "o3-mini-2025-01-01-preview",
    max_chunk_tokens: int = 100_000,
) -> ImplementationResult:
    """
    Score implementation correctness (I) by comparing agent git diff to ground truth.

    Evaluates step-by-step whether each ground-truth requirement is satisfied
    in the agent's diff. Uses reference scripts as code-level guidance (not
    requiring exact match — variations in filenames/function names are acceptable
    if the requirement's intent is fulfilled).

    Args:
        setup_output_diff: agent-generated git diff (patch format)
        setup_ground_truth: list of step-by-step NL implementation requirements
        setup_ground_truth_scripts: dict mapping script paths to source code
        llm_client: initialized LLM API client
        model: judge model name
        max_chunk_tokens: for chunked processing of long diffs

    Returns:
        ImplementationResult with setup_score (0–100) and error analysis
    """
    chunks = _chunk_text(setup_output_diff, max_chunk_tokens)
    accumulated_score = 0
    accumulated_explanation = ""
    accumulated_errors = ""

    for i, chunk in enumerate(chunks):
        prompt = _build_implementation_prompt(
            setup_output=chunk,
            setup_gt=setup_ground_truth,
            setup_scripts=setup_ground_truth_scripts,
            prior_context=accumulated_explanation,
        )
        response = llm_client.complete(model=model, prompt=prompt)
        chunk_result = _parse_implementation_response(response)
        accumulated_score, accumulated_explanation, accumulated_errors = _merge_implementation(
            prior=(accumulated_score, accumulated_explanation, accumulated_errors),
            new=chunk_result,
        )

    return ImplementationResult(
        setup_score=accumulated_score,
        setup_explanation=accumulated_explanation,
        setup_error_analysis=accumulated_errors,
    )


def run_code_execution_validator(
    repo_path: str,
    agent_diff: str,
    expected_outputs: Optional[dict] = None,
) -> bool:
    """
    Binary executability check: apply agent diff and run in clean container.

    Args:
        repo_path: path to clean repository clone
        agent_diff: agent-generated git diff (patch format)
        expected_outputs: optional dict of expected output patterns for comparison

    Returns:
        True if code executes successfully (and matches expected outputs if provided),
        False otherwise.
    """
    # Apply diff to clean repo
    patched_repo = _apply_diff(repo_path, agent_diff)

    # Execute in containerized environment (Ubuntu 24.04, 4× A40)
    result = _execute_in_container(patched_repo)

    if not result["success"]:
        return False

    if expected_outputs:
        return _check_output_matches(result["output"], expected_outputs)

    return True


def compute_aggregate_scores(
    eval_results: list[EvalResult],
) -> dict[str, float]:
    """
    Compute aggregate benchmark scores across all tasks.

    Args:
        eval_results: list of EvalResult objects for all evaluated tasks

    Returns:
        dict with keys: 'D', 'I', 'C', 'E', 'IE', 'All', 'All_E'
        Values are percentages (0–100) averaged over all tasks.
    """
    n = len(eval_results)
    if n == 0:
        return {}

    return {
        "D":     sum(r.D for r in eval_results) / n,
        "I":     sum(r.I for r in eval_results) / n,
        "C":     100.0 * sum(r.C for r in eval_results) / n,
        "E":     100.0 * sum(r.E for r in eval_results) / n,
        "IE":    100.0 * sum(r.IE for r in eval_results) / n,
        "All":   100.0 * sum(r.all_correct for r in eval_results) / n,
        "All_E": 100.0 * sum(r.all_correct_executable for r in eval_results) / n,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Private helper stubs
# ─────────────────────────────────────────────────────────────────────────────

def _chunk_text(text: str, max_tokens: int) -> list[str]:
    """Split text into chunks of at most max_tokens tokens."""
    raise NotImplementedError

def _build_monitor_prompt(chunk: str, prior_context: str) -> str:
    """Construct monitor prompt from log chunk and prior evaluation context."""
    raise NotImplementedError

def _parse_monitor_response(response: str) -> MonitorResult:
    """Parse JSON monitor response into MonitorResult."""
    raise NotImplementedError

def _merge_monitor_results(a: MonitorResult, b: MonitorResult) -> MonitorResult:
    """Merge two MonitorResults (OR for booleans, concatenate reasons)."""
    raise NotImplementedError

def _build_design_conclusion_prompt(design_output, conclusion_output, design_gt, conclusion_gt) -> str:
    """Construct design/conclusion evaluation prompt."""
    raise NotImplementedError

def _parse_design_conclusion_response(response: str) -> DesignConclusionResult:
    """Parse JSON design/conclusion response."""
    raise NotImplementedError

def _build_implementation_prompt(setup_output, setup_gt, setup_scripts, prior_context) -> str:
    """Construct implementation evaluation prompt."""
    raise NotImplementedError

def _parse_implementation_response(response: str) -> ImplementationResult:
    """Parse JSON implementation evaluation response."""
    raise NotImplementedError

def _merge_implementation(prior: tuple, new: ImplementationResult) -> tuple:
    """Merge implementation evaluation across chunks."""
    raise NotImplementedError

def _apply_diff(repo_path: str, diff: str) -> str:
    """Apply git diff patch to repository; return path to patched repo."""
    raise NotImplementedError

def _execute_in_container(repo_path: str) -> dict:
    """Execute repository scripts in Docker container."""
    raise NotImplementedError

def _check_output_matches(actual: str, expected: dict) -> bool:
    """Check if actual output matches expected output patterns."""
    raise NotImplementedError
