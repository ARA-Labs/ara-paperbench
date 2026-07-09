"""
Evaluation module: answer generation and grading for all three benchmarks.

Implements dataset-specific grading for AQuA-RAT, SVAMP, and StrategyQA.
A critical evaluation protocol:
  - For the top-prob (greedy) method: ONLY generations where an answer
    could be successfully extracted are counted when computing accuracy.
  - For AQuA-RAT: ONLY generations where an answer could be extracted
    are considered when computing metrics.
  - For ALL methods: unparseable responses are excluded from scoring.

This mirrors the parsing extraction approach from baseline self-consistency
(Wang et al., 2023). Source: paper §F (Sample analysis), §I.3.

Reference: Knappe et al., NeurIPS 2024, arXiv:2410.07839
"""

from __future__ import annotations
from typing import List, Optional, Dict, Tuple
import re


# ============================================================
# Answer Parsing
# ============================================================

def parse_answer(text: str) -> Optional[str]:
    """
    Extract the final answer from a chain-of-thought response.

    For SVAMP and AQuA-RAT: parses the string after "The answer is",
    removing surrounding whitespace, trailing full stops, and parentheses.

    For StrategyQA: parses the full string answer after the model
    generates "The answer is" (yes/no).

    Only responses where an answer can be extracted should be considered
    when computing accuracy metrics (paper §F).

    Args:
        text: Full generated text from the LLM.

    Returns:
        Extracted answer string (lowercased and stripped), or None if the
        trigger phrase "The answer is" is not found in the text.
    """
    trigger = "The answer is"
    if trigger not in text:
        return None
    answer = text.split(trigger)[-1]
    # Remove whitespace, trailing full stops, parentheses
    answer = answer.strip().rstrip(".").strip("()")
    # Take only first token/word for cleaner comparison
    answer = answer.split()[0] if answer.split() else ""
    return answer.lower() if answer else None


def parse_answer_aqua(text: str) -> Optional[str]:
    """
    Parse answer for AQuA-RAT (multiple choice: a/b/c/d/e).

    Only generations where an answer could be extracted should be
    considered when computing metrics for AQuA-RAT (paper §F).

    Returns the letter choice (a–e) if found after "The answer is".
    Returns None if unparseable (excluded from accuracy computation).
    """
    trigger = "The answer is"
    if trigger not in text:
        return None
    answer = text.split(trigger)[-1].strip().rstrip(".").strip("()").lower()
    # Accept single letter a-e
    if answer and answer[0] in 'abcde':
        return answer[0]
    return None


def parse_answer_svamp(text: str) -> Optional[str]:
    """
    Parse answer for SVAMP (numeric answer).

    Extracts the numeric value from after "The answer is".
    Returns None if unparseable (excluded from accuracy computation).
    """
    trigger = "The answer is"
    if trigger not in text:
        return None
    answer = text.split(trigger)[-1].strip().rstrip(".")
    # Extract first numeric token
    match = re.search(r'-?\d+\.?\d*', answer)
    return match.group(0) if match else None


def parse_answer_strategyqa(text: str) -> Optional[str]:
    """
    Parse answer for StrategyQA (yes/no).

    Parses the full string answer after "The answer is" as a yes/no
    decision. For commonsense reasoning tasks, the full string after the
    model generates "The answer is" is parsed as the final answer
    (paper Appendix K, footnote 6).

    Returns 'yes' or 'no', or None if unparseable.
    """
    trigger = "The answer is"
    if trigger not in text.lower():
        return None
    # Case-insensitive search
    lower_text = text.lower()
    answer = lower_text.split("the answer is")[-1].strip().rstrip(".")
    if answer.startswith("yes"):
        return "yes"
    elif answer.startswith("no"):
        return "no"
    return None


# ============================================================
# Grading Functions (per dataset)
# ============================================================

def grade_aqua_rat(predicted: Optional[str], gold: str) -> bool:
    """
    Grade a single AQuA-RAT prediction.

    AQuA-RAT is multiple choice (a/b/c/d/e). Comparison is
    case-insensitive. Returns False if prediction is None
    (unparseable, excluded from accuracy counting).

    Args:
        predicted: Extracted letter answer (a-e) or None.
        gold: Ground-truth letter answer (a-e).

    Returns:
        True if correct, False otherwise.
    """
    if predicted is None:
        return False
    return predicted.lower().strip() == gold.lower().strip()


def grade_svamp(predicted: Optional[str], gold: str) -> bool:
    """
    Grade a single SVAMP prediction.

    SVAMP requires exact numeric match. Handles integer vs float
    comparison (e.g., "6" == "6.0"). Returns False if prediction
    is None (excluded from accuracy counting).

    Args:
        predicted: Extracted numeric string or None.
        gold: Ground-truth numeric string.

    Returns:
        True if numeric values match, False otherwise.
    """
    if predicted is None:
        return False
    try:
        return float(predicted) == float(gold)
    except (ValueError, TypeError):
        return predicted.strip() == gold.strip()


def grade_strategyqa(predicted: Optional[str], gold: str) -> bool:
    """
    Grade a single StrategyQA prediction.

    StrategyQA is binary (yes/no). Comparison is case-insensitive.
    Returns False if prediction is None (excluded from accuracy counting).

    Args:
        predicted: 'yes' or 'no', or None.
        gold: Ground-truth 'yes' or 'no'.

    Returns:
        True if correct, False otherwise.
    """
    if predicted is None:
        return False
    return predicted.lower().strip() == gold.lower().strip()


# ============================================================
# Accuracy Computation
# ============================================================

def compute_accuracy(
    predictions: List[Optional[str]],
    gold_labels: List[str],
    dataset: str,
    exclude_unparseable: bool = True,
) -> float:
    """
    Compute accuracy over a list of predictions and gold labels.

    IMPORTANT: For the top-prob method and for AQuA-RAT, only generations
    where an answer could be extracted (predictions != None) should be
    considered when computing metrics. Set exclude_unparseable=True
    (default) to enforce this. Source: paper §F (Sample analysis).

    Args:
        predictions: List of predicted answer strings (None = unparseable).
        gold_labels: List of ground-truth answer strings.
        dataset: One of 'aqua_rat', 'svamp', 'strategyqa'.
        exclude_unparseable: If True, skip None predictions in denominator.
            If False, count None as incorrect (use for SC/CPW/SCW methods).

    Returns:
        Accuracy as a float in [0, 1].
    """
    grade_fn = {
        'aqua_rat': grade_aqua_rat,
        'svamp': grade_svamp,
        'strategyqa': grade_strategyqa,
    }.get(dataset)

    if grade_fn is None:
        raise ValueError(f"Unknown dataset: {dataset}")

    correct = 0
    total = 0
    for pred, gold in zip(predictions, gold_labels):
        if exclude_unparseable and pred is None:
            continue  # Skip unparseable responses in accuracy computation
        total += 1
        if grade_fn(pred, gold):
            correct += 1

    return correct / total if total > 0 else 0.0


def evaluate_dataset(
    method_predictions: Dict[str, List[Optional[str]]],
    gold_labels: List[str],
    dataset: str,
) -> Dict[str, float]:
    """
    Evaluate multiple methods on a dataset.

    For 'top_prob' method: only parseable answers are counted
    (exclude_unparseable=True), matching paper §F protocol.
    For all other methods (SC, CPW, SCW, outlier methods):
    all questions are counted in denominator (exclude_unparseable=False).

    Args:
        method_predictions: Dict mapping method name to list of predictions.
            Keys: 'top_prob', 'sc_baseline', 'cpw', 'scw',
                  'knn', 'isolation_forest', 'one_class_svm'
        gold_labels: Ground-truth answers.
        dataset: One of 'aqua_rat', 'svamp', 'strategyqa'.

    Returns:
        Dict mapping method name to accuracy percentage (0–100).
    """
    results = {}
    for method, preds in method_predictions.items():
        # For top_prob and AQuA-RAT: exclude unparseable from denominator
        exclude = (method == 'top_prob') or (dataset == 'aqua_rat')
        acc = compute_accuracy(preds, gold_labels, dataset,
                               exclude_unparseable=exclude)
        results[method] = acc * 100.0  # as percentage
    return results
