"""
Evaluation utilities for forecasting forgetting and model refinement.

Paper: "What Will My Model Forget? Forecasting Forgotten Examples in Language Model Refinement"
Authors: Xisen Jin, Xiang Ren (ICML 2024, arXiv:2402.01865)

Implements evaluation for:
- Table 1: F1 of forecasting methods across 7 model/tuning configurations
- Table 2: In-domain vs OOD generalization of forecasting (BART0)
- Table 3: Sequential model refinement (Edit Success Rate + EM Drop)
- Table 4: Single error fixing (EM Drop)
- Figure 3: Continual refinement F1/Precision/Recall over time
"""

from typing import List, Dict, Tuple, Callable, Any
import torch
import numpy as np


def evaluate_forecasting_table1(
    forecasters: Dict[str, Any],          # {name: forecasting_model}
    dr_test: List[Dict],                   # DTest_R: test online examples
    dpt_hat: List[Dict],                   # D̂PT: filtered upstream examples
    forgetting_labels_test: Dict[int, List[int]],  # Ground-truth zij^test for each i
) -> Dict[str, float]:
    """
    Evaluate all forecasting methods for Table 1.

    For each method m and each (xi, xj) pair:
        ẑij = m(xi, xj)
        Compute F1 over all pairs

    Args:
        forecasters: Dict mapping method name to callable g(xi, xj) -> {0,1}
        dr_test: Test mispredicted examples DTest_R
        dpt_hat: Filtered upstream examples D̂PT
        forgetting_labels_test: Ground-truth binary labels for each test pair
    Returns:
        f1_scores: {method_name: F1}
    """
    f1_scores = {}
    for method_name, forecaster in forecasters.items():
        all_pred = []
        all_true = []
        for i, xi_example in enumerate(dr_test):
            true_labels = forgetting_labels_test[i]
            for j, xj_example in enumerate(dpt_hat):
                pred = forecaster.predict(xi_example, xj_example)
                all_pred.append(pred)
                all_true.append(true_labels[j])
        from src.execution.data_pipeline import compute_f1_score
        f1_scores[method_name] = compute_f1_score(all_pred, all_true) * 100  # as percentage
    return f1_scores


def evaluate_forecasting_ood(
    forecasters: Dict[str, Any],
    dr_id: List[Dict],                       # DTrain_R from P3-TestID tasks
    dr_ood: List[Dict],                      # DTest_R from P3-TestOOD tasks
    dpt_hat: List[Dict],
    forgetting_labels_id: Dict[int, List[int]],
    forgetting_labels_ood: Dict[int, List[int]],
) -> Dict[str, Dict[str, float]]:
    """
    Evaluate in-domain and out-of-domain F1 for Table 2 (BART0 Full FT).

    P3-TestID: super_glue-cb, super_glue-rte, super_glue-wsc.fixed,
               super_glue-copa, super_glue-wic
    P3-TestOOD: storycloze, hellaswag, anli, winogrande-winogrande_xl

    Returns:
        results: {method: {"ID": f1, "OOD": f1}}
    """
    results = {}
    for method_name, forecaster in forecasters.items():
        id_pred, id_true = _collect_pairs(forecaster, dr_id, dpt_hat, forgetting_labels_id)
        ood_pred, ood_true = _collect_pairs(forecaster, dr_ood, dpt_hat, forgetting_labels_ood)
        from src.execution.data_pipeline import compute_f1_score
        results[method_name] = {
            "ID": compute_f1_score(id_pred, id_true) * 100,
            "OOD": compute_f1_score(ood_pred, ood_true) * 100,
        }
    return results


def evaluate_continual_refinement_stream(
    forecasters: Dict[str, Any],
    dr_test_stream: List[List[Dict]],        # DTest_R divided into time-step batches (1/8 each)
    dpt_hat: List[Dict],
    forgetting_labels_stream: List[Dict[int, List[int]]],  # Ground-truth for each time step
) -> Dict[str, Dict[str, List[float]]]:
    """
    Compute running average F1, Precision, Recall over continual refinement stream (Figure 3).

    At each time step t:
        - Compute F1_t, Precision_t, Recall_t for current batch
        - Compute running average: (1/t) * sum(metric_1..t)

    Args:
        dr_test_stream: List of time-step batches; each batch = 1/8 of DTest_R
        forgetting_labels_stream: Ground-truth labels for each time step
    Returns:
        metrics: {method: {"f1": [f1_t, ...], "precision": [...], "recall": [...]}}
    """
    metrics = {m: {"f1": [], "precision": [], "recall": []} for m in forecasters}

    for method_name, forecaster in forecasters.items():
        cumulative_f1 = []
        cumulative_precision = []
        cumulative_recall = []

        running_f1_sum = 0.0
        running_prec_sum = 0.0
        running_rec_sum = 0.0

        for t, (batch, labels_t) in enumerate(zip(dr_test_stream, forgetting_labels_stream), 1):
            batch_pred, batch_true = _collect_pairs(forecaster, batch, dpt_hat, labels_t)
            f1_t, prec_t, rec_t = _compute_f1_prec_rec(batch_pred, batch_true)

            running_f1_sum += f1_t
            running_prec_sum += prec_t
            running_rec_sum += rec_t

            # Running average up to time step t
            cumulative_f1.append(running_f1_sum / t)
            cumulative_precision.append(running_prec_sum / t)
            cumulative_recall.append(running_rec_sum / t)

        metrics[method_name]["f1"] = cumulative_f1
        metrics[method_name]["precision"] = cumulative_precision
        metrics[method_name]["recall"] = cumulative_recall

    return metrics


def _collect_pairs(
    forecaster,
    dr: List[Dict],
    dpt_hat: List[Dict],
    forgetting_labels: Dict[int, List[int]],
) -> Tuple[List[int], List[int]]:
    """Helper: collect all (predicted, ground_truth) pairs for a forecaster."""
    all_pred, all_true = [], []
    for i, xi in enumerate(dr):
        for j, xj in enumerate(dpt_hat):
            pred = forecaster.predict(xi, xj)
            all_pred.append(pred)
            all_true.append(forgetting_labels[i][j])
    return all_pred, all_true


def _compute_f1_prec_rec(
    predicted: List[int],
    ground_truth: List[int],
) -> Tuple[float, float, float]:
    """Compute F1, Precision, Recall for binary prediction."""
    tp = sum(p == 1 and g == 1 for p, g in zip(predicted, ground_truth))
    fp = sum(p == 1 and g == 0 for p, g in zip(predicted, ground_truth))
    fn = sum(p == 0 and g == 1 for p, g in zip(predicted, ground_truth))
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    return f1, precision, recall
