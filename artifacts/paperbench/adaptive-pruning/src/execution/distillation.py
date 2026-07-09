"""
Efficient Self-Knowledge Distillation for APT.

Based on: "APT: Adaptive Pruning and Tuning Pretrained Language Models
           for Efficient Training and Inference" (Zhao et al., ICML 2024)
arXiv:2401.12200

Implements:
  - Random teacher layer sampling (4 layers from quarter-slices, per epoch)
  - Teacher-student layer mapping φ(i) = argmin_j MSE(W_layer·Hs^j, Ht^i)
  - Layer distillation loss: L_layer = Σ MSE(Tr(Hs^φ(i)), Ht^i)
  - Prediction distillation loss: L_pred = KL(p_s || p_t)
  - Combined loss: L = μ·L_distill + (1-μ)·L_ft
  - μ linearly scales from 0 to 1 during the distillation phase
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List, Tuple, Optional
import random


def sample_teacher_layers(n_layers: int, n_samples: int = 4) -> List[int]:
    """
    Randomly sample teacher layers from quarter-slices of the network.

    Following RAIL-KD (Haidar et al., 2022): sample n_samples layers,
    one from each equal-depth slice of the network.

    For a 12-layer network: slices = [0-2, 3-5, 6-8, 9-11];
    one random layer is selected from each slice.

    Args:
        n_layers: total number of transformer layers
        n_samples: number of teacher layers to sample (default 4)

    Returns:
        list of n_samples layer indices (one per quarter-slice)
    """
    slice_size = n_layers // n_samples
    teacher_layers = []
    for i in range(n_samples):
        start = i * slice_size
        end = start + slice_size if i < n_samples - 1 else n_layers
        teacher_layers.append(random.randint(start, end - 1))
    return teacher_layers


def compute_layer_mapping(
    student_hidden_states: List[torch.Tensor],  # list of (batch, seq, d) per student layer
    teacher_hidden_states: List[torch.Tensor],  # list of (batch, seq, d) for teacher layers
    W_layer: nn.Linear,                         # learnable transformation Tr (d×d, init=I)
    active_student_layers: List[int],           # indices of non-pruned student layers
) -> List[int]:
    """
    Compute teacher-student layer mapping (re-computed every training step).

    φ(i) = argmin_{j: z_FFN^(j) > 0} MSE(W_layer · Hs^j, Ht^i)

    For each teacher layer i, find the closest non-pruned student layer j.

    Args:
        student_hidden_states: hidden states from all student layers
        teacher_hidden_states: hidden states from selected teacher layers
        W_layer: tunable LoRA transformation (Tr), initialized as identity
        active_student_layers: list of non-pruned student layer indices

    Returns:
        mapping: list of student layer indices, one per teacher layer
    """
    mapping = []
    for ht in teacher_hidden_states:
        best_j = active_student_layers[0]
        best_mse = float('inf')
        for j in active_student_layers:
            hs = student_hidden_states[j]
            transformed = W_layer(hs)  # apply learnable Tr
            mse = F.mse_loss(transformed, ht).item()
            if mse < best_mse:
                best_mse = mse
                best_j = j
        mapping.append(best_j)
    return mapping


def compute_layer_distillation_loss(
    student_hidden_states: List[torch.Tensor],  # list of (batch, seq, d)
    teacher_hidden_states: List[torch.Tensor],  # list of (batch, seq, d)
    mapping: List[int],                          # φ(i) for each teacher layer i
    W_layer: nn.Linear,                          # tunable Tr layer
) -> torch.Tensor:
    """
    Compute layer-wise distillation loss.

    L_layer = Σ_{i=1}^{4} MSE(Tr(Hs^{φ(i)}), Ht^i)

    where Tr is a tunable LoRA transformation layer initialized as identity.

    Args:
        student_hidden_states: hidden states indexed by layer
        teacher_hidden_states: teacher hidden states (4 selected layers)
        mapping: φ(i) — student layer index for each teacher layer i
        W_layer: learnable transformation Tr (initialized as identity matrix)

    Returns:
        L_layer: scalar distillation loss
    """
    total_loss = torch.tensor(0.0, device=teacher_hidden_states[0].device)
    for i, (phi_i, ht) in enumerate(zip(mapping, teacher_hidden_states)):
        hs = student_hidden_states[phi_i]
        transformed = W_layer(hs)
        total_loss = total_loss + F.mse_loss(transformed, ht.detach())
    return total_loss / len(teacher_hidden_states)


def compute_prediction_distillation_loss(
    student_logits: torch.Tensor,   # (batch, vocab_size) or (batch, n_classes)
    teacher_logits: torch.Tensor,   # same shape as student_logits
) -> torch.Tensor:
    """
    Compute prediction-level KL divergence distillation loss.

    L_pred = KL(p_s || p_t) where p_s, p_t are softmax distributions.

    Args:
        student_logits: student model output logits
        teacher_logits: teacher model output logits

    Returns:
        L_pred: scalar KL divergence loss
    """
    p_s = F.log_softmax(student_logits, dim=-1)
    p_t = F.softmax(teacher_logits, dim=-1)
    return F.kl_div(p_s, p_t, reduction='batchmean')


def compute_distillation_loss(
    L_pred: torch.Tensor,
    L_layer: torch.Tensor,
    task_type: str = 'glue',  # 'glue' | 'squad_cnndm'
) -> torch.Tensor:
    """
    Combine prediction and layer distillation losses.

    For GLUE:       L_distill = L_pred + 0.9 * L_layer
    For SQuAD/CNN/DM: L_distill = 0.1 * L_pred + 0.9 * L_layer

    Args:
        L_pred: prediction-level KL divergence
        L_layer: layer-level MSE distillation loss
        task_type: 'glue' or 'squad_cnndm'

    Returns:
        L_distill: combined distillation loss
    """
    if task_type == 'glue':
        return L_pred + 0.9 * L_layer
    elif task_type == 'squad_cnndm':
        return 0.1 * L_pred + 0.9 * L_layer
    else:
        raise ValueError(f"Unknown task_type: {task_type}. Use 'glue' or 'squad_cnndm'.")


def compute_combined_loss(
    L_distill: torch.Tensor,
    L_ft: torch.Tensor,
    mu: float,
) -> torch.Tensor:
    """
    Compute combined APT training loss (Equation 7).

    L = μ · L_distill + (1 - μ) · L_ft

    μ linearly scales from 0 to 1 during the distillation phase:
    - At t=0: L = L_ft (pure task loss, allows initial adaptation)
    - At t=T_distill: L = L_distill (pure distillation)

    Args:
        L_distill: distillation loss (layer + prediction)
        L_ft: supervised fine-tuning loss
        mu: mixing coefficient ∈ [0, 1] (increases linearly during distillation phase)

    Returns:
        total loss scalar
    """
    return mu * L_distill + (1 - mu) * L_ft


def compute_mu(t: int, T_distill: int) -> float:
    """
    Compute linear μ schedule for distillation mixing.

    μ linearly increases from 0 to 1 over T_distill steps.

    Args:
        t: current step within distillation phase (0-indexed)
        T_distill: total distillation phase steps

    Returns:
        mu: float in [0, 1]
    """
    if T_distill == 0:
        return 1.0
    return min(1.0, t / T_distill)
