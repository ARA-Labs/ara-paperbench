"""
Efficient Self-Knowledge Distillation for APT.

Implements Section 4.4:
- Teacher = snapshot of student's APT adapter weights (shared frozen W)
- 4 teacher layers sampled per epoch (one per network quarter, RAIL-KD style)
- Dynamic teacher-student layer mapping: phi(i) = argmin_j MSE(W_layer * H_s^j, H_t^i)
- Loss: L = mu * L_distill + (1 - mu) * L_ft
  - For GLUE: L_distill = L_pred + 0.9 * L_layer
  - For SQuAD/CNN-DM: L_distill = 0.1 * L_pred + 0.9 * L_layer

distillation_type=self_momentum in all training scripts
distill_mapping_strategy=dynamic_block_teacher_dynamic_student
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List, Tuple, Optional, Dict
import random


def sample_teacher_layers(num_layers: int, num_teacher_samples: int = 4) -> List[int]:
    """
    Sample teacher layer indices using RAIL-KD block-wise strategy.
    
    Divides network into num_teacher_samples equal quarters.
    Samples one layer uniformly at random from each quarter.
    
    For a 12-layer network, quarters are: [0-2], [3-5], [6-8], [9-11]
    
    Args:
        num_layers: Total number of transformer layers (e.g., 12 for RoBERTa-base)
        num_teacher_samples: Number of teacher layers to sample (default 4)
    
    Returns:
        List of sampled layer indices (one per quarter)
    """
    quarter_size = num_layers // num_teacher_samples
    teacher_layers = []
    
    for i in range(num_teacher_samples):
        start = i * quarter_size
        end = (i + 1) * quarter_size if i < num_teacher_samples - 1 else num_layers
        sampled_layer = random.randint(start, end - 1)
        teacher_layers.append(sampled_layer)
    
    return teacher_layers


def compute_dynamic_layer_mapping(
    student_hidden_states: List[torch.Tensor],   # H_s^j for j = 0..n_student_layers
    teacher_hidden_states: List[torch.Tensor],   # H_t^i for i in teacher_layers
    layer_transform: nn.Module,                  # W_layer (learnable, init=identity)
    student_ffn_active: List[bool],              # z_FFN^j > 0 (not pruned)
) -> Dict[int, int]:
    """
    Dynamic teacher-to-student layer mapping function phi(·).
    
    phi(i) = argmin_{j: z_FFN^j > 0} MSE(Tr(H_s^j), H_t^i)
    
    where Tr is the tunable LoRA layer transformation (initialized as identity).
    Re-computed every training step.
    
    Args:
        student_hidden_states: Hidden reps from all student FFN layers
        teacher_hidden_states: Hidden reps from sampled teacher layers
        layer_transform: Tr — learnable linear transformation (init identity)
        student_ffn_active: Mask indicating non-pruned student layers
    
    Returns:
        Mapping dict: teacher_layer_idx -> student_layer_idx
    """
    mapping = {}
    active_student_indices = [j for j, active in enumerate(student_ffn_active) if active]
    
    for i, h_t in enumerate(teacher_hidden_states):
        min_mse = float('inf')
        best_student_idx = active_student_indices[0]
        
        for j in active_student_indices:
            h_s = student_hidden_states[j]
            # Apply learnable transformation Tr: W_layer * H_s^j
            h_s_transformed = layer_transform(h_s)
            mse = F.mse_loss(h_s_transformed, h_t).item()
            if mse < min_mse:
                min_mse = mse
                best_student_idx = j
        
        mapping[i] = best_student_idx
    
    return mapping


def compute_layer_distillation_loss(
    student_hidden_states: List[torch.Tensor],
    teacher_hidden_states: List[torch.Tensor],
    layer_mapping: Dict[int, int],
    layer_transform: nn.Module,
) -> torch.Tensor:
    """
    Compute layer-wise distillation loss L_layer (Eq. 7).
    
    L_layer = Σ_{i=1}^{4} MSE(Tr(H_s^{phi(i)}), H_t^i)
    
    Tr is a tunable LoRA layer for layer transformation, init as identity I.
    
    Args:
        student_hidden_states: List of student layer hidden representations
        teacher_hidden_states: List of teacher sampled layer hidden reps
        layer_mapping: phi(i) -> j mapping
        layer_transform: Tr layer transformation
    
    Returns:
        Scalar loss value
    """
    loss = torch.tensor(0.0, device=teacher_hidden_states[0].device)
    
    for i, h_t in enumerate(teacher_hidden_states):
        j = layer_mapping[i]
        h_s = student_hidden_states[j]
        h_s_transformed = layer_transform(h_s)  # Tr(H_s^{phi(i)})
        loss = loss + F.mse_loss(h_s_transformed, h_t)
    
    return loss


def compute_prediction_distillation_loss(
    student_logits: torch.Tensor,   # pruned student logits
    teacher_logits: torch.Tensor,   # teacher logits
) -> torch.Tensor:
    """
    Compute prediction-level distillation loss L_pred.
    
    L_pred = KL(p_s || p_t) = D_KL(softmax(student) || softmax(teacher))
    
    Args:
        student_logits: Student output logits
        teacher_logits: Teacher output logits
    
    Returns:
        Scalar KL divergence loss
    """
    p_s = F.log_softmax(student_logits, dim=-1)
    p_t = F.softmax(teacher_logits, dim=-1)
    return F.kl_div(p_s, p_t, reduction='batchmean')


def compute_apt_distillation_loss(
    student_logits: torch.Tensor,
    teacher_logits: torch.Tensor,
    student_hidden_states: List[torch.Tensor],
    teacher_hidden_states: List[torch.Tensor],
    layer_mapping: Dict[int, int],
    layer_transform: nn.Module,
    task_type: str = 'glue',        # 'glue' or 'squad' or 'cnndm'
    mu: float = 0.5,                 # linear interpolation weight (0 → 1)
    fine_tuning_loss: Optional[torch.Tensor] = None,  # L_ft
) -> torch.Tensor:
    """
    Full APT distillation loss (Eq. 7).
    
    L = mu * L_distill + (1 - mu) * L_ft
    
    For GLUE:   L_distill = L_pred + 0.9 * L_layer
    For SQuAD/CNN-DM: L_distill = 0.1 * L_pred + 0.9 * L_layer
    
    mu increases linearly from 0 to 1 during distillation phase.
    
    Args:
        student_logits, teacher_logits: Output logits
        student_hidden_states, teacher_hidden_states: Intermediate activations
        layer_mapping: Dynamic teacher-student layer mapping
        layer_transform: Learnable Tr transformation (init identity)
        task_type: 'glue', 'squad', or 'cnndm'
        mu: Current interpolation weight (increases 0→1 over distillation phase)
        fine_tuning_loss: L_ft (supervised fine-tuning objective)
    
    Returns:
        Combined training loss
    """
    # Prediction distillation
    L_pred = compute_prediction_distillation_loss(student_logits, teacher_logits)
    
    # Layer distillation
    L_layer = compute_layer_distillation_loss(
        student_hidden_states, teacher_hidden_states, layer_mapping, layer_transform
    )
    
    # Combine based on task type
    if task_type == 'glue':
        # GLUE: L_distill = L_pred + 0.9 * L_layer  (distill_loss_alpha=0.9, ce_alpha=0.1/1.0)
        L_distill = L_pred + 0.9 * L_layer
    else:
        # SQuAD / CNN-DM: L_distill = 0.1 * L_pred + 0.9 * L_layer
        L_distill = 0.1 * L_pred + 0.9 * L_layer
    
    # Total loss: mu interpolates from L_ft to L_distill over training
    if fine_tuning_loss is not None:
        total_loss = mu * L_distill + (1 - mu) * fine_tuning_loss
    else:
        total_loss = L_distill
    
    return total_loss
