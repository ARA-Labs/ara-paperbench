"""
Data pipeline for constructing DPT, DR, D̂PT and collecting ground-truth forgetting labels.

Paper: "What Will My Model Forget? Forecasting Forgotten Examples in Language Model Refinement"
Authors: Xisen Jin, Xiang Ren (ICML 2024, arXiv:2402.01865)

Dataset construction details (§4.1, Appendix B):
- DPT: 36 tasks × 100 examples from P3 train split
- DR for BART0Large: P3 test split (8 tasks)
- DR for FLAN-T5: MMLU validation split (57 tasks)
- DR split: 60% DTrain_R / 40% DTest_R (random)
- P3-TestID: SuperGlue-Cb, SuperGlue-RTE, SuperGLUE-wsc.fixed, SuperGlue-Copa, SuperGlue-wic
- P3-TestOOD: storycloze, hellaswag, anli, winograde-xl
"""

from typing import List, Dict, Tuple, Any, Optional
import random
import copy
import torch
from torch import Tensor


# ─── P3 Task Lists ─────────────────────────────────────────────────────────────

# 36 tasks used for DPT (P3 train split) — from rubric Dataset Acquisition §1
DPT_TASKS = [
    "glue-mrpc", "glue-qqp", "paws_x-en", "kilt_tasks-hotpotqa", "wiki_qa",
    "adversarial_qa-dbert", "adversarial_qa-dbidaf", "adversarial_qa-droberta",
    "duorc-SelfRC", "duorc-ParaphraseRC", "ropes", "quoref",
    "cos_e-v1.11", "cosmos_qa", "dream", "qasc", "quail", "quartz", "sciq",
    "social_i_qa", "wiki_hop-original", "wiqa",
    "amazon_polarity", "app_reviews", "imdb", "rotten_tomatoes", "yelp_review_full",
    "common_gen", "wiki_bio", "cnn_dailymail-3.0.0", "gigaword", "multi_news",
    "samsum", "xsum", "ag_news", "dbpedia_14",
]

# P3 test tasks for BART0Large DR — from rubric Dataset Acquisition §2
# Source: https://github.com/INK-USC/ReCross/blob/main/data/
P3_TEST_TASKS = [
    "super_glue-wsc.fixed", "winogrande-winogrande_xl", "super_glue-cb",
    "super_glue-rte", "anli", "super_glue-copa", "hellaswag", "super_glue-wic",
]

# OOD evaluation splits (Appendix B)
P3_TEST_ID_TASKS = [
    "super_glue-cb", "super_glue-rte", "super_glue-wsc.fixed",
    "super_glue-copa", "super_glue-wic",
]
P3_TEST_OOD_TASKS = [
    "storycloze", "hellaswag", "anli", "winogrande-winogrande_xl",
]

# MMLU validation split for FLAN-T5 DR (57 tasks)
# Source: https://people.eecs.berkeley.edu/~hendrycks/data.tar


def build_dpt(
    p3_train_loader,            # Dataset loader for P3 train split
    tasks: List[str] = DPT_TASKS,
    examples_per_task: int = 100,  # 100 examples per task (§4.1)
    seed: int = 42,
) -> List[Dict[str, Any]]:
    """
    Construct DPT: 36 P3 train tasks × 100 balanced examples/task.

    Args:
        p3_train_loader: Object with .load(task_name) -> List[{input, output}]
        tasks: List of 36 P3 task names
        examples_per_task: Number of examples to sample per task (default: 100)
        seed: Random seed for reproducibility
    Returns:
        dpt: List of (input, output, task) dicts, total length = len(tasks) × examples_per_task
    """
    random.seed(seed)
    dpt = []
    for task in tasks:
        task_examples = p3_train_loader.load(task)
        sampled = random.sample(task_examples, min(examples_per_task, len(task_examples)))
        for ex in sampled:
            dpt.append({"input": ex["input"], "output": ex["output"], "task": task})
    return dpt


def build_dr(
    dataset_loader,           # Dataset loader (P3 test or MMLU validation)
    model,                    # Base LM f0 for generating predictions
    tokenizer,
    tasks: Optional[List[str]] = None,
    split: str = "validation",  # "test" for P3, "validation" for MMLU
    train_ratio: float = 0.6,   # 60% train, 40% test split of DR
    seed: int = 42,
) -> Tuple[List[Dict], List[Dict]]:
    """
    Construct DR from mispredicted examples of the base model.
    Split into DTrain_R (60%) and DTest_R (40%).

    Args:
        dataset_loader: Data loader with .load(task, split) -> List[{input, output}]
        model: Base LM f0 to generate predictions
        tokenizer: Tokenizer for model
        tasks: Task list (P3_TEST_TASKS for BART0, MMLU tasks for FLAN-T5)
        split: Dataset split to use
        train_ratio: Fraction of DR for training the forecasting model (default: 0.6)
        seed: Random seed
    Returns:
        dr_train: Training split of mispredicted examples (60%)
        dr_test: Test split of mispredicted examples (40%)
    """
    model.eval()
    all_mispredicted = []
    if tasks is None:
        tasks = ["all"]

    for task in tasks:
        examples = dataset_loader.load(task, split)
        for ex in examples:
            pred = generate_prediction(model, tokenizer, ex["input"])
            # Exact Match grading
            if pred.strip() != ex["output"].strip():
                all_mispredicted.append({
                    "input": ex["input"],
                    "output": ex["output"],
                    "task": task,
                    "prediction": pred,
                })

    # Random 60/40 split
    random.seed(seed)
    random.shuffle(all_mispredicted)
    split_idx = int(len(all_mispredicted) * train_ratio)
    dr_train = all_mispredicted[:split_idx]
    dr_test = all_mispredicted[split_idx:]
    return dr_train, dr_test


def build_dpt_hat(
    model,
    tokenizer,
    dpt: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """
    Construct D̂PT: subset of DPT correctly predicted by base model f0 (§2).

    D̂PT = {⟨xj, yj⟩ ∈ DPT | f0(xj) = yj}  (Exact Match)

    Args:
        model: Base LM f0
        tokenizer: Tokenizer
        dpt: Full upstream pretraining dataset DPT
    Returns:
        dpt_hat: Correctly predicted subset
    """
    model.eval()
    dpt_hat = []
    for ex in dpt:
        pred = generate_prediction(model, tokenizer, ex["input"])
        if pred.strip() == ex["output"].strip():
            dpt_hat.append(ex)
    return dpt_hat


def generate_prediction(model, tokenizer, input_text: str, max_new_tokens: int = 50) -> str:
    """
    Generate model prediction for a single input using greedy decoding.
    Used for Exact Match evaluation.

    Args:
        model: Language model (BART0Large, FLAN-T5Large, or FLAN-T53B)
        tokenizer: Corresponding tokenizer
        input_text: Input string
        max_new_tokens: Maximum tokens to generate
    Returns:
        predicted: Decoded prediction string
    """
    inputs = tokenizer(
        input_text, return_tensors="pt", padding=True, truncation=True, max_length=512
    )
    inputs = {k: v.to(model.device) for k, v in inputs.items()}
    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            num_beams=1,  # greedy decoding
        )
    predicted = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return predicted


def compute_exact_match(prediction: str, reference: str) -> int:
    """
    Exact Match score between prediction and reference.
    Returns 1 if strings match exactly (case-sensitive, stripped), 0 otherwise.
    """
    return int(prediction.strip() == reference.strip())


def compute_em_score(
    model,
    tokenizer,
    dataset: List[Dict[str, Any]],
) -> float:
    """
    Compute Exact Match (EM) score of a model on a dataset.

    EM_D,f = |{⟨x,y⟩ ∈ D | f(x) = y}| / |D|

    Args:
        model: Language model
        tokenizer: Tokenizer
        dataset: List of {input, output} examples
    Returns:
        em_score: Fraction of correctly predicted examples
    """
    correct = 0
    for ex in dataset:
        pred = generate_prediction(model, tokenizer, ex["input"])
        correct += compute_exact_match(pred, ex["output"])
    return correct / len(dataset) if dataset else 0.0


def compute_em_drop_ratio(
    model_fi,
    model_f0,
    tokenizer,
    dpt: List[Dict[str, Any]],
) -> float:
    """
    Compute EM Drop Ratio on upstream pretraining data DPT.

    EM_Drop = (EM_DPT(fi) - EM_DPT(f0)) / EM_DPT(f0)

    Negative values indicate forgetting (EM decreased after update).

    Args:
        model_fi: Updated model after refinement
        model_f0: Original base model f0
        tokenizer: Tokenizer
        dpt: Upstream pretraining dataset DPT
    Returns:
        em_drop_ratio: Relative EM change (negative = forgetting)
    """
    em_fi = compute_em_score(model_fi, tokenizer, dpt)
    em_f0 = compute_em_score(model_f0, tokenizer, dpt)
    if em_f0 == 0.0:
        return 0.0
    return (em_fi - em_f0) / em_f0


def compute_edit_success_rate(
    model_fi,
    tokenizer,
    dr_test: List[Dict[str, Any]],
) -> float:
    """
    Compute Edit Success Rate (ESR) — fraction of mispredicted examples now
    correctly predicted after model refinement.

    ESR = |{⟨xi, yi⟩ ∈ DR | fi(xi) = yi}| / |DR|

    Args:
        model_fi: Updated model
        tokenizer: Tokenizer
        dr_test: Test set of originally mispredicted examples DTest_R
    Returns:
        esr: Edit success rate in [0, 1]
    """
    return compute_em_score(model_fi, tokenizer, dr_test)


def collect_ground_truth_forgetting(
    base_model,
    tokenizer,
    dr_train: List[Dict[str, Any]],
    dpt_hat: List[Dict[str, Any]],
    n_steps_per_example: int = 30,   # K gradient steps (LoRA/Full FT)
    learning_rate: float = 1e-4,     # LR for FLAN-T5 LoRA/Full FT
    fine_tuning_mode: str = "full",  # "head" | "lora" | "full"
    lora_config: Optional[Dict] = None,
) -> Dict[int, List[int]]:
    """
    Collect ground-truth binary forgetting labels zij for all (xi, xj) pairs.

    For each ⟨xi, yi⟩ ∈ DTrain_R:
        fi = update(f0; ⟨xi, yi⟩)  (K gradient steps)
        zij = 1 if fi(xj) ≠ yj else 0  for each ⟨xj, yj⟩ ∈ D̂PT

    Hyperparameters (§4.1):
    - LoRA/Full FT: 30 steps; LR=1e-5 (BART0) or 1e-4 (FLAN-T5)
    - Head only: 100 steps; LR=1e-3 (BART0) or 1e-4 (FLAN-T5)

    Args:
        base_model: Base LM f0
        tokenizer: Tokenizer
        dr_train: Training split of mispredicted examples
        dpt_hat: Correctly predicted upstream examples D̂PT
        n_steps_per_example: K gradient steps per online example
        learning_rate: Learning rate for fine-tuning
        fine_tuning_mode: "head" | "lora" | "full"
        lora_config: LoRA configuration dict if fine_tuning_mode=="lora"
    Returns:
        forgetting_labels: {i: [zij for each j in dpt_hat]} for each i in dr_train
    """
    import torch.optim as optim

    forgetting_labels: Dict[int, List[int]] = {}

    for i, xi_example in enumerate(dr_train):
        # Create fresh copy of f0 for each online example
        fi = copy.deepcopy(base_model)
        fi.train()

        # Configure optimizer based on fine-tuning mode
        if fine_tuning_mode == "head":
            # Only fine-tune LM head parameters
            params = [p for n, p in fi.named_parameters() if "lm_head" in n]
        elif fine_tuning_mode == "lora":
            # Only fine-tune LoRA parameters
            # Note: LoRA applied to query and value (not key) matrices in all self-attention layers
            params = [p for n, p in fi.named_parameters() if "lora_" in n]
        else:  # "full"
            params = list(fi.parameters())

        optimizer = optim.AdamW(params, lr=learning_rate)

        # K gradient steps on online example ⟨xi, yi⟩
        xi_inputs = tokenizer(
            xi_example["input"], return_tensors="pt",
            padding=True, truncation=True, max_length=512
        )
        yi_ids = tokenizer(
            xi_example["output"], return_tensors="pt",
            padding=True, truncation=True, max_length=64
        )["input_ids"]
        xi_inputs["labels"] = yi_ids
        xi_inputs = {k: v.to(base_model.device) for k, v in xi_inputs.items()}

        for _ in range(n_steps_per_example):
            optimizer.zero_grad()
            loss = fi(**xi_inputs).loss
            loss.backward()
            optimizer.step()

        # Evaluate fi on D̂PT to collect forgetting labels
        fi.eval()
        zij_list = []
        for xj_example in dpt_hat:
            pred = generate_prediction(fi, tokenizer, xj_example["input"])
            zij = int(pred.strip() != xj_example["output"].strip())  # 1 = forgotten
            zij_list.append(zij)
        forgetting_labels[i] = zij_list

    return forgetting_labels


def compute_f1_score(
    predicted: List[int],
    ground_truth: List[int],
) -> float:
    """
    Compute F1 score for binary forgetting prediction.
    Positive class (label=1) = forgotten example.

    Args:
        predicted: List of predicted binary labels ẑij
        ground_truth: List of ground-truth binary labels zij
    Returns:
        f1: F1 score (harmonic mean of precision and recall)
    """
    tp = sum(p == 1 and g == 1 for p, g in zip(predicted, ground_truth))
    fp = sum(p == 1 and g == 0 for p, g in zip(predicted, ground_truth))
    fn = sum(p == 0 and g == 1 for p, g in zip(predicted, ground_truth))
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)
