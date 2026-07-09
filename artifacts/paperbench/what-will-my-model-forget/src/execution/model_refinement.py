"""
Model refinement with forecasting-guided replay.

Implements:
1. Single-error fine-tuning with optional replay
2. Sequential error fixing over D^Test_R
3. Evaluation of Edit Success Rate and EM Drop Ratio

Replay uses distillation loss against base model f0 (DER, Buzzega et al. 2020a).
"""

from __future__ import annotations
import torch
import torch.nn.functional as F
from torch import Tensor
from typing import Optional, List, Tuple, Dict
import copy


def exact_match(prediction: str, ground_truth: str) -> bool:
    """Exact string match evaluation."""
    return prediction.strip() == ground_truth.strip()


def compute_em_score(
    model,
    dataset: List[Tuple[str, str]],  # list of (input, expected_output) pairs
    tokenizer,
    max_new_tokens: int = 50,
) -> float:
    """
    Compute Exact Match score of model on a dataset.
    
    Returns:
        EM score in [0, 1]
    """
    correct = 0
    total = len(dataset)
    model.eval()
    with torch.no_grad():
        for x, y in dataset:
            inputs = tokenizer(x, return_tensors="pt").to(model.device)
            outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)
            pred = tokenizer.decode(outputs[0], skip_special_tokens=True)
            if exact_match(pred, y):
                correct += 1
    return correct / total if total > 0 else 0.0


def compute_em_drop_ratio(
    em_after: float,
    em_base: float,
) -> float:
    """
    EM Drop Ratio = (EM_after - EM_base) / EM_base
    Positive = forgetting; negative = improvement.
    """
    if em_base == 0:
        return 0.0
    return (em_after - em_base) / em_base


def distillation_loss(
    student_logits: Tensor,  # [B, V] — logits from updated model fi
    teacher_logits: Tensor,  # [B, V] — logits from base model f0
    temperature: float = 1.0,
) -> Tensor:
    """
    Knowledge distillation loss: KL divergence from teacher to student.
    Used as replay loss against base model f0 (DER approach, Buzzega et al. 2020a).
    """
    teacher_probs = F.softmax(teacher_logits / temperature, dim=-1)
    student_log_probs = F.log_softmax(student_logits / temperature, dim=-1)
    return F.kl_div(student_log_probs, teacher_probs, reduction='batchmean')


def fine_tune_single_example(
    model,
    base_model,              # f0: frozen base model for distillation
    example_input_ids: Tensor,    # [1, L_in] tokenized input xi
    example_labels: Tensor,       # [1, T] tokenized output yi
    replay_examples: Optional[List[Tuple[Tensor, Tensor]]] = None,
    # List of (input_ids, labels) for replay examples from D̂PT
    n_steps: int = 30,
    learning_rate: float = 1e-5,
    replay_interval: int = 10,      # Replay every this many steps
    replay_batch_size: int = 8,     # Number of examples to replay per interval
) -> None:
    """
    Fine-tune model on a single online example (xi, yi) with optional replay.
    
    Replay uses distillation loss against base model f0.
    
    Args:
        model: The model to be fine-tuned (modified in-place)
        base_model: Frozen copy of f0 for distillation loss
        example_input_ids: Tokenized input of online example xi
        example_labels: Tokenized labels of online example yi
        replay_examples: Pool of upstream examples to replay from
        n_steps: Number of gradient steps (30 for LoRA/Full FT, 100 for head-only)
        learning_rate: Fine-tuning learning rate
        replay_interval: Replay a mini-batch every this many steps
        replay_batch_size: Number of upstream examples to replay per interval
    """
    optimizer = torch.optim.Adam(
        [p for p in model.parameters() if p.requires_grad],
        lr=learning_rate,
    )
    
    model.train()
    base_model.eval()
    
    for step in range(n_steps):
        optimizer.zero_grad()
        
        # Online learning loss: cross-entropy on (xi, yi)
        outputs = model(
            input_ids=example_input_ids,
            labels=example_labels,
        )
        loss = outputs.loss
        
        # Replay step (distillation against f0)
        if (
            replay_examples is not None
            and len(replay_examples) > 0
            and (step + 1) % replay_interval == 0
        ):
            # Sample replay mini-batch
            import random
            batch_indices = random.sample(
                range(len(replay_examples)),
                min(replay_batch_size, len(replay_examples)),
            )
            replay_loss = torch.tensor(0.0, device=model.device)
            
            for idx in batch_indices:
                replay_input_ids, replay_attention_mask = replay_examples[idx]
                
                # Get student logits from updated model
                with model.parameters():
                    student_out = model(
                        input_ids=replay_input_ids,
                        decoder_input_ids=replay_input_ids,
                    )
                
                # Get teacher logits from frozen base model
                with torch.no_grad():
                    teacher_out = base_model(
                        input_ids=replay_input_ids,
                        decoder_input_ids=replay_input_ids,
                    )
                
                replay_loss = replay_loss + distillation_loss(
                    student_out.logits.view(-1, student_out.logits.shape[-1]),
                    teacher_out.logits.view(-1, teacher_out.logits.shape[-1]),
                )
            
            loss = loss + replay_loss / len(batch_indices)
        
        loss.backward()
        optimizer.step()


def sequential_model_refinement(
    base_model,
    test_errors: List[Tuple[Tensor, Tensor, str]],
    # List of (input_ids, labels, expected_output_str) for D^Test_R
    upstream_data: List[Tuple[Tensor, Tensor]],
    # List of (input_ids, labels) for D̂PT
    forecasted_forgotten: Optional[Dict[int, List[int]]] = None,
    # Maps online example index i -> list of upstream example indices predicted to be forgotten
    replay_mode: str = "random",  # "random" | "forecasted" | "gt_forgotten" | "none"
    ground_truth_forgotten: Optional[Dict[int, List[int]]] = None,
    # GT forgetting (oracle): maps i -> list of actually forgotten xj indices
    n_steps: int = 30,
    learning_rate: float = 1e-5,
    replay_interval: int = 10,
    replay_batch_size: int = 8,
    tokenizer=None,
    d_pt_texts: Optional[List[Tuple[str, str]]] = None,
    em_base: Optional[float] = None,
) -> Tuple[float, float]:
    """
    Sequentially fix errors in D^Test_R with optional replay.
    
    Returns:
        (edit_success_rate, em_drop_ratio)
        - edit_success_rate: fraction of D^Test_R correctly predicted at stream end
        - em_drop_ratio: relative EM change on D_PT at stream end
    """
    import random
    
    model = copy.deepcopy(base_model)
    base_model_frozen = copy.deepcopy(base_model)
    for p in base_model_frozen.parameters():
        p.requires_grad = False
    
    n_correct_edits = 0
    
    for i, (input_ids, labels, expected_output) in enumerate(test_errors):
        # Select replay examples
        if replay_mode == "none":
            replay_examples = None
        elif replay_mode == "random":
            indices = random.sample(range(len(upstream_data)), min(replay_batch_size * (n_steps // replay_interval), len(upstream_data)))
            replay_examples = [upstream_data[idx] for idx in indices]
        elif replay_mode == "forecasted" and forecasted_forgotten is not None:
            forgotten_indices = forecasted_forgotten.get(i, [])
            replay_examples = [upstream_data[idx] for idx in forgotten_indices] if forgotten_indices else None
        elif replay_mode == "gt_forgotten" and ground_truth_forgotten is not None:
            forgotten_indices = ground_truth_forgotten.get(i, [])
            replay_examples = [upstream_data[idx] for idx in forgotten_indices] if forgotten_indices else None
        else:
            replay_examples = None
        
        fine_tune_single_example(
            model=model,
            base_model=base_model_frozen,
            example_input_ids=input_ids,
            example_labels=labels,
            replay_examples=replay_examples,
            n_steps=n_steps,
            learning_rate=learning_rate,
            replay_interval=replay_interval,
            replay_batch_size=replay_batch_size,
        )
    
    # Evaluate edit success rate on D^Test_R
    model.eval()
    if tokenizer is not None:
        for i, (input_ids, labels, expected_output) in enumerate(test_errors):
            with torch.no_grad():
                output_ids = model.generate(input_ids=input_ids, max_new_tokens=50)
                predicted = tokenizer.decode(output_ids[0], skip_special_tokens=True)
            if exact_match(predicted, expected_output):
                n_correct_edits += 1
        edit_success_rate = n_correct_edits / len(test_errors)
    else:
        edit_success_rate = -1.0  # Not evaluated
    
    # Evaluate EM Drop Ratio on D_PT
    if d_pt_texts is not None and tokenizer is not None and em_base is not None:
        em_after = compute_em_score(model, d_pt_texts, tokenizer)
        em_drop = compute_em_drop_ratio(em_after, em_base)
    else:
        em_drop = -999.0  # Not evaluated
    
    return edit_success_rate, em_drop
